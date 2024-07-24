FROM joyzoursky/python-chromedriver:3.8

WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt

# Копируем скрипт в контейнер
COPY 5_hw.py /app/5_hw.py

# Команда для запуска скрипта
CMD ["python", "5_hw.py"]