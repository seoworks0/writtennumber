import base64
import os
from io import BytesIO
from django.shortcuts import render
from django.views import generic
from .forms import FileForm,TextForm,NameForm
#from .lib import predict
from .mnist_predict import predict
from .mnist_predict_strong import predict_strong
import numpy as np
from PIL import Image

class HomeView(generic.FormView):
    template_name = 'mnist/home.html'
    form_class = NameForm

    def form_valid(self, form):
        # アップロードファイル本体を取得
        #name = request.POST['name']
        name = form.cleaned_data['name']
        """f = open('mnist/templates/mnist/home.html', 'w')
        name2 = '{% extends "mnist/base.html" %}{% block content %}<form action="" method="POST" enctype="multipart/form-data">{{ form.name }}<hr>{% csrf_token %}<input type="submit" class="btn btn-outline-primary btn-lg" value="送信する"></form>{% block name %}' + name + '{% endblock %}{% endblock %}'
        f.writelines(name2)
        f.close()"""
        return render(self.request, 'mnist/name.html',{'name': name,})

class UploadView(generic.FormView):
    template_name = 'mnist/upload.html'
    form_class = FileForm

    def form_valid(self, form):
        # アップロードファイル本体を取得
        file = form.cleaned_data['file']
        fn = file.name
        # ファイルのサイズを計算
        file_size = os.path.getsize(fn)
        if file_size < 5000:
            open('a.txt','w')
        else:
            open('b.txt','w')

        return render(self.request, 'mnist/read_done.html')

class PaintView(generic.TemplateView):
    template_name = 'mnist/paint.html'
    a = np.random.rand(784)
    a = np.array([a])
    b = predict(a)
    c = predict_strong(a)

    def post(self, request):
        base_64_string = request.POST['img-src'].replace(
            'data:image/png;base64,', '')
        file = BytesIO(base64.b64decode(base_64_string))

        # ファイルを、28*28にリサイズし、グレースケール(モノクロ画像)
        img = Image.open(file).resize((28, 28)).convert('L')

        # 学習時と同じ形に画像データを変換する
        img_array = np.asarray(img) / 255
        img_array = img_array.reshape(1, 784)

        #aのみがあればweakのみ、aもbもあればweak,strong共に表示
        if os.path.isfile('a.txt')==True and os.path.isfile('b.txt')==False:
            result = predict(img_array)
        elif os.path.isfile('a.txt')==True and os.path.isfile('b.txt')==True:
            result = 'weak|' + str(predict(img_array)) + 'strong|' + str(predict_strong(img_array))

        # 推論した結果を、テンプレートへ渡して表示
        context = {
            'result': result,
        }
        return render(self.request, 'mnist/result_paint.html', context)

class CalcView(generic.TemplateView):
    template_name = 'mnist/calc.html'
    form = TextForm
    a = np.random.rand(784)
    a = np.array([a])
    b = predict(a)
    c = predict_strong(a)

    def post(self, request):
        formula = request.POST['formula']
        formula.replace(" ","").replace("　","")

        print(formula)
        base_64_string = request.POST['img-src'].replace(
            'data:image/png;base64,', '')
        file = BytesIO(base64.b64decode(base_64_string))

        # ファイルを、28*28にリサイズし、グレースケール(モノクロ画像)
        img = Image.open(file).resize((28, 28)).convert('L')

        base_64_string2 = request.POST['img-src2'].replace(
            'data:image/png;base64,', '')
        file = BytesIO(base64.b64decode(base_64_string2))
        img2 = Image.open(file).resize((28, 28)).convert('L')

        # 学習時と同じ形に画像データを変換する
        img_array = np.asarray(img) / 255
        img_array = img_array.reshape(1, 784)
        img_array2 = np.asarray(img2) / 255
        img_array2 = img_array2.reshape(1, 784)

        #aのみがあればweakのみ、aもbもあればweak,strong共に表示
        if os.path.isfile('a.txt')==True and os.path.isfile('b.txt')==False:
            result = predict(img_array)
            result2 = predict(img_array2)
            num1 = int(result)
            num2 = int(result2)
        elif os.path.isfile('a.txt')==True and os.path.isfile('b.txt')==True:
            num1 = int(predict_strong(img_array))
            num2 = int(predict_strong(img_array2))
            result = 'weak|' + str(predict(img_array)) + 'strong|' + str(predict_strong(img_array))
            result2 = 'weak|' + str(predict(img_array2)) + 'strong|' + str(predict_strong(img_array2))

        try:
            answer = eval(formula)
            # 推論した結果を、テンプレートへ渡して表示
            context = {
                'result': result,
                'result2':result2,
                'answer':answer,
            }
            return render(self.request, 'mnist/result.html', context)
        except:
            return render(self.request, 'mistake.html')
