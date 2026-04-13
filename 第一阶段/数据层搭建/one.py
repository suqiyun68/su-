import tushare as ts

# 1. 初始化接口，替换 '你的token' 为刚才复制的真实token
pro = ts.pro_api('你的token')

# 2. 调用接口，获取永兴材料（600519.SH）的日线数据
df = pro.daily(ts_code='002756.SZ', start_date='20260320', end_date='20260413')

# 3. 查看数据
print("永兴材料")
print(df.head())
