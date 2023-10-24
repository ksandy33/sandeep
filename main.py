def load_confidential_data():
    
    confidential_data = os.environ.get('CONFIDENTIAL_DATA')

    if confidential_data is None:
        confidential_data = input("Enter the confidential data: ")
        
    return confidential_data

def main():
    confidential_data = load_confidential_data()

    data = pd.read_csv('data.csv')

    #  and now we use the data further

if __name__ == "__main__":
    main()