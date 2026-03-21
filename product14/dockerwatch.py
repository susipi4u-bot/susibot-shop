import docker
import time
from datetime import datetime

def get_containers():
    client = docker.from_env()
    return client.containers.list()

def get_container_stats(container):
    try:
        stats = container.stats(stream=False)
        cpu = calculate_cpu_percent(stats)
        mem = stats['memory_stats']['usage'] / 1024 / 1024
        return f"CPU: {cpu:.1f}% | MEM: {mem:.1f}MB"
    except:
        return "N/A"

def calculate_cpu_percent(stats):
    cpu_delta = stats['cpu_stats']['cpu_usage']['total_usage'] - stats['precpu_stats']['cpu_usage']['total_usage']
    system_delta = stats['cpu_stats']['system_cpu_usage'] - stats['precpu_stats']['system_cpu_usage']
    if system_delta > 0:
        return (cpu_delta / system_delta) * len(stats['cpu_stats']['cpu_usage']['percpu_usage']) * 100
    return 0

def main():
    print("📦 DockerWatch Started")
    
    while True:
        try:
            containers = get_containers()
            print(f"\n[{datetime.now()}] {len(containers)} Container")
            for c in containers:
                status = "running" if c.status == "running" else c.status
                stats = get_container_stats(c)
                print(f"  {c.name}: {status} | {stats}")
        except Exception as e:
            print(f"Error: {e}")
        
        time.sleep(30)

if __name__ == "__main__":
    main()