# Engineering Notebook
Welcome to King of Games Engineering Notebook! Today we are going to help you get started in provisioning your 
terminal and shell in a few quick and easy steps.

Step 1. Open your Command Prompt by going to the start menu in your desktop opening "Command Prompt"
Step 2. Go to https://www.docker.com/products/docker-desktop/ Download Docker Desktop app and install on your desktop
Step 3. Open and Run Docker
Step 4. Go back to your commandline terminal and copy and paste the following

   mkdir -p ~/swexp-engineering-notebook && cd ~/swexp-engineering-notebook

Step 5. Within the newly created directory copy and paste the following to initialize git

   apt-get update
   apt-get install -y git

Step 6. Finally, copy and paste the final command in your Commandline Termianl 

   git init
   printf '# Engineering Notebook\n\n## %s — Environment\n' "$(date +%F)" > NOTEBOOK.md
   git add NOTEBOOK.md && git commit -m "INFRA-1001: open engineering notebook"

Step 7. Open your NOTEBOOK.md by copy and pasting the commandline prompt 

   nano NOTEBOOK.md

Step 8. Add your instructions on how you got here to this md file!

Good luck!!


## 2026-07-24 — Environment
