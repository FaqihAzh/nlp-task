from tabulate import tabulate

def levenshtein_distance(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)

    # Membuat tabel 2D dengan ukuran (len_str1+1) x (len_str2+1)
    dp = [[0 for _ in range(len_str2 + 1)] for _ in range(len_str1 + 1)]

    for i in range(len_str1 + 1):
        dp[i][0] = i  # Mengisi jarak saat salah satu string kosong
    for j in range(len_str2 + 1):
        dp[0][j] = j

    for i in range(1, len_str1 + 1):
        for j in range(1, len_str2 + 1):
            if str1[i - 1] == str2[j - 1]:
                cost = 0
            else:
                cost = 2

            dp[i][j] = min(
                dp[i - 1][j] + 1,        # delete
                dp[i][j - 1] + 1,        # insert
                dp[i - 1][j - 1] + cost  # substitute
            )

    headers = [''] + list(str2)
    dp_table = [[str1[i - 1]] + dp[i] for i in range(1, len_str1 + 1)]
    dp_table.insert(0, [''] + dp[0])
    print(tabulate(dp_table, headers=headers, tablefmt="grid"))

    edit_distance = dp[len_str1][len_str2]

    changes = []
    i, j = len_str1, len_str2

    while i > 0 or j > 0:
        if i > 0 and j > 0 and dp[i][j] == dp[i - 1][j - 1] + (0 if str1[i - 1] == str2[j - 1] else 2):
            if str1[i - 1] != str2[j - 1]:
                changes.append(f"Substitute '{str1[i - 1]}' dengan '{str2[j - 1]}' pada posisi {i}")
            i -= 1
            j -= 1
        elif i > 0 and dp[i][j] == dp[i - 1][j] + 1:
            changes.append(f"Delete '{str1[i - 1]}' dari posisi {i}")
            i -= 1
        else:
            changes.append(f"Insert '{str2[j - 1]}' pada posisi {j}")
            j -= 1

    changes.reverse()
    for change in changes:
        print(change)

    return edit_distance

str1 = "KOMPUTER"
str2 = "BLUNDER"
result = levenshtein_distance(str1, str2)
print(f"\nMinimum Edit Distance (MED) untuk kata '{str1}' dan kata '{str2}' adalah {result}")
