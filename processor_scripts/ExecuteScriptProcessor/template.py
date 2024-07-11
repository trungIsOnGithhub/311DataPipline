import urllib
import urllib2
import json
import java.io
from org.apache.nifi.processor.io import StreamCallback

errorOccurred = False
flowFile = session.get()

class ModJSON(StreamCallback):
    def __init__(self):
        pass
    def process(self, inputStream, outputStream):
        # code goes here

if (flowFile is not None):
    flowFile = session.write(flowFile, ModJSON())

    if(errorOccurred):
        # session.transfer(flowFile, REL_FAILURE) # if processor failed
    else:
        # session.transfer(flowFile, REL_SUCCESS) # if success
  
session.commit()