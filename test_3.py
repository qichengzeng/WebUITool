import os
import inspect
from base_method import BasePage
class Test:
  def __init__(self):
   self.back_data_list = []
def package_excute_method(self,test_case):
    with open(os.path.join(os.path.dirname(__file__), "SERVICEIP.ini"), "r") as f:
        ip_text = f.read()
    self.driver_true.get(ip_text + test_case.url)
    self.driver_true.maximize_window()
    self.excute_script = BasePage(self.driver_true, test_case.title + ".log")
    # self.excute_script.logger.info("\n")
    self.excute_script.logger.info("{}_用例开始执行".format(test_case.title))
    self.true_dict = self.excute_script.back_method_dict()
    for i in range(0, len(test_case.step)):
        if test_case.page[i] == "NONE":  # 此时为浏览器没有元素定位操作和python语句操作
            para_num = len(inspect.getfullargspec(self.true_dict[test_case.step[i]]).args)
            if para_num > 1:  # 有参数
                if para_num == 2:
                    if test_case.step[i] == "get":
                        if test_case.data[i].endswith(".web"):
                            index = int(test_case.data[i].split(".")[0])
                            back_data = self.true_dict[test_case.step[i]](ip_text + self.global_para[index])
                        else:
                            back_data = self.true_dict[test_case.step[i]](ip_text+test_case.data[i])
                            self.back_data_list.append(back_data)
                        if back_data:  # 判断是否有返回值
                            if test_case.data_transfer[i]:
                                if len(eval(test_case.data_transfer[i])) == 3:  # 判断是否有参数传递
                                    num = int(eval(test_case.data_transfer[i])[0]) - 1
                                    if int(eval(test_case.data_transfer[i])[1]) == 1:
                                       test_case.data[num] = back_data
                                    if int(eval(test_case.data_transfer[i])[1]) == 2:
                                        test_case.data_two[num] = back_data
                                    if int(eval(test_case.data_transfer[i])[1]) == 3:
                                        test_case.data_three[num] = back_data
                                    index = eval(test_case.data_transfer[i])[2]
                                    self.global_para[index] = back_data
                                if len(eval(test_case.data_transfer[i])) == 1:
                                    index = eval(test_case.data_transfer[i])[0]
                                    self.global_para[index] = back_data
                                if len(eval(test_case.data_transfer[i])) == 2:
                                    num = int(eval(test_case.data_transfer[i])[0]) - 1
                                    if int(eval(test_case.data_transfer[i])[1]) == 1:
                                        test_case.data[num] = back_data
                                    if int(eval(test_case.data_transfer[i])[1]) == 2:
                                        test_case.data_two[num] = back_data
                                    if int(eval(test_case.data_transfer[i])[1]) == 3:
                                        test_case.data_three[num] = back_data
                    else:
                        if test_case.data[i].endswith(".web"):
                            index = int(test_case.data[i].split(".")[0])
                            back_data = self.true_dict[test_case.step[i]](self.global_para[index])
                            self.back_data_list.append(back_data)
                        else:
                            back_data = self.true_dict[test_case.step[i]](test_case.data[i])
                            self.back_data_list.append(back_data)
                        if back_data:  # 判断是否有返回值
                            if test_case.data_transfer[i]:
                                if len(eval(test_case.data_transfer[i])) == 3:  # 判断是否有参数传递
                                    num = int(eval(test_case.data_transfer[i])[0]) - 1
                                    if int(eval(test_case.data_transfer[i])[1]) == 1:
                                        test_case.data[num] = back_data
                                    if int(eval(test_case.data_transfer[i])[1]) == 2:
                                        test_case.data_two[num] = back_data
                                    if int(eval(test_case.data_transfer[i])[1]) == 3:
                                        test_case.data_three[num] = back_data
                                    index = eval(test_case.data_transfer[i])[2]
                                    self.global_para[index] = back_data
                                if len(eval(test_case.data_transfer[i])) == 1:
                                    index = eval(test_case.data_transfer[i])[0]
                                    self.global_para[index] = back_data
                                if len(eval(test_case.data_transfer[i])) == 2:
                                    num = int(eval(test_case.data_transfer[i])[0]) - 1
                                    if int(eval(test_case.data_transfer[i])[1]) == 1:
                                        test_case.data[num] = back_data
                                    if int(eval(test_case.data_transfer[i])[1]) == 2:
                                        test_case.data_two[num] = back_data
                                    if int(eval(test_case.data_transfer[i])[1]) == 3:
                                        test_case.data_three[num] = back_data
                if para_num == 3:
                    if test_case.data[i].endswith(".web"):
                        test_case.data[i] = (self.global_para[int(test_case.data[i].split(".")[0])])
                    if test_case.data_two[i].endswith(".web"):
                            test_case.data_two[i] = self.global_para[int(test_case.data_two[i].split(".")[0])]

                    back_data = self.true_dict[test_case.step[i]](test_case.data[i],test_case.data_two[i])
                    self.back_data_list.append(back_data)
                    if back_data:  # 判断是否有返回值
                        if test_case.data_transfer[i]:
                            if len(eval(test_case.data_transfer[i])) == 3:  # 判断是否有参数传递
                                num = int(eval(test_case.data_transfer[i])[0]) - 1
                                if int(eval(test_case.data_transfer[i])[1]) == 1:
                                    test_case.data[num] = back_data
                                if int(eval(test_case.data_transfer[i])[1]) == 2:
                                    test_case.data_two[num] = back_data
                                if int(eval(test_case.data_transfer[i])[1]) == 3:
                                    test_case.data_three[num] = back_data
                                index = eval(test_case.data_transfer[i])[2]
                                self.global_para[index] = back_data
                            if len(eval(test_case.data_transfer[i])) == 1:
                                index = eval(test_case.data_transfer[i])[0]
                                self.global_para[index] = back_data
                            if len(eval(test_case.data_transfer[i])) == 2:
                                num = int(eval(test_case.data_transfer[i])[0]) - 1
                                if int(eval(test_case.data_transfer[i])[1]) == 1:
                                    test_case.data[num] = back_data
                                if int(eval(test_case.data_transfer[i])[1]) == 2:
                                    test_case.data_two[num] = back_data
                                if int(eval(test_case.data_transfer[i])[1]) == 3:
                                    test_case.data_three[num] = back_data
                if para_num == 4:
                    if test_case.data[i].endswith(".web"):
                            test_case.data[i] = self.global_para[int(test_case.data[i].split(".")[0])]
                    if test_case.data_two[i].endswith(".web"):
                        test_case.data_two[i] = self.global_para[int(test_case.data_two[i] .split(".")[0])]
                    if test_case.data_three[i].endswith(".web"):
                        test_case.data_three[i] = self.global_para[int(test_case.data_three[i] .split(".")[0])]
                    back_data = self.true_dict[test_case.step[i]](test_case.data[i],test_case.data_two[i],test_case.data_three[i] )
                    self.back_data_list.append(back_data)
                    if back_data:  # 判断是否有返回值
                        if test_case.data_transfer[i]:
                            if len(eval(test_case.data_transfer[i])) == 3:  # 判断是否有参数传递
                                num = int(eval(test_case.data_transfer[i])[0]) - 1
                                if int(eval(test_case.data_transfer[i])[1]) == 1:
                                    test_case.data[num] = back_data
                                if int(eval(test_case.data_transfer[i])[1]) == 2:
                                    test_case.data_two[num] = back_data
                                if int(eval(test_case.data_transfer[i])[1]) == 3:
                                    test_case.data_three[num] = back_data
                                index = eval(test_case.data_transfer[i])[2]
                                self.global_para[index] = back_data
                            if len(eval(test_case.data_transfer[i])) == 1:
                                index = eval(test_case.data_transfer[i])[0]
                                self.global_para[index] = back_data
                            if len(eval(test_case.data_transfer[i])) == 2:
                                num = int(eval(test_case.data_transfer[i])[0]) - 1
                                if int(eval(test_case.data_transfer[i])[1]) == 1:
                                    test_case.data[num] = back_data
                                if int(eval(test_case.data_transfer[i])[1]) == 2:
                                    test_case.data_two[num] = back_data
                                if int(eval(test_case.data_transfer[i])[1]) == 3:
                                    test_case.data_three[num] = back_data
            else:  # 无参数
                back_data = self.true_dict[test_case.step[i]]()
                self.back_data_list.append(back_data)
                if back_data:  # 判断是否有返回值
                    if test_case.data_transfer[i]:
                        if len(eval(test_case.data_transfer[i])) == 3:  # 判断是否有参数传递
                            num = int(eval(test_case.data_transfer[i])[0]) - 1
                            if int(eval(test_case.data_transfer[i])[1]) == 1:
                                test_case.data[num] = back_data
                            if int(eval(test_case.data_transfer[i])[1]) == 2:
                                test_case.data_two[num] = back_data
                            if int(eval(test_case.data_transfer[i])[1]) == 3:
                                test_case.data_three[num] = back_data
                            index = eval(test_case.data_transfer[i])[2]
                            self.global_para[index] = back_data
                        if len(eval(test_case.data_transfer[i])) == 1:
                            index = eval(test_case.data_transfer[i])[0]
                            self.global_para[index] = back_data
                        if len(eval(test_case.data_transfer[i])) == 2:
                            num = int(eval(test_case.data_transfer[i])[0]) - 1
                            if int(eval(test_case.data_transfer[i])[1]) == 1:
                                test_case.data[num] = back_data
                            if int(eval(test_case.data_transfer[i])[1]) == 2:
                                test_case.data_two[num] = back_data
                            if int(eval(test_case.data_transfer[i])[1]) == 3:
                                test_case.data_three[num] = back_data
        else:  # 为浏览器存在元素定位操作
            para_num = len(inspect.getfullargspec(self.true_dict[test_case.step[i]]).args)
            locator_name = self.cf.back_locator_tuple(test_case.page[i],test_case.locator_name[i])
            if para_num > 2:  # 有参数
                if para_num == 3:
                    if test_case.data[i] == "USERNAME":
                        file_path = os.path.join(os.path.dirname(__file__), "LOGIN.ini")
                        with open(file_path, "r") as f:
                            read_text = f.read()
                            read_list = read_text.split(";")
                        self.true_dict[test_case.step[i]](locator_name, read_list[0])
                        continue
                    if test_case.data[i] == "PASSWORD":
                        file_path = os.path.join(os.path.dirname(__file__), "LOGIN.ini")
                        with open(file_path, "r") as f:
                            read_text = f.read()
                            read_list = read_text.split(";")
                        self.true_dict[test_case.step[i]](locator_name, read_list[1])
                        continue
                    if test_case.data[i].endswith(".web"):
                        test_case.data[i] = self.global_para[int(test_case.data[i].split(".")[0])]
                    back_data = self.true_dict[test_case.step[i]](locator_name,test_case.data[i])
                    self.back_data_list.append(back_data)
                    if back_data:  # 判断是否有返回值
                        if test_case.data_transfer[i]:
                            if len(eval(test_case.data_transfer[i])) == 3:  # 判断是否有参数传递
                                num = int(eval(test_case.data_transfer[i])[0]) - 1
                                if int(eval(test_case.data_transfer[i])[1]) == 1:
                                    test_case.data[num] = back_data
                                if int(eval(test_case.data_transfer[i])[1]) == 2:
                                    test_case.data_two[num] = back_data
                                if int(eval(test_case.data_transfer[i])[1]) == 3:
                                    test_case.data_three[num] = back_data
                                index = eval(test_case.data_transfer[i])[2]
                                self.global_para[index] = back_data
                            if len(eval(test_case.data_transfer[i])) == 1:
                                index = eval(test_case.data_transfer[i])[0]
                                self.global_para[index] = back_data
                            if len(eval(test_case.data_transfer[i])) == 2:
                                num = int(eval(test_case.data_transfer[i])[0]) - 1
                                if int(eval(test_case.data_transfer[i])[1]) == 1:
                                    test_case.data[num] = back_data
                                if int(eval(test_case.data_transfer[i])[1]) == 2:
                                    test_case.data_two[num] = back_data
                                if int(eval(test_case.data_transfer[i])[1]) == 3:
                                    test_case.data_three[num] = back_data
                if para_num == 4:
                    if test_case.data[i].endswith(".web"):
                        test_case.data[i] = self.global_para[int(test_case.data[i].split(".")[0])]
                    if test_case.data_two[i].endswith(".web"):
                        test_case.data_two[i] = self.global_para[int(test_case.data_two[i].split(".")[0])]
                    back_data = self.true_dict[test_case.step[i]](locator_name,test_case.data[i],test_case.data_two[i])
                    self.back_data_list.append(back_data)
                    if back_data:  # 判断是否有返回值
                        if test_case.data_transfer[i]:
                            if len(eval(test_case.data_transfer[i])) == 3:  # 判断是否有参数传递
                                num = int(eval(test_case.data_transfer[i])[0]) - 1
                                if int(eval(test_case.data_transfer[i])[1]) == 1:
                                    test_case.data[num] = back_data
                                if int(eval(test_case.data_transfer[i])[1]) == 2:
                                    test_case.data_two[num] = back_data
                                if int(eval(test_case.data_transfer[i])[1]) == 3:
                                    test_case.data_three[num] = back_data
                                index = eval(test_case.data_transfer[i])[2]
                                self.global_para[index] = back_data
                            if len(eval(test_case.data_transfer[i])) == 1:
                                index = eval(test_case.data_transfer[i])[0]
                                self.global_para[index] = back_data
                            if len(eval(test_case.data_transfer[i])) == 2:
                                num = int(eval(test_case.data_transfer[i])[0]) - 1
                                if int(eval(test_case.data_transfer[i])[1]) == 1:
                                    test_case.data[num] = back_data
                                if int(eval(test_case.data_transfer[i])[1]) == 2:
                                    test_case.data_two[num] = back_data
                                if int(eval(test_case.data_transfer[i])[1]) == 3:
                                    test_case.data_three[num] = back_data
                if para_num == 5:
                    if test_case.data[i].endswith(".web"):
                        test_case.data[i] = self.global_para[int(test_case.data[i].split(".")[0])]
                    if test_case.data_two[i].endswith(".web"):
                        test_case.data_two[i] = self.global_para[int(test_case.data_two[i].split(".")[0])]
                    if test_case.data_three[i].endswith(".web"):
                        test_case.data_three[i] = self.global_para[int(test_case.data_three[i].split(".")[0])]
                    back_data = self.true_dict[test_case.step[i]](locator_name,test_case.data[i],test_case.data_two[i],test_case.data_three[i])
                    self.back_data_list.append(back_data)
                    if back_data:  # 判断是否有返回值
                        if len(eval(test_case.data_transfer[i])) == 3:  # 判断是否有参数传递
                            num = int(eval(test_case.data_transfer[i])[0]) - 1
                            if int(eval(test_case.data_transfer[i])[1]) == 1:
                                test_case.data[num] = back_data
                            if int(eval(test_case.data_transfer[i])[1]) == 2:
                                test_case.data_two[num] = back_data
                            if int(eval(test_case.data_transfer[i])[1]) == 3:
                                test_case.data_three[num] = back_data
                            index = eval(test_case.data_transfer[i])[2]
                            self.global_para[index] = back_data
                        if len(eval(test_case.data_transfer[i])) == 1:
                            index = eval(test_case.data_transfer[i])[0]
                            self.global_para[index] = back_data
                        if len(eval(test_case.data_transfer[i])) == 2:
                            num = int(eval(test_case.data_transfer[i])[0]) - 1
                            if int(eval(test_case.data_transfer[i])[1]) == 1:
                                test_case.data[num] = back_data
                            if int(eval(test_case.data_transfer[i])[1]) == 2:
                                test_case.data_two[num] = back_data
                            if int(eval(test_case.data_transfer[i])[1]) == 3:
                                test_case.data_three[num] = back_data
            else:  # 无参数
                back_data = self.true_dict[test_case.step[i]](locator_name)
                self.back_data_list.append(back_data)
                if back_data:  # 判断是否有返回值
                    if test_case.data_transfer[i]:
                        if len(eval(test_case.data_transfer[i])) == 3:  # 判断是否有参数传递
                            num = int(eval(test_case.data_transfer[i])[0]) - 1
                            if int(eval(test_case.data_transfer[i])[1]) == 1:
                                test_case.data[num] = back_data
                            if int(eval(test_case.data_transfer[i])[1]) == 2:
                                test_case.data_two[num] = back_data
                            if int(eval(test_case.data_transfer[i])[1]) == 3:
                                test_case.data_three[num] = back_data
                            index = eval(test_case.data_transfer[i])[2]
                            self.global_para[index] = back_data
                        if len(eval(test_case.data_transfer[i])) == 1:
                            index = eval(test_case.data_transfer[i])[0]
                            self.global_para[index] = back_data
                        if len(eval(test_case.data_transfer[i])) == 2:
                            num = int(eval(test_case.data_transfer[i])[0]) - 1
                            if int(eval(test_case.data_transfer[i])[1]) == 1:
                                test_case.data[num] = back_data
                            if int(eval(test_case.data_transfer[i])[1]) == 2:
                                test_case.data_two[num] = back_data
                            if int(eval(test_case.data_transfer[i])[1]) == 3:
                                test_case.data_three[num] = back_data
    if test_case.exp.endswith(".web"):
        test_case.exp = self.global_para[int(test_case.exp.split(".")[0])]
    png_name = os.path.join(os.path.dirname(__file__), "test_screenshot_png", test_case.title + ".png")
    self.true_dict["test_screenshot_png"](png_name)