2018-02-08 21:53
Virutualbox打造自己使用的Linux虚拟机
  * 从Ubuntu官网下载最新的Ubuntu 17.10 Server的ISO；
  * 用ISO在vbox里面装机，注意的是，安装过程只能使用英文，否则会出错。这是近两年ubuntu的安装程序的小bug，至今也没解决，好在对中文的支持可以后期添加。记得末尾选择ssh服务器，其他都可以不选择；
  * 安装完毕后，默认的NAT模式显示的网络地址是无法ssh上去的；需要更改网络模式为桥接；或者是设置NAT的端口转发也可以，只要填写主机端口和客户机端口两个参数，例如主机端口2022，客户机端口22，即可通过主机的127.0.0.1:2022就可以SSH到客户机了。
  * sudo systemctl enable ssh.socket设置SSH服务自启动；
  * 添加SSH公钥：步骤：cd ~;mkdir .ssh;chmod 700 .ssh;cd .ssh;vi authorized_keys;填入你的公钥;chmod 600 authorized_keys;然后就可以公钥登录了；
  * 安装docker,sudo apt install docker,还有docker.io这两个；
  * sudo docker pull几个常用镜像：
  ubuntu,alpine,
  postgres, mongo,
  golang,ruby,pypy,gcc,perl, jruby,node,java,r-base,rust,haskell,swift,
  python,pypy,django,julia,plone,zope,
  elasticsearch,redis,nginx,rabbitmq,
  jetty, zookeeper,thrift,
  jenkins,drupal，joomla, redmine,
  * 设置SSH反向隧道，使得在外面也可以访问处于NAT后面，内网里面的虚拟机，同时使用AutoSSH保持SSH的稳定连接；做法参考https://linux.cn/article-5975-1.html，具体操作如下：
    *   在内网服务器上ssh -fN -R 41722:localhost:22 root@work2 -i ~/.ssh/vps.pem ,含义是把公网服务器41722端口的流量转发到本机的22端口,-i指定使用哪个公钥登录公网 服务器；root@work2是公网服务器的用户名和域名；请把公网机器的域名，私钥事先准备好，在hosts文件和~/.ssh目录；
    *   现在可以登录到公网机器后ssh -p 10022 homeserver_user@localhost连接内网机器；
    * 上述方法要登录外网服务器，然后再次登录内网服务器；更好的方法是直接让外网服务器中继转发，命令如下：
        *   ssh -fN -R work2:41722:localhost:22 root@work2，但是目前尚未成功，错误消息如下Warning: remote port forwarding failed for listen port 22，所以暂且搁置；不过两次登录的做法也更安全一些；
    *   这个方法要求稳定，所以还要加上AutoSSH来保持稳定连接；
