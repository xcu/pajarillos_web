from django.http import HttpResponse
from django.shortcuts import render
from db.db_manager import DBManager
from db.chunk import ChunkMgr
from pymongo import MongoClient
from datetime import datetime


def parse_date(date_str):
  day, month, year, hour, minute = [int(i) for i in date_str.split('-')]
  return year, month, day, hour, minute

def index(request):
  return HttpResponse("Hello, world. You're at the chunk index.")

def chunk_details(request, sdate):
  db = DBManager(MongoClient('localhost', 27017), 'stats', 'chunk_containers', index='start_date', flush=False)
  sdate = datetime(*parse_date(sdate))
  context = db.get_chunk(sdate)
  return render(request, 'chunks/index.html', context)

def chunk_range(request, sdate, edate):
  # how are we fetching current_chunk in the chunk_container?
  db = DBManager(MongoClient('localhost', 27017), 'stats', 'chunk_containers', index='start_date', flush=False)
  sdate = datetime(*parse_date(sdate))
  edate = datetime(*parse_date(edate))
  chunk_objs = [db.load_chunk_from_id(c) for c in db.get_chunk_range(sdate, edate)]
  context = ChunkMgr().get_top_occurrences(chunk_objs, 20)
  context.update({'tweet_ids': sum((c.num_tweets() for c in chunk_objs)),
                  'users': sum((c.num_users() for c in chunk_objs))})
  return render(request, 'chunks/index.html', context)


