import subprocess
import sys
import os
import tempfile

def run_with_wine(executable, args):
    wine_cmd = ['wine', executable] + args
    subprocess.check_call(wine_cmd)

def copy_metadata(source_file, target_file, resource_hacker_path, sigthief_path):
    with tempfile.TemporaryDirectory() as temp_dir:
        resource_file = os.path.join(temp_dir, 'resources.res')
        extract_args = [
            '-open', source_file,
            '-save', resource_file,
            '-action', 'extract',
            '-mask', ',,,'
        ]
        run_with_wine(resource_hacker_path, extract_args)
        
        res_target_file = os.path.join(os.path.dirname(target_file), 'res_' + os.path.basename(target_file))
        add_args = [
            '-open', target_file,
            '-save', res_target_file,
            '-action', 'addoverwrite',
            '-resource', resource_file,
        ]
        run_with_wine(resource_hacker_path, add_args)

    signed_target_file = os.path.join(os.path.dirname(res_target_file), 'signed_' + os.path.basename(res_target_file))
    sigthief_args = [
        '-i', source_file,
        '-t', res_target_file,
        '-o', signed_target_file
    ]
    run_with_wine(sigthief_path, sigthief_args)
    
    print(f"Resources copied from {source_file} to {res_target_file}")
    print(f"Signature copied from {source_file} to {signed_target_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 metatwin.py <source_file> <target_file>")
        sys.exit(1)

    source_file = sys.argv[1]
    target_file = sys.argv[2]

    resource_hacker_path = 'ResourceHacker.exe'
    sigthief_path = 'sigthief.exe'

    if not os.path.isfile(resource_hacker_path) or not os.path.isfile(sigthief_path):
        print("Resource Hacker or SigThief not found. Please ensure they are installed and in the system's PATH.")
        sys.exit(1)

    copy_metadata(source_file, target_file, resource_hacker_path, sigthief_path)
