def dosya_yaz():
    # Kullanıcıdan 5 satır veri alıp 'veri.txt' dosyasına yazan fonksiyon
    with open("veri.txt", "w", encoding="utf-8") as dosya:
        print("Lütfen 5 satır veri girin:")

        for i in range(1, 6):
            satir = input(f"Satır {i}: ")
            dosya.write(satir + "\n")  # Kullanıcının girdisini dosyaya yaz

    print("Veriler 'veri.txt' dosyasına kaydedildi.\n")


def dosya_oku():
    # 'veri.txt' dosyasını okuyup içeriğini ekrana yazdıran fonksiyon
    try:
        with open("veri.txt", "r", encoding="utf-8") as dosya:
            print("Dosya içeriği:\n")
            for satir in dosya:
                print(satir, end="")  # Satırları olduğu gibi ekrana yaz
    except FileNotFoundError:
        print("Önce dosyaya veri yazmalısınız!")


if __name__ == "__main__":
    dosya_yaz()  # Önce dosyaya veri yaz
    dosya_oku()  # Sonra dosyanın içeriğini oku
