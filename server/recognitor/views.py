from django.shortcuts import render, redirect
import os
from django.conf import settings

from .forms import AudioUploadForm
from .models import AudioUploadFile

from .live_prediction import LivePredictions


# Create your views here.
def index(request):
    uploaded_file = AudioUploadFile.objects.last()
    if request.method == 'POST':
        print(request.FILES)
        form = AudioUploadForm(request.POST, request.FILES)

        # Get upload image name
        file = request.FILES['audioFile']
        # Get upload image path
        path = settings.MEDIA_ROOT + "/audio_files/" + file.name
        print(path)
        ser_model_path = os.path.join(settings.BASE_DIR, 'SER_model.h5')
        prediction = LivePredictions(path=ser_model_path, file=path)
        prediction.load_model()

        if form.is_valid():
            form.save()
            uploaded_file = AudioUploadFile.objects.last()
            uploaded_file.textOutput = prediction.make_predictions()
            uploaded_file.save()
            return redirect('index')
    else:
        form = AudioUploadForm()
    return render(request, 'index.html', {
        'form': form,
        'uploaded_file': uploaded_file
    })
