
s = input("")
ans = ""
res = []


def dfs(s, n, ip):
    if n == 4:
        if len(s) == 0:
            res.append(ip)
    else:
        for i in range(1, 4):
            if len(s) < i:
                break
            ss = s[0:i]
            val = int(ss)
            if val > 255 or s[0] == '0':
                continue

            if n < 3:
                dfs(s[i:], n+1, ip+ss+".")
            else:
                dfs(s[i:], n+1, ip+ss)
    return


dfs(s, 0, ans)

print(res)