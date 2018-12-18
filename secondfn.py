from flask import request 

def main():
	b = request.get_data()
	return "second fun \n"+ str(b)+" headers:"+str(request.headers.get("username"))+"\n"

if __name__ == "__main__":
	main()
