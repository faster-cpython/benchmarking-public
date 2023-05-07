
# Results vs. 3.10.4

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 42f54d1
- commit date: 2023-05-06
- overall geometric mean: 1.25x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230506-linux-x86_64-python-main-3.12.0a7+-42f54d1 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 269 ms: 1.25x faster                                   |
| docutils       | 3.19 sec                                                            | 2.72 sec: 1.17x faster                                 |
| tornado_http   | 129 ms                                                              | 99.9 ms: 1.29x faster                                  |
| Geometric mean | (ref)                                                               | 1.24x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230506-linux-x86_64-python-main-3.12.0a7+-42f54d1 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 146 ms                                                              | 88.0 ms: 1.66x faster                                  |
| float          | 110 ms                                                              | 81.2 ms: 1.35x faster                                  |
| pidigits       | 190 ms                                                              | 197 ms: 1.04x slower                                   |
| Geometric mean | (ref)                                                               | 1.29x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230506-linux-x86_64-python-main-3.12.0a7+-42f54d1 |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 146 ms: 1.22x faster                                   |
| regex_v8       | 24.9 ms                                                             | 22.3 ms: 1.12x faster                                  |
| regex_dna      | 213 ms                                                              | 200 ms: 1.06x faster                                   |
| regex_effbot   | 3.22 ms                                                             | 3.54 ms: 1.10x slower                                  |
| Geometric mean | (ref)                                                               | 1.07x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230506-linux-x86_64-python-main-3.12.0a7+-42f54d1 |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 311 us: 1.47x faster                                   |
| unpickle_pure_python | 300 us                                                              | 216 us: 1.39x faster                                   |
| json_dumps           | 13.7 ms                                                             | 9.94 ms: 1.38x faster                                  |
| xml_etree_process    | 74.8 ms                                                             | 59.0 ms: 1.27x faster                                  |
| json_loads           | 29.3 us                                                             | 25.4 us: 1.15x faster                                  |
| xml_etree_generate   | 94.9 ms                                                             | 85.3 ms: 1.11x faster                                  |
| xml_etree_iterparse  | 111 ms                                                              | 104 ms: 1.07x faster                                   |
| xml_etree_parse      | 164 ms                                                              | 155 ms: 1.06x faster                                   |
| unpickle_list        | 4.94 us                                                             | 4.85 us: 1.02x faster                                  |
| pickle               | 10.2 us                                                             | 10.6 us: 1.04x slower                                  |
| pickle_dict          | 27.8 us                                                             | 31.4 us: 1.13x slower                                  |
| Geometric mean       | (ref)                                                               | 1.12x faster                                           |

Benchmark hidden because not significant (2): pickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230506-linux-x86_64-python-main-3.12.0a7+-42f54d1 |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 9.17 ms: 1.54x faster                                  |
| python_startup_no_site | 5.80 ms                                                             | 6.69 ms: 1.15x slower                                  |
| Geometric mean         | (ref)                                                               | 1.16x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230506-linux-x86_64-python-main-3.12.0a7+-42f54d1 |
|-----------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| mako      | 14.7 ms                                                             | 11.0 ms: 1.34x faster                                  |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230506-linux-x86_64-python-main-3.12.0a7+-42f54d1 |
|-------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| generators              | 75.7 ms                                                             | 31.3 ms: 2.42x faster                                  |
| deltablue               | 7.30 ms                                                             | 3.51 ms: 2.08x faster                                  |
| asyncio_tcp             | 922 ms                                                              | 512 ms: 1.80x faster                                   |
| richards                | 74.2 ms                                                             | 43.0 ms: 1.73x faster                                  |
| logging_silent          | 169 ns                                                              | 99.3 ns: 1.70x faster                                  |
| nbody                   | 146 ms                                                              | 88.0 ms: 1.66x faster                                  |
| go                      | 226 ms                                                              | 137 ms: 1.65x faster                                   |
| scimark_sor             | 198 ms                                                              | 124 ms: 1.59x faster                                   |
| sqlglot_parse           | 2.07 ms                                                             | 1.32 ms: 1.57x faster                                  |
| raytrace                | 470 ms                                                              | 301 ms: 1.56x faster                                   |
| python_startup          | 14.1 ms                                                             | 9.17 ms: 1.54x faster                                  |
| chaos                   | 106 ms                                                              | 68.9 ms: 1.54x faster                                  |
| hexiom                  | 9.50 ms                                                             | 6.22 ms: 1.53x faster                                  |
| pyflate                 | 671 ms                                                              | 441 ms: 1.52x faster                                   |
| sqlglot_transpile       | 2.45 ms                                                             | 1.64 ms: 1.50x faster                                  |
| scimark_monte_carlo     | 109 ms                                                              | 72.7 ms: 1.49x faster                                  |
| pickle_pure_python      | 457 us                                                              | 311 us: 1.47x faster                                   |
| crypto_pyaes            | 117 ms                                                              | 80.2 ms: 1.45x faster                                  |
| unpack_sequence         | 65.6 ns                                                             | 45.1 ns: 1.45x faster                                  |
| async_tree_io           | 1.78 sec                                                            | 1.23 sec: 1.45x faster                                 |
| coroutines              | 31.8 ms                                                             | 22.1 ms: 1.44x faster                                  |
| async_tree_none         | 713 ms                                                              | 498 ms: 1.43x faster                                   |
| scimark_lu              | 160 ms                                                              | 113 ms: 1.41x faster                                   |
| spectral_norm           | 150 ms                                                              | 108 ms: 1.39x faster                                   |
| async_tree_memoization  | 853 ms                                                              | 613 ms: 1.39x faster                                   |
| unpickle_pure_python    | 300 us                                                              | 216 us: 1.39x faster                                   |
| json_dumps              | 13.7 ms                                                             | 9.94 ms: 1.38x faster                                  |
| deepcopy_memo           | 51.8 us                                                             | 37.8 us: 1.37x faster                                  |
| float                   | 110 ms                                                              | 81.2 ms: 1.35x faster                                  |
| mako                    | 14.7 ms                                                             | 11.0 ms: 1.34x faster                                  |
| pprint_pformat          | 1.98 sec                                                            | 1.49 sec: 1.33x faster                                 |
| pycparser               | 1.53 sec                                                            | 1.16 sec: 1.32x faster                                 |
| pprint_safe_repr        | 953 ms                                                              | 728 ms: 1.31x faster                                   |
| async_tree_cpu_io_mixed | 944 ms                                                              | 721 ms: 1.31x faster                                   |
| logging_simple          | 8.21 us                                                             | 6.31 us: 1.30x faster                                  |
| logging_format          | 9.07 us                                                             | 7.00 us: 1.30x faster                                  |
| tornado_http            | 129 ms                                                              | 99.9 ms: 1.29x faster                                  |
| fannkuch                | 485 ms                                                              | 380 ms: 1.28x faster                                   |
| xml_etree_process       | 74.8 ms                                                             | 59.0 ms: 1.27x faster                                  |
| 2to3                    | 336 ms                                                              | 269 ms: 1.25x faster                                   |
| nqueens                 | 98.8 ms                                                             | 80.2 ms: 1.23x faster                                  |
| mypy2                   | 432 ms                                                              | 351 ms: 1.23x faster                                   |
| deepcopy                | 438 us                                                              | 358 us: 1.22x faster                                   |
| regex_compile           | 177 ms                                                              | 146 ms: 1.22x faster                                   |
| deepcopy_reduce         | 3.80 us                                                             | 3.14 us: 1.21x faster                                  |
| sqlglot_normalize       | 135 ms                                                              | 111 ms: 1.21x faster                                   |
| sqlglot_optimize        | 65.3 ms                                                             | 54.7 ms: 1.19x faster                                  |
| scimark_fft             | 425 ms                                                              | 358 ms: 1.19x faster                                   |
| docutils                | 3.19 sec                                                            | 2.72 sec: 1.17x faster                                 |
| comprehensions          | 27.3 us                                                             | 23.4 us: 1.16x faster                                  |
| json_loads              | 29.3 us                                                             | 25.4 us: 1.15x faster                                  |
| bench_thread_pool       | 954 us                                                              | 829 us: 1.15x faster                                   |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.91 ms: 1.14x faster                                  |
| sqlalchemy_declarative  | 166 ms                                                              | 147 ms: 1.13x faster                                   |
| dulwich_log             | 76.3 ms                                                             | 67.7 ms: 1.13x faster                                  |
| json                    | 5.41 ms                                                             | 4.80 ms: 1.13x faster                                  |
| regex_v8                | 24.9 ms                                                             | 22.3 ms: 1.12x faster                                  |
| create_gc_cycles        | 1.64 ms                                                             | 1.47 ms: 1.11x faster                                  |
| xml_etree_generate      | 94.9 ms                                                             | 85.3 ms: 1.11x faster                                  |
| sqlalchemy_imperative   | 21.2 ms                                                             | 19.3 ms: 1.10x faster                                  |
| meteor_contest          | 115 ms                                                              | 105 ms: 1.09x faster                                   |
| sqlite_synth            | 2.97 us                                                             | 2.76 us: 1.08x faster                                  |
| xml_etree_iterparse     | 111 ms                                                              | 104 ms: 1.07x faster                                   |
| mdp                     | 2.75 sec                                                            | 2.58 sec: 1.07x faster                                 |
| regex_dna               | 213 ms                                                              | 200 ms: 1.06x faster                                   |
| xml_etree_parse         | 164 ms                                                              | 155 ms: 1.06x faster                                   |
| pathlib                 | 19.8 ms                                                             | 18.9 ms: 1.05x faster                                  |
| unpickle_list           | 4.94 us                                                             | 4.85 us: 1.02x faster                                  |
| telco                   | 6.67 ms                                                             | 6.88 ms: 1.03x slower                                  |
| pickle                  | 10.2 us                                                             | 10.6 us: 1.04x slower                                  |
| pidigits                | 190 ms                                                              | 197 ms: 1.04x slower                                   |
| gc_traversal            | 3.53 ms                                                             | 3.68 ms: 1.04x slower                                  |
| async_generators        | 420 ms                                                              | 451 ms: 1.07x slower                                   |
| regex_effbot            | 3.22 ms                                                             | 3.54 ms: 1.10x slower                                  |
| pickle_dict             | 27.8 us                                                             | 31.4 us: 1.13x slower                                  |
| python_startup_no_site  | 5.80 ms                                                             | 6.69 ms: 1.15x slower                                  |
| dask                    | 437 ms                                                              | 537 ms: 1.23x slower                                   |
| coverage                | 70.6 ms                                                             | 102 ms: 1.45x slower                                   |
| Geometric mean          | (ref)                                                               | 1.25x faster                                           |

Benchmark hidden because not significant (3): bench_mp_pool, pickle_list, unpickle
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
