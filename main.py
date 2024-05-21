import easyocr
import imageio as iio


def text_recognition(file_path):
    reader = easyocr.Reader([], gpu=True, download_enabled=True, user_network_directory='this', model_storage_directory='this')
    img1 = iio.imread(file_path)
    result = reader.readtext(img1)
    return result


def main():
    print(text_recognition(file_path='phone.jpg'))


if __name__ == '__main__':
    # # read an image
    # img = iio.imread("phone.jpg")
    #
    # # write it in a new format
    # iio.imwrite("phone.png", img)
    main()
