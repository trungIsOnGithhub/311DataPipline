import urllib
import urllib2
import json

import java.io
from org.apache.commons.io import IOUtils
from java.nio.charset import StandardCharsets
from org.apache.nifi.processor.io import StreamCallback
from org.python.core.util import StringUtil

# print(session)
errorOccurred=False
flowFile = session.get()

BASE_URL = 'https://seeclickfix.com/api/v2/issues?'

class ModJSON(StreamCallback):
  def __init__(self):
        pass
  def process(self, inputStream, outputStream):
    try:
        param = {'place_url':'clark-county','per_page':'100','status':'archived'} # same with query script but has status: archived

        url = BASE_URL + urllib.urlencode(param)

        raw = urllib2.urlopen(url).read()
        response = json.loads(raw)

        outputStream.write(bytearray(json.dumps(response, indent=4).encode('utf-8')))
    except:
        global errorOccurred
        errorOccurred=True
        
        outputStream.write(bytearray(json.dumps(response, indent=4).encode('utf-8')))


if (flowFile != None):
    flowFile = session.write(flowFile, ModJSON())
        if(errorOccurred):
            session.transfer(flowFile, REL_FAILURE)
        else:
            session.transfer(flowFile, REL_SUCCESS)
  
session.commit()