# gradient-json-minecraft
Python script that generates a Minecraft json string with a linear gradient between two hex codes.

## Usage
Download the repository and open the python file inside. The file automatically closes after printing the ending string, so make sure you open it in an existing terminal.

### Prompts
![image](https://user-images.githubusercontent.com/42397332/159161930-ae0f0e09-66b2-4e0e-80db-ef0c1506f422.png)

**Text:** The string to make into a gradient.

**Color A:** The first colour of the gradient as a hexcode. The gradient is generated left to right, so this will be the leftmost colour. The # is optional.

**Color B:** The second colour of the gradient as a hexcode. The rightmost colour. The # is optional.

**Bold?:** Bold text? Any input other than _true_ (case sensitive) will be considered false.

**Underline?:** Underlined text? Any input other than _true_ (case sensitive) will be considered false.

**Italics?:** Italic text? Any input other than _true_ (case sensitive) will be considered false.

### Output

The program will print a long string of text that you can then paste into any tellraw command or other command that accepts JSON.

![image](https://user-images.githubusercontent.com/42397332/159162049-19eee235-cd6c-42fb-a3ce-b3650fdf505d.png)

![image](https://user-images.githubusercontent.com/42397332/159162081-fbd79a8f-11bc-42c4-be9e-668ff83e4d13.png)
