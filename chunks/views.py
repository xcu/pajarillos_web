from django.http import HttpResponse
from django.shortcuts import render
from db.injector import TimeChunkInjector
from db.db_manager import DBManager
from pymongo import MongoClient
from datetime import datetime
from utils import convert_date

def index(request):
  return HttpResponse("Hello, world. You're at the chunk index.")

def chunk_details(request, sdate, edate=''):
  def parse_date(date_str):
    day, month, year, hour, minute = [int(i) for i in date_str.split('-')]
    return year, month, day, hour, minute
  injector = TimeChunkInjector(DBManager(MongoClient('localhost', 27017), 'stats', 'time_chunks', index='start_date', flush=False))
  sdate = datetime(*parse_date(sdate))
  if edate:
    edate = datetime(*parse_date(edate))
  context = dict(zip(('terms', 'user_mentions', 'hashtags', 'num_users', 'num_tweets'), get_all_chunks(injector, sdate, edate)))
  context['num_users'] = len(context['num_users'])
  return render(request, 'chunks/index.html', context)

def get_all_chunks(injector, sdate, edate):
  if not edate:
    # just one, no need to gather
    return injector.from_db(convert_date(sdate))
  return injector.reduce_range(convert_date(sdate), convert_date(edate))
   

