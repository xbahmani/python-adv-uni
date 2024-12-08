import urllib.request
import json
import statistics


class Fetcher:
    def __init__(self):
        url = "https://cdn.ituring.ir/ex/users.json"
        try:
            with urllib.request.urlopen(url) as response:
                data = response.read()
                self.__students = json.loads(data)
        except Exception as e:
            raise Exception("Error fetching data:", e)

    def nerds(self):
        
        return {
            f"{student.get('first_name', 'Unknown')} {student.get('last_name')}"
            for student in self.__students
            if student.get('score', 0) > 18.5
        }

    def sultans(self):
        
        highest_score = max(student.get('score', 0) for student in self.__students)
        
        return tuple(
            f"{student.get('first_name', 'Unknown')} {student.get('last_name')}"
            for student in self.__students
            if student.get('score', 0) == highest_score
        )

    def mean(self):
    
        scores = [student.get('score', 0) for student in self.__students]
        return statistics.mean(scores)

    def get_students(self):
        
        return [
            {
                key: value
                for key, value in student.items()
                if key not in {'city', 'province', 'location'}
            }
            for student in self.__students
        ]



if __name__ == "__main__":
    fetcher = Fetcher()

    print("Students with scores above 18.5 (nerds):")
    print(fetcher.nerds())

    print("\nStudent(s) with the highest score (sultans):")
    print(fetcher.sultans())

    print("\nAverage score of all students (mean):")
    print(fetcher.mean())

    print("\nStudents list without city, province, or location (get_students):")
    print(fetcher.get_students())