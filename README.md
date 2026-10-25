# KeyboardSounder

동물의 숲 스타일 키보드 타이핑 사운드 앱입니다. **macOS / Windows** 한 저장소에서 빌드·배포합니다.

## 다운로드

[Releases](https://github.com/joeyycho/acnh_keyboard_sounder/releases)에서 OS에 맞는 zip을 받으세요.

| OS | 파일 | 실행 |
| --- | --- | --- |
| macOS | `KeyboardSounder-macos.zip` | 압축 해제 후 `KeyboardSounder.app` 실행 |
| Windows | `KeyboardSounder-windows.zip` | 압축 해제 후 `KeyboardSounder.exe` 실행 |

태그(`v0.2.0` 등)를 푸시하면 GitHub Actions가 두 플랫폼 빌드를 만들고 Release에 올립니다.

---

## macOS 보안 / 권한

처음 실행 시 "알 수 없는 개발자" 경고가 날 수 있습니다.

1. 실행을 시도한 뒤
2. **시스템 설정 → 개인정보 보호 및 보안**에서 차단된 앱 **허용**
3. **입력 모니터링(Input Monitoring)** 권한을 `KeyboardSounder`에 부여

권한 없이는 키 입력을 듣지 못합니다.

## Windows 보안

- Windows Defender SmartScreen이 뜨면 **추가 정보 → 실행**
- 일부 환경에서는 관리자 권한이 필요할 수 있습니다

## 사용 방법

1. 앱을 실행합니다.
2. 볼륨 슬라이더로 키음 크기를 조절합니다.
3. 키보드를 치면 사운드가 재생됩니다.

별도 Python 설치는 필요 없습니다.

## 지원 키

- 영어 알파벳 (a–z), 숫자 (0–9)
- 특수문자 (`!@#$%^&*()_+` 등)
- Space, Enter, Tab, Backspace, Shift, Caps Lock, Esc

## 개발자: 로컬 실행

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

## 개발자: 바이너리 빌드

```bash
pip install -r requirements-dev.txt
./scripts/build.sh
# 또는: python -m PyInstaller --noconfirm --clean KeyboardSounder.spec
```

산출물:

- macOS → `dist/KeyboardSounder.app`
- Windows → `dist/KeyboardSounder.exe`

## CI

`.github/workflows/build-release.yml`

- `workflow_dispatch`: macOS / Windows 아티팩트 빌드 (Actions에서 다운로드)
- `v*` 태그 푸시: 빌드 후 GitHub Release에 zip 첨부

```bash
git tag v0.2.0
git push origin v0.2.0
```

---

감사합니다.
