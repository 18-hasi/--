import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#タイトル
st.title("財務諸表分析アプリ")

#サンプルデータ（売上高、流動資産、負債を追加）
data={
    "年": ["2020","2021","2022"],
    "売上高": [10000,11000,13000],
    "純利益": [500,600,700], #単位：百万
    "自己資本": [5000,5200,5400],
    "総資産": [12000,12500,13000],
    "流動資産": [6000, 6500,7000],
    "流動負債":[3000,3200,3500]
    }

df=pd.DataFrame(data)


df["ROE (%)"]=(df["純利益"] / df["自己資本"])*100
df["自己資本比率 (%)"]=(df["自己資本"] / df["総資産"])*100
df["流動比率 (%)"]=(df["流動資産"] / df["流動負債"])*100
df["売上成長率(%)"]=df["売上高"].pct_change()*100   #前年比成長率
df["総資産回転率"]=df["売上高"] / df["総資産"]

#財務諸表データを表示
st.write("**財務諸表データ**")
st.dataframe(df)

#グラフ作成
fig, ax=plt.subplots()
ax.plot(df["年"], df["ROE (%)"], marker="o",label="ROE (%)",linestyle="-")
ax.plot(df["年"], df["自己資本比率 (%)"],marker="s", label="Equity Ratio (%)",linestyle="--")
ax.plot(df["年"],df["流動比率 (%)"],marker="^",label="Current Ratio (%)",linestyle="-.")
ax.legend()

#グラフの装飾
ax.set_xlabel("Year")
ax.set_ylabel("Ratio(%)")
ax.set_title("Financial Metrics Over Time")   
ax.grid(True)

#Streamlitで表示
st.pyplot(fig)