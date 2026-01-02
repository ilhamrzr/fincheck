import json
import sys

WHITE = "\033[97m"
GREEN = "\033[92m"
GRAY = "\033[90m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

_progress_open = False


def c(text, color):
    return f"{color}{text}{RESET}"


def close_progress_if_any():
    global _progress_open
    if _progress_open:
        sys.stdout.write("\n")
        sys.stdout.flush()
        _progress_open = False


def mark_progress_open():
    global _progress_open
    _progress_open = True


def mark_progress_closed():
    global _progress_open
    _progress_open = False


def print_success(title, data):
    close_progress_if_any()
    print(c(f"\n[✓] {title}", GREEN))
    for k, v in data.items():
        print(f"{k.capitalize():10}: {v}")


def print_error(msg):
    close_progress_if_any()
    print(c("\n[✗] ERROR", RED))
    print(f"Reason      : {msg}")


def print_warning(msg):
    close_progress_if_any()
    print(c("\n[!] WARNING", YELLOW))
    print(msg)


def print_info(msg):
    close_progress_if_any()
    print(c(msg, BLUE))


def print_json(data):
    close_progress_if_any()
    print(json.dumps(data, indent=2))


def print_summary_single(target, provider, input_value, result):
    close_progress_if_any()
    print("\n---------- SUMMARY ----------")
    print(f"Target    : {target}")
    print(f"Provider  : {provider}")
    print(f"Input     : {input_value}")

    if result == "SUCCESS":
        print(f"Result    : {c(result, GREEN)}")
    elif result == "FAILED":
        print(f"Result    : {c(result, RED)}")
    else:
        print(f"Result    : {c(result, YELLOW)}")

    print("-----------------------------")
