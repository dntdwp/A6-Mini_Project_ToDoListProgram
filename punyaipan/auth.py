from pathlib import Path
import json
import hashlib

# user.json akan disimpan di folder project root
USERS_FILE = Path(__file__).resolve().parent.parent / "user.json"


def load_users():
	if USERS_FILE.exists():
		try:
			return json.loads(USERS_FILE.read_text(encoding="utf-8"))
		except Exception:
			return {}
	return {}


def save_users(users: dict):
	USERS_FILE.write_text(json.dumps(users, indent=2, ensure_ascii=False), encoding="utf-8")


def _hash_password(password: str) -> str:
	return hashlib.sha256(password.encode("utf-8")).hexdigest()


def validate_username(username: str) -> bool:
	return bool(username and username.strip())


def validate_password(password: str) -> bool:
	return len(password or "") >= 6


def register_user(username: str, password: str):
	username = (username or "").strip()
	if not validate_username(username):
		return False, "Username tidak boleh kosong"
	if not validate_password(password):
		return False, "Password minimal 6 karakter"

	users = load_users()
	if username in users:
		return False, "Username sudah terdaftar"

	users[username] = {"password": _hash_password(password)}
	save_users(users)
	return True, "Registrasi berhasil"


def login_user(username: str, password: str):
	users = load_users()
	if username not in users:
		return False, "Username tidak ditemukan"
	if users[username].get("password") != _hash_password(password):
		return False, "Password salah"
	return True, "Login berhasil"

