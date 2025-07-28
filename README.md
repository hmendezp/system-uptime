## Main Target of `print_uptime.py`

This Python script determines and prints the system uptime in a human-readable format, supporting both Unix-like and Windows systems.

### How it Works

- **Platform Detection:**  
  The script checks the operating system using `platform.system()`.

- **Unix-like Systems:**
  - Tries to read uptime from `/proc/uptime`.
  - If unavailable, falls back to using the `uptime -s` command to get the system boot time and calculates uptime.

- **Windows Systems:**
  - Uses the `net stats srv` command and parses the output line containing "Statistics since" to get the system boot time, then calculates uptime.

- **Formatting:**  
  The uptime (in seconds) is formatted into days, hours, minutes, and seconds.

- **Output:**  
  Prints the formatted system uptime. If uptime cannot be determined, an error message is shown.

---

**Entry Point:**  
If run as a script, it executes the `main()` function to perform the above logic.
