from core.menu import show_menu

from utils.youtube_downloader import download_video
from utils.background_remover import remove_background
from utils.pdf_converter import pdf_to_text
from utils.qr_generator import generate_qr


def main():
    while True:
        show_menu()
        choice = input("Seçim: ").strip()

        if choice == "1":
            url = input("Video URL: ").strip()
            download_video(url)

        elif choice == "2":
            inp = input("Giriş görseli: ").strip()
            out = input("Çıkış dosyası: ").strip()
            remove_background(inp, out)

        elif choice == "3":
            path = input("PDF yolu: ").strip()
            print(pdf_to_text(path))

        elif choice == "4":
            data = input("QR içeriği: ").strip()
            filename = input("Dosya adı (enter=qr.png): ").strip() or "qr.png"
            generate_qr(data, filename)

        elif choice == "0":
            print("Çıkış yapıldı.")
            break

        else:
            print("Geçersiz seçim.")


if __name__ == "__main__":
    main()