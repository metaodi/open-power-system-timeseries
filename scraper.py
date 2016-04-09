# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

import os
import scraperwiki
import subprocess
import sys
import logging

console = logging.StreamHandler()
console.setLevel(logging.INFO)
# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)

# add the handler to the root logger
log = logging.getLogger('')
log.addHandler(console)


# import lxml.html

scripts = ["download.py", "read.py", "processing.py"]

try:
    for script in scripts:
        log.info("Now running: {}".format(script))
        subprocess.check_call("{python} {script}".format(python=os.path.join(sys.prefix, "bin", "python"), script=script), shell=True)
except subprocess.CalledProcessError as e:
    log.error("%s failed" % e.cmd)
    sys.exit(e.returncode)
