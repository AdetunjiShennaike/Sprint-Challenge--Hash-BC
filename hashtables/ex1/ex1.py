#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    for x in range(0, length):
      hash_table_insert(ht, weights[x], x)
    
    for x in range(0, length):
      temp = hash_table_retrieve(ht, (limit - weights[x]))
      if temp is not None:
        value = temp
        if value > x:
          return [value, x]
        return [x, value]

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
