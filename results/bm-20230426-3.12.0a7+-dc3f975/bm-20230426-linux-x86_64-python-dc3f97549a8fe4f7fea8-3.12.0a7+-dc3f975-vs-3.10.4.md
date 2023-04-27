
# Results vs. 3.10.4

- fork: python
- ref: dc3f97549a8fe4f7fea8
- machine: linux-x86_64
- commit hash: dc3f975
- commit date: 2023-04-26
- overall geometric mean: 1.23x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230426-linux-x86_64-python-dc3f97549a8fe4f7fea8-3.12.0a7+-dc3f975 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 268 ms: 1.25x faster                                                   |
| chameleon      | 9.13 ms                                                             | 6.94 ms: 1.32x faster                                                  |
| docutils       | 3.19 sec                                                            | 2.70 sec: 1.18x faster                                                 |
| html5lib       | 86.4 ms                                                             | 65.2 ms: 1.32x faster                                                  |
| tornado_http   | 129 ms                                                              | 105 ms: 1.23x faster                                                   |
| Geometric mean | (ref)                                                               | 1.26x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230426-linux-x86_64-python-dc3f97549a8fe4f7fea8-3.12.0a7+-dc3f975 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 146 ms                                                              | 88.2 ms: 1.65x faster                                                  |
| float          | 110 ms                                                              | 80.0 ms: 1.37x faster                                                  |
| pidigits       | 190 ms                                                              | 198 ms: 1.04x slower                                                   |
| Geometric mean | (ref)                                                               | 1.30x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230426-linux-x86_64-python-dc3f97549a8fe4f7fea8-3.12.0a7+-dc3f975 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 145 ms: 1.22x faster                                                   |
| regex_v8       | 24.9 ms                                                             | 22.2 ms: 1.13x faster                                                  |
| regex_dna      | 213 ms                                                              | 204 ms: 1.04x faster                                                   |
| regex_effbot   | 3.22 ms                                                             | 3.75 ms: 1.17x slower                                                  |
| Geometric mean | (ref)                                                               | 1.05x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230426-linux-x86_64-python-dc3f97549a8fe4f7fea8-3.12.0a7+-dc3f975 |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 313 us: 1.46x faster                                                   |
| unpickle_pure_python | 300 us                                                              | 218 us: 1.38x faster                                                   |
| json_dumps           | 13.7 ms                                                             | 10.0 ms: 1.37x faster                                                  |
| xml_etree_process    | 74.8 ms                                                             | 58.6 ms: 1.28x faster                                                  |
| json_loads           | 29.3 us                                                             | 25.8 us: 1.14x faster                                                  |
| xml_etree_generate   | 94.9 ms                                                             | 83.9 ms: 1.13x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                              | 103 ms: 1.08x faster                                                   |
| xml_etree_parse      | 164 ms                                                              | 152 ms: 1.08x faster                                                   |
| pickle_list          | 4.73 us                                                             | 4.62 us: 1.02x faster                                                  |
| unpickle_list        | 4.94 us                                                             | 4.90 us: 1.01x faster                                                  |
| pickle               | 10.2 us                                                             | 10.7 us: 1.05x slower                                                  |
| pickle_dict          | 27.8 us                                                             | 31.6 us: 1.14x slower                                                  |
| Geometric mean       | (ref)                                                               | 1.12x faster                                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230426-linux-x86_64-python-dc3f97549a8fe4f7fea8-3.12.0a7+-dc3f975 |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 9.03 ms: 1.57x faster                                                  |
| python_startup_no_site | 5.80 ms                                                             | 6.62 ms: 1.14x slower                                                  |
| Geometric mean         | (ref)                                                               | 1.17x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230426-linux-x86_64-python-dc3f97549a8fe4f7fea8-3.12.0a7+-dc3f975 |
|-----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 14.7 ms                                                             | 10.9 ms: 1.36x faster                                                  |
| genshi_text     | 30.4 ms                                                             | 22.7 ms: 1.34x faster                                                  |
| django_template | 45.8 ms                                                             | 34.7 ms: 1.32x faster                                                  |
| genshi_xml      | 64.3 ms                                                             | 51.5 ms: 1.25x faster                                                  |
| Geometric mean  | (ref)                                                               | 1.32x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230426-linux-x86_64-python-dc3f97549a8fe4f7fea8-3.12.0a7+-dc3f975 |
|-------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 75.7 ms                                                             | 32.4 ms: 2.33x faster                                                  |
| deltablue               | 7.30 ms                                                             | 3.53 ms: 2.07x faster                                                  |
| asyncio_tcp             | 922 ms                                                              | 507 ms: 1.82x faster                                                   |
| richards                | 74.2 ms                                                             | 43.4 ms: 1.71x faster                                                  |
| logging_silent          | 169 ns                                                              | 99.9 ns: 1.69x faster                                                  |
| go                      | 226 ms                                                              | 135 ms: 1.67x faster                                                   |
| nbody                   | 146 ms                                                              | 88.2 ms: 1.65x faster                                                  |
| scimark_sor             | 198 ms                                                              | 126 ms: 1.57x faster                                                   |
| python_startup          | 14.1 ms                                                             | 9.03 ms: 1.57x faster                                                  |
| raytrace                | 470 ms                                                              | 302 ms: 1.56x faster                                                   |
| sqlglot_parse           | 2.07 ms                                                             | 1.33 ms: 1.56x faster                                                  |
| chaos                   | 106 ms                                                              | 69.3 ms: 1.53x faster                                                  |
| hexiom                  | 9.50 ms                                                             | 6.27 ms: 1.52x faster                                                  |
| pyflate                 | 671 ms                                                              | 451 ms: 1.49x faster                                                   |
| sqlglot_transpile       | 2.45 ms                                                             | 1.65 ms: 1.49x faster                                                  |
| scimark_monte_carlo     | 109 ms                                                              | 73.1 ms: 1.49x faster                                                  |
| crypto_pyaes            | 117 ms                                                              | 79.5 ms: 1.47x faster                                                  |
| pickle_pure_python      | 457 us                                                              | 313 us: 1.46x faster                                                   |
| scimark_lu              | 160 ms                                                              | 112 ms: 1.42x faster                                                   |
| coroutines              | 31.8 ms                                                             | 22.5 ms: 1.41x faster                                                  |
| unpack_sequence         | 65.6 ns                                                             | 46.6 ns: 1.41x faster                                                  |
| async_tree_io           | 1.78 sec                                                            | 1.28 sec: 1.39x faster                                                 |
| spectral_norm           | 150 ms                                                              | 108 ms: 1.38x faster                                                   |
| unpickle_pure_python    | 300 us                                                              | 218 us: 1.38x faster                                                   |
| float                   | 110 ms                                                              | 80.0 ms: 1.37x faster                                                  |
| json_dumps              | 13.7 ms                                                             | 10.0 ms: 1.37x faster                                                  |
| mako                    | 14.7 ms                                                             | 10.9 ms: 1.36x faster                                                  |
| async_tree_none         | 713 ms                                                              | 527 ms: 1.35x faster                                                   |
| pycparser               | 1.53 sec                                                            | 1.14 sec: 1.35x faster                                                 |
| genshi_text             | 30.4 ms                                                             | 22.7 ms: 1.34x faster                                                  |
| pprint_pformat          | 1.98 sec                                                            | 1.48 sec: 1.33x faster                                                 |
| deepcopy_memo           | 51.8 us                                                             | 39.0 us: 1.33x faster                                                  |
| html5lib                | 86.4 ms                                                             | 65.2 ms: 1.32x faster                                                  |
| django_template         | 45.8 ms                                                             | 34.7 ms: 1.32x faster                                                  |
| logging_simple          | 8.21 us                                                             | 6.24 us: 1.32x faster                                                  |
| chameleon               | 9.13 ms                                                             | 6.94 ms: 1.32x faster                                                  |
| logging_format          | 9.07 us                                                             | 6.90 us: 1.31x faster                                                  |
| pprint_safe_repr        | 953 ms                                                              | 726 ms: 1.31x faster                                                   |
| async_tree_memoization  | 853 ms                                                              | 654 ms: 1.30x faster                                                   |
| thrift                  | 1.04 ms                                                             | 805 us: 1.29x faster                                                   |
| xml_etree_process       | 74.8 ms                                                             | 58.6 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed | 944 ms                                                              | 747 ms: 1.26x faster                                                   |
| fannkuch                | 485 ms                                                              | 385 ms: 1.26x faster                                                   |
| 2to3                    | 336 ms                                                              | 268 ms: 1.25x faster                                                   |
| genshi_xml              | 64.3 ms                                                             | 51.5 ms: 1.25x faster                                                  |
| tornado_http            | 129 ms                                                              | 105 ms: 1.23x faster                                                   |
| mypy2                   | 432 ms                                                              | 351 ms: 1.23x faster                                                   |
| regex_compile           | 177 ms                                                              | 145 ms: 1.22x faster                                                   |
| sqlglot_normalize       | 135 ms                                                              | 111 ms: 1.21x faster                                                   |
| sqlglot_optimize        | 65.3 ms                                                             | 54.3 ms: 1.20x faster                                                  |
| deepcopy                | 438 us                                                              | 368 us: 1.19x faster                                                   |
| docutils                | 3.19 sec                                                            | 2.70 sec: 1.18x faster                                                 |
| deepcopy_reduce         | 3.80 us                                                             | 3.22 us: 1.18x faster                                                  |
| nqueens                 | 98.8 ms                                                             | 84.5 ms: 1.17x faster                                                  |
| scimark_fft             | 425 ms                                                              | 364 ms: 1.17x faster                                                   |
| comprehensions          | 27.3 us                                                             | 23.5 us: 1.16x faster                                                  |
| bench_thread_pool       | 954 us                                                              | 836 us: 1.14x faster                                                   |
| sqlalchemy_declarative  | 166 ms                                                              | 146 ms: 1.14x faster                                                   |
| json_loads              | 29.3 us                                                             | 25.8 us: 1.14x faster                                                  |
| xml_etree_generate      | 94.9 ms                                                             | 83.9 ms: 1.13x faster                                                  |
| regex_v8                | 24.9 ms                                                             | 22.2 ms: 1.13x faster                                                  |
| dulwich_log             | 76.3 ms                                                             | 67.9 ms: 1.12x faster                                                  |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 5.00 ms: 1.12x faster                                                  |
| create_gc_cycles        | 1.64 ms                                                             | 1.46 ms: 1.12x faster                                                  |
| sympy_integrate         | 24.3 ms                                                             | 21.9 ms: 1.11x faster                                                  |
| sqlalchemy_imperative   | 21.2 ms                                                             | 19.1 ms: 1.11x faster                                                  |
| pylint                  | 521 ms                                                              | 471 ms: 1.10x faster                                                   |
| sqlite_synth            | 2.97 us                                                             | 2.70 us: 1.10x faster                                                  |
| json                    | 5.41 ms                                                             | 4.96 ms: 1.09x faster                                                  |
| xml_etree_iterparse     | 111 ms                                                              | 103 ms: 1.08x faster                                                   |
| djangocms               | 36.3 us                                                             | 33.6 us: 1.08x faster                                                  |
| xml_etree_parse         | 164 ms                                                              | 152 ms: 1.08x faster                                                   |
| sympy_expand            | 540 ms                                                              | 501 ms: 1.08x faster                                                   |
| mdp                     | 2.75 sec                                                            | 2.57 sec: 1.07x faster                                                 |
| pathlib                 | 19.8 ms                                                             | 18.5 ms: 1.07x faster                                                  |
| sympy_str               | 328 ms                                                              | 312 ms: 1.05x faster                                                   |
| regex_dna               | 213 ms                                                              | 204 ms: 1.04x faster                                                   |
| pickle_list             | 4.73 us                                                             | 4.62 us: 1.02x faster                                                  |
| sympy_sum               | 185 ms                                                              | 182 ms: 1.02x faster                                                   |
| unpickle_list           | 4.94 us                                                             | 4.90 us: 1.01x faster                                                  |
| telco                   | 6.67 ms                                                             | 6.78 ms: 1.02x slower                                                  |
| pidigits                | 190 ms                                                              | 198 ms: 1.04x slower                                                   |
| pickle                  | 10.2 us                                                             | 10.7 us: 1.05x slower                                                  |
| gc_traversal            | 3.53 ms                                                             | 3.76 ms: 1.07x slower                                                  |
| async_generators        | 420 ms                                                              | 449 ms: 1.07x slower                                                   |
| pickle_dict             | 27.8 us                                                             | 31.6 us: 1.14x slower                                                  |
| python_startup_no_site  | 5.80 ms                                                             | 6.62 ms: 1.14x slower                                                  |
| regex_effbot            | 3.22 ms                                                             | 3.75 ms: 1.17x slower                                                  |
| dask                    | 437 ms                                                              | 541 ms: 1.24x slower                                                   |
| coverage                | 70.6 ms                                                             | 99.0 ms: 1.40x slower                                                  |
| Geometric mean          | (ref)                                                               | 1.23x faster                                                           |

Benchmark hidden because not significant (3): bench_mp_pool, unpickle, meteor_contest
Ignored benchmarks (3) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, flaskblogging, gunicorn
