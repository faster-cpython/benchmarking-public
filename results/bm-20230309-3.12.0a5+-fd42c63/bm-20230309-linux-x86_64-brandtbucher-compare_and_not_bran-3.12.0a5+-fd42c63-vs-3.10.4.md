
# Results vs. 3.10.4

- fork: brandtbucher
- ref: compare_and_not_bran
- machine: linux-x86_64
- commit hash: fd42c63
- commit date: 2023-03-09
- overall geometric mean: 1.28x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-fd42c63 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 253 ms: 1.33x faster                                                         |
| chameleon      | 9.17 ms                                                | 6.41 ms: 1.43x faster                                                        |
| docutils       | 3.18 sec                                               | 2.58 sec: 1.23x faster                                                       |
| html5lib       | 85.9 ms                                                | 62.8 ms: 1.37x faster                                                        |
| tornado_http   | 128 ms                                                 | 94.9 ms: 1.35x faster                                                        |
| Geometric mean | (ref)                                                  | 1.34x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-fd42c63 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 93.9 ms: 1.53x faster                                                        |
| float          | 109 ms                                                 | 74.7 ms: 1.46x faster                                                        |
| pidigits       | 190 ms                                                 | 193 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                  | 1.30x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-fd42c63 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 135 ms: 1.32x faster                                                         |
| regex_v8       | 25.0 ms                                                | 21.9 ms: 1.15x faster                                                        |
| regex_dna      | 214 ms                                                 | 199 ms: 1.07x faster                                                         |
| regex_effbot   | 3.19 ms                                                | 3.53 ms: 1.11x slower                                                        |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-fd42c63 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 290 us: 1.56x faster                                                         |
| unpickle_pure_python | 302 us                                                 | 207 us: 1.46x faster                                                         |
| json_dumps           | 13.4 ms                                                | 9.42 ms: 1.43x faster                                                        |
| xml_etree_process    | 74.5 ms                                                | 55.6 ms: 1.34x faster                                                        |
| json_loads           | 28.7 us                                                | 23.9 us: 1.20x faster                                                        |
| pickle_list          | 4.72 us                                                | 4.07 us: 1.16x faster                                                        |
| xml_etree_generate   | 93.8 ms                                                | 81.9 ms: 1.15x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 148 ms: 1.10x faster                                                         |
| xml_etree_iterparse  | 111 ms                                                 | 104 ms: 1.07x faster                                                         |
| unpickle             | 14.2 us                                                | 13.4 us: 1.06x faster                                                        |
| pickle_dict          | 27.6 us                                                | 30.7 us: 1.11x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                                 |

Benchmark hidden because not significant (2): unpickle_list, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-fd42c63 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 9.02 ms: 1.56x faster                                                        |
| python_startup_no_site | 5.78 ms                                                | 6.54 ms: 1.13x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.17x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-fd42c63 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 10.2 ms: 1.43x faster                                                        |
| genshi_text     | 30.6 ms                                                | 21.7 ms: 1.41x faster                                                        |
| django_template | 46.3 ms                                                | 33.5 ms: 1.38x faster                                                        |
| genshi_xml      | 63.7 ms                                                | 47.9 ms: 1.33x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.39x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230309-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-fd42c63 |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 76.4 ms                                                | 30.9 ms: 2.47x faster                                                        |
| deltablue               | 7.28 ms                                                | 3.28 ms: 2.22x faster                                                        |
| logging_silent          | 176 ns                                                 | 97.2 ns: 1.82x faster                                                        |
| asyncio_tcp             | 914 ms                                                 | 504 ms: 1.81x faster                                                         |
| scimark_sor             | 197 ms                                                 | 110 ms: 1.79x faster                                                         |
| richards                | 75.2 ms                                                | 43.8 ms: 1.71x faster                                                        |
| pyflate                 | 676 ms                                                 | 412 ms: 1.64x faster                                                         |
| raytrace                | 467 ms                                                 | 287 ms: 1.62x faster                                                         |
| go                      | 226 ms                                                 | 140 ms: 1.61x faster                                                         |
| crypto_pyaes            | 117 ms                                                 | 73.1 ms: 1.60x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                 | 68.3 ms: 1.59x faster                                                        |
| chaos                   | 106 ms                                                 | 66.6 ms: 1.59x faster                                                        |
| spectral_norm           | 150 ms                                                 | 95.6 ms: 1.56x faster                                                        |
| python_startup          | 14.1 ms                                                | 9.02 ms: 1.56x faster                                                        |
| pickle_pure_python      | 452 us                                                 | 290 us: 1.56x faster                                                         |
| hexiom                  | 9.43 ms                                                | 6.10 ms: 1.55x faster                                                        |
| nbody                   | 144 ms                                                 | 93.9 ms: 1.53x faster                                                        |
| deepcopy_memo           | 51.7 us                                                | 35.0 us: 1.48x faster                                                        |
| float                   | 109 ms                                                 | 74.7 ms: 1.46x faster                                                        |
| unpickle_pure_python    | 302 us                                                 | 207 us: 1.46x faster                                                         |
| mako                    | 14.7 ms                                                | 10.2 ms: 1.43x faster                                                        |
| chameleon               | 9.17 ms                                                | 6.41 ms: 1.43x faster                                                        |
| json_dumps              | 13.4 ms                                                | 9.42 ms: 1.43x faster                                                        |
| scimark_lu              | 161 ms                                                 | 113 ms: 1.42x faster                                                         |
| genshi_text             | 30.6 ms                                                | 21.7 ms: 1.41x faster                                                        |
| pprint_pformat          | 1.98 sec                                               | 1.41 sec: 1.41x faster                                                       |
| sqlglot_parse           | 2.04 ms                                                | 1.46 ms: 1.40x faster                                                        |
| sqlglot_transpile       | 2.43 ms                                                | 1.74 ms: 1.39x faster                                                        |
| unpack_sequence         | 59.4 ns                                                | 42.7 ns: 1.39x faster                                                        |
| pprint_safe_repr        | 953 ms                                                 | 686 ms: 1.39x faster                                                         |
| django_template         | 46.3 ms                                                | 33.5 ms: 1.38x faster                                                        |
| logging_format          | 8.85 us                                                | 6.41 us: 1.38x faster                                                        |
| logging_simple          | 8.10 us                                                | 5.87 us: 1.38x faster                                                        |
| async_tree_io           | 1.78 sec                                               | 1.29 sec: 1.38x faster                                                       |
| pycparser               | 1.53 sec                                               | 1.12 sec: 1.37x faster                                                       |
| html5lib                | 85.9 ms                                                | 62.8 ms: 1.37x faster                                                        |
| async_tree_none         | 711 ms                                                 | 524 ms: 1.36x faster                                                         |
| thrift                  | 1.03 ms                                                | 765 us: 1.35x faster                                                         |
| tornado_http            | 128 ms                                                 | 94.9 ms: 1.35x faster                                                        |
| coroutines              | 31.6 ms                                                | 23.5 ms: 1.35x faster                                                        |
| xml_etree_process       | 74.5 ms                                                | 55.6 ms: 1.34x faster                                                        |
| genshi_xml              | 63.7 ms                                                | 47.9 ms: 1.33x faster                                                        |
| aiohttp                 | 1.34 ms                                                | 1.01 ms: 1.33x faster                                                        |
| 2to3                    | 335 ms                                                 | 253 ms: 1.33x faster                                                         |
| regex_compile           | 177 ms                                                 | 135 ms: 1.32x faster                                                         |
| gunicorn                | 1.43 ms                                                | 1.09 ms: 1.31x faster                                                        |
| async_tree_memoization  | 855 ms                                                 | 655 ms: 1.30x faster                                                         |
| deepcopy                | 438 us                                                 | 337 us: 1.30x faster                                                         |
| fannkuch                | 488 ms                                                 | 375 ms: 1.30x faster                                                         |
| mypy2                   | 430 ms                                                 | 332 ms: 1.29x faster                                                         |
| scimark_fft             | 421 ms                                                 | 326 ms: 1.29x faster                                                         |
| sqlglot_normalize       | 134 ms                                                 | 105 ms: 1.28x faster                                                         |
| async_tree_cpu_io_mixed | 949 ms                                                 | 745 ms: 1.27x faster                                                         |
| sqlglot_optimize        | 65.2 ms                                                | 51.4 ms: 1.27x faster                                                        |
| deepcopy_reduce         | 3.79 us                                                | 2.99 us: 1.27x faster                                                        |
| docutils                | 3.18 sec                                               | 2.58 sec: 1.23x faster                                                       |
| nqueens                 | 100 ms                                                 | 82.9 ms: 1.21x faster                                                        |
| json_loads              | 28.7 us                                                | 23.9 us: 1.20x faster                                                        |
| dulwich_log             | 75.8 ms                                                | 63.5 ms: 1.19x faster                                                        |
| sqlalchemy_imperative   | 21.5 ms                                                | 18.0 ms: 1.19x faster                                                        |
| bench_thread_pool       | 946 us                                                 | 795 us: 1.19x faster                                                         |
| sqlalchemy_declarative  | 165 ms                                                 | 140 ms: 1.18x faster                                                         |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.62 ms: 1.18x faster                                                        |
| json                    | 5.35 ms                                                | 4.60 ms: 1.16x faster                                                        |
| sympy_integrate         | 24.0 ms                                                | 20.7 ms: 1.16x faster                                                        |
| pickle_list             | 4.72 us                                                | 4.07 us: 1.16x faster                                                        |
| sympy_expand            | 534 ms                                                 | 465 ms: 1.15x faster                                                         |
| regex_v8                | 25.0 ms                                                | 21.9 ms: 1.15x faster                                                        |
| xml_etree_generate      | 93.8 ms                                                | 81.9 ms: 1.15x faster                                                        |
| djangocms               | 36.9 us                                                | 32.5 us: 1.13x faster                                                        |
| sympy_str               | 325 ms                                                 | 288 ms: 1.13x faster                                                         |
| sqlite_synth            | 2.92 us                                                | 2.61 us: 1.12x faster                                                        |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.11x faster                                                        |
| create_gc_cycles        | 1.65 ms                                                | 1.48 ms: 1.11x faster                                                        |
| xml_etree_parse         | 163 ms                                                 | 148 ms: 1.10x faster                                                         |
| sympy_sum               | 183 ms                                                 | 167 ms: 1.10x faster                                                         |
| meteor_contest          | 114 ms                                                 | 105 ms: 1.09x faster                                                         |
| regex_dna               | 214 ms                                                 | 199 ms: 1.07x faster                                                         |
| xml_etree_iterparse     | 111 ms                                                 | 104 ms: 1.07x faster                                                         |
| unpickle                | 14.2 us                                                | 13.4 us: 1.06x faster                                                        |
| mdp                     | 2.74 sec                                               | 2.61 sec: 1.05x faster                                                       |
| telco                   | 6.73 ms                                                | 6.44 ms: 1.05x faster                                                        |
| async_generators        | 426 ms                                                 | 420 ms: 1.02x faster                                                         |
| pidigits                | 190 ms                                                 | 193 ms: 1.02x slower                                                         |
| regex_effbot            | 3.19 ms                                                | 3.53 ms: 1.11x slower                                                        |
| pickle_dict             | 27.6 us                                                | 30.7 us: 1.11x slower                                                        |
| python_startup_no_site  | 5.78 ms                                                | 6.54 ms: 1.13x slower                                                        |
| dask                    | 436 ms                                                 | 513 ms: 1.17x slower                                                         |
| gc_traversal            | 3.53 ms                                                | 4.19 ms: 1.19x slower                                                        |
| coverage                | 74.7 ms                                                | 96.5 ms: 1.29x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.28x faster                                                                 |

Benchmark hidden because not significant (3): bench_mp_pool, unpickle_list, pickle
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: flaskblogging, pylint
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230309-3.12.0a5+-fd42c63/bm-20230309-linux-x86_64-brandtbucher-compare_and_not_bran-3.12.0a5+-fd42c63.json: comprehensions
