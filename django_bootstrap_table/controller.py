import logging

from django.shortcuts import render

logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s %(name)s %(levelname)s func:[%(funcName)s] %(message)s',
                    datefmt='%Y-%m-%d %I:%M:%S')
logger = logging.getLogger(__name__)


def index(request):
    logger.info("index")
    # return HttpResponse("index controller")
    return render(request, "manage.html")
