# coding: utf-8
import json
import os
import re

import paramiko


class Udocker(object):

    def __init__(self):
        self.host = "10.1.100.213"
        self.username = "root"
        self.password = "ant123456"
        self.port = 22
        self.agent_path = "/opt"

    def get_connection(self):
        """与远程机器建立连接"""
        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(hostname=self.host, username=self.username,
                        password=self.password, port=self.port)
            return True
        except Exception as e:
            print(u"远程连接主机失败: {}".format(e))
            return False

    def get_agent_message(self):
        agent_yaml_path = self.agent_path + "/ant-agent/agent/config.yaml"
        stdin, stdout, stderr = self.ssh.exec_command("cat {}".format(agent_yaml_path))
        cmd_result = list((stdout.read(), stderr.read()))
        agent_id = ""
        if cmd_result[1]:
            print("读取文件失败: {}".format(cmd_result[1]))
        else:
            result_list = cmd_result[0].decode("utf-8").split("\n")
            for i in result_list:
                if "id" in i:
                    agent_id = i.split(":")[1].strip()
        return agent_id


def main():
    udocker = Udocker()
    connect_result = udocker.get_connection()
    if connect_result:
        print(udocker.get_agent_message())
    else:
        print(2222)


if __name__ == '__main__':
    main()
