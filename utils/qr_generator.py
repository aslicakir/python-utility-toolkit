def generate_qr(data, filename="qr.png"):
    try:
        import qrcode
    except ImportError:
        print("qrcode kurulu değil. Kurulum: pip install qrcode[pil]")
        return

    img = qrcode.make(data)
    img.save(filename)
    print(f"QR kod oluşturuldu: {filename}")