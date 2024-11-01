import glob

DEFAULT_ENTRIES = [
    "Deletable true",
    "Format EX509Certificate",
    "CertOwnerType ECACertificate",
    "SubjectKeyId auto",
    "StartApplicationList",
    "EndApplicationList",
    "Trusted true",
]


def indentate(n: int, input: str) -> str:
    return " " * n + input + "\n"


def gen_entry_str(cert_file: str, cert_num: int) -> str:
    cert_name = cert_file.split(".")[0]
    cert_label = f"{cert_num}_{cert_name[:60]}"
    output = indentate(2, f'StartEntry "{cert_label}"')
    for entry in DEFAULT_ENTRIES:
        output += indentate(4, entry)
    output += indentate(4, f'DataFileName "{cert_file}"')
    output += indentate(2, "EndEntry")
    return output


with open("cacerts.txt", "w") as f:
    f.write("StartCertStoreEntries")
    cert_num = 0
    for cert_path in glob.glob("*.pem"):
        f.write(gen_entry_str(cert_path, cert_num))
        cert_num += 1
    f.write("EndCertStoreEntries")
