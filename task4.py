from multiprocessing import Pool
from firstname import merge, merge_sort


def parallel_merge_sort(nums):
    print(nums)
    if len(nums) <= 1:
        return nums
    pool = Pool()
    mid = len(nums) // 2
    # Сортируем и объединяем подсписки
    left_list, right_list = pool.map(merge_sort, [nums[:mid], nums[mid:]])
    print(left_list, right_list)
    return merge(left_list, right_list)


if __name__ == "__main__":
    # Проверяем, что оно работает
    random_list_of_nums = [120, 40, 68, 250, 176]
    random_list_of_nums = parallel_merge_sort(random_list_of_nums)
    print(random_list_of_nums)
    random_list_of_nums = [1, 12, 85, 45, 39, 5, 4, 7, 12]
    random_list_of_nums = parallel_merge_sort(random_list_of_nums)
    print(random_list_of_nums)
    # pool = multiprocessing.Pool()
    # print(pool.map(sum, [(2, 5)]))
    # print(pool.map(sum, [(3, 5)]))
