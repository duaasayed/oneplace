from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .forms import AddApplicationForm
from django.views.decorators.http import require_http_methods
from pprint import pprint
from .models import Application
from django.core import serializers
import json
import io
import xlsxwriter



def show(request):
    statistics = []
    statistics.append(Application.objects.filter(status=0).count())
    statistics.append(Application.objects.filter(status=1).count())
    statistics.append(Application.objects.filter(status=2).count())
    statistics.append(Application.objects.filter(status=3).count())
    statistics.append(Application.objects.filter(status=4).count())
    statistics.append(Application.objects.filter(status=5).count())

    return render(request, 'report/show.html', {'statistics': statistics})


def report_data(request):
    applications = request.user.application_set.all()

    #pprint(applications)
    response = serializers.serialize('json', applications)
    response = json.loads(response)
    return JsonResponse(response, safe=False)


@require_http_methods(["GET", "POST"])
def add_application(request):
    if request.method == 'POST':
        form = AddApplicationForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            
            request.user.application_set.create(
                title=data['title'],
                company=data['company'],
                medium=data['medium'],
                link=data['link'],
                job_type=data['job_type'],
                experience_level=data['level'],                
                posted_at=data['posted_at'],
                applied_at=data['applied_at'],
                status=0
            )

            return redirect('/report')

    else:
        form = AddApplicationForm()

    return render(request, 'report/add_application.html', {'form': form})


def change_status(request, pk):
    application = Application.objects.filter(pk=pk)
    application.update(status=request.POST['status'])

    return JsonResponse({'status': 200})



def export(request):
    output = io.BytesIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()

    columns = ['#', 'Title', 'Company', 'Medium', 'Job Type', 'Experience Level',
    'Posted at', 'Applied at', 'Status']

    bold = workbook.add_format({'bold': True})

    for col_num in range(len(columns)):
        worksheet.write(0, col_num, columns[col_num], bold)

    data = request.user.application_set.all().values_list('id', 'title', 'company', 'medium', 'job_type', 'experience_level',
    'posted_at', 'applied_at', 'status', 'link')

    statuses = [
        ['No Response', '#808080'], 
        ['Viewed', '#800080'],
        ['Contacted', '#FF6600'],
        ['Interviewed', '#0000FF'],
        ['Accepted', '#008000'],
        ['Rejected', '#FF0000']
    ]
    
    row_num = 1

    for row in data:
        for col_num in range(len(columns)):
            if col_num == 1:
                cell_format = workbook.add_format({'font_color': 'blue'})
                worksheet.write_url(row_num, col_num, row[9], cell_format, string=row[col_num])
            elif col_num in [6,7]:
                cell_format = workbook.add_format({'num_format': 'mmm d yyyy'})
                worksheet.write(row_num, col_num, row[col_num], cell_format)
            elif col_num == 8:
                status = statuses[row[col_num]][0]
                cell_format = workbook.add_format({'bold': True, 'font_color': '#FFFFFF', 'bg_color': statuses[row[col_num]][1]})
                worksheet.write(row_num, col_num, status, cell_format)
            else:
                worksheet.write(row_num, col_num, row[col_num])
        row_num += 1


    worksheet.autofit()

    workbook.close()

    output.seek(0)

    filename = 'report.xlsx'
    response = HttpResponse(
        output,
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=%s' % filename

    return response
