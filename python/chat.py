# from openai import OpenAI
# import requests

# url = 'https://api.openai.com/v1/chat/completions'

# # Set up the headers with your API key
# headers = {
#     'Authorization': f'Bearer {apikey}',
#     'Content-Type': 'application/json',
# }

# # Define your request payload
# data = {
#     "model": "gpt-4o-mini",  # You can also use "gpt-4" if you have access
#     "messages": [
#         {"role": "user", "content": "Hello! How can I use the OpenAI API?"}
#     ],
#     "max_tokens": 100  # You can adjust the response length
# }

# # Send a POST request to the API
# response = requests.post(url, headers=headers, json=data)

# # Check the response
# if response.status_code == 200:
#     output = response.json()
#     print(output['choices'][0]['message']['content'])
# else:
#     print(f"Error: {response.status_code}, {response.text}")

# # import openai
# # import time
# # client = openai.OpenAI()


# # def get_response(prompt):
# #     while True:
# #         try:
# #             response = client.chat.completions.create(
# #                 model="gpt-3.5-turbo",
# #                 messages=[{"role": "user", "content": prompt}],
# #                 max_tokens=100
# #             )
# #             return response['choices'][0]['message']['content']
# #         except openai.error.RateLimitError as e:
# #             print("Rate limit exceeded. Waiting before retrying...")
# #             time.sleep(10)  # Wait for 10 seconds before retrying
# #         except Exception as e:
# #             print(f"An error occurred: {e}")
# #             break

# # # Example usage
# # user_input = "Hello! How can I use the OpenAI API?"
# # output = get_response(user_input)
# # print(output)
# from openai import OpenAI

# # Replace with your actual OpenAI API key

# client = OpenAI(api_key=api_key)

# response = client.chat.completions.create(
#     messages=[{
#         "role": "user",
#         "content": "Say this is a test",
#     }],
#     model="gpt-4o-mini",  # Make sure this is a valid model name
# )

# print(response._request_id)

from openai import OpenAI

client = OpenAI(api_key=api_key)

stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "Say this is a test"}],
    stream=True,
)
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")



import copy

def _deepcopy_method(x, memo): # Copy instance methods
    return type(x)(x.__func__, deepcopy(x.__self__, memo))



def _reconstruct(x, memo, func, args,
                 state=None, listiter=None, dictiter=None,
                 deepcopy=deepcopy):
    deep = memo is not None
    if deep and args:
        args = (deepcopy(arg, memo) for arg in args)
    y = func(*args)
    if deep:
        memo[id(x)] = y

    if state is not None:
        if deep:
            state = deepcopy(state, memo)
        if hasattr(y, '__setstate__'):
            y.__setstate__(state)
        else:
            if isinstance(state, tuple) and len(state) == 2:
                state, slotstate = state
            else:
                slotstate = None
            if state is not None:
                y.__dict__.update(state)
            if slotstate is not None:
                for key, value in slotstate.items():
                    setattr(y, key, value)

    if listiter is not None:
        if deep:
            for item in listiter:
                item = deepcopy(item, memo)
                y.append(item)
        else:
            for item in listiter:
                y.append(item)
    if dictiter is not None:
        if deep:
            for key, value in dictiter:
                key = deepcopy(key, memo)
                value = deepcopy(value, memo)
                y[key] = value
        else:
            for key, value in dictiter:
                y[key] = value
    return y

_deepcopy_dispatch = d = {}

def _deepcopy_atomic(x, memo):
    return x


dispatch_table = {}


def deepcopy(x, memo=None, _nil=[]):
    if memo is None:
        memo = {}

    d = id(x)
    y = memo.get(d, _nil)
    if y is not _nil:
        return y

    cls = type(x)

    copier = _deepcopy_dispatch.get(cls)
    if copier is not None:
        y = copier(x, memo)
    else:
        if issubclass(cls, type):
            y = _deepcopy_atomic(x, memo)
        else:
            copier = getattr(x, "__deepcopy__", None)
            if copier is not None:
                y = copier(memo)
            else:
                reductor = dispatch_table.get(cls)
                if reductor:
                    rv = reductor(x)
                else:
                    reductor = getattr(x, "__reduce_ex__", None)
                    if reductor is not None:
                        rv = reductor(4)
                    else:
                        reductor = getattr(x, "__reduce__", None)
                        if reductor:
                            rv = reductor()
                if isinstance(rv, str):
                    y = x
                else:
                    y = _reconstruct(x, memo, *rv)

    if y is not x:
        memo[d] = y
        _keep_alive(x, memo)
    return y