from datetime import datetime
import os
from os.path import basename
import pandas
import random

language_codes = ['ENG', 'HIN', 'TGL']
print(basename(__file__), f'language_codes: {language_codes}')

android_ids = ['e387e38700000001', 'e387e38700000002', 'e387e38700000003']
print(basename(__file__), f'android_ids: {android_ids}')

# Should be the same version as the most recent release of the Analytics app: 
# https://github.com/elimu-ai/analytics/releases
analytics_version_code = 3001018
print(basename(__file__), f'analytics_version_code: {analytics_version_code}')

date = datetime.today().strftime('%Y-%m-%d')
print(basename(__file__), f'date: {date}')

def simulateVideoLearningEvent(android_id):
    """
    Simulate a VideoLearningEvent, e.g. a video being opened.
    
    Should match the CSV format in https://github.com/elimu-ai/analytics/blob/main/app/src/main/java/ai/elimu/analytics/task/ExportEventsToCsvWorker.java
    """

    id = 0
    time = 0

    return {
        'id': id,
        'time': time
    }

for language_code in language_codes:
    print(basename(__file__))
    print(basename(__file__), f'language_code: {language_code}')

    videos_csv_url = f'https://raw.githubusercontent.com/elimu-ai/webapp/main/src/main/resources/db/content_PROD/{language_code.lower()}/videos.csv'
    print(basename(__file__), f'videos_csv_url: {videos_csv_url}')
    videos_df = pandas.read_csv(videos_csv_url)
    print(basename(__file__), f'videos_df: \n{videos_df}')

    base_url = f'http://{language_code.lower()}.elimu.ai'
    print(basename(__file__), f'base_url: {base_url}')

    rest_url = f'{base_url}/rest/v2'
    print(basename(__file__), f'rest_url: {rest_url}')

    for android_id in android_ids:
        print(basename(__file__))
        print(basename(__file__), f'android_id: {android_id}')
        
        video_learning_events = []
        random_number_of_events = random.randrange(0, 20)
        print(basename(__file__), f'random_number_of_events: {random_number_of_events}')
        for i in range(random_number_of_events):
            print(basename(__file__))
            event = simulateVideoLearningEvent(android_id)
            print(basename(__file__), f'event: {event}')
            video_learning_events.append(event)
        
        video_learning_events_df = pandas.DataFrame(video_learning_events)
        print(basename(__file__), f'video_learning_events_df: \n{video_learning_events_df}')

        # Export to CSV
        language_dir = f'lang-{language_code}'
        android_id_dir = os.path.join(language_dir, f'android-id-{android_id}')
        version_code_dir = os.path.join(android_id_dir, f'version-code-{analytics_version_code}')
        storybook_learning_events_dir = os.path.join(version_code_dir, f'storybook-learning-events')
        if not os.path.exists(storybook_learning_events_dir):
            os.makedirs(storybook_learning_events_dir)
        csv_path = os.path.join(storybook_learning_events_dir, f'{android_id}_{analytics_version_code}_storybook-learning-events_{date}.csv')
        print(basename(__file__), f'csv_path: \n{csv_path}')
        video_learning_events_df.to_csv(csv_path, index=False)
