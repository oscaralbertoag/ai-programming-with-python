#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#                                                                             
# PROGRAMMER: Oscar A
# DATE CREATED: 12/12/2020                            
# REVISED DATE: 
# PURPOSE: Test modifications done to funtionality in get_pet_labels.py
#
##
import get_pet_labels as gpl

def test_get_pet_labels_with_normal_filenames_return_correct_dictionary(tmp_path):
    # GIVEN: 3 files in a test image directory
    d = tmp_path / 'test_pet_images'
    d.mkdir()
    a = d / 'Boston_terrier_1234.jpg'
    b = d / 'Golden_retriever_dog_0987.jpg'
    c = d / 'Dalmatian_0123.jpg'
    a.write_text('test-data')
    b.write_text('test-data')
    c.write_text('test-data')
    
    # WHEN: pet labels are read from the test directory
    results = gpl.get_pet_labels(str(d))
    
    # THEN: the returned dictionary contains expected data
    assert results == {'Boston_terrier_1234.jpg':['boston terrier'], 'Dalmatian_0123.jpg':['dalmatian'], 'Golden_retriever_dog_0987.jpg':['golden retriever dog']}
    
def test_get_pet_labels_with_normal_and_bad_filenames_return_correct_dictionary(tmp_path):
    # GIVEN: good & bad file names in a test image directory
    d = tmp_path / 'test_pet_images'
    d.mkdir()
    a = d / 'Boston_terrier_1234.jpg'
    b = d / 'Golden_retriever_dog_0987.jpg'
    c = d / 'Dalmatian_0123.jpg'
    e = d / '.Should_not_read_this_0123.jpg'
    f = d / 'DALMATIAN.jpg'
    g = d / '01234_Dalmatian.jpg'
    h = d / '1Golden_12345_234_retriever_098dog.jpeg'
    a.write_text('test-data')
    b.write_text('test-data')
    c.write_text('test-data')
    e.write_text('test-data')
    f.write_text('test-data')
    g.write_text('test-data')
    h.write_text('test-data')
    
    # WHEN: pet labels are read from the test directory
    results = gpl.get_pet_labels(str(d))
    
    # THEN: the returned dictionary contains expected data
    assert results == {'Boston_terrier_1234.jpg':['boston terrier'], 'Dalmatian_0123.jpg':['dalmatian'], 'Golden_retriever_dog_0987.jpg':['golden retriever dog'], 'DALMATIAN.jpg':['dalmatian'], '01234_Dalmatian.jpg':['dalmatian'], '1Golden_12345_234_retriever_098dog.jpeg':['golden retriever dog']}

def test_single_word_filename_returns_correct_label():
    assert 'dalmatian' == gpl.get_pet_label('Dalmatian_1234.jpg')
        
def test_multiple_word_filename_returns_correct_label():
    assert 'german shepherd dog' == gpl.get_pet_label('German_Shepherd_dog_1234.jpg')
    assert 'german shepherd dog name' == gpl.get_pet_label('GeRmAn_Shepherd_dog_NaMe_1234.jpg')
        
def test_single_word_filename_returns_correct_label():
    assert 'dalmatian' == gpl.get_pet_label('Dalmatian_1234.jpg')
   
