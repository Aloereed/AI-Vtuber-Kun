# AI-Vtuber-Kun

Makes your AI vtuber.

> 让 AI 成为虚拟主播：看懂弹幕，妙语连珠，悲欢形于色，以一种简单的实现

- 不定期的测试直播：http://live.bilibili.com/22747237
- QQ 交流群：569686683

## 项目构成

| 说明        | 基于           |
|-----------|--------------|
| GPT       | OpenAI       |
| TTS       | pyttsx3      |
| 直播间弹幕弹幕获取 | bilibili_api |

## 起步

（首次使用，毋必按照如下步骤走一边，不能直接看后面的部署一节）

1. 开发环境

```sh
$ python
Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>
$ pip -V
pip 23.0.1 from C:\Users\Xzai\AppData\Local\Programs\Python\Python311\Lib\site-packages\pip (python 3.11)
```
2. 如何运行？

```python
打开"AI-Vtuber.py"，编辑文件内容

将"API-KEY"修改为你的OpenAI Key
将"room_id"的内容改为你的直播间id

然后打开终端，依次输入
pip3 install openai
pip3 install pyttsx3
pip3 install bilibili-api-python
来安装依赖
```
3. 启动！
```sh
直接双击"AI-Vtuber.py"即可
```

给新手的 OBS 配置详解：

- blivechat：来源 > `+` > 浏览器 > 新建 > URL:
    - 填入：https://bilichat.3shain.com/bilibili/你的直播间id 即可
- 音频：来源 > `+` > 应用程序音频采集 > 新建 > 选择python
- B 站推流：设置（Preferences）> 直播 > 服务：选 `Bilibili Live ...`，推流码填「B 站首页 > 头像 > 推荐服务 > 直播中心 >
  左侧“我的直播间”> 填好直播分类、房间标题 > 开始直播，然后会显示的串流密钥」


## TODO

- [ ] 文档：各项目的 README、文档
- [ ] Topic：直播话题：一起看，打游戏，互动游戏，……
- [ ] murecom for muvtuber：基于心情的 BGM
- [ ] Live2D View & Driver：焦点控制、像官方的 Viewer 那样丰富的任意动作、表情控制（离散 -> 连续）
- [ ] Chatbot：
    - [ ] ChatGPT 平替
    - [x] ChatGPT 多用户轮流访问：提高可用性
    - [ ] MusharingChatbot（ChatterBot）重新训练
- [ ] 一个 muvtuber 出道介绍视频
- [ ] Filter：优先 + 排队，不要直接扔，存着，词穷的时候别冷场
- [ ] ……

## 开放源代码

所有下属项目除非特别说明，一律在 Apache License 2.0 协议下开放源代码。

欢迎任何有关 Issue 问题、PR 贡献以及讨论。