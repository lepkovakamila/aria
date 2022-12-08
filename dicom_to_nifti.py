import dicom2nifti
import os


def dicom_to_nifti_aria(path):
    path_to_dataset = path
    patients_folders = os.listdir(path_to_dataset)
    for pat in patients_folders:
        if pat[-4:] == 'xlsx':
            print('Skipped xlsx format')
        elif pat == '.DS_Store':
            print('Skipped .DS_Store')
        else:
            sequence_path = os.path.join(path_to_dataset, pat)
            sequences = os.listdir(sequence_path)
            for idx, seq in enumerate(sequences):
                if seq == 'T2STAR':
                    t2_path = os.path.join(path_to_dataset, pat, 'T2STAR_NIFTI')
                    if not os.path.exists(t2_path):
                        os.makedirs(t2_path)
                    dicom2nifti.convert_directory(os.path.join(sequence_path, 'T2STAR'), t2_path, compression=False,
                                                  reorient=True)
                    files = os.listdir(t2_path)
                    for file in files:
                        if file[-4:] == '.nii':
                            os.rename(os.path.join(t2_path, file), os.path.join(t2_path, pat + '_' + seq + '.nii'))
                elif seq == 'T1':
                    t1_path = os.path.join(path_to_dataset, pat, 'T1_NIFTI')
                    if not os.path.exists(t1_path):
                        os.makedirs(t1_path)
                    dicom2nifti.convert_directory(os.path.join(sequence_path, 'T1'), t1_path, compression=False,
                                                  reorient=True)
                    files = os.listdir(t1_path)
                    for file in files:
                        if file[-4:] == '.nii':
                            os.rename(os.path.join(t1_path, file), os.path.join(t1_path, pat + '_' + seq + '.nii'))
                elif seq == 'SWI':
                    swi_path = os.path.join(path_to_dataset, pat, 'SWI_NIFTI')
                    if not os.path.exists(swi_path):
                        os.makedirs(swi_path)
                    dicom2nifti.convert_directory(os.path.join(sequence_path, 'SWI'), swi_path, compression=False,
                                                  reorient=True)
                    files = os.listdir(swi_path)
                    for file in files:
                        if file[-4:] == '.nii':
                            os.rename(os.path.join(swi_path, file), os.path.join(swi_path, pat + '_' + seq + '.nii'))
                elif seq == 'FLAIR':
                    flair_path = os.path.join(path_to_dataset, pat, 'FLAIR_NIFTI')
                    if not os.path.exists(flair_path):
                        os.makedirs(flair_path)
                    dicom2nifti.convert_directory(os.path.join(sequence_path, 'FLAIR'), flair_path, compression=False,
                                                  reorient=True)
                    files = os.listdir(flair_path)
                    for file in files:
                        if file[-4:] == '.nii':
                            os.rename(os.path.join(flair_path, file),
                                      os.path.join(flair_path, pat + '_' + seq + '.nii'))
                elif seq == 'DWI':
                    dwi_path = os.path.join(path_to_dataset, pat, 'DWI_NIFTI')
                    if not os.path.exists(dwi_path):
                        os.makedirs(dwi_path)
                    dicom2nifti.convert_directory(os.path.join(sequence_path, 'DWI'), dwi_path, compression=False,
                                                  reorient=True)
                    files = os.listdir(dwi_path)
                    for file in files:
                        if file[-4:] == '.nii':
                            os.rename(os.path.join(dwi_path, file), os.path.join(dwi_path, pat + '_' + seq + '.nii'))
