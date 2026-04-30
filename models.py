platform = "LeetCode"
topic = "Arrays"

# core data structure.

# creating class
class Problem:
    def __init__(self, id, title, platform, difficulty, topic, status, notes, date_added):
        self.id = id
        self.title = title
        self.platform = platform
        self.difficulty = difficulty
        self.topic = topic
        self.status = status
        self.notes = notes
        self.date_added = date_added

# Add Method to Convert Object --> Dictionary
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "platform": self.platform,
            "difficulty": self.difficulty,
            "topic": self.topic,
            "status": self.status,
            "notes": self.notes,
            "date_added": self.date_added

        }

# Add Method to Convert Dictionary --> Object
    @staticmethod
    def from_dict(data):
        return Problem(
            data["id"],
            data["title"],
            data["platform"],
            data["difficulty"],
            data["topic"],
            data["status"],
            data["notes"],
            data["date_added"]
        )



