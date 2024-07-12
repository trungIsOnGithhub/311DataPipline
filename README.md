### Build a 311* Data Pipeline with Visualization

> *311 mean next up after 911 in the US. It is like 911, but for non-emergencies. It is about reported issues within a city: potholes in the road, trees down, trash problems, homeless that might be in need of assistance... This project used a [SeeClickFix](https://crm.seeclickfix.com/) as data source, also a 311 data site.

> Build with Apache Nifi 1.27.x - Python 3.10.x - Elasticsearch - Kibana

![Material Book Cover](/assets/book-cover.png)
> This repo is implementation(with modification) for Chapter exercise in Data Engineering with Python

1. To start the data pipeline, use the GenerateFlowFile processor as a trick, since other processor cannot be the first 
processor in a data pipeline. The processor should be OK with default setting

![image](/assets/set-up-cron-for-file-gen-1st-trigger.png)

+ Dont forget to add the Scheduling with ![CronMakerExpressionGenerate](http://www.cronmaker.com/)

![image](/assets/set-up-cron-for-file-gen-1st-trigger.png)

2. 

3. Add query processor for Archived Data from Source with Script

+ Choose the python Script option and add script to query data
![image](/assets/split-json-config-expression.png)

4. Add ```SplitJson``` processor for extract data fields

![image](/assets/split-json-config-expression.png)
+ In this example, I want to extract the issue in data payload

+ We can use this [site](https://jsonpath.com/) to write and check our json path

+ Image of the full flow of data pipelines:
![image](/assets/full-pipline-flow.png)

#### Common Errors

- Elastic/Kibana service need enrollment key for the first time.

![image](/assets/common-error-cannot-get-ekey-elastic.png)

**Solve:** The default username of elastic(and kibana) is ```elastic```. Find the generated password in the command running of script to start-up Elasticache
