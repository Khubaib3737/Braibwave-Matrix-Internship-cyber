# 🦠 Malware Detector

A simple Python script to scan a file for common malware indicators.  
It checks for:
- Known malware hashes.
- Suspicious Unicode RTLO characters in filename (extension spoofing).
- Mismatch between file extension and magic number (file signature).

## 📂 Features

✅ Detects file type by magic number (signature)  
✅ Checks if file extension matches detected type  
✅ Warns if suspicious RTLO character is present in filename  
✅ Compares file hash (MD5) against known malware hashes  
✅ Prints a detailed scan report with a final verdict

## 🚀 Usage

### Requirements
- Python 3.x

No additional libraries are required (uses only Python standard library).

### Run the script

```bash
python malware_detector.py
```

You will be prompted to enter the path of the file to scan:
```bash
== 🦠 Malware Detection Script ==
Enter file path to scan: /path/to/your/file.exe
```

The script will analyze the file and print a scan report like this:
```bash
================= 🦠 Malware Scan Report =================
📄 File: /path/to/your/file.exe
===========================================================
🔍 Detected file type (by signature): EXE (MZ)
✅ File extension matches detected content type
🔑 MD5 Hash: 44d88612fea8a8f36de82e1278abb02f

⚠️ Detected Issues:
 - 🚨 Hash matches known malware signature

===========================================================
🏁 Final Verdict: 🚨 Malware detected!
===========================================================
```
