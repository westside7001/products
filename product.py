import os

#讀取檔案
products = []
if os.path.isfile('products.csv'): #檢查檔案是否存在
    print('file exist')
    with open('products.csv', 'r',encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:
                continue  # 遇到"商品,價格"字串，則跳過此行
            name, price = line.strip().split(',')
            products.append([name, price])
else:
    print('file is not exist')
#讀取檔案



print(products)

products = []
while True:
    name = input('請輸入商品名稱:')
    if name == 'q':
        break
    price = input('請輸入商品價格:')
    products.append([name,price])
print(products)

for p in products:
    print(p[0],'價格是',p[1])

with open('products.csv','w', encoding='utf-8') as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0]+','+p[1]+'\n')
