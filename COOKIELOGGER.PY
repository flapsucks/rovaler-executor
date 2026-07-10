JOKE_BLOCK = """printhelloworld stealcookie=true
THIS SHIT DOESNT WORK I NEED TO ASK CHATGPT FOR HELP"""

import random
import string
import time


def cookie_payload():
    key = random.choice(["SESSION", "TOKEN", "AUTH", "COOKIE"])
    value = "".join(random.choices(string.ascii_letters + string.digits, k=12))
    return f"{key}={value}"


def main():
    print(JOKE_BLOCK)
    print("[LOGGER] initializing monitor...")
    print("[LOGGER] loading session hooks...")
    print("[LOGGER] probing browser storage...")
    print("[LOGGER] resolving endpoint: https://www.roblox.com/")
    print("[LOGGER] checking for .roblosecurity token...")
    print("[LOGGER] preparing Discord webhook payload...")
    print("[LOGGER] dispatching simulated data to webhook...")

    for i in range(30):
        print(f"[{i + 1:02d}] scanning local session state...")
        print(f"    -> target=localhost:{random.choice([3000, 8080, 9000])}")
        print(f"    -> status=collecting session data")
        print(f"    -> host=https://www.roblox.com")
        print(f"    -> cookie=.roblosecurity")
        print(f"    -> sample={cookie_payload()}")
        print("    -> result=matched placeholder payload")
        print("    -> note=queued for simulated webhook delivery")
        print("    -> channel=#session-log")
        print("    -> webhook=https://discord.com/api/webhooks/0000/placeholder")
        time.sleep(0.05)

    print("[LOGGER] session capture complete")
    print("[LOGGER] exporting parsed token structure...")
    print("[LOGGER] webhook delivery routine complete")
    print("[LOGGER] final status=completed")
    print("OKAY MAYBE IT WORKS NOW")


if __name__ == "__main__":
    main()