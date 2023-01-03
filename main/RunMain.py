import os, unittest

def load_all_test():
    """
        批量加载全部用例
    :return:
    """
    # 获取测试用例文件路径
    case_path = os.path.join(os.getcwd(), "../case")
    discover = unittest.defaultTestLoader.discover(case_path,pattern="*Case.py",top_level_dir=None)
    print(discover)
    return discover

if __name__ == '__main__':
    discover = load_all_test()
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(discover)
