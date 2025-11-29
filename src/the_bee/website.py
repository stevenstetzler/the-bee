header = """
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>NYT Bee Answers</title>
<style>
body {
  margin: 0;
  position: relative;
  min-height: 100vh;
}

body::before {
  content: "";
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;

  background-image: url("bee.jpg");
  background-size: 200px;     /* adjust tile size */
  background-repeat: repeat;

  opacity: 0.35;               /* alpha fade */
  pointer-events: none;       /* background only */
  z-index: -1;                /* behind everything */
}  

.content {
  max-width: 800px;     /* keeps text readable */
  margin: 50px auto;    /* <-- margin around your content */
  padding: 20px;        /* internal spacing */
  background: rgba(255, 255, 255, 0.85);  /* optional for readability */
  border-radius: 12px;  /* looks clean */
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2); /* optional */
}

</style>  
</head>

<body>

<div class='content'>
"""

footer = """

<p>
Image credit: "Lys jordhumle (Bombus lucorum)" by Arnstein Staverløkk, Norsk institutt for naturforskning, licensed under CC BY 3.0.
</p>
<p>
<a href="https://artsdatabanken.no/Pages/149643/Lys_jordhumle">https://artsdatabanken.no/Pages/149643/Lys_jordhumle</a>
</p>
<p>
<a href="https://creativecommons.org/licenses/by/3.0/">https://creativecommons.org/licenses/by/3.0/</a>
</p>

</div>
<footer>
<script>
</script>
</footer>
</body>
</html>
"""

def main():
    from subprocess import Popen, PIPE
    print(header)
    p = Popen("the-bee-answers today", shell=True, stdout=PIPE)
    p2 = Popen("the-bee-format-answers", shell=True, stdin=p.stdout, stdout=PIPE)
    p.stdout.close()
    output, err = p2.communicate()
    print(output.decode())
    # print(os.system("the-bee-answers today | the-bee-format-answers"))
    print(footer)

if __name__ == "__main__":
    main()