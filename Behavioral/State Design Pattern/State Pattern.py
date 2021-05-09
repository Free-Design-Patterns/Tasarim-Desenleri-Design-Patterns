from __future__ import annotations
from abc import abstractmethod, ABCMeta


class State(object, metaclass=ABCMeta):
    """
    Abstract bir State sınıfı oluşturuyoruz. Burada State(Durum)'lerde kesinlikle kullanılacak fonksiyonları tanımlıyoruz.
    Tanımladığımız fonksiyonlarda abstract olarak tanımlıyoruz.
    """

    @abstractmethod
    def disari_cikar(self, atm):
        raise NotImplementedError('')

    @abstractmethod
    def iceri_al(self, atm):
        raise NotImplementedError('')


class KartYok(State):
    """
    Her bir State(Durum) bir sınıf olarak tanımlanır ve State sınıfından inherited edilir. Ayrıca State sınıfında tanımlanan
    abstract fonksiyonlar durumun getirdiği davranışlara göre yazılır.
    """

    """
    Fonksiyonlarda ki atm değişkeni aslında aşağıda tanımlanmış ATM sınıfını temsil eder. Bu sayede ATM sınıfının state(durum)'ini
    değiştirebiliriz.
    """

    def disari_cikar(self, atm):
        print('Hata : kart yok!')

    def iceri_al(self, atm):
        print('Islem Tamam!')
        atm.state = KartVar()


class KartVar(State):
    def disari_cikar(self, atm):
        print('Islem Tamam!')
        atm.state = KartYok()

    def iceri_al(self, atm):
        print('Hata : Iceride kart var!')


class ATM:
    """
    Bu sınıf Context sınıf yerine de geçebilir. İstemci(Client) tarafından istenilen işlemin fonksiyonları burada tanımlanır.
    İstemcilerle(Client) ilişkili arayüz tanımlanır.
    """

    def __init__(self):
        self.state = KartYok()

    def karti_iceri_al(self):
        self.state.iceri_al(self)

    def karti_disari_cikar(self):
        self.state.disari_cikar(self)


if __name__ == "__main__":
    atm = ATM()
    atm.karti_disari_cikar()  # Başlangıçta kart yok durumunu verdik. Ve buna rağmen kartı dışarı çıkarmaya çalıştığımız için hata alıyoruz.
    atm.karti_iceri_al()  # Sistemdeki durum kart yok olduğu için. Kartı içeri al komutu başarıyla çalışmaktadır.
    atm.karti_iceri_al()  # Sistemdeki durum kart var olduğu için tekrar kartı sisteme alma komutunda hata mesajı döndürür.
    atm.karti_disari_cikar()  # Sistemde kart olduğu için başarıyla dışarı çıkarma işlemi yapabiliyoruz.
    atm.karti_disari_cikar()  # Sistemde kart olmadığı için tekrar kartı çıkarma komutunda hata alıyoruz.