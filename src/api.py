import json
import traceback
from datetime import datetime, timezone
from predict import ModelPredict


def handler(event, context):
    if 'warmup' in event and event['warmup'] is True:
        predict = ModelPredict()
        print(f"WARMUP: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        return None
    else:
        try:
            # Input Request
            request = json.loads(json.dumps(event['body']))
            predict = predict = ModelPredict()
            
            # Process / Evaluate
            outputs = []
            start_time = datetime.now()
            for input in request['inputs']:
                value = predict.evaluate(input)
                outputs.append(value)
            end_time = datetime.now()

            # Output Response
            results = {
                "success": True,
                "message": "",
                "outputs": outputs,
                "metadata": {
                    "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                    "processing_time_ms": (end_time - start_time).total_seconds() * 1000
                }
            }
            response = {
                "statusCode": 200,
                "headers": {"Content-Type": "application/json"},
                "isBase64Encoded": False,
                "body": json.dumps(results)
            }
            print(json.dumps(response))
            return response 
    
        except Exception as e:
            # Error Handling
            print(f"EVENT:", end='\n')
            print(json.dumps(event), end='\n\n')
            print(f"ERROR:", end='\n')
            print(traceback.format_exc(), end='\n\n')

            # Server Error
            results = {
                "success": False,
                "message": "Internal server error",
                "outputs": [],
                "metadata": {
                    "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                    "processing_time_ms": 0
                }
            }
            response = {
                "statusCode": 500,
                "headers": {"Content-Type": "application/json"},
                "isBase64Encoded": False,
                "body": json.dumps(results)
            }
            print(json.dumps(response))
            return response
        
event = {
    "body": {
        "inputs": [{
            "sepal_length": 6.4,
            "sepal_width": 2.8,
            "petal_length": 5.6,
            "petal_width": 2.2
            }]
        }
    }   

handler(event=event, context=None)