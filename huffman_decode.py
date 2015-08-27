__author__ ='richard'

from PIL import Image
import webbrowser
import sys

if __name__ == '__main__':
    image_path = sys.argv[1]
    huffman_encoded_image_file = open(image_path + '.huffman_encoded_image', 'r')
    huffman_code_file = open(image_path+'.huffman_code','r')
    huffman_code = dict()
    for line in huffman_code_file:
        fields = line.strip().split(' ')
        char, code = int(fields[0]), fields[1]
        huffman_code.update({code:char})

    huffman_decoded_image = []
    for line in huffman_encoded_image_file:
        row = line.strip().split('\t')
        pixel_line = []
        for pixel in row:
            #print (pixel[0],pixel[1],pixel[2])
            each_pixel=pixel.split(' ')
            pixel_line.append((huffman_code[each_pixel[0]],huffman_code[each_pixel[1]],huffman_code[each_pixel[2]]))
        huffman_decoded_image.append(pixel_line)
    #original_image = Image.fromarray(huffman_decoded_image)
    print len(huffman_decoded_image), len(huffman_decoded_image[0])
    original_image=Image.new('RGBA',(len(huffman_decoded_image), len(huffman_decoded_image[0])))
    for i in range(len(huffman_decoded_image)):
        for j in range(len(huffman_decoded_image[0])):
            original_image.putpixel((i, j), huffman_decoded_image[i][j])
    original_image_file='D:\GithubRepo\KNNFaceDetection\ppm\Matisse-Small.jpg'
    original_image.save(original_image_file)
    webbrowser.open(original_image_file)