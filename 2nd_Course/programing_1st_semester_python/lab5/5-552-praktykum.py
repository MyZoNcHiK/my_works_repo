mountains = {
    "Hoverla": 2061,
    "Brebenescul": 2032,
    "Pip Ivan Chernogirsky (Chorna gora)": 2028,
    "Petros": 2020,
    "Gutin Tomnatyk": 2016,
    "Rebra": 2001,
    "Menchul": 1998,
    "Turkul": 1933,
    "Danzher": 1850,
    "Pozhyzhevska": 1822
}

top = sorted(mountains.items(), key=lambda x: x[1], reverse=True)

for name, height in top[:3]:
    print(f"{name}: {height} m")
