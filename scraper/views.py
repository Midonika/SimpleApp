from django.shortcuts import render

from .forms import UrlForm
from .helpers import Helper


def get_url_address(request):

    if request.method == 'GET':
        form = UrlForm()
        data = {'form': form}
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            parsed_html, meta = Helper.get_html_and_meta_tags(form['url'].value())
            keywords = Helper.get_keywords(meta)

            data = {'form': form, 'keywords': Helper.count_keywords_in_html(parsed_html, keywords)}

    return render(request, 'scraper/get_url.html', data)
