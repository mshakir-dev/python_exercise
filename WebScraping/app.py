import requests
import urllib
from urllib import request
from bs4 import BeautifulSoup

# print(dir(requests))
# print(dir(urllib))
# print(dir(request))

resp = request.urlopen("https://www.wikipedia.org")
print(type(resp))
print(resp.code)
print(resp.length)

""" Important Code"""
# python --version
# pip3 --version
# pip3 install (camelcase, bs4, request, pandas, urllib)
name = "Muhammad SHakir"
print(f' Hello, {name}')

# The Process by whihc useful information is extracted from the websites. It becomes very useful with websites where data is updated frequently 

"""
# For Instance:
# Amazon Product
# Ebay
# Bonds Online.
"""