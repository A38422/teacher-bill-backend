-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Máy chủ: 127.0.0.1
-- Thời gian đã tạo: Th5 05, 2023 lúc 09:41 PM
-- Phiên bản máy phục vụ: 10.4.28-MariaDB
-- Phiên bản PHP: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Cơ sở dữ liệu: `teacher_bill`
--

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `bangcap`
--

CREATE TABLE `bangcap` (
  `id` int(11) NOT NULL,
  `ten_bang_cap` varchar(50) DEFAULT NULL,
  `he_so_giao_vien` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `bangcap`
--

INSERT INTO `bangcap` (`id`, `ten_bang_cap`, `he_so_giao_vien`) VALUES
(1, 'Tiến sĩ', 1),
(2, 'Thạc sĩ', 1.2);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `giaovien`
--

CREATE TABLE `giaovien` (
  `id` int(11) NOT NULL,
  `ho_ten` varchar(100) DEFAULT NULL,
  `ma_so` varchar(10) DEFAULT NULL,
  `bang_cap_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `giaovien`
--

INSERT INTO `giaovien` (`id`, `ho_ten`, `ma_so`, `bang_cap_id`) VALUES
(2, 'min', 'a123', 1),
(3, 'minh', 'b123', 2);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `lophoc`
--

CREATE TABLE `lophoc` (
  `id` int(11) NOT NULL,
  `ten_lop_hoc` varchar(50) DEFAULT NULL,
  `so_sinh_vien` int(11) DEFAULT NULL,
  `he_so_lop_hoc` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `lophoc`
--

INSERT INTO `lophoc` (`id`, `ten_lop_hoc`, `so_sinh_vien`, `he_so_lop_hoc`) VALUES
(1, 'Hệ thống thông tin', 35, 1.4);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `monhoc`
--

CREATE TABLE `monhoc` (
  `id` int(11) NOT NULL,
  `ten_mon_hoc` varchar(50) DEFAULT NULL,
  `he_so_mon_hoc` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `monhoc`
--

INSERT INTO `monhoc` (`id`, `ten_mon_hoc`, `he_so_mon_hoc`) VALUES
(1, 'HTTT', 1.2);

-- --------------------------------------------------------

--
-- Cấu trúc bảng cho bảng `tienday`
--

CREATE TABLE `tienday` (
  `id` int(11) NOT NULL,
  `giao_vien_id` int(11) NOT NULL,
  `mon_hoc_id` int(11) NOT NULL,
  `lop_hoc_id` int(11) NOT NULL,
  `so_tiet` float DEFAULT NULL,
  `tien_day_mot_gio` int(11) DEFAULT NULL,
  `tien_day` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Đang đổ dữ liệu cho bảng `tienday`
--

INSERT INTO `tienday` (`id`, `giao_vien_id`, `mon_hoc_id`, `lop_hoc_id`, `so_tiet`, `tien_day_mot_gio`, `tien_day`) VALUES
(1, 3, 1, 1, 40, 100000, 15200000);

--
-- Chỉ mục cho các bảng đã đổ
--

--
-- Chỉ mục cho bảng `bangcap`
--
ALTER TABLE `bangcap`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `giaovien`
--
ALTER TABLE `giaovien`
  ADD PRIMARY KEY (`id`),
  ADD KEY `bang_cap_id` (`bang_cap_id`);

--
-- Chỉ mục cho bảng `lophoc`
--
ALTER TABLE `lophoc`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `monhoc`
--
ALTER TABLE `monhoc`
  ADD PRIMARY KEY (`id`);

--
-- Chỉ mục cho bảng `tienday`
--
ALTER TABLE `tienday`
  ADD PRIMARY KEY (`id`),
  ADD KEY `giao_vien_id` (`giao_vien_id`),
  ADD KEY `mon_hoc_id` (`mon_hoc_id`),
  ADD KEY `lop_hoc_id` (`lop_hoc_id`);

--
-- AUTO_INCREMENT cho các bảng đã đổ
--

--
-- AUTO_INCREMENT cho bảng `bangcap`
--
ALTER TABLE `bangcap`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT cho bảng `giaovien`
--
ALTER TABLE `giaovien`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT cho bảng `lophoc`
--
ALTER TABLE `lophoc`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT cho bảng `monhoc`
--
ALTER TABLE `monhoc`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT cho bảng `tienday`
--
ALTER TABLE `tienday`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Các ràng buộc cho các bảng đã đổ
--

--
-- Các ràng buộc cho bảng `giaovien`
--
ALTER TABLE `giaovien`
  ADD CONSTRAINT `giaovien_ibfk_1` FOREIGN KEY (`bang_cap_id`) REFERENCES `bangcap` (`id`);

--
-- Các ràng buộc cho bảng `tienday`
--
ALTER TABLE `tienday`
  ADD CONSTRAINT `tienday_ibfk_1` FOREIGN KEY (`giao_vien_id`) REFERENCES `giaovien` (`id`),
  ADD CONSTRAINT `tienday_ibfk_2` FOREIGN KEY (`mon_hoc_id`) REFERENCES `monhoc` (`id`),
  ADD CONSTRAINT `tienday_ibfk_3` FOREIGN KEY (`lop_hoc_id`) REFERENCES `lophoc` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
