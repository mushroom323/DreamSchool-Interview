def Parentheses(sentence=""):
    """
    :type sentence: str
    """
    if sentence == "":
        sentence = input()
    count = 0
    ans = " " * len(sentence)
    ans = list(ans)
    # 从左往右查 )
    for i in range(len(sentence)):
        if sentence[i] == "(":
            count += 1
        elif sentence[i] == ")":
            if count == 0:
                ans[i] = "?"
            else:
                count -= 1
    count = 0
    # 从右往左查 (
    for i in range(len(sentence)):
        j = len(sentence) - 1 - i
        if sentence[j] == ")":
            count += 1
        elif sentence[j] == "(":
            if count == 0:
                ans[j] = "x"
            else:
                count -= 1
    print(sentence)
    print("".join(ans))

# test
Parentheses("bge)))))))))")
Parentheses("((IIII))))))")
Parentheses("()()()()(uuu")
Parentheses("))))UUUU((()")

