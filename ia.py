from sklearn import tree

# Datos de entrenamiento: [Peso en gramos, Textura (1 para lisa, 0 para rugosa)]
# Manzanas suelen ser lisas (1), Naranjas suelen ser rugosas (0)
caracteristicas = [[140, 1], [130, 1], [150, 0], [170, 0]]

# Etiquetas: 0 para Manzana, 1 para Naranja
etiquetas = [0, 0, 1, 1]

# Creamos el "cerebro" de nuestra IA (un árbol de decisión)
clasificador = tree.DecisionTreeClassifier()

# Entrenamos a la IA con los datos
clasificador.fit(caracteristicas, etiquetas)

# Le pedimos que adivine una fruta nueva: 160 gramos y textura rugosa (0)
resultado = clasificador.predict([[160, 0]])

if resultado[0] == 0:
    print("La IA dice: ¡Es una Manzana!")
else:
    print("La IA dice: ¡Es una Naranja!")