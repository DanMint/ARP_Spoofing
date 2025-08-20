import re

input_file = "./outputs/output.txt"
output_file = "./outputs/unique_hosts.txt"

def get_unique_data():
    row_re = re.compile(
    r"(?P<ip>\d{1,3}(?:\.\d{1,3}){3})\s+"
    r"(?P<mac>[0-9a-f:]{17}|[0-9a-f:]{2,})\s+"
    r"(?P<count>\d+)\s+"
    r"(?P<len>\d+)\s+"
    r"(?P<vendor>.+)",
    re.IGNORECASE
    )

    hosts = {}

    with open(input_file) as f:
        for line in f:
            m = row_re.search(line)
            if m:
                ip = m.group("ip")
                hosts[ip] = {
                    "mac": m.group("mac"),
                    "count": m.group("count"),
                    "len": m.group("len"),
                    "vendor": m.group("vendor").strip()
                }

    with open(output_file, "w") as out:
        out.write(f"{'IP':<15} {'MAC Address':<20} {'Count':<6} {'Len':<6} Vendor\n")
        out.write("-" * 80 + "\n")
        for ip, data in hosts.items():
            out.write(f"{ip:<15} {data['mac']:<20} {data['count']:<6} {data['len']:<6} {data['vendor']}\n")

    print(f"Wrote {len(hosts)} unique hosts to {output_file}")

def main():
    get_unique_data()
    

if __name__ == "__main__":
    main()