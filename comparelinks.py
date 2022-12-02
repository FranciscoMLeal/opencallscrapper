## This function will serve to compare links

# Falta comparar os Links
# Falta fazer o append dos novos links com os antigos


old_links = [
"FORD","ALPHA","PRIUS","BABA","TRES"
]


new_links = [
"FORD","ALPHA","PRIUS","BABA","RATO","NIssan","toyota","honda"
]


old_links.sort()
new_links.sort()

rmlinks = []

for c in new_links:
    for a in old_links:
        if c == a:
            rmlinks.append(c)

for rm in rmlinks:
    new_links.remove(rm)

for d in new_links:
	print(d)
