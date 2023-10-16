import requests

class InfoServer : 
    def get_info(self) : 
        # Info Server 연결
        response = requests.get('http://localhost:8080/info')
        return response
    
    
if __name__ == '__main__' :
    info_server = InfoServer()
    print(info_server.get_info().status_code)
    