#!/usr/bin/python

# cymru_filter.py
# http://www.dnspython.org/examples.html

# requires dnspython
# pip install dnspython

import dns.resolver
import re
import sys

def parse_txt_rec(result, pos):
    ans = []
    for rdata in result:
      for s in rdata.strings:
        a = s.split(" | ")
        ans.append(a[pos])
    return ans

def find_asn_helper(matchobj):
    return "(" + find_asn(matchobj.group(1)) + ")"

def find_asn(ipv4_addr):
    if not re.match('^\d+\.\d+\.\d+\.\d+$', ipv4_addr):
      return ipv4_addr

    rev_ipv4_addr = ".".join(ipv4_addr.split(".")[::-1])

    try:
      asnum_answers = dns.resolver.query(rev_ipv4_addr + '.origin.asn.cymru.com', 'TXT')
    except:
      return ipv4_addr

    asn_list = parse_txt_rec(asnum_answers, 0)

    asn = asn_list[0]
    if re.match('^\d+$', asn):
      try: asname_answers = dns.resolver.query("AS" + asn + ".asn.cymru.com", 'TXT')
      except:
        return ipv4_addr
      asname_list = parse_txt_rec(asname_answers, 4)
      return ipv4_addr + "; " + asname_list[0]
    else:
      return ipv4_addr

for line in sys.stdin:
  line = re.sub('\((\d+\.\d+\.\d+\.\d+)\)', find_asn_helper, line)
  print line,
