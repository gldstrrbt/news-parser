from __future__ import print_function
from urllib.request import urlopen
import sys, os, json
from HTMLParser import HTMLParser
from glob import glob
reload(sys)
sys.setdefaultencoding("utf-8")
sys.path.append("/Users/slessa/usr/local/lib/python2.7/site-packages/bs4/builder")
sys.path.append("/Users/slessa/usr/local/lib/python2.7/site-packages")
import bs4
from bs4 import BeautifulSoup
import urlparse
from urlparse import urlparse
from urlparse import urljoin
import requests
 
 
ifup_url = "http://google.com"
news_urls = ["http://news.ycombinator.com", "http://reddit.com/r/politics", "http://reddit.com/r/technology", "http://reddit.com/r/worldnews", "http://theintercept.com"]
 
 
 
 
rel_links = []
abs_links = []
split_rel = []
split_abs = []
 
storylink = ["a.storylink"]
storylink_rel = []
storylink_abs = []
 
storylink_t_rel = []
storylink_t_abs = []
 
testing = []
for a, b in enumerate(news_urls):
                c = BeautifulSoup(requests.get(b).content, "html5lib")
                testing.append(c)
                for d in c.select("a.storylink"):
                                e = d.get("href")
                                l = d.text
                                print(d)
                                print(l)
 
                # for d in c.select("a"):
                #              e = d.get("href")
                #              l = d.text
                #              print(l)
                                if not e.startswith("http"):
                                                join_rel = urljoin(b, e)
                                                storylink_rel.append(join_rel)
                                                storylink_t_rel.append(l)
                                else:
                                                storylink_abs.append(e)
                                                storylink_t_abs.append(l)
 
# print(rel_links)                                 
# print(abs_links)                               
 
 
# abs_parse_a = []
# abs_parse_b = []
# fucks_given = 0
# for f in abs_links:             
#              abs_parse_a.append(f.split("/"))
 
#              for f in abs_parse_a:
#                              for g in f:
#                                              abs_parse_b.append(g.split("-"))
 
# abs_parse_a = []
 
# for h in abs_parse_b:
#              for i in h:
#                              abs_parse_a.append(i.split("="))
 
# abs_parse_b = []
 
# for j in abs_parse_a:
#              for k in j:
#                              abs_parse_b.append(k.split("&"))
 
# abs_parse_a = []
 
# for j in abs_parse_b:
#              for k in j:
#                              abs_parse_a.append(k.split("?"))
 
# abs_parse_b = []
 
# for j in abs_parse_a:
#              for k in j:
#                              abs_parse_b.append(k.split("."))
 
# abs_parse_a = []
 
# for j in abs_parse_b:
#              for k in j:
#                              print(k)
 
 
with open("test_gen.html", "w") as file:
                file.write("<DOCTYPE><html><head></head><body><ul>")
                for x, z in enumerate(storylink_abs):
                                file.write("<a href='" + z + "' target='_blank'>" + storylink_t_abs[x] + "</a><br><br>")
 
                for w, y in enumerate(storylink_rel):
                                # file.write(y)
                                file.write("<a href='" + y + "' target='_blank'>" + storylink_t_rel[w] + "</a><br><br>")
 
                file.write("</ul></body>")
