# Com REPORTLAB
import io
from django.http import FileResponse
from django.views.generic import View
from reportlab.pdfgen import canvas

# Com WEASY PRINT
from django.core.files.storage import FileSystemStorage
from django.template.loader import render_to_string
from weasyprint import HTML
from django.http import HttpResponse


# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        # Cria arquivo para receber os dados e gerar o pdf
        buffer = io.BytesIO()  # cria arquivo temporário no disco

        # Criando o arquivo pdf
        pdf = canvas.Canvas(buffer)

        # Insere data no pdf
        pdf.drawString(100, 100, "Jesus Cristo, meu pai e Salvador!")

        # Quando finalizar inserção de data no pdf
        pdf.showPage()
        pdf.save()

        # Por fim, retornar buffer pro início do arquivo
        buffer.seek(0)

        # Faz o download do pdf gerado
        # return FileResponse(buffer, as_attachment=True, filename='relatorio1.pdf')

        # Abre o pdf direto no navegador
        return FileResponse(buffer, filename='relatorio1.pdf')


class IndexView2(View):
    def get(self, request, *args, **kwargs):
        texto = [
            'Jesus',
            'Python',
            'Curso',
            'Prosperidade',
            'Riqueza'
        ]

        # Renderizando conteúdo do template 'relatorio.html'
        html_string = render_to_string('relatorio.html', {'texto': texto})

        # Instanciado classe HTML criando objeto
        html = HTML(string=html_string)

        # Escreve o pdf no diretório '/tmp/'
        html.write_pdf(target='/tmp/relatorio2.pdf')

        # Usado pelo django que permite escrever no disco
        fs = FileSystemStorage('/tmp')

        with fs.open('relatorio2.pdf') as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')

            # Faz o download do pdf direto
            # response['Content-Disposition'] = 'attachment; filename="relatorio2.pdf"'

            # Abre o pdf direto no navegador
            response['Content-Disposition'] = 'inline; filename="relatorio2.pdf"'

        return response
