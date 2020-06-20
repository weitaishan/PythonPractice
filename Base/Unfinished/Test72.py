# *_*coding:utf-8 *_*

'''
题目：创建一个链表。


去了解什么是链表

链表学习地址1：https://blog.csdn.net/qq_36831816/article/details/100664508
链表学习地址2：https://blog.csdn.net/Tonywu2018/article/details/88853533?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase
'''

# 实例一
if __name__ == '__main__':
    ptr = []
    for i in range(5):
        num = int(input('please input a number:'))
        ptr.append(num)
    print(ptr)




# 实例二
class Node(object):
    "定义链表节点类"
    def __init__(self, data=None, next=None):     "data为数据项，next为下一节点的链接，初始化数据和节点为None"
        self._value = data
        self._next = next

    def get_value(self):
        return self._value

    def get_next(self):
        return self._next

    def set_value(self, new_data):
        self._value = new_data

    def set_next(self, new_next):
        self._next = new_next


class LinkList(object):
    "定义一个链表类"
    def __init__(self):
        self._head = Node()
        self._tail = self._head
        self._length = 0

    def head(self):
        """
        链表的第一个元素(除去头节点)
        :return:
        """
        if self._head.get_next():
            return self._head.get_next()
        else:
            return Node()

    def tail(self):
        """
        链表的最后一个元素
        :return:
        """
        return self._tail

    def is_empty(self):
        """
        判断链表是否为空
        :return:
        """
        return self._length == 0

    def size(self):
        """
        链表的大小
        :return:
        """
        return self._length

    def add(self, value):
        """
        从头部插入节点
        :param value:
        :return:
        """
        new_node = Node(value)
        new_node.set_next(self._head.get_next())
        self._head.set_next(new_node)
        self._length += 1

    def append(self, value):
        """
        从尾部追加节点
        :param value:
        :return:
        """
        new_node = Node(value)
        if self.is_empty():
            self._head.set_next(new_node)
        else:
            current = self._head
            while current.get_next():
                current = current.get_next()
            current.set_next(new_node)
        self._tail = new_node
        self._length += 1

    def search(self, value):
        """
        查找数据，返回-1或者节点索引
        :param value:
        :return:
        """
        current = self._head.get_next()
        count = 0
        while current.get_next():
            if current.get_value() == value:
                return count
            current = current.get_next()
            count += 1
        return -1

    def remove(self, value):
        """
        删除 返回该数据或者-1
        :param value:
        :return:
        """
        current = self._head
        pre = None
        while current.get_next():
            if current.get_value() == value:
                if not pre:
                    self._head = current.get_next()
                else:
                    pre.set_next(current.get_next())
                self._length -= 1
                return current.get_value()
            pre = current
            current = current.get_next()
        else:
            return -1


    def insert(self, index, value):
        """
        插入数据节点
        :param index:
        :param value:
        :return:
        """
        if index <= 1:
            self.add(value)
        elif index > self.size():
            self.append(value)
        else:
            new_node = Node(value)
            count = 0
            current = self._head
            pre = None
            while count < index:
                count += 1
                pre = current
                current = current.get_next()
            pre.set_next(new_node)
            new_node.set_next(current)
            self._length += 1


if __name__ == '__main__':
    arr = [1, 4, 2, 6, 8, 4, 9]
    print("数组的长度: ", len(arr))
    link_list = LinkList()
    print("空链表size: ", link_list.size())
    print("空链表是否为空：", link_list.is_empty())
    print("空链表的第一个数据：", link_list.head().get_value())
    print("空链表的最后一个数据：", link_list.tail().get_value())
    for i in arr:
        link_list.append(i)

    # 添加
    link_list.append(10)
    link_list.add(10)
    link_list.insert(1, 11)
    link_list.insert(3, 12)
    link_list.insert(7, 13)
    print("删除的元素：", link_list.remove(1))
    link_list.append(1)
    link_list.add(10)

    current = link_list.head()
    l = ""
    while current.get_next():
        l += str(current.get_value()) + " "
        current = current.get_next()
    l += str(current.get_value())
    print("遍历链表的值", l)
    print("链表的尺寸：", link_list.size())
    print("链表的查找：", link_list.search(8))
    print("链表的第一个数据：", link_list.head().get_value())
    print("链表的最后一个数据：", link_list.tail().get_value())