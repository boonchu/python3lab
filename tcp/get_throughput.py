#! /usr/bin/env python3

import sys
import dpkt

def Bps_to_Mbps(val):
    """ convert bytes/sec to Mbits/sec   """
    return (val*8)/(1000*1000)

def print_results(data):
    interval = 1
    for connections in data.keys():

        sum_prev = total_sum = 0; 
        prev_time = start_time = data[connections][0][0]
        for packet in data[connections]:

            total_sum = total_sum + packet[1]    
            if(start_time != packet[0]):
                if( (packet[0] - prev_time) >= 1):
                    sys.stdout.write(" " + str( Bps_to_Mbps(float((total_sum -sum_prev)/(packet[0] -prev_time)))))
                    prev_time = packet[0]
                    sum_prev = total_sum
        sys.stdout.write("\n")

def main():
    data={}
    f = open(sys.argv[1])
    pcap = dpkt.pcap.Reader(f)
    
    start = 0
    for ts, buf in pcap:
        eth = dpkt.ethernet.Ethernet(buf)
        ip = eth.data
        tcp = ip.data


        """ I don't care about the 0 length ACK packets """
        if (ip.len > 52):
            entry = (tcp.dport, tcp.sport)
            if entry not in data:
                data[entry] = []
            data[entry].append( (ts, ip.len-52) )

    print_results(data)
        
if __name__=="__main__":
    main()

