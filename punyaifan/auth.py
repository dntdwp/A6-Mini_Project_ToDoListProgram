from punyaipan import auth
import getpass


def main():
	while True:
		print("\nPILIHAN:")
		print("1. Registrasi")
		print("2. Login")
		print("3. Keluar")
		choice = input("Pilih (1/2/3): ").strip()

		if choice == "1":
			username = input("Username: ").strip()
			password = getpass.getpass("Password: ")
			ok, msg = auth.register_user(username, password)
			print(msg)

		elif choice == "2":
			username = input("Username: ").strip()
			password = getpass.getpass("Password: ")
			ok, msg = auth.login_user(username, password)
			print(msg)
			if ok:
				print(f"Selamat datang, {username}!")

		elif choice == "3":
			print("Keluar.")
			break

		else:
			print("Pilihan tidak dikenal.")


if __name__ == "__main__":
	main()

