# 🛡️ Phishing Link Scanner — Task 1

A lightweight Python tool built for the **Brainwave Cybersecurity Internship**, this script analyzes and detects potentially malicious or phishing URLs using simple heuristics — without relying on APIs or external services.

---

## 🚀 Features

- Analyze a **single URL** via console input  
- Analyze **multiple URLs** from a `.txt` file  
- Detects:
  - IP-based URLs
  - Obfuscation via `@` symbol
  - Suspicious keywords (e.g., `login`, `verify`, `secure`)
  - Unsecure `http://` usage
  - Long URLs
  - Hidden redirects using `//`
  - Too many subdomains  
- Outputs results to both **console** and **`output_report.txt`**  
- Minimal dependencies — built using only Python’s standard library  

---

## 📁 Files

- `Phishing_Link_Scanner_Task1.py` → Main phishing detection script  
- `urls.txt` → (Optional) Input file with one URL per line  
- `output_report.txt` → Output file generated during file-based scan  

---

## 🧰 Requirements

- Python 3.x  
- No third-party libraries required  

---

## 🖥️ How to Use

To run the script, open your terminal (Command Prompt or PowerShell), navigate to the folder containing the file, and type:

`python Phishing_Link_Scanner_Task1.py`

You’ll see a prompt:

== Phishing Link Scanner ==

Scan a single URL

Scan multiple URLs from a file
Choose (1 or 2):


If you enter `1`, it will ask:

`Enter a URL to scan:`

You can input something like:

`http://login-secure-paypal.com`

It will analyze the URL and display results directly in the console.

If you enter `2`, it will ask:

`Enter input file path (.txt):`

You can type:

`urls.txt`

Make sure `urls.txt` contains one URL per line, like:
http://example.com
http://login-secure.paypal.com
https://www.google.com
http://192.168.0.1/login



The tool will scan each URL, print results in the console, and also save them to `output_report.txt` in the same directory.

---

## 💡 Scoring Logic

Each URL is scored from 0 to 7 based on the following suspicious features:

| Feature                     | Description                                      |
|-----------------------------|--------------------------------------------------|
| `has_ip`                   | Raw IP address in domain                         |
| `has_at_symbol`            | `@` symbol used to mislead users                 |
| `url_length`               | Length > 75 characters                           |
| `has_http`                 | Uses `http://` instead of `https://`             |
| `has_double_slash_redirect`| Too many `//` (e.g., redirect tricks)            |
| `subdomain_count`          | 3 or more subdomains                             |
| `suspicious_words`         | Phishing-related keywords (login, bank, etc.)    |

### Verdict:
- **Score ≥ 3** → ⚠️ Phishing Likely  
- **Score < 3** → ✅ URL Seems Safe

---

## 📦 Convert to .exe (Optional)

If you want to run the tool as a Windows executable (.exe) without Python installed:

1. Install PyInstaller by running: `pip install pyinstaller`  
2. Open terminal in the script directory and run:  
   `pyinstaller --onefile --console Phishing_Link_Scanner_Task1.py`  
3. After it finishes, your `.exe` file will be located in the `dist/` folder as:  
   `dist/Phishing_Link_Scanner_Task1.exe`

Double-click it or run it in terminal like any normal program.

---

## 📜 License

This project is for **educational and ethical use only**.  
Do not use it to scan or analyze URLs without proper authorization.

---

## 🙋‍♂️ Author

Developed as part of the **Brainwave Cybersecurity Internship — Task 1**  
Suggestions, improvements, and forks are always welcome!
