from supabase import create_client, Client

users = ["mabdullah.elahi", "hussain.sheikh", "ifham.elahi"]
url: str = "https://keaqhyhbatixvekvbopx.supabase.co"
key: str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtlYXFoeWhiYXRpeHZla3Zib3B4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTc3OTIyMjIsImV4cCI6MjAzMzM2ODIyMn0.nf3a7CtkNlsfnGjYycVU8WpwCh6GOqhUZZXvYfibo3s"
supabase: Client = create_client(url, key)


def get_sales_data(user=""):

    if user not in users:
        return "404"
    else:        
        response = supabase.table('db_sales').select("*").execute().data
        return response