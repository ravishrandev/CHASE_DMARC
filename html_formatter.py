def generate_html_table (records):
    if not records:
        return "<p>No DMARC records exist to display</p>"
    
    html= """
    <html>
    <head>
        <style>
            table {
                width: 100%;
                border-collapse: collapse;
                font-family: Arial, sans-serif;
            }
            th, td {
                border: 1px solid #ccc;
                padding: 8px;
                text-align: left;
            }
            th {
                background-color: #f2f2f2;
            }
        </style>
    </head>
    <body>
        <h2>DMARC Weekly Summary</h2>
        <table>
            <thead>
                <tr>
                    <th>Source IP</th>
                    <th>Count</th>
                    <th>Envelope To</th>
                    <th>Envelope From</th>
                    <th>Header From</th>
                    <th>DKIM Domain</th>
                    <th>DKIM Result</th>
                    <th>SPF Result</th>
                    <th>Disposition</th>
                </tr>
            </thead>
            <tbody>
    """

    for record in records:
        html += f"""
        <tr>
            <td>{record.get('ip', '')}</td>
            <td>{record.get('count', '')}</td>
            <td>{record.get('envelope_to', '')}</td>
            <td>{record.get('envelope_from', '')}</td>
            <td>{record.get('header_from', '')}</td>
            <td>{record.get('dkim_domain', '')}</td>
            <td>{record.get('dkim_result', '')}</td>
            <td>{record.get('spf_result', '')}</td>
            <td>{record.get('disposition', '')}</td>
        </tr>
    """
        
    html += """
            </tbody>
        </table>
    </body>
    </html>
    """
    return html