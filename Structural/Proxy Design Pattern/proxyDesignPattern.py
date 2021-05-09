from abc import ABC, abstractmethod


class CollegeAbstract(ABC):
    """
    CollegeAbstract arabirimi hem College hem de CollegeProxy için ortak işlemleri bildirir.
    İstemci(Client) bu arayüzü kullanarak College ile çalıştığı sürece,
    ona gerçek bir konu yerine bir vekil sunucu iletebileceksiniz.
    """

    @abstractmethod
    def studyingInCollege(self) -> None:
        pass


class College(CollegeAbstract):
    """Kaynak - Bellekte büyük yer kaplayan nesne"""

    def studyingInCollege(self):
        print("Studying In College.")


class CollegeProxy(CollegeAbstract):
    """Aracı olarak hareket eden nispeten daha az kaynak - yoğun vekil nesne.
    Gerekli şartlar veya işlemler sağlandığında gerçek kaynak ile iletişim kurulur."""

    def __init__(self):
        self.feeBalance = 1000
        self.college = None

    def studyingInCollege(self):
        print("Proxy in action. Checking to see if the balance of student is clear or not...")
        if self.feeBalance <= 500:
            # Bakiye 500'den azsa, çalışmasına izin verir
            self.college = College()
            self.college.studyingInCollege()
        else:
            # Aksi takdirde, College nesnesini somutlaştırma olmaz boş yere.
            print("Your fee balance is greater than 500, first pay the fee")


if __name__ == "__main__":
    # CollegeProxy sınıfından nesne oluşturulur.
    collegeProxy = CollegeProxy()

    # İstemci(Client), üniversitede varsayılan bakiye olan 1000'de okumaya çalışıyor.
    # Mantıksal olarak böyle bir bakiye ile okuyamayacağı için,
    # Kolej nesnesini yapmaya gerek yok.
    collegeProxy.studyingInCollege()

    # Bakiye 500 sınırının altına çekiliyor
    collegeProxy.feeBalance = 100

    # Sınırın altında bir değer ile işlem yapılmaya çalışıldığı için nesne oluşturuluyor ve işlem yapılıyor.
    collegeProxy.studyingInCollege()
