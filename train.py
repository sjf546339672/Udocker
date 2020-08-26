# coding: utf-8

str1 = input("请输入问题(采控代理离线/任务下发卡住/指标无法上报):")
if str1 == "采控代理离线":
    print("采控代理离线原因: ")
    print("""
        1. 检查platfrom-ant-transport模块运行异常，
        2. platfrom-ant-transport日志中数据是否成功发送心跳到kafka，且kafka的状态是正常的
        3. 查看store-res状态是否稳定，因为R16版本之后，agent状态是存放在mongodb的Pacific库reobject表中的
        4. 使用了ant-nginx做上报地址，端口不通，或者R16.40端口默认为80，升级到R16.40默认端口为7583，没有修改 
        5. platfrom-ant-lss 服务异常，状态同步失败
        6. agent日志报错http502
    """)
    print("解决方案: ")
    print("""
    个别机器离线:
        1. 根据离线的节点的agentid，在platfrom-ant-transport模块的connect.log，agent连接正常会输出[${agentid}]cached   断开连接会输出[${agentid}]remove
        2. 获取executor的agentid，同上在platfrom-ant-transport模块的connect.log中搜索
        3. 如果没有连上 ant-transporter，需要检查 agent 的日志，查看agent/var/logs目录下的defult.log日志，daemon.log日志
        4. 查看platfrom-ant-lss的日志，通过agentid查询结合store-res异常的时间点，注意，如果res异常状态持续时间长，环境的agent状态会大量丢失，时间短，只会有少量代理同步状态失败
    整个环境大批量离线:
        1. 查询服务端platfrom-ant-transport的日志，确认心跳上报是否正常，通过agentid查询具体心跳上报状态的信息，
           是否已经推送到kafka，登录到kafka机器上，执行命令查看topic信息，topicconsumer的情况，
           获取分区的offset是否正常--------R16之后状态不正确大部分原因症状，因为kafka不稳定的因素
        2. 因为store-res服务异常，间接性影响agent状态
        3. 使用了ant-nginx转发，端口填写错误，与agent的config.yaml中实际上报的端口不符合（80和7583端口错误）
        4. ant-nginx的虚拟ip地址不通。网络环境问题
        5. 查看agent日志报错http502错误时，查看platfrom-ant-transport.log会有报错信息输出
    """)
elif str1 == "任务下发卡住":
    pass
elif str1 == "指标无法上报":
    pass

