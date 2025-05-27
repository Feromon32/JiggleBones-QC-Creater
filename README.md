ALL JIGGLE BONE MUST BE WATCHED IN -Z COORDINATES FOR PROPER PHYSICS IN THE GAME

# JiggleBones-QC-Creater
Simple script that copies all jiggleBones to your clipboard.

Usage:
Just select skelet, and run script in blender

![GIF 20 06 2023 18-30-40](https://github.com/Feromon32/JiggleBones-QC-Creater/assets/65503900/41da793f-071d-496f-aba4-f8e9ccf68af3)


Examples for qc:

# Jigglebone Configurations

This README provides jigglebone configurations for various models like tails, coats, breasts, items, and long ponytails. Use the provided configurations to enhance your models with realistic physics.

---

## Table of Contents

1. [Jiggles for Tails](#jiggles-for-tails)
2. [Jiggles for Coats](#jiggles-for-coats)
3. [Jiggles for Breast](#jiggles-for-breast)
4. [Jiggles for Items](#jiggles-for-items)
5. [Jiggles for Long Ponytails](#jiggles-for-long-ponytails)

---

## Jiggles for Tails

```plaintext
$jigglebone "your_bone_name"
{
    is_flexible
    {
        length 6
        tip_mass 250
        pitch_constraint -80 80
        pitch_stiffness 55
        pitch_damping 7
        yaw_stiffness 35
        yaw_damping 7
        along_stiffness 100
        yaw_constraint -80 80
        along_damping 0
        angle_constraint 39.999999
    }
}
```
![1kVzv00](https://github.com/user-attachments/assets/b2c8ce00-38f6-4a9c-9107-81f355665503)

## Jiggles for Coats
```plaintext
$jigglebone "your_bone_name"
{
    is_rigid
    {
        length 20
        tip_mass 400
        pitch_constraint -79.999998 -5
        pitch_friction 2
        pitch_bounce 0
        yaw_constraint -50 50
        yaw_friction 2
        yaw_bounce 0
    }
}

$jigglebone "your_bone_name2"
{
    is_flexible
    {
        length 6
        tip_mass 250
        pitch_stiffness 55
        pitch_damping 7
        yaw_stiffness 35
        yaw_damping 7
        along_stiffness 100
        along_damping 0
        angle_constraint 39.999999
    }
}

$jigglebone "your_bone_name3"
{
    is_flexible
    {
        length 6
        tip_mass 250
        pitch_stiffness 54
        pitch_damping 7
        yaw_stiffness 40
        yaw_damping 7
        along_stiffness 100
        along_damping 0
        angle_constraint 50
    }
}

$jigglebone "your_bone_name4"
{
    is_flexible
    {
        length 6
        tip_mass 250
        pitch_stiffness 44
        pitch_damping 7
        yaw_stiffness 40
        yaw_damping 7
        along_stiffness 100
        along_damping 0
        angle_constraint 60.000002
    }
}
```
![DTL4ev1](https://github.com/user-attachments/assets/9013a9b3-3889-4e95-828b-76bb8cd53087)

## Jiggles for Breast
```plaintext
$jigglebone "your_bone_name"
{
    has_base_spring
    {
        base_mass 0
        stiffness 400
        damping 10
        left_constraint -0.4 0.4
        left_friction 0
        up_constraint -0.1 0.1
        up_friction 0
        forward_constraint -0.5 0.5
        forward_friction 0
    }
}
```
![Jg6d6d4](https://github.com/user-attachments/assets/436d85d9-f4c1-43cc-b56a-cd7e94a99489)

## Jiggles for Items
(From Cuba Jigglebone Attachments)

```plaintext
$jigglebone "your_bone_name"
{
    is_flexible
    {
        length 100
        tip_mass 0
        pitch_stiffness 200
        pitch_damping 10
        yaw_stiffness 200
        yaw_damping 10
        along_stiffness 100
        along_damping 0
        angle_constraint 19.999999
    }
}
```
![6krw6o0](https://github.com/user-attachments/assets/9f1d1fc2-7f89-4eab-bd53-f4274500e4c0)


## Jiggles for Long Ponytails
```plaintext
$jigglebone "your_bone_name"
{
    is_flexible
    {
        length 10
        tip_mass 250
        pitch_constraint -30 30
        pitch_stiffness 55
        pitch_damping 20
        yaw_stiffness 35
        yaw_damping 20
        along_stiffness 100
        yaw_constraint -30 30
        along_damping 0
        angle_constraint 39.999999
    }
}
```
![uE1sx9b](https://github.com/user-attachments/assets/2d5f912e-5c4b-453c-8834-a5e911515a3d)

---

**Special thanks to this guy and his guide! Please give it a like: [Guide on Steam](https://steamcommunity.com/sharedfiles/filedetails/?id=3219785194).**

---
