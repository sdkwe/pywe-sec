============
pywe-wxa-sec
============

Wechat MiniProgram Security Module for Python.

Sandbox
=======

* https://mp.weixin.qq.com/debug/cgi-bin/sandbox?t=sandbox/login

Installation
============

::

    pip install pywe-wxa-sec


Usage
=====

::

    from pywe_wxa_sec.pywxasec import Security, msg_sec_check, img_sec_check, media_check_async, audio_check_async, img_check_async


Method
======

::

    class Security(BaseToken):
        def __init__(self, appid=None, secret=None, token=None, storage=None):
            super(Security, self).__init__(appid=appid, secret=secret, token=token, storage=storage)

    def img_sec_check(self, media_file=None, media_file_path=None, appid=None, secret=None, token=None, storage=None, res_bool_val=False):

    def msg_sec_check(self, content, appid=None, secret=None, token=None, storage=None, res_bool_val=False):

    def media_check_async(self, media_url=None, media_type=None, appid=None, secret=None, token=None, storage=None, res_bool_val=False):

    def audio_check_async(self, audio_url=None, media_url=None, appid=None, secret=None, token=None, storage=None, res_bool_val=False):

    def img_check_async(self, img_url=None, media_url=None, appid=None, secret=None, token=None, storage=None, res_bool_val=False):

