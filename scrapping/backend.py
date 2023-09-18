from bs4 import BeautifulSoup
import requests

class Scrapable:
    def __init__(self, url):
        self.url = url

    def get(self, url):
        response = requests.get(url)
        return response

    def parse(self, parser):
        pass

    def scrape(self):
        response = self.get(self.url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            results = self.parse(soup, response)
            return results
        return []

  
class LinkedIn(Scrapable):
    def __init__(self, query):
        url = f'https://www.linkedin.com/jobs/search?keywords={query}&location=Egypt&geoId=106155005&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
        super().__init__(url)

    def parse(self, parser):
        results = []
        links = parser.select('.base-card__full-link')[:10]
        titles = parser.select('.base-search-card__title')[:10]
        companies = parser.select('.base-search-card__subtitle')[:10]
        locations = parser.select('.base-search-card__metadata')[:10]
        dates = parser.select('.job-search-card__listdate')[:10]

        for link, title, company, location, date in zip(links, titles, companies, locations, dates):
            link = link.get('href').split('?')[0]
            title = title.getText().strip()
            company = company.find('a', recursive=False).getText().strip()
            location = location.find('span', recursive=False).getText().strip()
            date = date.getText().strip()

            result = requests.get(link, headers={'Accept-Language': 'en-US'})
            soup = BeautifulSoup(result.text, 'html.parser')

            level = job_type = ''    

            if len(soup.select('.description__job-criteria-list')) >= 1:
                info = soup.select('.description__job-criteria-list')[0]
                if len(info.findAll('li', recursive=False)) >= 2:
                    level = info.findAll('li', recursive=False)[0].find('span', recursive=False).getText().strip()
                    job_type = info.findAll('li', recursive=False)[1].find('span', recursive=False).getText().strip()

            results.append({
                'title': title, 'link': link, 'company': company, 
                'location': location, 'date': date, 'job_type': job_type,
                'level': level
            })

        return results


class Wuzzuf(Scrapable):
    def __init__(self, query):
        url = f'https://wuzzuf.net/search/jobs/?q={query}&a=hpb'
        super().__init__(url)

    def parse(self, parser):
        results = []
        heads = parser.select('.css-laomuu')
        metas = parser.select('.css-d7j1kk')
        infos = parser.select('.css-y4udm8')

        for head, meta, info in zip(heads, metas, infos): 
            head = head.find("h2", recursive=False).find('a', recursive=False)
            link = f"https://wuzzuf.net{head.get('href')}"
            title = head.getText()
            company = meta.find('a', recursive=False).getText()[:-2]
            location = meta.find('span', recursive=False).getText()
            date = meta.find('div', recursive=False).getText()
            job_type = info.findAll('div', recursive=False)[0].find('a', recursive=False).find('span', recursive=False).getText()
            level = info.findAll('div', recursive=False)[1].find('a', recursive=False).getText()
            
            results.append({
                'title': title, 'link': link, 'company': company, 
                'location': location, 'date': date, 'job_type': job_type,
                'level': level})

        return results


class Glassdoor(Scrapable):
    def __init__(self, query):
        url = f'https://www.glassdoor.com/Job/egypt-{query}-jobs-SRCH_IL.0,5_IN69_KO6,22.htm'
        super().__init__(url)

    def parse(self, parser):
        results = []
        jobs = parser.select('.e1rrn5ka4')
        dates = parser.select('.css-1vfumx3')

        for job, date in zip(jobs, dates):
            head = job.find('a', recursive=False)
            title = head.find('span', recursive=False).getText().strip()
            link = f"https://www.glassdoor.com/{head.get('href')}"
            
            where = job.findAll('div', recursive=False)

            company = where[0].find('a', recursive=False) \
            .find('span', recursive=False).getText()

            location = where[1].find('span', recursive=False).getText()

            date = date.getText()

            results.append({'title': title, 'link': link, 'company': company,
            'location': location, 'date': date})

        return results
    

class Bayt(Scrapable):
    def __init__(self, query):
        url = f'https://www.linkedin.com/jobs/search?keywords={query}&location=Egypt&geoId=106155005&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0'
        super().__init__(url)

    def parse(self, parser):
        results = []
        links = parser.select('.base-card__full-link')[:10]
        titles = parser.select('.base-search-card__title')[:10]
        companies = parser.select('.base-search-card__subtitle')[:10]
        locations = parser.select('.base-search-card__metadata')[:10]
        dates = parser.select('.job-search-card__listdate')[:10]

        for link, title, company, location, date in zip(links, titles, companies, locations, dates):
            link = link.get('href').split('?')[0]
            title = title.getText().strip()
            company = company.find('a', recursive=False).getText().strip()
            location = location.find('span', recursive=False).getText().strip()
            date = date.getText().strip()


            result = requests.get(link, headers={'Accept-Language': 'en-US'})
            soup = BeautifulSoup(result.text, 'html.parser')


            level = job_type = ''    

            if len(soup.select('.description__job-criteria-list')) >= 1:
                info = soup.select('.description__job-criteria-list')[0]
                if len(info.findAll('li', recursive=False)) >= 2:
                    level = info.findAll('li', recursive=False)[0].find('span', recursive=False).getText().strip()
                    job_type = info.findAll('li', recursive=False)[1].find('span', recursive=False).getText().strip()       

            results.append({
                'title': title, 'link': link, 'company': company, 
                'location': location, 'date': date, 'job_type': job_type,
                'level': level
            })

        return results
    


