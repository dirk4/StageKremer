import pandas as pd


class Generator:
    csv = pd.read_csv('C:\\Users\\Lukassen\\Desktop\\Stage\\Dataset v2\\KremerDataLog_Full.csv')

    peaks = []
    number = None
    part = None
    shift = None
    location = None
    low_middle = None
    high_middle = None

    def generate(self, number, part, shift):
        self.number = number
        self.part = part
        self.shift = shift
        self.location = 'GP' + str(number) + '_' + part
        self.low_middle = max(self.csv[self.location]) * 0.40
        self.high_middle = max(self.csv[self.location]) * 0.60
        print('NEW CSV BEING SCANNED: ' + self.csv[self.location].name)

        self.generate_dataset()
        return self.get_rows()
        pass

    def get_rows(self):
        unique_values = list(dict.fromkeys(self.peaks))
        pieken_rows: pd.DataFrame = None
        for j in unique_values:
            if pieken_rows is None:
                pieken_rows = self.csv.loc[self.csv['GP' + str(self.number) + '_' + self.part] == j]
            else:
                pieken_rows = pieken_rows.append(self.csv.loc[self.csv['GP' + str(self.number) + '_' + self.part] == j])

        pieken_rows = pieken_rows.sort_values('Timestamp')
        name = 'GP' + str(self.number) + '_' + self.part
        print(name)
        print(pieken_rows[name])
        print(self.shift)
        pieken_rows['next'] = pieken_rows[name].shift(-self.shift)
        if 'Unnamed: 0' in pieken_rows:
            pieken_rows = pieken_rows.drop(columns='Unnamed: 0')

        return pieken_rows

    def generate_dataset(self):
        pass

    pass


class LowGenerator(Generator):
    def generate_dataset(self):
        for j in range(1, len(self.csv) - 1):
            current_row = self.csv[self.location][j]
            if current_row < self.csv[self.location][j - 1] \
                    and current_row < self.csv[self.location][j + 1] \
                    and current_row < self.low_middle:
                self.peaks.append(current_row)

    pass


class PeakGenerator(Generator):
    def generate_dataset(self):
        for j in range(1, len(self.csv) - 1):
            current_row = self.csv[self.location][j]
            if current_row > self.csv[self.location][j - 1] \
                    and current_row > self.csv[self.location][j + 1] \
                    and current_row > self.high_middle:
                self.peaks.append(current_row)

    pass


class MiddlePeakGenerator(Generator):
    def generate_dataset(self):
        for j in range(1, len(self.csv) - 1):
            current_row = self.csv[self.location][j]
            if self.csv[self.location][j - 1] < current_row < self.high_middle \
                    and current_row > self.csv[self.location][j + 1] > self.low_middle:
                self.peaks.append(current_row)

    pass


class MiddleLowGenerator(Generator):
    def generate_dataset(self):
        for j in range(1, len(self.csv) - 1):
            current_row = self.csv[self.location][j]
            if self.csv[self.location][j - 1] < current_row > self.low_middle \
                    and current_row < self.csv[self.location][j + 1] and self.csv[self.location] \
                    [j] < self.high_middle:
                self.peaks.append(current_row)

    pass


def generator_factory(version):
    generator: Generator = Generator()
    if version == 'peak':
        generator.__class__ = PeakGenerator
    elif version == 'low':
        generator.__class__ = LowGenerator
    elif version == 'middle_peak':
        generator.__class__ = MiddlePeakGenerator
    elif version == 'middle_low':
        generator.__class__ = MiddleLowGenerator
    else:
        raise Exception('Unavailable version')
    return generator
