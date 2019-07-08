
# coding: utf-8

# In[1]:


import pandas as pd
import csv
import json


# In[2]:


file_path = 'cvs2json_test.csv'


# In[4]:


def csv2json(filepath):

    reader = csv.reader(open(file_path))
    data = []
    for row in reader:
        data.append(row)
    result = {}
    layer = []
    for i in range(len(data)):
        cur_row = data[i]
        cur_state = result
        for j in range(len(cur_row)):
            cur_col = cur_row[j]
            if cur_col != '':
                new_item = data[i][j]
                if j >= len(layer):
                    layer.append(new_item)
                else:
                    layer[j] = new_item

                if isinstance(cur_state, dict):
                    cur_state[new_item] = []
                    cur_state = cur_state[new_item]
                else:
                    cur_state.append({new_item: []})
                    #print(cur_state)
                    cur_state = cur_state[-1][new_item]
            else:
                #print(cur_state)
                if isinstance(cur_state, dict):
                    cur_state = cur_state[layer[j]]
                else:
                    cur_state = cur_state[-1][layer[j]]
            #cur_state = cur_state[layer[cur_col]]
    return result


# In[5]:


result


# In[18]:


def find_key_in_json(d, key, cur_path):
    if key in d:
        cur_path.append(key)
        yield '.'.join(cur_path)
    for k in d:
        cur_path.append(k)
        v = d[k]
        if v == []:
            return
        if v:
            for item in v:
                yield from find(item, key, cur_path)
                cur_path.pop()


# In[32]:


ans = []
for item in find(result, '帝国的征服与扩展', []):
    ans.append(item)
if ans:
    print(ans)
else:
    print(u'不存在关键字')


# In[8]:


res = []
find(result, '两河流域文明', res)


# In[ ]:


import queue

def generate(string, dic):
    index_string = 0
    string_list = list(string)
    q = queue.Queue()
    q.put(string_list)
    while index_string < len(string_list):
        if string_list[index_string] in dic:
            q_len = q.qsize()
            for i in range(q_len):
                temp_str = q.get().copy()
                for el in dic[string_list[index_string]]:
                    temp_str[index_string] = el
                    q.put(temp_str.copy())
        index_string += 1
    while q.qsize():
        print(''.join(q.get()))



string = 'adcbf'
dic = {'a': ['B', 'C'], 'b': ['X','Y'], 'f':['&', '#']}
generate(string, dic)

