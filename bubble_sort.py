def bubble_sort(arr):
    """
    使用冒泡排序对列表进行从小到大的排序。
    :param arr: 可变序列（如 list）
    :return: 排序后的同一列表对象
    """
    n = len(arr)
    for i in range(n - 1):
        # 提前结束标记：如果这一趟没有交换，说明已经有序
        swapped = False
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                # 交换相邻元素
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


if __name__ == "__main__":
    data = [5, 3, 8, 4, 2]
    print("原始：", data)
    sorted_data = bubble_sort(data)
    print("排序后：", sorted_data)
  

