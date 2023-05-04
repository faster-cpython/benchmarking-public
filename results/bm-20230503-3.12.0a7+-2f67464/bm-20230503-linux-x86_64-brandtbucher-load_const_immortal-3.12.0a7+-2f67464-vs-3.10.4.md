
# Results vs. 3.10.4

- fork: brandtbucher
- ref: load_const_immortal
- machine: linux-x86_64
- commit hash: 2f67464
- commit date: 2023-05-03
- overall geometric mean: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230503-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-2f67464 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 270 ms: 1.24x faster                                                        |
| docutils       | 3.19 sec                                                            | 2.76 sec: 1.16x faster                                                      |
| tornado_http   | 129 ms                                                              | 99.8 ms: 1.29x faster                                                       |
| Geometric mean | (ref)                                                               | 1.23x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230503-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-2f67464 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 146 ms                                                              | 89.2 ms: 1.63x faster                                                       |
| float          | 110 ms                                                              | 81.9 ms: 1.34x faster                                                       |
| pidigits       | 190 ms                                                              | 197 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                               | 1.28x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230503-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-2f67464 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 146 ms: 1.21x faster                                                        |
| regex_v8       | 24.9 ms                                                             | 22.3 ms: 1.12x faster                                                       |
| regex_dna      | 213 ms                                                              | 209 ms: 1.02x faster                                                        |
| regex_effbot   | 3.22 ms                                                             | 3.55 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                               | 1.06x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230503-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-2f67464 |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 318 us: 1.44x faster                                                        |
| json_dumps           | 13.7 ms                                                             | 9.86 ms: 1.39x faster                                                       |
| unpickle_pure_python | 300 us                                                              | 219 us: 1.37x faster                                                        |
| xml_etree_process    | 74.8 ms                                                             | 60.4 ms: 1.24x faster                                                       |
| json_loads           | 29.3 us                                                             | 26.0 us: 1.13x faster                                                       |
| xml_etree_generate   | 94.9 ms                                                             | 86.3 ms: 1.10x faster                                                       |
| xml_etree_iterparse  | 111 ms                                                              | 104 ms: 1.07x faster                                                        |
| xml_etree_parse      | 164 ms                                                              | 153 ms: 1.07x faster                                                        |
| pickle_list          | 4.73 us                                                             | 4.48 us: 1.06x faster                                                       |
| pickle               | 10.2 us                                                             | 10.8 us: 1.06x slower                                                       |
| pickle_dict          | 27.8 us                                                             | 32.1 us: 1.16x slower                                                       |
| Geometric mean       | (ref)                                                               | 1.12x faster                                                                |

Benchmark hidden because not significant (2): unpickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230503-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-2f67464 |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 9.16 ms: 1.54x faster                                                       |
| python_startup_no_site | 5.80 ms                                                             | 6.68 ms: 1.15x slower                                                       |
| Geometric mean         | (ref)                                                               | 1.16x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230503-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-2f67464 |
|-----------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 14.7 ms                                                             | 10.7 ms: 1.38x faster                                                       |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230503-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-2f67464 |
|-------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| generators              | 75.7 ms                                                             | 31.0 ms: 2.44x faster                                                       |
| deltablue               | 7.30 ms                                                             | 3.57 ms: 2.04x faster                                                       |
| asyncio_tcp             | 922 ms                                                              | 510 ms: 1.81x faster                                                        |
| logging_silent          | 169 ns                                                              | 102 ns: 1.66x faster                                                        |
| go                      | 226 ms                                                              | 137 ms: 1.65x faster                                                        |
| richards                | 74.2 ms                                                             | 45.4 ms: 1.63x faster                                                       |
| nbody                   | 146 ms                                                              | 89.2 ms: 1.63x faster                                                       |
| scimark_sor             | 198 ms                                                              | 123 ms: 1.61x faster                                                        |
| python_startup          | 14.1 ms                                                             | 9.16 ms: 1.54x faster                                                       |
| raytrace                | 470 ms                                                              | 306 ms: 1.54x faster                                                        |
| sqlglot_parse           | 2.07 ms                                                             | 1.35 ms: 1.54x faster                                                       |
| chaos                   | 106 ms                                                              | 69.4 ms: 1.53x faster                                                       |
| hexiom                  | 9.50 ms                                                             | 6.30 ms: 1.51x faster                                                       |
| pyflate                 | 671 ms                                                              | 450 ms: 1.49x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                              | 73.4 ms: 1.48x faster                                                       |
| sqlglot_transpile       | 2.45 ms                                                             | 1.67 ms: 1.47x faster                                                       |
| crypto_pyaes            | 117 ms                                                              | 80.5 ms: 1.45x faster                                                       |
| async_tree_io           | 1.78 sec                                                            | 1.24 sec: 1.44x faster                                                      |
| pickle_pure_python      | 457 us                                                              | 318 us: 1.44x faster                                                        |
| async_tree_none         | 713 ms                                                              | 500 ms: 1.42x faster                                                        |
| coroutines              | 31.8 ms                                                             | 22.3 ms: 1.42x faster                                                       |
| scimark_lu              | 160 ms                                                              | 113 ms: 1.42x faster                                                        |
| spectral_norm           | 150 ms                                                              | 108 ms: 1.39x faster                                                        |
| json_dumps              | 13.7 ms                                                             | 9.86 ms: 1.39x faster                                                       |
| async_tree_memoization  | 853 ms                                                              | 615 ms: 1.39x faster                                                        |
| mako                    | 14.7 ms                                                             | 10.7 ms: 1.38x faster                                                       |
| unpickle_pure_python    | 300 us                                                              | 219 us: 1.37x faster                                                        |
| float                   | 110 ms                                                              | 81.9 ms: 1.34x faster                                                       |
| pycparser               | 1.53 sec                                                            | 1.15 sec: 1.33x faster                                                      |
| deepcopy_memo           | 51.8 us                                                             | 38.8 us: 1.33x faster                                                       |
| unpack_sequence         | 65.6 ns                                                             | 50.0 ns: 1.31x faster                                                       |
| async_tree_cpu_io_mixed | 944 ms                                                              | 722 ms: 1.31x faster                                                        |
| pprint_pformat          | 1.98 sec                                                            | 1.51 sec: 1.31x faster                                                      |
| logging_simple          | 8.21 us                                                             | 6.31 us: 1.30x faster                                                       |
| tornado_http            | 129 ms                                                              | 99.8 ms: 1.29x faster                                                       |
| pprint_safe_repr        | 953 ms                                                              | 740 ms: 1.29x faster                                                        |
| logging_format          | 9.07 us                                                             | 7.08 us: 1.28x faster                                                       |
| fannkuch                | 485 ms                                                              | 379 ms: 1.28x faster                                                        |
| 2to3                    | 336 ms                                                              | 270 ms: 1.24x faster                                                        |
| xml_etree_process       | 74.8 ms                                                             | 60.4 ms: 1.24x faster                                                       |
| mypy2                   | 432 ms                                                              | 354 ms: 1.22x faster                                                        |
| regex_compile           | 177 ms                                                              | 146 ms: 1.21x faster                                                        |
| scimark_fft             | 425 ms                                                              | 353 ms: 1.20x faster                                                        |
| deepcopy                | 438 us                                                              | 367 us: 1.19x faster                                                        |
| sqlglot_normalize       | 135 ms                                                              | 113 ms: 1.19x faster                                                        |
| nqueens                 | 98.8 ms                                                             | 83.3 ms: 1.19x faster                                                       |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.74 ms: 1.19x faster                                                       |
| sqlglot_optimize        | 65.3 ms                                                             | 55.4 ms: 1.18x faster                                                       |
| deepcopy_reduce         | 3.80 us                                                             | 3.23 us: 1.18x faster                                                       |
| docutils                | 3.19 sec                                                            | 2.76 sec: 1.16x faster                                                      |
| comprehensions          | 27.3 us                                                             | 23.5 us: 1.16x faster                                                       |
| bench_thread_pool       | 954 us                                                              | 833 us: 1.15x faster                                                        |
| sqlalchemy_declarative  | 166 ms                                                              | 147 ms: 1.13x faster                                                        |
| json_loads              | 29.3 us                                                             | 26.0 us: 1.13x faster                                                       |
| dulwich_log             | 76.3 ms                                                             | 68.0 ms: 1.12x faster                                                       |
| regex_v8                | 24.9 ms                                                             | 22.3 ms: 1.12x faster                                                       |
| sqlite_synth            | 2.97 us                                                             | 2.68 us: 1.11x faster                                                       |
| xml_etree_generate      | 94.9 ms                                                             | 86.3 ms: 1.10x faster                                                       |
| sqlalchemy_imperative   | 21.2 ms                                                             | 19.3 ms: 1.10x faster                                                       |
| create_gc_cycles        | 1.64 ms                                                             | 1.49 ms: 1.10x faster                                                       |
| meteor_contest          | 115 ms                                                              | 105 ms: 1.10x faster                                                        |
| json                    | 5.41 ms                                                             | 4.98 ms: 1.09x faster                                                       |
| xml_etree_iterparse     | 111 ms                                                              | 104 ms: 1.07x faster                                                        |
| xml_etree_parse         | 164 ms                                                              | 153 ms: 1.07x faster                                                        |
| pathlib                 | 19.8 ms                                                             | 18.5 ms: 1.07x faster                                                       |
| pickle_list             | 4.73 us                                                             | 4.48 us: 1.06x faster                                                       |
| mdp                     | 2.75 sec                                                            | 2.62 sec: 1.05x faster                                                      |
| regex_dna               | 213 ms                                                              | 209 ms: 1.02x faster                                                        |
| pidigits                | 190 ms                                                              | 197 ms: 1.04x slower                                                        |
| pickle                  | 10.2 us                                                             | 10.8 us: 1.06x slower                                                       |
| telco                   | 6.67 ms                                                             | 7.05 ms: 1.06x slower                                                       |
| async_generators        | 420 ms                                                              | 455 ms: 1.08x slower                                                        |
| regex_effbot            | 3.22 ms                                                             | 3.55 ms: 1.10x slower                                                       |
| gc_traversal            | 3.53 ms                                                             | 3.94 ms: 1.12x slower                                                       |
| python_startup_no_site  | 5.80 ms                                                             | 6.68 ms: 1.15x slower                                                       |
| pickle_dict             | 27.8 us                                                             | 32.1 us: 1.16x slower                                                       |
| dask                    | 437 ms                                                              | 542 ms: 1.24x slower                                                        |
| coverage                | 70.6 ms                                                             | 102 ms: 1.45x slower                                                        |
| Geometric mean          | (ref)                                                               | 1.24x faster                                                                |

Benchmark hidden because not significant (3): unpickle_list, bench_mp_pool, unpickle
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
