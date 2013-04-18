import requests
import json

URL = 'https://coveralls.io/api/v1/jobs'


def post_report(coverage):
    """Post coverage report to coveralls.io
    """
    response = requests.post(URL, files={'json_file': json.dumps(coverage)})
    try:
        result = response.json()
    except ValueError:
        result = {'error': 'Failure to submit data. '
            'Response [%(status)s]: %(text)s' % {
            'status': response.status_code,
                'text': response.text}}
    print result