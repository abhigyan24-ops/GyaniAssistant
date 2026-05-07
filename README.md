<div align="center">

<img src="Gyani.ico" alt="Gyani Logo" width="120"/>

# 🧠 Gyani Assistant

### Your Personal AI-Powered Voice Assistant

[![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)](https://python.org)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-412991?style=for-the-badge&logo=openai)](https://openai.com)
[![Platform](https://img.shields.io/badge/Platform-Windows-0078D6?style=for-the-badge&logo=windows)](https://microsoft.com/windows)
[![Built](https://img.shields.io/badge/Built-2021-orange?style=for-the-badge)](https://github.com/abhigyan24-ops/GyaniAssistant)
[![Status](https://img.shields.io/badge/Status-Archive%20%2F%20WIP-yellow?style=for-the-badge)](https://github.com/abhigyan24-ops/GyaniAssistant)

*Gyani listens, understands Hindi & English, thinks with GPT, and talks back — all hands-free.*

</div>

---

## 🕰️ Built in 2021 — Before AI Was Cool

> Back in 2021, ChatGPT didn't exist. Asking your computer a question and getting a spoken, intelligent answer back was not something most people had seen outside of Siri or Alexa — both of which required expensive ecosystems to build on.
>
> Gyani was built as a **solo project** to explore what was possible with the OpenAI API (which was barely public at the time), Python speech recognition, and desktop automation — all stitched together into a Hindi-English voice assistant that could genuinely hold a conversation, read you the news, control your PC, and more.
>
> This was before the AI wave. Before everyone had a ChatGPT wrapper. Just curiosity, Python, and a mic. 🎤

---

## ⚠️ Important — Read Before Running

**This is the original 2021 source code, preserved as-is for archival purposes.**

A lot has changed in the Python/AI ecosystem since 2021. If you try to run this code today, several things will likely break:

| What's broken | Why | Fix |
|---|---|---|
| `openai` API calls | OpenAI released v1.0 SDK in 2023 — completely different syntax | Upgrade to `openai>=1.0` and rewrite calls |
| `googletrans` | Unofficial API breaks frequently | Pin to `googletrans==3.1.0a0` |
| `pyaudio` | Needs PortAudio C library — painful on modern Windows | Use `conda install pyaudio` |
| `BeautifulSoup` scraping | Google changes its HTML structure often — temperature scraping may fail | Use a proper weather API instead |
| API keys | All hardcoded keys have been removed and are expired anyway | Get fresh keys from each provider |
| Python 3.14 | Many packages don't have wheels for 3.14 yet | Use Python 3.11 |

> **TL;DR** — This code was written in 2021 with library versions from that era. It is being actively updated and refactored. Treat this as a reference / work-in-progress, not a plug-and-play project.

---

## ✨ Features

| Feature | Description |
|---|---|
| 🎤 **Voice Input** | Speaks in Hindi or English — Gyani understands both |
| 🌐 **Auto Translation** | Hindi speech auto-translated to English via Google Translate |
| 🧠 **GPT-Powered Brain** | Conversations powered by OpenAI GPT-3.5-turbo |
| 🔊 **Text-to-Speech** | Responds out loud using pyttsx3 TTS engine |
| 📰 **Live News** | Fetches top headlines by category via NewsAPI |
| 🌡️ **Weather/Temperature** | Scrapes real-time temperature from Google |
| 😂 **Jokes** | Tells random programmer jokes |
| 🎵 **Spotify Control** | Opens and plays Spotify Daily Mix automatically |
| ⚡ **Speed Test** | Checks your internet download & upload speed |
| 🖼️ **Image Generation** | Generates AI images using DALL-E 2 |
| ⏰ **Reminders** | Sets desktop notification reminders |
| 🎂 **Birthday Alerts** | Reads from Excel and announces today's birthdays |
| 🖥️ **System Control** | Shutdown, sleep, hibernate, lock, recycle bin |
| 👏 **Wake Word / Clap** | Wake Gyani with a clap or by saying "wake up" |
| 💬 **Chat Logs** | Every conversation saved to `chatlogs.txt` |

---

## 🏗️ Project Structure

```
GyaniAssistant/
│
├── brain.py              # Core AI engine (GPT-3.5 integration)
├── Listen.py             # Microphone input + Hindi→English translation
├── Speak.py              # Text-to-speech output (pyttsx3)
├── wishing.py            # Time-based greeting (Good Morning/Afternoon/Evening)
├── clap.py               # Wake detection (clap or voice "wake up")
│
├── Tell_News.py          # Live news via NewsAPI
├── Temperature.py        # Real-time weather scraping
├── Joke.py               # Random jokes via pyjokes
├── spotify.py            # Spotify automation via pyautogui
├── speed_test.py         # Internet speed test
├── image_generator.py    # DALL-E 2 image generation
├── SetReaminder.py       # Desktop reminder notifications
├── birthdates.py         # Birthday detection from Excel
├── systemRelated_info.py # System control (shutdown, lock, etc.)
├── song_detection.py     # Song title detection from lyrics
├── gyani.py              # Google Maps integration
│
├── gui.py                # GUI (customtkinter) — in progress
├── dates.xlsx            # Birthday data file
├── chatlogs.txt          # Conversation history
├── requirements.txt      # Python dependencies
└── Gyani.ico             # App icon
```

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.11** (strongly recommended — not 3.12+ or 3.14)
- **Windows OS** (some modules are Windows-only)
- A working **microphone**

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/abhigyan24-ops/GyaniAssistant.git
cd GyaniAssistant
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

> ⚠️ **PyAudio on Windows** requires PortAudio. If `pip install pyaudio` fails:
> ```bash
> conda install pyaudio
> ```

**3. Set up your API keys**

Create a `.env` file in the root folder:
```env
OPENAI_API_KEY=your_openai_key_here
NEWS_API_KEY=your_newsapi_key_here
GENIUS_API_KEY=your_genius_key_here
GOOGLE_MAPS_API_KEY=your_google_maps_key_here
```

Then replace the `YOUR_OPENAI_API_KEY` placeholders in the `.py` files with `os.getenv("OPENAI_API_KEY")`.

**4. Run Gyani**
```bash
python clap.py    # Start with wake detection
# OR
python brain.py   # Start conversation directly
```

---

## 🔑 API Keys Required

| Service | Used In | Get Key |
|---|---|---|
| OpenAI | `brain.py`, `image_generator.py` | [platform.openai.com](https://platform.openai.com/api-keys) |
| NewsAPI | `Tell_News.py` | [newsapi.org](https://newsapi.org) |
| Genius | `song_detection.py` | [genius.com/api-clients](https://genius.com/api-clients) |
| Google Maps | `gyani.py` | [console.cloud.google.com](https://console.cloud.google.com) |

---

## 🗺️ How It Works

```
👏 Clap / Say "wake up"
        ↓
   wishing.py  →  Good Morning / Afternoon / Evening
        ↓
   Listen.py   →  Mic input → Hindi/English → Translated text
        ↓
   brain.py    →  GPT-3.5 generates response
        ↓
   Speak.py    →  Speaks the response aloud
        ↓
  [Feature modules triggered by voice command]
  News / Weather / Joke / Spotify / Reminder / etc.
```

---

## 🛣️ Refactor Roadmap

This project is being modernised. Here's what's planned:

- [ ] Upgrade OpenAI SDK from v0 to v1.x
- [ ] Move all API keys to `.env` with python-dotenv
- [ ] Fix `SetReminder.py` elif chain bug
- [ ] Replace Google scraping in `Temperature.py` with a proper weather API
- [ ] Build full GUI with customtkinter (`gui.py`)
- [ ] Add voice command intent detection to route to feature modules
- [ ] Cross-platform support (Linux / macOS)

---

## 🤝 Contributing

Pull requests are welcome! Especially help with the refactor roadmap above.

1. Fork the repo
2. Create your branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -m 'Add YourFeature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

---

## 👨‍💻 Author

**Abhigyan** — [@abhigyan24-ops](https://github.com/abhigyan24-ops)

*Built in 2021 as a solo project — when building something like this actually took some digging.*

---

<div align="center">

Made with ❤️ and a lot of `speak("debugging...")` calls

⭐ **Star this repo if you found it useful!**

</div>
