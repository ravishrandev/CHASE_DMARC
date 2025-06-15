from tabulate import tabulate

def print_dmarc_table(records):
    if not records:
        print ("⚠️ No DMARC records to display.")
        return
    
    headers = ["IP Address", "Email Volume", "SPF", "DKIM", "DMARC"]
    row = [[r['ip'], r['count'], r['spf'], r['disposition']] for r in records]

    print("\n DMARC Report Summary:\n")
    print(tabulate(row, headers=headers, tablefmt="grid"))

