import datetime

def log_prompt(question, response):

    with open("prompt_logs.txt", "a") as f:

        f.write("\n\n")

        f.write(f"Time: {datetime.datetime.now()}\n")
        f.write(f"Question: {question}\n")
        f.write(f"Response: {response}\n")