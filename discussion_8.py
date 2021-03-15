from bs4 import BeautifulSoup
import requests
import unittest

# Task 2: Get the URL that links to list of Nobel Prize Winners
# HINT: You will have to add https://en.wikipedia.org to the URL retrieved using BeautifulSoup
def getLink(soup):
    
    pass

# Task 3: Get the details from the box titled "College/school founding". Get all the college/school names and the year they were
# founded and organize the same into key-value pairs.
def getAdmissionsInfo2019(soup):

    pass



def main():
    # Task 1: Create a BeautifulSoup object and name it soup. Refer to discussion slides or lecture slides to complete this

    #### YOUR CODE HERE####

    #Call the functions getLink(soup) and getAdmissionsInfo2019(soup) on your soup object.
    getLink(soup)
    getAdmissionsInfo2019(soup)

class TestAllMethods(unittest.TestCase):
    def setUp(self):
        self.soup = BeautifulSoup(requests.get('https://en.wikipedia.org/wiki/University_of_Michigan').text, 'html.parser')

    def test_link_nobel_laureates(self):
        self.assertEqual(getLink(self.soup), 'https://en.wikipedia.org/wiki/List_of_Nobel_laureates_by_university_affiliation')

    def test_admissions_info(self):
        self.assertEqual(getAdmissionsInfo2019(self.soup), {'College of Literature, Science, and the Arts': '1841', 'School of Medicine': '1850', 'College of Engineering': '1854', 'School of Law': '1859', 'School of Dentistry': '1875', 'School of Pharmacy': '1876', 'School of Music, Theatre & Dance': '1880', 'School of Nursing': '1893', 'A. Alfred Taubman College of Architecture & Urban Planning': '1906', 'Horace H. Rackham School of Graduate Studies': '1912', 'Gerald R. Ford School of Public Policy': '1914', 'School of Education': '1921', 'Stephen M. Ross School of Business': '1924', 'School for Environment and Sustainability': '1927', 'School of Public Health': '1941', 'School of Social Work': '1951', 'School of Information': '1969', 'Penny W. Stamps School of Art & Design': '1974', 'School of Kinesiology': '1984'})

if __name__ == "__main__":
    main()
    unittest.main(verbosity = 2)