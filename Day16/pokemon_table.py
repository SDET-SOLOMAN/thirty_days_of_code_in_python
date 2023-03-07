from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type",["Electric Freak", "Water Damage", "Fire Psycho"])
table.align = 'l'


print(table)

