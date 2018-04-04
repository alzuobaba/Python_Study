"""
定义一个递归函数计算 list的sum
"""
def ListSum(l1):
    try:
        return l1[0]+ListSum(l1[1:])        
    except:
        return 0
    
result = ListSum([3,4])
# result = []
print(result)