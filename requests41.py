import requests
import gc
def call():
    response=requests.get("https://www.google.com")
    print("Status code",response.status_code)
    return 

def main():
    print("no of tracked objects before calling get method")
    print(len(gc.get_objects()))
    call()
    gc.collect()
    print("no of tracked objects after calling get method and gc.collect all non refrenced are deleted ")
    print(len(gc.get_objects()))
    
if __name__=='__main__':
    main()
