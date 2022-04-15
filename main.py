import pygame
import random
import time
# import winsound

# HARDCODED VALUES:
WIDTH = 900
LENGTH = 600
numberofbars = 90
barwidth = int(WIDTH/numberofbars)

pygame.init()
screen = pygame.display.set_mode((WIDTH, LENGTH))
pygame.display.set_caption("Sorting Algorithms Vissualiser by ephraim")

whiteRGB = (210, 210, 210)
blackRGB = (30, 30, 30)
blueRGB = (10, 10, 255)
greenRGB = (190, 240, 179)


def generateArray(valMin, valMax):
    array = [random.randrange(valMin, valMax) for i in range(numberofbars)]
    return array

the_array = []
arr_clr = []

# def drawArray(array, highlights):
#     screen.fill(blackRGB)
#     for i in range(0, len(array) - 1):
#         xpos = 3 + barwidth * i
#         pygame.draw.line(screen, whiteRGB, (xpos, LENGTH), (xpos, LENGTH - array[i]), 3)
#         if highlights[0] == -2:
#             pygame.draw.line(screen, greenRGB, (xpos, LENGTH), (xpos, LENGTH - array[i]), 3)
#
#     for h in highlights:
#         pygame.draw.line(screen, blueRGB, (3 + barwidth * h, LENGTH), (3 + barwidth * h, LENGTH - array[h]), 3)
#
#     pygame.display.update()

def draw():
    screen.fill(blackRGB)
    pygame.event.pump()
    for i in range(0, numberofbars - 1):
        xpos = 3 + barwidth * i
        pygame.draw.line(screen, arr_clr[i], (xpos, LENGTH), (xpos, LENGTH - the_array[i]), 3)
        # if arr_clr[i] == blueRGB:
        #     winsound.Beep(3*the_array[i]+500, 100)
    pygame.display.update()


# BUBBLE SORT CODE:
def bubbleSort(array):
    for i in range(len(array)):
        swapped = False
        for j in range(0, len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
            # time.sleep(.01)
            arr_clr[j] = blueRGB
            draw()
            arr_clr[j] = whiteRGB
        if not swapped:
            break


# MERGE SORT CODE:
def merge(array, x1, y1, x2, y2):
    i = x1
    j = x2
    temp = []
    pygame.event.pump()
    while i <= y1 and j<= y2:
        arr_clr[i] = blueRGB
        arr_clr[j] = blueRGB
        draw()
        arr_clr[i] = whiteRGB
        arr_clr[j] = whiteRGB
        if array[i] < array[j]:
            temp.append(array[i])
            i += 1
        else:
            temp.append(array[j])
            j += 1
    while i <= y1:
        arr_clr[i] = blueRGB
        draw()
        arr_clr[i] = whiteRGB
        temp.append(array[i])
        i += 1
    while j<= y2:
        arr_clr[j] = blueRGB
        draw()
        arr_clr[j] = whiteRGB
        temp.append(array[j])
        j += 1
    j = 0
    for i in range(x1, y2 + 1):
        pygame.event.pump()
        array[i] = temp[j]
        j += 1
        arr_clr[i] = blueRGB
        draw()
        if y2 - x1 == len(array) - 2:
            arr_clr[i] = blueRGB
        else:
            arr_clr[i] = whiteRGB

def mergeSort(array, l, r):
    mid = (l + r)//2
    if l < r:
        mergeSort(array, l, mid)
        mergeSort(array, mid + 1, r)
        merge(array, l, mid, mid + 1, r)


# QUICK SORT CODE:
def partition(start, end, array):
    # Initializing pivot's index to start
    pivot_index = start
    pivot = array[pivot_index]

    # This loop runs till start pointer crosses
    # end pointer, and when it does we swap the
    # pivot with element on end pointer
    while start < end:

        # Increment the start pointer till it finds an
        # element greater than  pivot
        while start < len(array) and array[start] <= pivot:
            start += 1

        # Decrement the end pointer till it finds an
        # element less than pivot
        while array[end] > pivot:
            end -= 1

        # If start and end have not crossed each other,
        # swap the numbers on start and end
        if (start < end):
            array[start], array[end] = array[end], array[start]

    # Swap pivot element with element on end pointer.
    # This puts pivot on its correct sorted place.
    array[end], array[pivot_index] = array[pivot_index], array[end]

    # Returning end pointer to divide the array into 2
    return end

def quickSort(start, end, array):
    if start < end:
        time.sleep(.1)
        arr_clr[start] = blueRGB
        arr_clr[end] = blueRGB
        draw()
        arr_clr[start] = whiteRGB
        arr_clr[end] = whiteRGB

        # p is partitioning index, array[p]
        # is at right place
        p = partition(start, end, array)

        # Sort elements before partition
        # and after partition
        quickSort(start, p - 1, array)
        quickSort(p + 1, end, array)

def selectionSort(array):
    for i in range(len(array)):

        # Find the minimum element in remaining
        # unsorted array
        min_idx = i
        for j in range(i + 1, len(array)):
            arr_clr[i] = blueRGB
            arr_clr[j] = blueRGB
            draw()
            arr_clr[i] = whiteRGB
            arr_clr[j] = whiteRGB

            if array[min_idx] > array[j]:
                min_idx = j

        # Swap the found minimum element with
        # the first element
        array[i], array[min_idx] = array[min_idx], array[i]

def runSort(sort_type):
    global arr_clr, the_array
    the_array = generateArray(100, 500)
    arr_clr = [whiteRGB] * numberofbars
    draw()

    time.sleep(2)
    print("Starting sorting ")

    if sort_type == 1:
        bubbleSort(the_array)
    elif sort_type == 2:
        selectionSort(the_array)
    elif sort_type == 3:
        quickSort(0, len(the_array) - 1, the_array)
    elif sort_type == 4:
        mergeSort(the_array, 0, numberofbars - 1)

    arr_clr = [greenRGB]*numberofbars
    draw()

    print("Done sorting.")

    time.sleep(3)


def main():
    menu = pygame.image.load(r"D:\All_things\Coding\PycharmProjects\sorting_viz1\assets\menu.png")

    run = True
    while run:
        screen.fill(blackRGB)
        screen.blit(menu, (0, 0))
        pygame.display.update()

        ev = pygame.event.get()
        for event in ev:
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                # print(pos)
                if 188 < pos[1] < 282:
                    print("Bubble sort")
                    runSort(1)
                elif 282 < pos[1] < 369:
                    print("Selection sort")
                    runSort(2)
                elif 370 < pos[1] < 465:
                    print("Quick sort")
                    runSort(3)
                elif 467 < pos[1] < 555:
                    print("Merge sort")
                    runSort(4)
                else:
                    run = False

    pygame.quit()


if __name__ == '__main__':
    main()

