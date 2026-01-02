# fincheck

**fincheck** adalah CLI tool berbasis API untuk membantu validasi akun bank dan e-wallet. Tool ini ditujukan untuk keperluan pengujian, riset, dan edukasi, serta digunakan secara legal dan etis.

---

## Preview

<p align="center">
  <img src="https://raw.githubusercontent.com/ilhamrzr/fincheck/main/assets/preview.png" alt="fincheck preview" width="720">
</p>

---

## Features

- Bank account checker
- E-Wallet account checker
- Bulk checking from file
- Dry-run mode
- Request control (delay & timeout)
- Endpoint selector
- JSON & text output

---

## Supported Providers

Daftar bank dan e-wallet yang didukung oleh **fincheck** didefinisikan secara statis
pada file konfigurasi berikut:

- **Banks**  
  [`config/banks.py`](config/banks.py)

- **E-Wallets**  
  [`config/ewallets.py`](config/ewallets.py)

File tersebut berisi mapping kode provider yang digunakan oleh perintah
`list`, `bank`, `ewallet`, dan `bulk`.

Perubahan pada file ini ditujukan untuk kebutuhan pengembangan
atau penggunaan internal.

---

## Installation

```bash
git clone https://github.com/ilhamrzr/fincheck.git
cd fincheck
chmod +x fincheck
```

---

## Usage

```bash
./fincheck -h

usage: fincheck [-h] [--version] [--api-key API_KEY] [--json] [-v] [-d DELAY] [-t TIMEOUT] [--endpoint {primary,mirror1,mirror2}] [--dry-run]
                [-o OUTPUT]
                {list,bank,ewallet,bulk,gen-bulk} ...

FINCHECK — Financial Intelligence Account Checker

positional arguments:
  {list,bank,ewallet,bulk,gen-bulk}
    list                Show supported banks and e-wallets
    bank                Check bank account
    ewallet             Check e-wallet account
    bulk                Bulk check from file
    gen-bulk            Generate bulk list template

options:
  -h, --help            show this help message and exit
  --version             Show version
  --api-key API_KEY     API key (optional / required for bulk)
  --json                Output JSON format
  -v, --verbose         Verbose output
  -d, --delay DELAY     Delay between bulk requests (sec)
  -t, --timeout TIMEOUT
                        Request timeout (sec)
  --endpoint {primary,mirror1,mirror2}
  --dry-run             Simulate without API call
  -o, --output OUTPUT   Save result summary to a text file
```

---

## Commands

| Command    | Description                      |
| ---------- | -------------------------------- |
| `list`     | show supported banks & e-wallets |
| `bank`     | check bank account               |
| `ewallet`  | check e-wallet account           |
| `bulk`     | bulk check from file             |
| `gen-bulk` | generate bulk template           |

---

## Catatan API Key

- **Bulk mode membutuhkan API key**

- `--dry-run` dapat digunakan tanpa API key

- API key **tidak disimpan** oleh tool

---

## ⚠️ Disclaimer

Tool ini:

- Hanya untuk penggunaan **legal & etis**

- Ditujukan untuk **edukasi dan riset**

- Akurasi bergantung pada API provider

Developer **tidak bertanggung jawab atas penyalahgunaan**.

---

## 🙏 Special Thanks

**API Provider**
Restu Fadhilah
[https://www.facebook.com/restugbk/](Restu Fadhilah)

---

## ☕ Support

[![☕ Trakteer](https://img.shields.io/badge/☕%20Trakteer-red?style=flat-square&logo=coffee&logoColor=white)](https://trakteer.id/ilhamrzr)
[![☕ Saweria](https://img.shields.io/badge/☕%20Saweria-6f4e37?style=flat-square&logo=coffee&logoColor=white)](https://saweria.co/ilhamrzr)

---

## 📄 License

MIT License

---

## 👨‍💻 Author

**Ilham**
GitHub: https://github.com/ilhamrzr
