import subprocess
import os

def execute_command(command):
    try:
        result = subprocess.run(command, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("Command Output:", result.stdout)
        print("Command Errors:", result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Command failed {' '.join(command)}: {e}")
        print(e.stdout)
        print(e.stderr)
    except Exception as e:
        print(f"Unexpected error: {e}")

def run_limbo(java_limbo_jar, rsf_file_path, output_path, project_name, project_version, language='java', measure='IL'):
    command = [
        'java', '-Xmx14024m', '-jar', java_limbo_jar,
        'algo=LIMBO', f'language={language}', 
        f'deps={rsf_file_path}', 
        f'measure={measure}',
        f'projname={project_name}', 
        f'projversion={project_version}', 
        f'projpath={output_path}',
        'stop=preselected',
        'stopthreshold=12', 'packageprefix=""', 'filelevel=true'
    ]
    execute_command(command)

def run_limbo_for_commits(commits_directory, java_limbo_jar, project_name):
    commit_folders = [os.path.join(commits_directory, f) for f in os.listdir(commits_directory) if os.path.isdir(os.path.join(commits_directory, f))]
    
    for commit_folder in commit_folders:
        commit_id = os.path.basename(commit_folder)
        rsf_files = [f for f in os.listdir(commit_folder) if f.endswith('.rsf')]
        
        for rsf_file in rsf_files:
            rsf_file_path = os.path.join(commit_folder, rsf_file)
            output_path = os.path.join(commit_folder, 'limbo_output', rsf_file.replace('.rsf', ''))
            print(f"Processing {rsf_file_path} into {output_path}")
            run_limbo(java_limbo_jar, rsf_file_path, output_path, project_name, commit_id)

if __name__ == "__main__":
    java_limbo_jar = '/Users/shrutikhule/Desktop/DS4SE/ds4se/arcade_core_clusterer.jar'
    commits_directory = '/Users/shrutikhule/Desktop/DS4SE/ds4se/parent_jars'
    project_name = 'HDFS'

    run_limbo_for_commits(commits_directory, java_limbo_jar, project_name)
