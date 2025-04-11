import os

def update_project_status(project_name):
    # This function updates the project status based on the current state
    if 'updated' in os.listdir('project_directory'):
        print("The project has been updated.")
    else:
        print("No changes made.")

update_project_status('project_name')
