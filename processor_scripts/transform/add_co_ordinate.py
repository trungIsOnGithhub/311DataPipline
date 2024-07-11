  def process(self, inputStream, outputStream):
    try:
        text = IOUtils.toString(inputStream, StandardCharsets.UTF_8)
        reply=json.loads(text)
        
        reply['coords']=str(reply['lat'])+","+str(reply['lng'])
        d=reply['created_at'].split("T")
        reply['opendate']=d[0]
        outputStream.write(bytearray(json.dumps(reply, indent=4).encode('utf-8')))
    except:
        global errorOccurred
        errorOccurred=True
        
        outputStream.write(bytearray(json.dumps(reply, indent=4).encode('utf-8')))