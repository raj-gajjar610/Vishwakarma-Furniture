# from django.shortcuts import render, redirect
# from myapp.models import *
#
#
# # 🔐 ADMIN LOGIN
# def admin_login(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#
#         user = User.objects.filter(
#             email=email,
#             password=password,
#         ).first()
#
#         if user:
#             request.session['admin'] = user.id
#             return redirect('dashboard.htm')  # ✅ FIXED
#     return render(request, 'wlogin.html')
#
#
# # 📊 DASHBOARD
# def admin_dashboard(request):
#     if not request.session.get('admin'):
#         return redirect('/admin-login/')
#
#     return render(request, 'dashboard.html')
#
#
# # 📦 PRODUCT LIST
# def admin_product(request):
#     if not request.session.get('admin'):
#         return redirect('/admin-login/')
#
#     products = Subcategory.objects.all()
#
#     return render(request, 'admin/product.html', {
#         'products': products
#     })
#
#
# # ➕ ADD PRODUCT
# def add_product(request):
#     if request.method == 'POST':
#         name = request.POST['name']
#         price = request.POST['price']
#         detail = request.POST['detail']
#
#         Subcategory.objects.create(
#             s_name=name,
#             price=price,
#             detail=detail
#         )
#
#         return redirect('/admin-product/')
#
#     return render(request, 'admin/add_product.html')
#
#
# # ❌ DELETE PRODUCT
# def delete_product(request, id):
#     Subcategory.objects.filter(s_id=id).delete()
#     return redirect('/admin-product/')
