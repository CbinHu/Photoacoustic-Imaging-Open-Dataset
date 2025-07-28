#!/usr/bin/env python3
import pathlib, textwrap, datetime

# 项目介绍内容
project_overview = textwrap.dedent("""
## 🔍 Project Overview

### 🌟 Introduction

Photoacoustic imaging (PAI) is a rapidly evolving, non-invasive imaging modality that combines the high contrast of optical imaging with the high spatial resolution of ultrasound imaging. It has garnered significant interest across various fields, including biomedical research, clinical diagnostics, and preclinical studies, due to its ability to provide detailed images of biological tissues and structures without the use of ionizing radiation.

![Photoacoustic Imaging](images/PA.png) <br>
Figure 1: PAT setup for noninvasive transdermal and transcranial imaging of the rat brain in vivo with the skin and skull intact. (From [Noninvasive laser-induced photoacoustic tomography for structural and functional in vivo imaging of the brain](https://www.nature.com/articles/nbt839)).

### 🎯 Objectives

The primary goal of the **PAID (Photoacoustic Imaging Dataset)** repository is to serve as a centralized, up-to-date, and comprehensive resource for researchers, clinicians, and students interested in PAI. This repository aims to:

- **Curate and Organize**: Collect and systematically organize all publicly available datasets related to photoacoustic imaging, ensuring that users have access to a wide range of data sources in one place.
- **Support Research**: Facilitate the advancement of research in PAI by providing a diverse set of datasets that can be used for algorithm development, validation, and benchmarking.
- **Promote Collaboration**: Encourage collaboration among the PAI community by making data accessible and easy to share, thereby fostering innovation and the development of new applications.
- **Educational Resource**: Serve as an educational tool for students and newcomers to the field, offering a variety of datasets to learn and experiment with.

### 📚 Dataset Categories

The datasets included in this repository cover a broad spectrum of PAI techniques and applications, such as:

- **Photoacoustic Microscopy (PAM)**: High-resolution imaging of small-scale biological structures, often used for studying cellular and sub-cellular processes.
- **Photoacoustic Computed Tomography (PACT)**: Whole-body or large-scale imaging, suitable for visualizing organs and tissues in vivo.
- **Multispectral Photoacoustic Imaging**: Datasets that capture multiple wavelengths of light to provide detailed information about different tissue types and their properties.
""")

# README 内容
README = textwrap.dedent(f"""
# 📝 PAID: Photoacoustic Imaging Dataset

📚 This repository is a continuously updated, comprehensive collection of all publicly available photoacoustic imaging datasets.

---

{project_overview}

---



## 📊 Dataset Summary Table

| Dataset Name | Paper Title | Year / Venue | Data Modality | Task Type | Size | Download Link |
|--------------|-------------|--------------|---------------|-----------|------|---------------|
| **Breast Cancer PAT - Twente Photoacoustic Mammoscope 2** | [Imaging breast malignancies with the Twente Photoacoustic Mammoscope 2](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0281434#pone.0281434.ref011) | 2023.03.06 | Photoacoustic Imaging | Breast Cancer Diagnosis, Vascular Imaging | 4 cases, each with 2 .mat files, 4-D single format | [Download](https://figshare.com/articles/dataset/Open_data_and_codes_for_Imaging_breast_malignancies_with_the_Twente_Photoacoustic_Mammoscope_2/22109687) |
| **Mouse PACT - Twente Photoacoustic Mammoscope 2** | [data](https://figshare.com/articles/dataset/data-mouse/9250634) | 2020.12.02 | Photoacoustic Imaging | Mouse Brain Imaging, Vascular Imaging | Phantom, Vascular Phantom, Mouse Data, Full and Sparse Reconstructions | [Download](https://figshare.com/articles/dataset/data-mouse/9250634) |
| **Mouse MSOT - Twente Photoacoustic Mammoscope 2** | [Domain Transform Network for Photoacoustic Tomography from Limited-view and Sparsely Sampled Data](http://www.radiomics.net.cn/post/132) | 2022 | Photoacoustic Imaging | Mouse Brain Imaging, Functional Imaging | 128x128 images, enhanced to 256x256 with denoising | [Download](http://www.radiomics.net.cn/post/132) |
| **Human Forearm Artery and Vein PACT** | [Machine learning enabled multiple illumination quantitative optoacoustic oximetry imaging in humans](https://zenodo.org/records/6466446) | 2022.02.04 | Photoacoustic Imaging | Human Forearm Imaging, Oxygenation Mapping | Raw optoacoustic signals, reconstructed images | [Download](https://zenodo.org/records/6466446) |
| **3D-PACT** | [High-speed three-dimensional photoacoustic computed tomography for preclinical research and clinical translation](https://figshare.com/articles/dataset/3D-PACT_Data_and_Codes/13114544) | 2021.02.09 | Photoacoustic Imaging | 3D Vascular Imaging, Functional Imaging | Supporting source data and codes | [Download](https://figshare.com/articles/dataset/3D-PACT_Data_and_Codes/13114544) |
---

## 👥💻 Contributors
- 🏫 **SMU Intelligent Optical Tomography Lab**  
  Southern Medical University  
  ✉️ [https://smu-iotlab.github.io/](https://smu-iotlab.github.io/) 

- 🧑‍🎓 **Chaobin Hu**  
  Southern Medical University  
  ✉️ cbinhu95@gmail.com

- 🧑‍🎓 **Yutian Zhong**  
  Southern Medical University  
  ✉️ 920460325@qq.com

- 👨‍🏫 **Li Qi**  
  Southern Medical University
  ✉️ qili@smu.edu.cn

---
## 📢 Latest Updates

- **2025-07-20**: 🎉 Create our GitHub project!

---

## 📊 GitHub Stats
![Stars](https://img.shields.io/github/stars/CbinHu/PAID-Photoacoustic-imaging-dataset?style=social)
![Forks](https://img.shields.io/github/forks/CbinHu/PAID-Photoacoustic-imaging-dataset?style=social)
![License](https://img.shields.io/github/license/CbinHu/PAID-Photoacoustic-imaging-dataset)
![Last Commit](https://img.shields.io/github/last-commit/CbinHu/PAID-Photoacoustic-imaging-dataset)
![Open Issues](https://img.shields.io/github/issues/CbinHu/PAID-Photoacoustic-imaging-dataset)
![Closed Issues](https://img.shields.io/github/issues-closed/CbinHu/PAID-Photoacoustic-imaging-dataset)

---

## 🙏 Acknowledgments

We would like to thank the following individuals and organizations for their support and contributions:

- **SMU Intelligent Optical Tomography Lab**  
  [Visit Website](https://smu-iotlab.github.io/)

- **Institute of Medical Information, School of Biomedical Engineering, Southern Medical University**  
  [Visit Website](https://portal.smu.edu.cn/swyxgcxy/info/1016/1115.htm)


## 📬 Contact
For any questions or inquiries, please contact:

- **Chaobin Hu**  
  Email: cbinhu95@gmail.com  
  GitHub: [CbinHu](https://github.com/CbinHu)

---

## 🌟 Support Us
If you find this project useful, please give us a star ⭐ to support our work and help us grow the community!

---

> Last generated: {datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M')} UTC
""").strip()

# 写入 README.md
pathlib.Path("README.md").write_text(README, encoding="utf-8")
print("✅ README.md 已生成完毕！")
