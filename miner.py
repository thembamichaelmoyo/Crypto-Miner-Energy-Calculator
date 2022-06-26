from hashlib import sha256
import random
import locale

nonce_limit = 999999999999999999999999999999999999999
previous_hash = input("What is the previous hash?\n")
unit_price = int(input("What is your unit price in cents, per KWh?\n"))
device_pwr = float(input("What is the maximum power rating in Watts?\n"))
difficulty = random.randint(6, 8)
locale.setlocale(locale.LC_ALL, ("", "utf-8"))
currency_symbol = locale.localeconv()["int_curr_symbol"]
block_number = random.randint(1, 999999999999999)


def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()


def coining(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = "0" * int(prefix_zeros)
    for nonce in range(nonce_limit):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"Success at {nonce} nonce.")
            return new_hash

    raise BaseException("Coining failed.")


if __name__ == "__main__":
    transactions = """Sender->Receiver->10
    Sender->Receiver->100
    Sender->Receiver->1000"""
    import time

    start = time.time()
    print("Coining in progress...")
    new_hash = coining(block_number, transactions, previous_hash, difficulty)
    duration = float((time.time() - start))
    pwr_cons = float((duration / 360000) * device_pwr)
    pwr_cost = float(pwr_cons) * unit_price
    print(f"Coining on block {block_number}, lasted {duration} seconds.")
    print(f"Coining power usage was {pwr_cons} Watts.")
    print(f"This cost you {currency_symbol}{pwr_cost}.")
    print("The new hash is...")
    print(new_hash)
# This is a new line that ends the file.
