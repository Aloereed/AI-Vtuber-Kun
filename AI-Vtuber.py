import openai  # 导入OpenAI API库
import pyttsx3  # 导入TTS（文本到语音）库
from bilibili_api import live, sync  # 导入bilibili直播API库

openai.api_key = "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"  # 设置OpenAI API Key
model_engine = "text-davinci-003"  # 设置模型引擎

room_id = 22747237  # 直播间编号
room = live.LiveDanmaku(room_id)  # 连接弹幕服务器

initial_prompt = "你是一个来自二次元的AI虚拟主播，之后我的输入均为观众输入，请简要回答，15个字左右吧。不要回答有关政治的问题！也不要回答敏感信息！。"  # 初始提示信息

engine = pyttsx3.init()  # 初始化TTS引擎

async def generate_response(prompt):
    """
    生成AI的回复
    :param prompt: 观众提出的问题
    :return: AI的回复
    """
    full_prompt = f"{initial_prompt} {prompt}"  # 合并初始提示和观众提问
    response = openai.Completion.create(
        engine=model_engine,
        prompt=full_prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text.strip()  # 调用OpenAI API生成回复
    return response

@room.on('DANMU_MSG')
async def on_danmaku(event):
    """
    处理弹幕消息
    :param event: 弹幕消息事件
    """
    content = event["data"]["info"][1]  # 获取弹幕内容
    user_name = event["data"]["info"][2][1]  # 获取用户昵称
    print(f"[{user_name}]: {content}")  # 打印弹幕信息

    prompt = f"{content}"  # 设置观众提问
    response = await generate_response(prompt)  # 生成回复

    print(f"[AI回复”{user_name}“]: {response}")  # 打印AI回复信息

    with open("C:\\Users\\Xzai\\Desktop\\aioutput.txt", "a", encoding="utf-8") as f:
        f.write(f"{response}\n")  # 将回复写入文件

    engine.say(response)  # 文本转语音
    engine.runAndWait()  # 播放语音

sync(room.connect())  # 开始监听弹幕流

#TODO 1.敏感词过滤
#TODO 2.微软TTS
