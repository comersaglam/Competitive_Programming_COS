 #! DP (DYNAMIC PROGRAMMING)
#!Knapsack problem
#* elimizdeki sayıların bir kısmını toplayarak bir yere ulaşabiliyor muyuz?
#* sondan başlayarak listemizdeki her k değeri için eğer k sayı geriyi oluşturabiliyor
    #* muyuz, evetse o sayı da oluşur diyerek ilerliyoruz.
#* sondan olmasının sebebi aynı sayının katlarını hesaba katmak istemememiz(1 kez kullanılabilir)
lst = [2,3,1]
target = 6
dp = [ 0 for i in range(target+1)]
dp[0] = 1
for i in lst:
    for j in range(target, i, -1):# geriye doğru tarıyoruz ki katları dahil etmeyelim
        dp[j] = dp[j] or dp[j-i] #iki sayıdan biri oluşabiliyorsa geriye doğru, o da 1 olsun
print(dp)

#! Coin Problems (Unordered)
#* bu sefer baştan başlayarak tarıyoruz, çünkü bu sefer aynı paradan çok tane olduğu için tekrar tekrar kullanabiliyoruz
#* true false olarak saklamaktan ziyade her oluşturduğumuzda +1 yaparak saklarsak kaç farklı yol olduğunu bulmuş oluruz
#* her muhtemel duruma aynı zamandaa önceki sayıları oluşturanların listesi+k sayısını liste olarak eklersek de hangi ihtimallerle oluştuğunu bulmuş oluruz
        #* yani aslında dictionary de kaç tane ve nasılı tutmuş oluyourz
#dp yi 0 larla doldurma kodu
for coin in lst:
    for t in range(coin, target+1):
        dp[t] = dp[t] + dp[t-coin] #or yerine + koyduk her ihtimali dahil etmek için
print(dp)

#! Coin Problems (Ordered)
#dp yi 0 larla doldurma kodu
for i in range(target +1):
        for coin in lst:
             if t-coin >= 0:
                  dp[t] = dp[t] + dp[t-coin] #* for döngülerinin yerini değiştirince her k yı her puan için dahil ediyoruz. böylece sayıların sırası önemli oluyor
print(dp)