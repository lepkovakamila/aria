import time
import os
import shutil



class ImagePreprocessing:
    def __init__(self, directory_path, WORKING_DIR, pat_directory, aria_type_directory,
                 JHU_ATLAS_TEMPLATE_NII_PATH, EXCEL_INFO):

        start = time.time()
        self.directory_path = directory_path
        self.pat_directory = pat_directory
        self.aria_type_directory = aria_type_directory
        self.patients_path = []
        self.flair_path = []
        self.t1_path = []
        self.swi_path = []
        self.mni_path = []
        self.work_path = []

        self.WORKING_DIR = WORKING_DIR
        self.JHU_ATLAS_TEMPLATE_NII_PATH = JHU_ATLAS_TEMPLATE_NII_PATH
        self.EXCEL_INFO = EXCEL_INFO



        end = time.time()
        print('Image pre-processing took:', round(end - start, 1), 'sec')


    def get_patients_path(self):
        self.patients_list = os.listdir(self.directory_path)
        self.patients_list.remove('.DS_Store')
        self.patients_list.remove(self.EXCEL_INFO)

        for pat in self.patients_list:
            path = os.path.join(self.directory_path, pat)
            self.patients_path.append(path)

        return self.patients_path


    def get_flair_path(self):
        for pat in self.patients_list:
            self.flair_path.append(os.path.join(self.directory_path, pat, 'FLAIR_NIFTI'))

        return self.flair_path


    def get_t1_path(self):
        for pat in self.patients_list:
            self.t1_path.append(os.path.join(self.directory_path, pat, 'T1_NIFTI'))

        return self.t1_path


    def get_swi_path(self):
        for pat in self.patients_list:
            self.swi_path.append(os.path.join(self.directory_path, pat, 'SWI_NIFTI'))

        return self.swi_path



    def create_pat_directory(self):
        if not os.path.exists(self.pat_directory):
            os.makedirs(self.pat_directory)


    def create_aria_type_directory(self):
        if not os.path.exists(self.aria_type_directory):
            os.makedirs(self.aria_type_directory)


    def create_patients_mni_folders(self):
        for idx in range(len(self.patients_list)):
            path = os.path.join(self.aria_type_directory, self.patients_list[idx], 'mnispace')
            self.mni_path.append(path)
            if not os.path.exists(path):
                os.makedirs(path)

        return self.mni_path


    def create_patients_work_folders(self):
        for idx in range(len(self.patients_list)):
            path_workspace = os.path.join(self.aria_type_directory, self.patients_list[idx], 'workspace')
            self.work_path.append(path_workspace)
            if not os.path.exists(path_workspace):
                os.makedirs(path_workspace)

        return self.work_path


    def ants_atlas_registration_t1(self, path):
        start = time.time()
        template = self.JHU_ATLAS_TEMPLATE_NII_PATH
        pat = path.split('/')[-2]
        moving_path_t1 = os.path.join(path, pat + '_T1.nii')
        output = os.path.join(self.aria_type_directory, pat, 'workspace')
        cmd = 'antsRegistrationSyN.sh -d 3 -f {} -m {} -o {} -t s'.format(template, moving_path_t1,
                                                                          output + '/')
        os.system(cmd)
        end = time.time()
        print('ANTs Registration with atlas took ', round(end - start, 1), 'sec')
        shutil.move(output + '/Warped.nii.gz', os.path.join(self.aria_type_directory, pat, 'mnispace', 't1.nii'))
        print('Done', os.path.join(self.aria_type_directory, pat, 'mnispace', 't1.nii'))

    def ants_atlas_registration_flair(self, path):
        start = time.time()
        template = self.JHU_ATLAS_TEMPLATE_NII_PATH
        pat = path.split('/')[-2]
        moving_path_flair = os.path.join(path, pat + '_FLAIR.nii')
        output = os.path.join(self.aria_type_directory, pat, 'workspace')
        cmd = 'antsRegistrationSyN.sh -d 3 -f {} -m {} -o {} -t s'.format(template, moving_path_flair,
                                                                          output + '/')
        os.system(cmd)
        end = time.time()
        print('ANTs Registration with atlas took ', round(end - start, 1), 'sec')
        shutil.move(output + '/Warped.nii.gz', os.path.join(self.aria_type_directory, pat, 'mnispace', 'flair.nii'))
        print('Done', os.path.join(self.aria_type_directory, pat, 'mnispace', 'flair.nii'))

    def ants_atlas_registration_swi(self, path):
        start = time.time()
        template = self.JHU_ATLAS_TEMPLATE_NII_PATH
        pat = path.split('/')[-2]
        moving_path_swi = os.path.join(path, pat + '_SWI.nii')
        output = os.path.join(self.aria_type_directory, pat, 'workspace')
        cmd = 'antsRegistrationSyN.sh -d 3 -f {} -m {} -o {} -t s'.format(template, moving_path_swi,
                                                                          output + '/')
        os.system(cmd)
        end = time.time()
        print('ANTs Registration with atlas took ', round(end - start, 1), 'sec')
        shutil.move(output + '/Warped.nii.gz', os.path.join(self.aria_type_directory, pat, 'mnispace', 'swi.nii'))
        print('Done', os.path.join(self.aria_type_directory, pat, 'mnispace', 'swi.nii'))