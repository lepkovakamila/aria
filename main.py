# IMPORTS
import os
import nibabel as nib
import matplotlib.pyplot as plt
from dicom_to_nifti import dicom_to_nifti_aria
from data_preprocessing import *

# EDEMA DETECTION AND SEGMENTATION

# 1. PATH TO DATASET
# 1.1 Loading dataset = ARIA-E (FLAIR, T1), ARIA-H (T2*/SWI, T1) and Health Control in DICOM
PATH_DICOM_ARIA_E = '/Users/M217789/PycharmProjects/aria/dataset/aria_data_e'
PATH_DICOM_CONTROL_ARIA_E = '/Users/M217789/PycharmProjects/aria/dataset/control_data_e'


# 1.2 Converting DICOM to NIFTI format (ALREADY DONE)
# Define path to directory with DICOM format
#path = ''
#dicom_to_nifti_aria(path)

# 1.1 Initializing path for media, atlases
WORKING_DIR = os.getcwd()
MEDIA_DIR = WORKING_DIR + '/media'
ATLAS_DIR = MEDIA_DIR + '/atlases'
JHU_ATLAS_DIR = ATLAS_DIR + '/JHU'
JHU_ATLAS_TEMPLATE_NII_PATH = JHU_ATLAS_DIR + '/JHU_MNI_SS_template_T1.nii'
IXI_TEMPLATE_DIR = ATLAS_DIR + '/IXI'
IXI_TEMPLATE_NII_PATH = IXI_TEMPLATE_DIR + '/T_template0.nii'
IXI_TEMPLATE_BRAIN_CEREBELLUM_PROBABILITY_MASK_NII_PATH = IXI_TEMPLATE_DIR + \
                                                          '/T_template_BrainCerebellumProbabilityMask.nii '

pat_directory = os.path.join(WORKING_DIR, 'pat_directory')
directory_path = '/Users/M217789/PycharmProjects/aria/dataset/aria_data_e'
EXCEL_INFO = 'aria_e_info.xlsx'


# 2. DATA PRE-PROCESSING
image_preprocessing = ImagePreprocessing(directory_path, WORKING_DIR, pat_directory, JHU_ATLAS_TEMPLATE_NII_PATH, EXCEL_INFO)
patients_path = image_preprocessing.get_patients_path()
image_preprocessing.create_pat_directory()
image_preprocessing.create_patients_mni_folders()
image_preprocessing.create_patients_work_folders()

flair_paths = image_preprocessing.get_flair_path()
t1_paths = image_preprocessing.get_t1_path()

for path in t1_paths:
    image_preprocessing.ants_atlas_registration_t1(path)

for path in flair_paths:
    image_preprocessing.ants_atlas_registration_flair(path)




stop = 1


PATH_ARIA_E_001_DWI_NIFTI = '/dataset/aria_e_data/001/NIFTI/001_DWI.nii'
PATH_ARIA_E_001_FLAIR_NIFTI = '/Users/M217789/PycharmProjects/mri_pet_amyloid/dataset/aria_e_data/001/FLAIR/NIFTI/001_FLAIR.nii'
PATH_ARIA_E_001_T1_NIFTI = '/Users/M217789/PycharmProjects/mri_pet_amyloid/dataset/aria_e_data/001/T1/NIFTI/001_T1.nii'

# 2.1. Data Loading in Nifti1Image
DWI_nifti_image = nib.load(PATH_ARIA_E_001_DWI_NIFTI)
FLAIR_nifti_image = nib.load(PATH_ARIA_E_001_FLAIR_NIFTI)
T1_nifti_image = nib.load(PATH_ARIA_E_001_T1_NIFTI)

# 2.1. Data Loading in Numpy Array
DWI_numpy_image = nib.load(PATH_ARIA_E_001_DWI_NIFTI).get_fdata()
FLAIR_numpy_image = nib.load(PATH_ARIA_E_001_FLAIR_NIFTI).get_fdata()
T1_numpy_image = nib.load(PATH_ARIA_E_001_T1_NIFTI).get_fdata()


# 2.2. Plotting Images

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(20, 10))
slice_w = 10
ax1.imshow(DWI_numpy_image[:, :, DWI_numpy_image.shape[2]//2-slice_w, 0], cmap='gray')
ax1.set_title('Image DWI')
ax2.imshow(FLAIR_numpy_image[:, :, FLAIR_numpy_image.shape[2]//2-slice_w], cmap='gray')
ax2.set_title('Image FLAIR')
ax3.imshow(T1_numpy_image[:, :, T1_numpy_image.shape[2]//2-slice_w], cmap='gray')
ax3.set_title('Image T1')
fig.show()

STOP = 1
# 2.1. Data Co-registering into Same Anatomical Template


# 2.2. Interpolating to the Same Resolution


# 2.3. Intensity Normalization (Histogram Matching)


# 2.4. N4 Correction


# 2.5. Orientation Check, Artefact Check, Motion Correction


# 3. SKULL STRIPPING


# 4. MACHINE LEARNING - ARIA-E, ARIA-H DETECTION


