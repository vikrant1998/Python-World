class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        emailSet = set()
        for email in emails:
            localName, domainName = email.split('@')[0], email.split('@')[1]
            localName = localName.replace(".", "")
            localName = localName.split('+')[0]
            emailSet.add(localName + '@' + domainName)

        return len(emailSet)

if __name__ == "__main__":
    s = Solution()
    emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    s.numUniqueEmails(emails)
