from datetime import datetime
import os
from os.path import basename
import pandas
import random
import requests

language_codes = ['ENG', 'HIN', 'TGL', 'THA', 'VIE']
print(basename(__file__), f'language_codes: {language_codes}')

android_ids = ['e387e38700000001', 'e387e38700000002', 'e387e38700000003']
print(basename(__file__), f'android_ids: {android_ids}')

# Should match the package name (`applicationId`) of the Application where 
# the event originated (e.g. `ai.elimu.vitabu`)
package_name = 'ai.elimu.filamu'
print(basename(__file__), f'package_name: {package_name}')

# Should be the same version as the most recent release of the Analytics app: 
# https://github.com/elimu-ai/analytics/releases
analytics_version_code = 3001018
print(basename(__file__), f'analytics_version_code: {analytics_version_code}')

date_iso_8601 = datetime.today().strftime('%Y-%m-%d')
print(basename(__file__), f'date_iso_8601: {date_iso_8601}')

timestamp_ms = int(datetime.now().timestamp() * 1_000)
print(basename(__file__), f'timestamp_ms: {timestamp_ms}')

def simulate_video_learning_event(android_id, videos_df: pandas.DataFrame, video_learning_events):
    print(basename(__file__), 'simulate_video_learning_event')
    """
    Simulate a VideoLearningEvent, e.g. a video being opened.
    
    Should match the CSV format in https://github.com/elimu-ai/analytics/blob/main/app/src/main/java/ai/elimu/analytics/task/ExportEventsToCsvWorker.java
    """

    # Increment database ID
    # TODO
    id = 0

    # Increase timestamp to simulate passage of time between events for different 
    # videos. Increase by a random number between 15 seconds and 120 seconds.
    global timestamp_ms
    timestamp_ms += random.randrange(1_000 * 15, 1_000 * 120)

    # Locate a random video in the DataFrame
    number_of_videos = len(videos_df.index)
    random_video_index = random.randrange(0, number_of_videos)
    random_video = videos_df.loc[random_video_index]

    # https://github.com/elimu-ai/model/blob/main/src/main/java/ai/elimu/model/v2/enums/analytics/LearningEventType.java
    learning_event_types = ['VIDEO_OPENED', 'VIDEO_CLOSED_BEFORE_COMPLETION', 'VIDEO_COMPLETED']

    video_learning_events.append({
        'id': id,
        'timestamp': timestamp_ms,
        'android_id': android_id,
        'package_name': package_name,
        'video_id': random_video.id,
        'video_title': random_video.title,
        'learning_event_type': learning_event_types[0]
    })

    # A `VIDEO_OPENED_EVENT` should always be followed by a `VIDEO_CLOSED_BEFORE_COMPLETED` 
    # event or a `VIDEO_COMPLETED` event.
    second_learning_event_type = random.choice(learning_event_types[1:])

    # Increase timestamp to simulate passage of time between the `VIDEO_OPENED` event and the 
    # second event. Increase by a random number between 2 seconds and 60 seconds.
    timestamp_ms += random.randrange(1_000 * 2, 1_000 * 60)

    video_learning_events.append({
        'id': id,
        'timestamp': timestamp_ms,
        'android_id': android_id,
        'package_name': package_name,
        'video_id': random_video.id,
        'video_title': random_video.title,
        'learning_event_type': second_learning_event_type,
        'additional_data': {'video_playback_position_ms': random.randrange(1000, 60000)}
    })

for language_code in language_codes:
    print()
    print(basename(__file__), f'language_code: {language_code}')

    videos_csv_url = f'https://raw.githubusercontent.com/elimu-ai/webapp-lfs/refs/heads/main/lang-{language_code}/videos.csv'
    print(basename(__file__), f'videos_csv_url: {videos_csv_url}')
    videos_df = pandas.read_csv(videos_csv_url)
    print(basename(__file__), f'videos_df: \n{videos_df}')
    number_of_videos = len(videos_df.index)
    print(basename(__file__), f'number_of_videos: {number_of_videos}')
    if (number_of_videos == 0):
        print(basename(__file__), 'Zero videos. Skipping event simulation.')
        continue

    base_url = f'http://{language_code.lower()}.elimu.ai'
    # base_url = 'http://localhost:8080/webapp'
    print(basename(__file__), f'base_url: {base_url}')

    rest_url = f'{base_url}/rest/v2'
    print(basename(__file__), f'rest_url: {rest_url}')

    for android_id in android_ids:
        print()
        print(basename(__file__), f'android_id: {android_id}')

        # Make it 30% likely that the student will skip learning
        random_learning_probability = random.randrange(0, 100)
        print(basename(__file__), f'random_learning_probability: {random_learning_probability}%')
        if (random_learning_probability < 30):
            continue
        
        video_learning_events = []
        random_number_of_events = random.randrange(0, 20)
        print(basename(__file__), f'random_number_of_events: {random_number_of_events}')
        if (random_number_of_events == 0):
            continue
        for i in range(random_number_of_events):
            simulate_video_learning_event(android_id, videos_df, video_learning_events)
        
        video_learning_events_df = pandas.DataFrame(video_learning_events)
        # print(basename(__file__), f'video_learning_events_df: \n{video_learning_events_df}')

        # Export to CSV
        language_dir = f'lang-{language_code}'
        android_id_dir = os.path.join(language_dir, f'android-id-{android_id}')
        version_code_dir = os.path.join(android_id_dir, f'version-code-{analytics_version_code}')
        video_learning_events_dir = os.path.join(version_code_dir, 'video-learning-events')
        if not os.path.exists(video_learning_events_dir):
            os.makedirs(video_learning_events_dir)
        csv_path = os.path.join(video_learning_events_dir, f'{android_id}_{analytics_version_code}_video-learning-events_{date_iso_8601}.csv')
        print(basename(__file__), f'csv_path: {csv_path}')
        video_learning_events_df.to_csv(csv_path, index=False)

        # Upload to webapp's REST API
        endpoint_url = f'{rest_url}/analytics/video-learning-events/csv'
        print(basename(__file__), f'endpoint_url: {endpoint_url}')
        with open(csv_path, 'r') as file:
            files = {'file': file}
            response = requests.post(endpoint_url, files=files)
            print(basename(__file__), f'response: {response}')
