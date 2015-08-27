requirement:
install PIL

encode:

input: ppm image
output: huffman_code, huffman_encoded_image

python huffman_encode.py 'D:\GithubRepo\KNNFaceDetection\ppm\Matisse-Small.ppm'
::path change to your local path


decode:

input: huffman_code, huffman_encoded_image
output: jpg image

python huffman_decode.py 'D:\GithubRepo\KNNFaceDetection\ppm\Matisse-Small.ppm'

::path change to your local path