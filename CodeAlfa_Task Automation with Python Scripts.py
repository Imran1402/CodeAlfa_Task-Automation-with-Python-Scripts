import re

def extract_emails(input_file, output_file):
    try:
        with open(input_file, 'r') as f:
            content = f.read()

        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails = re.findall(email_pattern, content)
        unique_emails = sorted(set(emails))

        with open(output_file, 'w') as f:
            for email in unique_emails:
                f.write(email + '\n')

        print(f"✅ Successfully extracted {len(unique_emails)} emails to '{output_file}'.")

    except FileNotFoundError:
        print("❌ Input file not found.")
    except Exception as e:
        print("❌ An error occurred:", e)

# Example Usage
input_file = 'sample_input.txt'         # Ensure this file exists in your directory
output_file = 'extracted_emails.txt'

extract_emails(input_file, output_file)
