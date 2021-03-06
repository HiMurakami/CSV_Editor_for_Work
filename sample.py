import pandas as pd
from datetime import datetime
from tqdm import tqdm

while True:
    try:
        print('Set USD Rate (default: 110)')
        #print('USD: ', end='')
        USD = float(input('USD: '))
        break
    except ValueError:
        USD = 110.0
        break
while True:
    try:
        print('Set RMB Rate (default: 18)')
        #print('USD: ', end='')
        RMB = float(input('RMB: '))
        break
    except ValueError:
        RMB = 18.0
        break


c_range = range(2)
#読み込むCSVの列幅は決め打ちしてあとで整形が良い気がする
#今回は整形せず決め打ちのまま

df = pd.read_csv('input.csv', header=None, names = c_range)
print(df)       # show all column

print("\nstart")
for i in range( len(df.index) ):
    if df.iat[i,0] == "<REF>":
        df0 = df.drop(range(i))

print("\ndf0: header is deleted")
print(df0)

df1=df0.dropna(how='any')
print("\ndf1: shrink")
print(df1)
ryou = len(df1.index)

df2 = df1.sort_values(by=1)
print(df2)
df2[2] = 0
print("\ndf2: sort and add empty_column")
print(df2)

d_list=[0]
#print("\ndf3")
#df3=df2
pbar0 = tqdm(total=len(df2.index) )
for i in range( len(df2.index) ):
    cnt=0
    pbar0.update(1)
    for j in range( len(df2.index) ):
        if df2.iat[i,1] == df2.iat[j,1]:
#            print(df2.iat[i,1] +"=="+ df2.iat[j,1])
            if cnt != 0 and j>0 and d_list[-1] <j :
                d_list.append(j)
            cnt+=1
    df2.iat[i,2]=cnt
#    print(cnt)
#    print(d_list)
#    print("")
#print(d_list)
pbar0.close()

#df.reset_index(drop=True)
df3 = df2.reset_index(drop=True).drop(d_list)
print("\ndf3: counting")
print(df3)
mount=0
for i in range(len(df3.index)):
    mount = mount + df3.iat[i,2]
print("合計：")
print( mount)
print("")
print(len(df1.index)-1)#<REF>行の分を引く

df3.to_csv(datetime.now().strftime("output_%Y_%m%d_%H%M.csv"),header=False,index=False)
