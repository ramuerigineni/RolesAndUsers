# Role Hierarchy

## Execution test as
#### python3 role_hierarcy.py


## Sampler Test execution details
### 1. Create the root role and display it.
```
Enter root role name : CEO
```
### 2. Now support the add sub role operation to the root role
```
Operations :
1. Add Sub Role.
2. Display Roles
3. Delete Role.
4. Add User.
5. Display Users.
6. Display Users and Sub Users.
7. Number of users from top
8. Height of role hierachy.
Operation to be performed : 1
Enter sub role name : CTO
Enter reporting to role name : CEO
Operations :
1. Add Sub Role.
2. Display Roles
3. Delete Role.
4. Add User.
5. Display Users.
6. Display Users and Sub Users.
7. Number of users from top
8. Height of role hierachy.
Operation to be performed : 1
Enter sub role name : COO
Enter reporting to role name : CEO
Operations :
1. Add Sub Role.
2. Display Roles
3. Delete Role.
4. Add User.
5. Display Users.
6. Display Users and Sub Users.
7. Number of users from top
8. Height of role hierachy.
Operation to be performed : 1
Enter sub role name : Director of Technology
Enter reporting to role name : CTO
```
### 3. Display Roles.
```
Operations :
1. Add Sub Role.
2. Display Roles
3. Delete Role.
4. Add User.
5. Display Users.
6. Display Users and Sub Users.
7. Number of users from top
8. Height of role hierachy.
Operation to be performed : 2
CEO, CTO, Director of Technology, Technical Architect, COO, Senior Product Engineering Manager, Manager Engineering, Developer, DevOps, Tester, Senior Product Marketing Manager, Manager Marketing, Marketing analyst, Marketing Executive,
```
### 4. Delete Role
```
Operations :
1. Add Sub Role.
2. Display Roles
3. Delete Role.
4. Add User.
5. Display Users.
6. Display Users and Sub Users.
7. Number of users from top
8. Height of role hierachy.
Operation to be performed : 3
Enter the role to be deleted : CTO
Enter the role to be transferred : Director of Technology

Operations :
1. Add Sub Role.
2. Display Roles
3. Delete Role.
4. Add User.
5. Display Users.
6. Display Users and Sub Users.
7. Number of users from top
8. Height of role hierachy.
Operation to be performed : 2
CEO, Director of Technology, Technical Architect, COO, Senior Product Engineering Manager, Manager Engineering, Developer, DevOps, Tester, Senior Product Marketing Manager, Manager Marketing, Marketing analyst, Marketing Executive,
```
### 5. Add User name to existing role
```
Operations :
1. Add Sub Role.
2. Display Roles
3. Delete Role.
4. Add User.
5. Display Users.
6. Display Users and Sub Users.
7. Number of users from top
8. Height of role hierachy.
Operation to be performed : 4
Enter User Name : Tyson
Enter Role : CEO
Operations :
1. Add Sub Role.
2. Display Roles
3. Delete Role.
4. Add User.
5. Display Users.
6. Display Users and Sub Users.
7. Number of users from top
8. Height of role hierachy.
Operation to be performed : 4
Enter User Name : COO
Enter Role : COO
```
### 6. Display Users
```
Operations :
1. Add Sub Role.
2. Display Roles
3. Delete Role.
4. Add User.
5. Display Users.
6. Display Users and Sub Users.
7. Number of users from top
8. Height of role hierachy.
Operation to be performed : 5
Tyson - CEO
Ray - COD
Will - Senior Product Engineering Manager
Sam - Manager Engineering
Mike - Developer
Ram - DevOps
Naresh - Tester
Vidhu - Senior Product Marketing Manager
Nameesh - Manager Marketing
Ravi - Marketing analyst
Mahesh - Marketing Executive
Max - Director of Technology
Kenny - Technical Architect
```
### 7. Display Users and Sub Users
```
Operations :
1. Add Sub Role.
2. Display Roles
3. Delete Role.
4. Add User.
5. Display Users.
6. Display Users and Sub Users.
7. Number of users from top
8. Height of role hierachy.
Operation to be performed : 6
Tyson - John , Will , Vidhu
John - Max
Max - Kenny
Kenny -
Will - Sam
Vidhu - Nameesh
Sam - Mike , Ram , Naresh
Mike -
Ram -
Naresh -
Nameesh - Ravi , Mahesh
Ravi -
Mahesh -
```
### 8. Number of users from top for given user
```
Operations :
1. Add Sub Role.
2. Display Roles
3. Delete Role.
4. Add User.
5. Display Users.
6. Display Users and Sub Users.
7. Number of users from top
8. Height of role hierachy.
Operation to be performed : Mike
Enter user name : 3
```
### 9. Display height of role hierachy
```
Operations :
1. Add Sub Role.
2. Display Roles
3. Delete Role.
4. Add User.
5. Display Users.
6. Display Users and Sub Users.
7. Number of users from top
8. Height of role hierachy.
Operation to be performed : 8
height 3
```

