#! python3
#pw.py - An insecure password locker program.

PASSWORDS = {'email': 'OFhoiakmnaolimjnaoifa',
             'blog': 'dadaaclakmdwa',
              'luggage': '12345'}
import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]   # 1st command line arg is the acccount name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Passwords for ' + account + 'copied to clipbard.')
else:
    print('There is no account named ' + account)
