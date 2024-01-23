def main() -> None:
    pass  # Kezd a kódolást itt!


# Klasszikus for ciklus megvalósitása pythonban.
# számsorozat bejárás
# for(int i = 0 ; i< 10 ; i ++) print(i)
for i in range(0, 10):
    print(i)


# napok: list[str] = []
# napok.append("Hétfő")
# napok.append("Kedd")
# napok.append("Szerda")

napok: list[str] = ["Hétfő", "Kedd", "Szerda"]
for nap in napok:
    print(nap)
for i in range(0, len(napok)):
    print(f"{i+1}. ->{napok[i]}")
# i -> index ; e -> elem
for i, e in enumerate(napok):
    print(f"napok[{i}]=[{e}]")
# bejárás az első leme kihagyásával
for nap in napok[1:]:
    print(nap)
# utolsó elem a listában
print(napok[-1])


if __name__ == "__main__":
    main()
