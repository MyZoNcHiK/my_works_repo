class MeanCalculator:
    def calculate(self, data):
        total = sum(data)
        count = len(data)
        return total / count

    def weighted_mean(self, data, weights):
        total = 0

        for i in range(len(data)):
            total += data[i] * weights[i]

        return total / sum(weights)

class MedianCalculator:
    def calculate(self, data):
        sorted_data = sorted(data)
        count = len(sorted_data)

        if count % 2 == 1:
            middle = count // 2
            return sorted_data[middle]
        else:
            middle = count // 2
            first = sorted_data[middle - 1]
            second = sorted_data[middle]
            return (first + second) / 2

    def grouped_median(self, data):
        return self.calculate(data)


class ModeCalculator:
    def calculate(self, data):
        frequencies = self.frequency_table(data)

        max_frequency = max(frequencies.values())

        result = []

        for value in frequencies:
            if frequencies[value] == max_frequency:
                result.append(value)

        return result

    def frequency_table(self, data):
        frequencies = {}

        for value in data:
            if value in frequencies:
                frequencies[value] += 1
            else:
                frequencies[value] = 1

        return frequencies

mean = MeanCalculator()
median = MedianCalculator()
mode = ModeCalculator()

data = [2, 4, 4, 6, 8, 8, 8, 10]
weights = [1, 2, 2, 1, 1, 2, 3, 1]

calculators = [mean, median, mode]

for calculator in calculators:
    print(calculator.calculate(data))

print("Зважене середнє:", mean.weighted_mean(data, weights))
print("Згрупована медіана:", median.grouped_median(data))
print("Таблиця частот:", mode.frequency_table(data))
