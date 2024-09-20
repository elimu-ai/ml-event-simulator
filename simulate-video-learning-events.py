from os.path import basename
import pandas

language_codes = ['ENG', 'HIN', 'TGL']
print(basename(__file__), f'language_codes: {language_codes}')

android_ids = ['e387e38700000001', 'e387e38700000002', 'e387e38700000003']
print(basename(__file__), f'android_ids: {android_ids}')

# Should be the same version as the most recent release of the Analytics app: 
# https://github.com/elimu-ai/analytics/releases
analytics_version_code = 3001018
print(basename(__file__), f'analytics_version_code: {analytics_version_code}')

def simulateVideoLearningEvent(android_id):
    """Simulate a VideoLearningEvent, e.g. a video being opened."""

    # TODO

    return {}

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
        
        event = simulateVideoLearningEvent(android_id)
        print(basename(__file__), f'event: {event}')

        # Export to CSV
        # TODO
