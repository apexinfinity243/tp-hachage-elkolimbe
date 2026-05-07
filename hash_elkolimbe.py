#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔══════════════════════════════════════════════════════════╗
║          HASH FUNCTION :: EL-KOLIMBE CIPHER              ║
║          Author   : EL-KOLIMBE                           ║
║          Version  : 1.0.0                                ║
║          Lang     : Python 3.x                           ║
╚══════════════════════════════════════════════════════════╝
"""

import time
import sys
import hashlib

# ── Couleurs terminal ──────────────────────────────────────
RED     = "\033[91m"
GREEN   = "\033[92m"
YELLOW  = "\033[93m"
CYAN    = "\033[96m"
WHITE   = "\033[97m"
BOLD    = "\033[1m"
RESET   = "\033[0m"

BANNER = f"""
{RED}
 ██╗  ██╗ █████╗ ███████╗██╗  ██╗
 ██║  ██║██╔══██╗██╔════╝██║  ██║
 ███████║███████║███████╗███████║
 ██╔══██║██╔══██║╚════██║██╔══██║
 ██║  ██║██║  ██║███████║██║  ██║
 ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
{RESET}
{CYAN}  [ EL-KOLIMBE HASH ENGINE v1.0.0 ]{RESET}
{YELLOW}  [ Custom Cryptographic Function  ]{RESET}
"""

# ══════════════════════════════════════════════════════════
#   CORE HASH FUNCTION
# ══════════════════════════════════════════════════════════

def hashELKOLIMBE(data: str) -> dict:
    """
    Fonction de hachage personnalisée EL-KOLIMBE.
    Algorithme basé sur multiplication polynomiale + XOR + modulo 2^32.
    """
    raw        = str(data).encode("utf-8")
    hash_val   = 0xDEADBEEF          # Seed initial (style hacker)
    prime      = 31
    salt       = 0xC0FFEE            # Salt personnel EL-KOLIMBE

    for i, byte in enumerate(raw):
        hash_val ^= (byte * (prime ** (i + 1))) & 0xFFFFFFFF
        hash_val  = (hash_val + salt) % (2 ** 32)

    # Représentations multiples
    hex_val  = f"0x{hash_val:08X}"
    bin_val  = f"{hash_val:032b}"
    sha_ref  = hashlib.sha256(raw).hexdigest()[:16]   # Référence SHA256

    return {
        "input"    : data,
        "decimal"  : hash_val,
        "hex"      : hex_val,
        "binary"   : bin_val,
        "sha_ref"  : sha_ref,
    }


# ══════════════════════════════════════════════════════════
#   AFFICHAGE
# ══════════════════════════════════════════════════════════

def typing_effect(text: str, delay: float = 0.03):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()


def display_result(result: dict):
    print(f"\n{CYAN}  ┌─────────────────────────────────────────┐{RESET}")
    print(f"{CYAN}  │{RESET} INPUT   : {BOLD}{WHITE}{result['input']:<31}{RESET}{CYAN}│{RESET}")
    print(f"{CYAN}  │{RESET} DECIMAL : {GREEN}{result['decimal']:<31}{RESET}{CYAN}│{RESET}")
    print(f"{CYAN}  │{RESET} HEX     : {YELLOW}{result['hex']:<31}{RESET}{CYAN}│{RESET}")
    print(f"{CYAN}  │{RESET} BINARY  : {RED}{result['binary'][:16]}...{RESET}    {CYAN}│{RESET}")
    print(f"{CYAN}  │{RESET} SHA_REF : {WHITE}{result['sha_ref']:<31}{RESET}{CYAN}│{RESET}")
    print(f"{CYAN}  └─────────────────────────────────────────┘{RESET}")


# ══════════════════════════════════════════════════════════
#   MAIN
# ══════════════════════════════════════════════════════════

def main():
    print(BANNER)
    time.sleep(0.5)

    typing_effect(f"{GREEN}[*] Initialisation du moteur de hachage...{RESET}")
    typing_effect(f"{GREEN}[*] Chargement de l'algorithme EL-KOLIMBE...{RESET}")
    typing_effect(f"{GREEN}[*] Système prêt.{RESET}\n")
    time.sleep(0.3)

    # ── Données de test ───────────────────────────────────
    targets = [
        "EL-KOLIMBE",
        "hello world",
        "python3",
        "cybersecurity",
        "hachage",
        "0xDEADBEEF",
    ]

    print(f"{YELLOW}[>>] Lancement du hachage sur {len(targets)} cibles...{RESET}")
    time.sleep(0.4)

    for target in targets:
        typing_effect(f"\n{CYAN}[~] Hachage de : '{target}'{RESET}", delay=0.02)
        result = hashELKOLIMBE(target)
        display_result(result)
        time.sleep(0.2)

    print(f"\n{GREEN}[✔] Opération terminée avec succès.{RESET}")
    print(f"{RED}[!] EL-KOLIMBE HASH ENGINE — All rights reserved.{RESET}\n")


if __name__ == "__main__":
    main()
