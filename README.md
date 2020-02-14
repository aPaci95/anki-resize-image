This is incompatible with addons:
* [ImageResizer](https://ankiweb.net/shared/info/1214357311): indeed,
  the point of image resizer is to ensure that images are not too big
  nor too small. The point of the current add-on is to set the size
  you want. So they try to do opposite things.
  
This add-on is partially compatible with:
* [maximum image height in card editor](https://ankiweb.net/shared/info/229181581): When an image has not been resized, the add-on "maximum image height in card editor" will work. When the image has been resized, the add-on "maximum image height in card editor" will have no effect and you're free to resize as much as you want. I must admit in this case that it was not the result I expected and I don't understand why it works this way. Normally "max-height" override "height"; but since jquery-ui does some works which I don't understand, it may makes all of this interact in an unexpected way.
* [Edit Field During Review](https://ankiweb.net/shared/info/1020366288) and [Edit Field During Review (Cloze)](https://ankiweb.net/shared/info/385888438): because my add-on only interacts with the editor, and those two add-ons interact with the reviewer. I may eventually change the second add-on to incorporate the current add-on; but this is not something I expect to do immediately. Mostly because those add-ons are quite complex.
* [Image Occlusion Enhanced for Anki 2.1](https://ankiweb.net/shared/info/1374772155): You can't resize images used in cards created through "Image occlusion enhanced". Or more precisely, you could, but you would need to resize all of the four images the same way. That seems to be complex and error-prone. However, both add-ons works correctly together; you can resize any image in other note type; and you can style create "image occlusion" notes.


It has been tested to be compatible with: 
* [Image style editor](https://ankiweb.net/shared/info/1593969147), that's mostly pure luck; but they works perfectly fine together. 
* [Browser: Table/Editor side-by-side (horizontal split)](https://ankiweb.net/shared/info/831846358)
* [Field History](https://ankiweb.net/shared/info/1247884413) 

