# Hồ sơ nộp Lab 11 — mã 02457

- Mã sinh viên đầy đủ: `2A202602457`.
- Mã dùng để tạo thị trấn và seed của bài: **`02457`**, giữ số 0 đầu.
- Thị trấn: A. Seed do `space.student_variant("02457")` tạo, không tự chọn.

## Chạy lại

```powershell
cd D:\AI-Vin\Track4-Day11-Scenario-Forge-Student
python -m pip install -r requirements.txt
python -m pytest -q tests/test_todos.py
python run_lab.py all
```

`run_lab.py` đọc đúng 5 số ở dòng đầu REPORT.md rồi đặt `LAB11_MSSV` trước khi gọi bộ chạy gốc. Cần tiện ích này vì biểu thức đọc REPORT.md trong bản gốc yêu cầu 6–12 chữ số. Có thể chạy trực tiếp như sau:

```powershell
$env:LAB11_MSSV = '02457'
python run_all.py all
```

Không chuyển mã sang số nguyên, không dùng mã đầy đủ để tạo seed và không thêm chữ số đệm. `avsim/`, `run_all.py`, `tests/` và các ứng viên policy gốc được giữ nguyên. `--quick` chỉ dành cho thử code; hồ sơ này sử dụng ngân sách đầy đủ.

## Xem bằng chứng 3D

Mở `viewer/index.html` trực tiếp trong trình duyệt:

1. Chương 9: mở `evidence/viewer.json` để xem các tình huống tìm được, log phát lại và ví dụ phần G.
2. Chương 9: mở `evidence/fix-viewer.json` để xem policy được chọn bằng xe đặc và policy gốc bằng bóng mờ trên cùng cảnh.
3. Chương 10: mở `hazard.json` để xem cảnh xe đạp chính xác đã dựng.

Ảnh thực tế của trình xem nằm trong `evidence/shots/`; thông số và sự kiện tương ứng được ghi trong `evidence/scene_notes.json`. Không dùng ảnh mẫu của giảng viên làm bằng chứng của bài.

## Ý nghĩa của tình huống mới

`exposure = 0.068` lần mỗi chuyến = 1.4 lần gặp xe đạp/km (Kegalle et al. 2025, bảng 4, đo thực địa ở Melbourne) × 0.2142 km mỗi chuyến mô phỏng (`fix.json`) × 94/414 lần gặp mà xe đạp nhập ngang vào làn xe (Al-Taie et al. CHI 2023, bảng 1, quan sát ở Glasgow). Khoảng tốc độ có mốc từ nghiên cứu FHWA. Các khoảng vị trí, độ lạng, thời gian và kích hoạt là miền kiểm thử thiết kế, có căn cứ hình học/vật lý ghi trong `hazard.json: why`. Exposure là ước lượng bậc độ lớn ghép từ hai thành phố, không phải số đo trên tuyến của thị trấn A; hướng sai lệch được ghi ở câu 9.

Không có thử nghiệm tự lái của sinh viên được ghi nhận. Oracle phanh chương trình không được trình bày như kết quả người dùng tự lái.

## Thành phần bài nộp

- Sáu file `lab11/*.py` chứa đủ 10 TODO.
- `hazard.json`, giữ định dạng studio và các trường params/policy/hazards.
- `REPORT.md`: đủ 9 câu, số trích từ evidence và ảnh được chụp ở sự kiện tương ứng.
- `evidence/*.json` và `evidence/shots/*.png`.
- `run_lab.py` và tài liệu này để tái tạo đúng mã 5 số.

Các JSON do pipeline tạo giữ nguyên. `scene_notes.json` và `fix-viewer.json` là bằng chứng kiểm tra và hiển thị bổ sung. Kết quả khám phá trong `.work/` không dùng để báo xác suất và không nằm trong gói nộp.
