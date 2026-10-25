# ttnganhuyen.com — Website cá nhân của Margot

Website cá nhân của Trần Thị Ngân Huyền (Huyen Tran / Margot), bám sát phong cách của untold.site/en.
Khẩu hiệu: "consulting by day, blooming by night".

## Quy tắc của chủ site (luôn tuân theo)

- Margot viết tiếng Việt, nên trả lời Margot bằng tiếng Việt.
- Commit thẳng lên `main`. Không tạo nhánh mới và không xoá file khác trong repo.
- Cloudflare Pages tự deploy từ `main`, không có bước build.
- Không bao giờ in email liên hệ ra trang hay trong tin nhắn. Form gửi qua Web3Forms, người xem chỉ thấy "Submitted".
- Không sửa câu chữ trong các bài blog của Margot (`#/blog/...`).
- Giữ `<meta charset="utf-8">` trong `index.html`. File `_headers` cũng ép UTF-8. Thiếu khai báo này thì tiếng Việt bị lỗi font.
- Tên tiếng Anh là **Margot** (không dùng "Hailey").

## Các file

| Đường dẫn | Nội dung |
| --- | --- |
| `index.html` | Toàn bộ site trong một file: CSS và JS viết trong file, ảnh nhúng base64 (khoảng 1,2 MB) |
| `_headers` | Quy tắc header cho Cloudflare (UTF-8) |
| `favicon.ico`, `apple-touch-icon.png` | Hình bông hoa trong ly coupe, nét trắng trên nền xanh `#8FACD8` |
| `img/chuyen-ke.jpg` | Ảnh bìa bài blog "Chuyện kể" |
| `img/flower-*.png` | Hình vẽ tay gốc của bông hoa ở hero |

## Hệ thống thiết kế

- Nền trắng tinh. Màu nhấn xanh `#8FACD8`. Biến CSS của màu này vẫn tên là `--orange` vì lý do lịch sử. Chữ nhỏ màu nhấn dùng `--accent-ink` `#4d6f9f`.
- Khoảng cách giống untold: lề hai bên rộng, các phần gọn, khi cuộn chủ yếu là tiêu đề lớn.
- Các đường kẻ mảnh, mờ nằm đúng trên chân chữ (baseline). JS tính vị trí các đường này (`layoutHero`, `baselineRules`). Đường kẻ không bao giờ cắt qua chữ chú thích.
- Nút (`.btn`) nhỏ gọn. **Mọi nút CTA đều kết thúc bằng "!"**, cả tiếng Anh lẫn tiếng Việt.
- Dấu nháy (`|`) không nhấp nháy. Nó chỉ hiện trong lúc chữ đang gõ, gõ xong thì dừng.
- Header ghi "( EN, VI )" nghĩa là web dùng cả tiếng Anh lẫn tiếng Việt, **không phải nút chuyển ngôn ngữ**. Chức năng chuyển đổi sẽ làm sau: tiếng Việt đã soạn sẵn trong thuộc tính `data-vi` (`setLang`), đang khoá bằng `VI_ON = false`.
- Trên điện thoại (≤720px), mọi thứ phải vừa chiều ngang màn hình, không cuộn ngang.

## Các trang (router theo hash, hàm `route()`)

Đường dẫn trùng tên tab: `#/about` (trang chủ; bấm vào tên ở góc trái cũng về đây), `#/my-journey`, `#/use-cases`, `#/blog`. Tên view bên trong vẫn là `work`, `consulting`, `stories` (bảng `PUB`/`VIEW` trong `route()`); link cũ `#/work`, `#/consulting`, `#/stories` tự chuyển sang tên mới. Mỗi route ứng với một `<div class="view" id="v-…">`. Thứ tự trong nav và menu: **About, My journey (`#/work`), Use Cases (`#/consulting`), Blog, contact**. Tiếng Việt: Giới thiệu, Hành trình, Tình huống, Blog.

| Hash | View | Nội dung |
| --- | --- | --- |
| `#/about` (hoặc `#/`) | `v-home` | Trang About (trang chủ), chi tiết ở phần dưới |
| `#/my-journey` | `v-work` | Danh sách vị trí, chỉ có chữ, lấy từ mảng `WORK`. Chưa có ảnh hay logo, sau này sẽ thêm output từng dự án |
| `#/my-journey/<id>` | `v-case` | Trang chi tiết, `fillCase(id)` lấy dữ liệu từ `WORK`: tên đơn vị, năm, vai trò, các đoạn `p`, năng lực `caps`, các slide tạm `slides` |
| `#/use-cases` | `v-consulting` | "use cases coming soon": 01 Strategy, 02 Data, 03 Process |
| `#/blog` | `v-stories` | Trang blog ("coming soon", nút Follow me on Instagram) |
| `#/blog/<id>` | `v-post` | Các bài blog, ví dụ `post-chuyen-ke` (tiếng Việt, 24.10.2026) |
| contact | hộp thoại `#talk` | Form liên hệ / xin lời khuyên (các nút `.talk-open`, `data-mode="contact"` hoặc `"advice"`) |

## Trang chủ (`v-home`), từ trên xuống

1. **Màn hình chờ**: chữ "h" chữ ký của Margot được vẽ dần trên nền xanh.
2. **Header**:
   - Góc trái là "Huyen Tran / Margot"; "Margot" và dấu nháy màu xanh.
   - Nav có nhãn thu lại còn chữ cái đầu.
   - Nhãn "( EN, VI )" (chỉ để hiển thị, không bấm được).
   - Nút hamburger mở menu xanh toàn màn hình.
3. **Hero** `#hero`: tiêu đề "consulting ( thẻ ảnh ) by day & blooming ( chồng thẻ ) by ( ly ) night |".
   - **Thẻ ảnh** `.shot` tỉ lệ 16:9 (máy tính 2.133em × 1.2em; điện thoại giữ chiều rộng 1.95em) gồm 9 thẻ `.slide.scN`. Mỗi thẻ có dấu `*` xoay tròn, tên đơn vị, vai trò và năm:
     - sc2 HUST · Business Analytics
     - sc6 TEDxBachkhoa · Communications
     - sc5 SoICT Innovation Club · Public Relations
     - sc7 Young Leaders Network · National Project Manager
     - sc4 Maritime Bank · Data Administration
     - sc1 Base.vn · Business Analyst
     - sc3 FPT Telecom International · Account Manager
     - sc8 Hasselt University · Entrepreneurial Governance
     - sc9 De Orangerie · Barback
   - Thẻ tự chuyển sau mỗi 2,2 giây. Bấm hoặc chạm vào thẻ thì chuyển ngay sang thẻ tiếp theo với hiệu ứng mờ nhanh hơn, và bộ đếm giờ chạy lại từ đầu.
   - **Chồng thẻ** (Flowers / Bartender / Sketching): xoè ra khi rê chuột. Trên màn hình cảm ứng thì chạm để mở hoặc đóng.
   - **Ly coupe** `.sun`: bông hoa mọc lên từ ly cocktail, vẽ dần từng nét. Phía sau đầu hoa, mặt trăng và mặt trời thay nhau xuất hiện.
   - **Bài thơ** (*): thơ của ông nội, chú thích "My grandfather, Nghệ An, 07/01/2006".
   - **CTA**: "Grab a drink with me!".
4. **About** `#about`: "four names, one person". Đây là một carousel các mẫu chữ tên, dùng các hàm `replaySpec`, `typeMargot` và hỗ trợ vuốt:
   - Ngân Huyền (Danh, do ông nội đặt; chú thích "The Cosmic Origin of Carbonado")
   - Pie At Ounl (Tự, bắt nguồn từ "Enigma")
   - Margot Tran (Hiệu): một đoạn ngắn của các đường kẻ hiện ra trước (giống Pie At Ounl: đỉnh dấu, đỉnh chữ hoa, đỉnh chữ thường, chân chữ, chân chữ g; `margotGuides`), rồi các đường chạy dài theo từng chữ khi tên được gõ, dừng ở cuối tên
   - Mỗi lần vuốt, hiệu ứng chạy lại từ đầu.
5. **Where I've lived** `#t-work`: Nghệ An → Hà Nội → Thành phố Hồ Chí Minh → Hasselt, kèm cờ, và nút "Give me some advice!".
6. **Where I've worked** `#t-projects`: kệ sách kéo ngang được, xếp theo thời gian. Tên gáy sách nhỏ, nhẹ, căn lề dưới; hàm `fitBooks` chỉ thu nhỏ hoặc bẻ 2 dòng khi tên quá dài. Dòng "Every step has a story" dẫn tới `#/my-journey`.
7. **The circles of my life** `#t-community`: sáu vòng tròn Business, Flowers, Nature, Cocktails, Technology, Sketching. Bốn vòng sở thích dùng ảnh của Margot đã phủ màu xanh. Nút "Let's connect!".
8. **My untold stories** `#t-stories`: ba tờ giấy note (4 names / 4 loves / 4 cities).
   - Bấm vào thì các tờ dạt sang hai bên rồi về lại chỗ cũ.
   - Dòng "Click to uncover more!" nằm bên trái vùng giấy note dạt ra, nên không bị che.
   - Nút "Read the stories!".
9. Câu **I believe…**, rồi phần **Contact** ("let's grab the next drink", nút "Ready when you are!").
10. **Footer** (nền tối):
    - Chữ "margot tran".
    - Liên kết tới các trang trong site.
    - LinkedIn, Instagram, Facebook.

## Ảnh

- Ảnh là ảnh của Margot, nhúng dạng base64 data URI.
- Dùng nguyên khung ảnh Margot đã cắt, không tự cắt lại.
- Ảnh ở hero và ở các vòng tròn được phủ màu xanh (duotone) bằng PIL: `ImageOps.colorize(autocontrast(gray, cutoff=1), black='#1d2a40', mid='#8facd8', white='#f2f6fc', midpoint=110)`.
- Thẻ ảnh ở hero có thêm lớp gradient tối để chữ dễ đọc.

## Liên kết cá nhân

- Substack: https://substack.com/@lofopmartii
- LinkedIn: https://www.linkedin.com/in/ttnganhuyen
- Instagram: https://www.instagram.com/pie.at.ounl
- Facebook: https://www.facebook.com/pie.at.ounl/

## Kiểm tra trước khi commit

- Không có bộ test. Trước khi commit, mở `index.html` bằng Playwright (đã có sẵn Chromium) ở hai khổ rộng 390px và 1440px.
- Kiểm tra không có `pageerror`, và chụp màn hình phần vừa sửa.
