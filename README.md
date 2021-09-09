# SSH Brute Force using Python
_Disclaimer: This projecte was created for educational purposes.
Use for malicious or illegal activities is not authorized within the scope of taking from this code._

## Purpose
Takes files containing line-separated passwords and usernames, user provided port at command line,
and target(hostname) and attempts all combinations

#### Example use
``` python sshBruteForce.py localhost -u usernames.txt -P passwords.txt -p 1818 ```

## Future Features and Known Bugs
- There is currently a known issue with the Paramiko library throwing an EOF error
- Ability to use a file with multiple targets
- ability to check multiple ports for each attempted target
