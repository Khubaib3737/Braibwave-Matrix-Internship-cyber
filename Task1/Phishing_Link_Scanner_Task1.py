import re
from urllib.parse import urlparse  # Used for safely splitting URL into components

# Function to extract suspicious traits from a URL
def extract_features(url):
    """
    Extracts suspicious features from a URL using manual checks.
    Returns a dictionary of boolean or numeric features.
    """
    parsed = urlparse(url)              # Split URL into components
    domain = parsed.netloc              # Extract the domain portion (e.g., www.example.com)

    features = {
        "has_ip": bool(re.search(r'\d{1,3}(\.\d{1,3}){3}', domain)),  # Check if domain is an IP
        "has_at_symbol": '@' in url,                                 # '@' used to mislead users
        "url_length": len(url),                                      # Count total characters
        "has_http": url.startswith("http://"),                       # Not HTTPS → less secure
        "has_double_slash_redirect": url.count("//") > 1,            # Too many slashes may be redirect trick
        "subdomain_count": domain.count('.'),                        # More subdomains → suspicious
        "suspicious_words": any(word in url.lower() for word in [    # Look for common phishing words
            "secure", "account", "update", "login", "verify", "bank", "signin", "urgent"
        ])
    }

    return features

# Function to score the extracted features
def score_features(features):
    """
    Scores the URL based on how many suspicious features are found.
    Returns a number between 0 and 7.
    """
    score = 0
    for key, value in features.items():
        if isinstance(value, bool) and value:
            score += 1
        elif key == "url_length" and value > 75:
            score += 1
        elif key == "subdomain_count" and value >= 3:
            score += 1
    return score

# Function to show the results on screen and save to file if needed
def print_and_save_report(url, features, score, output_file=None):
    """
    Prints the report of URL analysis to the console.
    Optionally saves the same report to an output file.
    """
    verdict = "Phishing Likely" if score >= 3 else "URL Seems Safe"

    # Prepare all lines for output
    result_lines = [
        f"\n[+] Scanning: {url}",
        f" - has_ip: {features['has_ip']}",
        f" - has_at_symbol: {features['has_at_symbol']}",
        f" - url_length: {features['url_length']}",
        f" - has_http: {features['has_http']}",
        f" - has_double_slash_redirect: {features['has_double_slash_redirect']}",
        f" - subdomain_count: {features['subdomain_count']}",
        f" - suspicious_words: {features['suspicious_words']}",
        f"[!] Final Verdict: {verdict} (Score: {score}/7)"
    ]

    # Display on console
    for line in result_lines:
        print(line)

    # Save to file if requested
    if output_file:
        with open(output_file, 'a') as f:
            for line in result_lines:
                f.write(line + '\n')

# Scan a single URL via console input
def analyze_single_url():
    """
    Asks the user for a URL, analyzes it, and prints results.
    """
    url = input("Enter a URL to scan: ").strip()
    features = extract_features(url)
    score = score_features(features)
    print_and_save_report(url, features, score)

# Scan multiple URLs from a .txt file
def input_file():
    """
    Asks for a file path, reads URLs, and saves the report to a file.
    """
    input_file = input("Enter input file path (.txt): ").strip()
    output_file = "output_report.txt"  # Output filename

    try:
        with open(input_file, 'r') as f:
            urls = [line.strip() for line in f if line.strip()]  # Remove empty lines .strip()
    except FileNotFoundError:
        print("File not found.")
        return

    print(f"\n== Scanning {len(urls)} URLs from file ==\nResults will be saved to '{output_file}'")

    # Clear previous content in the output file
    open(output_file, 'w').close()

    # Analyze each URL one by one
    for url in urls:
        features = extract_features(url)
        score = score_features(features)
        print_and_save_report(url, features, score, output_file)

# Main menu
def main():
    """
    Entry point: asks the user whether to scan one URL or many from a file.
    """
    print("== Phishing Link Scanner ==")
    print("1. Scan a single URL")
    print("2. Scan multiple URLs from a file")
    choice = input("Choose (1 or 2): ").strip()

    if choice == '1':
        analyze_single_url()
    elif choice == '2':
        input_file()
    else:
        print("Invalid choice. Exiting.")

# Run the program
if __name__ == "__main__":
    main()
