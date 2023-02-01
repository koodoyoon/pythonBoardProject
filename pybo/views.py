from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone
from .models import Question
from .forms import QuestionForm


# menu
def boot_menu(requset):
    # 개발에 사용되는 임시 메뉴
    return render(requset, 'pybo/menu.html')


def question_create(request):
    ''' 질문 등록 '''
    print('request.method = {}'.format(request.method))
    if request.method == 'POST':
        print('question_create post')
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
    question = get_object_or_404(Question, pk=question_id)
    # Question 과 Answer 처럼 서로 연결되어 있는 경우
    # 연결 모델명_set 연결데이터를 조회 할 수 있다.
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('pybo:detail', question_id=question_id)


def detail(request, question_id):
    ''' question 상세 '''
    # print(question_id)
    # question = Question.objects.get(id=question_id)
    question = get_object_or_404(Question, pk=question_id)
    print(question)
    context = {'question': question}
    print(context)
    return render(request, 'pybo/question_detail.html', context)


# Create your views here.
def index(request):
    ''' question 목록 '''
    question_list = Question.objects.order_by('create_date')  # order by 에 -가 붙으면 desc, 안붙으면 asc
    context = {'question_list': question_list}
    return render(request, 'pybo/question_list.html', context)
