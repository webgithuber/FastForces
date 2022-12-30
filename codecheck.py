import subprocess
from problem.models import TestCase

def match(out,correct_out):
    verdict=""
    if len(correct_out)<len(out):
        correct_out+="\n"
    print(len(correct_out))
    print(len(out))
    if correct_out==(out):   
        verdict = "Accepted"
    elif len(correct_out)==len(out):
        verdict = "Wrong answer"
    else:
        verdict = "Compilation error"
    return verdict


class CodeCheck():
    def __init__(self, lang,TestCase, code=None ):
        self.code = code
        self.lang=lang
        self.stderr = None
        file_in = open("\home\ubuntu\project2\FastForces\static\code\input.txt","w")
        correct_out = open("\home\ubuntu\project2\FastForces\static\code\correct_out.txt","w")
        
        for element in TestCase.input:
            element = element.strip('\n')
            file_in.write(element)
        file_in.close()
        
        for element in TestCase.output:
            element = element.strip('\n')
            correct_out.write(element)
        correct_out.close()

    def run_cpp(self):

        file_out = open("\home\ubuntu\project2\FastForces\static\code\output.txt","w")
        file_in = open("\home\ubuntu\project2\FastForces\static\code\input.txt", "r")
        code_file = open("\home\ubuntu\project2\FastForces\static\code\code.cpp", "w")
        code_file.write(self.code)
        code_file.close()
        
        subprocess.run(["g++", "\home\ubuntu\project2\FastForces\static\code\code.cpp","-o", "output"],shell=True)
        subprocess.run([".\output.exe"], stdin=file_in, stdout=file_out,shell=True)
        
        file_out.close()
        file_in.close()

        file_out = open("\home\ubuntu\project2\FastForces\static\code\output.txt", "r")
        correct_out = open("\home\ubuntu\project2\FastForces\static\code\correct_out.txt", "r")
        
        out = file_out.read()
        correct_out = correct_out.read()
        

        return match(out,correct_out)

    def run_python(self):
        file_out = open("\home\ubuntu\project2\FastForces\static\code\output.txt","w")
        file_in = open("\home\ubuntu\project2\FastForces\static\code\input.txt", "r")
        code_file = open("\home\ubuntu\project2\FastForces\static\code\code.py", "w")
        code_file.write(self.code)
        code_file.close()
        
        subprocess.run(["python" , "\home\ubuntu\project2\FastForces\static\code\code.py"], stdin=file_in, stdout=file_out, shell=True)
        file_out.close()
        file_in.close()

        file_out = open("\home\ubuntu\project2\FastForces\static\code\output.txt", "r")
        correct_out = open("\home\ubuntu\project2\FastForces\static\code\correct_out.txt", "r")
        
        out = file_out.read()
        correct_out = correct_out.read()
        

        return match(out,correct_out)
    def run_java(self):
        file_out = open("\home\ubuntu\project2\FastForces\static\code\output.txt","w")
        file_in = open("\home\ubuntu\project2\FastForces\static\code\input.txt", "r")
        code_file = open("\home\ubuntu\project2\FastForces\static\code\code.java", "w")
        code_file.write(self.code)
        code_file.close()

        subprocess.run(["javac" , "\home\ubuntu\project2\FastForces\static\code\Code.java"], shell=True)
        subprocess.run(["java" , "\home\ubuntu\project2\FastForces\static\code\Code"], stdin=file_in, stdout=file_out, shell=True)
        file_out.close()
        file_in.close()

        file_out = open("\home\ubuntu\project2\FastForces\static\code\output.txt", "r")
        correct_out = open("\home\ubuntu\project2\FastForces\static\code\correct_out.txt", "r")
        
        out = file_out.read()
        correct_out = correct_out.read()
        
        return match(out,correct_out)


    def run_code(self):
        if self.lang=='C++':
            return self.run_cpp()
        elif self.lang=='Python':
            return self.run_python()
        else:
            return self.run_java()
        