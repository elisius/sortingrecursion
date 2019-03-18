def bubble_sort(items):
    for passnum in range(len(items)-1,0,-1):
        for i in range(passnum):
            if items[i]>items[i+1]:
                temp = items[i]
                items[i] = items[i+1]
                items[i+1] = temp
    return items


def merge_sort(items):
    if len(items)>1:
        mid = len(items)//2
        lefthalf = items[:mid]
        righthalf = items[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                items[k]=lefthalf[i]
                i=i+1
            else:
                items[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            items[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            items[k]=righthalf[j]
            j=j+1
            k=k+1

    return items


def quick_sort(items):
   if len(items) == 2:
       if items[0] > items[1]:
           return [items[1], items[0]]
       else:
           return items
   else:
       pivot_val = items[0]
       left_list = []
       right_list = []
       equal_list = []

       for idx in range(len(items)):
           if items[idx] == pivot_val:
               equal_list.append(items[idx])
           elif items[idx] < pivot_val:
               left_list.append(items[idx])
           else:
               right_list.append(items[idx])

       if len(left_list) > 1:
           left_list = quick_sort(left_list)
       if len(right_list) > 1:
           right_list = quick_sort(right_list)

       sorted_list = left_list + equal_list + right_list

   return sorted_list
