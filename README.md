# Affine Cipher On Image
The affine is a type of monoalphabetical substitution cipher, where each letter in an alphabet is mapped to its numberic equivalent, encrypted using a simple mathematical fucntion, and converted back to a letter.
But here, I use this technique on image at pixel level taking alphabet size m = 256 (i.e. 0,1,2,...,255).

## Above Python code work successfully on Encryption and Decryption : 
* Take input original color image **cat.png** 
* Encrypt **cat.png** image and save it as **encrypted_img.png** image
* Decrypt **encrypted_img.png** image and save it as **decrypted_img.png** image
 
Package		|   Version
----------------|------------
numpy           |    1.18.1
opencv-python   |   4.1.2.30

# Original Image 
![Cat.png](https://raw.githubusercontent.com/Gyanesh-Gunjan/affine-cipher-on-image/master/cat.png)

# Encrypted Image 
![Cat.png](https://raw.githubusercontent.com/Gyanesh-Gunjan/affine-cipher-on-image/master/encrypted_img.png)

# Decrypted Image 
![Cat.png](https://raw.githubusercontent.com/Gyanesh-Gunjan/affine-cipher-on-image/master/decrypted_img.png)
### Ref : https://en.wikipedia.org/wiki/Affine_cipher
