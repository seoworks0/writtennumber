import base64
import os
from io import BytesIO
from django.shortcuts import render
from django.views import generic
from .forms import FileForm
#from .lib import predict
from .mnist_predict import predict
from .mnist_predict_strong import predict_strong
import numpy as np
from PIL import Image



class UploadView(generic.FormView):
    template_name = 'mnist/upload.html'
    form_class = FileForm

    def form_valid(self, form):
        # アップロードファイル本体を取得
        file = form.cleaned_data['file']
        fn = file.name
        # ファイルのサイズを計算
        file_size = os.path.getsize(fn)
        if file_size < 50000:
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
        return render(self.request, 'mnist/result.html', context)
