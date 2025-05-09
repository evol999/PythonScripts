from flask import Flask, Response
import json
from collections import OrderedDict

app = Flask(__name__)

@app.route('/dhsv2/acquirers/HAR/merchants/982600045/dccoffers', methods=['GET'])
def get_dcc_offers():
    response = OrderedDict([
        ("uuid", "a140fc20-0d30-4f58-a714-a4ce6b3c6ec2"),
        ("baseAmount", "155.00"),
        ("exchangeRate", OrderedDict([
            ("uuid", "e8284604-6b00-419a-a109-e50aa54377b1"),
            ("baseCurrency", OrderedDict([
                ("alphaCode", "GBP"),
                ("minorUnits", 2),
                ("numericCode", "826")
            ])),
            # ("rate", "0.4037"),
            ("rate", "0.9997"),
            ("foreignCurrency", OrderedDict([
                # ("alphaCode", "KWD"),
                ("alphaCode", "EUR"),
                ("minorUnits", 3),
                ("numericCode", "414")
            ])),
            ("marginPercentage", "2.95"),
            ("commissionPercentage", "0.000000"),
            ("source", "REUTERS WHOLESALE INTERBANK"),
            ("sourceTimestamp", "2025-03-04T10:28:34.000+0000"),
            ("expiry", "2026-03-04T10:28:34.000+0000")
        ])),
        # ("foreignAmount", "62.574"),
        ("foreignAmount", "55.555"),
        ("bin", OrderedDict([
            ("number", "4417768190"),
            ("currency", OrderedDict([
                # ("alphaCode", "KWD"),
                ("alphaCode", "EUR"),
                ("minorUnits", 3),
                ("numericCode", "414")
            ])),
            ("schemeCode", 1)
        ]))
    ])
    
    return Response(
        json.dumps(response, indent=4, sort_keys=False),
        mimetype='application/json'
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)