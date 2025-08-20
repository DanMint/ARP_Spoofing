import subprocess


def main():
    with open("./outputs/output.txt", "w") as f:
        proc = subprocess.Popen(
            ["sudo", "netdiscover"],
            stdout=f,
            stderr=subprocess.STDOUT,
            text=True
        )
        proc.wait()

if __name__ == "__main__":
    main()