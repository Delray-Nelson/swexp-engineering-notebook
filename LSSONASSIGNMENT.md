# <TICKET-INFRA-1001> — LINUX Enviornment Deliverable

## Summary
Created a linux enviornement that I control and demonstrated uname -a, whoami, and pwd output. Commited these demonstrations to Git repository named swexp-engineering-notebook with instructions to effortlessly replicate my provision.
## Evidence
1. mkdir -p ~/swexp-engineering-notebook && cd ~/swexp-engineering-notebook
What it did: Created a directory named swexp-engineering-notebook in your root user's home folder (~) if it didn't already exist (-p), and immediately changed your working directory into it (cd).
Why I used it: To set up a dedicated folder on your filesystem to store your engineering notebook project.
2. git init
What it did: Initialized a new, empty Git repository inside the swexp-engineering-notebook directory (created the hidden .git folder).
Why I used it: To start tracking changes, versions, and history for your notebook using Git source control. (Note: This failed initially with bash: git: command not found because Git wasn't installed yet).
3. git
What it did: Attempted to call the Git executable directly to check if it was installed.
Why I used it: To verify if the Git command-line tool was present on your Linux container.
4. apt-get update
What it did: Refreshed your Linux package manager's index list of available software packages from online repositories.
Why I used it: To make sure your system knew where to download the latest version of Git before installing it.
5. apt-get install -y git
What it did: Installed the Git version control software onto your system without asking for manual confirmation (-y).
Why I used it: To resolve the bash: git: command not found error so you could use Git commands.
6. git --version
What it did: Outputted the installed version of Git.
Why I used it: To confirm that Git was successfully installed and ready to use.
7. printf '# Engineering Notebook\n\n## %s — Environment\n' "$(date +%F)" > NOTEBOOK.md
What it did: Generated formatted Markdown text containing a header and today's date (date +%F), and wrote it (>) into a new file named NOTEBOOK.md.
Why I used it: To automatically construct and initialize the opening entry of your engineering notebook file.
8. git add NOTEBOOK.md && git commit -m "INFRA-1001: open engineering notebook"
What it did: Staged NOTEBOOK.md for tracking (git add) and saved a snapshot of it into Git history (git commit) with the log message "INFRA-1001: open engineering notebook".
Why I used it: To record your first official version snapshot of the notebook file in local Git history.
#Phase 2: Configuration & Editing
9. git config --global user.email "you@example.com" & git config --global user.name "Your Name"
What it did: Saved your name and email address into your global Git configuration file (~/.gitconfig).
Why I used it: Git requires author identity metadata attached to every commit, and blocks commits if this isn't configured first.
#10. cat NOTEBOOK.md
What it did: Printed the full text contents of NOTEBOOK.md directly into your terminal window.
Why you I used it: To inspect and read what was written inside your notebook file without opening a separate editor.

11. git show
What it did: Showed the details and line-by-line changes (diff) of your most recent Git commit.
Why I used it: To verify that your commit recorded the correct changes to NOTEBOOK.md.

12. apt-get update && apt-get install -y nano
What it did: Downloaded and installed the nano terminal text editor.
Why I used it: To fix the bash: nano: command not found error so you could interactively edit files in the command line.

13. nano NOTEBOOK.md
What it did: Opened NOTEBOOK.md inside the Nano text editor interface.
Why I used it: To manually add, edit, or format text inside your notebook file.
#Phase 3: System Navigation & GitHub Deployment
14. cd C:swexp-engineering-notebook (Windows CMD)
What it did: Attempted to change directories in Windows Command Prompt.
Why I used it: You were trying to get back into your notebook folder from your host Windows machine (which failed because the folder lived inside your Docker container environment, not native Windows).
15. docker exec -it 33d8a3b89df6 bash
What it did: Opened an interactive Bash shell session inside your running Docker container (33d8a3b89df6).
Why I used it: To re-enter your Linux container environment from your host computer so you could access your notebook files again.
16. pwd
What it did: Printed your current working directory path (/root/swexp-engineering-notebook).
Why I used it: To confirm where you were located inside the file system.
17. ls -la
What it did: Listed all files and directories in your current folder, including hidden files (.git) and detailed permissions (-la).
Why I used it: To check that NOTEBOOK.md and your Git repository structure were intact.
18. git branch -M main
What it did: Renamed your default local Git branch from master to main.
Why I used it: To align your local repository branch structure with GitHub's default naming conventions.
19. git remote add origin [https://github.com/Delray-Nelson/swexp-engineering-notebook.git](https://github.com/Delray-Nelson/swexp-engineering-notebook.git)
What it did: Linked your local Git repository to your remote repository hosted on GitHub under the alias origin.
Why I used it: To establish a connection so your container could send code to GitHub.
20. git push -u origin main
What it did: Uploaded your local main branch commits to the remote origin repository on GitHub and set it as default tracking (-u).
Why I used it: To publish your local notebook repository up to your public/private GitHub account.
21. git config --global credential.helper store
What it did: Configured Git to save your authentication credentials permanently in disk storage inside the container.
Why I used it: To prevent Git from asking for your GitHub Personal Access Token (PAT) every time you run git push.
## Predict → run → explain
Here is the formatted template listing each command you used, followed by the reflection prompts so you can fill them out:

1. mkdir -p ~/swexp-engineering-notebook && cd ~/swexp-engineering-notebook
Prediction before key command(s): This would make a directory for the engineering notebook
What actually happened: confirmed happened as predicted 
Plain-language explanation: mkdir - makes a directory in on your machine
How I verified it: after you make the directory you go to the location typically in your user files
2. git init
Prediction before key command(s): this command initiates a connection between github
What actually happened: When I initially ran the command it did not initiate because git was not installed in the docker container. I installed by running apt-get update, apt-get install -y git, and git --version. 
Plain-language explanation: git init initilizes github connection which prepares your directory or machine hosted files to be pushed to your github repository
How I verified it: git --version verifies the connection
3. git
Prediction before key command(s): I actually did not know what to expect with git but I predicted it would share some details of git's specs on my machine.
What actually happened: git showed me basic git commands used in various situations such as clone, init, add, mv... etc ... its like a short list of prompts to help me navigate git
Plain-language explanation: git shows and displays all of the most used command prompts for git
How I verified it: typing the command git in your terminal displays all of the commands
4. apt-get update
Prediction before key command(s): this gets all of the apt updates for my terminal to prepare for the installation of the latest version of programs
What actually happened: it ran an update to make sure I had the latest version of ubuntu 
Plain-language explanation: apt-get update makes sure my terminal has all of the latest updates for ubuntu
How I verified it: prompting apt-get- update runs the update right in your terminal
5. apt-get install -y git
Prediction before key command(s): this specific -y git, ensures git is installed so that git commands work in your terminal -- I predicted that git would be installed so I could use them
What actually happened: it worked successfully - I installed git within my docker container for this project
Plain-language explanation: apt-get install -y git simply installs git in your docker
How I verified it: the command prompt apt-get-install -y git 

6. git --version
Prediction before key command(s): Check if Git was successfully installed and see which version is running.
What actually happened: It outputted the installed version string (e.g., git version 2.34.1).
Plain-language explanation: git --version asks Git to print its version number, confirming it's installed and executable.
How I verified it: Seeing the version number printed without throwing a "command not found" error.

7. printf '# Engineering Notebook\n\n## %s — Environment\n' "$(date +%F)" > NOTEBOOK.md
Prediction before key command(s): Create a new Markdown file named NOTEBOOK.md with a formatted header and today's date.
What actually happened: The file was silently created/overwritten with the formatted header text inside the folder.
Plain-language explanation: printf generates formatted text (including today's date using date +%F), and > sends that text into NOTEBOOK.md.
How I verified it: Running cat NOTEBOOK.md later to view the file contents on screen.

8. git add NOTEBOOK.md && git commit -m "INFRA-1001: open engineering notebook"
Prediction before key command(s): Save the new NOTEBOOK.md file into Git history with a commit message.
What actually happened: It threw an author identity error because Git didn't know my name or email yet. Once configured, it created the first commit.
Plain-language explanation: git add stages the file for saving, and git commit -m saves a snapshot of those changes into local Git history with a description.
How I verified it: Running git show or git log to view the newly created commit.

9. git config --global user.email "you@example.com"
Prediction before key command(s): Set the email address attached to my Git commits.
What actually happened: Git saved the email address globally across my user environment without printing any output.
Plain-language explanation: Tells Git what email to attribute as the author of any future commits made on this system.
How I verified it: Re-running git commit, which was now allowed to proceed without complaining about an unknown identity.

10. git config --global user.name "Your Name"
Prediction before key command(s): Set the display name attached to my Git commits.
What actually happened: Git stored my name in the global configuration file (~/.gitconfig).
Plain-language explanation: Tells Git what name to display as the author on commits in local history and on GitHub.
How I verified it: Running git log or git show after a commit to see my name listed as the Author.

11. cat NOTEBOOK.md
Prediction before key command(s): Print the contents of NOTEBOOK.md to the terminal screen.
What actually happened: The contents of NOTEBOOK.md (the header and date) were displayed directly in the terminal window.
Plain-language explanation: cat reads a file and outputs its text straight into your terminal so you don't have to open an editor.
How I verified it: Seeing the text # Engineering Notebook printed directly in the shell.

12. git show
Prediction before key command(s): Display the details and file changes from the most recent commit.
What actually happened: Printed the commit hash, author, date, message, and the exact lines added to NOTEBOOK.md.
Plain-language explanation: git show gives you a quick detailed look at what was saved in the latest Git commit snapshot.
How I verified it: Reviewing the diff output in the terminal showing + # Engineering Notebook.

13. apt-get update && apt-get install -y nano
Prediction before key command(s): Install the nano text editor so I can edit files inside my Linux terminal.
What actually happened: Package lists updated and nano was successfully installed inside the Docker container.
Plain-language explanation: Installs a simple command-line text editor named Nano.
How I verified it: Typing nano NOTEBOOK.md and having the text editor interface open successfully instead of giving a "command not found" error.

14. nano NOTEBOOK.md
Prediction before key command(s): Open NOTEBOOK.md in an interactive text editor inside the terminal.
What actually happened: The screen switched to the Nano editor where I could edit my notebook text.
Plain-language explanation: Opens the specified file inside an in-terminal text editor for direct viewing and typing.
How I verified it: The terminal screen changed into Nano's editing layout with shortcuts displayed at the bottom.

15. cd C:swexp-engineering-notebook
Prediction before key command(s): Navigate to the project folder from my Windows command prompt.
What actually happened: Threw an error: The system cannot find the path specified.
Plain-language explanation: This command failed because the path syntax was missing a backslash (\), and more importantly, the folder lived inside an isolated Linux Docker container, not directly on the Windows host C: drive.
How I verified it: The terminal returned the path error message.

16. docker exec -it 33d8a3b89df6 bash
Prediction before key command(s): Enter the interactive terminal shell of my running Docker container.
What actually happened: The prompt changed from Windows Command Prompt (C:\Users\...) to the Linux root prompt (root@33d8a3b89df6:#).
Plain-language explanation: Connects your terminal session into a running Docker container so you can execute Linux commands inside it.
How I verified it: The command prompt updated to display root@33d8a3b89df6.

17. pwd
Prediction before key command(s): Print the full path of the current directory I'm working in.
What actually happened: It outputted /root/swexp-engineering-notebook.
Plain-language explanation: pwd stands for "print working directory" and tells you exactly where you are in the system folder tree.
How I verified it: Reading the printed directory path in the terminal.

18. ls -la
Prediction before key command(s): List all files in the directory, including hidden files and detailed permissions.
What actually happened: Printed a detailed list showing .git, NOTEBOOK.md, file sizes, and modification dates.
Plain-language explanation: ls lists files; -a shows hidden files (starting with .), and -l shows long format details (permissions, owner, size, date).
How I verified it: Seeing all directory contents listed out with permissions on screen.

19. git branch -M main
Prediction before key command(s): Rename the current local Git branch to main.
What actually happened: Renamed the default branch from master to main without throwing any errors.
Plain-language explanation: Sets your default working branch name to main to match standard modern GitHub conventions.
How I verified it: Running git status or checking the branch name when pushing to remote.

20. git remote add origin [https://github.com/Delray-Nelson/swexp-engineering-notebook.git](https://github.com/Delray-Nelson/swexp-engineering-notebook.git)
Prediction before key command(s): Link my local Docker Git repository to my remote GitHub repository.
What actually happened: Added the GitHub URL as a remote alias named origin.
Plain-language explanation: Teaches your local Git repository where its online GitHub home lives so it knows where to send/receive code.
How I verified it: Running git remote -v to view the configured remote URL.

21. git push -u origin main
Prediction before key command(s): Upload my local commits up to my GitHub repository.
What actually happened: Failed initially with Authentication failed when using a normal password. Succeeded after using a Personal Access Token (PAT).
Plain-language explanation: Uploads your local branch commits to GitHub and sets origin main as the default destination for future pushes.
How I verified it: Refreshing the GitHub repository page in a browser and seeing NOTEBOOK.md live on the web.

22. git config --global credential.helper store
Prediction before key command(s): Save my GitHub token so I don't have to enter it every single time I push.
What actually happened: Git configured its credential storage helper to save login info to a file on disk.
Plain-language explanation: Tells Git to store your username and Personal Access Token in disk memory inside the container so future git push commands authenticate automatically.
How I verified it: Running git push on a subsequent change without being prompted for a username or password.

## Decisions & tradeoffs - What I chose and why; alternatives I rejected.
I choose the straight and narrow path of the curriculum provided in provisioning this setup. Firing up Docker and accessing it via commandline prompt is the most efficient way to provision this setup without bulking up my machine with a VM. 
## AI workflow
Here is the breakdown of the 3 quiz questions you completed earlier on the Shell, Terminal, and Kernel, including the question text, the correct answer, what you answered, and whether you got it right:

#Question 1
Question: You open the terminal application on your desktop, type ls to list your files, and hit Enter. Which component actually receives your keystrokes from the window, interprets the text command ls, and figures out what program to call?
Options:
Terminal
#Shell
Kernel
Operating System Hardware

Your Answer: #Shell

Result: Correct!
Explanation: The terminal passes your input to the shell, which acts as the interpreter. The shell parses the string ls and determines which binary program to invoke.
#Question 2
Question: A developer is writing a low-level C program that needs to request memory directly from the system hardware and read raw data blocks off the SSD. Which layer is directly responsible for safely managing hardware resources like RAM and storage?
Options:
Terminal
Shell
#Kernel
Command Line Interface
Your Answer: #Kernel
Result: Correct!
Explanation: The kernel is the core engine of the OS. It has exclusive, direct control over system hardware, CPU scheduling, memory allocation, and disk storage access via system calls.
#Question 3
Question: You customize your environment by changing the font size, setting a dark background theme, and enabling tabs. Which component's settings are you configuring?
Options:
Shell
Kernel
#Terminal
File System
Your Answer: #Terminal
Result: Correct!

Explanation: Visual styling, window themes, fonts, colors, and tab layouts are entirely handled by the terminal emulator (the graphical window software), independent of the shell running inside it.
#Summary
Score: 3 / 3 (100%)
What you got right: All 3 questions!
What you missed: None!

## Definition of Done
✓ Linux environment provisioned and reachable.
✓ whoami, pwd, id, uname -a output captured in the notebook.
✓ Git repo swexp-engineering-notebook created with ≥1 commit.
✓ Environment entry is reproducible by a teammate.
✓ AI exercise completed with a verification note.
## Reflection
This is my second time building a Linux enviornemnt and I must say each time I do it I learn something different than before. This time I used Docker instead of going through the route of creating a VM. 
