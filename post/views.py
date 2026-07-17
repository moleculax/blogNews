# post/views.py

from urllib import request

from django.views import View
from django.http import HttpResponse
from rest_framework.views import APIView
import datetime
from drf_spectacular.utils import extend_schema

from django.db import connection

from django.shortcuts import render, get_object_or_404
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import Http404


