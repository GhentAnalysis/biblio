# biblio
Tiny repository to hold the script to handle the web of science records

# Instructions

1) Do a search on Web of Science (www.webofknowledge.com) by using the fields "Group Author: CMS Collaboration" AND "Address: Ghent" (the second helps to filter out a lot of proceedings from non-Ghent people), maybe also add the year (given that everything before 2019 is in now)

2) The resulting list can be exported by "Save To Other Formats", then you need to select "All records on page" (but there is a maximum of 500, so you can also select 1-500, 501-1000, etc...), "Full Record" as record content and "plain text" as file format. Note I did this export on the search results webpage (hence "all records on page") which takes way less time than going to all records individually.

3) I've written a script (see attachment) which breaks down this export file and divides them in separate records + downloads the pdf's for each of these records [possibly there might be a few special cases which have to be checked manually, just add it to the elif statements]

4) Zip the directory with wos-records and pdf's, as created by the script, and upload it to a filesharing link, and ask the Biblio people to upload it (+tell them who are the UGent authors, even though this can actually be deduced from the records itself)


