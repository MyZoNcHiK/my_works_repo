class Training:
    def start_training(self):
        print("Початок тренування")
    def end_training(self):
        print("Завершення тренування")

class FootballTraining(Training):
    def start_training(self):
        print("Розминка, тактичні вправи, гра в міні-футбол")
    def end_training(self):
        print("Заключна розтяжка та короткий підсумок тренера")

class BasketballTraining(Training):
    def start_training(self):
        print("Вправи з кидків, командна робота, захисні стратегії")
    def end_training(self):
        print("Вправи на кидки з лінії штрафного кидка")

class TennisTraining(Training):
    def start_training(self):
        print("Вправи на техніку ударів, подачі, стратегія одиночної гри")
    def end_training(self):
        print("Завершальні вправи на витривалість та техніку")

football = FootballTraining()
football.start_training()
football.end_training()
print()
basketball = BasketballTraining()
basketball.start_training()
basketball.end_training()
print()
tenis = TennisTraining()
tenis.start_training()
tenis.end_training()
