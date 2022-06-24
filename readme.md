## 用来网站自动签到的小脚本

项目是起始于4.2的一个自用小脚本

此项目托管于``Github Action``进行网站自动签到，仅供交流学习使用。

如果您喜欢这个项目，请给一个小小的Star

## 免责声明

本项目的开发者完全出于以下目的而进行开发：

1. 练习 selenium、fastapi 等 python 全栈与爬虫技术
2. 学习完整的开源项目流程，包括开发、测试、维护等
3. 掌握 GitHub 的相关进阶操作

本项目承诺：

1. 该项目的所有代码、文档、示例等均是以学习全过程软件开发与学习交流为目的，所有开发者除了必要的功能测试以外，没有在任何时间下使用过这个项目。
2. 本项目不会保存您的所有个人信息，不必担心隐私泄露。


本项目遵守 [MIT License](LICENSE) ,任何个人或组织拥有任意使用、复制、修改、合并、出版发行、散布、再许可和/或贩售软件及软件的副本，及授予被供应人同等权利的权利。因为第三方个人或组织使用该软件而产生的任何不良后果，本项目的 所有开发者不承担任何责任。


## 更新日志

+ 2022/6/24 加入baiwangame
+ 2022/6/23 修正重试策略
+ 2022/5/31 修复bug 现在web driver可以删除cookie了
+ 2022/5/30 由于action因为网络不稳定的问题经常出现打卡失败的情况，添加重试10次的功能
+ 2022/5/24 huaxia首页弹窗修复 已经可以正常签到
+ 2022/5/23 huaxia签到第一版（2账号）
+ 2022/5/22 开始着手开发huaxia的签到逻辑
+ 2022/5/21 修复光板小镇的bug 从而更加正确的获取menu
+ 2022/5/21 开始着手编写readme

## 目前支持的网站

1. wanbianios
2. moe17
3. rjhome
4. clfans
5. huaxia_ios


## 如何与维护者联系

如果有疑问需要联系作者，可以提issue


## 配置说明

用js信息写入账号密码到secret→CONFIG
若账号数量不一致请自行修改python代码 后期维护压力过大会考虑集成函数...（太懒了QAQ）
具体名称参见py代码
