import os


class DynamicCsvConverter:

    def __init__(self, gripper_jack_nr, part, time_interval, value_type, dataframe):
        """
        :param gripper_jack_nr: the number of the gripperjack
        :param part: String of the desired part
        :param time_interval: The time interval
        :param value_type: The value times (min, avg, max)
        :param dataframe: The dataframe that needs to be used
        """
        self.gripper_jack_nr = gripper_jack_nr

        # available parts are (Position, Velocity, PushPressure, PressureA, PressureB, ClaspPressure, OilTemperature)
        self.part = part

        # use S to signify seconds
        # use Min to signify minutes
        # use H to signify hours
        # use D to signify days

        self.time_interval = time_interval

        # use 'avg' to signify the average value of the given time_interval
        # use 'max' to signify the maximum value of the given time_interval
        # use 'min' to signify the minimum value of the given time_interval
        self.type = value_type

        self.logging_gelredome = dataframe.copy()

    def print_info(self):
        print('========================')
        print('CSV INFO')
        print('========================')

        print('Predicting gripperjack nr:   ' + str(self.gripper_jack_nr))
        print('part:                        ' + self.part)
        print('Interval:                    ' + self.time_interval)
        print('Type:                        ' + self.type)
        print('')

    def prepare_dataframe(self):
        self.logging_gelredome['Timestamp'] = self.logging_gelredome['Timestamp'].astype('datetime64')

        self.logging_gelredome['Timestamp'] = self.logging_gelredome['Timestamp'].dt.floor(self.time_interval)
        self.logging_gelredome = self.logging_gelredome[[
            'Timestamp',
            'GP' + str(self.gripper_jack_nr) + '_Position',
            'GP' + str(self.gripper_jack_nr) + '_Velocity',
            'GP' + str(self.gripper_jack_nr) + '_PushPressure',
            'GP' + str(self.gripper_jack_nr) + '_PressureA',
            'GP' + str(self.gripper_jack_nr) + '_PressureB',
            'GP' + str(self.gripper_jack_nr) + '_ClaspPressure',
            'GP' + str(self.gripper_jack_nr) + '_OilTemperature',
            'OutsideTemp'
        ]]

    def add_to_be_predicted(self):
        times = self.logging_gelredome['Timestamp'].unique()
        for t in range(0, len(times) - 1):
            var = self.logging_gelredome.loc[self.logging_gelredome['Timestamp'] == times[t + 1]]
            for i in var:
                if self.type == 'avg':
                    self.logging_gelredome.loc[
                        self.logging_gelredome['Timestamp'] == times[t], 'to_be_predicted'] = sum(
                        var['GP' + str(self.gripper_jack_nr) + '_' + self.part].dropna()) / len(
                        var['GP' + str(self.gripper_jack_nr) + '_' + self.part].dropna())
                elif self.type == 'max':
                    self.logging_gelredome.loc[
                        self.logging_gelredome['Timestamp'] == times[t], 'to_be_predicted'] = max(
                        var['GP' + str(self.gripper_jack_nr) + '_' + self.part])
                elif self.type == 'min':
                    self.logging_gelredome.loc[
                        self.logging_gelredome['Timestamp'] == times[t], 'to_be_predicted'] = min(
                        var['GP' + str(self.gripper_jack_nr) + '_' + self.part])

    def save_file(self):
        location = 'Recources\\GripperjackLogs\\GP' + str(
            self.gripper_jack_nr) + '\\' + self.part + '\\' + self.type + '\\' + self.time_interval.replace(' ',
                                                                                                            '') + '.csv'
        directory = os.path.dirname(location)
        if not os.path.exists(directory):
            os.makedirs(directory)
        self.logging_gelredome.to_csv(location, index=False)

    def make_file(self):
        self.prepare_dataframe()
        self.add_to_be_predicted()
        self.save_file()
        return self.logging_gelredome

    def existence(self):

        return os.path.exists('Recources\\GripperjackLogs\\GP' + str(
            self.gripper_jack_nr) + '\\' + self.part + '\\' + self.type + '\\' + self.time_interval.replace(' ',
                                                                                                            '') + '.csv')
