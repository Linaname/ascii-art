# ascii-art
Скрипт для создания **теперь цветного!** отображаемого в консоли ASCII-арта из несложного изображения

# Usage
```bash
$ python main.py --help
usage: main.py [-h] [--width WIDTH] [--block BLOCK] [--mode MODE] path

positional arguments:
  path           path to image

optional arguments:
  -h, --help     show this help message and exit
  --width WIDTH  art width (default: current terminal width)
  --block BLOCK  size of pixel block converted to single char.
                 Available: 'x1'(default), '1x2'
  --mode MODE    color depth (bits) used in art. Available: '1' (monochrome),
                 '3', '3/4', '4', '24'
$ python main.py /home/lina/lina.jpg --width 120 --block 2x2 --mode 1
▄▀ ▖  ▖ ▄▞▗▞▘▄▘        ▗▖           ▖  ▗                                   ▗▖         ▗▖       ▄▝▖▘  ▖ ▘▖   ▀█▄▝ ▗      
▘▖▝ ▞▘▗▀▚▞▘▄▀▗       ▗▖▘▗ ▗▖▘     ▝▘ ▖▀   ▄         ▖▘  ▗▝     ▗▖  ▗▀    ▗▞▘ ▖      ▗▖▘ ▄▘   ▄▀▄▝  ▄▀   ▝▘▖   ▀█▄▘▄▝▗▞▘ 
▝ ▖▀▗▀▚▖▘▗▝▚▞▚ ▘ ▄▝▚▝▘▗█▙▞▀▗▝▘▄▄▖▀▀▝▘▖▘  ▝ ▖▝▗ ▗  ▄▝▘▗▄▀▗  ▗  ▖▐█▄ ▀ ▖▘▖▗▀ ▗▛    ▄▝▄▘ ▗▝ ▖▘▄▀▄▞  ▗▞▘    ▗▖▝▘▄▖ ▝▀▜▄▞▘▗▖ 
▗▘▗▝ ▄▘ ▞▘▟▙▝ ▗▟▀ ▗▘ ▟▛▚▛ ▝ ▄▛▀   ▞ ▘▗ ▖▘▗▀ ▄▌▝ ▗▞ ▄ ▖▘▗▘ ▝▘▗▝ ▐▛▜▄ ▘▖▘▞▘ ▟▌▘▝ ▄▝▗▞▘ ▄▘▗▀▗▀▗▟ ▖▗▄▀  ▗▝  ▝▜▖▖ ▀▄▖   ▀█▙▄▖
▗▀▘▄▘ ▄▀▗▛▌▀▗▞▘  ▗▙▞▀ ▗▘  ▄▀     ▗▘▗▝  ▗▛▘ ▞ ▐▖▞▘     ▝ ▖▘▗▞   ▐▖  ▜▄    ▞▘▖▘▄▝ ▟▘ ▗▀▗▞▚▀▗▀  ▝▀▙▖  ▄▘▄▘ ▖ ▜▞▜▄  ▀▙▄    ▘
 ▄▀ ▗▀▗█▖▜ ▝    ▄█▘  ▟▌ ▄▘       ▐▞ ▗▟█▌  ▟   ▜    ▚▗▘ ▝▙▖▘ ▗▞ ▐▘   ▝▜▖ ▀▗▘ ▝ ▗▀  ▞▘▞▚ ▗ ▗▞▘▄   ▀▛▚▄▖ ▗▘   ▜▖▝▜█▙▙▄▀▜▄▄ 
▝ ▗▛▗▟▛▀▝▘     ▟▛   ▄▘ ▘        ▐▘▗▟▛▚▝▌ ▞     ▚▖▗▞    ▗▐▙ ▝▘▖▘▐▙     ▝█▄▘  ▗▛▀▄▄▛    ▝▜██▌▗▄    ▝▀▄▝▜▄▄▞   ▜▖   ▀▀▜███▙
 ▞▘▄█▀        ▟▛   ▗            ▖▟▛▘▐▘ ▚▞       ▐▖       █▌▙▘   █       ▝▜▄▗▛  ▄ ▝▜▙▖    ▜▟▚▖ ▝▘▗   ▜▄ ▀▜▙▞  ▜▖      ▝▜▌
▝▟█▛         ▗▛    ▘           ▗█▘ ▐▘  ▝▌   ▖    ▝▌▗  ▗▐▛▘█▌▙▖  ▜▌        ▝▀▄  ▜▖   ▝▀▙▟   ▀▞▜▄    ▘ ▝▚   ▝▀▙▄▜▖        
▐█▀         ▗█▘   ▝           ▄▛▌ ▗▛    █▘  ▌     ▝▚  ▘▐▌▗▀█▖▀▄▖ ▙      ▚    ▀▗▘▀▄     ▝▀▄▄ ▝▚▞▜▄            ▝▀█▄       
█▘          ▟▛               ▟▛ ▌▗▛      ▙▝ ▌       ▘▖ ▖██▖▝█▖▝▀▄▟▖     ▝▙     ▀ ▝▚▖      ▝▀▗▖▝▚▞▜▄             ▀▚▖     
▘           █▌              ▟█▞ ▙▝▘      ▝▖ ▌         ▗ █▄▙▖▞█▖          ▝▙        ▘          ▀▗█▖▝▜▄                   
           ▐▛           ▗▌▗██▄▄▄█▌        ▝▖▌           █▙█▟▟██▙          ▝█▖                    ▀▚▖▝█▄                 
           ▐▌          ▗▝▗▟██████▌          ▙           ▐███████▙▖         ▝█▖                     █▖ ▀▙▖      ▐▖       
           ▟▌         ▖  ▟████████          ▝     ▗     ▐█████████▄         ▝▜▄         ▗▄▄▄ ▀▀▀▘       ▜▙▖     ▀▄      
      ▄    █▘   ▌    ▟▘ ▐█████████▙               ▝▜▖   ▝██████████▙          ▜█▖  ▗▄▄▛▀▀▗▄▖▝▘           ▝▜▙     █▌▖    
     ▐▘    █   ▗▌   ▟▌ ▐███████████▙                ▜▄   ▐███████████▙ ▜█▄    ▄███▛ ▄▄▀▀▘                  ▝▙▖   ▝█▐    
     █ ▌   █▖  ▐▌  ▟█  █████████████▙       ▄      ▘ ▝▙  ▐█████████████▖▀███▛▀▗▄▟███▖  ▝▀▜▄▄▖       ▝▜▄     ▝▜▄   ▜▌    
▟   ▐▙ ▙  ▟█▌  ▟████▄▀▜██████████████▙       ▘     █   ▜▖ ███████████████▛█▄██▙   ▝▜▛▜▄   ▀▙ ▀▚▄▖     ▗▀▜▄    ▝█▖  ▜▄   
▌▖  ▟  █ ▟▌▟█▛▀▜█▀█▝▀▜█▙▟▜████████████▙▖     ▖ ▙▖  ▐▖   ▝▚▟█████████▛▀▙▄██▙██▀▝▀▙▄  ▜█▖▀█▄  ▀▙  ▝▜▄▖   ▀▖ ▀▚▖   ▀▙ ▝█   
▘█  █  █▟█ ▝█▖ ▐▖▟▌  ▐████▙▀████████████▖    ▐▗▘▝▖  ▌    ▗▛████████▄██████▖ ▀█ ▄▛▝▜▙▖ ▜█▖▝▀█▄▟▜▄▘▞ ▝▀▄▖ ▚▖  ▝▜▄  ▝█ ▟▌  
▞▜▖ ▌   █▘  █▌ ▐▌▜   ▟▜█████▙████████████▙▖  ▐▛ ▗  ▖▐▖ ▖ ▟ ▝████████▛▜███████▙▟█  ▖ ▀▚▄▞▀▙▖ ▗▀▜█▟▌  ▖ ▝▄▟█ ▗  ▝▀▄▖ ▜▖█▖ 
▘▐▌ ▘  ▟▌ ▗▘▐█▖▐▌▐ ▖ ▛  ▝▀▀████████████████▙▄ ▐▄ ▟▌ ▝▚▞ ▝▘▞ ▜█▛▜▛▀▘ ▄██▛▀▀▀███████▄▄▟▘ ▝▀▐▀▙▖   ▝▀█▙▄▄▀  ▚▝▘▗▖ ▗ ▀▄ ▀▄▘ 
  █ ▌ ▝█▘▄▘  ▜▙▐▙ ▞ ▐▌▝  ▗▟███████▀▛▀▀▀▀▀▀▀▀▀▀▙█▄▘   ▛ ▗▚▞▗▞▀▛▜▟ ▗▞▐██▛ ▗ ▗█▛   ▀▀███▄▞▘▄ ▖▝▀▙▖▗▙▀  ▀▀▜▄▟▘ ▗▝ ▞▘ ▘ ▝▗▝▚ 
  ▐▖  ▗█▟▛▗▘  ▜██ ▝ ▟▌▗▞▚██▛▘▗████▛▖▗▖▗▖▗ ▖    ▝▀▜▄▄▞  ▚▘▗▘ ▘ ▗▀█▛▄██▀▄▟▘ ▐█▌      ▝▜███▌▖▘ ▌▄▟▛▙▗▝ ▄  ▝▀█▄▘▄▝ ▞▗▘ ▗  ▗▘
▝▖▘▘  ▐█▛▚▘   ▝▜█   ▐▌▝▗██▛   █▘▝▜▙▄▘▗▘▗▀▞ ▗▝      ▝▀▀▘▙▄▙▄▝  ▘  ███▄▀▘   ▝▀        ▗▟███▙▄███▛ ▖▘▄▝  ▖   ▀█▖▗▀ ▘ ▄▘   ▘
▗▘ ▗  ▐█▐▛▗▟ ▗▝▜█▙  ▖▌▗██▌▞▗  ▛   ▀█▙▖▗▘▟ ▄▘ ▄▘ ▗▞ ▗▖     ▝▀▀▀▘▀▟█▀▘                ▟█▛▀████▌▘▗▝▖▀  ▄▀ ▄▄▖▀▘▀▙▖  ▞▘▗▘▄▌ 
▌     ▐█▌ ▟▌ ▖▞▘ ▜█▙▄█▟██  ▄▘ ▘    ▝▜█▌▝ ▞▘ ▟▘ ▗▞ ▗▘ ▄ ▟ ▗▖ ▖ ▝▜▛          ▗▄     ▗▟██▌  ▀███▄▄▘  ▗█▟█▛▀   ▗ ▐█▙  ▗▚█▘  
 ▞  ▘ ▐█▙▟▙▄ ▟    ▀█▀███▘▞▘          ▝█▙   █  ▗▘ ▞▘ ▗▘▞▀▜▙▄▞ ▐▘▗           ▐██  ▗▄████▌    ▜██████▛▀  ▗  ▗▘▄█▘ ▝█▖ ▀ ▞▘ 
 ▗█▘  ▐▙▝█  █████▄▄▟████▘             ▐█▙    ▝▀▄▄   ▌▄ ▚   ▀▀▀▞▘            ██████▙ ▐█▌    ▐███▀  ▖ ▗▝ ▗▝ ▐█▖▘ ▗ █▙  ▗▛ 
▗▛▘▗▘ ▐█ ▀▙▟▌  ▟▀▜▜████▀▙     ▐▙     ▄██▛        ▝▀▀▄▄▖                     ██▐▝██▌▖▐█▘    ▐██▙▄▄▙▄▄  ▞▘   █▗▄█▀▘ ▜▙   ▖
▝ ▗▘▗ ▐█  ▐█ ▗▟▌▗▌▐ ▜██▀ ▙    ▝██▄▄▄█▀██▌               ▝                   ▐█▛▞▜█▌ ▟▛     ██▘ ▞▘▞▘ ▄▀  ▖▘ ▟█▘▗   ▖▜▙▖  
  ▛▗▘ ▐█   ▝█▗▛▗▛▗▀▗▟██▌  ▘    ██▛▜██ ▐█▌                                   ▝█▞▄▛▛▖▚█▘    ▗█▘▟▀▗  ▗▛▘ ▗▀▗▄█▛▀█▖ ▗▞▄ ▀▙ ▖
 ▝▗▘ ▞ █▖  ▗██ ▝ █▄█▀▀▜█▖      ▀█▌▝▜█▝▐█▌                                    ▝▜▜▙▗▗▟▌     ▀▗▞▘▖▘▗▟▀  ▄▘ █▘  ▞█▘▄▀▟▚  ▜█ 
 ▗▘ ▞  █▌ ▗█▌▟▙▞█▀▘▖   ▜█▖      ▜▛▚▞ ▗▜█▘                                      ▟▙▙▟▛       ▜▄  ▞▘▘ ▄▛   ▜▙ ▝▐▛▞▚█▛  ▗▟█▌
▄  ▟  ▞▝█▄▚█  ▝▙▛ ▟               ▟▌▗▛▟▛                                       ▝▀▀▘      ▗▖ ▝▚▞▝ ▗▟▙▄▟▛▀▀▀▀▜██▄▛▀  ▄█▘▖▘
▝▙▟▘ ▝  █▌▐▌▖  ▝█▖▘               ▝▀▚▟▛ ▄▖                              ▄▄▄▄▄▄▄▄       ▗▄▜▄▄  ▝▚▄█▀▀          ▀▀█▄█▀▄▘▗ 
 ▟▜▄   ▞▜█▟▌    ▀▙                  ▄▄▞▀▘  ▗▄ ▄                              ▀▀▀▀▀▀▜▙▄▟▛▀▙    ▗█▀▘▄▟▛▀▀██▛▜▙▄▄   ▀█▟▘▞▘▖
 ▘▗▀▙▖▟  ▜▛▗▄▄▟██▛        ▗█▙▖  ▗▄▟▛▀▘     ▐▛▖▝▚▖                                   ▗▄  ▄▄█  ▗█▘ ▟█▘    ▜█▝▌▝▀█▄   ▜█ ▝ 
   ▖▀█▙ ▗▟██▀ ▖▗█▘       ▝▀ ▐█▀▀▀▀         ▟▘▘  ▜                                ▗▟████▀▀    █▘ ▐██     ▐█▐▞▗ ▝▜▙  ▝█▌▞ 
▗   ▟▀▜█▛▘▟██▀▟▛▘▗▄▟█▙▄▄▖   ▀            ▗█▛▄▘ ▟▛                              ▀▀   ▀▘      ▟▌ ▐█▗▞█▙▄▄▟█▌▙▀▗▞ ▄█▌  ▜█▛▛
  ▗▛▐ █▀▜█▟▀▙▖█▛▀▜█▀                  ▐█▛▀▄▛  ▟▘                                          ▗▖█▌ ▟▛ ▄█▀▜▙▝▙▀▗▟▘▐▞▘▝█  ▐██▌
 ▗▛▗▗█▌▄▛▀▜████▙ ▀                      ▜▙ ▞ ▞▘                                       ▗▄▛▀  ▜▙ ▐█▘▐▙ ▄█▘▄▞▚▄▀▘▖▘▗▛  ▟██▌
▗▛▗▘▟█▐▛   ▝▜██▛█▄                       ▝▜▄▝                                       ▄▛▘ ▗▘   █▌▝█▄ ▝▀▀▚▀▙▞ ▗▟▘ ▄█▘ ▗███▌
▛ ▖▟▜█▜▙     ▐██▄▀█▄                                          ▗▄▄█▌              ▄▛▀  ▟▀ ▗▄  ▝█▌▝█▙▛ ▚▞▀ ▄█▛▟▀█▛  ▗████▌
▘▝▐▛▐█▙▀▙▄▄▄▟█▘▐▜▙▖▝▀▙▄                             ▄▄▄▄▄▄▄▟▀▀▀▀▘             ▗▄▛▘ ▗▄▛▘▄▄▛   ▟██▙▖▀▀██▄▄██▙▟▟▛▀ ▗▟█████▌
 ▟█  ███▖▝▀▗▞▚▛▚▄▀█▙▄▝▜█▄▖                   ▐▛▀▀▀▀▀▀▀▀▘                    ▗▝▀  ▗▟█▄▝▜█▘▖ ▖ █▛▌▐▜█▄▄ ▀▀▀▀▀▘ ▄▄▟▀██████▌
▗▜▛   ▜▄▀▜▟▙▀▘▗▛▄▞▘▜█▟▀  ▜█▙▄▄                                            ▖▀  ▗▄█▛▀▘  ▞▗▞▚▀▄▟███▙█▚▛█▜▜█████▜██▙▗██████▘
▘▐▌ ▖  █▙▄▝▀▀▀▙▄█▛▀▀▘  ▗▄▛▀ ▀▀█▙▄▄                                         ▄▄█▀▀      ▄▀▖▚█████████████▛▄▛▄████▘█████▀  
▖  ▟▘  █▚▀▜▙▄▄      ▄▄▟▛▀▗▖▄▘▗▖ ▛▀▜█▄▄                                 ▄▄██▀▘  ▗▗▛▘▖▙▝▗▟██████████▛▟████▛▟████▚▟██▛▀ ▗▞▗
█ ▗▘▞ ▐█▛ ▗ ▝▀▀▀▀▀▀▀▀▙▝▗▄▚▞▗▟▀▄▛▖ ▞ ▀▀▜▙▄▄                        ▄▄▄▛▀██▀▚ ▘▄▐ ▘▗▟▀▗▟█████████▜█▙▟█████████▛███▀▘▖▄█▛▘ 
▛▙▖▟  ▐█▄▗▘▞ ▗  ▗▖ ▗█▘▗▛▚▚▟▜▚▟▛ ▗█▚▟▘▄▛▘▟███▄▖                ▄▄██▀▘▄▐▛▘▗▝▘▗▐▖▘ ▄▛▚▟█▜▜███████▙▟██▛▙██████▛▜██▀▗▄████▜█▘
███▖ ▀▐██▌▌▟▛ ▗▞▘▄▚▛▗▟▛▐▟▀▄▀▟▀▗█▀▟▛▗▛▜▖▜███████▙▄         ▄▟████▀▄▞▚▀ ▄▀ ▄█▝  ▗█████▞▗▚▟ ▟███████▙███▛███▄█▛▘▄▛▚████▚█▛▖
██▜█▟ ▐█▐▙▟▛ ▗▘▗▘▟▀▟█▘▗▛▚▛▚▟▚▟▘▗█▘▐█▐█▗████████████▙▄▄▄▟█████▛▘ ▜▝ ▗▖▘ ▄▛▘▗▄▟██▀▙▛▟▌▞▚▛▗▟███████▟███▚███▀▘▗▟█▘▟████▜██▟▖
██████▖█▗█▚▙▛▚▛▚▛▚█▛▗█▘▞▘▟▀▄▛ ▟█▘▖▐▌▜▛▐██████████▙▟▌▀█▀▀▀████▙▄▄▄▄█▄▄▟███▛▛▛█▛▗▛▚▛▗▛▐▛▄█████████▘▟██▛▀ ▗▟███▚▟████▚██▛▟▌
▖▝▀█████▝▜█▘▟▀▟▀ █▘▟▀▟▘▄▛▗▟▘▐██▀▐▘▐▙▛ ▐███████████▙▄▘█      ▝▀▀▀▀▀██▀▗▄▞▘▄▟▛▚█▚▟▘▟▘▟▛█▘▟▘▗▛██████▀▘ ▗▄██████████████ ▟█▌
███▄▄▛▀██▙▄█▙▛ ▗▀ ▛▗▀▗▟▚▟█▘▟▀▟▘▗▟▌▟█▗▖▐█████████████▟█▘          ▗█▗█▛█▟▜▛▚▟▀▗▛▄█▚█▘▟▚▛ ▟█▄██▛▀  ▗▄█████████████▛▟█▚███▌
███████▙▄▄▛▀▀▀▜█▄▄▄▙▟█▘▐▛ ▝▘▗▀ ▟▙▟▐█▐▘▐█████████████▛ ▖  ▗    ▖ ▗███▙█▜▞▀▟▛▚▞▙▗█▄▛▘▝▚▄▄▟█▀▀▘ ▗▄▄███████████████▛▄█▙▟███▖
█████████████▙▄▄▄  ▀▀▀▀▀▀▀▀▀▀▀█▙██▖█▖▙█████████▀▜█▀▀▀▜███▙▄▞▝▀▀██▚▟▛▜▞▀▄█▜▚█▞▗▄██▙█▀▀▀▀  ▄▄▟██████████████▚▛██▀▐███████▌
████████████████████▄▄▄▄▖      ███▜█▙█▟██████▘▗█▛▘           ▗▟█▟▛▀▟█▄▟██▟█▀▀▀▀▘   ▗▄▄▟██████████████▀████▛▚█▀▐██▛▀▛▚██ 


```
