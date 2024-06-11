import pandas as pd
from jira import JIRA
import re


file_path = "/Users/abhayvaghasiya/Desktop/DS4SE/assingment_2/assignment-2/Issues_2nd.xlsx"
issue_df = pd.read_excel(file_path, sheet_name="Tajo")


issue_keys_list = issue_df["Issue key"].tolist()


print(f"Total issues: {len(issue_keys_list)}")


JIRA_SERVER_URL = 'https://issues.apache.org/jira/'
jira_client = JIRA(JIRA_SERVER_URL)


query_template = 'issuekey in ({}) AND project = TAJO'
required_fields = "parent,summary,description,issuetype,status,comment"
fields_list = required_fields.split(',')


field_mapping = {
    "issuetype": "name",
    "parent": "key",
    "status": "name"
}

# Create the JQL query for all issue keys
jql = query_template.format(','.join(issue_keys_list))


collected_issue_data = []

# Fetch all issues in one go
search_results = jira_client.search_issues(jql, fields=required_fields, maxResults=len(issue_keys_list))

for issue in search_results:
    issue_info = [issue.key]
    for field in fields_list:
        field_value = issue.raw['fields'].get(field)
        if field == 'comment' and field_value:
            comment_bodies = [comment['body'] for comment in field_value['comments']]
            issue_info.append(comment_bodies)
        elif field in field_mapping and field_value:
            issue_info.append(field_value.get(field_mapping[field], None))
        else:
            issue_info.append(field_value)
    collected_issue_data.append(issue_info)


columns = ["Issue key", "Parent", "Summary", "Description", "Issue Type", "Status", "Comments"]
issues_df = pd.DataFrame(collected_issue_data, columns=columns)


def clean_illegal_chars(text):
    illegal_char_pattern = re.compile(r'[\x00-\x08\x0b-\x0c\x0e-\x1f]')
    if isinstance(text, str):
        return illegal_char_pattern.sub('', text)
    return text


cleaned_issues_df = issues_df.apply(clean_illegal_chars)


output_file_path = "/Users/abhayvaghasiya/Desktop/DS4SE/assingment_2/assignment-2/Tajo_Issues.xlsx"
cleaned_issues_df.to_excel(output_file_path, index=False)
