import json
import openai

# Read the configuration from the JSON file
with open("OAI_CONFIG_LIST_B", "r") as config_file:
    config_data = json.load(config_file)

# Specify the model name you want to use
desired_model_name = "gpt-3.5-turbo"

# Find the API key associated with the desired model name
api_key = None
for model_config in config_data:
    if model_config["model"] == desired_model_name:
        api_key = model_config["api_key"]
        break

if api_key:
    # Set the API key for the OpenAI Python client
    openai.api_key = api_key

    # Make the API call using the specified model
    completion = openai.ChatCompletion.create(
      model=desired_model_name,
      messages=[
        {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
        {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
      ]
    )

    print(completion.choices[0].message)
else:
    print(f"No API key found for model: {desired_model_name}")