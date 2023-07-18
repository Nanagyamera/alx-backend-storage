NoSQL Database and Nginx Log Analysis

This repository provides scripts and functions to perform analysis on NoSQL databases, specifically MongoDB, as well as Nginx log files. It offers various capabilities such as retrieving database information, manipulating data, and extracting statistics from log files.

REQUIREMENT

- Python 3.x
- pymongo library
- MongoDB server

SETUP

1. Clone the repository to your local machine.

2. Install the required dependencies by running `pip install -r requirements.txt`.

3. Ensure that your MongoDB server is up and running.

SCRIPTS AND FUNCTIONS

The following sections describe each script or function in detail, along with their usage and purpose.

1. 0-list_databases

This script lists all databases in a MongoDB NoSQL database.

2. 1-use_or_create_database

This script creates or uses a specific database in a MongoDB NoSQL database.

3. 2-insert

This script inserts a new document into a collection in a MongoDB NoSQL database.

4. 3-all

This script lists all documents in a collection in a MongoDB NoSQL database.

5. 4-match

This script list all documents with a particular name

6. 5-count

This script displays the number of documents in the collection school

7. 6-update

This script adds a new attribute to a document in the collection school

8. 7-delete

This script deletes documents from a collection in a MongoDB NoSQL database

9. 8-all.py

This function lists all documents in a collection

10. 9-insert_school.py

This function inserts a new document in a collection based on kwargs

11. 10-update_topics.py

This function updates a document in a collection in a MongoDB NoSQL database.

12. 11-schools_by_topic.py

This function retrieves a list of schools with a specific topic from a collection in a MongoDB NoSQL database.

13. 12-log_stats.py

This function  provides statistics about Nginx logs stored in a MongoDB NoSQL database.
top_students.py

14. 100-find

This script lists all documents with name starting by Holberton in the collection school

15. 101-students.py

This function retrieves a list of top students sorted by average score from a collection in a MongoDB NoSQL database.

16. 102-log_stats.py

In this function I improve 12-log_stats.py by adding the top 10 of the most present IPs in the collection nginx of the database logs


CONTRIBUTIONS

Contributions to this repository are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

LICENSE

This project is licensed under the [MIT License](LICENSE).
