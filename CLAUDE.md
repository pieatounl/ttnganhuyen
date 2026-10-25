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
- **Luôn cập nhật thumbnail xem trước link khi site thay đổi** (Margot dặn 25.10.2026): đổi headline của trang chủ hoặc của tab My journey / Use Cases / Blog thì vẽ lại `img/og-*.png` tương ứng (mẫu ở `/mnt/project-files/website/thumbnail/`); thêm, sửa bài hoặc đổi ảnh bài thì chạy lại `python3 tools/make-share-pages.py`. Commit chung với thay đổi đó.

## Các file

| Đường dẫn | Nội dung |
| --- | --- |
| `index.html` | Toàn bộ site trong một file: CSS và JS viết trong file, ảnh nhúng base64 (khoảng 1,2 MB) |
| `_headers` | Quy tắc header cho Cloudflare (UTF-8) |
| `favicon.ico`, `apple-touch-icon.png` | Hình bông hoa trong ly coupe, nét trắng trên nền xanh `#8FACD8` |
| `img/chuyen-ke.jpg` | Ảnh bìa bài blog "Chuyện kể" |
| `img/flower-*.png` | Hình vẽ tay gốc của bông hoa ở hero |
| `img/og-image.png` | Ảnh xem trước khi gửi link (1200×630, mẫu B Margot duyệt): "consulting by day & blooming by night" trên nền trắng, 3 đường kẻ nằm đúng chân chữ, ly hoa màu xanh. Khai báo bằng thẻ `og:*` và `twitter:*` trong `<head>`. Nguồn HTML để vẽ lại: `/mnt/project-files/website/thumbnail/og-b.html` |
| `about.html`, `my-journey.html`, `use-cases.html`, `blog.html`, `blog/<id>.html`, `my-journey/<id>.html` | Trang chia sẻ: mỗi trang chỉ chứa thẻ `og:*` riêng rồi chuyển ngay sang `/#/…`. Ảnh xem trước là ảnh đầu tiên của bài (blog: `<img>` đầu trong `<article class="post">`; my journey: trường `img: '…'` trong `WORK` nếu có), không có ảnh thì dùng thumbnail của tab đó (`img/og-my-journey.png`, `img/og-use-cases.png`, `img/og-blog.png`: cùng kiểu với `og-image.png`, headline của tab trên 2 dòng kẻ; vẽ lại bằng `/mnt/project-files/website/thumbnail/og-tab.html` + `ogtabs.js`). Trang About dùng `img/og-image.png`. Tạo bằng `python3 tools/make-share-pages.py`, **chạy lại mỗi khi thêm hoặc sửa bài**. Link gửi đi có ảnh riêng phải ở dạng không có `#`, ví dụ `www.ttnganhuyen.com/blog/chuyen-ke`. Các thẻ `og:*` trỏ về `https://www.ttnganhuyen.com` (bản có www phân giải chắc chắn) (link có `#/` luôn hiện thumbnail gốc, vì các app bỏ qua phần sau `#`) |

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
   - Nút hamburger mở menu xanh toàn màn hình; mỗi tên trong menu nằm trên một dòng (cỡ chữ tự nhỏ lại khi thiếu chỗ).
3. **Hero** `#hero`: tiêu đề "consulting ( thẻ ảnh ) by day & blooming ( chồng thẻ ) by ( ly ) night |".
   - **Thẻ ảnh** `.shot` tỉ lệ 16:9 (máy tính 2.133em × 1.2em; điện thoại giữ chiều rộng 1.95em) gồm 8 thẻ `.slide.scN` (chỉ các vị trí consulting; De Orangerie là việc thuộc horeca nên không có ở đây, chỉ có ở My journey và kệ sách). Mỗi thẻ có dấu `*` xoay tròn, tên đơn vị, vai trò và năm:
     - sc2 HUST · Business Analytics
     - sc6 TEDxBachkhoa · Communications
     - sc5 SoICT Innovation Club · Public Relations
     - sc7 Young Leaders Network · National Project Manager
     - sc4 Maritime Bank · Data Administration
     - sc1 Base.vn · Business Analyst
     - sc3 FPT Telecom International · Account Manager
     - sc8 Hasselt University · Entrepreneurial Governance
   - Thẻ tự chuyển sau mỗi 2,2 giây. Bấm hoặc chạm vào thẻ thì chuyển ngay sang thẻ tiếp theo với hiệu ứng mờ nhanh hơn, và bộ đếm giờ chạy lại từ đầu.
   - **Chồng thẻ** (Flowers / Bartender / Sketching): xoè ra khi rê chuột. Trên màn hình cảm ứng thì chạm để mở hoặc đóng.
   - **Ly coupe** `.sun`: bông hoa mọc lên từ ly cocktail, vẽ dần từng nét. Phía sau đầu hoa, mặt trăng và mặt trời thay nhau xuất hiện.
   - **Bài thơ** (*): thơ của ông nội, chú thích "- Words from my grandfather. Nghệ An, 07 Jan 2006." (Margot gõ "07 Jun"; mình giữ ngày cũ 07/01 là 7 tháng 1, đã hỏi lại Margot).
   - **CTA**: "Grab a drink with me!". Nút cuộn "SCROLL!".
4. **About** `#about`: nhãn "Identity", tiêu đề "four names, one person". Đây là một carousel các mẫu chữ tên, dùng các hàm `replaySpec`, `typeMargot` và hỗ trợ vuốt. Mỗi tên có một đoạn tiếng Anh do Margot tự viết (nhãn xanh: "The Origin:", "The Chosen Self:", "The Persona:"); không sửa câu chữ này. Các chú thích có mũi tên quanh chữ cũng do Margot viết (`SPEC_TXT`); câu dài được bẻ dòng để không đè nhau hay bị đường kẻ cắt qua:
   - Ngân Huyền (Danh, do ông nội đặt; chú thích "The Cosmic Origin of Carbonado")
   - Pie At Ounl (Tự, bắt nguồn từ "Enigma")
   - Margot Tran (Hiệu): các đường kẻ luôn hiện sẵn đủ dài ngay từ đầu, không hiện dần (giống Pie At Ounl: đỉnh dấu, đỉnh chữ hoa, đỉnh chữ thường, chân chữ, chân chữ g; chỉ dài vừa tên; `margotGuides`), rồi tên gõ từng chữ lên đó
   - Mỗi lần vuốt, hiệu ứng chạy lại từ đầu.
5. **Footprints** `#t-work` (nhãn cũ "Where I've lived"): Nghệ An → Hà Nội → Sài Gòn → Hasselt, kèm cờ, dòng "and many more bases to build…" và nút "Your guide to starting fresh!" (Margot đổi từ "Give me some advice!", đuôi "!" giữ theo quy tắc CTA). Hai bản đồ Việt Nam và Bỉ nằm hai bên tiêu đề, đã căn đối xứng hai bên màn hình ở mọi chiều rộng từ 981px (đo phần nét vẽ, lệch ≤3px).
6. **The Craft** (nhãn cũ "Where I've worked") `#t-projects`: tiêu đề "work that" + chữ đổi dần (`#rot2`): untangles complexity / sparks conversations / bridges borders (Margot viết). kệ sách kéo ngang được, xếp theo thời gian. Tên gáy sách nhỏ, nhẹ, căn lề dưới; hàm `fitBooks` chỉ thu nhỏ hoặc bẻ 2 dòng khi tên quá dài. Dòng "Every step has a story" dẫn tới `#/my-journey`.
7. **The circles of my life** `#t-community`: sáu vòng tròn Business, Flowers, Nature, Cocktails, Technology, Sketching. Bốn vòng sở thích dùng ảnh của Margot đã phủ màu xanh. Khi cuộn tới, các vòng dàn thành hàng thì ảnh tự hiện (như lúc rê chuột); cuộn tiếp, vòng dạt ra hai bên thì trở lại nền trắng đục (`--ph` trong `ecoFrame`). Nút "Let's connect!".
8. **My untold stories** `#t-stories`: ba tờ giấy note (4 names / 4 loves / 4 cities).
   - Bấm vào thì các tờ dạt sang hai bên rồi về lại chỗ cũ.
   - Từ 761px trở lên các tờ giấy note luôn xoè quạt và căn giữa (chỉ xếp dọc trên điện thoại ≤760px). Dòng "Click to uncover more!" nằm bên trái vùng giấy note dạt ra khi cửa sổ ≥1200px, nên không bị che; hẹp hơn thì nằm dưới các tờ giấy, căn giữa.
   - Nút "Read the stories!".
9. Câu **I believe…**, rồi phần **Contact** ("let's grab the next drink", nút "Ready when you are!").
10. **Footer** (nền tối):
    - Chữ "margot tran".
    - Liên kết tới các trang trong site.
    - LinkedIn, Instagram, Facebook.
    - Ngay dưới chữ "margot tran" là đồng hồ `#here-now`: chỉ giờ "HH:MM:SS GMT+X" (không ngày, không địa điểm), cùng kiểu chữ với "margot tran" nhưng nhỏ hơn, nền trắng như chữ đang được bôi chọn. Theo múi giờ của chính thiết bị đang xem, cập nhật mỗi giây, tự đổi khi thiết bị sang múi giờ khác.
    - Dòng nhỏ "EST. 2002 · Margot · Ngân Huyền · pie.at.ounl" (năm sinh của Margot, thay cho ©).

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

- Không có bộ test. Trước khi commit, mở `index.html` bằng Playwright (đã có sẵn Chromium) ở hai khổ rộng 390px và 1440px, và thêm các cỡ cửa sổ giữa chừng khi sửa bố cục (ví dụ 768×1024, 918×693, 1024×768, 1180×640): web phải co giãn liền mạch khi Margot kéo đổi kích thước cửa sổ trên máy tính, không chồng chữ, không tràn mép, bản đồ và giấy note luôn căn giữa.
- Kiểm tra không có `pageerror`, và chụp màn hình phần vừa sửa.
