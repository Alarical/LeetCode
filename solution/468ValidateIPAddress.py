class Solution:
    def validIPAddress(self, IP: str) -> str:
        ip_list = IP.split('.')
        if len(ip_list) == 4:
            for s in ip_list:
                if not s.isdigit():
                    return 'Neither'
                if 0 <= int(s) <= 255 :
                    if str(int(s)) != s:
                        return 'Neither'
                else:
                    return 'Neither'
            return 'IPv4'

        IPv6 = IP.split(':')
        IPv6len = len(IPv6)
        if IPv6len == 8:
            if "" in IPv6:
                return 'Neither'

            for c in IPv6:
                if len(c) > 4:
                    return 'Neither'
                for a in c:
                    if a.upper() > 'F' or (a.isdigit() == False and a.isalpha() == False):
                        return 'Neither'
            return 'IPv6'
        return 'Neither'