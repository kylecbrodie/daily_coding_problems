import heapq

def merge(sorted_lists: [list]) -> list:
	merged_list = []
	heap = [(sorted_list[0], i, 0) for i, sorted_list in enumerate(sorted_lists) if len(sorted_list) > 0]
	heapq.heapify(heap)
	while len(heap) > 0:
		value, list_index, value_index = heapq.heappop(heap)
		merged_list.append(value)
		if value_index + 1 < len(sorted_lists[list_index]):
			next_heap_element = (sorted_lists[list_index][value_index + 1], list_index, value_index + 1)
			heapq.heappush(heap, next_heap_element)
	
	return merged_list

merge([[1, 2, 3], [5, 11, 17], [10, 20, 40]])