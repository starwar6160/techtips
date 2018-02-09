*   Virutualbox打造自己使用的Linux虚拟机（2018-02-08 21:53）
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
  * 设置SSH反向隧道，方便从外网访问该服务器，具体步骤参见另一篇文章；此外，内网服务器也可以是Windows的，使用cygwin里面的ssh,autossh，可以达到同样的稳定隧道效果，用于把windows的诸如3389等端口选择性的开放出来；
