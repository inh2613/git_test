# # 알고리즘 수업 - 병합 정렬 1
def merge_sort(arr, front, rear):
    if front < rear and cnt <= k:
        mid = (front + rear) // 2
        merge_sort(arr, front, mid)
        merge_sort(arr, mid+1, rear)
        merge(arr, front, mid, rear)


def merge(arr, front, mid, rear):
    global cnt, res
    tmp = []
    i = front
    j = mid+1

    while i <= mid and j <= rear:
        if arr[i] <= arr[j]:
            tmp.append(arr[i])
            i += 1

        else:
            tmp.append(arr[j])
            j += 1

    while i <= mid:
        tmp.append(arr[i])
        i += 1

    while j <= rear:
        tmp.append(arr[j])
        j += 1

    i = front
    t = 0
    while i <= rear:
        arr[i] = tmp[t]
        cnt += 1
        if cnt == k:
            res = arr[i]
            break
        i += 1
        t += 1


n, k = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
res = -1
merge_sort(arr, 0, n-1)
print(res)

