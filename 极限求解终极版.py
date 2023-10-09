import sympy

# 定义自变量x和函数y
x = sympy.symbols('x')
y = sympy.sympify(input("请输入函数y(x): "))

# 输入趋向的值
print('如输入无穷请输入oo')
c = sympy.sympify(input("请输入趋向的值c: "))

# 计算x趋向c时的极限
limit_at_c = sympy.limit(y, x, c)

print('当x趋向', c, '时的极限：', limit_at_c)

# 等待用户输入，防止命令行窗口自动关闭
input("按任意键退出")