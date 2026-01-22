def remove_background(input_path, output_path):
    try:
        from rembg import remove
        from PIL import Image
    except ImportError:
        print("rembg/pillow kurulu değil veya bu ortamda desteklenmiyor.")
        print("Kurulum: pip install rembg pillow")
        return

    img = Image.open(input_path)
    result = remove(img)
    result.save(output_path)
    print("Arka plan silindi:", output_path)