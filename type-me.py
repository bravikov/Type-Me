import datetime
import random

MIN_TEXT_SIZE = 200

report = '''
Typos: {}.
Characters per minute: {}.
Time: {} sec.
Number of characters: {}.
'''

test_texts = []

with open('Forrest_Gump-John_Escott. English.txt', 'r') as texts:
    for text in texts:
        text = text.strip()
        if (len(text) >= MIN_TEXT_SIZE):
            test_texts.append(text)

random.shuffle(test_texts)
            
def test(origin_text):
    input('Press Enter to start.')
    print()
    print(origin_text)
    start_time = datetime.datetime.now()
    print()
    input_text = input()

    end_time = datetime.datetime.now()
    delta = start_time - end_time
    cwm = len(input_text) / (abs(delta.total_seconds()) / 60)

    print(report.format(
        'No' if origin_text == input_text else 'Yes',
        cwm,
        abs(delta.total_seconds()),
        len(input_text)
    ))

for test_text in test_texts:
    test(test_text)
