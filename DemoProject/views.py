from django.http import HttpResponse       # Returns response
from django.shortcuts import render     # To render to a template ..


# def Homepage(request):      # Request response ..
#     return HttpResponse("Hello World....!!!!!!!! How are you ....")
#     # return HttpResponse("<h1>Hello World....!!!!!!!! How are you ....<h1>")



#  Rendering to a HTML Page ....



# def Homepage(request):      # Request response ..
#     my_html= """
#
#                 <!doctype html>
#                         <html lang="en">
#                           <head>
#                             <!-- Required meta tags -->
#                             <meta charset="utf-8">
#                             <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
#
#                             <!-- Bootstrap CSS -->
#                             <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.2/css/bootstrap.min.css" integrity="sha384-Smlep5jCw/wG7hdkwQ/Z5nLIefveQRIY9nfy6xoR1uRYBtpZgI6339F5dgvm/e9B" crossorigin="anonymous">
#
#                             <title>Hello, world!</title>
#                           </head>
#                           <body>
#
#
#
#                             <h1 class = "text-center">Hello, world!</h1>
#
#                                 <div class="jumbotron">
#                                       <h1 class="display-4">Hello, world!</h1>
#                                       <p class="lead">This is a simple hero unit, a simple jumbotron-style component for calling extra attention to featured content or information.</p>
#                                       <hr class="my-4">
#                                       <p>It uses utility classes for typography and spacing to space content out within the larger container.</p>
#                                       <a class="btn btn-primary btn-lg" href="#" role="button">Learn more</a>
#                                     </div>
#                                                                 <!-- Optional JavaScript -->
#                             <!-- jQuery first, then Popper.js, then Bootstrap JS -->
#                             <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
#                             <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
#                             <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.2/js/bootstrap.min.js" integrity="sha384-o+RDsa0aLu++PJvFqy8fFScvbHFLtbvScb8AjopnFD+iEQ7wo/CG0xlczd+2O/em" crossorigin="anonymous"></script>
#                         </body>
#                 </html>
#
#
#     """
#     return HttpResponse(my_html)








def Homepage(request):      # Request response ..
    context = {
        "title":"We Welcomes You to our Web Live session..",
        "Name": "Mukesh Dubey"
    }

    return render(request, "homeview.html" , context)

def ContactPage(request):      # Request response ..
    return render(request, "homeview.html" , {})

def SamplePage(request):      # Request response ..
    return render(request, "homeview.html" , {})

