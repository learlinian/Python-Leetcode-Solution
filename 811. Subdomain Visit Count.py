# runtime: 96%, memory: 24%

class Solution(object):
    def subdomainVisits(self, cpdomains):
        cp_subdomains = {}
        for cpdomain in cpdomains:
            count, domain = cpdomain.split()[0], cpdomain.split()[1]
            subdomains = domain.split('.')
            subdomain = ''
            for i in range(len(subdomains) - 1, -1, -1):
                subdomain = subdomains[i] if i == len(subdomains) - 1 else subdomains[i] + '.' + subdomain
                if subdomain not in cp_subdomains:
                    cp_subdomains[subdomain] = int(count)
                else:
                    cp_subdomains[subdomain] += int(count)

        result = []
        for subdomain, count in cp_subdomains.items():
            result.append(str(count) + " " + subdomain)
        return result


if __name__ == '__main__':
    cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    print(Solution().subdomainVisits(cpdomains))
