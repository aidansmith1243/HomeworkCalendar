FasdUAS 1.101.10   ��   ��    k             l     ��  ��     use scripting additions     � 	 	 . u s e   s c r i p t i n g   a d d i t i o n s   
  
 l     ��  ��      use framework "Foundation"     �   4 u s e   f r a m e w o r k   " F o u n d a t i o n "      l     ��  ��    G Aproperty NSString : a reference to current application's NSString     �   � p r o p e r t y   N S S t r i n g   :   a   r e f e r e n c e   t o   c u r r e n t   a p p l i c a t i o n ' s   N S S t r i n g      l     ��������  ��  ��        l     ��  ��      @author Aidan Smith     �   (   @ a u t h o r   A i d a n   S m i t h      l     ����  r         b     	   !   l     "���� " c      # $ # l     %���� % I    �� &��
�� .earsffdralis        afdr &  f     ��  ��  ��   $ m    ��
�� 
ctxt��  ��   ! m     ' ' � ( ( f C o n t e n t s : R e s o u r c e s : S c r i p t s : P y t h o n : C a l e n d a r R u n n e r . p y  o      ���� 0 filepath filePath��  ��     ) * ) l    +���� + r     , - , m     . . � / /  : - 1    ��
�� 
txdl��  ��   *  0 1 0 l    2���� 2 r     3 4 3 n     5 6 5 2   ��
�� 
citm 6 o    ���� 0 filepath filePath 4 o      ���� 	0 paths  ��  ��   1  7 8 7 l    9���� 9 r     : ; : m     < < � = =  / ; 1    ��
�� 
txdl��  ��   8  > ? > l   + @���� @ r    + A B A l   ) C���� C n    ) D E D 7   )�� F G
�� 
ctxt F m   # %����  G m   & (������ E o    ���� 	0 paths  ��  ��   B o      ���� 	0 paths  ��  ��   ?  H I H l  , 9 J���� J r   , 9 K L K l  , 7 M���� M n   , 7 N O N 7  - 7�� P Q
�� 
ctxt P m   1 3����  Q m   4 6������ O o   , -���� 	0 paths  ��  ��   L o      ���� 
0 paths2  ��  ��   I  R S R l  : ? T���� T r   : ? U V U c   : = W X W o   : ;���� 	0 paths   X m   ; <��
�� 
ctxt V o      ���� 	0 paths  ��  ��   S  Y Z Y l  @ E [���� [ r   @ E \ ] \ c   @ C ^ _ ^ o   @ A���� 
0 paths2   _ m   A B��
�� 
ctxt ] o      ���� 
0 paths2  ��  ��   Z  ` a ` l     ��������  ��  ��   a  b c b l     ��������  ��  ��   c  d e d l     �� f g��   f J D mod for adding "\" before the space to allow the terminal to run it    g � h h �   m o d   f o r   a d d i n g   " \ "   b e f o r e   t h e   s p a c e   t o   a l l o w   t h e   t e r m i n a l   t o   r u n   i t e  i j i l  F K k���� k r   F K l m l m   F G n n � o o   m 1   G J��
�� 
txdl��  ��   j  p q p l  L Q r���� r r   L Q s t s n   L O u v u 2  M O��
�� 
citm v o   L M���� 	0 paths   t o      ���� 	0 paths  ��  ��   q  w x w l  R w y���� y Y   R w z�� { |�� z Z   _ r } ~���� } =  _ e  �  n   _ c � � � 4   ` c�� �
�� 
cobj � o   a b���� 0 x   � o   _ `���� 	0 paths   � m   c d � � � � �    ~ r   h n � � � m   h i � � � � �  \   � n       � � � 4   j m�� �
�� 
cobj � o   k l���� 0 x   � o   i j���� 	0 paths  ��  ��  �� 0 x   { m   U V����  | n   V Z � � � 1   W Y��
�� 
leng � o   V W���� 	0 paths  ��  ��  ��   x  � � � l  x } ����� � r   x } � � � c   x { � � � o   x y���� 	0 paths   � m   y z��
�� 
ctxt � o      ���� 	0 paths  ��  ��   �  � � � l     ��������  ��  ��   �  � � � l  ~ � ����� � Q   ~ � � ��� � I  � ��� ���
�� .sysoexecTEXT���     TEXT � b   � � � � � b   � � � � � b   � � � � � m   � � � � � � �  c d   � o   � ����� 	0 paths   � m   � � � � � � �  ; � m   � � � � � � �  p y t h o n   r u n . p y��   � R      ������
�� .ascrerr ****      � ****��  ��  ��  ��  ��   �  ��� � l      �� � ���   ���#########################################set accountName to "iCloud"set folderName to "School"set noteName to "My Homework"set noteContents to ""set filePath to paths & "/lib/data/notes.txt"set Shows to paragraphs of (read filePath)set ls to {}repeat with ccd in Shows	set end of ls to "<div>" & ccd & "</div>"end repeatset noteContents to ls as texttell application "Notes"	tell account accountName		tell folder folderName			try				set body of note noteName to noteContents			on error				make new note with properties {name:noteName, body:noteContents}			end try		end tell	end tellend telldelay 10tell application "Notes" to quit#display dialog noteContents
    � � � �`  # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #  s e t   a c c o u n t N a m e   t o   " i C l o u d "  s e t   f o l d e r N a m e   t o   " S c h o o l "  s e t   n o t e N a m e   t o   " M y   H o m e w o r k "  s e t   n o t e C o n t e n t s   t o   " "   s e t   f i l e P a t h   t o   p a t h s   &   " / l i b / d a t a / n o t e s . t x t "  s e t   S h o w s   t o   p a r a g r a p h s   o f   ( r e a d   f i l e P a t h )  s e t   l s   t o   { }  r e p e a t   w i t h   c c d   i n   S h o w s  	 s e t   e n d   o f   l s   t o   " < d i v > "   &   c c d   &   " < / d i v > "  e n d   r e p e a t  s e t   n o t e C o n t e n t s   t o   l s   a s   t e x t   t e l l   a p p l i c a t i o n   " N o t e s "  	 t e l l   a c c o u n t   a c c o u n t N a m e  	 	 t e l l   f o l d e r   f o l d e r N a m e  	 	 	 t r y  	 	 	 	 s e t   b o d y   o f   n o t e   n o t e N a m e   t o   n o t e C o n t e n t s  	 	 	 o n   e r r o r  	 	 	 	 m a k e   n e w   n o t e   w i t h   p r o p e r t i e s   { n a m e : n o t e N a m e ,   b o d y : n o t e C o n t e n t s }  	 	 	 e n d   t r y  	 	 e n d   t e l l  	 e n d   t e l l  e n d   t e l l   d e l a y   1 0  t e l l   a p p l i c a t i o n   " N o t e s "   t o   q u i t  # d i s p l a y   d i a l o g   n o t e C o n t e n t s 
��       �� � � � � ���   � ��������
�� .aevtoappnull  �   � ****�� 0 filepath filePath�� 	0 paths  �� 
0 paths2   � �� ����� � ���
�� .aevtoappnull  �   � **** � k     � � �   � �  ) � �  0 � �  7 � �  > � �  H � �  R � �  Y � �  i � �  p � �  w � �  � � �  �����  ��  ��   � ���� 0 x   � ���� '�� .������ <���� n���� � � � � �����~
�� .earsffdralis        afdr
�� 
ctxt�� 0 filepath filePath
�� 
txdl
�� 
citm�� 	0 paths  ������ 
0 paths2  
�� 
leng
�� 
cobj
�� .sysoexecTEXT���     TEXT�  �~  �� �)j  �&�%E�O�*�,FO��-E�O�*�,FO�[�\[Zl\Z�2E�O�[�\[Zl\Z�2E�O��&E�O��&E�O�*�,FO��-E�O $k��,Ekh  ���/�  ����/FY h[OY��O��&E�O a �%a %a %j W X  h � � � � � M a c i n t o s h   H D : U s e r s : A i d a n : P r o g r a m m i n g : P y t h o n : H o m e w o r k C a l e n d a r : H o m e w o r k . a p p : C o n t e n t s : R e s o u r c e s : S c r i p t s : P y t h o n : C a l e n d a r R u n n e r . p y � � � � � U s e r s / A i d a n / P r o g r a m m i n g / P y t h o n / H o m e w o r k C a l e n d a r / H o m e w o r k . a p p / C o n t e n t s / R e s o u r c e s / S c r i p t s / P y t h o n � � � � � A i d a n / P r o g r a m m i n g / P y t h o n / H o m e w o r k C a l e n d a r / H o m e w o r k . a p p / C o n t e n t s / R e s o u r c e s / S c r i p t s ascr  ��ޭ