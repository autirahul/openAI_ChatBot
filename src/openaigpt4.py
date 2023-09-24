import openai
from train_cypher import node_properties,relationships_props
from train_utils import schema_text,get_system_message


def get_graph_model_metadata():
    return schema_text(node_props=node_properties,rels=relationships_props)

def get_sys_prompts():
    schema_txt = get_graph_model_metadata()
    return get_system_message(schema_txt)

def generate_cypher(messages):
    messages = [
        {"role": "system", "content": get_sys_prompts()}
    ] + messages
    # Make a request to OpenAI
    completions = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=0.0
    )
    response = completions.choices[0].message.content

    return response