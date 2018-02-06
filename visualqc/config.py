"""
Central place to store the config info

"""

# default values
default_out_dir_name = 'visualqc'
default_mri_name = 'brainmask.mgz'
default_seg_name = 'aparc+aseg.mgz'
required_files = (default_mri_name, default_seg_name)

default_freesurfer_dir = None
freesurfer_vis_types = ('cortical_volumetric', 'labels', 'cortical_surface', 'cortical_composite',
                                     'subcortical_volumetric')
visualization_combination_choices = ('cortical_volumetric', 'labels', 'cortical_surface', 'cortical_composite',
                                     'subcortical_volumetric', 'user_defined')
default_vis_type = 'cortical_volumetric'
default_label_set = None

default_user_dir = None

default_alpha_set = (0.7, 0.7)

default_views = (0, 1, 2)
default_num_slices = 12
default_num_rows = 2

suffix_ratings_dir='ratings'
file_name_ratings = 'ratings.all.csv'
file_name_ratings_backup = 'backup_ratings.all.csv'

# visualization layout
zoomed_position = [0.2, 0.2, 0.7, 0.7]
