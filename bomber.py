import time
import random

def send_fake_otp(number):
    otp = random.randint(100000, 999999)
    print(f"[+] Sending OTP to {number} -> {otp}")
    time.sleep(1)

def main():
    print("""
===============================
      SATHANIC BOMBER v1.0
         FOR FUN ONLY
===============================
    """)
    number = input("Enter target number (e.g. +91xxxxxxxxxx): ")
    count = int(input("Enter how many OTPs to send (fake): "))

    for i in range(count):
        send_fake_otp(number)

    print("\n[✔] Finished sending fake OTPs.")

if __name__ == "__main__":
    main()
