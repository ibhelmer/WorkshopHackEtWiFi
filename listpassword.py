import subprocess
import re

def run_cmd(cmd):
    result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
    return result.stdout

def get_wifi_profiles():
    output = run_cmd("netsh wlan show profiles")
    profiles = re.findall(r"All User Profile\s*:\s*(.*)", output)
    return [p.strip() for p in profiles]

def get_wifi_password(profile):
    output = run_cmd(f'netsh wlan show profile name="{profile}" key=clear')
    match = re.search(r"Key Content\s*:\s*(.*)", output)
    if match:
        return match.group(1).strip()
    return "Ingen password gemt"

def main():
    profiles = get_wifi_profiles()

    print("\nGemte Wi-Fi netværk i Windows\n")
    print("{:<30} {}".format("SSID", "Password"))
    print("-"*50)

    for profile in profiles:
        password = get_wifi_password(profile)
        print("{:<30} {}".format(profile, password))

if __name__ == "__main__":
    main()