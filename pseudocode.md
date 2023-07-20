# MVP #
    By default, the app should perform full CRUD operations (at least one of each Create, Read, Update, Delete) on the supplied SQL Database file and prompt the user for input in the terminal to show aq list of heroes and their friends.

# MoSCoW #

    Must haves:
        Create a Connection to a Database using Python 3 and view the database (using the vscode extension)
        The supplied superheroes.sql database file (attached the Google Classroom assignment) contains CREATE TABLE and INSERT statements to get you started with seeded data. (Do not modify the SQL file) Use the VSCode extension to execute the file from top to bottom to get the appropriate tables/entries created.
        Decide/Plan/Pseudocode on a minimum of four CRUD operations you wish to implement (at least one operation for Create, Read, Update, & Delete) - document these in your README.md
        Interactive creation, update, delete of a hero in the terminal via Python script, with commands that are available for the README.md

    Should haves:
        Can have mutual friends
        Can add new friends
        Can have mutual enemies
        Can add new enemies

    Should haves:
        More interactivity in the terminal (i.e. a search of heroes, get list of heroes friends, add abilities, etc.)
        Can add likes
        Can add dislikes
        Can have multiple hero abilities

    Won't haves:
        ASCII art for visual elements

# Procedural #

## Database Schema ##

    Database schemas define how data is organized in a RDBMS

    Conceptual schema 
        big picture overview of what the system will contain, how it's organized, and which business rules are involved.

    Logitcal db schema
        less abstract than conceptual. They clearly define objects with info like tables names, field names, entity relationships, and integrity constraints.

    Physical db schema
        provide technical info that the logical schema lacks. Includes the syntax that is used to create data structures within disk storage.

    Star schema
        has a single central fact table that is surrounded by dimension tables.
    
    Snowflake schema
        has of one fact table that is coneected to many dimension tables that are connected to many other dimentions tables through many to one relationship.

    The schema will relate how the different fields interact with one another. It will also distinguish the primary key (PK) and the foreign key (FK).

# Functional #

List of tables:

    table
        abilities
    fields
        id
        hero_id
        ability_type_id
    
    table
        ability_types
    fields
        id
        name
    
    table
        heroes
    fields
        id
        name
        about_me
    
    table
        relationship_types
    fields
        id
        name
    
    table
        relationships
    fields
        id
        hero1_id
        hero2_id
        relationship_type_id


![SQL heroes schema](/img/SQL%20Heroes%20schema.png)

# Queries #

CRUD

    create a data instance
    read a data instance
    update a data instance
    delete a data instance

CREATE
    INSERT INTO heroes (id, name, about_me)
    VALUES (id, name, about_me);

READ
    SELECT name, about_me
    FROM heroes;

UPDATE
    UPDATE heroes
    SET id = 1, name = 'Shawn', about_me = 'super coding skills'
    WHERE id = 1; (this is just a placeholder for now)

DELETE
    DELETE FROM heroes WHERE id = 1;