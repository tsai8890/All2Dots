<a id="readme-top"></a>


<h1 align="center">
  <br>
  All2Dots
  <br>
</h1>

<h4 align="center">Convert images to dot-based text.</h4>

<p align="center">
  <a href="#about-the-project">About The Project</a> •
  <a href="#getting-started">Getting Started</a> •
  <a href="#prerequisites">Prerequisites</a> •
  <a href="#usage">Usage</a> •
  <a href="#roadmap">Roadmap</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#contact">Contact</a> •
  <a href="#acknowledgments">Acknowledgments</a>
</p>
<br>


<!-- ABOUT THE PROJECT -->
## About The Project

### Key Features
* Text to dots
    * Convert input text to vertically-aligned dot-based text.
* Image to dots
    * Convert input image to dot-based text.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started


<!-- PREQUISITES -->
### Prerequisites
1. Clone the repo
    ```bash
    git clone https://github.com/tsai8890/All2Dots.git
    ```
2. Install python packages
    ```bash
    cd All2Dots
    pip3 install -r requirements.txt
    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- USAGE -->
## Usage
1. Convert the specified image to dot-based text
    ```bash
    cd All2Dots
    python3 src/main.py <target> [options]
    
    # Ex: python3 src/main.py -t "早安"
    # Ex: python3 src/main.py -t "早安" -s line
    # Ex: python3 src/main.py -f ./images/shiba.jpg
    # Ex: python3 src/main.py -f ./images/shiba.jpg -w 100 -b light -t 110

    # Target:
    #    -f <filepath>       Convert any image to dot-based text
    #    -t <text>           Convert any text to vertically-aligned dot-based text
    #    
    # Options:
    #    -s <style>          Output style, other format-related params will be ignored if this option is specified. 
    #                        ['terminal', 'line']
    #                        
    #    -w <width>          Maximal width for each line
    #                        (default: 100)
    #
    #    -b <background>     Light or dark background mode
    #                        ['dark', 'light']
    #                        (default: 'dark')
    #    
    #    -T <threshold>      Threshold for converting grayscale image to binary image
    #                        (default: 132)
    ```
<br>

2. The result will be directly shown on your terminal
    ```bash
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⢸⣟⠛⠛⠛⠛⠛⠛⠛⠛⢻⡇⠀⠀⠀
    ⠀⠀⠀⢸⣿⣤⣤⣤⣤⣤⣤⣤⣤⣼⡇⠀⠀⠀
    ⠀⠀⠀⢸⣟⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀
    ⠀⠀⠀⠘⠛⠛⠛⠻⢿⡟⠛⠛⠛⠛⠃⠀⠀⠀
    ⠀⢠⣤⣤⣤⣤⣤⣤⣼⣧⣤⣤⣤⣤⣤⣄⡀⠀
    ⠀⠈⠉⠉⠉⠉⠉⠉⢹⡏⠉⠉⠉⠉⠉⠉⠁⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠠⢶⡄⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠠⣾⡿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⣟⠀⠀
    ⠀⠠⣿⠇⠀⠀⠀⣰⡗⠀⠀⠀⠀⠀⠠⣟⠀⠀
    ⠀⢠⣤⣤⣤⣤⣼⣿⣤⣤⣤⣤⣤⣤⣤⣤⡄⠀
    ⠀⠀⠀⠀⢠⣼⠟⠀⠀⠀⠀⣸⡟⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠺⠿⢶⣤⣄⣠⣴⠟⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢀⣨⣽⠿⠿⣶⣄⣀⠀⠀⠀⠀
    ⠀⠠⢶⠶⠶⠟⠛⠋⠁⠀⠀⠀⠉⠻⠿⡖⠀⠀
    ```

    ```bash
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠛⠉        ⠉⠻⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁              ⠈⠹⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠃                   ⠹⢿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠶⠶⣶⣄⡀                 ⠨⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢉⣀⣀⡀ ⠹⢿⠆                ⠠⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠋  ⠉⠋⢛⣲⢦⡄   ⠠⣴⣶⣤⣄         ⠠⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟             ⢀⣀⡀⠉⠙⠻⢆⡀      ⢠⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟      ⢀       ⠈⠙⠳⢄⣀ ⠠⠇      ⣸⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠁    ⣀⣠⣼⣷⣤⣄⣀       ⠉⠱⠄     ⢠⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⠁  ⢠⣶⣿⣟⡛⠻⠿⣿⣿⡿⠗             ⢠⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇   ⢸⠿⢟⠋⠉  ⣈⠙⠛⣀            ⠠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇    ⢰⣿⣿⣶⣤⣄⡀⠡⢆⣰⣖⣀         ⠠⡜⠛⣉⣩⣍⢻⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⡖   ⠈ ⠹⠿⣿⣿⣷⣤⣿⣷⡟         ⠐⠡⣞⠉ ⠻⣼⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁         ⠉⠉⠁          ⠠⡌ ⠉  ⣰⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⡟⠛⠁                         ⣘⡀  ⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⠟⠁              ⠠⣄⣠⣄        ⣰⣿⣷⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣟⠁              ⠠⢶⣾⣿⣿⣿⡮⣔⣠⣄⣀⣀⣠⣴⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣶⣆⡀               ⠹⠿⠟⣀⣻⣿⣿⣿⣿⣿⠏⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣆             ⢰⡖⠃⣈⣹⣿⣿⣿⣿⣿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⡄            ⠠⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣗            ⠠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄          ⠠⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ```

    ```bash
    ⣿⣿⡟                     ⠠⣾⠟⠛⠉⠻⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
    ⣿⡟⠁        ⢠⣤⣄⡀                  ⠉⠙⠻⠿⠿⢿⣟⣻⣽⣿⣿⣿⣿⣿⣿⠟⠉
    ⡟         ⠠⣾⣿⠟⠋⢸⣆                    ⢠⣌⠙⠉⠻⣿⣿⣿⣿⣿⣟
              ⠠⡏   ⠈⠹⣷⣄                 ⣠⣟⠃    ⠻⣿⣿⣿⡟
               ⠁ ⢠⣄⡀⠠⣿⣿⣷⣤⠤⠴⡤⠄⠠⠦⣶⣦⠤⣤⣤⡤⢤⣴⣿⣿⣟⣠⣶⣟   ⠈⠙⠛⠁
    ⡞          ⡀ ⠨⣿⣿⣆⠻⣿⣿⣿⣇⣠⣶⣶⡾⠿⣿⡟⠻⣿⣿⣷⣄⢻⣿⣟⢻⣿⣿⡏ ⠠⠄
               ⢛  ⠻⣿⣟⡀⢸⡟⠣⢿⣿⣯⣭⣦⣦⣿⣿⣷⡤⠆⠹⠟⠃⠻⢟⣰⣿⡟⠁⣀
               ⢠⣼⡗ ⠛⠫⠗  ⠠⡿⠏⠛⢻⣯⣾⣿⣿⣿⣇   ⢀  ⠉⠛⠁ ⠠⣔   ⠰⣄⡀
               ⢸⣟⠡⡄⠚⠁        ⢹⣿⣿⣿⣿⠏           ⠛    ⠸⢿⡄
          ⠠⣄⡀  ⠈⠃             ⢹⣿⣟⠃     ⠘⠂           ⠸⣿⡄
          ⠠⣿⣿⣶⡄         ⣠⣄⣀   ⠺⢿⡏   ⠠⣤⣶⣦⣄            ⠹⣗
          ⠠⣿⣿⣿⠇        ⠻⣿⣷⣿⣷⣄⡀⢠⣼⣇ ⠠⢴⣿⣿⣿⡟⠋             ⢹
          ⢠⣿⣿⡏          ⠈⠉⠉⠉⠛⠡⣼⣿⢏⣰⡄                   ⠠
        ⠠⣴⣿⣿⣟                ⠠⠿⠟⠚⠛⠃
       ⠠⣾⣿⣿⣿⡏                  ⢀⣀⣀⣀                 ⣀⣠⣴
      ⠠⣼⣿⣿⣿⣿⡇                ⠠⣴⣿⣿⣿⣿⣷⡄            ⢠⣾⣿⣿⣿⣿
      ⠠⣟⡉⠛⠸⣿⡇                ⠠⢿⣿⣿⣿⣿⣿⠇           ⣰⠿⠿⠿⣿⣿⣿
      ⢸⣟⠁ ⠠⣟⡂            ⠁⡀   ⠨⣿⣿⣿⣿⣟           ⠠⢽⣄   ⠉
     ⠠⣿⣏  ⠠⠟⠁            ⠠⢿⣄⣀⣠⣼⣿⣿⣿⣿⣿⢤⣤⡞        ⠠⣿⡏⠉⠓
    ⣠⣼⣿⣟⡀ ⠠⡗              ⠈⢻⣿⣇⠈⠛⠛⠛⠛⠫⣿⡟         ⠠⣿⡇
    ⣿⣿⠿⠿⠇ ⢀⡉                ⢻⡿⢷⣦⣤⣤⣤⡞⠛⠃          ⢸⡇
    ⣿⣟   ⠠⣌⡀                 ⠉ ⠉⠙⠛⠉             ⠈⠁ ⠠⠄⠐
    ⣿⡇   ⠰⡟                                   ⠠⣤⣤⣄ ⢘⡀
    ⣿⣟   ⠠⠟⡀                                  ⠠⣬⣟
    ⣿⣿⡆   ⠺⠇                                  ⢀⠸⣿⣿⣤⣴⣄⣀⣀
    ⣿⣿⣇                      ⡀  ⡀  ⡀           ⡠⢿⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⡄                    ⠺⣿⣿⣿⣿⣷⠟⠁           ⠐⠺⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⡄                                      ⠠⣾⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣗                                       ⢹⣿⣿⣿⣿⣿⣿
    ⣿⣿⣿⣿⣿⡆                                      ⢸⣿⣿⣿⣿⣿⣿

    ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ROADMAP -->
## Roadmap
- [x] Convert input image to dot-based text
- [x] Convert input text to dot-based text
- [x] Customized parameters for converting images
- [ ] A good GUI

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTRIBUTING -->
## Contributing
<!-- Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**. -->

If you have a suggestion that would make the project better, please fork the repo and create a pull request. <br> 
You can also simply open an issue with the tag `enhancement`. 

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<br>

Besides, if you find this project useful, don't forget to give it a star !

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- CONTACT -->
## Contact

Aaron Tsai - aarontsaai@gmail.com

Project Link: [https://github.com/tsai8890/LeetTimer](https://github.com/tsai8890/LeetTimer)

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
* [Best README Template](https://github.com/othneildrew/Best-README-Template)
* [Electron-Markdownify's README](https://github.com/amitmerchant1990/electron-markdownify/blob/master/README.md)

<p align="right">(<a href="#readme-top">back to top</a>)</p>
