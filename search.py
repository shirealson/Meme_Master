#coding:utf-8
#!/usr/bin/python
import jieba
import jieba.analyse
import sys
import  os
from collections import Counter
import mysql.connector
from generate  import generateWithTemplate
import sys 
sentenceI = sys.argv[1] #即为获取到的PHP传入python的入口参数
conn = mysql.connector.connect(user='root', password='', database='test', use_unicode=True)
cursor=conn.cursor()
def  search(sentence):
    cursor.execute('SELECT  path  FROM  image   WHERE   sentence="%s"   LIMIT 0,1;'%sentence)
    path = cursor.fetchall()
    if len(path):
        return  (path[0][0])
    sentence_list = jieba.cut(sentence,cut_all=False)
    #print (sentence_list)
    categorylist=[]
    for  word  in  sentence_list:
        #print (word)
        cursor.execute('SELECT  category  FROM  category   WHERE   label_name="%s" ORDER BY  label_num  desc  LIMIT 0,1;'%word)
        result = cursor.fetchall()
        if  len(result):
            categorylist.append(result[0][0])
    #print (categorylist)
    category=Counter(categorylist).most_common(10)[0]
    templatepath=(os.path.join('template',str(category[0])+'.jpg'))
    path=generateWithTemplate(templatepath,sentence)
    return  path
print (search(sentenceI))
cursor.close()
conn.close()

