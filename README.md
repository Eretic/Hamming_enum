# Enum with error protection values
Generate codes for enum and calculates its minimal Hamming distance

[![Build Status](https://travis-ci.org/Eretic/Hamming_enum.svg?branch=master)](https://travis-ci.org/Eretic/Hamming_enum) [![Coverage Status](https://coveralls.io/repos/github/Eretic/Hamming_enum/badge.svg?branch=master)](https://coveralls.io/github/Eretic/Hamming_enum?branch=master)
[![codecov](https://codecov.io/gh/Eretic/Hamming_enum/branch/master/graph/badge.svg)](https://codecov.io/gh/Eretic/Hamming_enum)

##### Minimal Hamming distance 14
```c
enum {
    CODE_00 = 0x00000000,
    CODE_01 = 0x1746B8B9,
    CODE_02 = 0x2B9E45A4,
    CODE_03 = 0x3CD8FD1D,
    CODE_04 = 0x44751A27,
    CODE_05 = 0x5333A29E,
    CODE_06 = 0x6FEB5F83,
    CODE_07 = 0x78ADE73A,
    CODE_08 = 0x88EA344E,
    CODE_09 = 0x9FAC8CF7,
    CODE_10 = 0xA37471EA,
    CODE_11 = 0xB432C953,
    CODE_12 = 0xCC9F2E69,
    CODE_13 = 0xDBD996D0,
    CODE_14 = 0xE7016BCD,
    CODE_15 = 0xF047D374,
};
```

##### Minimal Hamming distance 16:
```c
enum {
    CODE_00 = 0x00000000,
    CODE_01 = 0x3CD8FD1D,
    CODE_02 = 0x5A19EAA7,
    CODE_03 = 0x66C117BA,
    CODE_04 = 0x9B4FAC52,
    CODE_05 = 0xA797514F,
    CODE_06 = 0xC15646F5,
    CODE_07 = 0xFD8EBBE8,
};
```
