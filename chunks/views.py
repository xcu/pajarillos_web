from django.http import HttpResponse
from django.shortcuts import render
from db.injector import TimeChunkInjector
from pymongo import MongoClient
from datetime import datetime
from utils import convert_date

def index(request):
  return HttpResponse("Hello, world. You're at the poll index.")

def chunk_details(request, day, month, year, hour, minute):
  injector = TimeChunkInjector(MongoClient('localhost', 27017), 'stats', 'time_chunks', index='start_date', flush=False)
  d = datetime(int(year), int(month), int(day), hour=int(hour), minute=int(minute))
  chunk_id = convert_date(d)
  context = dict(zip(('terms', 'user_mentions', 'hashtags', 'num_users', 'num_tweets'), injector.from_db(chunk_id)))
  return render(request, 'chunks/index.html', context)

def chunk_gather(request, day, month, year, hour, minute, gather_amount):
  injector = TimeChunkInjector(MongoClient('localhost', 27017), 'stats', 'time_chunks', index='start_date', flush=False)
  d = datetime(int(year), int(month), int(day), hour=int(hour), minute=int(minute))
  chunk_id = convert_date(d)
  context = dict(zip(('terms', 'user_mentions', 'hashtags', 'num_users', 'num_tweets'), injector.from_db(chunk_id)))
  return render(request, 'chunks/index.html', context)
  
