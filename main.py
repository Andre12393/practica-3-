import flet as ft

def main(page: ft.Page):
 page.title="calculadora"
 page.vertical_alignment=ft.MainAxisAlignment.CENTER
 page.horizontal_alignment=ft.CrossAxisAlignment.CENTER

 txt1=ft.TextField(label="cuenta")
 txt2=ft.TextField(label="propina")
 res=ft.Text("")

 def boton(e):
  try:
   a=float(txt1.value)
   b=float(txt2.value)
   c=a*b/100
   d=a+c
   res.value="propina es "+str(c)+" total "+str(d)
  except:
   res.value="error pon numeros"
  page.update()

 btn=ft.ElevatedButton("calcular",on_click=boton)

 page.add(txt1,txt2,btn,res)

ft.run(main)