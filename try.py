#this script write by X-VSOUL-X please credit me
import requests

def check_proxy(proxy):
    try:
        response = requests.get("http://www.google.com", proxies={'http': proxy, 'https': proxy}, timeout=5)
        if response.status_code == 200:
            print(f"Proxy {proxy} is working.")
            return True
    except requests.RequestException:
        pass
    print(f"Proxy {proxy} is not working.")
    return False

def check_and_save_proxies(input_file, output_file):
    working_proxies = []

    try:
        with open(input_file, 'r') as file:
            proxies_list = [line.strip() for line in file.readlines()]

        for proxy in proxies_list:
            if check_proxy(proxy):
                working_proxies.append(proxy)

        # Save working proxies to the output file
        with open(output_file, 'w') as output_file:
            for proxy in working_proxies:
                output_file.write(f"{proxy}\n")

        print(f"Working proxies saved to {output_file}")

    except Exception as e:
        print(f"Error: {e}")

def main():
    # Get user input for the file paths
    input_file = input("Enter the path to the file containing proxy addresses and ports: ")
    output_file = input("Enter the path to save working proxies: ")

    # Check and save proxies
    check_and_save_proxies(input_file, output_file)

if __name__ == "__main__":
    main()
