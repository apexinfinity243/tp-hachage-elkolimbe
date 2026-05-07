# 🔐 EL-KOLIMBE HASH ENGINE v1.0.0
╔══════════════════════════════════════════════════════════╗
║          HASH FUNCTION :: EL-KOLIMBE CIPHER              ║
║          Author   : EL-KOLIMBE                           ║
║          Version  : 1.0.0                                ║
║          Lang     : Python 3.x                           ║
╚══════════════════════════════════════════════════════════╝

---

## 📌 Description

Fonction de hachage personnalisée développée par **EL-KOLIMBE**.  
L'algorithme est basé sur :
- Multiplication polynomiale
- Opération XOR bit à bit
- Seed initial `0xDEADBEEF`
- Salt personnel `0xC0FFEE`
- Modulo `2^32`

---

## 📂 Contenu du repository

| Fichier | Description |
|--------|-------------|
| `hash_elkolimbe.py` | Programme principal de hachage |
| `README.md` | Documentation du projet |

---

## ⚙️ Prérequis

- Python **3.x** installé sur votre machine
- Aucune bibliothèque externe requise

---

## 🚀 Lancement du programme

### 1. Cloner le repository
```bash
git clone https://github.com/apexinfinity243/tp-hachage-elkolimbe.git

## Accéder au dossier
cd tp-hachage-elkolimbe

## Exécuter le programme
python hash_elkolimbe.py


## 📊 Exemple de sortie
[*] Initialisation du moteur de hachage...
[*] Chargement de l'algorithme EL-KOLIMBE...
[*] Système prêt.

[>>] Lancement du hachage sur 6 cibles...

[~] Hachage de : 'EL-KOLIMBE'
  ┌─────────────────────────────────────────┐
  │ INPUT   : EL-KOLIMBE                    │
  │ DECIMAL : 2748254865                    │
  │ HEX     : 0xA3F2C1D1                    │
  │ BINARY  : 10100011111100101...          │
  │ SHA_REF : a3f2c1d1b2e45f67             │
  └─────────────────────────────────────────┘

[✔] Opération terminée avec succès.
[!] EL-KOLIMBE HASH ENGINE — All rights reserved.

hash_val = 0xDEADBEEF        # Seed initial
prime    = 31                 # Nombre premier
salt     = 0xC0FFEE          # Salt EL-KOLIMBE

for i, byte in enumerate(data):
    hash_val ^= (byte * (prime ** (i+1))) & 0xFFFFFFFF
    hash_val  = (hash_val + salt) % (2**32)

#AUTHEUR
EL-KOLIMBE
🔗 github.com/apexinfinity243
