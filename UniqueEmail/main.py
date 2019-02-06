input = 'testw.email+alex@leetcode.com'

uniqueEmail = set()

local, domain = input.split('@')

local
domain

if '+' in local:
    local = local[:local.index('+')].replace('.','')

    uniqueEmail.add(local + '@' + domain)


class Solution(object):
    def numUniqueEmails(self, emails):
        uniqueEmail = set()
        for email in emails:
            local, domain = email.split('@')
            if '+' in local:
                local = local[:local.index('+')]
            uniqueEmail.add(local.replace('.', '') + '@' + domain)
        return len(uniqueEmail)

