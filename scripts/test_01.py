"""
Allure报告
    1、安装 pip install pytest-allure-adaptor
    2、pytest.ini配置文件 addopts = -s --alluredir report
    3、生成报告 为 xml 文件
    4、allure-2.6.0 文件 路径配置环境变量path
    5、对生成的xml文件 更改为html
    6、Terminal 窗口运行  allure generate report/ -o report/html --clean (清空原有报告，重新生成报告)

Allure报告增强
1、添加步骤
    语法：allure.step(title = "原因")
2、添加描述
    语法: allure.attach("描述","原因")
    注意：1）只能修饰函数体
         2）两个参数一个都不能少
3、添加用例优先级
    语法：@pytest.allure.severity(pytest.allure.severity_level.MINOR)

"""
import allure
import pytest


class Test01():
    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title ="执行登录！")
    def test_01(self):
        allure.attach("失败原因","账户错误")
        print("test02")



    @allure.step(title = "执行退出登录！")
    def test_02(self):
        with open('./img/aa.jpeg','rb')as f:
            allure.attach("失败原因",f.read(),allure.attach_type.PNG)
        assert 0

    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    def test_03(self):
        print("test03")