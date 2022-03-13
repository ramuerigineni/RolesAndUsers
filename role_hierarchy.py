class Role:
    def __init__(self,data):
        self.data = data
        self.name = data.lower()
        self.children = []
        self.parent = None

    def add_user(self,child):
        child.parent = self
        self.children.append(child)

    def get_role_object(self,role):
        role_obj = None
        if self.data == role:
            return self
        else:
            childrens = self.children

        while True:
            tmp_child = []
            for child in childrens:
                if child.data == role:
                    role_obj = child
                else:
                    tmp_child.extend(child.children)

            if role_obj:
                return role_obj
            else:
                childrens = tmp_child

    def get_user_object(self,user):
        role_obj = None
        if self.name == user:
            return self
        else:
            childrens = self.children

        while True:
            tmp_child = []
            for child in childrens:
                if child.name == user:
                    role_obj = child
                else:
                    tmp_child.extend(child.children)

            if role_obj:
                return role_obj
            else:
                childrens = tmp_child

    def display(self):
        print(self.data,end=' , ')
        if self.children:
            for child in self.children:
                child.display()

    def display_users(self):
        print(self.name + " - " + self.data)
        if self.children:
            for child in self.children:
                child.display_users()

    def get_depth(self,xdict):
        count = 0
        while True:
            tmp_dict = []
            if len(xdict) ==  0:
                break
            count = count + 1
            for i in xdict:
                if isinstance(i,Role):
                    if len(i.children) != 0:
                        tmp_dict.extend(i.children)

            xdict = tmp_dict
        return count

    def height_role_hierachy(self):
        max_depth = 1
        if self.children:
            for child in self.children:
                childrens = child.children
                level = self.get_depth(child.children)

            if max_depth < level:
                max_depth = level
        print("height " + str(max_depth))

    def number_users(self,role):
        user_count = 0
        parent_role = role.parent
        while True:
            tmp_dict = None
            user_count = user_count  + 1

            if parent_role.parent :
                tmp_dict = parent_role.parent
            if not tmp_dict:
                break
            parent_role = tmp_dict
        print("Number of users from top " + str(user_count))

def display_operators():
    print("Operations :")
    print("1. Add Sub Role.")
    print("2. Display Roles")
    print("3. Delete Role.")
    print("4. Add User.")
    print("5. Display Users.")
    print("6. Display Users and Sub Users.")
    print("7. Number of users from top")
    print("8. Height of role hierachy.")

def add_sub_role(root):
    sub_role = input("Enter sub role name : ")
    role = input("Enter reporting to role name : ")
    sub = Role(sub_role)
    parent = root.get_role_object(role)
    parent.add_user(sub)

def add_role_name(root):
    name = input("Enter User Name : ")
    role = input("Enter Role : ")
    role_obj = root.get_role_object(role)
    role_obj.name = name

def get_roles_info(root):
    my_dict = {}
    my_dict[root.name] = []
    users_list = root.children
    while True:
        if(len(users_list)) == 0:
            break
        children = []
        for i in users_list:
            if i.parent.name in my_dict:
                my_dict[i.parent.name] = my_dict[i.parent.name] +  [i.name]
            else:
                my_dict[i.parent.name] = [i.name]

            children.extend(i.children)
            if len(i.children) == 0:
               my_dict[i.name] = []

        users_list = children
    return my_dict

def display_users_and_sub_users(my_dict):
    for user,sub_user in my_dict.items():
        sub_users = " , ".join(sub_user)
        print(user + " - " + sub_users)

def delete_role(root):
    del_role = input("Enter the role to be deleted : ")
    transfer_role = input("Enter the role to be transferred : ")
    del_role_obj = root.get_role_object(del_role)
    transfer_role_obj = root.get_role_object(transfer_role)
    par_del_role_name = del_role_obj.parent.data
    parent_obj = root.get_role_object(par_del_role_name)
    parent_obj.add_user(transfer_role_obj)

    # Transfering roles to parenet role
    for role in list(del_role_obj.children):
      if role.data != transfer_role:
       transfer_role_obj.add_user(role)

    childrens = []
    for j in parent_obj.children:
      if j.data != del_role:
        childrens.append(j)
    parent_obj.children = childrens

def main():
    # Create root user
    name = input("Enter root role name : ")
    root = Role(name)
    while True:
        display_operators()
        operator = input("Operation to be performed : ")
        if int(operator) == 1:
            add_sub_role(root)
        elif int(operator) == 2:
            root.display()
			print(" ")
        elif int(operator) == 3:
            delete_role(root)
        elif int(operator) == 4:
            add_role_name(root)
        elif int(operator) == 5:
            root.display_users()
        elif int(operator) == 6:
            users_info = get_roles_info(root)
            display_users_and_sub_users(users_info)
        elif int(operator) == 7:
           user = input("Enter user name : ")
           user_obj = root.get_user_object(user)
           root.number_users(user_obj)
        elif int(operator) == 8:
            root.height_role_hierachy()

        if int(operator) == 0:
            break

if __name__ == '__main__':
    main()
