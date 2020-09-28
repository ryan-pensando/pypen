def quickstart_create_flow_export_policy(psm_ip, session):

    #todo add params into dict - ,source, dest, protoport, flow_dest, flow_dest_port

    url = psm_ip + 'configs/monitoring/v1/flowExportPolicy'
    data = """
    {
  "kind": "FlowExportPolicy",
  "api-version": "v1",
  "meta": {
    "name": "ipfix-export",
    "tenant": "default",
    "namespace": "default",
    "self-link": "/configs/monitoring/v1/tenant/default/flowExportPolicy/ipfix-export"
  },
  "spec": {
    "interval": "10s",
    "template-interval": "5m",
    "format": "ipfix",
    "match-rules": [
      {
        "source": {
          "ip-addresses": [
            "172.16.0.1"
          ]
        },
        "destination": {
          "ip-addresses": [
            "172.16.0.2"
          ]
        },
        "app-protocol-selectors": {
          "proto-ports": [
            "icmp"
          ]
        }
      }
    ],
    "exports": [
      {
        "destination": "192.168.68.138",
        "transport": "udp/4739"
      }
    ]
  }
}
"""
    rdata = session.post(url, data)
    if rdata.status_code==200:
        return "Quickstart environment successfully installed here are the details" + str(rdata.json())
    elif rdata.status_code==409:
        return "Quickstart code returned an error - is environment already installed?"