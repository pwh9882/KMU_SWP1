html = """
<html>
    <head>
        <title>calc from 20203070</title>
        <style>
            .True {
                visibility: visible;
            }
            .False {
                visibility: hidden;
            }
        </style>
    </head>
    <body>
        made by 20203070 Woohyeok-Park <br><br>

        <form action="">
            a: <input type="number" name="a" /> b: <input type="number" name="b" />
            <input type="submit" value="submit" />
        </form>

        printing a + b and  a * b <br><br>

        <div class="%(result)s">
        a + b = %(sum)d <br><br>
        a * b = %(mul)d
        <div>
        
    </body>
</html>
"""
