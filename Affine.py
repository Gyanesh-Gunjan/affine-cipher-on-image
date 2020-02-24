import cv2 
import math
import numpy as np
import random

class Affine:
    def __init__(self, a, b, m ):
        self.a = a
        self.b = b
        self.m = m
        while self.IsCoprime() is False:
            print(a," and ",m," Must be Coprime! ")
            a,m = map(int,input("Enter a and m (Seperated by single space): ").split(" "))
            self.a = a
            self.m = m
        self.inv_a =  self.ModInv()

    def IsCoprime(self):
        """
        Check whether a and m is prime or not. If it is prime then it return true else false
        """
        if math.gcd(self.a, self.m) == 1:
            return True
        return False

    def ModInv(self):
        """
        Form equation 1 = inv(a)*a mod m. we find inv(a)
        Inverse exist only if a and m be Coprime
        """
        for i in range(2,self.m):
            if (self.a * i) % self.m == 1 :
                return i
        return 1
 
    def E(self, x):
        """
        m is the length of range. a and b are the Keys of the cipher.
        The value a must be chosen such that a and are coprime.
        """
        
        return (self.a*x + self.b) % self.m

    def D(self,y):
        """
        Decryption at pixel level
        """
        return (self.inv_a * (y-self.b)) % self.m

    def encryption(self, original_img):
        """
        Encryption of image 
        """
        height = original_img.shape[0]
        width = original_img.shape[1]
        
        for i in range(0,height):
            for j in range(0,width):
                a = original_img[i][j]      # rgb list
                r = self.E(a[0])
                g = self.E(a[1])
                b = self.E(a[2])
                original_img[i][j] = [r,g,b]
        
        cv2.imwrite('encrypted_img.png', original_img)  # saving encrypted image


    def decryption(self, encry_img):
        """
        Decryption of image 
        """
        height = encry_img.shape[0]
        width = encry_img.shape[1]

        for i in range(0,height):
            for j in range(0,width):
                a = encry_img[i][j]         # rgb list
                r = self.D(a[0])
                g = self.D(a[1])
                b = self.D(a[2])
                encry_img[i][j] = [r,g,b]

        cv2.imwrite('decrypted_img.png', encry_img)   # Saving decrypted image


#------------- main program -------------------
A = Affine(71,37,256)
original_img = cv2.imread('cat.png')
A.encryption(original_img)
encry_img = cv2.imread('encrypted_img.png')
A.decryption(encry_img)
