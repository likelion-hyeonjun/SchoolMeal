from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import cafeteria
import json

# Create your views here.

cafeteria = cafeteria.Cafeteria(0,0,0)

def keyboard(request):
    return JsonResponse({
        'type': 'text'
    })

@csrf_exempt
def depart(request):
    global cafeteria
    waiting, eating = cafeteria.getValue()
    cafeteria.addWaiting()
    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['userRequest']['utterance']
    #if datacontent == '급식실 출발':
    return JsonResponse({
        'version': "2.0",
        'template': {
            'outputs': [
                {
                "basicCard": {
                    "title": "밥먹으로 출발~!😃",
                    'description': "현재 급식실 상황은 다음과 같습니다.\n\n"+"- "+str(waiting)+"명 대기중\n"+"- "+str(eating)+"명 식사중",
                    "thumbnail":{
                        "imageUrl":"https://i.esdrop.com/d/xoriGEmjHU.png"
                    },
                }
            }],
            'quickReplies': [{
                'label': '급식실 출발',
                'action': 'message',
                'messageText': '급식실 출발'
            },
            {
                'label': '배식 완료',
                'action': 'message',
                'messageText': '배식 완료'
            },
            {
                'label': '다 먹었다!',
                'action': 'message',
                'messageText': '다 먹었다!'
            },
            ]
        }
    })
 
# @csrf_exempt
# def Eating(request):


# @csrf_exempt
# def Finish(request):

@csrf_exempt
def initialize(request):
    global cafeteria
    cafeteria.initialize()
    answer = ((request.body).decode('utf-8'))
    return_json_str = json.loads(answer)
    return_str = return_json_str['userRequest']['utterance']

    if return_str == '초기화':
        return JsonResponse({
            'version': "2.0",
            'template': {
                'outputs': [{
                    'simpleText': {
                        'text': '기존 내용이 초기화 되었습니다.'
                    }
                }],
                'quickReplies': [{
                    'label': '급식실 출발',
                    'action': 'message',
                    'messageText': '급식실 출발'
                },
                {
                    'label': '배식 완료',
                    'action': 'message',
                    'messageText': '배식 완료'
                },
                {
                    'label': '다 먹었다!',
                    'action': 'message',
                    'messageText': '다 먹었다!'
                },
                ]
            }
        })
    
        
 

