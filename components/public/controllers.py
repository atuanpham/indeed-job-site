from flask import (
    flash, redirect, url_for, render_template, Blueprint, request
)
from .indeed import Indeed

public_blueprint = Blueprint(
    'public', __name__,
    template_folder='templates'
)

indeed = Indeed()


@public_blueprint.route('/')
def home():
    request_page = request.args.get('page') if request.args.get('page') is not None else 0
    response = indeed.search(page=int(request_page))

    total = int(response['totalResults'])
    last_job_of_page = int(response['end'])
    current_page = int(response['pageNumber'])
    prev_page = current_page - 1
    next_page = current_page + 1

    if last_job_of_page >= total:
        next_page = -1

    jobs = response['results']

    return render_template('index.html', prev_page=prev_page, next_page=next_page, jobs=jobs)


@public_blueprint.route('/search')
def search():
    request_query = request.args.get('query') if request.args.get('query') is not None else "" 
    request_page = request.args.get('page') if request.args.get('page') is not None else 0
    response = indeed.search(page=int(request_page), query=request_query)

    total = int(response['totalResults'])
    last_job_of_page = int(response['end'])
    current_page = int(response['pageNumber'])
    prev_page = current_page - 1
    next_page = current_page + 1

    if last_job_of_page >= total:
        next_page = -1

    jobs = response['results']

    return render_template('search.html', prev_page=prev_page, next_page=next_page, jobs=jobs, search_query=request_query)


@public_blueprint.route('/<jobkey>')
def job_detail(jobkey):
    job_data = indeed.get_job(jobkey)
    return render_template('job_detail.html', job=job_data)

