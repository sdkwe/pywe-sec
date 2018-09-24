# -*- coding: utf-8 -*-

from pywe_wxa_sec.pywxasec import Security, img_sec_check, msg_sec_check

from local_wecfg_example import CONTENT, IMAGE_PATH, WECHAT


class TestSecCommands(object):
    def test_img_sec_check(self):
        appid = WECHAT.get('WXA', {}).get('appID')
        appsecret = WECHAT.get('WXA', {}).get('appsecret')
        media_file = open(IMAGE_PATH, 'rb')
        security = Security(appid=appid, secret=appsecret)
        data = security.img_sec_check(media_file=media_file)
        assert isinstance(data, dict)
        assert data.get('errcode') == 0

        data = img_sec_check(media_file=None, media_file_path=IMAGE_PATH, appid=appid, secret=appsecret)
        assert isinstance(data, dict)
        assert data.get('errcode') == 0

    def test_msg_sec_check(self):
        appid = WECHAT.get('WXA', {}).get('appID')
        appsecret = WECHAT.get('WXA', {}).get('appsecret')
        # media_file = open(IMAGE_PATH, 'rb')
        security = Security(appid=appid, secret=appsecret)
        data = security.msg_sec_check(CONTENT)
        assert isinstance(data, dict)
        assert data.get('errcode') == 87014

        data = msg_sec_check(CONTENT, appid=appid, secret=appsecret)
        assert isinstance(data, dict)
        assert data.get('errcode') == 87014
