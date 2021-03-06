## 中文文本分类项目

### 背景介绍
股市新闻包含财务数据、经营公告、行业动向、国家政策等大量文本信息，包含了一定的情感倾向，影响股民对公司股票未来走势的预期，进一步造成公司的股价波动。如果能够挖掘出这些新闻中蕴含的情感信息，则可以对股票价格进行预测，对于指导投资有很大的作用。

为及时了解广大用户的情感偏向并分析舆情，面向网络新闻领域的情感分析具有重要意义。

### 数据集介绍
数据集来源是中债资信提供的新闻标注数据，即对每篇新闻打一个分数，越大越正面，越小越负面；如-1是负面新闻，1是正面新闻，0是中性新闻

路径：`/data/nfsdata/nlp/shannon_bootcamp/04_text_classification`

说明：每一行是一个json字符串，可以用json.loads转化为dict，里面包含content, title和label，label<0是负面, label>=0是非负面；content和title是分词+POS后的List[str]，每个str形如word/pos，词语和词性用"/"隔开

### 要求

1. 使用SVM实现情感分类，特征任选，推荐使用的特征有：字级别的unigram, bigram，词级别的unigram，词性标签等等。
2. 使用ShannonNLP框架实现情感分类，模型任选，推荐使用的模型有BiLSTM，CNN和BERT。
3. 情感分类的准确率达到75%以上 。
4. 继承TextClassifier，重写classifier方法，实现情感极性的预测。