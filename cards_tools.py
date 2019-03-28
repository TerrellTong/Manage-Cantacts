#记录所有的名片字典
card_list = []
def show_menu():
    '''显示菜单'''
    print("*"*50)
    print("欢迎使用【名片管理系统】V 1.0")
    print("")
    print("1.新增名片")
    print("2.显示全部")
    print("3.搜索名片")
    print("")
    print("0.退出系统")
    print("*"*50)

def new_card():
    '''新增名片'''
    print("-"*50)
    print("新增名片")

    #1.输入信息
    name_str=input("请输入姓名:")
    phone_str=input("请输入电话号码:")
    qq_str=input("请输入QQ:")
    email_str=input("请输入邮箱:")
    #2.使用信息构造一个字典
    card_dic={  "name":name_str,
                "phone":phone_str,
                "qq":qq_str,
                "email":email_str}
    #3.将名片放到列表中
    card_list.append(card_dic)
    print(card_list)
    #4.添加名片成功
    print("添加%s 的名片成功！"% name_str)

def show_all():
    '''显示所有名片'''
    print("-" * 50)
    print("所有名片")

    #判断是否存在名片记录，如果没有，提示用户并且返回
    if len(card_list)==0:
        print("没有用户，请使用新增功能添加名片")
        #return下方的代码不会执行并且返回到调用函数的位置
        return
    #打印表头
    for name in ["姓名","电话","QQ","邮箱"]:
        print(name, end="\t\t")
    print("")
    #打印分割线
    print("="*50)

    #遍历名片列表并依次输出信息
    for info in card_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t"% (info["name"],
                                           info["phone"],
                                           info["qq"],
                                           info["email"],))

def search_card():
    '''搜索名片'''
    print("-" * 50)
    print("搜索名片")

    #1.提示用户要搜索的姓名
    find_name=input("提示用户要搜索的姓名:")
    #2.遍历名片列表，如果没有找到则提示用户
    for info in card_list:
        if info["name"]==find_name:
            print("姓名\t\t电话\t\tQQ\t\t邮箱\t\t")
            print("="*50)
            print("%s\t\t%s\t\t%s\t\t%s\t\t"% (info["name"],
                                               info["phone"],
                                               info["qq"],
                                               info["email"]))
            #针对找到的名片进行修改和删除操作
            deal_card(info)
            break
    else:
        print("%s不存在这个列表中"% find_name)

def deal_card (find_dic):
    """
    处理查找到的名片
    :param find_dic:查找到的名片
    """
    print(find_dic)
    action_str=input("请选择要执行的操作 "
                     "[1] 修改 [2] 删除 [0] 返回主菜单")
    if action_str == "1":
        find_dic["name"]=input_card_info(find_dic["name"],"姓名:")
        find_dic["phone"] = input_card_info(find_dic["phone"],"电话:")
        find_dic["qq"] = input_card_info(find_dic["qq"],"qq:")
        find_dic["email"] = input_card_info(find_dic["email"],"邮箱:")
        print("修改名片成功")
    elif action_str == "2":
        card_list.remove(find_dic)
        print("删除名片成功")

def input_card_info(dict_value,tip_message):
    """
    输入名片信息
    :param dict_value:字典中原有的值
    :param tip_message:输入的提示文字
    :return:如果用户输入了内容，就返回内容，否则就返回字典中原有的值
    """
    #1.提示用户输入内容
    result=input(tip_message)
    #2.针对用户的输入进行判断，如果用户输入了内容，直接返回结果
    if len(result)>0:
        return result
    #3.如果用户没有输入内容，返回‘字典中原有的值’
    else:
        return  dict_value