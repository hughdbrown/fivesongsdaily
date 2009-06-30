#!/usr/bin/env python
# http://docs.djangoproject.com/en/dev/topics/testing/

from sys import stderr
import unittest
from django.test.client import Client

class NavigateTestCase(unittest.TestCase):
    good_return_codes = [200, 302]
    bad_return_codes = [404]
    redirect_codes = [301, 302]
    get_bad_urls = [  ]
    get_redirecting_urls = [ '/playlist/preview/1/', '/preview/1',
                            '/playlist/1/', '/playlist/id/1/', '/id/1/', '/1/', ]
    get_good_urls = ['/admin/', '/',
                    '/pages/about/', '/pages/', '/contact/',
                    '/profile/fivesongs/', '/profile/edit/fivesongs/', '/profile/edit/foobar/', '/profile/band/foobar/',
                    '/playlist/all/', '/all/', ]
    post_urls = []
    
    #url(r'^song/add/$',		            views.user_song_upload,	    name='playlist_song_upload'),
    #url(r'^upload/(?P<message>.+)/$',	views.user_playlist,	    name='playlist_save'),
    #url(r'^upload/$',			        views.user_playlist,	{'message':None},    name='playlist_save'),
    
    def setUp(self):
        self.credentials = {'username': 'fivesongs', 'password': '604bear2'}
        self.client = Client()

    def testURLs(self):
        print  >>stderr, "Logging in"
        response = self.client.post('/accounts/login/', self.credentials)
        self.failUnlessEqual(response.status_code in NavigateTestCase.good_return_codes, True)

        for url in NavigateTestCase.get_good_urls:
            response = self.client.get(url)
            print >>stderr, "Test(%d): %s" % (response.status_code, url)
            self.failUnlessEqual(response.status_code in NavigateTestCase.good_return_codes, True)

        print  >>stderr, "Logging out"
        response = self.client.post('/accounts/logout/', {})
        self.failUnlessEqual(response.status_code in NavigateTestCase.good_return_codes, True)

    def testRedirectingURLs(self):
        print  >>stderr, "Logging in"
        response = self.client.post('/accounts/login/', self.credentials)
        self.failUnlessEqual(response.status_code in NavigateTestCase.good_return_codes, True)

        for url in NavigateTestCase.get_redirecting_urls:
            response = self.client.get(url)
            print  >>stderr, "Test(%d): %s" % (response.status_code, url)
            self.failUnlessEqual(response.status_code in NavigateTestCase.redirect_codes, True)

        print  >>stderr, "Logging out"
        response = self.client.post('/accounts/logout/', {})
        self.failUnlessEqual(response.status_code in NavigateTestCase.good_return_codes, True)

    def testBadURLs(self):
        print  >>stderr, "Logging in"
        response = self.client.post('/accounts/login/', self.credentials)
        self.failUnlessEqual(response.status_code in NavigateTestCase.good_return_codes, True)

        for url in NavigateTestCase.get_bad_urls:
            try:
                print  >>stderr, "Expecting bad: ", url
                response = self.client.get(url)
                print  >>stderr, "Test(%d): %s" % (response.status_code, url)
                self.failUnlessEqual(response.status_code in NavigateTestCase.bad_return_codes, True)
            except Exception, err:
                print  >>stderr, err

        print  >>stderr, "Logging out"
        response = self.client.post('/accounts/logout/', {})
        self.failUnlessEqual(response.status_code in NavigateTestCase.good_return_codes, True)

    def testPostURLs(self):
        print  >>stderr, "Logging in"
        response = self.client.post('/accounts/login/', self.credentials)
        self.failUnlessEqual(response.status_code in NavigateTestCase.good_return_codes, True)

        for url in NavigateTestCase.post_urls:
            response = self.client.post(url)
            print  >>stderr, "Test(%d): %s" % (response.status_code, url)
            self.failUnlessEqual(response.status_code in NavigateTestCase.good_return_codes, True)

        print  >>stderr, "Logging out"
        response = self.client.post('/accounts/logout/', {})
        self.failUnlessEqual(response.status_code in NavigateTestCase.good_return_codes, True)


    #(r'^comments/', include('django.contrib.comments.urls')),
    #(r'^comments/post/', include('django.contrib.comments.urls')),
    #(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'accounts/login/login.html'}),
    #(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    #
    #(r'^password_reset/$', 'django.contrib.auth.views.password_reset'),
    #(r'^password_reset/done/$', 'django.contrib.auth.views.password_reset_done'),
    #(r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm'),
    #(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete'),
    #
    #(r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
    #(r'^profile/', include('fivesongsdaily.profiles.urls')),
    #(r'^playlist/', include('fivesongsdaily.playlist.urls')),
    #(r'^messages/', include('fivesongsdaily.message.urls')),
    #(r'^pages/', include('fivesongsdaily.pages.urls')),
    #(r'^contact/', include('fivesongsdaily.contact.urls')),
    #(r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
