# Database Schema #

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

