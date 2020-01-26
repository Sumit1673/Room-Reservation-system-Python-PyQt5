## How to set up github using pycharm
1. Install github for your OS.
	# Windows: 
		https://git-scm.com/downloads
	# Linux: Run following commands in terminal:
			 1. sudo apt update
			 2. sudo apt install git
			 3. git --version  --> verify installation
2. Create a new project from Pycharm. 
3. After creating the project open the same folder if anything is there delete it.
4. Go to Pycharm, in menu bar click on the VCS option. 
5. Find Git-->clone. 
6. A new window will open to enter the details of the repository. 
7. Always enter the URL of your Github repo. ( not of any branch). 
8. Once all that is correct you can find files from your repository master branch into your folder.
9. Now switch your branch do: VCS --> Git --> Branch. 
10. Once that is done your Pycharm will indicate the branch version control.Or you can verify from the 
	version control tab at the bottom. 

# To add any file to Github repo of 
1. Right Click on the new file --> Git --> Add.
2. Right Click on the new file --> Git --> Commit file. Add Comments and commit. 
3. Right Click on the new file --> Git --> Push.

# To download any file from the other branch.
1. Open terminal in pycharm. 
2. Run the following commands. 
	git checkout master. 
	git checkout branch_name -- file_name 
	git checout your_previous_branch. 

	