class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Combine the positions and speeds into a list of tuples (position, speed)
        # and sort the list in ascending order by position
        combined = sorted(zip(position, speed))

        prev_time = 0  # Initialize the time taken by the previous car to reach the target
        fleet_count = 0  # Initialize the count of car fleets

        # Iterate over the combined list in reverse order (from the car farthest from the target)
        for p, s in combined[::-1]:
            # Calculate the time taken by the current car to reach the target
            curr_time = (target - p) / s

            # If the current car takes more time than the previous car,
            # it means it will form a new fleet
            if curr_time > prev_time:
                fleet_count += 1
                prev_time = curr_time  # Update the previous car's time

        return fleet_count