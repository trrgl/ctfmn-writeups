# We Will Rock You

Use `binwalk -e erveehei.jpg` to extract the embedded files in the picture.

We will found a file `34EE.zip` with a password.

Use a common password list -> `fcrackzip -u -D -p rockyou.txt 34EE.zip` to crack the zip.

    PASSWORD FOUND!!!!: pw == !butterfly!

Unzipping the file will get you the flag.

> Flag : HZ{brut3forcing_is_c00l}