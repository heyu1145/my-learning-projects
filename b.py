def repeatfn(limit:int = 1000) -> bool:
    try:
        lines:list[str] = [
                    "try:\n",
                    "    a = int(input())\n",
                    "except ValueError:\n",
                    "    exit(1)\n",
                    "if a == 0:\n",
                    "    print('even')\n"
                ]
        for i in range(1, limit + 1):
            a = 'even' if i % 2 == 0 else 'odd'
            lines.append(f"elif a == {i}:\n")
            lines.append(f"    print('{a}')\n")
        with open('a.py','w') as f:
            f.writelines(lines)
        return True
    except Exception:
        return False

print(repeatfn(1500))
