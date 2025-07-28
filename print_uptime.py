import platform
import subprocess
import sys
import time
import os

def get_uptime_unix():
    try:
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            return uptime_seconds
    except Exception:
        # fallback to 'uptime -s' if /proc/uptime is not available
        try:
            output = subprocess.check_output(['uptime', '-s']).decode().strip()
            boot_time = time.mktime(time.strptime(output, "%Y-%m-%d %H:%M:%S"))
            uptime_seconds = time.time() - boot_time
            return uptime_seconds
        except Exception:
            return None

def get_uptime_windows():
    try:
        # 'net stats srv' output has a line "Statistics since MM/DD/YYYY HH:MM:SS AM/PM"
        output = subprocess.check_output("net stats srv", shell=True).decode(errors='ignore')
        for line in output.split('\n'):
            if "Statistics since" in line:
                from datetime import datetime
                boot_time = line.strip().split("since")[1].strip()
                try:
                    boot_dt = datetime.strptime(boot_time, "%m/%d/%Y %I:%M:%S %p")
                except ValueError:
                    boot_dt = datetime.strptime(boot_time, "%d/%m/%Y %H:%M:%S")
                uptime_seconds = (datetime.now() - boot_dt).total_seconds()
                return uptime_seconds
    except Exception:
        return None

def format_uptime(seconds):
    seconds = int(seconds)
    days = seconds // (24 * 3600)
    seconds %= (24 * 3600)
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return f"{days}d {hours}h {minutes}m {seconds}s"

def main():
    system = platform.system()
    if system == 'Windows':
        uptime = get_uptime_windows()
    else:
        uptime = get_uptime_unix()
    if uptime is None:
        print("Could not determine uptime.")
        sys.exit(1)
    print(f"System Uptime: {format_uptime(uptime)}")

if __name__ == "__main__":
    main()