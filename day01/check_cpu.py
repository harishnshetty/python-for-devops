import psutil

def check_cpu_threshold():
    check_cpu_threshold = int(input("Enter the CPU threshold: "))
    current_cpu_usage = psutil.cpu_percent()
    print("Current CPU usage:", current_cpu_usage)
    if current_cpu_usage > check_cpu_threshold:
        print("CPU usage is above threshold")
    else:
        print("CPU usage is below threshold")

check_cpu_threshold()