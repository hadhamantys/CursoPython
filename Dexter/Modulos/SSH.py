#!/usr/bin/python
# arquivo: SSH.py

import paramiko

class SSH:


    def __init__(self):
        ssh = paramiko.SSHClient()
        ssh.load_system_host_keys()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname='192.168.0.2', username='forlinux', password='4linux')
        return ssh


    def exec_comandos(comms):
        ssh = conn_ssh()
        stdin, stdout, stderr = ssh.exec_command(comms)
        if stderr.channel.recv_exit_status() != 0:
            return stderr.read()

        else:
            return stdout.read()
