# pep8的代码风格


## 1.缩进

### 1.1 使用四个空格缩进（或使用同一种格式，不混用tab和空格）（或使用tab转空格）

### 1.2 参数或条件过多时的换行缩进
* 函数定义，函数调用，if条件,数组定义

```
foo = long_function_name(var_one, var_two,
                         var_three, var_four)
foo = long_function_name(
    var_one, var_two,
    var_three, var_four)
```
```
def long_function_name(
        var_one, var_two, var_three,
        var_four):
    print(var_one)
```
```
if (this_is_one_thing and
    that_is_another_thing):
    do_something()
```
```
my_list = [
    1, 2, 3,
    4, 5, 6,
    ]
```


## 2.行字符限制

### 2.1 代码行限制 79 个字符；文档/注释行限制 72 个字符
### 2.2 必要可以用反斜杠续行
```
with open('/path/to/some/file/you/want/to/read') as file_1, \
     open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())
```


## 3.运算符的换行
```
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)
```


## 4.空白行

### 4.1 顶级函数和类前后都用两行空行
### 4.2 类内部函数前后用一行空行
### 4.3 功能组之间可加额外空行
### 4.4 函数内部空行由逻辑决定


## 5.文件编码

### 5.1 Python核心发布版本中的代码总是以UTF-8格式编码（或者在Python2中用ASCII编码）。
### 使用ASCII（在Python2中）或UTF-8（在Python3中）编码的文件不应具有编码声明。 


## 6.引入模块

### 6.1 位置：在模块注释和全局变量定义之间
### 6.2 顺序：
> (1) 系统包  
> (2) 第三方包  
> (3) 自己写的本地包  
### 6.3 建议的是使用绝对路径导入包


## 7.引号

### 7.1 一般情况选择单引号或双引号一种使用
### 7.2 引号内还要引号时合用单双引号，不需要转义


## 8.空格
```
spam(ham[1], {eggs: 2})
foo = (0,)
if x == 4: print x, y; x, y = y, x（鼓励不使用复合句）
```
```
切片没逻辑运算时不加空格，有时加：两边空格
ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
ham[lower:upper], ham[lower:upper:], ham[lower::step]
ham[lower+offset : upper+offset]
ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
ham[lower + offset : upper + offset]
```
```
最低优先级两边加空格
i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)
```
```
参数等号不加空格
def complex(real, imag=0.0):
    return magic(r=real, i=imag)
```


## 9.逗号

### 9.1 尾随逗号
```
FILES = [
    'setup.cfg',
    'tox.ini',
    ]
initialize(FILES,
           error=True,
           )
```

## 10.命名

### 10.1 全小写，全大写，全小写下划线,全大写下划线，首字母大写拼接，驼峰式

## 11.[编程建议](https://www.python.org/dev/peps/pep-0008/#programming-recommendations)
