# x-officers
It's just a simple Python3 based script which will crawl the list of urls from a given file and then it will fetch all the JavaScript files available on the page and then will find your custom given keyword inside the JavaScript files.

#Options
The script takes three command-line arguments:

-f or --file: Required argument, the file containing URLs to check.
-k or --keyword: Required argument, the keyword to search for in JavaScript files.
-t or --timeout: Optional argument, the request timeout in seconds. The default value is 5 seconds.

#Examples
./x-officers.py -k dev -t 10 urls.txt

Alternatively, you can pipe URLs into the script like this:

cat url.txt | ./x-officers.py -k dev -t 10

You can also provide a single URL as an argument:

./x-officers.py -k my_keyword -t 10 https://example.com

#Thanks to Team SafeCottage.org
