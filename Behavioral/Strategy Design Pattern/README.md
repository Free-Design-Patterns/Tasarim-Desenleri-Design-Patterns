# Strateji Tasarım Deseni(Strategy Design Pattern)
> Bu projede Strateji tasarım deseni python programlama dili kullanılarak kodlanmıştır

## Strateji Tasarım Deseni nedir ?
Strateji tasarım deseni en sık kullanılan davranışsal tasarım desenlerinden biridir.
Bu desenin amacı, bir istemcinin(Client) aynı görevi yapabilmek için birden farklı algoritma veya prosedürler arasında seçim yapabilmesini sağlamaktır.
Strateji tasarım modeli, onu kullanan istemcilerden(Client) bağımsız olarak algoritmayı kolayca değiştirmesini ve yeni bir algoritma eklenmesini sağlar.

## Strateji Tasarım Deseni Class Diagramı
![Algorithm schema](./Strategy%20Pattern%20UML.jpeg)

## Proje Açıklaması
Örnek olarak yapılan projede 4 işlem yapabilen ufak bir program Strateji tasarım deseni ile yazılmıştır.


* Öncelikle bir Strategy interface'i yazılır ve burada kalıtım(inherited) yapılacak sınıflarda kullanılacak(implement) ortak fonksiyonlar belirtilir.
![Strateji Interface](./Ekran%20goruntuleri/Strategy%20sinifi.JPG)

* Yapılacak işlem için olan farklı algoritmalar farklı sınıfların içine yazılır ve yazılan sınıflar Strategy interface'sine kalıtım yapılır.
![Different Algorithm](./Ekran%20goruntuleri/Farkli%20algoritma%20siniflari.JPG)

* Oluşturulan Strategy interface'ini kullanmak için bir Context sınıfı yazılır. Yapılacak işlem için hangi algoritmanın kullanılacağı yazılan Context sınıfında belirtilir.Context sınıfında kullanılacak algoritmanın sınıfı Strategy olarak tutulur ve gerekli işlemler(Business Logic) Context sınıfı içindeki algoritmayı çalıştıracak fonksiyonun içinde yapılır.
![Different Algorithm](./Ekran%20goruntuleri/Context%20sinifi.JPG)

* Istemci tarafında context sınıf çağırılır ve context sınıfa bir strateji sınıfından kalıtılmış bir sınıf verilir. Daha sonra context sınıfındaki fonksiyon çalıştırılır.Istenildiği takdirde Context sınıfındaki Strategy değiştirilip farklı algoritmalar kullanılabilir.
![Different Algorithm](./Ekran%20goruntuleri/Istemci%20tarafi.JPG)


## Geliştiriciler
* [@kbskl](https://github.com/kbskl)