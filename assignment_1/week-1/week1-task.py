import pandas as pd
from pydriller import Repository
from radon.metrics import mi_visit


# Load the Excel file to get issue IDs
df = pd.read_excel("hdfs_id.xlsx")
issue_ids = df["Key"].tolist()  # Adjust the column name if needed

# Dictionaries to store results
issue_commits = {}
parent_commits = {}
commit_data = []

# Traverse commits with Repository
for commit in Repository(assignment_repo).traverse_commits():
    # Find commits related to the issue IDs
    relevant_issues = [issue_id for issue_id in issue_ids if str(issue_id) in commit.msg]

    if relevant_issues:
        # Store commit hashes and parent commits
        for issue_id in relevant_issues:
            issue_commits[issue_id] = commit.hash
        parent_commits[commit.hash] = [parent.hash for parent in commit.parents if hasattr(parent, 'hash')]

        # Gather detailed commit information
        commit_info = {
            "commit_hash": commit.hash,
            "author": commit.author.name,
            "author_date": commit.author_date,
            "message": commit.msg,
            "relevant_issues": relevant_issues,
        }

        # Ensure the commit has modifications
        if hasattr(commit, 'modifications'):
            # Basic commit metrics
            commit_info["added_files"] = len(commit.modifications)  # Added files
            commit_info["deleted_files"] = sum(1 for mod in commit.modifications if mod.change_type.name == "DELETE")
            commit_info["modified_files"] = sum(1 for mod in commit.modifications if mod.change_type.name == "MODIFY")

            # Lines of code added and deleted
            commit_info["added_lines"] = sum(mod.added for mod in commit.modifications)
            commit_info["deleted_lines"] = sum(mod.removed for mod in commit.modifications)

            # Cyclomatic complexity with Radon
            for mod in commit.modifications:
                if mod.source_code:
                    dmm = mi_visit(mod.source_code)
                    commit_info["complexity"] = dmm.complexity  # Cyclomatic complexity

        commit_data.append(commit_info)

# Save the commit data to an Excel file for further analysis
commit_data_df = pd.DataFrame(commit_data)
commit_data_df.to_csv("commit_analysis_results.csv", index=False)

# Output the stored dictionaries for reference
#print("Issue Commits:", issue_commits)
#print("Parent Commits:", parent_commits)
