import streamlit as st
import pandas as pd
import tkinter as tk


# レイアウト
# # 数値のフォーマット選択
# radio = st.radio(label = '金額のスタイルを選択してください：', options = ('10', '10.00'), horizontal = True)
# if radio is '10':
#     min = 0
#     step = 1
#     format = '0'
# else:
#     min = 0.0
#     step = 1.0
#     format = '2'
# price = st.number_input(label = '金額を入力してください：', min_value = min, step = step, format = f'%.{format}f')

price = st.number_input(label = '金額を入力してください：', min_value = 0, max_value = 100000, step = 1)
# コンテナに表を入れることでデータに合わせてサイズが変わる
container = st.empty()


# データ取得
def get_data(price):
    list_price = []
    list_change = []

    # 桁数取得
    digit = len(str(price))

    # 各桁ごとに計算
    for i in range(1, digit):
        ten = 10**(i)
        rem = price%ten # 余り
        rem = int(str(rem)[0]) # 余りの最上位を取得
        
        # 5以上の場合
        if rem > 4:
            # 金額の算出
            pay = price + 5*(10**(i - 1))

            # リストに追加
            list_price.append(pay)
            list_change.append(5*10**(i - 1))

    # 9円以下用
    if digit == 1 and price > 4:
        # 金額の算出
        pay = price + 5

        # リストに追加
        list_price.append(pay)
        list_change.append(5)

    return list_price, list_change


# データ取得
list_price, list_change = get_data(price)
list_column = ['支払金額']

# 表示
# 個々でコンテナを空にしないとうまくいかない
# これでもうまくいったり行かなかったりだけど範囲制限で解決
if list_price != []:
    container.empty()
    df = pd.DataFrame(data = list_price, index = list_change, columns = list_column)
    df.index.name = 'お釣り'
    container.dataframe(data = df)
else:
    container.empty()
    container.markdown('5刻みのお釣りをもらうための支払いは非効率です。')