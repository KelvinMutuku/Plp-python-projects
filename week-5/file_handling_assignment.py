me, content):
      """
        Writes content to a file in write mode ('w').

          Args:
                filename: The name of the file to write to.
                      content: The content to write to the file (string or list of strings).
                        """
                          try:
                                  with open(filename, "w") as file:
                                            if isinstance(content, list):
                                                        file.writelines(content)
                                                              else:
                                                                          file.write(content + "\n")
                                                                              print(f"Successfully wrote to {filename}")
                                                                                except (IOError, FileNotFoundError) as e:
                                                                                        print(f"Error writing to {filename}: {e}")

                                                                                        def read_from_file(filename):
                                                                                              """
                                                                                                Reads the contents of a file and displays them on the console.

                                                                                                  Args:
                                                                                                        filename: The name of the file to read from.
                                                                                                          """
                                                                                                            try:
                                                                                                                    with open(filename, "r") as file:
                                                                                                                              content = file.read()
                                                                                                                                    print(f"Contents of {filename}:\n{content}")
                                                                                                                                      except (IOError, FileNotFoundError) as e:
                                                                                                                                              print(f"Error reading from {filename}: {e}")

                                                                                                                                              def append_to_file(filename, content):
                                                                                                                                                    """
                                                                                                                                                      Appends content to a file in append mode ('a').

                                                                                                                                                        Args:
                                                                                                                                                              filename: The name of the file to append to.
                                                                                                                                                                    content: The content to append to the file (string or list of strings).
                                                                                                                                                                      """
                                                                                                                                                                        try:
                                                                                                                                                                                with open(filename, "a") as file:
                                                                                                                                                                                          if isinstance(content, list):
                                                                                                                                                                                                      file.writelines(content)
                                                                                                                                                                                                            else:
                                                                                                                                                                                                                        file.write(content + "\n")
                                                                                                                                                                                                                            print(f"Successfully appended to {filename}")
                                                                                                                                                                                                                              except (IOError, PermissionError) as e:
                                                                                                                                                                                                                                      print(f"Error appending to {filename}: {e}")

                                                                                                                                                                                                                                      # Create the file
                                                                                                                                                                                                                                      initial_content = [
                                                                                                                                                                                                                                                  "This is the first line of text.\n",
                                                                                                                                                                                                                                                      "Here's another line with a number: 42\n",
                                                                                                                                                                                                                                                          "And a final line for now.\n"
                                                                                                                                                                                                                                                          ]
                                                                                                                                                                                                                                      write_to_file("my_file.txt", initial_content)

                                                                                                                                                                                                                                      # Read and display the file contents
                                                                                                                                                                                                                                      read_from_file("my_file.txt")

                                                                                                                                                                                                                                      # Append additional content
                                                                                                                                                                                                                                      additional_content = [
                                                                                                                                                                                                                                                  "Appending some more text...\n",
                                                                                                                                                                                                                                                      "Numbers are fun! 10.5\n",
                                                                                                                                                                                                                                                          "This is the final appended line.\n"
                                                                                                                                                                                                                                                          ]
                                                                                                                                                                                                                                      append_to_file("my_file.txt", additional_content)

                                                                                                                                                                                                                                      # Read and display the file contents again (including appended data)
                                                                                                                                                                                                                                      read_from_file("my_file.txt")

