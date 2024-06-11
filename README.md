# DS4SE
Assignments 1 and 2 of DS4SE

# Report: DS4SE

**by Abhay Kishorbhai Vaghasiya - 6987244**

## Assignment 1

### Week 1

**Task 3: Determine Size and Quality Information of Commit Changes**

I developed a Python script using PyDriller to analyze commits comprehensively. The script performs various tasks, including counting the number of files added, modified, and deleted for each commit. It also measures the lines of code added and deleted per file and tracks the number of methods added, deleted, and changed per file. To enhance the analysis, the script collects design and quality metrics (DMM metrics) for each commit and calculates the complexity for each file. This thorough approach provides a detailed examination of the changes made in each commit.

### Week 2

**Task 4: Running Clustering Algorithms on Commit Source Code**

I developed a Python script to run clustering algorithms on the source code of each commit. The script automated resetting the Git repository to a specific commit, building the project using Maven, and extracting dependencies. Using JavaParser, I created another script to extract dependencies for each commit for the Limbo clustering algorithm, which I planned to run on each commit's dependencies.

Additionally, the Python script automated the build and dependency extraction process. It reset the repository to specific commits, built the project with Maven, and moved the generated JAR files to a designated output directory. However, I encountered issues when running Maven directly on commits 50 to 70 and was unable to generate JAR files for these commits.

### Week 3

I was still working on running the script on multiple commits. I managed to generate a JAR file for commit number 30. However, I faced issues generating more files. It took 23 minutes to run one commit on my computer. I also tried running it directly from the Hadoop folder, but I encountered the same problem there.

### Week 4

I joined group number 7. Here, I worked on assignment 1 and week 4, which were still incomplete at that time. I analyzed and answered the remaining research questions, created the summary, completed the report, and worked on creating the presentation for the group. This teamwork ensured that we covered all parts of the assignment and presented them well.

## Assignment 2 in Group 5

### Week 1: Report on Issue Data Extraction and Preparation

**Task 1 & 2:**

For this task, I extracted and preprocessed issue data for the Tajo project from JIRA. I used the `jira` Python library to connect to the JIRA server and constructed a JQL query to fetch the relevant issues. I retrieved essential information such as issue summaries, descriptions, types, statuses, parent issues (if available), and comments. I processed each issue to extract this information, handling special cases like nested fields and multiple comments. I then cleaned the data by removing any illegal characters that could interfere with further analysis. After processing and cleaning the data, I organized it into a pandas DataFrame. Finally, I exported the cleaned data to an Excel file for further analysis.

###Only My contribution to the assignments mentioned here and in the repo.

### Week 2

Started working with group 7.
