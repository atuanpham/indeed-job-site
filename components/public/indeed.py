import requests
import html2text
from bs4 import BeautifulSoup
from . import indeed_constants


class Indeed(object):

    def __init__(self):
        pass

    def search(self, page=0, query=None, start=0):

        self.data = indeed_constants.SEARCH_PARAMS
        self.data['q'] = indeed_constants.BASE_QUERY

        start = page * int(self.data['limit'])
        self.data['start'] = start

        if query is not None:
            self.data['q'] = '{} + {}'.format(indeed_constants.BASE_QUERY, query)


        response = requests.get(indeed_constants.SEARCH_API, params=self.data)
        return response.json()

    def get_job(self, jobkey):

        job_data = {}

        self.data = indeed_constants.GET_JOB_PARAM
        self.data['jobkeys'] = jobkey

        response = requests.get(indeed_constants.JOBS_API, params=self.data).json()

        result = response['results'][0]
        job_data['jobtitle'] = result['jobtitle']
        job_data['company'] = result['company']
        job_data['formattedLocationFull'] = result['formattedLocationFull']
        job_data['formattedRelativeTime'] = result['formattedRelativeTime']
        job_data['jobkey'] = result['jobkey']
        job_data['url'] = result['url']

        job_page = requests.get(indeed_constants.VIEW_JOB_URL, params={'jk': jobkey})
        soup = BeautifulSoup(job_page.text, 'html.parser')
        job_summary = soup.find(id='job_summary').contents
        job_summary = list(map(str, job_summary))
        job_summary_html = ''.join(job_summary)

        job_data['content'] = html2text.html2text(job_summary_html)

        return job_data

