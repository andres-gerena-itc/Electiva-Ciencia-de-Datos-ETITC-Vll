# ANDRÉS FELIPE GERENA CONTRERAS - ETITC

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random

# Función para calcular la distancia euclidiana entre dos ciudades
def euclidean_distance(coord1, coord2):
    return np.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Cargar el dataset (supongamos que el archivo se llama 'small.csv')
cities = pd.read_csv('small.csv', header=None, names=['X', 'Y'])

# Calcular la matriz de distancias
n_cities = len(cities)
distance_matrix = np.zeros((n_cities, n_cities))

for i in range(n_cities):
    for j in range(i + 1, n_cities):
        dist = euclidean_distance(cities.iloc[i][['X', 'Y']], cities.iloc[j][['X', 'Y']])
        distance_matrix[i, j] = dist
        distance_matrix[j, i] = dist  # Simetría

print("Matriz de distancias:\n", distance_matrix)

# Función para calcular la distancia total de una ruta
def total_distance(route, distance_matrix):
    distance = 0
    for i in range(len(route) - 1):
        distance += distance_matrix[route[i], route[i + 1]]
    distance += distance_matrix[route[-1], route[0]]  # Regresar al punto inicial
    return distance

# Crear una población inicial de rutas aleatorias
def create_initial_population(pop_size, n_cities):
    population = []
    for _ in range(pop_size):
        route = random.sample(range(n_cities), n_cities)
        population.append(route)
    return population

# Selección basada en la aptitud (menor distancia)
def selection(population, fitness_scores):
    selected = random.choices(population, weights=[1/f for f in fitness_scores], k=2)
    return selected

# Cruce entre dos rutas
def crossover(parent1, parent2):
    size = len(parent1)
    start, end = sorted(random.sample(range(size), 2))
    
    child = [-1] * size
    child[start:end] = parent1[start:end]
    
    pointer = 0
    for i in range(size):
        if parent2[i] not in child:
            while child[pointer] != -1:
                pointer += 1
            child[pointer] = parent2[i]
    
    return child

# Mutación: intercambio aleatorio de dos ciudades
def mutate(route, mutation_rate=0.01):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(route)), 2)
        route[i], route[j] = route[j], route[i]

# Evaluación de la aptitud de la población
def evaluate_population(population, distance_matrix):
    fitness_scores = [total_distance(route, distance_matrix) for route in population]
    return fitness_scores

# Algoritmo genético para resolver el TSP
def genetic_algorithm(n_cities, distance_matrix, pop_size=100, generations=500, mutation_rate=0.01):
    population = create_initial_population(pop_size, n_cities)
    
    best_route = None
    best_distance = float('inf')
    
    for gen in range(generations):
        fitness_scores = evaluate_population(population, distance_matrix)
        
        new_population = []
        for _ in range(pop_size // 2):
            parent1, parent2 = selection(population, fitness_scores)
            child1 = crossover(parent1, parent2)
            child2 = crossover(parent2, parent1)
            mutate(child1, mutation_rate)
            mutate(child2, mutation_rate)
            new_population.extend([child1, child2])
        
        population = new_population
        
        current_best_distance = min(fitness_scores)
        if current_best_distance < best_distance:
            best_distance = current_best_distance
            best_route = population[fitness_scores.index(best_distance)]
        
        print(f"Generación {gen + 1}: Mejor distancia = {best_distance}")
    
    return best_route, best_distance

# Ejecutar el algoritmo genético
best_route, best_distance = genetic_algorithm(n_cities, distance_matrix, pop_size=100, generations=500, mutation_rate=0.01)

print("Mejor ruta encontrada:", best_route)
print("Distancia total de la mejor ruta:", best_distance)

# Visualizar la mejor ruta
def plot_route(route, cities):
    plt.figure(figsize=(8, 6))
    x = cities['X'].values
    y = cities['Y'].values
    
    route_cities = cities.iloc[route]
    plt.plot(route_cities['X'], route_cities['Y'], marker='o', color='b', linestyle='-')
    
    plt.scatter(x, y, color='red')
    for i, (x_pos, y_pos) in enumerate(zip(x, y)):
        plt.text(x_pos, y_pos, str(i), fontsize=12)
    
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Ruta óptima encontrada por el algoritmo genético")
    plt.show()

# Graficar la mejor ruta y mostrar
plot_route(best_route, cities)
