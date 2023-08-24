from django.shortcuts import render , redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.

def index(request): 
    articles = Article.objects.all()

    context = {
        'articles': articles,
    }

    return render(request, 'index.html', context)


def detail(request, id): 
    article = Article.objects.get(id=id)

    context = {
        'article': article,

    }
    return render(request, 'detail.html', context)

def create(request): 
    # 모든 경우의 수를 찾는다
    # 1. 기본값 GET : From만들어 html문서를 사용자에게 리턴
    # 2. POST : invalid data 데이터 검증에 실패한경우 (빈공간 등)
    #           -> 검증 성공한 일부데이터만 살린채, Form만들어 html문서를 사용자에게 리턴 
    # 3. POST : valid data 데이터 검증에 성공한 경우 
    #           -> DB에 데이터 저장 후, detail로 redirect 

    # ------------------------------------------

    # 5. POST 요청일 때 (데이터 잘못 들어온경우)
    # 10.POST 요청일 때 (데이터가 잘~들어온경우)
    if request.method == 'POST': 
        # 6. Form에 사용자가 입력한 올바르지않은 정보를 담아, Form생성 
        # 11. Form에 사용자가 입력한 올바른 정보를 담아, Form생성 
        form = ArticleForm(request.POST)

        # 7. Form을 검증함 (검증에 실패해서 False)
        # 12. Form을 건증  (검증에 성공해서 True)
        if form.is_valid(): 
            # 13. Form을 저장하고, 그 결과를 article변수에 저장 
            article = form.save() 
            # 14. detail.html로 redirct 
            return redirect('articles:detail', id= article.id)
        else: 
            pass

    # 1. GET 요청일 때, 
    else: 
        # 2. 비어있는 Form을 만든다. 
        form = ArticleForm()
    # 3. context dict에 담는다. 
    # 8. 검증에 실패한 Form을 context dict에 담는다. 
    context = {
        'form' : form,
    }
    # 4. create.html을 보여준다. (랜더링)
    # 9. create.html을 보여준다. (랜더링)
    return render(request,'create.html', context)