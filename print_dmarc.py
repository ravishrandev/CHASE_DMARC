from tabulate import tabulate

def print_dmarc_table(records):
    if not records:
        print("⚠️ No DMARC records to display.")
        return

    headers = [
        "IP Address", "Email Volume", "Envelope To", "Envelope From",
        "Header From", "DKIM Domain", "DKIM Result", "SPF Result", "DMARC Disposition"
    ]

    rows = [
        [
            r['ip'],
            r['count'],
            r['envelope_to'],
            r['envelope_from'],
            r['header_from'],
            r['dkim_domain'],
            r['dkim_result'],
            r['spf_result'],
            r['disposition'],
        ]
        for r in records
    ]

    print("\n DMARC Report Summary:\n")
    print(tabulate(rows, headers=headers, tablefmt="fancy_grid"))
