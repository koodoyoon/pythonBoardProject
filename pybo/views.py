from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotAllowed
from django.utils import timezone
from .models import Question
from .forms import QuestionForm, AnswerForm
import logging


# menu
def boot_menu(requset):
    # 개발에 사용되는 임시 메뉴
    return render(requset, 'pybo/menu.html')


def question_create(request):
    ''' 질문 등록 '''
    print('request.method = {}'.format(request.method))
    if request.method == 'POST':
        logging.info('question_create post')
        # 저장
        form = QuestionForm(request.POST)  # request.POST 데이터 (subject, content 자동 생성)

        if form.is_valid():  # form(질문등록)이 유용하면
            question = form.save(commit=False)  # subject, content 만 저장(commit은 하지 않음)
            question.create_date = timezone.now()
            question.save()  # 날짜 까지 생성해서 저장(commit)
            return redirect('pybo:index')
    else:
        form = QuestionForm()
    context = {'form': form}
    return render(request, 'pybo/question_form.html', {'form': form})


# register
def boot_reg(request):
    return render(request, 'pybo/reg.html')


# bootstrap list
def boot_list(request):
    ''' bootstrap template '''

    return render(request, 'pybo/list.html')


def answer_create(request, question_id):
    ''' 답변 등록 '''
    question = get_object_or_404(Question, pk=question_id)

    if request.method == 'POST':
        form = AnswerForm(request.POST)

        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('pybo:detail', question_id=question_id)
    else:
        return HttpResponseNotAllowed('Post만 가능 합니다.')

    # form validation
    context = {'question': question, 'form': form}
    return render(request, 'pybo/question_detail.html', context)


def detail(request, question_id):
    ''' question 상세 '''
    # print(question_id)
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    logging.info(question)
    context = {'question': question}
    logging.info(context)
    return render(request, 'pybo/question_detail.html', context)


# Create your views here.
def index(request):
    ''' question 목록 '''
    logging.info('index 레벨로 출력')
    # print('index 레벨로 출력')
    question_list = Question.objects.order_by('create_date')  # order by 에 -가 붙으면 desc, 안붙으면 asc
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)
