### Build a 311* Data Pipeline with Visualization

> *311 mean next up after 911 in the US. It is like 911, but for non-emergencies. It is about reported issues within a city: potholes in the road, trees down, trash problems, homeless that might be in need of assistance... This project used a [SeeClickFix](https://crm.seeclickfix.com/) as data source, also a 311 data site.

> Build with Apache Nifi 1.27.x - Python 3.10.x - Elasticsearch - Kibana

[Material Book Cover](/assets/set-up-cron-for-file-gen-1st-trigger.png)
> This repo is implementation(with modification) for Chapter exercise in Data Engineering with Python

1. To start the data pipeline, use the GenerateFlowFile processor as a trick, since other processor cannot be the first 
processor in a data pipeline. The processor should be OK with default setting

[image](/assets/set-up-cron-for-file-gen-1st-trigger.png)

+ Dont forget to add the Scheduling with [CronMakerExpressionGenerate](http://www.cronmaker.com/)

2. 


#### Common Errors

