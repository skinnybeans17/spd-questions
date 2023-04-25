link_lists = [ : list[list[int]]]
    [1, 4, 7],
    [5, 3, 2],
    [6, 9, 8]
]

def merged_lists(link_lists: List[List[int]]) -> List[int]:
    new_list = [] : list[Unknown]
    remaining_items = True : Literal[True]

    while remaining_items:
        least_head = None : None

        for (_, link_list) in enumerate(link_lists):
            if len(link_list) == 0:
                continue
            
            if least_head is None:
                least_head = link_list : List[int] : List[int]

            elif least_head[0] > link_list[0]:
                least_head = link_list : List[int] : List[int]

        if least_head is None or len(least_head) == 0:
            remaining_items = False : Literal[False]
            break
        else:
            new_list.append(least_head.pop(0))
    return new_list

print(merged_lists(link_lists))
