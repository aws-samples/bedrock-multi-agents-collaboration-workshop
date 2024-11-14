import json
import random

PEAK_LIST = ['fridge','bathtub','iron','dry-machine','car charger socket','light bulbs','gardening electrical system']

def get_named_parameter(event, name):
    return next(item for item in event['parameters'] if item['name'] == name)['value']
    
def populate_function_response(event, response_body):
    return {'response': {'actionGroup': event['actionGroup'], 'function': event['function'],
                'functionResponse': {'responseBody': {'TEXT': {'body': str(response_body)}}}}}

def get_consumption_info(customer_id):
    # TODO: Implement real business logic

    return [
        {
         "monthly_avg": "150kw",
         "monthly_p90": "140kw",
         "monthly_max": "440kw",
         "monthly_mix": "90kw",
         "peak_load_day": "55kw",
         "price_per_kw": '%.2f'%(random.uniform(1.0, 20.0)),
         "peak_item": PEAK_LIST[random.randint(0, 6)]
        }
    ]

def lambda_handler(event, context):
    print(event)
    
    # name of the function that should be invoked
    function = event.get('function', '')

    # parameters to invoke function with
    parameters = event.get('parameters', [])
    
    if function == 'get_consumption_info':
        customer_id = get_named_parameter(event, "customer_id")
        result = get_consumption_info(customer_id)
    else:
        result = f"Error, function '{function}' not recognized"

    response = populate_function_response(event, result)
    print(response)
    return response