import qrcode
import os
import time

from qrcode.main import make

os.system("pip install qrcode[pil]")

def makeqr():
    data = f"{qrcode1}"
    
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5,
    )
    qr.add_data(data)
    qr.make(fit=True)
    
    img = qr.make_image(fill="black", back_color="white")
    img.save('yourcodeqr.png')

def banner():
    banner1 = """
    =======================
    Generator Code QR
    Credit qrcode Module
    =======================
    """
    print(banner1)

if __name__ == "__main__":
    banner()
    qrcode1 = input("Put your TEXT For qrcode: ")
    print("Wait 5 sec....")
    time.sleep(5)
    makeqr()
    print("Heres your QR Code")