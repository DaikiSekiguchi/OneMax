# coding: utf-8

from . import ga_onemax

# Parameter
SELECT_RATE = 0.5  # 選択割合
MUTATE_RATE = 0.1  # 突然変異の確立
GENE_SIZE = 10  # 個体がもつ0/1のリスト長さ
POPULATION_SIZE = 10  # 集団の個体数
GENERATION = 25  # 世代数

# インスタンスを生成
ga_one_max = ga_onemax.GA_OneMax(GENE_SIZE, POPULATION_SIZE, SELECT_RATE, MUTATE_RATE)

# 1. 初期集団を生成
ga_one_max.generate_initial_population()

for i in range(GENERATION):
    print("{0}世代".format(i + 1))

    # 2. 選択
    ga_one_max.selection()

    # 3. 交叉
    ga_one_max.crossover()

    # 4. 突然変異
    ga_one_max.mutate()

    # 集合に属する個体の情報を描画する
    ga_one_max.draw_population_info()
