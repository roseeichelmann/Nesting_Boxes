
#  File: Boxes.py

#  Description: Program using recursion to identify largest possible number of boxes from a list 
# that can fit into each other 

#  Student Name: Rose Eichelmann

#  Student UT EID: ree585

#  Course Name: CS 313E

#  Unique Number: 86610

#  Date Created: 07/08/21

#  Date Last Modified: 7/10/21

import sys

# generates all subsets of boxes and stores them in all_box_subsets
# box_list is a list of boxes that have already been sorted
# sub_set is a list that is the current subset of boxes
# idx is an index in the list box_list
# all_box_subsets is a 3-D list that has all the subset of boxes
def sub_sets_boxes (box_list, sub_set, idx, all_box_subsets):
  # When index reaches length of box list, add current subset to all subsets list
  if idx == len(box_list):
    # print("Current sub set: ", sub_set)
    all_box_subsets.append(sub_set)
  # Else either add or dont add next box to current subset
  else:
    sub_set_copy = sub_set[:]
    sub_set.append(box_list[idx])
    sub_sets_boxes(box_list, sub_set, idx + 1, all_box_subsets)
    sub_sets_boxes(box_list, sub_set_copy, idx + 1, all_box_subsets)


# goes through all the subset of boxes and only stores the
# largest subsets that nest in the 3-D list all_nesting_boxes
# largest_size keeps track what the largest subset is
def largest_nesting_subsets (all_box_subsets, largest_size, all_nesting_boxes, index):
  # Loop through each sub set to determine if it is a nested set with the largest possible size
  for index in range(len(all_box_subsets)):
    sub_set = all_box_subsets[index]
    current_size = 1
    # if length of current sub set is less than largest size, start at next iteration of loop
    if len(sub_set) < largest_size:
      continue
    # loop through the boxes in current subset and see if box1 fits into box 2
    for i in range(len(sub_set) - 1):
      # if box 1 fits into box 2 increase current size by 1
      if does_fit(sub_set[i], sub_set[i + 1]):
        current_size += 1
      else:
        current_size = 0
        break
    # if sub set is not nested continue to next iteration of loop
    if current_size == 0:
      continue
    # if set had more nested boxes than largest size, make current size the new largest size
    # and create new nesting boxes list with just the current sub set
    elif current_size > largest_size:
      largest_size = current_size
      all_nesting_boxes = []
      all_nesting_boxes.append(sub_set)
    # if set had had same number of boxes as largest size, append current set to
    # nesting boxes list
    elif current_size == largest_size:
      all_nesting_boxes.append(sub_set)
  # if nesting boxes list is empty, largest size is 1
  if len(all_nesting_boxes) == 0:
    largest_size = 1
  return largest_size, all_nesting_boxes


# returns True if box1 fits inside box2
def does_fit (box1, box2):
  return (box1[0] < box2[0] and box1[1] < box2[1] and box1[2] < box2[2])

def main():
  # read the number of boxes 
  line = sys.stdin.readline()
  line = line.strip()
  num_boxes = int (line)

  # create an empty list for the boxes
  box_list = []

  # read the boxes from the file
  for i in range (num_boxes):
    line = sys.stdin.readline()
    line = line.strip()
    box = line.split()
    for j in range (len(box)):
      box[j] = int (box[j])
    box.sort()
    box_list.append (box)

  # # print to make sure that the input was read in correctly
  # print (box_list)
  # print()

  # sort the box list
  box_list.sort()

  # # print the box_list to see if it has been sorted.
  # print ("box list: ", box_list)
  # print()

  # create an empty list to hold all subset of boxes
  all_box_subsets = []

  # create a list to hold a single subset of boxes
  sub_set = []

  # generate all subsets of boxes and store them in all_box_subsets
  sub_sets_boxes(box_list, sub_set, 0, all_box_subsets)

  # all_box_subsets should have a length of 2^n where n is the number
  # of boxes

  # go through all the subset of boxes and only store the
  # largest subsets that nest in all_nesting_boxes
  all_nesting_boxes = []
  largest_number, all_nesting_boxes = largest_nesting_subsets (all_box_subsets, 0, all_nesting_boxes, 0)

  # print the largest number of boxes that fit
  print(largest_number)

  # print the number of sets of such boxes and
  # print length of original boxes list if there are no nests
  if len(all_nesting_boxes) == 0:
    print(len(num_boxes))
  else:
      print(len(all_nesting_boxes))


if __name__ == "__main__":
  main()

