
# Results vs. 3.10.4

- fork: brandtbucher
- ref: immortal_interpreter
- machine: linux-x86_64
- commit hash: fd95518
- commit date: 2023-04-26
- overall geometric mean: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230426-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-fd95518 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 269 ms: 1.25x faster                                                         |
| chameleon      | 9.13 ms                                                             | 7.01 ms: 1.30x faster                                                        |
| docutils       | 3.19 sec                                                            | 2.72 sec: 1.17x faster                                                       |
| html5lib       | 86.4 ms                                                             | 65.6 ms: 1.32x faster                                                        |
| tornado_http   | 129 ms                                                              | 106 ms: 1.22x faster                                                         |
| Geometric mean | (ref)                                                               | 1.25x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230426-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-fd95518 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 146 ms                                                              | 88.5 ms: 1.65x faster                                                        |
| float          | 110 ms                                                              | 81.1 ms: 1.35x faster                                                        |
| pidigits       | 190 ms                                                              | 189 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                               | 1.31x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230426-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-fd95518 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 143 ms: 1.24x faster                                                         |
| regex_v8       | 24.9 ms                                                             | 22.4 ms: 1.11x faster                                                        |
| regex_dna      | 213 ms                                                              | 207 ms: 1.03x faster                                                         |
| regex_effbot   | 3.22 ms                                                             | 3.49 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                               | 1.07x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230426-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-fd95518 |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 315 us: 1.45x faster                                                         |
| unpickle_pure_python | 300 us                                                              | 216 us: 1.39x faster                                                         |
| json_dumps           | 13.7 ms                                                             | 9.92 ms: 1.38x faster                                                        |
| xml_etree_process    | 74.8 ms                                                             | 58.8 ms: 1.27x faster                                                        |
| json_loads           | 29.3 us                                                             | 25.6 us: 1.14x faster                                                        |
| xml_etree_generate   | 94.9 ms                                                             | 84.6 ms: 1.12x faster                                                        |
| xml_etree_iterparse  | 111 ms                                                              | 103 ms: 1.08x faster                                                         |
| xml_etree_parse      | 164 ms                                                              | 154 ms: 1.06x faster                                                         |
| pickle_list          | 4.73 us                                                             | 4.52 us: 1.05x faster                                                        |
| unpickle             | 15.0 us                                                             | 14.7 us: 1.02x faster                                                        |
| pickle               | 10.2 us                                                             | 10.4 us: 1.01x slower                                                        |
| pickle_dict          | 27.8 us                                                             | 30.9 us: 1.11x slower                                                        |
| Geometric mean       | (ref)                                                               | 1.13x faster                                                                 |

Benchmark hidden because not significant (1): unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230426-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-fd95518 |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 9.13 ms: 1.55x faster                                                        |
| python_startup_no_site | 5.80 ms                                                             | 6.69 ms: 1.16x slower                                                        |
| Geometric mean         | (ref)                                                               | 1.16x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230426-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-fd95518 |
|-----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                             | 10.8 ms: 1.36x faster                                                        |
| genshi_text     | 30.4 ms                                                             | 22.8 ms: 1.33x faster                                                        |
| django_template | 45.8 ms                                                             | 34.7 ms: 1.32x faster                                                        |
| genshi_xml      | 64.3 ms                                                             | 51.6 ms: 1.25x faster                                                        |
| Geometric mean  | (ref)                                                               | 1.32x faster                                                                 |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230426-linux-x86_64-brandtbucher-immortal_interpreter-3.12.0a7+-fd95518 |
|-------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| generators              | 75.7 ms                                                             | 31.2 ms: 2.42x faster                                                        |
| deltablue               | 7.30 ms                                                             | 3.53 ms: 2.07x faster                                                        |
| asyncio_tcp             | 922 ms                                                              | 505 ms: 1.82x faster                                                         |
| richards                | 74.2 ms                                                             | 43.4 ms: 1.71x faster                                                        |
| logging_silent          | 169 ns                                                              | 99.0 ns: 1.71x faster                                                        |
| nbody                   | 146 ms                                                              | 88.5 ms: 1.65x faster                                                        |
| go                      | 226 ms                                                              | 139 ms: 1.63x faster                                                         |
| scimark_sor             | 198 ms                                                              | 122 ms: 1.62x faster                                                         |
| raytrace                | 470 ms                                                              | 300 ms: 1.57x faster                                                         |
| sqlglot_parse           | 2.07 ms                                                             | 1.32 ms: 1.56x faster                                                        |
| hexiom                  | 9.50 ms                                                             | 6.13 ms: 1.55x faster                                                        |
| python_startup          | 14.1 ms                                                             | 9.13 ms: 1.55x faster                                                        |
| chaos                   | 106 ms                                                              | 69.2 ms: 1.53x faster                                                        |
| scimark_monte_carlo     | 109 ms                                                              | 71.3 ms: 1.52x faster                                                        |
| pyflate                 | 671 ms                                                              | 446 ms: 1.51x faster                                                         |
| sqlglot_transpile       | 2.45 ms                                                             | 1.65 ms: 1.49x faster                                                        |
| scimark_lu              | 160 ms                                                              | 110 ms: 1.45x faster                                                         |
| pickle_pure_python      | 457 us                                                              | 315 us: 1.45x faster                                                         |
| crypto_pyaes            | 117 ms                                                              | 80.5 ms: 1.45x faster                                                        |
| spectral_norm           | 150 ms                                                              | 105 ms: 1.43x faster                                                         |
| async_tree_io           | 1.78 sec                                                            | 1.28 sec: 1.39x faster                                                       |
| unpickle_pure_python    | 300 us                                                              | 216 us: 1.39x faster                                                         |
| coroutines              | 31.8 ms                                                             | 23.0 ms: 1.38x faster                                                        |
| json_dumps              | 13.7 ms                                                             | 9.92 ms: 1.38x faster                                                        |
| mako                    | 14.7 ms                                                             | 10.8 ms: 1.36x faster                                                        |
| float                   | 110 ms                                                              | 81.1 ms: 1.35x faster                                                        |
| async_tree_none         | 713 ms                                                              | 528 ms: 1.35x faster                                                         |
| deepcopy_memo           | 51.8 us                                                             | 38.5 us: 1.35x faster                                                        |
| pprint_pformat          | 1.98 sec                                                            | 1.47 sec: 1.35x faster                                                       |
| genshi_text             | 30.4 ms                                                             | 22.8 ms: 1.33x faster                                                        |
| pycparser               | 1.53 sec                                                            | 1.15 sec: 1.33x faster                                                       |
| django_template         | 45.8 ms                                                             | 34.7 ms: 1.32x faster                                                        |
| logging_simple          | 8.21 us                                                             | 6.22 us: 1.32x faster                                                        |
| pprint_safe_repr        | 953 ms                                                              | 724 ms: 1.32x faster                                                         |
| html5lib                | 86.4 ms                                                             | 65.6 ms: 1.32x faster                                                        |
| async_tree_memoization  | 853 ms                                                              | 650 ms: 1.31x faster                                                         |
| logging_format          | 9.07 us                                                             | 6.96 us: 1.30x faster                                                        |
| chameleon               | 9.13 ms                                                             | 7.01 ms: 1.30x faster                                                        |
| fannkuch                | 485 ms                                                              | 374 ms: 1.30x faster                                                         |
| thrift                  | 1.04 ms                                                             | 800 us: 1.30x faster                                                         |
| xml_etree_process       | 74.8 ms                                                             | 58.8 ms: 1.27x faster                                                        |
| async_tree_cpu_io_mixed | 944 ms                                                              | 750 ms: 1.26x faster                                                         |
| 2to3                    | 336 ms                                                              | 269 ms: 1.25x faster                                                         |
| genshi_xml              | 64.3 ms                                                             | 51.6 ms: 1.25x faster                                                        |
| regex_compile           | 177 ms                                                              | 143 ms: 1.24x faster                                                         |
| nqueens                 | 98.8 ms                                                             | 79.8 ms: 1.24x faster                                                        |
| mypy2                   | 432 ms                                                              | 349 ms: 1.24x faster                                                         |
| tornado_http            | 129 ms                                                              | 106 ms: 1.22x faster                                                         |
| unpack_sequence         | 65.6 ns                                                             | 54.1 ns: 1.21x faster                                                        |
| scimark_fft             | 425 ms                                                              | 352 ms: 1.21x faster                                                         |
| sqlglot_normalize       | 135 ms                                                              | 112 ms: 1.21x faster                                                         |
| sqlglot_optimize        | 65.3 ms                                                             | 54.3 ms: 1.20x faster                                                        |
| deepcopy                | 438 us                                                              | 366 us: 1.20x faster                                                         |
| deepcopy_reduce         | 3.80 us                                                             | 3.19 us: 1.19x faster                                                        |
| docutils                | 3.19 sec                                                            | 2.72 sec: 1.17x faster                                                       |
| comprehensions          | 27.3 us                                                             | 23.4 us: 1.17x faster                                                        |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.85 ms: 1.16x faster                                                        |
| json_loads              | 29.3 us                                                             | 25.6 us: 1.14x faster                                                        |
| bench_thread_pool       | 954 us                                                              | 835 us: 1.14x faster                                                         |
| sqlalchemy_declarative  | 166 ms                                                              | 146 ms: 1.14x faster                                                         |
| dulwich_log             | 76.3 ms                                                             | 67.8 ms: 1.13x faster                                                        |
| xml_etree_generate      | 94.9 ms                                                             | 84.6 ms: 1.12x faster                                                        |
| regex_v8                | 24.9 ms                                                             | 22.4 ms: 1.11x faster                                                        |
| sympy_integrate         | 24.3 ms                                                             | 21.9 ms: 1.11x faster                                                        |
| pylint                  | 521 ms                                                              | 471 ms: 1.11x faster                                                         |
| json                    | 5.41 ms                                                             | 4.91 ms: 1.10x faster                                                        |
| sqlite_synth            | 2.97 us                                                             | 2.71 us: 1.10x faster                                                        |
| djangocms               | 36.3 us                                                             | 33.3 us: 1.09x faster                                                        |
| create_gc_cycles        | 1.64 ms                                                             | 1.51 ms: 1.09x faster                                                        |
| sqlalchemy_imperative   | 21.2 ms                                                             | 19.5 ms: 1.09x faster                                                        |
| xml_etree_iterparse     | 111 ms                                                              | 103 ms: 1.08x faster                                                         |
| sympy_expand            | 540 ms                                                              | 498 ms: 1.08x faster                                                         |
| pathlib                 | 19.8 ms                                                             | 18.5 ms: 1.07x faster                                                        |
| mdp                     | 2.75 sec                                                            | 2.59 sec: 1.06x faster                                                       |
| xml_etree_parse         | 164 ms                                                              | 154 ms: 1.06x faster                                                         |
| sympy_str               | 328 ms                                                              | 311 ms: 1.05x faster                                                         |
| pickle_list             | 4.73 us                                                             | 4.52 us: 1.05x faster                                                        |
| regex_dna               | 213 ms                                                              | 207 ms: 1.03x faster                                                         |
| meteor_contest          | 115 ms                                                              | 112 ms: 1.02x faster                                                         |
| unpickle                | 15.0 us                                                             | 14.7 us: 1.02x faster                                                        |
| sympy_sum               | 185 ms                                                              | 183 ms: 1.01x faster                                                         |
| pidigits                | 190 ms                                                              | 189 ms: 1.00x faster                                                         |
| pickle                  | 10.2 us                                                             | 10.4 us: 1.01x slower                                                        |
| telco                   | 6.67 ms                                                             | 6.90 ms: 1.03x slower                                                        |
| async_generators        | 420 ms                                                              | 437 ms: 1.04x slower                                                         |
| regex_effbot            | 3.22 ms                                                             | 3.49 ms: 1.08x slower                                                        |
| pickle_dict             | 27.8 us                                                             | 30.9 us: 1.11x slower                                                        |
| gc_traversal            | 3.53 ms                                                             | 3.99 ms: 1.13x slower                                                        |
| python_startup_no_site  | 5.80 ms                                                             | 6.69 ms: 1.16x slower                                                        |
| dask                    | 437 ms                                                              | 539 ms: 1.23x slower                                                         |
| coverage                | 70.6 ms                                                             | 100 ms: 1.42x slower                                                         |
| Geometric mean          | (ref)                                                               | 1.23x faster                                                                 |

Benchmark hidden because not significant (2): unpickle_list, bench_mp_pool
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn
