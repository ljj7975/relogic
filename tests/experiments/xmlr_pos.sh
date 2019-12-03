CUDA_VISIBLE_DEVICES=1
output_dir=saves/ner/conll2006/pos/es/test

mkdir -p output_dir

python -u -m relogic.main \
--task_name pos \
--mode train \
--encoder_type xlmr \
--bert_model xlmr.large.v0 \
--output_dir ${output_dir} \
--raw_data_path ${DATA_DIR}/CONLL_POS/el/ \
--label_mapping_path data/preprocessed_data/conll0607_pos_label_mapping.json \
--model_name default \
--no_cuda \
--learning_rate 1e-5 \
--train_batch_size 3 \
--test_batch_size 3 \
--epoch_number 3 \
--eval_dev_every 5 \
--pretokenized \
--metrics accuracy \
--early_stop_at 5 \
--config_file configurations/xlmr_large_config.json

python -u -m relogic.main \
--mode eval \
--restore_path ${output_dir} \
--no_cuda

rm -r ${output_dir}

