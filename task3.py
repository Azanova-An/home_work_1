from multiprocessing.dummy import Pool as ThreadPool
from firstname import merge, merge_sort
import threading
from queue import Queue
import random

def new_merge_sort(nums, queue):
    queue.put(merge_sort(nums))


def parallel_merge_thread(nums):
    print(nums)
    if len(nums) <= 1:
        return nums
    mid = len(nums) // 2

    answer = Queue()

    t1 = threading.Thread(target=new_merge_sort, args=(nums[:mid], answer, ))
    t2 = threading.Thread(target=new_merge_sort, args=(nums[mid:], answer, ))

    t2.start()
    t1.start()

    t1.join()
    t2.join()

    # Сортируем и объединяем подсписки
    left_list = answer.get()
    right_list = answer.get()
    print(left_list, right_list)
    return merge(left_list, right_list)


def parallel_merge_sort(nums):
    print(nums)
    if len(nums) <= 1:
        return nums
    pool = ThreadPool()
    mid = len(nums) // 2
    # Сортируем и объединяем подсписки
    left_list, right_list = pool.map(merge_sort, [nums[:mid], nums[mid:]])
    print(left_list, right_list)
    return merge(left_list, right_list)


if __name__ == "__main__":
    # Проверяем, что оно работает
    #list = [random.randrange(100) for _ in range(1, 100)]
    #random_list_of_nums = parallel_merge_thread(list)
    #print(random_list_of_nums)
    random_list_of_nums = [127, 40, 68, 250, 176, 125, 478]
    random_list_of_nums = parallel_merge_thread(random_list_of_nums)
    print(random_list_of_nums)
    random_list_of_nums = [1, 12, 85, 45, 39, 5, 4, 7, 12, 74, 14]
    random_list_of_nums = parallel_merge_sort(random_list_of_nums)
    print(random_list_of_nums)
    # pool = multiprocessing.Pool()
    # print(pool.map(sum, [(2, 5)]))
    # print(pool.map(sum, [(3, 5)]))
