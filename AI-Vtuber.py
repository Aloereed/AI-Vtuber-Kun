import openai
import pyttsx3
from bilibili_api import live, sync

# 用你自己的API Key替换下面的字符串
openai.api_key = "API-KEY"
# 使用Davinci模型引擎
model_engine = "text-davinci-003"

room_id = 10000000
room = live.LiveDanmaku(room_id)

initial_prompt = "你是一个来自二次元的AI虚拟主播，之后我的输入均为观众输入，请简要回答，15个字左右吧。不要回答有关政治的问题！也不要回答敏感信息！。"

engine = pyttsx3.init()


async def generate_response(prompt):
    """
    生成AI的回复
    :param prompt: 观众提出的问题
    :return: AI的回复
    """
    full_prompt = f"{initial_prompt} {prompt}"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=full_prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.5,
    ).choices[0].text.strip()
    return response


@room.on('DANMU_MSG')
async def on_danmaku(event):
    """
    处理弹幕消息
    :param event: 弹幕消息事件
    """
    content = event["data"]["info"][1]
    user_name = event["data"]["info"][2][1]
    print(f"[{user_name}]: {content}")  # 打印弹幕信息

    prompt = f"{content}"
    response = await generate_response(prompt)

    print(f"[AI回复”{user_name}“]: {response}")

    # 写入到文本文件中
    with open("C:\\Users\\Xzai\\Desktop\\aioutput.txt", "a", encoding="utf-8") as f:
        f.write(f"{response}\n")

    # 播放 TTS 音频
    engine.say(response)
    engine.runAndWait()


sync(room.connect())

#TODO 1.敏感词过滤
#TODO 2.微软TTS
