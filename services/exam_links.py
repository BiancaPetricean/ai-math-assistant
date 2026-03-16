import random

bac_links = [

"https://subiecte.edu.ro/2023/bacalaureat/Matematica/MATE_INFO_VAR1_2023.pdf",

"https://subiecte.edu.ro/2022/bacalaureat/Matematica/MATE_INFO_VAR2_2022.pdf",

"https://subiecte.edu.ro/2021/bacalaureat/Matematica/MATE_INFO_VAR1_2021.pdf",

"https://subiecte.edu.ro/2020/bacalaureat/Matematica/MATE_INFO_VAR1_2020.pdf"

]


class8_links = [

"https://subiecte.edu.ro/2023/evaluare-nationala/matematica/EN_Var1_2023.pdf",

"https://subiecte.edu.ro/2022/evaluare-nationala/matematica/EN_Var1_2022.pdf",

"https://subiecte.edu.ro/2021/evaluare-nationala/matematica/EN_Var1_2021.pdf"

]


def random_bac():

    return random.choice(bac_links)


def random_class8():

    return random.choice(class8_links)