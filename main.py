
import hashlib
import re
import os

HASH_TYPES = {
    32: ("MD5", "md5"),
    40: ("SHA1", "sha1"),
    56: ("SHA224", "sha224"),
    64: ("SHA256", "sha256"),
    96: ("SHA384", "sha384"),
    128: ("SHA512", "sha512")
}

def banner():
    os.system("cls" if os.name == "nt" else "clear")
    print("=" * 50)
    print("          ADVANCED HASH CRACKER")
    print("=" * 50)

def identify_hash():
    value = input("\nEnter Hash: ").strip().lower()

    if not re.fullmatch(r"[a-f0-9]+", value):
        print("Invalid hash format!")
        return

    result = HASH_TYPES.get(len(value))

    if result:
        print("[+] Hash Type:", result[0])
    else:
        print("[-] Unknown hash type")

def generate_hash():
    text = input("\nEnter Text: ")

    print("\n1. MD5")
    print("2. SHA1")
    print("3. SHA256")
    print("4. SHA384")
    print("5. SHA512")

    choice = input("\nSelect Algorithm: ")

    algorithms = {
        "1": "md5",
        "2": "sha1",
        "3": "sha256",
        "4": "sha384",
        "5": "sha512"
    }

    algorithm = algorithms.get(choice)

    if not algorithm:
        print("Invalid choice!")
        return

    result = hashlib.new(
        algorithm, text.encode("utf-8")
    ).hexdigest()

    print("\n[+] Generated Hash:", result)

def wordlist_audit():
    target = input("\nEnter your test hash: ").strip().lower()

    if not re.fullmatch(r"[a-f0-9]+", target):
        print("Invalid hash!")
        return

    detected = HASH_TYPES.get(len(target))

    if not detected:
        print("Unsupported hash format!")
        return

    algorithm = detected[1]
    filename = input("Wordlist filename [wordlist.txt]: ").strip()
    filename = filename or "wordlist.txt"

    if not os.path.isfile(filename):
        print("Wordlist file not found!")
        return

    print("\n[+] Starting authorized wordlist audit...")

    with open(filename, "r", encoding="utf-8",
              errors="ignore") as file:
        for number, line in enumerate(file, 1):
            word = line.rstrip("\r\n")

            result = hashlib.new(
                algorithm, word.encode("utf-8")
            ).hexdigest()

            if result == target:
                print("\n[+] Match found!")
                print("[+] Candidate:", word)
                print("[+] Line:", number)
                return

    print("\n[-] No match found in wordlist.")

def menu():
    while True:
        banner()

        print("1. Identify Hash")
        print("2. Generate Hash")

        print("3. Wordlist Audit")
        print("4. Exit")

        choice = input("\nChoose Option: ")

        if choice == "1":
            identify_hash()
        elif choice == "2":
            generate_hash()
        elif choice == "3":
            wordlist_audit()
        elif choice == "4":
            print("Exiting HashCracker...")
            break
        else:
            print("Invalid Option!")

        input("\nPress Enter to continue...")

if __name__ == "__main__":
    menu()
