#!/usr/bin/env python
# -*- coding: utf-8 -*-
import subprocess
import ConfigParser
import time
import os, sys

# https://qf-project-01.quark.com:8443/svn/paydayloan/src/nxdapp/pdmg/2017-07-05

conf_file = '/home/itadmin/fabric/conf.ini'
fabric_file = '/home/itadmin/fabric/putfile.py'
base_deploy_dir = '/opt/platform/'
base_pro_dir = '/data/jenkins_slave/workspace/'
env_file = '/home/itadmin/fabric/myenv.py'

now_time = time.strftime('%Y%m%d', time.localtime(time.time()))

conf = ConfigParser.ConfigParser()
conf.read(conf_file)


# 写配置文件,字段默认都为空值
def write_conf(section):
    res = conf.sections()
    if conf.has_section(section):
        print '\033[31msection: [%s] already exist!\033[0m' % section
    else:
        f = open(conf_file, 'wb+')
        conf.add_section(section)
        conf.set(section, 'svn', '')
        conf.set(section, 'publishdir', section)
        conf.set(section, 'deploy_dir', section)
        conf.set(section, 'version', '0')
        conf.set(section, 'host_name', '')
        conf.set(section, 'real_ip', '')
        conf.write(f)
        f.close()
        print '\033[32;1m section: [%s] 添加成功，请确认配置是否正确!\033[0m' % section


# 读取配置文件
def read_conf(section, option):
    res = conf.get(section, option)
    return res


# 备份当前代码，并将配置文件conf.ini内version加1
def backup(view, section):
    bak_num = str(conf.get(section, 'version')) + '_' + now_time
    pro_dir = base_pro_dir + view + '/' + section + '/'
    bak_dir = base_pro_dir + 'backup' + '/' + view + '/' + section + '/' + bak_num + '/'
    if os.path.exists(bak_dir):
        pass
    else:
        os.makedirs(bak_dir)
    cmd = "rsync -av %s %s --exclude=.svn" % (pro_dir, bak_dir)
    res = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    print res.stdout.read()
    with open(conf_file, 'wb+') as f:
        version = str(int(read_conf(section, 'version')) + 1)
        conf.set(section, 'version', version)
        conf.write(f)

def main():
    if len(sys.argv) == 2 and sys.argv[1].startswith('--') and len(sys.argv[1]) > 2:
        section = sys.argv[1][2:]
        write_conf(section)
        sys.exit()
    elif len(sys.argv) != 4 or sys.argv[1] == '--help':
        print '''\033[31m请输入正确的参数形式：《视图+项目名+主机》,如:
        ./pub.py nxd payday-loan-bizapp test       上传项目代码到conf.ini配置中的第一台主机
        ./pub.py nxd payday-loan-bizapp all       上传项目代码到conf.ini配置中所有需上传的服务器
        ./pub.py --payday-loan-bizapp       在配置文件中添加项目payday-loan-bizapp配置\033[0m'''
        sys.exit()
    else:
        view = sys.argv[1]
        section = sys.argv[2]
        ip = sys.argv[3]
        if ip == 'all':
            hosts = read_conf(section, 'real_ip')
        elif ip == 'test':
            hosts = read_conf(section, 'real_ip').split(',')[0]

        else:
            print "\033[31m无此服务器：%s" % ip
            sys.exit()
        backup(view, section)

        res = read_conf(section, 'deploy_dir')
        local_dir = base_pro_dir + view + '/' + section + '/*' 
        remote_dir = base_deploy_dir + res + '/'
        cmd_upload = "fab -f %s upload:local_dir=%s,remote_dir=%s -H %s"%(fabric_file,local_dir,remote_dir,hosts)
        cmd_restart = "fab -f %s -H %s -- sh /home/ops/restart.sh %s"%(env_file,hosts,section)
        res_u = subprocess.Popen(cmd_upload, stdout=subprocess.PIPE, shell=True)
        print res_u.stdout.read()
        res_r = subprocess.Popen(cmd_restart, stdout=subprocess.PIPE, shell=True)
        print res_r.stdout.read()


if __name__ == '__main__':
    main()

