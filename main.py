import instaloader

# Create an instance of Instaloader
L = instaloader.Instaloader()

# Log in (if required)
# L.login("your_username", , "your_password")

# Prompts the user to enter the name of the profile they are interested in
username = input("Please enter your Instagram profile name: ")

# Obtém os detalhes do perfil
profile = instaloader.Profile.from_username(L.context, username)

print("User name: ", profile.username)
print("Name: ", profile.full_name)
print("Biography: ", profile.biography)
print("Number of followers: ", profile.followers)
print("External URL: ", profile.external_url)
print("Profile photo url: ", profile.profile_pic_url)
print("Number of posts: ", profile.mediacount)
