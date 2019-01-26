import allure


@allure.step(title="登录标题")
def test_login():
    print("aaa")
    allure.attach("登录","账号")
    allure.attach("登录","密码")
    allure.attach("密码")
    allure.attach("登录","点击登录")
    assert 1

def test_b():
    print("bbb")
    assert 0