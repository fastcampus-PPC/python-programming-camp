#!/usr/bin/env python3

import pandas as pd

url = 'https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv'
chipo = pd.read_csv(url, sep = '\t')

# 한 주문에 10달러 이상 사용한 주문의 id들 출력하기
chipo['item_price'] = chipo['item_price'].apply(lambda x: float(x[1:]))
chipo_group = chipo.groupby('order_id').sum()
chipo.groupby('order_id').sum()[chipo_group.item_price >= 10].index.values


# 각 아이템의 가격 구하기
#### chipo['item_name'] = chipo['item_name'].apply(lambda x: x.replace("-", " "))
chipo_filtered = chipo.drop_duplicates(['item_name','quantity', 'choice_descriptor'])
chipo_one_prod = chipo_filtered[chipo_filtered.quantity == 1]
price_per_item = chipo_one_prod.groupby('item_name').min()
price_per_item.sort_values(by = "item_price", ascending = False)


# 가장 비싼 주문에서 item이 몇개 팔렸는지 구하기
chipo.groupby('order_id').sum().sort_values(by='item_price', ascending=False)['quantity'].head(1)

########################################################
# “Veggie Salad Bowl”이 몇 번 주문되었는지 구하기
chipo_salad = chipo[chipo['item_name'] == "Veggie Salad Bowl"]
len(chipo_salad['order_id'].value_counts() == 1)


# “Chicken Bowl”을 2개 이상 주문한 사람 숫자 구하기
chipo_chicken = chipo[chipo['item_name'] == "Chicken Bowl"]
chipo_chicken_ordersum = chipo_chicken.groupby('order_id').sum()['quantity']
chipo_chicken_result = chipo_chicken_ordersum[chipo_chicken_ordersum >= 2]
len(chipo_chicken_result)