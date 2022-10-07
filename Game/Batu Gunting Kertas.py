import random
print("Batu, Gunting, Kertas.....")
def main():
    BGK = ["Batu", "Gunting", "Kertas"]
    komputer = random.choice(BGK)

    pemain = input("Pilihanmu: ").lower().capitalize()

    print(f"Aku memilih {komputer}, dan kamu memilih {pemain}")
    if komputer == "Batu":
        if pemain == "Batu":
            print("Kita seri!")
        if pemain == "Gunting":
            print("Kamu kalah!")
        if pemain == "Kertas":
            print("Kamu menang!")

    if komputer == "Gunting":
        if pemain == "Batu":
            print("Kamu menang!")
        if pemain == "Gunting":
            print("Kita seri!")
        if pemain == "Kertas":
            print("Kamu kalah!")

    if komputer == "Kertas":
        if pemain == "Batu":
            print("Kamu kalah!")
        if pemain == "Gunting":
            print("Kamu menang!")
        if pemain == "Kertas":
            print("Kita seri!")

    else:
        print("Masukan jawaban dengan benar")
        main()


    print("Apa kamu mau main lagi?")
    main_lagi = input("Iya atau Tidak?").lower().capitalize()
    if main_lagi == "Iya":
        main()

    elif main_lagi == "Tidak":
        print("Terima kasih telah bermain")
main()