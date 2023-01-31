from src.fix import fix_images
import time

if __name__ == "__main__":
    start_time = time.time()
    fix_images.fix_list()
    print("--- %s seconds ---" % (time.time() - start_time))
