from subprocess import run
import time  

result = run(["ip","a"],capture_output=True, text=True)
line = result.stdout.split("\n")
print ("Resultat:\n",line[4])
print ("Resultat:\n",result.returncode)
print ("Resultat:\n",result.stderr)