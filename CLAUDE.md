# ttnganhuyen.com — Website cá nhân của Margot

Website cá nhân của Trần Thị Ngân Huyền (Huyen Tran / Margot), bám sát phong cách của untold.site/en.
Khẩu hiệu: "consulting by day, blooming by night".

## Quy tắc của chủ site (luôn tuân theo)

- Margot viết tiếng Việt, nên trả lời Margot bằng tiếng Việt.
- Commit thẳng lên `main`. Không tạo nhánh mới và không xoá file khác trong repo.
- Cloudflare Pages tự deploy từ `main`, không có bước build.
- Không bao giờ in email liên hệ ra trang hay trong tin nhắn. Form gửi qua Web3Forms, người xem chỉ thấy "Submitted".
- Không sửa câu chữ trong các bài blog của Margot (`#/words/...`).
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
| `abt-me.html`, `chapters.html`, `cases.html`, `words.html`, `words/<id>.html`, `chapters/<id>.html` (cùng các trang cũ `me`, `about`, `profile`, `my-journey`, `use-cases`, `blog` giữ lại để link đã gửi vẫn chạy, canonical trỏ về tên mới) | Trang chia sẻ: mỗi trang chỉ chứa thẻ `og:*` riêng rồi chuyển ngay sang `/#/…`. Ảnh xem trước là ảnh đầu tiên của bài (blog: `<img>` đầu trong `<article class="post">`; my journey: trường `img: '…'` trong `WORK` nếu có), không có ảnh thì dùng thumbnail của tab đó (`img/og-my-journey.png`, `img/og-use-cases.png`, `img/og-blog.png`: cùng kiểu với `og-image.png`, headline của tab trên 2 dòng kẻ; vẽ lại bằng `/mnt/project-files/website/thumbnail/og-tab.html` + `ogtabs.js`). Trang Abt me dùng `img/og-image.png`. Tạo bằng `python3 tools/make-share-pages.py`, **chạy lại mỗi khi thêm hoặc sửa bài**. Link gửi đi có ảnh riêng phải ở dạng không có `#`, ví dụ `www.ttnganhuyen.com/words/chuyen-ke`. Các thẻ `og:*` trỏ về `https://www.ttnganhuyen.com` (bản có www phân giải chắc chắn) (link có `#/` luôn hiện thumbnail gốc, vì các app bỏ qua phần sau `#`) |

## Hệ thống thiết kế

- Nền trắng tinh. Màu nhấn xanh `#8FACD8`. Biến CSS của màu này vẫn tên là `--orange` vì lý do lịch sử. Chữ nhỏ màu nhấn dùng `--accent-ink` `#4d6f9f`.
- Khoảng cách giống untold: lề hai bên rộng, các phần gọn, khi cuộn chủ yếu là tiêu đề lớn.
- Các đường kẻ mảnh, mờ nằm đúng trên chân chữ (baseline). JS tính vị trí các đường này (`layoutHero`, `baselineRules`). Đường kẻ không bao giờ cắt qua chữ chú thích.
- Nút (`.btn`) nhỏ gọn. **Mọi nút CTA đều kết thúc bằng "!"**, cả tiếng Anh lẫn tiếng Việt. Ngoại lệ do Margot tự viết (kết thúc bằng "?"): "Your guide to starting fresh?" và nút trang Cases "what's on your whiteboard?" (26.10.2026; từng là "Have a similar puzzle on your desk? Let's brainstorm!").
- Dấu nháy (`|`) không nhấp nháy. Nó chỉ hiện trong lúc chữ đang gõ, gõ xong thì dừng.
- Header ghi "( EN, VI )" nghĩa là web dùng cả tiếng Anh lẫn tiếng Việt, **không phải nút chuyển ngôn ngữ**. Chức năng chuyển đổi sẽ làm sau: tiếng Việt đã soạn sẵn trong thuộc tính `data-vi` (`setLang`), đang khoá bằng `VI_ON = false`.
- Trên điện thoại (≤720px), mọi thứ phải vừa chiều ngang màn hình, không cuộn ngang.
- **Khoảng cách giữa các section phải đồng đều** (Margot dặn 26.10.2026): nhãn của mỗi section nằm cách phần trước khoảng 90–100px. The Spectrum là phần ghim cao 260vh nên dùng `.eco-a { justify-content: flex-start; padding-top: 155px }` (nhãn The Spectrum cách The Craft ~90–100px ở mọi cỡ cửa sổ, đã đo ở 390–1920px) và `.eco-b { padding-top: clamp(0px, calc(30vh - 130px), 140px) }` (nút "Read the unfiltered me!" phải nằm trọn trong màn hình, cách mép dưới ≥50px, kể cả cửa sổ thấp 640px) để kéo chữ lớn lên và nút xuống, `.eco { margin-top: -100px }` (kéo phần ghim lên sát The Craft; `.eco` để `pointer-events: none` nên không chặn link kệ sách), còn `.believe` có `min-height` tính theo chiều cao ly (`max(min(64vh, 540px), cao ly + 124px)`) và `padding-bottom: 96px` để chân ly **không bị cắt** (`overflow: hidden`) và cách phần Contact tương đương các section khác. Hàm `evenEcoGap()` đặt `margin-bottom` âm cho `.eco` để khoảng từ nút "Read the unfiltered me!" (điện thoại: từ hàng vòng tròn) tới nhãn "The Conversation" luôn ~96px ở mọi cỡ cửa sổ. Sau khi đổi bố cục, chụp các điểm nối About→Footprints→The Craft→The Spectrum→câu "Great ideas…" để so khoảng cách.
- **Không để chữ nhảy**: mọi dòng gõ hoặc đổi chữ (tên thành phố, `#rot2`, câu "Great ideas…") phải giữ sẵn chỗ bằng `min-height`, để phần bên dưới không dịch lên xuống. Khi sửa, chạy thử trên 360/390/430/768px, lấy vị trí các section theo thời gian (đứng yên mới đạt) và rà lại cả trang About.

## Các trang (router theo hash, hàm `route()`)

Đường dẫn trùng tên nhãn nav (26.10.2026): `#/abt-me` (trang chủ; bấm vào tên ở góc trái cũng về đây; Margot đổi từ `#/me` 26.10.2026), `#/chapters`, `#/cases`, `#/words`. Tên view bên trong vẫn là `work`, `consulting`, `stories` (bảng `PUB`/`VIEW`/`OLDNAME` trong `route()`); mọi link cũ (`#/me`, `#/about`, `#/my-journey`, `#/use-cases`, `#/blog`, `#/work`, `#/consulting`, `#/stories`, kể cả có `/<id>`) tự chuyển sang tên mới bằng `history.replaceState`. **Đổi nhãn nav nữa thì đổi luôn đường dẫn, bảng này và `tools/make-share-pages.py`.** Mỗi route ứng với một `<div class="view" id="v-…">`. Thứ tự trong nav và menu (nhãn nav ghi "Abt me", đường dẫn `#/abt-me`): **Me, Chapters (`#/work`), Cases (`#/consulting`), Words (Blog), contact**. Nhãn nav và menu: Margot đổi About thành "Profile", rồi "Me" và My journey thành "Chapters" (26.10.2026; từng thử "Trajectory"); tiêu đề trang chia sẻ của My journey ghi "Chapters". Use Cases đổi thành "Cases" (từng thử "Playbook") và Blog thành "Words" (cùng ngày; từng thử "Off Script"); `data-vi` của hai nhãn này giữ nguyên bản cũ. Tiêu đề lớn trong từng trang vẫn dùng headline cũ. Tiếng Việt: Giới thiệu, Hành trình, Tình huống, Blog. Ghi chú về hero: khi tiêu đề xuống 4 dòng và bài thơ rơi xuống dưới, `layoutHero` đẩy bài thơ cách chồng thẻ ít nhất 44px (không chồng lên thẻ).

| Hash | View | Nội dung |
| --- | --- | --- |
| `#/abt-me` (hoặc `#/`) | `v-home` | Trang About (trang chủ), chi tiết ở phần dưới |
| `#/chapters` | `v-work` | Nhãn "Tracing the dots", tiêu đề "making sense of / the moving parts" (Margot viết 26.10.2026; thumbnail `img/og-my-journey.png` đã vẽ lại). Cuối trang: nhãn "Turning the page", tiêu đề "let's dive into / the puzzles" (Margot sửa 26.10.2026; gõ chữ có dấu nháy khi cuộn tới, dùng `data-type`, giữ chỗ bằng `min-height`), nút "Step inside the cases!" dẫn tới `#/cases`. Danh sách chia 5 nhóm theo mảng `GROUPS` (Margot chốt 31.10.2026): ( 01 ) Education: mom, hust; ( 02 ) Work: fti, base, msb; ( 03 ) Clubs: tedx, sinno, yln; ( 04 ) Courses: 6 khoá ngắn (cắm hoa Tigon, data science FTU, bartending Nguyễn Trường Tộ, graphic design ColorMe, Hán ngữ Thanh Mai HSK, tiếng Dutch PCVO) chỉ ghi tên khoá và nơi học, nằm trong `GROUPS[].list`, **không** có trong `WORK` nên không hiện ở kệ sách và không có trang chi tiết; ( 05 ) Side gigs: orangerie. `LIST_ORDER` suy ra từ `GROUPS`; kệ sách ở trang chủ vẫn theo thời gian; tiêu đề lớn mỗi mục là tên role (`role`), không phải tên gáy sách (`title`), và cột trái mỗi mục ghi tên đơn vị, năm, rồi địa điểm bên dưới năm (trường `loc` trong `WORK`; Margot dặn 27.10.2026; Maritime Bank và YLN là mình suy ra, cần Margot xác nhận); nút mỗi mục "Flip to this chapter! →" (Margot chốt 27.10.2026), không có dòng "Told by Margot" (bỏ 27.10.2026 vì thừa; trang chi tiết vẫn dùng `title`); tên đơn vị viết đầy đủ (Maritime Bank, Young Leaders Network, SOICT Innovation Club, TEDx Bachkhoa, Hanoi University of Science and Technology). Chưa có ảnh hay logo, sau này sẽ thêm output từng dự án |
| `#/chapters/basevn` | `v-base` | Portfolio Base.vn (31.10.2026, Margot duyệt; `#/chapters/base` tự chuyển, WORK id vẫn là `base`, `slug()` đổi tên). Tiêu đề "automating the core". 6 phần: The why, The blocks (12 khối), Services that talk (sơ đồ Service A/B vẽ SVG), Case study PR → PO (bộ đếm số demo), In the house, The guide. Viết lại theo hướng BA logic (vấn đề, mô hình, quy tắc, logic, case), không dùng ảnh chụp slide: mọi hình đều vẽ SVG/HTML từ nội dung bộ HDSD Base Service Margot tự soạn (Canva `DAHWt6himAE`); không có số liệu bịa. Thumbnail `img/og-basevn.png` |
| `#/chapters/<id>` | `v-case` | Trang chi tiết, `fillCase(id)` lấy dữ liệu từ `WORK`: tên đơn vị, năm, vai trò, các đoạn `p`, năng lực `caps`, các slide tạm `slides` |
| `#/cases` | `v-consulting` | Nhãn "In practice", tiêu đề "putting the pieces / together" (Margot viết 26.10.2026, bỏ đoạn mô tả bên dưới; thumbnail `img/og-use-cases.png` đã vẽ lại theo tiêu đề này): ba thẻ "Coming soon" (Margot chọn 27.10.2026, thứ tự này): 01 Structure "LEGOs in business processes", 02 Curiosity "Ending with \"Why\"", 03 Adoption "Go-live is day one"; nhãn Strategy/Data/Process cũ bỏ vì không hợp chủ đề |
| `#/words` | `v-stories` | Trang blog ("coming soon", nhãn "stories & notes", nút "Say hi on IG!", ngày bài viết chỉ ghi `( 24.10.2026 )` không có chữ Blog (Margot đổi 26.10.2026); nhãn "SCROLL!" ở Chapters có "!") |
| `#/words/<id>` | `v-post` | Các bài blog, ví dụ `post-chuyen-ke` (tiếng Việt, 24.10.2026) |
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
   - **Bài thơ** (*): thơ của ông nội, chú thích "- Words from my grandfather. Nghệ An, 07/01/2006." (ngày/tháng/năm, Margot chốt).
   - **CTA**: "Grab a drink with me!". Nút cuộn "SCROLL!".
4. **About** `#about`: nhãn "Identity", tiêu đề "four names, one person". Đây là một carousel các mẫu chữ tên, dùng các hàm `replaySpec`, `typeMargot` và hỗ trợ vuốt. Mỗi tên có một đoạn tiếng Anh do Margot tự viết (nhãn xanh: "The Origin:", "The Chosen Self:", "The Persona:"); không sửa câu chữ này. Các chú thích có mũi tên quanh chữ cũng do Margot viết (`SPEC_TXT`); câu dài được bẻ dòng để không đè nhau hay bị đường kẻ cắt qua:
   - Ngân Huyền (Danh, do ông nội đặt; chú thích "The Cosmic Origin of Carbonado")
   - Pie At Ounl (Tự, bắt nguồn từ "Enigma")
   - Margot Tran (Hiệu): đoạn giải thích (Hiệu) chỉ hiện sau khi tên gõ xong (class `told`); các đường kẻ luôn hiện sẵn đủ dài ngay từ đầu, không hiện dần (giống Pie At Ounl: đỉnh dấu, đỉnh chữ hoa, đỉnh chữ thường, chân chữ, chân chữ g; chỉ dài vừa tên; `margotGuides`), rồi tên gõ từng chữ lên đó
   - Mỗi lần vuốt, hiệu ứng chạy lại từ đầu.
   - Các vòng tròn chú thích (Ngân Huyền: chân chữ n cuối; Pie At Ounl: đỉnh chữ n và đuôi chữ e) được đặt theo điểm ảnh thật của chữ (`strokeRight`), không đoán theo tỉ lệ; mũi tên "The true origin" thẳng hàng với mũi tên kích thước (Margot dặn 31.10.2026).
5. **Footprints** `#t-work` (nhãn cũ "Where I've lived"): Nghệ An → Hà Nội → Sài Gòn → Hasselt, kèm cờ, dòng "and many more bases to build…" (trên điện thoại ≤720px tên thành phố đang gõ nằm riêng một dòng bên dưới, đã giữ sẵn chỗ để trang không nhảy; lớp `.nx-t`, `.nx-c`) và nút "Your guide to starting fresh?" (Margot đổi từ "Give me some advice!"; Margot yêu cầu riêng nút này kết thúc bằng "?", ngoại lệ duy nhất của quy tắc CTA "!"). Hai bản đồ Việt Nam và Bỉ nằm hai bên tiêu đề, đã căn đối xứng hai bên màn hình ở mọi chiều rộng từ 981px (đo phần nét vẽ, lệch ≤3px). Hai bản đồ gióng theo trục giữa (tâm dọc trùng nhau, không gióng đáy) ở mọi độ rộng.
6. **The Craft** (nhãn cũ "Where I've worked") `#t-projects`: tiêu đề "work that" + chữ đổi dần (`#rot2`): untangles complexity / sparks conversations / bridges borders (Margot viết); trên điện thoại dòng này luôn giữ chỗ cho 2 dòng chữ (`min-height: 2em`) nên phần kệ sách bên dưới không bị đẩy lên xuống. kệ sách kéo ngang được, xếp theo thời gian. Tên gáy sách nhỏ, nhẹ, căn lề dưới; hàm `fitBooks` chỉ thu nhỏ hoặc bẻ 2 dòng khi tên quá dài. Dòng "Read between the lines" (Margot đổi từ "Every step has a story") dẫn tới `#/chapters`.
7. **The Spectrum** (nhãn cũ "The circles of my life") `#t-community`: chữ lớn "eclectic" (Margot đổi từ "curious"), chữ "e" thứ 2 màu xanh; sáu vòng tròn xếp chồng trên chữ e đó, 1/4 vòng phía dưới bên phải là nét đứt (khớp khe hở của chữ e, biến `--q`), mở dần thành vòng tròn liền khi các vòng dàn ra; caption "Six worlds, countless fragments." (Margot viết) Sáu vòng tròn Business, Flowers, Nature, Cocktails, Technology, Sketching. Bốn vòng sở thích dùng ảnh của Margot đã phủ màu xanh. Khi hai bên dạt ra, các vòng nằm gần tâm hơn (hàng trên cao `H*.31`, bước `H*.19`; cách mép `max(110px, 12%)`) để hai vòng trên cùng không bị cắt dưới header. Khi cuộn tới, các vòng dàn thành hàng thì ảnh tự hiện (như lúc rê chuột); cuộn tiếp, vòng dạt ra hai bên thì trở lại nền trắng đục (`--ph` trong `ecoFrame`). Nút "Read the unfiltered me!" (Margot đổi từ "Let's connect!"; nay dẫn tới `#/words`, không mở hộp thoại liên hệ nữa).
8. **My untold stories** `#t-stories` (**đang ẩn** bằng thuộc tính `hidden`, Margot dặn 25.10.2026 để dùng sau; muốn hiện lại thì bỏ `hidden`): ba tờ giấy note (4 names / 4 loves / 4 cities).
   - Bấm vào thì các tờ dạt sang hai bên rồi về lại chỗ cũ.
   - Từ 761px trở lên các tờ giấy note luôn xoè quạt và căn giữa (chỉ xếp dọc trên điện thoại ≤760px). Dòng "Click to uncover more!" nằm bên trái vùng giấy note dạt ra khi cửa sổ ≥1200px, nên không bị che; hẹp hơn thì nằm dưới các tờ giấy, căn giữa.
   - Nút "Read the stories!".
9. Câu **"Great ideas start on a whiteboard; the best ones bloom over a drink"** (cỡ chữ +4pt so với trước, Margot dặn 31.10.2026; vẫn đúng 2 dòng ở mọi chiều rộng, cỡ `clamp(1.28rem, 2vw + 5px, 2.07rem)`, trần `(100vw - 32px) / 16.5`) (đúng nguyên văn Margot sửa lúc 13:58 26.10.2026: dấu chấm phẩy, không có "!" cuối) (Margot viết 26.10.2026, thay cho câu "I believe…"; bản tiếng Việt trong `data-vi` là bản mình đoán), rồi phần liên hệ có nhãn "The Conversation" (nằm phía trên ly cocktail, trong phần `.believe`, không còn nằm cạnh tiêu đề; Margot đổi từ "Contact" 26.10.2026; data-vi "Cuộc trò chuyện" là bản đoán; hộp thoại liên hệ chỉ có MỘT format cho cả hai chế độ `contact` và `advice` (Margot dặn 26.10.2026): nhãn "Talk to me", tiêu đề "Write me an email", ô email có chú thích "I'll only use it to reply."; chế độ chỉ khác chủ đề thư gửi đi; trước đó ghi nhãn "Talk to me" (Margot đổi từ "Contact" 26.10.2026; data-vi là bản đoán)) (tiêu đề "let's mix things up!" (luôn trên 1 dòng) Margot viết 26.10.2026, đổi từ "let's grab the next drink"; không có dấu nháy gõ; data-vi là bản đoán), nút "Pull up a seat!" (Margot đổi từ "Ready when you are!" 26.10.2026, chỉ ở trang chủ; nút cùng tên ở các trang Use Cases và Blog giữ nguyên, chờ Margot quyết)).
10. **Footer** (nền tối):
    - Chữ "margot tran".
    - Liên kết tới các trang trong site.
    - LinkedIn, Instagram, Facebook.
    - Ngay dưới chữ "margot tran" là đồng hồ `#here-now`: chỉ giờ "HH:MM:SS GMT+X" (không ngày, không địa điểm), cùng kiểu chữ với "margot tran" nhưng nhỏ hơn, nền trắng như chữ đang được bôi chọn. Luôn là giờ của Margot, không theo máy người xem (Margot chốt 25.10.2026); múi giờ đặt ở hằng `HOME_TZ` (hiện là `Europe/Brussels`, cần Margot xác nhận), cập nhật mỗi giây.
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
