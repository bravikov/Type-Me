import datetime
import random
import csv
import os


class Report:
    def __init__(self,
                 start_time: datetime.datetime,
                 end_time: datetime.datetime,
                 text_length: int,
                 typo: bool):
        self.start_time = start_time
        self.end_time = end_time
        self.text_length = text_length
        self.typo = typo

    def delta_seconds(self):
        return (self.end_time - self.start_time).total_seconds()

    def delta_minutes(self):
        return self.delta_seconds() / 60

    def delta_mmss(self):
        total_sec = self.delta_seconds()
        minutes = int(total_sec // 60)
        seconds = int(total_sec % 60)
        return '{:02}m {:02}s'.format(minutes, seconds)

    def cpm(self):
        return self.text_length / self.delta_minutes()


def save_report_to_csv(report: Report):
    filename = 'statistics.csv'
    write_header = False if os.path.exists(filename) else True
    with open(filename, 'a') as csvfile:
        csv_writer = csv.writer(csvfile)
        if write_header:
            csv_writer.writerow(
                ['start_time', 'duration_sec', 'text_length', 'typos', 'CPM'])
        csv_writer.writerow([
            report.start_time.isoformat(sep=' ', timespec='seconds'),
            report.delta_seconds(),
            report.text_length,
            report.typo,
            report.cpm(),
        ])
    pass


def print_report(report: Report):
    report_text = 'Typos: {}.\n'\
                  'Characters per minute: {}.\n'\
                  'Duration: {} sec.\n'\
                  'Number of characters: {}.\n'

    print(report_text.format(
        'Yes' if report.typo else 'No',
        report.cpm(),
        report.delta_mmss(),
        report.text_length
    ))


def test(origin_text):
    input('Press Enter to start.')
    print()
    print(origin_text)
    start_time = datetime.datetime.now()
    print()
    input_text = input()
    print()
    end_time = datetime.datetime.now()
    report = Report(start_time, end_time, len(input_text),
                    origin_text != input_text)
    print_report(report)
    save_report_to_csv(report)


MIN_TEXT_SIZE = 200

test_texts = []

with open('Forrest_Gump-John_Escott. English.txt', 'r') as texts:
    for text in texts:
        text = text.strip()
        if (len(text) >= MIN_TEXT_SIZE):
            test_texts.append(text)

random.shuffle(test_texts)

for test_text in test_texts:
    test(test_text)
