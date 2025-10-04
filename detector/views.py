from django.shortcuts import render
from .ml_utils import models
from django.contrib.auth.decorators import login_required

from .models import MessageLog

def classify_message(request):
    all_predictions = {}
    if request.method == "POST":
        message = request.POST.get("message")
        for name, clf in models.items():
            try:
                pred = clf.predict([message])
                # Convert numpy.int64 → Python int
                if hasattr(pred, "item"):   
                    pred = pred.item()
            except Exception as e:
                pred = f"Error: {str(e)}"
            all_predictions[name] = pred

        # Save to DB (only pure Python types now)
        MessageLog.objects.create(message=message, predictions=all_predictions)

    return render(request, "detector/classify.html", {"all_predictions": all_predictions})


from django.shortcuts import render
from .models import MessageLog

from django.core.paginator import Paginator
from django.shortcuts import render
from .models import MessageLog

@login_required
def dashboard(request):
    filter_type = request.GET.get("filter")  # "ham", "spam", or empty
    model_name = request.GET.get("model")    # specific model filter
    search_query = request.GET.get("search", "").strip()  # keyword search

    logs = MessageLog.objects.all().order_by("-created_at")  # latest first

    # Filter by keyword in message
    if search_query:
        logs = logs.filter(message__icontains=search_query)

    # Filter by Ham/Spam
    if filter_type:
        filtered_logs = []
        for log in logs:
            predictions = log.predictions
            if model_name:
                if predictions.get(model_name) == filter_type:
                    filtered_logs.append(log)
            else:
                if filter_type in predictions.values():
                    filtered_logs.append(log)
        logs = filtered_logs

    # Pagination: 10 logs per page
    paginator = Paginator(logs, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "logs": page_obj,
        "page_obj": page_obj,
        "models": list(MessageLog.objects.first().predictions.keys()) if logs else [],
        "filter_type": filter_type,
        "model_name": model_name,
        "search_query": search_query,
    }
    return render(request, "detector/dashboard.html", context)
