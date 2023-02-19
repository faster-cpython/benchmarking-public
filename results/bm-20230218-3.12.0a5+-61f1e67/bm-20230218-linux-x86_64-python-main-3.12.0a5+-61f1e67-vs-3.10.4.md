
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 61f1e67
- commit date: 2023-02-18
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230218-linux-x86_64-python-main-3.12.0a5+-61f1e67 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 247 ms: 1.36x faster                                   |
| chameleon      | 9.17 ms                                                | 6.49 ms: 1.41x faster                                  |
| docutils       | 3.18 sec                                               | 2.54 sec: 1.25x faster                                 |
| html5lib       | 85.9 ms                                                | 61.1 ms: 1.40x faster                                  |
| tornado_http   | 128 ms                                                 | 95.2 ms: 1.35x faster                                  |
| Geometric mean | (ref)                                                  | 1.35x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230218-linux-x86_64-python-main-3.12.0a5+-61f1e67 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 144 ms                                                 | 92.9 ms: 1.55x faster                                  |
| float          | 109 ms                                                 | 73.1 ms: 1.49x faster                                  |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.32x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230218-linux-x86_64-python-main-3.12.0a5+-61f1e67 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 130 ms: 1.36x faster                                   |
| regex_v8       | 25.0 ms                                                | 22.0 ms: 1.14x faster                                  |
| regex_dna      | 214 ms                                                 | 220 ms: 1.03x slower                                   |
| regex_effbot   | 3.19 ms                                                | 3.38 ms: 1.06x slower                                  |
| Geometric mean | (ref)                                                  | 1.09x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230218-linux-x86_64-python-main-3.12.0a5+-61f1e67 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 283 us: 1.60x faster                                   |
| unpickle_pure_python | 302 us                                                 | 198 us: 1.52x faster                                   |
| json_dumps           | 13.4 ms                                                | 9.58 ms: 1.40x faster                                  |
| xml_etree_process    | 74.5 ms                                                | 55.4 ms: 1.34x faster                                  |
| json_loads           | 28.7 us                                                | 23.7 us: 1.21x faster                                  |
| xml_etree_generate   | 93.8 ms                                                | 81.2 ms: 1.16x faster                                  |
| xml_etree_iterparse  | 111 ms                                                 | 100 ms: 1.11x faster                                   |
| pickle_list          | 4.72 us                                                | 4.29 us: 1.10x faster                                  |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.10x faster                                   |
| unpickle             | 14.2 us                                                | 13.3 us: 1.06x faster                                  |
| unpickle_list        | 4.92 us                                                | 5.06 us: 1.03x slower                                  |
| pickle_dict          | 27.6 us                                                | 32.5 us: 1.18x slower                                  |
| Geometric mean       | (ref)                                                  | 1.17x faster                                           |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230218-linux-x86_64-python-main-3.12.0a5+-61f1e67 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 9.00 ms: 1.56x faster                                  |
| python_startup_no_site | 5.78 ms                                                | 6.52 ms: 1.13x slower                                  |
| Geometric mean         | (ref)                                                  | 1.18x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230218-linux-x86_64-python-main-3.12.0a5+-61f1e67 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.92 ms: 1.48x faster                                  |
| genshi_text     | 30.6 ms                                                | 21.0 ms: 1.46x faster                                  |
| django_template | 46.3 ms                                                | 34.0 ms: 1.36x faster                                  |
| genshi_xml      | 63.7 ms                                                | 48.3 ms: 1.32x faster                                  |
| Geometric mean  | (ref)                                                  | 1.40x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230218-linux-x86_64-python-main-3.12.0a5+-61f1e67 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| generators              | 76.4 ms                                                | 30.5 ms: 2.51x faster                                  |
| deltablue               | 7.28 ms                                                | 3.21 ms: 2.27x faster                                  |
| logging_silent          | 176 ns                                                 | 93.9 ns: 1.88x faster                                  |
| asyncio_tcp             | 914 ms                                                 | 501 ms: 1.82x faster                                   |
| scimark_sor             | 197 ms                                                 | 109 ms: 1.81x faster                                   |
| richards                | 75.2 ms                                                | 42.0 ms: 1.79x faster                                  |
| go                      | 226 ms                                                 | 133 ms: 1.70x faster                                   |
| pyflate                 | 676 ms                                                 | 400 ms: 1.69x faster                                   |
| raytrace                | 467 ms                                                 | 285 ms: 1.63x faster                                   |
| scimark_monte_carlo     | 109 ms                                                 | 66.4 ms: 1.63x faster                                  |
| chaos                   | 106 ms                                                 | 65.7 ms: 1.61x faster                                  |
| pickle_pure_python      | 452 us                                                 | 283 us: 1.60x faster                                   |
| crypto_pyaes            | 117 ms                                                 | 73.2 ms: 1.59x faster                                  |
| python_startup          | 14.1 ms                                                | 9.00 ms: 1.56x faster                                  |
| nbody                   | 144 ms                                                 | 92.9 ms: 1.55x faster                                  |
| spectral_norm           | 150 ms                                                 | 96.6 ms: 1.55x faster                                  |
| hexiom                  | 9.43 ms                                                | 6.13 ms: 1.54x faster                                  |
| unpickle_pure_python    | 302 us                                                 | 198 us: 1.52x faster                                   |
| scimark_lu              | 161 ms                                                 | 107 ms: 1.50x faster                                   |
| float                   | 109 ms                                                 | 73.1 ms: 1.49x faster                                  |
| deepcopy_memo           | 51.7 us                                                | 34.9 us: 1.48x faster                                  |
| mako                    | 14.7 ms                                                | 9.92 ms: 1.48x faster                                  |
| genshi_text             | 30.6 ms                                                | 21.0 ms: 1.46x faster                                  |
| pprint_pformat          | 1.98 sec                                               | 1.40 sec: 1.42x faster                                 |
| sqlglot_parse           | 2.04 ms                                                | 1.44 ms: 1.42x faster                                  |
| chameleon               | 9.17 ms                                                | 6.49 ms: 1.41x faster                                  |
| html5lib                | 85.9 ms                                                | 61.1 ms: 1.40x faster                                  |
| json_dumps              | 13.4 ms                                                | 9.58 ms: 1.40x faster                                  |
| sqlglot_transpile       | 2.43 ms                                                | 1.73 ms: 1.40x faster                                  |
| pprint_safe_repr        | 953 ms                                                 | 682 ms: 1.40x faster                                   |
| logging_simple          | 8.10 us                                                | 5.80 us: 1.40x faster                                  |
| unpack_sequence         | 59.4 ns                                                | 42.7 ns: 1.39x faster                                  |
| coroutines              | 31.6 ms                                                | 22.9 ms: 1.38x faster                                  |
| scimark_fft             | 421 ms                                                 | 305 ms: 1.38x faster                                   |
| scimark_sparse_mat_mult | 5.45 ms                                                | 3.98 ms: 1.37x faster                                  |
| logging_format          | 8.85 us                                                | 6.47 us: 1.37x faster                                  |
| pycparser               | 1.53 sec                                               | 1.12 sec: 1.37x faster                                 |
| django_template         | 46.3 ms                                                | 34.0 ms: 1.36x faster                                  |
| regex_compile           | 177 ms                                                 | 130 ms: 1.36x faster                                   |
| 2to3                    | 335 ms                                                 | 247 ms: 1.36x faster                                   |
| fannkuch                | 488 ms                                                 | 360 ms: 1.36x faster                                   |
| thrift                  | 1.03 ms                                                | 766 us: 1.35x faster                                   |
| async_tree_none         | 711 ms                                                 | 527 ms: 1.35x faster                                   |
| async_tree_io           | 1.78 sec                                               | 1.32 sec: 1.35x faster                                 |
| tornado_http            | 128 ms                                                 | 95.2 ms: 1.35x faster                                  |
| xml_etree_process       | 74.5 ms                                                | 55.4 ms: 1.34x faster                                  |
| aiohttp                 | 1.34 ms                                                | 1.01 ms: 1.33x faster                                  |
| genshi_xml              | 63.7 ms                                                | 48.3 ms: 1.32x faster                                  |
| deepcopy                | 438 us                                                 | 332 us: 1.32x faster                                   |
| async_tree_memoization  | 855 ms                                                 | 649 ms: 1.32x faster                                   |
| gunicorn                | 1.43 ms                                                | 1.09 ms: 1.31x faster                                  |
| mypy2                   | 430 ms                                                 | 331 ms: 1.30x faster                                   |
| sqlglot_normalize       | 134 ms                                                 | 104 ms: 1.29x faster                                   |
| sqlglot_optimize        | 65.2 ms                                                | 51.0 ms: 1.28x faster                                  |
| deepcopy_reduce         | 3.79 us                                                | 2.96 us: 1.28x faster                                  |
| async_tree_cpu_io_mixed | 949 ms                                                 | 749 ms: 1.27x faster                                   |
| docutils                | 3.18 sec                                               | 2.54 sec: 1.25x faster                                 |
| nqueens                 | 100 ms                                                 | 80.0 ms: 1.25x faster                                  |
| json_loads              | 28.7 us                                                | 23.7 us: 1.21x faster                                  |
| sympy_integrate         | 24.0 ms                                                | 19.9 ms: 1.21x faster                                  |
| dulwich_log             | 75.8 ms                                                | 62.9 ms: 1.20x faster                                  |
| sqlalchemy_declarative  | 165 ms                                                 | 137 ms: 1.20x faster                                   |
| bench_thread_pool       | 946 us                                                 | 790 us: 1.20x faster                                   |
| sympy_str               | 325 ms                                                 | 273 ms: 1.19x faster                                   |
| sqlalchemy_imperative   | 21.5 ms                                                | 18.1 ms: 1.19x faster                                  |
| json                    | 5.35 ms                                                | 4.54 ms: 1.18x faster                                  |
| sympy_expand            | 534 ms                                                 | 454 ms: 1.18x faster                                   |
| xml_etree_generate      | 93.8 ms                                                | 81.2 ms: 1.16x faster                                  |
| sympy_sum               | 183 ms                                                 | 159 ms: 1.15x faster                                   |
| djangocms               | 36.9 us                                                | 32.4 us: 1.14x faster                                  |
| regex_v8                | 25.0 ms                                                | 22.0 ms: 1.14x faster                                  |
| sqlite_synth            | 2.92 us                                                | 2.59 us: 1.13x faster                                  |
| meteor_contest          | 114 ms                                                 | 102 ms: 1.11x faster                                   |
| xml_etree_iterparse     | 111 ms                                                 | 100 ms: 1.11x faster                                   |
| mdp                     | 2.74 sec                                               | 2.48 sec: 1.11x faster                                 |
| pickle_list             | 4.72 us                                                | 4.29 us: 1.10x faster                                  |
| create_gc_cycles        | 1.65 ms                                                | 1.50 ms: 1.10x faster                                  |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.10x faster                                   |
| pathlib                 | 20.0 ms                                                | 18.3 ms: 1.09x faster                                  |
| unpickle                | 14.2 us                                                | 13.3 us: 1.06x faster                                  |
| telco                   | 6.73 ms                                                | 6.46 ms: 1.04x faster                                  |
| async_generators        | 426 ms                                                 | 411 ms: 1.04x faster                                   |
| pidigits                | 190 ms                                                 | 189 ms: 1.00x faster                                   |
| unpickle_list           | 4.92 us                                                | 5.06 us: 1.03x slower                                  |
| regex_dna               | 214 ms                                                 | 220 ms: 1.03x slower                                   |
| regex_effbot            | 3.19 ms                                                | 3.38 ms: 1.06x slower                                  |
| gc_traversal            | 3.53 ms                                                | 3.83 ms: 1.09x slower                                  |
| python_startup_no_site  | 5.78 ms                                                | 6.52 ms: 1.13x slower                                  |
| dask                    | 436 ms                                                 | 501 ms: 1.15x slower                                   |
| pickle_dict             | 27.6 us                                                | 32.5 us: 1.18x slower                                  |
| coverage                | 74.7 ms                                                | 96.3 ms: 1.29x slower                                  |
| Geometric mean          | (ref)                                                  | 1.30x faster                                           |

Benchmark hidden because not significant (2): pickle, bench_mp_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
