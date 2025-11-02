Perfect 👍 — let’s now **connect Bash scripting to networking** — just like you learned Python basics for networking.

We'll do this step-by-step:

---

## 🧠 Overview: Why Bash in Networking

Bash isn’t like Python (no classes, no imports, no complex data structures).
It’s **command-centric** — its power comes from automating and chaining Linux networking tools (ping, netstat, ifconfig, etc.).

So Bash is perfect for:

* Automating network diagnostics
* Monitoring network health
* Managing logs
* Running repetitive CLI commands across many devices

---

## ⚙️ Section 1: Essential Networking Commands You’ll Use in Bash

| Command           | Description                 | Example                               |
| ----------------- | --------------------------- | ------------------------------------- |
| `ping`            | Check if host is reachable  | `ping -c 4 google.com`                |
| `traceroute`      | Show the path packets take  | `traceroute google.com`               |
| `curl`            | Fetch a webpage or API data | `curl https://example.com`            |
| `wget`            | Download files              | `wget https://example.com/file.zip`   |
| `ifconfig` / `ip` | Show interface info         | `ifconfig` or `ip a`                  |
| `netstat`         | View network connections    | `netstat -tulnp`                      |
| `ss`              | Newer version of `netstat`  | `ss -tuln`                            |
| `dig`             | Query DNS servers           | `dig google.com`                      |
| `nslookup`        | DNS lookup tool             | `nslookup google.com`                 |
| `scp`             | Copy files over SSH         | `scp file.txt user@192.168.1.1:/tmp/` |
| `ssh`             | Connect to remote servers   | `ssh user@server`                     |
| `nc` (netcat)     | Test open ports             | `nc -zv google.com 80`                |
| `arp`             | View ARP table              | `arp -n`                              |

---

## 🧩 Section 2: Bash Networking Basics – Scripting Examples

### 🖥️ Example 1: Ping Sweep (Find live hosts in a network)

```bash
#!/bin/bash
# ping_sweep.sh
# Usage: ./ping_sweep.sh 192.168.1

for ip in {1..254}; do
    ping -c 1 -W 1 $1.$ip &> /dev/null
    if [ $? -eq 0 ]; then
        echo "Host $1.$ip is up"
    else
        echo "Host $1.$ip is down"
    fi
done
```

**Run:**

```bash
chmod +x ping_sweep.sh
./ping_sweep.sh 192.168.1
```

✅ Scans all IPs from `192.168.1.1` to `192.168.1.254` and reports which are alive.

---

### 📡 Example 2: Port Scanner (using Netcat)

```bash
#!/bin/bash
# port_scan.sh
# Usage: ./port_scan.sh 192.168.1.1

target=$1
for port in {1..1024}; do
    nc -zv -w 1 $target $port &> /dev/null
    if [ $? -eq 0 ]; then
        echo "Port $port is open on $target"
    fi
done
```

✅ Checks the first 1024 ports on a given host.

---

### 🧠 Example 3: Network Monitoring Script

```bash
#!/bin/bash
# monitor_net.sh

while true; do
    echo "Checking connection to 8.8.8.8..."
    ping -c 1 8.8.8.8 > /dev/null 2>&1

    if [ $? -eq 0 ]; then
        echo "$(date): Internet is up"
    else
        echo "$(date): Internet is down"
    fi
    sleep 10
done
```

✅ Continuously checks if the system can reach Google DNS every 10 seconds.

---

### 🧩 Example 4: Log Network Usage

```bash
#!/bin/bash
# log_net_usage.sh

logfile="/tmp/net_usage.log"
echo "Recording network traffic to $logfile..."
echo "Interface  RX(bytes)  TX(bytes)" > $logfile

while true; do
    ifconfig eth0 | awk '/RX p/{rx=$5} /TX p/{tx=$5} END{print "eth0",rx,tx}' >> $logfile
    sleep 5
done
```

✅ Records RX/TX byte counts for interface `eth0` every 5 seconds.

---

### 🔍 Example 5: DNS Check Automation

```bash
#!/bin/bash
# dns_check.sh
# Usage: ./dns_check.sh domain.com

domain=$1
result=$(dig +short $domain)

if [ -n "$result" ]; then
    echo "Domain $domain resolves to $result"
else
    echo "Domain $domain does not resolve!"
fi
```

---

## ⚙️ Section 3: Useful Bash Concepts for Networking Scripts

| Concept          | Purpose                     | Example                          |
| ---------------- | --------------------------- | -------------------------------- |
| **Variables**    | Store IPs, ports, etc.      | `ip="192.168.1.1"`               |
| **Conditionals** | Check ping success          | `if [ $? -eq 0 ]; then ... fi`   |
| **Loops**        | Iterate IPs or ports        | `for i in {1..254}; do ... done` |
| **Functions**    | Reuse scanning logic        | `function scan_port() { ... }`   |
| **Redirects**    | Save output to file         | `>> log.txt`                     |
| **`$?`**         | Return code of last command | `if [ $? -eq 0 ]`                |
| **`$(command)`** | Capture output              | `ip=$(hostname -I)`              |
| **Cron Jobs**    | Automate network scripts    | `crontab -e`                     |

---

## 📘 Section 4: Example — Full Diagnostic Script

```bash
#!/bin/bash
# network_diagnostics.sh

host="8.8.8.8"
log="net_diag.log"

echo "Starting network diagnostics..." > $log
echo "Timestamp: $(date)" >> $log

# Check internet
if ping -c 1 $host &> /dev/null; then
    echo "Internet is reachable" >> $log
else
    echo "No internet connectivity" >> $log
fi

# Check DNS
dns_ip=$(dig +short google.com | head -n 1)
if [ -n "$dns_ip" ]; then
    echo "DNS is working: google.com -> $dns_ip" >> $log
else
    echo "DNS resolution failed!" >> $log
fi

# Show top 5 connections
echo "Active connections:" >> $log
netstat -tunapl | head -n 5 >> $log

echo "Diagnostics saved to $log"
```

✅ Run:

```bash
chmod +x network_diagnostics.sh
./network_diagnostics.sh
```

---

## 🧭 Section 5: How Bash Differs from Python

| Feature        | Bash                                | Python                             |
| -------------- | ----------------------------------- | ---------------------------------- |
| Syntax         | Command-based                       | Object-oriented                    |
| Use case       | Automating CLI, text manipulation   | Complex logic, APIs, data analysis |
| Data types     | Strings, arrays, associative arrays | Lists, dicts, classes              |
| Error handling | Simple exit codes (`$?`)            | `try/except` blocks                |
| Networking use | Wrapping Linux tools                | Using `socket`, `requests`, etc.   |
| Speed          | Fast for small scripts              | Better for complex apps            |

**In networking:**

* Use **Bash** for automation, configuration, and quick checks.
* Use **Python** for complex analysis (packet manipulation, APIs, automation frameworks).

---

Would you like me to continue by showing **a Bash + Python hybrid example** (where Bash runs system commands and Python parses results — a real-world network admin combo)?
