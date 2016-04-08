# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import scraperwiki
import subprocess
import sys
import logging

log = logging.getLogger(__name__)

# import lxml.html

try:
    subprocess.check_call("python download.py", shell=True)
    subprocess.check_call("python read.py", shell=True)
    subprocess.check_call("python processing.py", shell=True)
except subprocess.CalledProcessError, e:
    log.error("%s failed" % e.cmd)
    sys.exit(e.returncode)

# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".

import os


# Inspired by: https://github.com/otherchirps/nsw_gov_docs/blob/master/scraper.py#L4-L7
# morph.io requires this db filename, but scraperwiki doesn't nicely
# expose a way to alter this. So we'll fiddle our environment ourselves
# before our pipeline modules load.
os.environ['SCRAPERWIKI_DATABASE_NAME'] = 'sqlite:///data.sqlite'