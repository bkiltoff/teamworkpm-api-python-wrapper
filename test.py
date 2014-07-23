import json
from TeamworkPM.api import API
from TeamworkPM.models import *

api = API("snoisle", "grass856wool")
COMPANY_ID = 27919					# replace w/ your company ID

people = {}							# TeamworkPM User Ids
people['User Name'] = 12345

DefaultNotifyList = [ people['User Name'] ]

category = {}
category['Category 1'] = 1234

def main():
	projectData = {}
	projectData['name']        = 'API Test Proj'
	projectData['description'] = 'Test Project Description'
	projectData['companyId']   = COMPANY_ID
	projectData["category-id"] = category['Category 1']

	proj = Project(api)
	proj.create(projectData)

	for userID in DefaultNotifyList:
		proj.addPerson(userID)

	personid = people['User Name']

	tasklistTemplates = [ {"name":"Task List Template","todo-list-template-id":123456} ]

	for tasklist in tasklistTemplates:
		tasklist_id = proj.createTaskList(tasklist)	
		
		if tasklist_id:
			tasklist_obj = TaskList(api,tasklist_id)
			td = tasklist_obj.getTasks()
			aa = json.loads(td)
			for tasks in aa['todo-items']:
				tk = Task(api,tasks['id'])
				tk.assignPerson(tasks['id'],personid,tasks['description'])
	
	proj.createMessage( {"title":"Project Message","body":"Job Start Message", "notify":DefaultNotifyList} )
	
main()





