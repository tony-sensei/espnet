#!/usr/bin/env bash
# Set bash to 'debug' mode, it will exit on :
# -e 'error', -u 'undefined variable', -o ... 'error in pipeline', -x 'print commands',
set -e
set -u
set -o pipefail

# language related
src_lang=lt 
tgt_lang=en 

stage=1
stop_stage=5

# kmeans related
clustering_portion=1
clustering_num_clusters=500
feature_layer=6

train_set=train_${src_lang}_${tgt_lang}
train_dev=dev_${src_lang}_${tgt_lang}
test_sets="test_${src_lang}_${tgt_lang} dev_${src_lang}_${tgt_lang}"

st_config=
use_src_lang=true
use_tgt_lang=true
inference_config=
vocoder_file=
score_asr_model_tag=

./s2st.sh \
    --stage ${stage} \
    --stop_stage ${stop_stage} \
    --ngpu 2 \
    --nj 64 \
    --inference_nj 64 \
    --use_discrete_unit true \
    --feats_type raw \
    --audio_format "wav" \
    --use_src_lang ${use_src_lang} \
    --use_tgt_lang ${use_tgt_lang} \
    --token_joint false \
    --src_lang ${src_lang} \
    --tgt_lang ${tgt_lang} \
    --feature_layer ${feature_layer} \
    --s3prl_upstream_name mhubert_base_vp_en_es_fr_it3 \
    --storage_save_mode false \
    --clustering_num_threads 60 \
    --clustering_portion ${clustering_portion} \
    --feature_num_clusters ${clustering_num_clusters} \
    --src_token_type "char" \
    --tgt_token_type "char" \
    --inference_config "${inference_config}" \
    --vocoder_file "${vocoder_file}" \
    --score_asr_model_tag "${score_asr_model_tag}" \
    --train_set "${train_set}" \
    --valid_set "${train_dev}" \
    --test_sets "${test_sets}" "$@"