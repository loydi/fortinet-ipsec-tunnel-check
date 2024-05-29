#!/usr/bin/env python3
#
# date   : 29.05.2024
# authot : Kemal Yildirim
import sys
import argparse
from easysnmp import Session

#GLOBAL VERIABLES for FORTIGATE 
oid_IPSEC_NAME_TABLE =".1.3.6.1.4.1.12356.101.12.2.2.1.2"
oid_IPSEC_STATUS =".1.3.6.1.4.1.12356.101.12.2.2.1.20"

def parseArgs():
    # Parse arguments and display help
    parser = argparse.ArgumentParser(description='This plugin checks all configured IPSEC tunnels, and gives the number of current IPSEC tunnels and SSL-VPN tunnels.')
    parser.add_argument('-H', help='STRING or IPADDRESS', default="127.0.0.1")
    parser.add_argument('-C', help='Community STRING', default="public")
    parser.add_argument('-M', help='Modus default = 2', default="2")
    parser.add_argument('-F', help='performance data output')
    args = parser.parse_args()
    return args

def create_snmp_session(ip, community):
    try:
        session = Session(hostname=ip, community=community, version=2)  # SNMP version 2c
        return session
    except Exception as e:
        print(f"Error creating SNMP session: {e}")
        return None
def get_snmp_value(session, oid):
    try:
        result = session.get(oid)
        return result.value
    except Exception as e:
        print(f"SNMP error: {e}")
        return None
def get_snmp_table(session, oid):
    try:
        results = session.walk(oid)
        return [(result.oid, result.value) for result in results]
    except Exception as e:
        print(f"SNMP error: {e}")
        return None

def main():
    args = parseArgs()
    snmp_session = create_snmp_session(args.H,args.C)
    P_TUNE_NAME = get_snmp_table(snmp_session,oid_IPSEC_NAME_TABLE)
    P_STATUS = get_snmp_table(snmp_session,oid_IPSEC_STATUS)

    # TO DO
    # SSL VPN Checks
    # Output options for monitoring system such as only down or up tunnels
  
    output_list = []
    for i in range(len(P_TUNE_NAME)):
        if P_STATUS[i][1] == '1':
            output_list.append({
                    'IPSEC NAME': P_TUNE_NAME[i][1],
                    'IPSEC STATUS': "DOWN",
                    'IPSEC VALUE' : P_STATUS[i][1]
                })
        else:
            output_list.append({
                    'IPSEC NAME': P_TUNE_NAME[i][1],
                    'IPSEC STATUS': "UP",
                    'IPSEC VALUE' : P_STATUS[i][1]
                })

    for item in output_list:
        print(f"{item['IPSEC NAME']} : ({item['IPSEC STATUS']}) | '{item['IPSEC NAME']}'={item['IPSEC VALUE']};;;; ")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
    except EOFError:
        sys.exit()
