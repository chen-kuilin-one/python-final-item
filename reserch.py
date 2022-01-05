def reserch4letters(py_vowels,py_word):
    """
    :param py_vowels: 在index.html默认的aeiou参数
    :param py_word: 用户在index.html输入的word参数
    :return: 返回词频字典结果
    """
    py_found = {}
    for i in py_word:
        if i in py_vowels:
            # 初始化 setdefault
            py_found.setdefault(i, 0)
            py_found[i] += 1
    return py_found