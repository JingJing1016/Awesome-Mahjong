# Awesome Mahjong

## 日麻书籍资料

* b站有大部分书籍的汉化版，up主光之行方做过[汇总和推荐视频](https://www.bilibili.com/video/BV1Vc411c7gF/)，置顶评论中有推荐书籍的专栏链接，包括但不限于：[79博客](https://www.bilibili.com/read/readlist/rl45758)，[麻将学习·牌效率](https://www.bilibili.com/read/readlist/rl509592)，[何切300](https://www.bilibili.com/read/readlist/rl380536)
* [日麻战术书链接合集](https://www.bilibili.com/read/cv18813609/)，b站南极大熊熊，除书籍以外还包括**国内爱好者随笔和杂谈**
* 其他推荐
  * [副露读牌体系化讲座](https://www.bilibili.com/read/readlist/rl119814)，b站纯全三色对对和
  * naga研究：[带亚两面型的两好型平和一向听，固定雀头吗？](https://b23.tv/9mhmypr)，b站谙锦
  * naga研究：[何切300选的NAGA分析](https://www.bilibili.com/read/readlist/rl499000)，b站纯能量

## 工具

### 常用网站

* 免费看谱ai [mortal](https://mjai.ekyu.moe/zh-cn.html)，[github项目地址](https://github.com/Equim-chan/mjai-reviewer)
* 付费看谱ai [naga](https://naga.dmv.nico/naga_report/order_form/)

* [雀魂牌谱屋](https://amae-koromo.sapk.ch/)，[github项目地址](https://github.com/SAPikachu/amae-koromo)
* [天凤水表网](https://nodocchi.moe/)
* [天风牌理](https://tenhou.net/2/)

### naga相关工具

* [naga使用介绍视频](https://www.bilibili.com/video/BV14s4y1x7an/)，b站多肉动物
* 雀魂牌谱转换工具
  * [油猴脚本](https://www.bilibili.com/video/BV1hL411K7eM/)，b站桔猫Orzcat，置顶评论中有[脚本链接](https://pan.baidu.com/s/1-OCScZ4F3tInqzy2YY_t0A?pwd=wbhp)
  * [浏览器插件](https://www.bilibili.com/read/cv17873540/)，b站五里梦中_，[edge插件链接](https://microsoftedge.microsoft.com/addons/detail/雀魂牌谱分析助手/jopdfhmfehndjpnjjidmkkmjmkaebodb?hl=zh-CN)，[chrome插件链接](https://chrome.google.com/webstore/detail/mahjongsoul-review-suppor/kdmfnkdgpialmejpgflfllkjakolamcc?hl=zh-CN)
  * [在线网站majsoul2naga](https://www.majsoul2naga.com/)
* [NAGA助手](https://www.bilibili.com/video/BV1XW421N7eL/)，b站嘉宁的多重宇宙
  * 功能：自动转天凤牌谱 / 小局选择 / 多账号管理 / NP点数分享 / NAGA网络代理
  * 网址：https://ricochet.cn/riichi/naga

### QQ机器人

* Freeze_Kirin
* 拉克丝
* [相关github项目](https://github.com/NekoRabi/Majsoul-QQBot)

### 分析工具

* [MajsoulPaipuAnalyzer](https://github.com/zyr17/MajsoulPaipuAnalyzer)，用于分析给出牌谱中每个玩家的和铳数据等

  ![](./img/analyzer示例.jpg)

### 比赛场牌谱点数修改

* [一个用gpt写的简单python脚本](./tool/comp2naga.py)，使用`pyinstaller -F`打包的[exe版本](./tool/comp2naga.exe)
* 功能：将联赛谱转为平场谱跑naga，南场 -> 东场，四家分数 -> 25000
* 输入：input.txt, json格式的联赛牌谱
* 输出：output.txt, json格式的平场牌谱

