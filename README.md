# biblio
Tiny repository to hold the script to handle the web of science records

# Instructions

## 1
Do a search on Web of Science (www.webofknowledge.com) by going to the advanced search and using
```
GP="CMS Collaboration" AND AD="Ghent" AND PY="2019" 
```
i.e. we search for a group author (GP) which matches the CMS Collaboration and for an address (AD) which matches Ghent, which
helps to filter out a lot of proceedings from non-Ghent people. The PY is the year of publication which you want to adjust for the previous year you are in now.

Note: the web of science webpage only works from the UGent network, and is not scriptable (unless you can convince the central administration to pay a very expensive licence).
Its lay-out changes all the time and the query for the advanced search has also changed in the past.

## 2
The resulting list can be exported ("Export...") by "Other File Formats", then you need to select the records (but there is a maximum of 500, so you can select 1-500, 501-1000, seperately etc... if needed),
"Full Record" as record content and "plain text" as file format. 
Note I did this export on the search results webpage which takes way less time than going to all records individually.

## 3
I've written a script (see attachment) which breaks down this export file and divides them in separate records + downloads the pdf's for each of these records [possibly there might be a few special cases which have to be checked manually, just add it to the elif statements]

## 4
Zip the directory with wos-records and pdf's, as created by the script, and upload it to a filesharing link, and ask the Biblio people (biblio@ugent.be) to upload it.

(you probably need to use wetransfer or dropbox for the large zipfile)

(+tell them who are the UGent authors, even though this can actually be deduced from the records itself)
