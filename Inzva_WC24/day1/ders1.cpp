int main(){
    //* IO input line are:
    //* ios::sync_with_stdio(false);
    //*cin.tis(nullptr)
}

//!QUEUE
queue<int> //queue call
q.front()   //öndekini söyler
q.pop()     //öndekini çıkarır ve döndürür
q.push(5)   //en arkaya 5 ekle

//!STACK
stack.push()
stack.pop()
//parantez sorularında gelebilir

//!SET VS MAP  (logn li data structure)
//^ Setler eleman ekleme(binary search ile ekleme yapar, ikili ikili arayıp ekleme çıkarma yapar)
//^ binary search tree, black flag tree??(özel versiyonu) in cpp
//^ sette set saklanmaz char vs eklenebilir sadece int değil
//^ duplicate yok
//^ sıralı ama tree halinde
//^ (hashle implemente edilebilir, olmaya da bilir. indexing bazen olur bazen olmaz)
//^ set ekleme logn arama logn. 
//^ map ekleme o1 arama on.

s.insert()
s.find()
// multiset (duplicatelar var)
// unordered-set (sıralı değil diğer özellikler var)(insert o1 de hash yapıyor(bazen))
//~
//&
map<int,int> //* pythondaki dictionary ye benzer, key-value
m.[key] = value
m.erase[key]


//!Matematik konuları
//! fast exponantiation
//? 1<= a,b <= 10^8 nasıl hızlı hesaplanır
//^ 5^32 yi bulmak için 5^16 yo bulup kendisiyle çarpalım. onun için 5^8 i bulur kendisiyle çarparım diye diye logn işlemde kendisiyle çarparak bulurum
//^eğer üs tek ise 5^13, 5*5^12 olarak hesaplayıp devam ederim
//* matris çarpmalarında kullanılır
//* fibonacciyi logn de çözebilir

//!FERMAT'S LITTLE THEOREM
//^m asal sayı iken. bir sayıyı a ya bölmek yerine a^m-1 = 1 mod(m) eşliğinden ==> a^m-2 = 1/a mod(m) yazıp, a^m-2 ile çarparsak hiçbir şey farketmez.
//^bölme işleminde mod alamadığımız için bu yöntemi kullanmak mantıklı

//! GCD euclid formula

//! SIEVE OF ERASTHOTENES
// n den küçük asal sayıların sayısı logn e yakınsar
// bu yüzden n tane sayıyı sieve yöntemle asal mı diye hesaplamak n^2 yerine nlog(logn) kadar olur

//!Binary Search