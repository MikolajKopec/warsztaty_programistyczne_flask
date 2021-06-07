def render_template(file_path,**template_args):
    print(template_args)
    with open(file_path,"r") as s:
        print(s.read().format(**template_args))
        

render_template("./tekst.txt",username="miki")