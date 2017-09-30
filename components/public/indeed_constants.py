ROOT_API = "http://api.indeed.com/ads"
SEARCH_API = "{}/apisearch".format(ROOT_API)
JOBS_API = "{}/apigetjobs".format(ROOT_API)
VIEW_JOB_URL = "https://vn.indeed.com/viewjob"

BASE_QUERY = "\"dịch thuật\""

SEARCH_PARAMS = {
    'co': 'vn',
    'format': 'json',
    'l': 'ho chi minh',
    'limit': 10,
    'v': 2,
    'publisher': '251554656160522',
    'highlight': 0
}

GET_JOB_PARAM = {
    'publisher': '251554656160522',
    'v': 2,
    'format': 'json'
}

