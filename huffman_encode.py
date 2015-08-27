__author__ = 'zhangruichang'
from PIL import Image
from heapq import heapify, heappush, heappop
import sys
#input: char frequency list
#output: huffman code list, sorted by char desc
def encode(symb2freq):
    """Huffman encode the given dict mapping symbols to weights"""
    heap = [[wt, [sym, ""]] for sym, wt in symb2freq.items()]
    heapify(heap)
    while len(heap) > 1:
        lo = heappop(heap)
        hi = heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    # print heappop(heap)[1:]
    return sorted(heappop(heap)[1:], key=lambda p: p[0])


if __name__ == '__main__':
    #ppm_path = 'D:\GithubRepo\KNNFaceDetection\ppm\Matisse-Small.ppm'
    ppm_path = sys.argv[1]
    ppm_image = Image.open(ppm_path)
    print ppm_image.size[0], ppm_image.size[1]
    freq = dict()
    for i in range(256):
        freq.update({i: 0})
    for i in range(ppm_image.size[0]):
        for j in range(ppm_image.size[1]):
            '''
            r, g, b = ppm_image.getpixel((i, j))[0] + 100, ppm_image.getpixel((i, j))[1] + 50, \
                      ppm_image.getpixel((i, j))[2] + 70
            if r > 255:
                r = 255
            if g > 255:
                g = 255
            if b > 255:
                b = 255
            ppm_image.putpixel((i, j), (r, g, b))
            '''
            for k in ppm_image.getpixel((i, j)):
                freq[k] += 1
    huffman_code_dict = encode(freq)
    #print huffman_code_dict
    #print ppm_path+'.huffman_encoded_image'
    huffman_encoded_image_file = open(ppm_path + '.huffman_encoded_image', 'w')
    huffman_code_file = open(ppm_path + '.huffman_code', 'w')
    for ele in huffman_code_dict:
        huffman_code_file.write(str(ele[0]) + ' ' + ele[1] + '\n')

    huffman_code_file.close()

    for i in range(ppm_image.size[0]):
        for j in range(ppm_image.size[1]):
            huffman_encoded_image_file.write(
                ' '.join(huffman_code_dict[ppm_image.getpixel((i, j))[k]][1] for k in range(3)) + '\t')
            # huffman_encoded_image_file.write('\t')
        huffman_encoded_image_file.write('\n')
    huffman_encoded_image_file.close()

