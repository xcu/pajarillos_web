from django.http import HttpResponse
from django.shortcuts import render
from db.db_manager import DBManager
from pymongo import MongoClient
from datetime import datetime
from utils import convert_date


def parse_date(date_str):
  day, month, year, hour, minute = [int(i) for i in date_str.split('-')]
  return year, month, day, hour, minute

def index(request):
  return HttpResponse("Hello, world. You're at the chunk index.")

def chunk_details(request, sdate):
  db = DBManager(MongoClient('localhost', 27017), 'stats', 'time_chunks', index='start_date', flush=False)
  sdate = datetime(*parse_date(sdate))
  context = db.get_chunk(sdate)
  return render(request, 'chunks/index.html', context)

def chunk_range(request, sdate, edate):
  db = DBManager(MongoClient('localhost', 27017), 'stats', 'time_chunks', index='start_date', flush=False)
  sdate = datetime(*parse_date(sdate))
  edate = datetime(*parse_date(edate))
  context = db.get_chunk_range(sdate, edate)
  return render(request, 'chunks/index.html', context)


