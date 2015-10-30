# -*- coding: utf-8 -*-

import requests
from django.conf import settings

# Get BrandCaptcha Public Key
BRANDCAPTCHA_PUBLIC_KEY = getattr(settings, "BRANDCAPTCHA_PUBLIC_KEY", None)

# Get BrandCaptcha Private Key
BRANDCAPTCHA_PRIVATE_KEY = getattr(settings, "BRANDCAPTCHA_PRIVATE_KEY", None)

# Get BrandCaptcha API Host
BRANDCAPTCHA_API_HOST = getattr(
    settings,
    "BRANDCAPTCHA_CHALLENGE_PATH",
    "api.pontamedia.net"
)

# Get BrandCaptcha "Verify Path"
BRANDCAPTCHA_VERIFY_PATH = getattr(
    settings,
    "BRANDCAPTCHA_VERIFY_PATH",
    "/verify.php"
)

# Get BrandCaptcha "Challenge Path"
BRANDCAPTCHA_CHALLENGE_PATH = getattr(
    settings,
    "BRANDCAPTCHA_CHALLENGE_PATH",
    "/challenge.php"
)

# Get BrandCaptcha SSL
BRANDCAPTCHA_SSL = getattr(settings, "BRANDCAPTCHA_SSL", True)


class BrandcaptchaValidator():
    def get_url(self):
        return "{}{}{}?k={}".format(
            self._get_protocol(),
            BRANDCAPTCHA_API_HOST,
            BRANDCAPTCHA_CHALLENGE_PATH,
            BRANDCAPTCHA_PUBLIC_KEY,
        )

    def verify(self, response, remoteip, challenge):
        url = "{}{}{}".format(
            self._get_protocol(),
            BRANDCAPTCHA_API_HOST,
            BRANDCAPTCHA_VERIFY_PATH,
        )

        params = dict(
            privatekey=BRANDCAPTCHA_PRIVATE_KEY,
            response=response,
            remoteip=remoteip,
            challenge=challenge,
        )

        response = requests.post(url=url, params=params)
        if 'true' in response.text:
            return True
        return False

    def _get_protocol(ssl=True):
        if BRANDCAPTCHA_SSL:
            return "https://"
        return "http://"
