## 日志分析项目

### 背景介绍
在我们的产品上线之后经常会出现一些在一开始设计的时候没想到的问题，这个时候就需要对日志数据进行分析，然后针对性的做改动。

### 数据集介绍
数据集是我从目前的已有的log中摘取的一部分。

路径：`/data/nfsdata/nlp/shannon_bootcamp/03_log_analyze/osprey_response.log`

说明：每一行数据为一条log，为dict嵌套格式。我们需要的信息在log['json']这个dict中。详细的读取方式见代码中的样例。

### 要求
思考如何处理内存不足的情况（python的dict会占用大量内存），尽管这种情况在服务器上处理的时候并不太可能出现。