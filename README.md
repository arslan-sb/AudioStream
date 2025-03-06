# Django Audio Streaming Project

This project is a Django-based web application for streaming audio files using HTTP Live Streaming (HLS). The application allows users to stream `.m3u8` files securely, making it difficult to download the audio files directly.

## Features

- Stream audio files in `.m3u8` format
- Securely serve audio files using Django views
- User authentication to restrict access to audio files
- Dynamic loading of audio files in HTML5 audio player using HLS.js

## Requirements

- Python 3.6+
- Django 3.2+
- HLS.js (included via CDN in the templates)

## Setup Instructions

### 1. Clone the Repository

```sh
git clone https://github.com/arslan-sb/AudioStream.git
cd AudioStream
```
