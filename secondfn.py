from flask import request 
import json

def main():
	b = request.get_data()
	#b = json.dumps(request.get_json())
	return "second fun \n"+ str(b)+" headers:"+str(request.headers.get("username"))+"\n"

if __name__ == "__main__":
	main()
