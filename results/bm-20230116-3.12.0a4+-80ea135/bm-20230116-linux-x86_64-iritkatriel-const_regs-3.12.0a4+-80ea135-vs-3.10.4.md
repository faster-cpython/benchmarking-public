
# Results vs. 3.10.4

- fork: iritkatriel
- ref: const_regs
- machine: linux-x86_64
- commit hash: 80ea135
- commit date: 2023-01-16
- overall geometric mean: 1.27x faster \*

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| 2to3           | 335 ms                                                 | 259 ms: 1.30x faster                                              |
| chameleon      | 9.17 ms                                                | 6.33 ms: 1.45x faster                                             |
| docutils       | 3.18 sec                                               | 2.62 sec: 1.21x faster                                            |
| html5lib       | 85.9 ms                                                | 61.5 ms: 1.40x faster                                             |
| Geometric mean | (ref)                                                  | 1.33x faster                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| nbody          | 144 ms                                                 | 96.2 ms: 1.50x faster                                             |
| float          | 109 ms                                                 | 74.1 ms: 1.47x faster                                             |
| pidigits       | 190 ms                                                 | 198 ms: 1.04x slower                                              |
| Geometric mean | (ref)                                                  | 1.28x faster                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 134 ms: 1.32x faster                                              |
| regex_v8       | 25.0 ms                                                | 22.2 ms: 1.13x faster                                             |
| regex_dna      | 214 ms                                                 | 217 ms: 1.02x slower                                              |
| regex_effbot   | 3.19 ms                                                | 3.63 ms: 1.14x slower                                             |
| Geometric mean | (ref)                                                  | 1.07x faster                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| pickle_pure_python   | 452 us                                                 | 297 us: 1.52x faster                                              |
| unpickle_pure_python | 302 us                                                 | 203 us: 1.48x faster                                              |
| json_dumps           | 13.4 ms                                                | 9.44 ms: 1.43x faster                                             |
| xml_etree_process    | 74.5 ms                                                | 54.5 ms: 1.37x faster                                             |
| xml_etree_generate   | 93.8 ms                                                | 78.4 ms: 1.20x faster                                             |
| json_loads           | 28.7 us                                                | 24.1 us: 1.19x faster                                             |
| pickle_list          | 4.72 us                                                | 4.07 us: 1.16x faster                                             |
| xml_etree_parse      | 163 ms                                                 | 149 ms: 1.09x faster                                              |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                              |
| unpickle             | 14.2 us                                                | 13.2 us: 1.08x faster                                             |
| unpickle_list        | 4.92 us                                                | 5.00 us: 1.02x slower                                             |
| pickle_dict          | 27.6 us                                                | 31.1 us: 1.13x slower                                             |
| Geometric mean       | (ref)                                                  | 1.17x faster                                                      |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                | 8.57 ms: 1.64x faster                                             |
| python_startup_no_site | 5.78 ms                                                | 6.11 ms: 1.06x slower                                             |
| Geometric mean         | (ref)                                                  | 1.25x faster                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| mako            | 14.7 ms                                                | 9.60 ms: 1.53x faster                                             |
| genshi_text     | 30.6 ms                                                | 21.2 ms: 1.44x faster                                             |
| django_template | 46.3 ms                                                | 34.3 ms: 1.35x faster                                             |
| genshi_xml      | 63.7 ms                                                | 47.6 ms: 1.34x faster                                             |
| Geometric mean  | (ref)                                                  | 1.41x faster                                                      |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------:|
| deltablue               | 7.28 ms                                                | 3.39 ms: 2.15x faster                                             |
| asyncio_tcp             | 914 ms                                                 | 504 ms: 1.81x faster                                              |
| scimark_sor             | 197 ms                                                 | 110 ms: 1.78x faster                                              |
| logging_silent          | 176 ns                                                 | 99.3 ns: 1.78x faster                                             |
| richards                | 75.2 ms                                                | 44.3 ms: 1.70x faster                                             |
| pyflate                 | 676 ms                                                 | 402 ms: 1.68x faster                                              |
| scimark_monte_carlo     | 109 ms                                                 | 65.1 ms: 1.67x faster                                             |
| python_startup          | 14.1 ms                                                | 8.57 ms: 1.64x faster                                             |
| go                      | 226 ms                                                 | 141 ms: 1.60x faster                                              |
| raytrace                | 467 ms                                                 | 298 ms: 1.57x faster                                              |
| chaos                   | 106 ms                                                 | 69.0 ms: 1.53x faster                                             |
| mako                    | 14.7 ms                                                | 9.60 ms: 1.53x faster                                             |
| spectral_norm           | 150 ms                                                 | 98.1 ms: 1.53x faster                                             |
| pickle_pure_python      | 452 us                                                 | 297 us: 1.52x faster                                              |
| crypto_pyaes            | 117 ms                                                 | 76.8 ms: 1.52x faster                                             |
| nbody                   | 144 ms                                                 | 96.2 ms: 1.50x faster                                             |
| hexiom                  | 9.43 ms                                                | 6.31 ms: 1.49x faster                                             |
| unpickle_pure_python    | 302 us                                                 | 203 us: 1.48x faster                                              |
| float                   | 109 ms                                                 | 74.1 ms: 1.47x faster                                             |
| deepcopy_memo           | 51.7 us                                                | 35.6 us: 1.45x faster                                             |
| chameleon               | 9.17 ms                                                | 6.33 ms: 1.45x faster                                             |
| scimark_lu              | 161 ms                                                 | 111 ms: 1.45x faster                                              |
| genshi_text             | 30.6 ms                                                | 21.2 ms: 1.44x faster                                             |
| json_dumps              | 13.4 ms                                                | 9.44 ms: 1.43x faster                                             |
| pprint_pformat          | 1.98 sec                                               | 1.40 sec: 1.41x faster                                            |
| html5lib                | 85.9 ms                                                | 61.5 ms: 1.40x faster                                             |
| thrift                  | 1.03 ms                                                | 745 us: 1.39x faster                                              |
| sqlglot_parse           | 2.04 ms                                                | 1.47 ms: 1.39x faster                                             |
| pprint_safe_repr        | 953 ms                                                 | 689 ms: 1.38x faster                                              |
| logging_simple          | 8.10 us                                                | 5.89 us: 1.38x faster                                             |
| sqlglot_transpile       | 2.43 ms                                                | 1.77 ms: 1.37x faster                                             |
| xml_etree_process       | 74.5 ms                                                | 54.5 ms: 1.37x faster                                             |
| logging_format          | 8.85 us                                                | 6.51 us: 1.36x faster                                             |
| scimark_fft             | 421 ms                                                 | 311 ms: 1.36x faster                                              |
| django_template         | 46.3 ms                                                | 34.3 ms: 1.35x faster                                             |
| async_tree_none         | 711 ms                                                 | 527 ms: 1.35x faster                                              |
| genshi_xml              | 63.7 ms                                                | 47.6 ms: 1.34x faster                                             |
| unpack_sequence         | 59.4 ns                                                | 44.5 ns: 1.33x faster                                             |
| async_tree_io           | 1.78 sec                                               | 1.33 sec: 1.33x faster                                            |
| fannkuch                | 488 ms                                                 | 366 ms: 1.33x faster                                              |
| regex_compile           | 177 ms                                                 | 134 ms: 1.32x faster                                              |
| pycparser               | 1.53 sec                                               | 1.16 sec: 1.32x faster                                            |
| scimark_sparse_mat_mult | 5.45 ms                                                | 4.15 ms: 1.31x faster                                             |
| 2to3                    | 335 ms                                                 | 259 ms: 1.30x faster                                              |
| async_tree_memoization  | 855 ms                                                 | 668 ms: 1.28x faster                                              |
| deepcopy                | 438 us                                                 | 343 us: 1.28x faster                                              |
| nqueens                 | 100 ms                                                 | 79.3 ms: 1.26x faster                                             |
| async_tree_cpu_io_mixed | 949 ms                                                 | 760 ms: 1.25x faster                                              |
| deepcopy_reduce         | 3.79 us                                                | 3.05 us: 1.24x faster                                             |
| sqlglot_optimize        | 65.2 ms                                                | 52.7 ms: 1.24x faster                                             |
| sqlglot_normalize       | 134 ms                                                 | 109 ms: 1.24x faster                                              |
| coroutines              | 31.6 ms                                                | 25.8 ms: 1.23x faster                                             |
| docutils                | 3.18 sec                                               | 2.62 sec: 1.21x faster                                            |
| xml_etree_generate      | 93.8 ms                                                | 78.4 ms: 1.20x faster                                             |
| dulwich_log             | 75.8 ms                                                | 63.5 ms: 1.19x faster                                             |
| bench_thread_pool       | 946 us                                                 | 794 us: 1.19x faster                                              |
| json_loads              | 28.7 us                                                | 24.1 us: 1.19x faster                                             |
| async_generators        | 426 ms                                                 | 359 ms: 1.19x faster                                              |
| pickle_list             | 4.72 us                                                | 4.07 us: 1.16x faster                                             |
| json                    | 5.35 ms                                                | 4.65 ms: 1.15x faster                                             |
| djangocms               | 36.9 us                                                | 32.5 us: 1.13x faster                                             |
| sqlite_synth            | 2.92 us                                                | 2.59 us: 1.13x faster                                             |
| regex_v8                | 25.0 ms                                                | 22.2 ms: 1.13x faster                                             |
| sympy_expand            | 534 ms                                                 | 473 ms: 1.13x faster                                              |
| create_gc_cycles        | 1.65 ms                                                | 1.46 ms: 1.13x faster                                             |
| pathlib                 | 20.0 ms                                                | 17.9 ms: 1.12x faster                                             |
| sympy_str               | 325 ms                                                 | 291 ms: 1.12x faster                                              |
| meteor_contest          | 114 ms                                                 | 103 ms: 1.11x faster                                              |
| xml_etree_parse         | 163 ms                                                 | 149 ms: 1.09x faster                                              |
| sympy_sum               | 183 ms                                                 | 168 ms: 1.09x faster                                              |
| sympy_integrate         | 24.0 ms                                                | 22.1 ms: 1.09x faster                                             |
| xml_etree_iterparse     | 111 ms                                                 | 103 ms: 1.08x faster                                              |
| unpickle                | 14.2 us                                                | 13.2 us: 1.08x faster                                             |
| telco                   | 6.73 ms                                                | 6.28 ms: 1.07x faster                                             |
| mdp                     | 2.74 sec                                               | 2.59 sec: 1.06x faster                                            |
| generators              | 76.4 ms                                                | 76.1 ms: 1.00x faster                                             |
| regex_dna               | 214 ms                                                 | 217 ms: 1.02x slower                                              |
| unpickle_list           | 4.92 us                                                | 5.00 us: 1.02x slower                                             |
| pidigits                | 190 ms                                                 | 198 ms: 1.04x slower                                              |
| python_startup_no_site  | 5.78 ms                                                | 6.11 ms: 1.06x slower                                             |
| gc_traversal            | 3.53 ms                                                | 3.80 ms: 1.08x slower                                             |
| pickle_dict             | 27.6 us                                                | 31.1 us: 1.13x slower                                             |
| regex_effbot            | 3.19 ms                                                | 3.63 ms: 1.14x slower                                             |
| dask                    | 436 ms                                                 | 518 ms: 1.19x slower                                              |
| coverage                | 74.7 ms                                                | 97.7 ms: 1.31x slower                                             |
| Geometric mean          | (ref)                                                  | 1.27x faster                                                      |

Benchmark hidden because not significant (2): bench_mp_pool, pickle
Ignored benchmarks (8) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn, mypy2, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20230116-3.12.0a4+-80ea135/bm-20230116-linux-x86_64-iritkatriel-const_regs-3.12.0a4+-80ea135.json: mypy
