def isSafe(stat,storage):
    '''
    本函数中定义的变量：
        1.  my_x,my_y:我纸卷的x坐标,我的纸卷的y坐标,为整型
        2.  RoundTrack:圈地路径，使用别名，方便写程序
    本函数中的辅助函数:
        见辅助函数部分，共有4个。辅助函数部分注释很详细
    输入参数:
        stat:
        storage:
    返回：
        'left' or 'right' or 'straight'     转向指令，即  左转|右转|直行
    version:
        0.1 date:2018/6/5   sid 将整体的架构写出来，辅助函数中有一些没完成，根函数（即isSafe函数，在这里用根函数代称）也没有写一些算法的实现，只是将算法用伪代码给写好了，然后明天需要找大家确定函数接口。
    '''
    #辅助函数部分
    #判断是否在制定路径上的函数
    def isOnTrack(x,y,path):
        '''
        辅助函数说明：判断某一个坐标是否在制定的路径上
        传入参数说明：
            x:  int 横坐标
            y:  int 纵坐标
            path:   list[list]  二重列表，路径
        返回：
            True:   bool    若在指定路径上，返回真
            False:  bool    若不在指定路径上，返回假
        version:
            1.0 date:2018/6/5   没有path中标记方式，暂时没法写，尚处于不能运行状态
        '''
        pass

    #判断路径上的下一步是否安全的函数
    def isNextStepSafe(x,y,path,storage):
        '''
        辅助函数说明：判断路径上的下一个位置，通过比较'路径上下一个位置回到领地的最短距离'和'对方到我当前纸带的最短距离'，判断是否会产生危险
        传入函数说明：
            x:  int 当前纸卷横坐标
            y:  int 当前纸卷纵坐标
            path:   list[list]  二维列表，指定的路径
            storage:
        返回：
            True:   bool    如果指定路径上的下一个位置是安全的，就返回真
            False:  bool    如果指定路径上的下一个位置是危险的，就返回假
        version:
            1.0:    date:2018/6/5   sid 整体架构建立，调用的辅助函数getNextPosition、isNowSafe还不够完整。这两个函数都需要用到童的函数。
        '''
        #得到路径上下一个位置坐标
        nextX,nextY=getNextPosition(x,y,path)
        #进行安全的判断并返回
        return isNowSafe(nextX,nextY,storage)   #isNowSafe返回bool 

    def isNowSafe(x,y,storage):
        '''
        辅助函数说明：判断传入坐标的位置是否是安全的
        传入参数说明：
            x:  int
            y:  int
            storage:
        返回：
            True:   当前位置安全
            False:  当前位置危险
        version:
            1.0 date:2018/6/5   sid 创建，因为不知道getdistance函数具体的参数模板，暂时无法使用
        '''
        disMe2Home=getdistance()#当前位置我纸卷到领地的最短距离
        disHe2Me=getdistance()#敌人纸卷到我目前纸带的最短距离
        if disMe2Home<disHe2Me-1:
            return False
        else:
            return True


    #找到路径上下一个位置的函数
    def getNextPosition(x,y,path):
        '''
        辅助函数说明：根据当前位置和指定路径，返回下一个路径上下一个位置的横纵坐标。
        传入函数说明：
            x:  int
            y:  int
            path:   list[list]
        返回：
            nextX,nextY int,int 下一个位置的横坐标，纵坐标 
        version:
            1.0：    date:2018/6/5   sid 建立架构，因为不知道path二维列表如何标记路径，还没有写具体的函数,还不能使用    
        '''
        #判断北面是否是下一个位置
        #判断东面是否是下一个位置
        #判断南面是否是下一个位置
        #判断西面是否是下一个位置

        

    #第一部分：声明本函数中定义的函数
    my_x=stat['now']['me']['x']
    my_y=stat['now']['me']['y']
    RoundTrack=storage['RoundTrack']    #这里需要自己后面将生成的路径放到storage中

    #判断是否在圈地路径上：
    if isOnTrack(my_x,my_y,RoundTrack):
        #已知在圈地路径上，判断圈地路径上下一个位置是否安全
        if isNextStepSafe():
            #安全，沿着路径走，返回下一个位置的绝对坐标
            pass
            #将当前位置的路径标记擦除
            pass
            #将坐标转换为相对方向
            pass
            #返回转向指令
            pass
        else:#不安全，返回逃跑路径，沿着逃跑路径走
            #创建逃跑路径，存到storage中
            #返回沿着逃跑路径走的一个方向（并将逃跑路径标记抹除）
            pass
    else:#如果不在圈地路径上
        if isOnTrack(my_x,my_y,EscapeTrack):
            #如果在逃跑路径上
            if isNowSafe(my_x,my_y,storage):
                #调用函数back_track
                pass
                #将逃跑路径清空
                pass
            else:#逃跑过程中一直处于不安全的状态
                #得到逃跑路径上的下一个坐标
                pass
                #将当前位置的逃跑路径标记擦除
                #转换为相对方向
                pass
                #返回转向指令
                pass
        else:#如果不在逃跑路径上，那就是在领地中
            #调用函数back_track
            pass


        


