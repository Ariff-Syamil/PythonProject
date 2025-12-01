# import prettytable from pypi
# https://pypi.org/
# https://code.google.com/archive/p/prettytable/wikis/Tutorial.wiki

from prettytable import PrettyTable
table = PrettyTable()

table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Electric","Water","Fire"])
table.align = "r"
print(table)