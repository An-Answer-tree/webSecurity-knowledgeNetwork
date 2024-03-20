from neo4j import GraphDatabase
import pandas as pd
import numpy as np
import json
from function import *

uri = "neo4j://127.0.0.1:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "12345678"))

# import event name(aka title) to varible title_list
title_list = []
with open('data_after_ner_ssid.json', 'rb') as f:
    json_list = json.loads(f.read())
for i in range(0, 2166):
    title_list.append(json_list[i]['title'][0])
for i in range(2166, 2818):
    title_list.append(json_list[i]['title'])

# import event featrues
features_df = pd.read_csv('./result_of_ner.csv')

# import relationship matrix
relationship_matrix = np.loadtxt('./0.9_0_1_matrix.csv', delimiter=',')
matrix_size = 2818

# 在Neo4j数据库中创建节点
with driver.session() as session:
    session.write_transaction(clear_all_nodes)
    session.write_transaction(create_event_nodes, title_list, features_df)
    session.write_transaction(connect_related_nodes, matrix_size, relationship_matrix)

driver.close()  # close the driver object