# Sorting Algorithms
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                yield arr

def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = arr[end]
    pIndex = start
    for i in range(start, end):
        if arr[i] < pivot:
            arr[i], arr[pIndex] = arr[pIndex], arr[i]
            pIndex += 1
            yield arr
    arr[pIndex], arr[end] = arr[end], arr[pIndex]
    yield arr
    yield from quick_sort(arr, start, pIndex-1)
    yield from quick_sort(arr, pIndex+1, end)

def merge_sort(arr, start, end):
    if end <= start:
        return

    mid = start + (end - start) // 2
    yield from merge_sort(arr, start, mid)
    yield from merge_sort(arr, mid + 1, end)
    yield from merge(arr, start, mid, end)
    yield arr

def merge(arr, start, mid, end):
    merged = []
    left_idx = start
    right_idx = mid + 1

    while left_idx <= mid and right_idx <= end:
        if arr[left_idx] < arr[right_idx]:
            merged.append(arr[left_idx])
            left_idx += 1
        else:
            merged.append(arr[right_idx])
            right_idx += 1

    while left_idx <= mid:
        merged.append(arr[left_idx])
        left_idx += 1

    while right_idx <= end:
        merged.append(arr[right_idx])
        right_idx += 1

    for i, sorted_val in enumerate(merged):
        arr[start + i] = sorted_val
        yield arr

import streamlit as st
import random
import time

def generate_random_array(n):
    return random.sample(range(1, n+1), n)

def visualize_sorting(sorting_algorithm, arr):
    for step in sorting_algorithm(arr):
        chart.bar_chart(step)
        time.sleep(0.1) # lessen to increase speed: TODO: do this on user input

# Streamlit UI
st.title("Sorting Algorithm Visualizer")

array_size = st.slider("Select Array Size", 10, 100, 50)

algorithm = st.selectbox("Select Algorithm", ["Bubble Sort", "Quick Sort", "Merge Sort"])

# Information about the Algorithm
if algorithm == "Bubble Sort":
    st.write("Bubble Sort, a classic comparison-based algorithm, is renowned for its simplicity. "
            "It operates by repeatedly traversing the list, comparing adjacent elements, and swapping them if needed to ensure order. "
            "While its implementation is straightforward, its time complexity is O(n²) in the worst and average cases, making it less efficient for large datasets.")

elif algorithm == "Quick Sort":
    st.write("Quick Sort is a highly efficient divide-and-conquer algorithm, famous for its speed in practice. "
            "It selects a 'pivot' element and partitions the array around it, recursively sorting the partitions. "
            "The average and best-case time complexity is O(n log n), although its worst-case complexity is O(n²). Quick Sort's performance and memory efficiency make it a popular choice for large datasets.")

elif algorithm == "Merge Sort":
    st.write("Merge Sort is a classic divide-and-conquer algorithm known for its efficiency and stability. "
            "It divides the array into halves, recursively sorts each half, and then merges the sorted halves. "
            "This algorithm is notable for its predictable time complexity of O(n log n) in all cases – best, average, and worst. "
            "Due to its stable sorting and consistent performance, Merge Sort is a preferred choice for sorting linked lists and large datasets where data is not stored in contiguous memory.")

# Launch Visualisation
if st.button("Sort"):
    arr = generate_random_array(array_size)
    chart = st.empty()

    if algorithm == "Bubble Sort":
        visualize_sorting(bubble_sort, arr.copy())

    elif algorithm == "Quick Sort":
        visualize_sorting(lambda arr: quick_sort(arr, 0, len(arr)-1), arr.copy())
        
    elif algorithm == "Merge Sort":
        visualize_sorting(lambda arr: merge_sort(arr, 0, len(arr)-1), arr.copy())

# Footer
st.sidebar.info("Created by Disha with ❤️")
