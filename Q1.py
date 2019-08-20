#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 20:27:00 2019

@author: jiajialu
"""

'''
在一个二维数组中（每个一维数组的长度相同
每一行都按照从左到右递增的顺序排序
每一列都按照从上到下递增的顺序排序
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if len(array[0]) > 0:
            for i in range(len(array)):
                if array[i][0] <= target:
                    for j in range(len(array[0])):
                        if array[i][j] == target:
                            return True
                else:
                    return False

sol = Solution()
result = sol.Find(7, [[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]])
print(result)