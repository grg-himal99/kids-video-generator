import os

import numpy as np
from gtts import gTTS
from scipy.io import wavfile


def generate_narration(text: str, scene_number: int, output_dir: str) -> str:
    tts = gTTS(text=text, lang="en", slow=False)
    path = os.path.join(output_dir, f"narration_{scene_number:02d}.mp3")
    tts.save(path)
    return path


def generate_background_music(duration_seconds: float, output_path: str) -> str:
    """
    Generates a gentle C-major arpeggio loop as background music.
    No external dependencies beyond numpy and scipy.
    """
    sample_rate = 44100
    total_samples = int(sample_rate * duration_seconds)
    t_full = np.linspace(0, duration_seconds, total_samples, endpoint=False)
    music = np.zeros(total_samples, dtype=np.float64)

    # C major pentatonic notes (C4, E4, G4, A4, C5, E5)
    notes = [261.63, 329.63, 392.00, 440.00, 523.25, 659.25]
    note_dur = 0.6  # seconds per note
    note_samples = int(sample_rate * note_dur)

    note_index = 0
    pos = 0
    while pos < total_samples:
        freq = notes[note_index % len(notes)]
        end = min(pos + note_samples, total_samples)
        seg_len = end - pos
        seg_t = np.linspace(0, note_dur, seg_len, endpoint=False)

        # Sine wave with soft attack/decay envelope
        envelope = np.sin(np.pi * seg_t / note_dur) ** 0.5
        music[pos:end] += 0.18 * np.sin(2 * np.pi * freq * seg_t) * envelope

        pos += note_samples
        note_index += 1

    # Soft bass pedal (C2)
    music += 0.08 * np.sin(2 * np.pi * 65.41 * t_full)

    # Global fade-in / fade-out (2 seconds each)
    fade = min(int(sample_rate * 2), total_samples // 4)
    music[:fade] *= np.linspace(0, 1, fade)
    music[-fade:] *= np.linspace(1, 0, fade)

    # Normalize to 80% of max
    peak = np.max(np.abs(music))
    if peak > 0:
        music = music / peak * 0.8

    stereo = np.column_stack([music, music])
    wavfile.write(output_path, sample_rate, (stereo * 32767).astype(np.int16))
    return output_path
