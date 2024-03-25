import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
from playsound import playsound
import random




def merge_sort_animation(array, start, end):


    if end <= start:
        return

    mid = start + ((end - start + 1) // 2) - 1

    yield from merge_sort_animation(array, start, mid)
    
    yield from merge_sort_animation(array, mid + 1, end)
   
    yield from merge(array, start, mid, end)
    
    yield array
    
    playsound('ringtone-1-46486.mp3')


def merge(array, start, mid, end):
    
    
    merged = []
    leftIdx = start
    rightIdx = mid + 1

    while leftIdx <= mid and rightIdx <= end:
        if array[leftIdx] < array[rightIdx]:
            merged.append(array[leftIdx])
            leftIdx += 1
        else:
            merged.append(array[rightIdx])
            rightIdx += 1

    while leftIdx <= mid:
        merged.append(array[leftIdx])
        leftIdx += 1

    while rightIdx <= end:
        merged.append(array[rightIdx])
        rightIdx += 1

    for i, sorted_val in enumerate(merged):
        array[start + i] = sorted_val
        yield array


def random_array_values(length, start, end):
    return [random.randint(start, end) for _ in range(length)]




def update(graph):
    ax.clear()
    ax.bar(range(len(graph)), graph, color='orange')

   
    ax.set_title(label = "Merge Sort", loc = "left", fontstyle = 'italic' )
   




fig, ax = plt.subplots()



length = int(input("pick the length value for the array:" ))
start = int(input("pick the start value of for the array:" ))
end = int(input("pick the end value for the array:" ))



data1 = np.random.randint(start, end, length)

anim = FuncAnimation(fig, update, frames=merge_sort_animation(data1.copy(), 0, length-1 ), repeat=False, blit=False, interval=10)
plt.show()


