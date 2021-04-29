from datetime import datetime
from .constants import socialNetworksListConstant, startDateConstant

# The getValuesFromRequest is handling the process of getting data from the inputs of the POST request
# and returning them in an array/list
def getValuesFromRequest(request):
    title = request.POST.get('titleContains')
    content = request.POST.get('contentContains')
    socialNetworks = socialNetworksListConstant if request.POST.get('socialNetwork') == '' else [request.POST.get('socialNetwork')]
    startDate = startDateConstant if request.POST.get('startDate') == '' else request.POST.get('startDate')
    endDate = datetime.now() if request.POST.get('endDate') == '' else request.POST.get('endDate')
    authorsList = request.POST.getlist('authorsList')

    return [title, content, socialNetworks, startDate, endDate, authorsList]
