#!/usr/bin/python

#import our modules
import json
import urllib2
import ssl

# open our file
with open("emails.txt") as inputfile:
    emails = inputfile.readlines()
                                                                                                                                                            
print"========================================"
print"="
print"=		HAVE I BEEN PWNED"
print"="
print"========================================"                                                                                                                                                                

# for each line in txt file query if its been pwned
for line in emails:
    email = line.strip()
    try:
        response = urllib2.urlopen("https://haveibeenpwned.com/api/v2/breachedaccount/"+email).read()
        account_data = json.loads(response.decode("utf-8"))
	print "\nUser\t\t\t\tStatus\t\t\tWhere"
	print "========\t\t\t========\t\t========"
        for record in account_data:
	    print("{}\t PWNED\t\t\t {}".format(email, record['Name']))
    except urllib2.HTTPError:
        print("{}\t\t seems ok".format(email))	
