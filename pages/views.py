from django.views.generic import TemplateView

from bs4 import BeautifulSoup
import requests


URL = "https://wttr.in"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/10"
        "4.0.0.0 Safari/537.36"
    )
}


class HomePageView(TemplateView):
    template_name = "pages/home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"

    def get(self, request, *args, **kwargs):
        context = self.get_content_data(**kwargs)
        resp = requests.get(URL, headers=HEADERS)
        if resp.status_code == 200:
            soup = BeautifulSoup(resp.content, "html.parser")
            weather_pre = soup.find("pre")
        else:
            weather_pre = "%s" % resp.text
        context["weather"] = str(weather_pre)
        return self.render_to_response(context)


# Create your views here.
