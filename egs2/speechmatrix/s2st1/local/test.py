from espnet2.tts.utils.hifigan_pretrained_vocoder import FairseqHifiGANPretrainedVocoder
import torch
import os
import pathlib
import numpy as np
from espnet2.torch_utils.device_funcs import to_device
import soundfile as sf

def load_code(in_file):
    with open(in_file) as f:
        out = [list(map(int, line.strip().split())) for line in f]
    return out


if __name__ == "__main__":
    config_file = "dump/pretrained_HifiGAN/config.yml"
    vocoder_file = "dump/pretrained_HifiGAN/g_00500000.pt"
    device = "cuda:0" if torch.cuda.is_available() else "cpu"

    vocoder = FairseqHifiGANPretrainedVocoder(vocoder_file, config_file).to(device)
    token_list = [63, 665, 991, 162, 116, 281, 238, 462, 761, 907, 597, 424, 818, 542, 272, 313, 469, 367, 167, 88, 650, 816, 325, 274, 477, 728, 56, 321, 948, 198, 711, 510, 297, 265, 675, 755, 237, 71, 6, 452, 379, 735, 102, 63, 951, 665, 662, 445, 137, 484, 488, 620, 915, 143, 38, 105, 326, 531, 643, 139, 253, 340, 380, 198, 711, 376, 124, 243, 290, 978, 161, 523, 793, 403, 477, 852, 56, 485, 620, 112, 654, 726, 38, 662, 479, 330, 435, 592, 103, 382, 867, 45, 914, 445, 137, 167, 761, 693, 934, 501, 137, 74, 228, 259, 453, 503, 822, 89, 194, 664, 817, 146, 283, 352, 915, 889, 172, 871, 877, 384, 879, 70, 918, 743, 852, 366, 713, 506, 545, 85, 297, 265, 675, 755, 193, 415]
    token_int = np.array(token_int)
    input_discrete_unit = to_device(
                        torch.tensor(token_int).view(-1, 1), device=device
                    )
    
    wav = vocoder(input_discrete_unit)

    sf.write(
        f"dump/pretrained_HifiGAN/pred.wav",
        wav.cpu().numpy(),
        16000,
    )