class SocialMediaProfile:
    def __init__(self, username):
        self.username = username
        self.posts = []

    #Add a display_timeline(self) method
    def display_timeline(self):
        print(f'timeline: {self.username}')
        print('====================')
        for i, post in enumerate(self.posts, start = 1):
            print(f"{i}, {post}")
    def add_post(self, content):
        self.posts.append(content)
        print(f"{self.username}, add new post{content}")

#main program:
def main():
    #creat user "johndoe"
    user = SocialMediaProfile("johndoe")
    
    #add posts
    user.add_post("Hello, world!")
    user.add_post("Had a great day at the park!")
    user.add_post("What's up, Natalie? How are you?")

    # Display the timeline
    user.display_timeline()

if __name__ == "__main__":
    main()
