from django.shortcuts import render


def index(request):
    context = {
        "latest_question_list": [1, 2, 3],
    }
    return render(request, "tanshin/index.html", context)
