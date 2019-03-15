# 新人入职Setup

## 日常
首先，需要在mentor的协助下获得tower、钉钉账户，这是公司日常交流的工具，许多资料、软件需要通过这两种方式获得

## 系统盘
找振鹏或者郭祺，分别是16.04和18.04的Ubuntu系统

## Ubuntu翻墙
https://tower.im/teams/619394/documents/5367/

## 参考资料
之所以将参考资料写在如此靠前的位置，是因为公司一些公共的setup已经有所积累，具体参见：[规范](https://tower.im/teams/619394/projects/49/)
其中，对setup比较重要的文件是：【进入开发环境】和【Ubuntu使用OpenVPN】

## 开发工具
* IDE：Jetbrains，python使用PyCharm，go使用GoLand。
* Git：除了安装命令行工具外，推荐安装source tree做可视化，习惯命令行的请随意，需要注意的是，如果你的工作会经常涉及server上的操作，那么需要熟悉命令行的git操作
注意，这里的推荐开发工具仅仅是我个人推荐，在用过vim、atom、vscode、sublime等开发工具后，我更倾向于使用pycharm开发大型项目，source tree也是同样道理，但是，很可能出现此之蜜糖彼之砒霜的情况，因此，请合理选择

## Server配置
### root用户
首先，不推荐在root下进行开发，因此，请为特定任务或你自己开设一个新的账户：
`adduser yourname`
如果需要sudo权限，请添加
`usermod -aG sudo pypi`
请注意，上述两条命令如果无法使用，可能是因为没有切换到root用户，使用`sudo -i`切换

## 非root用户（即你自己的或项目的用户）
软件安装：
1. zsh+oh-my-zsh （可选）：非sudo用户安装zsh参见[linux - Install zsh without root access? - Stack Overflow](https://stackoverflow.com/questions/15293406/install-zsh-without-root-access)的**高票**答案
2. anaconda（如果你需要开发python）：下载安装方法见官网，你可以选择从tuna的镜像下载anaconda安装包，详见[Anaconda | 镜像站使用帮助 | 清华大学开源软件镜像站 | Tsinghua Open Source Mirror](https://mirror.tuna.tsinghua.edu.cn/help/anaconda/)。另外谷歌anaconda cheat sheet 有惊喜。最后，建议安装完anaconda后，切换pip源，方法为：`pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple`
3. golang：参考[Tower - 简单、好用的团队协作工具](https://tower.im/teams/619394/documents/6920/)：我个人的习惯是，在本地配置go，不在server端配置

其他：
1. 可以选择将ssh key添加到server 的authorized_keys中，具体参见https://adamdehaven.com/blog/how-to-generate-an-ssh-key-and-add-your-public-key-to-the-server-for-authentication/

## 初始开发时的小建议
1. 特别喜欢vim的话可以选择在pycharm中使用vim，谷歌 `bounding vim in PyCharm`
2. 没听说过 `tqdm` 的话请谷歌一下


