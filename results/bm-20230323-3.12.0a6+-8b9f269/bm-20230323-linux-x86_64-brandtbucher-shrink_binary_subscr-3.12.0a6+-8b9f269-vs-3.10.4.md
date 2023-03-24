
# Results vs. 3.10.4

- fork: brandtbucher
- ref: shrink_binary_subscr
- machine: linux-x86_64
- commit hash: 8b9f269
- commit date: 2023-03-23
- overall geometric mean: 1.30x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-8b9f269 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 251 ms: 1.34x faster                                                         |
| chameleon      | 9.13 ms                                                             | 6.41 ms: 1.43x faster                                                        |
| docutils       | 3.19 sec                                                            | 2.53 sec: 1.26x faster                                                       |
| html5lib       | 86.4 ms                                                             | 61.9 ms: 1.39x faster                                                        |
| tornado_http   | 129 ms                                                              | 91.2 ms: 1.41x faster                                                        |
| Geometric mean | (ref)                                                               | 1.37x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-8b9f269 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 146 ms                                                              | 87.5 ms: 1.67x faster                                                        |
| float          | 110 ms                                                              | 73.3 ms: 1.50x faster                                                        |
| pidigits       | 190 ms                                                              | 188 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                               | 1.36x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-8b9f269 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 134 ms: 1.32x faster                                                         |
| regex_v8       | 24.9 ms                                                             | 21.4 ms: 1.16x faster                                                        |
| regex_dna      | 213 ms                                                              | 205 ms: 1.04x faster                                                         |
| regex_effbot   | 3.22 ms                                                             | 3.50 ms: 1.09x slower                                                        |
| Geometric mean | (ref)                                                               | 1.10x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-8b9f269 |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 286 us: 1.60x faster                                                         |
| unpickle_pure_python | 300 us                                                              | 199 us: 1.51x faster                                                         |
| json_dumps           | 13.7 ms                                                             | 9.65 ms: 1.42x faster                                                        |
| xml_etree_process    | 74.8 ms                                                             | 55.7 ms: 1.34x faster                                                        |
| json_loads           | 29.3 us                                                             | 24.4 us: 1.20x faster                                                        |
| xml_etree_generate   | 94.9 ms                                                             | 80.8 ms: 1.17x faster                                                        |
| unpickle             | 15.0 us                                                             | 13.3 us: 1.12x faster                                                        |
| xml_etree_iterparse  | 111 ms                                                              | 99.3 ms: 1.12x faster                                                        |
| xml_etree_parse      | 164 ms                                                              | 149 ms: 1.10x faster                                                         |
| pickle_list          | 4.73 us                                                             | 4.36 us: 1.08x faster                                                        |
| unpickle_list        | 4.94 us                                                             | 4.99 us: 1.01x slower                                                        |
| pickle               | 10.2 us                                                             | 10.5 us: 1.03x slower                                                        |
| pickle_dict          | 27.8 us                                                             | 31.5 us: 1.13x slower                                                        |
| Geometric mean       | (ref)                                                               | 1.18x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-8b9f269 |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 8.79 ms: 1.61x faster                                                        |
| python_startup_no_site | 5.80 ms                                                             | 6.49 ms: 1.12x slower                                                        |
| Geometric mean         | (ref)                                                               | 1.20x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-8b9f269 |
|-----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                             | 9.99 ms: 1.47x faster                                                        |
| genshi_text     | 30.4 ms                                                             | 21.4 ms: 1.42x faster                                                        |
| django_template | 45.8 ms                                                             | 33.3 ms: 1.38x faster                                                        |
| genshi_xml      | 64.3 ms                                                             | 47.7 ms: 1.35x faster                                                        |
| Geometric mean  | (ref)                                                               | 1.40x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230323-linux-x86_64-brandtbucher-shrink_binary_subscr-3.12.0a6+-8b9f269 |
|-------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 75.7 ms                                                             | 29.9 ms: 2.53x faster                                                        |
| deltablue               | 7.30 ms                                                             | 3.24 ms: 2.25x faster                                                        |
| asyncio_tcp             | 922 ms                                                              | 506 ms: 1.82x faster                                                         |
| scimark_sor             | 198 ms                                                              | 112 ms: 1.76x faster                                                         |
| logging_silent          | 169 ns                                                              | 96.6 ns: 1.75x faster                                                        |
| richards                | 74.2 ms                                                             | 44.3 ms: 1.67x faster                                                        |
| nbody                   | 146 ms                                                              | 87.5 ms: 1.67x faster                                                        |
| raytrace                | 470 ms                                                              | 285 ms: 1.65x faster                                                         |
| pyflate                 | 671 ms                                                              | 414 ms: 1.62x faster                                                         |
| python_startup          | 14.1 ms                                                             | 8.79 ms: 1.61x faster                                                        |
| pickle_pure_python      | 457 us                                                              | 286 us: 1.60x faster                                                         |
| spectral_norm           | 150 ms                                                              | 94.4 ms: 1.59x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                              | 68.3 ms: 1.59x faster                                                        |
| go                      | 226 ms                                                              | 142 ms: 1.59x faster                                                         |
| crypto_pyaes            | 117 ms                                                              | 73.8 ms: 1.58x faster                                                        |
| hexiom                  | 9.50 ms                                                             | 6.08 ms: 1.56x faster                                                        |
| chaos                   | 106 ms                                                              | 68.2 ms: 1.55x faster                                                        |
| unpack_sequence         | 65.6 ns                                                             | 42.8 ns: 1.53x faster                                                        |
| deepcopy_memo           | 51.8 us                                                             | 34.4 us: 1.51x faster                                                        |
| unpickle_pure_python    | 300 us                                                              | 199 us: 1.51x faster                                                         |
| float                   | 110 ms                                                              | 73.3 ms: 1.50x faster                                                        |
| mako                    | 14.7 ms                                                             | 9.99 ms: 1.47x faster                                                        |
| scimark_lu              | 160 ms                                                              | 109 ms: 1.47x faster                                                         |
| sqlglot_parse           | 2.07 ms                                                             | 1.43 ms: 1.45x faster                                                        |
| logging_simple          | 8.21 us                                                             | 5.73 us: 1.43x faster                                                        |
| logging_format          | 9.07 us                                                             | 6.34 us: 1.43x faster                                                        |
| chameleon               | 9.13 ms                                                             | 6.41 ms: 1.43x faster                                                        |
| sqlglot_transpile       | 2.45 ms                                                             | 1.73 ms: 1.42x faster                                                        |
| json_dumps              | 13.7 ms                                                             | 9.65 ms: 1.42x faster                                                        |
| genshi_text             | 30.4 ms                                                             | 21.4 ms: 1.42x faster                                                        |
| tornado_http            | 129 ms                                                              | 91.2 ms: 1.41x faster                                                        |
| pprint_pformat          | 1.98 sec                                                            | 1.41 sec: 1.41x faster                                                       |
| pprint_safe_repr        | 953 ms                                                              | 678 ms: 1.41x faster                                                         |
| html5lib                | 86.4 ms                                                             | 61.9 ms: 1.39x faster                                                        |
| pycparser               | 1.53 sec                                                            | 1.11 sec: 1.38x faster                                                       |
| django_template         | 45.8 ms                                                             | 33.3 ms: 1.38x faster                                                        |
| async_tree_io           | 1.78 sec                                                            | 1.30 sec: 1.37x faster                                                       |
| scimark_fft             | 425 ms                                                              | 310 ms: 1.37x faster                                                         |
| async_tree_none         | 713 ms                                                              | 523 ms: 1.36x faster                                                         |
| coroutines              | 31.8 ms                                                             | 23.4 ms: 1.36x faster                                                        |
| genshi_xml              | 64.3 ms                                                             | 47.7 ms: 1.35x faster                                                        |
| deepcopy                | 438 us                                                              | 326 us: 1.34x faster                                                         |
| xml_etree_process       | 74.8 ms                                                             | 55.7 ms: 1.34x faster                                                        |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.18 ms: 1.34x faster                                                        |
| aiohttp                 | 1.35 ms                                                             | 1.01 ms: 1.34x faster                                                        |
| 2to3                    | 336 ms                                                              | 251 ms: 1.34x faster                                                         |
| gunicorn                | 1.43 ms                                                             | 1.08 ms: 1.32x faster                                                        |
| regex_compile           | 177 ms                                                              | 134 ms: 1.32x faster                                                         |
| async_tree_memoization  | 853 ms                                                              | 649 ms: 1.31x faster                                                         |
| thrift                  | 1.04 ms                                                             | 793 us: 1.31x faster                                                         |
| mypy2                   | 432 ms                                                              | 335 ms: 1.29x faster                                                         |
| async_tree_cpu_io_mixed | 944 ms                                                              | 740 ms: 1.28x faster                                                         |
| deepcopy_reduce         | 3.80 us                                                             | 2.98 us: 1.28x faster                                                        |
| sqlglot_normalize       | 135 ms                                                              | 106 ms: 1.27x faster                                                         |
| sqlglot_optimize        | 65.3 ms                                                             | 51.4 ms: 1.27x faster                                                        |
| docutils                | 3.19 sec                                                            | 2.53 sec: 1.26x faster                                                       |
| fannkuch                | 485 ms                                                              | 388 ms: 1.25x faster                                                         |
| sqlalchemy_declarative  | 166 ms                                                              | 136 ms: 1.23x faster                                                         |
| nqueens                 | 98.8 ms                                                             | 81.6 ms: 1.21x faster                                                        |
| bench_thread_pool       | 954 us                                                              | 789 us: 1.21x faster                                                         |
| json_loads              | 29.3 us                                                             | 24.4 us: 1.20x faster                                                        |
| dulwich_log             | 76.3 ms                                                             | 63.8 ms: 1.20x faster                                                        |
| sqlalchemy_imperative   | 21.2 ms                                                             | 17.7 ms: 1.19x faster                                                        |
| sympy_integrate         | 24.3 ms                                                             | 20.6 ms: 1.18x faster                                                        |
| xml_etree_generate      | 94.9 ms                                                             | 80.8 ms: 1.17x faster                                                        |
| sympy_expand            | 540 ms                                                              | 463 ms: 1.17x faster                                                         |
| regex_v8                | 24.9 ms                                                             | 21.4 ms: 1.16x faster                                                        |
| json                    | 5.41 ms                                                             | 4.70 ms: 1.15x faster                                                        |
| sympy_str               | 328 ms                                                              | 286 ms: 1.15x faster                                                         |
| comprehensions          | 27.3 us                                                             | 24.0 us: 1.14x faster                                                        |
| sqlite_synth            | 2.97 us                                                             | 2.62 us: 1.14x faster                                                        |
| unpickle                | 15.0 us                                                             | 13.3 us: 1.12x faster                                                        |
| djangocms               | 36.3 us                                                             | 32.4 us: 1.12x faster                                                        |
| xml_etree_iterparse     | 111 ms                                                              | 99.3 ms: 1.12x faster                                                        |
| create_gc_cycles        | 1.64 ms                                                             | 1.46 ms: 1.12x faster                                                        |
| meteor_contest          | 115 ms                                                              | 102 ms: 1.12x faster                                                         |
| sympy_sum               | 185 ms                                                              | 166 ms: 1.11x faster                                                         |
| xml_etree_parse         | 164 ms                                                              | 149 ms: 1.10x faster                                                         |
| mdp                     | 2.75 sec                                                            | 2.52 sec: 1.09x faster                                                       |
| pathlib                 | 19.8 ms                                                             | 18.2 ms: 1.09x faster                                                        |
| pickle_list             | 4.73 us                                                             | 4.36 us: 1.08x faster                                                        |
| regex_dna               | 213 ms                                                              | 205 ms: 1.04x faster                                                         |
| telco                   | 6.67 ms                                                             | 6.49 ms: 1.03x faster                                                        |
| async_generators        | 420 ms                                                              | 415 ms: 1.01x faster                                                         |
| pidigits                | 190 ms                                                              | 188 ms: 1.01x faster                                                         |
| unpickle_list           | 4.94 us                                                             | 4.99 us: 1.01x slower                                                        |
| pickle                  | 10.2 us                                                             | 10.5 us: 1.03x slower                                                        |
| gc_traversal            | 3.53 ms                                                             | 3.66 ms: 1.04x slower                                                        |
| regex_effbot            | 3.22 ms                                                             | 3.50 ms: 1.09x slower                                                        |
| python_startup_no_site  | 5.80 ms                                                             | 6.49 ms: 1.12x slower                                                        |
| pickle_dict             | 27.8 us                                                             | 31.5 us: 1.13x slower                                                        |
| dask                    | 437 ms                                                              | 508 ms: 1.16x slower                                                         |
| coverage                | 70.6 ms                                                             | 95.7 ms: 1.36x slower                                                        |
| Geometric mean          | (ref)                                                               | 1.30x faster                                                                 |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: flaskblogging, pylint
