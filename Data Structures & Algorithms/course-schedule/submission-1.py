class Solution:
    from collections import defaultdict
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacancy_list = defaultdict(list)
        """ 
        0: [1.2.3]
        1: []
        2: []
        3: []
        4: [5]
        5: []
        """
        #create directed acyclic graphs 
        for course, prerequisite in prerequisites: 
            adjacancy_list[course].append(prerequisite)
        
        def search_cycles(course, seen):
            if course in seen: 
                return True
            if course not in adjacancy_list: 
                return False
            seen.add(course)
            prerequisites = adjacancy_list[course]
            for prereq in prerequisites: 
                return search_cycles(prereq, seen)
                         

        for course in range(numCourses): 
            #Cycle, a course can not be a prerequsite to each other
            seen = set() 
            if course in seen:
                continue 
            
            if search_cycles(course, seen): 
                return False
        
        return True
        
        

        





            
        



