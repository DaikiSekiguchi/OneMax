# coding: utf-8

import random
import copy


# 個体の適応度を計算する
def calc_fitness(individual):
    return sum(individual)


class GA_OneMax:

    # 初期化
    def __init__(self, gene_size, population_size, select_rate, mutate_rate):
        self.gene_size = gene_size
        self.population_size = population_size
        self.select_rate = select_rate
        self.mutate_rate = mutate_rate

        self.population = []                # 集団
        self.individuals_fitness = []       # 集合に属する各個体の適応度
        self.selected_individuals = []      # 選択で残った適応度の高い個体群
        self.child_individuals = []         # 交叉、突然変異を経て新たに生成された個体群

    # 1. 初期集団を生成する
    def generate_initial_population(self):

        for _ in range(self.population_size):
            # 個体(の遺伝子情報を格納するリスト)
            individual = []

            # ランダムに0か1を選択し、個体の情報(遺伝子)を設定する
            for _ in range(self.gene_size):
                individual.append(random.randint(0, 1))

            # 集団に個体を追加する
            self.population.append(individual)

        # 集合の各個体の適応度を計算し、適応度が高い順にsortする
    def sort_fitness(self):
        # 各個体の適応度を計算する
        for individual in self.population:
            fitness = calc_fitness(individual)
            self.individuals_fitness.append([individual, fitness])

        # 適応度が高い順にソートする
        self.individuals_fitness.sort(key=lambda x: x[1], reverse=True)

    # 2. 指定した選択割合に基づき、適応度の高い個体を残す
    def selection(self):
        # 適応度が高い順に集団をソートする
        self.sort_fitness()
        
        # 残す個体の数を指定
        n = int(self.select_rate * self.population_size)

        for i in range(n):
            self.selected_individuals.append(copy.deepcopy(self.individuals_fitness[i][0]))

    # 3. 選択された適応度の高い個体群(集合)から任意に２個体を選択し、交叉させ、子を生成する
    def crossover(self):

        # 新しく生成する子(個体)の数
        num_crossover = self.population_size - len(self.selected_individuals)

        # 交叉を行う数だけ、子を生成する
        for i in range(num_crossover):
            parent = random.sample(self.selected_individuals, 2)   # 残った個体群から2つの個体を選択する(重複なし)
            intersection = random.randint(1, self.gene_size - 2)   # 交叉点

            parent1_gene = copy.deepcopy(parent[0][0:intersection])
            parent2_gene = copy.deepcopy(parent[1][intersection:])

            # 子を生成
            parent1_gene.extend(parent2_gene)

            # 子をリストに格納
            self.child_individuals.append(parent1_gene)

    # 4. 一定の確率で突然変異させる
    def mutate(self):
        for individual in self.child_individuals:
            for i in range(len(individual)):
                n = random.random()
                if n < self.mutate_rate:
                    individual[i] = random.randint(0, 1)

        # 新しい集団 = 選択された個体群(親) + 新しく生成された個体群(子)
        self.selected_individuals.extend(self.child_individuals)
        self.population = copy.deepcopy(self.selected_individuals)

        # 変数を初期化
        self.reset()

    # 変数の初期化
    def reset(self):
        self.individuals_fitness = []
        self.selected_individuals = []
        self.child_individuals = []

    # 集団に属する各個体の遺伝子情報を表示する
    def draw_population_info(self):
        for individual in self.population:
            print(individual)

