

from PIL import Image
import webbrowser
import sys

def get_pixel(start, max_huffman_code_len, huffman_code):
    for len1 in range(1, max_huffman_code_len+1):
        if huffman_code.get(row[start : start+len1]) is not None:
            r = huffman_code[row[start : start+len1]]
            for len2 in range(1, max_huffman_code_len + 1 ):
                if huffman_code.get(row[start+len1: start+len1+len2]) is not None:
                    g = huffman_code[row[start+len1: start+len1+len2]]
                    for len3 in range(1, max_huffman_code_len + 1):
                        if huffman_code.get(row[start+len1+len2:start+len1+len2+len3]) is not None:
                            b = huffman_code[row[start+len1+len2:start+len1+len2+len3]]
                            start += len1+len2+len3
                            return [(r, g, b), len1+len2+len3]

if __name__ == '__main__':
    image_path = sys.argv[1]
    #image_path = 'ppm/gogol.ppm'
    #read huffman code
    huffman_code_file = open(image_path+'.huffman_code','r')
    huffman_code = dict()
    max_huffman_code_len = 0
    for line in huffman_code_file:
        fields = line.strip().split(' ')
        char, code = int(fields[0]), fields[1]
        max_huffman_code_len = max(max_huffman_code_len, len(code))
        huffman_code.update({code:char})

    #read huffman encoded file
    huffman_encoded_image_file = open(image_path + '.huffman_encoded_image', 'r')
    huffman_decoded_image = []
    for line in huffman_encoded_image_file:
        row = line.strip()
        line = []
        start = 0
        while start < len(row):
            res = get_pixel(start, max_huffman_code_len, huffman_code)
            line.append(res[0])
            start += res[1]
        huffman_decoded_image.append(line)

        '''
        pixel_line = []
        for pixel in row:
            #print (pixel[0],pixel[1],pixel[2])
            each_pixel = pixel.split(' ')
            pixel_line.append((huffman_code[each_pixel[0]],huffman_code[each_pixel[1]],huffman_code[each_pixel[2]]))
        huffman_decoded_image.append(pixel_line)
        '''
    #original_image = Image.fromarray(huffman_decoded_image)


    print len(huffman_decoded_image), len(huffman_decoded_image[0])
    original_image=Image.new('RGBA',(len(huffman_decoded_image), len(huffman_decoded_image[0])))
    for i in range(len(huffman_decoded_image)):
        for j in range(len(huffman_decoded_image[0])):
            original_image.putpixel((i, j), huffman_decoded_image[i][j])
    original_image_file = sys.argv[1] + '.jpg'
    #original_image_file='D:\GithubRepo\KNNFaceDetection\ppm\Matisse-Small.jpg'
    original_image.save(original_image_file)
    webbrowser.open(original_image_file)

    ppm_path = sys.argv[1]
    ppm_image = Image.open(ppm_path)
    dif_cnt = 0
    for i in range(len(huffman_decoded_image)):
        for j in range(len(huffman_decoded_image[0])):
            if ppm_image.getpixel((i, j)) != huffman_decoded_image[i][j]:
                dif_cnt += 1
    print float(dif_cnt) / (len(huffman_decoded_image) * len(huffman_decoded_image[0]))