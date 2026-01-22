import os


def file_exists(path):
    """Dosya var mı kontrol eder"""
    return os.path.exists(path)


def print_error(message):
    """Standart hata mesajı basar"""
    print(f"[HATA] {message}")


def print_success(message):
    """Standart başarı mesajı basar"""
    print(f"[OK] {message}")