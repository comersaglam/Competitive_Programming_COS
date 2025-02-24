 #! Bipartite graph
#* her nodun 2 alt(1tane de üst) node ile ilişkisi olabiliyor
#* coloring yöntemiyle bipartite olup olmadığı kontrol olmalı. Her nodun komşusu kendinden farklı renk almak zorundayken
    #* eğer ki 2 den fazla renge ihtiyacımız varsa bipartite değildir.
    #* bir cycle (kendinden çıkıp kendine girecek yol) çift uzunlukta değil ise bipartite değildir 
#* bfs (yahut dfs) ile tüm nodeları gezerken bunu bulabiliriz.
#* ama bu yöntemle idealde en az kaç renk gerekir sorusu çok zor çözülür.


#! Topological Sort
#! must be DAG(directed acyclic graph)
#* birden çok top sortu olabilir bir graphın.
#* oluşturma yöntemi: herhangi bir noddan dfs atıyoruz. daha ileri gidemediğimiz noktada sort listesine veriyoruz.
#* en sonda da visit edilmeyen nodelar için aynı algoritmayı çalıştırıp listeye eklemeye devam. 
#* en sonda oluşan listin ters hali bizim top sort'umuza eşit. her sayının solundaki hiçbir noda erişimi yok demek

#! siteler
"""cp algorithms
codeforce
leetcode
"""