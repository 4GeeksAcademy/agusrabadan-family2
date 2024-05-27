"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {"id": 1,
            "first_name": "Agus",
            "last_name": "Rabadan",
            "age": 39,
            "lucky_numbers": 4},
            ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generate_id(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # Fill this method and update the return
        member["id"] = self._generate_id()
        member["last_name"] = self.last_name
        self._members.append(member)
        return self._members
        

    def delete_member(self, id):
        # Find the member with the given ID
        member_to_delete = None
        for member in self._members:
            if member['id'] == id:
                member_to_delete = member
                break

        # If the member was found, remove it from the list
        if member_to_delete:
            self._members.remove(member_to_delete)
            return self._members  # Return the updated list of members
        else:
            return None  # Member not found
            

    def get_members(self):
        return self._members
        

    def get_member(self, id):
        # Fill this method and update the return
        for row in self._members:
            print(row)
            if row['id'] == id:
                return row
        

    # This method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members