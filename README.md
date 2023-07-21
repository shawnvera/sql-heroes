# **SQL HEROES TEMPLATE** 

## Setup
- After creating your own repo from the template, create a local copy either with the Github CLI tool (recommended) or a git clone.
- Make sure you have Docker Desktop downloaded and running
- Open VScode and install the [Dev Containers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers)
- Open your repo in VScode, after a few moments you should see a prompt from VScode asking if you want to reopen the repo in a dev container, follow the prompt to do so. If you are not prompted, you can click the remote connection icon in the bottom left corner and select 'Reopen in Container'
- Once the container is built, click the SQL tools extension to establish your database connection. All required fields, including password, are 'postgres'.
- Proceed to set up your file structure per Project document.


# CRUD operations

# Be able to create a new hero in the heroes table.
1. Open create_hero.py file
2. Run the file
3. When prompted enter the hero's name and press enter.
4. Enter the about me and press enter.
5. Enter the biography as prompted by the program and press enter.
6. The new hero is now in the database.

# Be able to read the heroes table and display information.
1. Open select all heroes python file
2. Run the program
3. All heroes currently in the database will be displayed

# Be able to update items already in the heroes table.
1. Open update_hero.py
2. Run the file
3. When prompted enter updated hero name
4. When prompted enter updated about me
5. When pompted enter updated biography
6. When prompted enter new hero name.
7. Press enter and the hero will be updated

# Be able to delete heroes from the table.
1. Open delete hero python file
2. Run the program
3. When prompted enter the name of the hero that you wish to delete
4. Press enter and the hero will be deleted

# Be able to create a relationship between characters
1. Open create relationship python file
2. Run the program
3. When prompted enter character information. The IDs of the two characters you want to create a relationship between will be required. The last prompt will determine "friend" or "enemy". Enter a "1" for friend or enter a "2" for enemy.
4. After pressing enter you'll get a notice of whether the relationship succeeded or failed.

# Be able to delete a relationship between characters
1. Open delete relationship python file
2. Run the program
3. When prompted enter the hero ID of the relationship you want to delete. WARNING: This will delete all relationships for that hero
4. Press enter and the relationships will be deleted