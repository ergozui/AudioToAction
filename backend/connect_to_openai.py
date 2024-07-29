import openai
import os
import requests
# 设置API密钥
# openai.api_key = 'your-api-key'
openai.api_key = os.environ.get("OPENAI_API_KEY")

# 调用API
# 提问代码
def summary_extraction(message):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0,
        n=1,
        messages=[
            {
                "role": "system",
                "content": "You are a highly skilled AI trained in language comprehension and summarization. I would like you to read the following text and summarize it into a concise abstract paragraph. Aim to retain the most important points, providing a coherent and readable summary that could help a person understand the main points of the discussion without needing to read the entire text. Please avoid unnecessary details or tangential points. Please use less than 30 words.",
            },
            {"role": "user", "content": message},
        ],
    )
    return response.choices[0].message.content


def key_points_extraction(message):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0,
        n=1,
        messages=[
            {
                "role": "system",
                "content": "You are a proficient AI with a specialty in distilling information into key points. Based on the following text, identify and list the main points that were discussed or brought up. These should be the most important ideas, findings, or topics that are crucial to the essence of the discussion. Your goal is to provide a list that someone could read to quickly understand what was talked about. Please use less than 30 words.",
            },
            {"role": "user", "content": message},
        ],
    )
    return response.choices[0].message.content


def action_item_extraction(message):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0,
        n=1,
        messages=[
            {
                "role": "system",
                "content": "You are an AI expert in analyzing conversations and extracting action items. Please review the text and identify any tasks, assignments, or actions that were agreed upon or mentioned as needing to be done. These could be tasks assigned to specific individuals, or general actions that the group has decided to take. Please list these action items clearly and concisely. Please use less than 30 words.",
            },
            {"role": "user", "content": message},
        ],
    )
    return response.choices[0].message.content


def sentiment_analysis(message):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        temperature=0,
        n=1,
        messages=[
            {
                "role": "system",
                "content": "As an AI with expertise in language and emotion analysis, your task is to analyze the sentiment of the following text. Please consider the overall tone of the discussion, the emotion conveyed by the language used, and the context in which words and phrases are used. Indicate whether the sentiment is generally positive, negative, or neutral, and provide brief explanations for your analysis where possible. Please use less than 30 words.",
            },
            {"role": "user", "content": message},
        ],
    )
    return response.choices[0].message.content


function_map = {
    "Key points identification": key_points_extraction,
    "Action item extraction": action_item_extraction,
    "summary": summary_extraction,
    "sentiment": sentiment_analysis,
}

def extract_audio(audio_name):
    file = open('uploads' + "/" + audio_name, "rb")#根据路径打开文件

    if not file:
        return None

    response = openai.audio.transcriptions.create(#response是一个对象，whisper-1返回结果存储在response中
        file=file,
        model="whisper-1",#调用openai api
        response_format="text",
        language="en"
    )

    return response
def extract_audio2(file):
    response = openai.audio.transcriptions.create(#response是一个对象，whisper-1返回结果存储在response中
        file=file,
        model="whisper-1",#调用openai api
        response_format="text",
        language="en"
    )
def get_audio(data):
    speech_file_path = "uploads/speech.mp3"
    response = openai.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input=data
    )
    response.stream_to_file(speech_file_path)
    return response


def image(filename):
    file_path='uploads/'
    true_file_path=os.path.join(file_path,filename)
    response = openai.images.create_variation(
      image=open(true_file_path, "rb"),
      n=2,
      size="1024x1024"
    )

    image_url = response.data[0].url
    return(image_url)
def save_image(image_url, filename):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(filename, 'wb') as f:
            f.write(response.content)
            print(f"图像已保存为 {filename}")
    else:
        print("无法下载图像")
if __name__ == '__main__':
    # text='智能合约为区块链应用带来了新的维度。随后，区块链从去中心化的加密货币分类账发展成了用于开发去中心化应用的平台。去中心化应用需要来自现实世界的各种数据，这些数据无法直接由智能合约提供。预言机为去中心化应用的智能合约提供了一种可信的机制，用于输入数据。预言机是从数据源收集数据、验证数据，然后将其传输到区块链的实体。预言机的引入重新引入了中心化、单点故障和对信任第三方的依赖等问题，这在区块链生态系统中产生了一些问题。预言机采用了不同的手段来减少中心化，并实现一些无需信任的操作机制，其中包括基于投票或声望的去中心化算法。在本文中，我们分析了区块链预言机问题的概念，它对各种区块链应用的影响，不同类型的预言机以及信任机制。我们还分析了一些重要的预言机（如Chainlink、Provable）及其基本机制，并进行了比较。最后，我们进行了差距分析，并讨论了一些必须解决的开放性研究问题，以实现强大且安全的去中心化。'
    # get_audio(text)
    image_url=image('digram.png')
    save_image(image_url, "uploads/saved_image.jpg")


