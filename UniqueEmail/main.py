input = 'testw.email+alex@leetcode.com'

uniqueEmail = set()

local, domain = input.split('@')

local
domain

if '+' in local:
    local = local[:local.index('+')].replace('.','')



uniqueEmail.add(local+'@'+domain)