from django.urls import reverse,resolve
from django.test import TestCase
from django.test.utils import override_settings
from django.conf import settings


class OverrideSettingsTest(TestCase):

    @override_settings(ROOT_URLCONF='movie_task.urls')
    def test_url_register(self):
        path= reverse('reg_user')
        assert resolve(path).view_name =='reg_user'
    

    @override_settings(ROOT_URLCONF='movie_task.urls')
    def test_url_collection(self):
        path= reverse('coll_movie')
        assert resolve(path).view_name =='coll_movie'
