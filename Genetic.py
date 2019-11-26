import random

GENES = "abcdefghijklmnopqrstuvwxyz123456789.#{}[]()"
TARGET = "vimaljamesprogram"

class Individual:
  
  #Default gnome is empty
  def __init__(self, p_gnome = "-1"):
    self.fit_score = 0
    if p_gnome == "-1":
      self.gnome = [self.mutate_gene() for _ in range(len(TARGET))]
    else:
      self.gnome = p_gnome
    self.fitness = self.get_fitness()

  def mutate_gene(self):
    gene = random.choice(GENES)
    return gene
  
  def get_fitness(self):
    self.fit_score = 0
    for a, b in zip(self.gnome, TARGET):
      if a != b:
        self.fit_score += 1
    return self.fit_score

  def mate(self, parent_2):
    child_gnome = []

    for p1, p2 in zip(self.gnome, parent_2.gnome):
      randomness = random.random()
      if randomness < 0.4:
        child_gnome.append(p1)
      elif randomness > 0.6:
        child_gnome.append(p2)
      else:
        child_gnome.append(self.mutate_gene())

    return child_gnome

def showPopulation(generation, population):
  print("Generation: ", generation)
  for individual in population:
    print(individual.gnome)
  print("*******************************\n\n\n")

def main():
  
  population = []
  new_generation = []

  generation_count = 0

  #Generate Initial Random Population
  for _ in range(21):
    population.append(Individual())

  #Show initial population
  print("Initial: ")
  showPopulation(generation_count, population)

  #Repeat Until Target String is Created
  while True:
    
    #Increment Generation Counter
    generation_count += 1

    #Sorted Population List according to fitness score
    population_sorted = sorted(population, key = lambda x : x.fit_score)
    
    #Check if the lowest fitness score available is 0
    if population_sorted[0].fit_score == 0:
      print("Got : ", population_sorted[0].gnome)
      break
    
    #Else Pick best 20% from pool to mate
    else:
      best_twenty_index = int(0.2 * len(population_sorted))
      worst_eighty_index = int(0.8 * len(population_sorted))
      average_thirty_index = int(0.3 * len(population_sorted))
      new_generation.extend(population_sorted[:best_twenty_index])
      
      #From the remaining 80% of the population, take parents from top 30%, let them mate and create new generation
      for _ in range(worst_eighty_index):
        parent_1 = random.choice(population_sorted[:average_thirty_index])
        parent_2 = random.choice(population_sorted[:average_thirty_index])
        child = parent_1.mate(parent_2)
        new_generation.append(Individual(child))

      del population[:]
      population = new_generation[:]
      del new_generation[:]
      showPopulation(generation_count, population)

      
main()
  

