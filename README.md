# Speech Emotion Recognition (SER) Project

A full-stack application that uses machine learning to analyze and recognize emotions from speech audio files.

## Features

- Audio file upload and processing
- Real-time emotion recognition
- User authentication system
- Modern and responsive UI
- Support for various audio formats

## Tech Stack

### Frontend
- HTML5
- CSS3
- JavaScript
- Bootstrap
- Font Awesome

### Backend
- Python
- Flask
- Machine Learning Models (CNN, LSTM)
- Audio Processing Libraries

## Project Structure

```
CODE/
├── Frontend/
│   ├── templates/
│   │   └── application.html
│   └── static/
│       ├── css/
│       ├── js/
│       └── images/
└── Backend/
    ├── Models/
    │   ├── model_final.h5
    │   ├── lstm.h5
    │   └── cnn.h5
    └── Data/
        └── berlin-database-of-emotional-speech-emodb/
```

## Setup and Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/SER_final_year_project.git
cd SER_final_year_project
```

2. Install backend dependencies
```bash
pip install -r requirements.txt
```

3. Run the application
```bash
python app.py
```

## Usage

1. Register/Login to the application
2. Navigate to the Application page
3. Upload an audio file
4. Wait for the emotion analysis results

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Berlin Database of Emotional Speech (EMO-DB)
- Flask Documentation
- Bootstrap Documentation 