{
    "metadata": {
        "kernelspec": {
            "name": "python3",
            "display_name": "Python 3 (ipykernel)",
            "language": "python"
        },
        "language_info": {
            "name": "python",
            "version": "3.8.10",
            "mimetype": "text/x-python",
            "codemirror_mode": {
                "name": "ipython",
                "version": 3
            },
            "pygments_lexer": "ipython3",
            "nbconvert_exporter": "python",
            "file_extension": ".py"
        },
        "extensions": {
            "azuredatastudio": {
                "version": 1,
                "views": []
            }
        }
    },
    "nbformat_minor": 2,
    "nbformat": 4,
    "cells": [
        {
            "cell_type": "code",
            "source": [
                "from selenium import webdriver\r\n",
                "from selenium.webdriver.common.keys import Keys\r\n",
                "from time import sleep\r\n",
                "from os import environ\r\n",
                ""
            ],
            "metadata": {
                "azdata_cell_guid": "878c141b-72fa-423e-83e6-5d30bf529866",
                "extensions": {
                    "azuredatastudio": {
                        "views": []
                    }
                }
            },
            "outputs": [],
            "execution_count": 20
        },
        {
            "cell_type": "code",
            "source": [
                "user_name = environ.get('charlesyou')\r\n",
                "password = environ.get('Fisherman')"
            ],
            "metadata": {
                "azdata_cell_guid": "cbe4542d-597c-4025-bc97-3003e897499b"
            },
            "outputs": [],
            "execution_count": 22
        },
        {
            "cell_type": "code",
            "source": [
                "def Booking():\r\n",
                "    browser=webdriver.Chrome(\"/Users/Charles You/Documents/chromedriver\")\r\n",
                "    browser.maximize_window()\r\n",
                "    try:\r\n",
                "            browser.get(\"https://member.truegroup.com.sg/\")\r\n",
                "            sleep(1)\r\n",
                "            browser.find_element_by_xpath('//*[@id=\"cphMain_txtUsername\"]').click()\r\n",
                "            browser.find_element_by_xpath('//*[@id=\"cphMain_txtUsername\"]').send_keys(\"charlesyou\")\r\n",
                "            browser.find_element_by_xpath('//*[@id=\"cphMain_btnNext\"]').click()\r\n",
                "            sleep(1)\r\n",
                "            browser.find_element_by_xpath('//*[@id=\"cphMain_txtPassword\"]').click()\r\n",
                "            browser.find_element_by_xpath('//*[@id=\"cphMain_txtPassword\"]').send_keys(\"True123!\")\r\n",
                "            browser.find_element_by_xpath('//*[@id=\"cphMain_lnkSubmit\"]').click()\r\n",
                "            sleep(1)\r\n",
                "            browser.find_element_by_xpath('//*[@id=\"cphMain_selClub\"]/option[8]').click()\r\n",
                "            sleep(1)\r\n",
                "            browser.find_element_by_xpath('//*[@id=\"cphMain_selClassCategory\"]/option[2]').click()\r\n",
                "            sleep(1)\r\n",
                "            browser.find_element_by_xpath('//*[@id=\"cphMain_pnlClassScheduleSearch\"]/div/div/div[3]/div/div[2]/label').click()\r\n",
                "            sleep(1)\r\n",
                "            browser.find_element_by_xpath('//*[@id=\"cphMain_txtDate_table\"]/tbody/tr[3]/td[6]/div').click()\r\n",
                "            sleep(2)\r\n",
                "            browser.find_element_by_xpath('//*[@id=\"divList\"]/div[3]/div[3]/a').click()\r\n",
                "            print(\"Booked Successfully\")\r\n",
                "\r\n",
                "    except:\r\n",
                "            print(\"Booking Failed\")\r\n",
                "\r\n",
                "if __name__ == '__main__':\r\n",
                "    Booking()"
            ],
            "metadata": {
                "azdata_cell_guid": "45f305d8-5766-45b0-a3b3-900c7ff13da1"
            },
            "outputs": [
                {
                    "name": "stdout",
                    "text": "Booked Successfully\n",
                    "output_type": "stream"
                }
            ],
            "execution_count": 40
        },
        {
            "cell_type": "code",
            "source": [
                "chrome_options = webdriver.ChromeOptions()\r\n",
                "chrome_options.binary_location = os.environ.get(\"GOOGLE_CHROME_BIN\")\r\n",
                "chrome_options.add_argument(\"--headless\")\r\n",
                "chrome_options.add_argument(\"--disable-dev-shm-usage\")\r\n",
                "chrome_options.add_argument(\"--no-sandbox\")\r\n",
                "browser = webdriver.Chrome(executable_path=environ.get(\"CHROMEDRIVER_PATH\"), options=chrome_options)"
            ],
            "metadata": {
                "azdata_cell_guid": "723a1f0c-844f-4e05-9805-685d5f42b8ba"
            },
            "outputs": [],
            "execution_count": null
        }
    ]
}