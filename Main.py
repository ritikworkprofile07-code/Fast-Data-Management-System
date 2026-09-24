import time

class FastDataManagementSystem:
    def __init__(self):
        # Hash Map (Dictionary) for O(1) time complexity search
        self.user_database = {}

    def add_user(self, user_id, name, score):
        """Add or Update a user record"""
        if user_id in self.user_database:
            print(f"--> Updating existing user with ID: {user_id}")
        else:
            print(f"--> Adding new user with ID: {user_id}")
            
        self.user_database[user_id] = {
            "name": name,
            "score": score
        }
        print(f"Success: Record saved for {name}.\n")

    def search_user(self, user_id):
        """O(1) Instant Search using Hash Map"""
        start_time = time.time()
        
        if user_id in self.user_database:
            user = self.user_database[user_id]
            end_time = time.time()
            print(f"--> [FOUND] ID: {user_id} | Name: {user['name']} | Score: {user['score']}")
            print(f"   (Search Time: {(end_time - start_time) * 1000:.4f} ms)\n")
            return user
        else:
            print(f"--> [NOT FOUND] No record associated with ID: {user_id}\n")
            return None

    def delete_user(self, user_id):
        """Delete user record"""
        if user_id in self.user_database:
            removed = self.user_database.pop(user_id)
            print(f"--> [DELETED] Successfully removed user {removed['name']} (ID: {user_id})\n")
        else:
            print(f"--> [ERROR] Cannot delete. ID {user_id} does not exist.\n")

    def get_ranked_users(self):
        """Sorts data by score using Timsort algorithm O(N log N)"""
        print("--- TOP RANKED USERS (Sorted by Score) ---")
        sorted_users = sorted(
            self.user_database.items(), 
            key=lambda item: item[1]['score'], 
            reverse=True
        )
        
        rank = 1
        for user_id, info in sorted_users:
            print(f"Rank {rank}: {info['name']} (ID: {user_id}) - Score: {info['score']}")
            rank += 1
        print("------------------------------------------\n")

# --- DEMO / RUNNING THE SYSTEM ---
if __name__ == "__main__":
    db = FastDataManagementSystem()

    # 1. Adding Records
    db.add_user("U101", "Ritik Yadav", 95)
    db.add_user("U102", "Aman Sharma", 82)
    db.add_user("U103", "Priya Singh", 89)
    db.add_user("U104", "Rohan Mehta", 91)

    # 2. Fast O(1) Search
    db.search_user("U101")

    # 3. Ranking / Sorting Users
    db.get_ranked_users()

    # 4. Deleting a Record
    db.delete_user("U102")

    # 5. Display Updated Leaderboard
    db.get_ranked_users()
  
