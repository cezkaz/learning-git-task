print("Lista zakupów_git")

expenditures = {
    "piekarnia": ["chleb", "bułki", "pączek"],
    "warzywniak": ["marchew", "seler", "rukola"]
}
for expenditure_name, expenditure in expenditures.items():
    # print(f"Ide do {expenditure_name.capitalize()} i kupuję tu następujące rzeczy: {expenditure[0].capitalize()}")
    print(f"Ide do {expenditure_name.capitalize()} i kupuję tu następujące rzeczy: {expenditure[0].capitalize()}, "
          f"{expenditure[1].capitalize()}, {expenditure[2].capitalize()}")
print(f"W sumie kupuję {len(expenditure) + len(expenditure)} produktów")