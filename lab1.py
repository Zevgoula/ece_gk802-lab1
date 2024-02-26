import datetime
import requests



def main():
    # url = input("ENTER URL: ")

    url = "https://www.google.com/"

    def format_expires(expdate):
        try:
            current_datetime = datetime.datetime.now()
            curdate = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
            time_dif = expdate - curdate
            return str(time_dif)
        except Exception as e:
            return f"The expiration date has passed. Error: ¨{e}"


    try:
        url_request = requests.get(url)

        # print the headers
        print("\n---------------------------------------------------------")
        print("HEADERS: \n")
        for header, value in url_request.headers.items():
            print(f"{header}: {value}")

        # web server
        print("\n---------------------------------------------------------")
        print("WEB SERVER: \n")
        server_header = url_request.headers.get('Server', 'Server header not found')
        print(f"Server: {server_header}")

        # cookies
        print("\n---------------------------------------------------------")
        print("COOKIES: ")
        if 'Set-Cookie' in url_request.headers:
            print("\n\t\tCookies are being set.")

            # Parse
            cookies = url_request.cookies
            for cookie in cookies:
                expdate = datetime.datetime.fromtimestamp(cookie.expires).strftime('%Y-%m-%d %H:%M:%S')
                expduration = format_expires(expdate)
                print(f"Cookie Name: {cookie.name}, Expires: {expduration}")


        else:
            print("No cookies are being set.")




    except:
        print("Please enter a valid URL")


if __name__ == '__main__':
    main()
