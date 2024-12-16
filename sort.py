companies = [
    ("Google", 2007, 134.81),
    ("Facebook", 2003, 133.5),
    ("Amazon", 2008, 70.5),
]
companies.sort(key=lambda company:company[2])
print(companies)
result = sorted(companies, key=lambda company:company[1])
print(result)
print(companies)