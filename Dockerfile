FROM  python

WORKDIR usr/src/app

COPY ..

RUN  pip install speech_recognition pyttsx3 pyaudio webbrowser

CMD ["python", "batman.py"]