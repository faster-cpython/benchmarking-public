
# Results vs. 3.10.4

- fork: brandtbucher
- ref: load_const_immortal
- machine: linux-x86_64
- commit hash: a39e7e6
- commit date: 2023-05-02
- overall geometric mean: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230502-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-a39e7e6 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 270 ms: 1.24x faster                                                        |
| docutils       | 3.19 sec                                                            | 2.71 sec: 1.18x faster                                                      |
| tornado_http   | 129 ms                                                              | 99.8 ms: 1.29x faster                                                       |
| Geometric mean | (ref)                                                               | 1.24x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230502-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-a39e7e6 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 146 ms                                                              | 90.3 ms: 1.62x faster                                                       |
| float          | 110 ms                                                              | 81.6 ms: 1.35x faster                                                       |
| pidigits       | 190 ms                                                              | 197 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                               | 1.28x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230502-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-a39e7e6 |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 146 ms: 1.21x faster                                                        |
| regex_v8       | 24.9 ms                                                             | 22.2 ms: 1.12x faster                                                       |
| regex_dna      | 213 ms                                                              | 200 ms: 1.06x faster                                                        |
| regex_effbot   | 3.22 ms                                                             | 3.57 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                               | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230502-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-a39e7e6 |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 317 us: 1.44x faster                                                        |
| json_dumps           | 13.7 ms                                                             | 10.0 ms: 1.37x faster                                                       |
| unpickle_pure_python | 300 us                                                              | 220 us: 1.36x faster                                                        |
| xml_etree_process    | 74.8 ms                                                             | 59.4 ms: 1.26x faster                                                       |
| json_loads           | 29.3 us                                                             | 26.2 us: 1.12x faster                                                       |
| xml_etree_generate   | 94.9 ms                                                             | 84.8 ms: 1.12x faster                                                       |
| xml_etree_iterparse  | 111 ms                                                              | 104 ms: 1.08x faster                                                        |
| xml_etree_parse      | 164 ms                                                              | 154 ms: 1.06x faster                                                        |
| pickle_list          | 4.73 us                                                             | 4.62 us: 1.02x faster                                                       |
| unpickle             | 15.0 us                                                             | 14.7 us: 1.02x faster                                                       |
| pickle               | 10.2 us                                                             | 10.7 us: 1.05x slower                                                       |
| pickle_dict          | 27.8 us                                                             | 30.7 us: 1.11x slower                                                       |
| Geometric mean       | (ref)                                                               | 1.12x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230502-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-a39e7e6 |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 9.21 ms: 1.54x faster                                                       |
| python_startup_no_site | 5.80 ms                                                             | 6.74 ms: 1.16x slower                                                       |
| Geometric mean         | (ref)                                                               | 1.15x faster                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230502-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-a39e7e6 |
|-----------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako      | 14.7 ms                                                             | 10.8 ms: 1.36x faster                                                       |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230502-linux-x86_64-brandtbucher-load_const_immortal-3.12.0a7+-a39e7e6 |
|-------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| generators              | 75.7 ms                                                             | 32.8 ms: 2.31x faster                                                       |
| deltablue               | 7.30 ms                                                             | 3.54 ms: 2.06x faster                                                       |
| asyncio_tcp             | 922 ms                                                              | 507 ms: 1.82x faster                                                        |
| logging_silent          | 169 ns                                                              | 101 ns: 1.68x faster                                                        |
| richards                | 74.2 ms                                                             | 44.6 ms: 1.66x faster                                                       |
| go                      | 226 ms                                                              | 138 ms: 1.63x faster                                                        |
| nbody                   | 146 ms                                                              | 90.3 ms: 1.62x faster                                                       |
| scimark_sor             | 198 ms                                                              | 124 ms: 1.59x faster                                                        |
| raytrace                | 470 ms                                                              | 304 ms: 1.55x faster                                                        |
| chaos                   | 106 ms                                                              | 68.6 ms: 1.54x faster                                                       |
| python_startup          | 14.1 ms                                                             | 9.21 ms: 1.54x faster                                                       |
| sqlglot_parse           | 2.07 ms                                                             | 1.35 ms: 1.53x faster                                                       |
| hexiom                  | 9.50 ms                                                             | 6.27 ms: 1.51x faster                                                       |
| pyflate                 | 671 ms                                                              | 450 ms: 1.49x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                              | 73.8 ms: 1.47x faster                                                       |
| sqlglot_transpile       | 2.45 ms                                                             | 1.68 ms: 1.47x faster                                                       |
| crypto_pyaes            | 117 ms                                                              | 80.6 ms: 1.45x faster                                                       |
| pickle_pure_python      | 457 us                                                              | 317 us: 1.44x faster                                                        |
| async_tree_io           | 1.78 sec                                                            | 1.24 sec: 1.44x faster                                                      |
| scimark_lu              | 160 ms                                                              | 113 ms: 1.42x faster                                                        |
| async_tree_none         | 713 ms                                                              | 503 ms: 1.42x faster                                                        |
| async_tree_memoization  | 853 ms                                                              | 615 ms: 1.39x faster                                                        |
| spectral_norm           | 150 ms                                                              | 109 ms: 1.38x faster                                                        |
| deepcopy_memo           | 51.8 us                                                             | 37.6 us: 1.38x faster                                                       |
| coroutines              | 31.8 ms                                                             | 23.1 ms: 1.37x faster                                                       |
| json_dumps              | 13.7 ms                                                             | 10.0 ms: 1.37x faster                                                       |
| unpickle_pure_python    | 300 us                                                              | 220 us: 1.36x faster                                                        |
| mako                    | 14.7 ms                                                             | 10.8 ms: 1.36x faster                                                       |
| float                   | 110 ms                                                              | 81.6 ms: 1.35x faster                                                       |
| pycparser               | 1.53 sec                                                            | 1.16 sec: 1.32x faster                                                      |
| pprint_pformat          | 1.98 sec                                                            | 1.50 sec: 1.31x faster                                                      |
| async_tree_cpu_io_mixed | 944 ms                                                              | 727 ms: 1.30x faster                                                        |
| tornado_http            | 129 ms                                                              | 99.8 ms: 1.29x faster                                                       |
| logging_simple          | 8.21 us                                                             | 6.36 us: 1.29x faster                                                       |
| pprint_safe_repr        | 953 ms                                                              | 742 ms: 1.29x faster                                                        |
| logging_format          | 9.07 us                                                             | 7.16 us: 1.27x faster                                                       |
| fannkuch                | 485 ms                                                              | 385 ms: 1.26x faster                                                        |
| xml_etree_process       | 74.8 ms                                                             | 59.4 ms: 1.26x faster                                                       |
| 2to3                    | 336 ms                                                              | 270 ms: 1.24x faster                                                        |
| mypy2                   | 432 ms                                                              | 351 ms: 1.23x faster                                                        |
| unpack_sequence         | 65.6 ns                                                             | 53.4 ns: 1.23x faster                                                       |
| nqueens                 | 98.8 ms                                                             | 80.6 ms: 1.23x faster                                                       |
| regex_compile           | 177 ms                                                              | 146 ms: 1.21x faster                                                        |
| deepcopy                | 438 us                                                              | 366 us: 1.20x faster                                                        |
| scimark_fft             | 425 ms                                                              | 356 ms: 1.19x faster                                                        |
| deepcopy_reduce         | 3.80 us                                                             | 3.21 us: 1.18x faster                                                       |
| sqlglot_optimize        | 65.3 ms                                                             | 55.3 ms: 1.18x faster                                                       |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.77 ms: 1.18x faster                                                       |
| docutils                | 3.19 sec                                                            | 2.71 sec: 1.18x faster                                                      |
| sqlglot_normalize       | 135 ms                                                              | 114 ms: 1.18x faster                                                        |
| comprehensions          | 27.3 us                                                             | 23.5 us: 1.16x faster                                                       |
| bench_thread_pool       | 954 us                                                              | 838 us: 1.14x faster                                                        |
| sqlalchemy_declarative  | 166 ms                                                              | 147 ms: 1.13x faster                                                        |
| regex_v8                | 24.9 ms                                                             | 22.2 ms: 1.12x faster                                                       |
| json_loads              | 29.3 us                                                             | 26.2 us: 1.12x faster                                                       |
| xml_etree_generate      | 94.9 ms                                                             | 84.8 ms: 1.12x faster                                                       |
| dulwich_log             | 76.3 ms                                                             | 68.3 ms: 1.12x faster                                                       |
| sqlalchemy_imperative   | 21.2 ms                                                             | 19.1 ms: 1.11x faster                                                       |
| sqlite_synth            | 2.97 us                                                             | 2.69 us: 1.11x faster                                                       |
| meteor_contest          | 115 ms                                                              | 104 ms: 1.10x faster                                                        |
| create_gc_cycles        | 1.64 ms                                                             | 1.50 ms: 1.10x faster                                                       |
| json                    | 5.41 ms                                                             | 5.00 ms: 1.08x faster                                                       |
| xml_etree_iterparse     | 111 ms                                                              | 104 ms: 1.08x faster                                                        |
| mdp                     | 2.75 sec                                                            | 2.58 sec: 1.07x faster                                                      |
| xml_etree_parse         | 164 ms                                                              | 154 ms: 1.06x faster                                                        |
| regex_dna               | 213 ms                                                              | 200 ms: 1.06x faster                                                        |
| pathlib                 | 19.8 ms                                                             | 18.7 ms: 1.06x faster                                                       |
| pickle_list             | 4.73 us                                                             | 4.62 us: 1.02x faster                                                       |
| unpickle                | 15.0 us                                                             | 14.7 us: 1.02x faster                                                       |
| bench_mp_pool           | 24.0 ms                                                             | 24.0 ms: 1.00x slower                                                       |
| telco                   | 6.67 ms                                                             | 6.94 ms: 1.04x slower                                                       |
| pidigits                | 190 ms                                                              | 197 ms: 1.04x slower                                                        |
| pickle                  | 10.2 us                                                             | 10.7 us: 1.05x slower                                                       |
| async_generators        | 420 ms                                                              | 451 ms: 1.07x slower                                                        |
| gc_traversal            | 3.53 ms                                                             | 3.89 ms: 1.10x slower                                                       |
| pickle_dict             | 27.8 us                                                             | 30.7 us: 1.11x slower                                                       |
| regex_effbot            | 3.22 ms                                                             | 3.57 ms: 1.11x slower                                                       |
| python_startup_no_site  | 5.80 ms                                                             | 6.74 ms: 1.16x slower                                                       |
| dask                    | 437 ms                                                              | 542 ms: 1.24x slower                                                        |
| coverage                | 70.6 ms                                                             | 102 ms: 1.44x slower                                                        |
| Geometric mean          | (ref)                                                               | 1.24x faster                                                                |

Benchmark hidden because not significant (1): unpickle_list
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
