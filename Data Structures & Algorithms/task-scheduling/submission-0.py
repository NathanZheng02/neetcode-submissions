class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Processing most freq guarentees least idle times
        counts = Counter(tasks)
        max_heap = [-count for count in counts.values()]
        heapq.heapify(max_heap)

        time = 0
        queue = deque() # [-count, available time]
        while max_heap or queue:
            time += 1

            # Check max_heap for the highest count value
            if not max_heap:
                # Heap is empty, time is pulled from queue
                time = queue[0][1]
            else:
                # Decrementing counter
                count = 1 + heapq.heappop(max_heap)

                # If count is not 0, add a "cooldown"
                if count != 0:
                    queue.append([count, time + n])
            
            # Now check if anything has come off cooldown
            if queue and queue[0][1] == time:
                # Push the count back onto the max_heap
                heapq.heappush(max_heap, queue.popleft()[0])
        
        return time