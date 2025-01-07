# Task-Management-API
A Django REST Framework application for managing tasks with user authentication and advanced features such as filtering, sorting, and role-based access control. This API enables users to create, manage, and update tasks while ensuring privacy and task ownership.
------------------------------------------------------------------------------------
# Features
1- User Registration: Users can register and create an account, with all CRUD operations.
2- User Authentication: Secure access to the API using token-based authentication.
3- Create, update, and delete tasks.
4- Mark tasks as completed or incomplete.
5- Tasks marked as completed cannot be edited unless reverted to incomplete.
5- Tracks completion timestamp.
6- Filter tasks by status, priority, and due date.
7- Sort tasks by priority or due date.
8- Users can only view and manage their own tasks.
---------------------------------------------------------------------------------------
# Endpoints
1-  POST    /user/	      (Register a new user)
2-  GET     /user/	      (Get all users)
3-  DELETE  /user/<id>/	  (Delete a specific user)
3-  GET	    /task/	      (List all tasks for the authenticated user)
4-  POST	  /tasks/	      (Create a new task for the authenticated user)
5-  GET	    /tasks/<id>/	(Retrieve details of a specific task)
6-  PUT     /tasks/<id>/	(Update a specific task (if incomplete))
7-  DELETE	/tasks/<id>/	(Delete a specific task)
8-  PATCH	  /tasks/<id>/mark_status/	 (Mark a task as complete or incomplete)
