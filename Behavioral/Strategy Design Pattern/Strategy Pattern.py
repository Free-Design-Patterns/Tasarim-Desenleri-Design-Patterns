from __future__ import annotations
from abc import ABC, abstractmethod


class Context():
    """
    İstemcilerin(Client), istenilen strategy tanımlaması ve tanımlanan algoritmayı çalıştırması için gereken sınıfdır.
    """

    def __init__(self, strategy: Strategy) -> None:
        """
        Genellikle istemci(Client) tarafından gönderilen strateji burada kabul edilir.
        """

        self._strategy = strategy

    @property
    def strategy(self) -> Strategy:
        """
        Context sınıfı, Strateji nesnesinin referansını korur.
        Context sınıfı, stratejilerin somut sınıflarını bilmez.
        Strateji interface'i ile tüm strateji sınıfları çalıştırılmalıdır.
        """

        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy) -> None:
        """
        Strateji değiştirilmek istenildiği takdirde bu fonksiyon kullanılır.
        """

        self._strategy = strategy

    def islemi_yap(self) -> None:
        """
        Context, birden fazla algoritmayı tek başına uygulamak yerine Strateji nesnesinden algoritmalarından yararlanır.
        """

        # Burada işlemler yapılabilir.

        sonuc = self._strategy.algoritmayi_calistir(20, 10)
        print("İşlemin sonucu:{}".format(sonuc))


class Strategy(ABC):
    """
    Strateji arayüzünde, Strateji sınıfından türetilecek tüm sınıflarda kullanılacak ortak fonksiyonlar belirtilir.

    Context bu interface'i kullanır Strateji için tanımlanan algoritmaları çalıştırmak için.
    """

    @abstractmethod
    def algoritmayi_calistir(self, sayi1, sayi2):
        pass


class StrategyAlgorithmAddition(Strategy):
    def algoritmayi_calistir(self, sayi1, sayi2):
        return sayi1 + sayi2


class StrategyAlgorithmExtraction(Strategy):
    def algoritmayi_calistir(self, sayi1, sayi2):
        return sayi1 - sayi2


class StrategyAlgorithmMultiplication(Strategy):
    def algoritmayi_calistir(self, sayi1, sayi2):
        return sayi1 * sayi2


class StrategyAlgorithmDivision(Strategy):
    def algoritmayi_calistir(self, sayi1, sayi2):
        return sayi1 / sayi2


if __name__ == "__main__":
    context = Context(StrategyAlgorithmAddition())
    print("İstemci(Client): Strateji olarak toplama yapacak algoritmayı çalıştırdı.")
    context.islemi_yap()
    print()

    print("İstemci(Client): Strateji olarak çıkarma yapacak algoritmayı çalıştırdı.")
    context.strategy = StrategyAlgorithmExtraction()
    context.islemi_yap()
    print()

    print("İstemci(Client): Strateji olarak çarpma yapacak algoritmayı çalıştırdı.")
    context.strategy = StrategyAlgorithmMultiplication()
    context.islemi_yap()
    print()

    print("İstemci(Client): Strateji olarak bölme yapacak algoritmayı çalıştırdı.")
    context.strategy = StrategyAlgorithmDivision()
    context.islemi_yap()
    print()
