# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import logging

import requests
from django.conf import settings
from django.http import JsonResponse, HttpResponseBadRequest


# This retrieves a Python logging instance (or creates it)
logger = logging.getLogger(__name__)

#
# Places views
#
def get_places(request):
    """
    View to get all the places from the website francesinhas.com (from the REST API)
    :param HttpRequest request: User request object
    :return:
    """

    #
    # 1) Get query parameters
    #
    page = request.GET.get('page', 1)  # Page

    #
    # 2) Query francesinhas.com places API to get places
    #
    url = '{}{}?page={}'.format(settings.FRANCESINHAS_URL, settings.FRANCESINHAS_PLACES_API, page)
    response = requests.get(url)

    #
    # 3) Response
    #

    # 3.1) Handle success request
    if response.status_code == 200:
        logger.debug('Success response!')
        return JsonResponse(json.loads(response.content))

    # 3.2) Handle bad request
    return HttpResponseBadRequest('Invalid Request to Francesinhas.com')
