from django.http import HttpResponse
from django.shortcuts import render
from db.db_manager import ChunkDB
from db.chunk import ChunkMgr
from pymongo import MongoClient
from datetime import datetime


def parse_date(date_str):
  day, month, year, hour, minute = [int(i) for i in date_str.split('-')]
  return year, month, day, hour, minute

def index(request):
  return HttpResponse("Hello, world. You're at the chunk index.")

def chunk_details(request, sdate):
  db = ChunkDB(MongoClient('localhost', 27017), 'stats')
  sdate = datetime(*parse_date(sdate))
  context = db.load_json_from_id(sdate)
  return render(request, 'chunks/index.html', context)

def chunk_range(request, sdate, edate):
  # how are we fetching current_chunk in the chunk_container?
  db = ChunkDB(MongoClient('localhost', 27017), 'stats')
  sdate = datetime(*parse_date(sdate))
  edate = datetime(*parse_date(edate))
  chunk_mgr = ChunkMgr(xxxxxxxxxxxxx)
  chunk_objs = [chunk_mgr.load_chunk_obj_from_id(c) for c in db.get_chunk_range(sdate, edate)]
  context = chunk_mgr.get_top_occurrences(chunk_objs, 20)
  context.update({'tweet_ids': sum((c.num_tweets() for c in chunk_objs)),
                  'users': sum((c.num_users() for c in chunk_objs))})
  return render(request, 'chunks/index.html', context)


