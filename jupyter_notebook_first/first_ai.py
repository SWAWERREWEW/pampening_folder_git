def first_numbers_ai():
    import numpy as np
    import tensorflow as tf

    # Создаем функцию для инициализации слоев нейронной сети
    def create_neural_network(input_dim, output_dim):
        model = tf.keras.Sequential([
            # Слой ввода
            tf.keras.layers.InputLayer(input_shape=(input_dim,)),
            # Слои персептрона
            tf.keras.layers.Dense(10, activation='relu', kernel_initializer='random_normal'),
            tf.keras.layers.Dense(output_dim, activation='linear')
        ])

        model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate=0.01), loss='mse')
        return model

    # Создаем нейросеть с одним входным и выходным нейроном
    input_dim = 1
    output_dim = 1
    model = create_neural_network(input_dim, output_dim)

    # Обучаем нейросеть на случайных данных (чтобы она "неграмотно" обучалась)
    x_train = np.random.rand(100, input_dim)
    y_train = np.random.rand(100, output_dim) * 2 - 1

    model.fit(x_train, y_train, epochs=1)

    # Функция для генерации ответа от нейросети
    def generate_response(query):
        query = np.array([query])
        response = model.predict(query)
        return response[0][0]

    # Пример использования
    query = 0.5
    response = generate_response(query)
    print(f"Запрос: {query}, Ответ: {response}")

def first_ai_wtf():
    import tensorflow as tf
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout

    # Гиперпараметры
    vocab_size = 10000  # Размер словарного запаса
    embedding_dim = 64  # Размер эмбеддинга
    max_length = 50  # Максимальная длина последовательности
    trunc_type = 'post'  # Тип обрезки
    padding_type = 'post'  # Тип паддинга

    # Создание модели нейросети
    model = Sequential()
    model.add(Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=max_length))
    model.add(LSTM(units=64, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=32))
    model.add(Dropout(0.2))
    model.add(Dense(units=vocab_size, activation='softmax'))

    # Компиляция модели
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

    print(model.summary())

    # Пример списка уникальных слов в словарном запасе
    vocab = ['это', 'пример', 'слова', 'в', 'словарном', 'запасе']

    # Создаем маппинг между словами и их индексами
    word_to_index = {word: i for i, word in enumerate(vocab)}

    # Пример предложения для обработки
    user_input = "Что?"

    # Преобразуем текст в последовательность индексов
    input_seq = [word_to_index.get(word, 0) for word in user_input.split()]  # Используем 0 как заменитель для неизвестных слов

    # Добавляем необходимое количество паддинга
    from tensorflow.keras.preprocessing.sequence import pad_sequences
    padded_seq = pad_sequences([input_seq], maxlen=max_length, padding=padding_type)

    # Теперь padded_seq содержит ваш текстовый запрос в виде последовательности индексов и готов к использованию моделью

    # Предсказание ответа от нейросети
    predicted_idx = model.predict(padded_seq)
    predicted_word_index = tf.argmax(predicted_idx, axis=-1).numpy()[0]

    # Преобразуем индекс в слово (простая маппинг для примера)
    index_to_vocab = {i: word for word, i in word_to_index.items()}
    predicted_word = index_to_vocab.get(predicted_word_index, "Неиз")

    print(f"Ответ от нейросети: {predicted_word}")


import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Пример данных: пары (вопрос, ответ)
data = [
    ("Какой сегодня погоды?", "Сегодня погода хорошая."),
    ("Кто такой Билл Гейтс?", "Билл Гейтс - основатель Microsoft."),
    # Добавьте больше примеров здесь
]

# Создаем словарные запасы и маппинг между словами и их индексами
vocab = set()
word_to_index = {}
index_to_word = {}

for question, answer in data:
    words = question.split() + answer.split()
    for word in words:
        vocab.add(word)

vocab = list(vocab)
word_to_index = {word: i for i, word in enumerate(vocab)}
index_to_word = {i: word for word, i in word_to_index.items()}

# Преобразуем текст в последовательности индексов
def text_to_sequences(texts):
    sequences = []
    for text in texts:
        words = text.split()
        seq = [word_to_index.get(word, 0) for word in words]  # Используем 0 как заменитель для неизвестных слов
        sequences.append(seq)
    return sequences


# Преобразуем вопросы и ответы в последовательности индексов
question_sequences = text_to_sequences([q for q, a in data])
answer_sequences = text_to_sequences([a for q, a in data])

# Обрезаем последовательности до максимальной длины
max_length = 50
question_sequences = pad_sequences(question_sequences, maxlen=max_length, padding='post')
answer_sequences = pad_sequences(answer_sequences, maxlen=max_length, padding='post')

# Создание модели нейросети
embedding_dim = 64
model = Sequential()
model.add(Embedding(input_dim=len(vocab), output_dim=embedding_dim, input_length=max_length))
model.add(LSTM(units=64, return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(units=32))
model.add(Dense(units=len(vocab), activation='softmax'))

# Компиляция модели
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy')

# Обучение модели
model.fit(question_sequences, answer_sequences[:, 1:], epochs=50, batch_size=8)

# Пример использования модели для генерации ответа на новый вопрос
new_question = "Кто такой Билл Гейтс?"
new_question_seq = text_to_sequences([new_question])
new_question_seq = pad_sequences(new_question_seq, maxlen=max_length, padding='post')

predicted_indexes = model.predict(new_question_seq)
predicted_words = [index_to_word[np.argmax(pred)] for pred in predicted_indexes[0]]

# Формируем ответ из предсказанных слов
generated_answer = ' '.join(predicted_words).strip()

print(f"Новый вопрос: {new_question}")
print(f"Генерированный ответ: {generated_answer}")
