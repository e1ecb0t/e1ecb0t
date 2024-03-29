# OS操作, 传入表达式/答案/正确率保存到文件
import os
from re import split

from utils.Calculate import *

# 获取文件当前位置
current_path = os.path.dirname(os.path.abspath(__file__))

root_path = os.path.dirname(current_path)

# 文件保存位置
if not os.path.exists(root_path):
    try:
        os.mkdir(root_path)
    except:
        raise FileNotFoundError


# 检查
def inspect(answer_file, expression_file):
    # 正确错误列表序号
    correct_seq = []
    wrong_seq = []

    try:
        # 读取文件
        with open(expression_file, 'r', encoding='utf-8') as fa:
            expression_content = fa.readlines()
        # 读取文件
        with open(answer_file, 'r', encoding='utf-8') as fb:
            answer_content = fb.readlines()

        # 由答案文件获取序号 再在运算式中找到相对应的题目计算答案 再比较
        # 获取列表
        for item_b in answer_content:

            # 当前答案的行数的序列号
            answer_sqe, answer = int(item_b.split('. ')[0]), item_b.split('. ')[1]

            # 找到对应的习题的行数
            expression = expression_content[answer_sqe - 1]

            # ###############################################
            # print(answer_sqe, expression)

            # 分割字符
            pattern = expression.strip().replace(' ', '').replace('　', '').split('.')[1]
            pattern = list(filter(None, split(r'([()×÷+-])', pattern)))

            # 提取表达式并计算 如若正确存进
            if Calculate(pattern).cal_expression()[0].to_string() == answer.strip():
                correct_seq.append(answer_sqe)

        # 生成错误列表
        for item_a in expression_content:
            a_sqe = int(item_a.split('. ')[0])
            if a_sqe not in correct_seq:
                wrong_seq.append(a_sqe)

        inspect_file = root_path + '/Grade.txt'
        try:
            with open(inspect_file, 'w+', encoding='utf-8') as f:
                f.write(f'Correct: {len(correct_seq)} {correct_seq}\n'
                        f'Wrong: {len(wrong_seq)} {wrong_seq}\n'
                        f'Accuracy: {round(len(correct_seq) / (len(wrong_seq) + len(correct_seq)), 4) * 100}%\n')
        except IOError:
            print('Grade.txt create failed. Please check again')
    except IOError:
        print('Failed to open file')
        return


# 保存题目 传入序列号以及题目
def save_exercise(expressions_list, order):
    exercise_file = root_path + '/Exercises{}.txt'.format(order)
    try:
        with open(exercise_file, 'a+', encoding='utf-8') as f:
            for line in expressions_list:
                f.write('{}\n'.format(line))
    except IOError:
        print('Exercise.txt create failed. Please check again')


# 保存答案 传入序列号以及答案
def save_answer(answers_list, order):
    answer_file = root_path + '/Answer{}.txt'.format(order)
    try:
        with open(answer_file, 'a+', encoding='utf-8') as f:
            for line in answers_list:
                f.write('{}\n'.format(line))
    except IOError:
        print('Answer.txt create failed. Please check again')


