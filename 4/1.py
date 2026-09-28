import csv

algoritm = [
    "C4.5",
    "k - means",
    "Метод опорных векторов",
    "Apriori",
    "EM",
    "PageRank",
    "AdaBoost",
    "kNN",
    "Наивный байесовский классификатор",
    "CART"
]

with open("algoritm.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "значение"])

    for i, value in enumerate(algoritm, start=1):
        writer.writerow([i, value])
