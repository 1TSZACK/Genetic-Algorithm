import random
import matplotlib.pyplot as plt

class Genetic_Algorithim:
    required = []
    population = []
    size_of_population = 0
    size_of_chromosone = 0
    fitness = {}

    def __init__(self, sc):
        # self.size_of_population = random.randint(4,10)
        self.size_of_population = 4
        self.size_of_chromosone = sc
        for i in range(0, self.size_of_chromosone):
            self.required.append(1)
        for i in range(0, self.size_of_population):
            self.population.append(0)

    def population_intialziation(self):

        for pop_size in range(0, self.size_of_population):
            chromosone = []
            for i in range(0, self.size_of_chromosone):
                chromosone.append(0)
            for chrom_size in range(0, self.size_of_chromosone):
                chromosone[chrom_size] = random.randint(0, 1)
            self.population[pop_size] = chromosone

        # print("Population Initialized")
        # print(self.population)

    def fitness_calculation(self):
        fit = 0
        for chromosone in self.population:
            for i in range(0, self.size_of_chromosone):
                fit += chromosone[i] * pow(2, (self.size_of_chromosone - 1) - i)

            self.fitness[fit] = chromosone
            fit = 0
        # print(self.fitness)

    def selection(self):
        key_to_be_deleted = 0
        for i in sorted(self.fitness.keys()):
            key_to_be_deleted = i
            break
        del self.fitness[key_to_be_deleted]
        # print(self.fitness)

    def crossover(self):
        chromosones = []
        cr_chromosones = []
        for key in self.fitness:
            chromosones.append(self.fitness[key])

        for i in range(0, 2):
            si_chromo = []
            for h in range(0, int(self.size_of_chromosone / 2)):
                si_chromo.append(chromosones[i][h])
            for k in range(int(self.size_of_chromosone / 2), self.size_of_chromosone):
                si_chromo.append(chromosones[i + 1][k])
            cr_chromosones.append(si_chromo)

        for i in range(0, 2):
            si_chromo = []
            for h in range(int(self.size_of_chromosone / 2), self.size_of_chromosone):
                si_chromo.append(chromosones[i][h])
            for k in range(0, int(self.size_of_chromosone / 2)):
                si_chromo.append(chromosones[i + 1][k])
            cr_chromosones.append(si_chromo)

        self.population = cr_chromosones

    def mutation(self):

        for i in range(0, 4):
            while self.population[i][random.randint(0, self.size_of_chromosone - 1)] == 0:
                self.population[i][random.randint(0, self.size_of_chromosone - 1)] = 1


    def checker(self):
        fit = 0
        for chromosone in self.population:
            for i in range(0, self.size_of_chromosone):
                fit += chromosone[i] * pow(2, (self.size_of_chromosone - 1) - i)
            if fit == 255:
                return True
            else:
                fit = 0
        return False


ga = Genetic_Algorithim(8)
flag = False
gen = 1

while not flag:
    ga.population_intialziation()
    ga.fitness_calculation()
    ga.selection()
    ga.crossover()
    ga.mutation()
    flag = ga.checker()
    print("Generation: ", gen, " -> ", ga.population)
    gen += 1
    if flag:
        print("Found required chromosone in ", gen-1)
        print("Population: ", ga.population)

# b Putting values in graph by myself after calculating and analyzing
x = [4, 5, 6, 7, 8, 9, 10]
y1 = [21, 37, 35, 21, 2, 1, 16]
y2 = [63, 10, 34, 9, 2, 3, 54]
y3 = [40, 22, 12, 10, 8, 25, 36]
y4 = [8, 32, 35, 21, 3, 14, 9]
plt.title('Population Size V/S Number of Generations')
plt.xlabel('Population Size')
plt.ylabel('Number of Generations')
plt.plot(x, y1, label="Generation 1")
plt.plot(x, y2, label="Generation 2")
plt.plot(x, y3, label="Generation 3")
plt.plot(x, y4, label="Generation 4")
plt.legend()
plt.show()

# c
x = [10, 12, 14, 16, 18, 22]
y1 = [56, 23, 12, 3, 9, 14]
y2 = [32, 29, 42, 39, 54, 12]
y3 = [20, 30, 2, 4, 9, 25]
y4 = [28, 32, 69, 10, 30, 4]
plt.title('Chromosome Length VS Num of Generations')
plt.xlabel('Chromosome Length')
plt.ylabel('Num of generations')
plt.plot(x, y1, label="Generation 1")
plt.plot(x, y2, label="Generation 2")
plt.plot(x, y3, label="Generation 3")
plt.plot(x, y4, label="Generation 4")
plt.legend()
plt.show()