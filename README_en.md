# AI Vtuber Kun

[简体中文](https://github.com/XzaiCloud/AI-Vtuber-Kun/blob/main/README.md) | English

AI Vtuber Kun is a virtual YouTuber powered by OpenAI, capable of real-time interaction with viewers on Bilibili live streaming platform. It uses natural language processing and text-to-speech technology to generate answers to viewers' questions.

Community: [745682833](https://jq.qq.com/?_wv=1027&k=IO1usMMj)

### Requirements
- Python 3.7 or higher
- OpenAI API key
- Bilibili account and room ID
- `openai`, `yttsx3`, and `bilibili-api-python` Python libraries

### Installation
1. Clone the repository:
```bash
git clone https://github.com/your_username/AI-Vtuber-Kun.git
```
2. Install the required packages:
```bash
pip install openai pyttsx3 bilibili-api-python
```

### Usage
1. Run the program:
```bash
python main.py
```
2. Start live streaming on Bilibili and enter your live room.
3. AI-Vtuber-Kun will start generating answers to viewers' questions in real-time and delivering them via speech.

### OBS Configuration Guide for Beginners:
#### blivechat Configuration
- Source > + > Browser > New > URL: https://bilichat.3shain.com/bilibili/your_live_room_id
Audio Configuration
- Source > + > Application Audio Capture > New > Choose Python
#### Bilibili Live Streaming Configuration
- Preferences > Live Streaming > Service: Bilibili Live ...
- Stream code: Enter "Stream Key" which can be found by going to homepage > avatar > recommended services > live center > my live room (on the left) > fill in live category and room title > start live streaming.
#### Live2D...
- Any skin will do.

### TODOs
- [ ] Implement sensitive word filtering
- [ ] Add Microsoft TTS support

### License
This project is licensed under the Apache License 2.0. See the LICENSE file for details.
