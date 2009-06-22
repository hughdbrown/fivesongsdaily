import datetime
from time import strftime

from django.contrib.syndication.feeds import Feed

from fivesongsdaily.playlist.models import Playlist

class LatestPlaylists(Feed):
    title = "Five Songs Daily"
    link = "http://www.fivesongsdaily.com/"
    description = "Latest playlists on Five Songs Daily"

    def items(self):
        todaysdate = datetime.datetime.now().strftime("%Y-%m-%d")
        return Playlist.objects.filter(active=True).filter(play_date__lte=todaysdate).order_by('-play_date')[:5]

