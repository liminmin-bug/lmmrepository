import pytest
import allure

class Testclass():
    def test01(self,login):
        print("测试用例1")

    def test02(self):
        print("测试用例2")

    def test03(self,login):
        print("测试用例3")

#
# if __name__ == '__main__':
#     pytest.main(["-s","F:\lmm-test\pytestallure\test.py"])
