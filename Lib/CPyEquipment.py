import subprocess, sys


class CPyEquipment:
    def __init__(self, params):
        self.params = params

    def cat_command(self, cmd):
        try:
            with open(cmd, "r") as f:
                content = f.read()
            return content
        except Exception as ex:
            print(ex)

    def shell_command(self, cmd):
        try:
            sc = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
            output = sc.communicate()
            return output
        except Exception as ex:
            print(ex)

    def test(self):
        for x in range(10, 110):
            p = subprocess.Popen(self.params + str(x), shell=True, stderr=subprocess.PIPE)
            while True:
                out = p.stderr.read(1)
                if out == '' and p.poll() is None:
                    break
                if out != '':
                    sys.stdout.write(out)
                    sys.stdout.flush()