hmap: dict = {}

hmap[12836] = " 小哈"
hmap[15937] = " 小囉"
hmap[16750] = " 小算"
hmap[13276] = " 小法"
hmap[10583] = " 小鴨"

name: str = hmap[15937]

hmap.pop(10583)

for key, value in hmap.items():
    print(key, "->", value)

for key in hmap.keys():
    print(key)

for value in hmap.values():
    print(value)
