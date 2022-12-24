class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:
        filtered_emails_set = set()

        for e in emails:
            local_name, domain_name = e.split('@')
            local_name = local_name.replace('.', '')
            local_name = local_name.split('+')[0]

            new_email = '@'.join([local_name, domain_name])
            filtered_emails_set.add(new_email)

        return len(filtered_emails_set)

if __name__ =='__main__':
    emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]

    entity = Solution()
    print(entity.numUniqueEmails(emails))