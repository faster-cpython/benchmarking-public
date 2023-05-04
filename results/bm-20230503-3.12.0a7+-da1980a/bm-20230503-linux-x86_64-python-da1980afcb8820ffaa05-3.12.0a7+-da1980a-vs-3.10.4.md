
# Results vs. 3.10.4

- fork: python
- ref: da1980afcb8820ffaa05
- machine: linux-x86_64
- commit hash: da1980a
- commit date: 2023-05-03
- overall geometric mean: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230503-linux-x86_64-python-da1980afcb8820ffaa05-3.12.0a7+-da1980a |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 271 ms: 1.24x faster                                                   |
| docutils       | 3.19 sec                                                            | 2.73 sec: 1.17x faster                                                 |
| tornado_http   | 129 ms                                                              | 99.9 ms: 1.29x faster                                                  |
| Geometric mean | (ref)                                                               | 1.23x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230503-linux-x86_64-python-da1980afcb8820ffaa05-3.12.0a7+-da1980a |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 146 ms                                                              | 87.4 ms: 1.67x faster                                                  |
| float          | 110 ms                                                              | 82.0 ms: 1.34x faster                                                  |
| pidigits       | 190 ms                                                              | 189 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                               | 1.31x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230503-linux-x86_64-python-da1980afcb8820ffaa05-3.12.0a7+-da1980a |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 145 ms: 1.22x faster                                                   |
| regex_v8       | 24.9 ms                                                             | 22.2 ms: 1.12x faster                                                  |
| regex_dna      | 213 ms                                                              | 205 ms: 1.04x faster                                                   |
| regex_effbot   | 3.22 ms                                                             | 3.40 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                               | 1.08x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230503-linux-x86_64-python-da1980afcb8820ffaa05-3.12.0a7+-da1980a |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 316 us: 1.45x faster                                                   |
| unpickle_pure_python | 300 us                                                              | 220 us: 1.37x faster                                                   |
| json_dumps           | 13.7 ms                                                             | 10.0 ms: 1.37x faster                                                  |
| xml_etree_process    | 74.8 ms                                                             | 58.7 ms: 1.27x faster                                                  |
| json_loads           | 29.3 us                                                             | 25.7 us: 1.14x faster                                                  |
| xml_etree_generate   | 94.9 ms                                                             | 84.3 ms: 1.13x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                              | 103 ms: 1.08x faster                                                   |
| xml_etree_parse      | 164 ms                                                              | 153 ms: 1.07x faster                                                   |
| pickle_list          | 4.73 us                                                             | 4.58 us: 1.03x faster                                                  |
| pickle               | 10.2 us                                                             | 10.5 us: 1.03x slower                                                  |
| unpickle_list        | 4.94 us                                                             | 5.10 us: 1.03x slower                                                  |
| pickle_dict          | 27.8 us                                                             | 31.8 us: 1.15x slower                                                  |
| Geometric mean       | (ref)                                                               | 1.12x faster                                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230503-linux-x86_64-python-da1980afcb8820ffaa05-3.12.0a7+-da1980a |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 9.14 ms: 1.55x faster                                                  |
| python_startup_no_site | 5.80 ms                                                             | 6.69 ms: 1.15x slower                                                  |
| Geometric mean         | (ref)                                                               | 1.16x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230503-linux-x86_64-python-da1980afcb8820ffaa05-3.12.0a7+-da1980a |
|-----------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako      | 14.7 ms                                                             | 10.9 ms: 1.35x faster                                                  |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230503-linux-x86_64-python-da1980afcb8820ffaa05-3.12.0a7+-da1980a |
|-------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 75.7 ms                                                             | 32.3 ms: 2.34x faster                                                  |
| deltablue               | 7.30 ms                                                             | 3.64 ms: 2.01x faster                                                  |
| asyncio_tcp             | 922 ms                                                              | 510 ms: 1.81x faster                                                   |
| nbody                   | 146 ms                                                              | 87.4 ms: 1.67x faster                                                  |
| richards                | 74.2 ms                                                             | 44.7 ms: 1.66x faster                                                  |
| go                      | 226 ms                                                              | 138 ms: 1.64x faster                                                   |
| logging_silent          | 169 ns                                                              | 104 ns: 1.63x faster                                                   |
| scimark_sor             | 198 ms                                                              | 127 ms: 1.56x faster                                                   |
| python_startup          | 14.1 ms                                                             | 9.14 ms: 1.55x faster                                                  |
| sqlglot_parse           | 2.07 ms                                                             | 1.34 ms: 1.54x faster                                                  |
| raytrace                | 470 ms                                                              | 306 ms: 1.53x faster                                                   |
| hexiom                  | 9.50 ms                                                             | 6.23 ms: 1.53x faster                                                  |
| chaos                   | 106 ms                                                              | 69.9 ms: 1.52x faster                                                  |
| scimark_monte_carlo     | 109 ms                                                              | 73.3 ms: 1.48x faster                                                  |
| sqlglot_transpile       | 2.45 ms                                                             | 1.67 ms: 1.47x faster                                                  |
| pyflate                 | 671 ms                                                              | 456 ms: 1.47x faster                                                   |
| crypto_pyaes            | 117 ms                                                              | 79.6 ms: 1.47x faster                                                  |
| async_tree_io           | 1.78 sec                                                            | 1.23 sec: 1.45x faster                                                 |
| pickle_pure_python      | 457 us                                                              | 316 us: 1.45x faster                                                   |
| async_tree_none         | 713 ms                                                              | 500 ms: 1.43x faster                                                   |
| async_tree_memoization  | 853 ms                                                              | 612 ms: 1.39x faster                                                   |
| scimark_lu              | 160 ms                                                              | 115 ms: 1.39x faster                                                   |
| coroutines              | 31.8 ms                                                             | 22.9 ms: 1.39x faster                                                  |
| spectral_norm           | 150 ms                                                              | 109 ms: 1.38x faster                                                   |
| unpickle_pure_python    | 300 us                                                              | 220 us: 1.37x faster                                                   |
| json_dumps              | 13.7 ms                                                             | 10.0 ms: 1.37x faster                                                  |
| mako                    | 14.7 ms                                                             | 10.9 ms: 1.35x faster                                                  |
| float                   | 110 ms                                                              | 82.0 ms: 1.34x faster                                                  |
| deepcopy_memo           | 51.8 us                                                             | 38.9 us: 1.33x faster                                                  |
| pycparser               | 1.53 sec                                                            | 1.15 sec: 1.33x faster                                                 |
| pprint_pformat          | 1.98 sec                                                            | 1.50 sec: 1.32x faster                                                 |
| unpack_sequence         | 65.6 ns                                                             | 49.9 ns: 1.32x faster                                                  |
| async_tree_cpu_io_mixed | 944 ms                                                              | 724 ms: 1.30x faster                                                   |
| pprint_safe_repr        | 953 ms                                                              | 734 ms: 1.30x faster                                                   |
| logging_simple          | 8.21 us                                                             | 6.35 us: 1.29x faster                                                  |
| tornado_http            | 129 ms                                                              | 99.9 ms: 1.29x faster                                                  |
| logging_format          | 9.07 us                                                             | 7.06 us: 1.28x faster                                                  |
| xml_etree_process       | 74.8 ms                                                             | 58.7 ms: 1.27x faster                                                  |
| fannkuch                | 485 ms                                                              | 383 ms: 1.27x faster                                                   |
| 2to3                    | 336 ms                                                              | 271 ms: 1.24x faster                                                   |
| mypy2                   | 432 ms                                                              | 352 ms: 1.23x faster                                                   |
| regex_compile           | 177 ms                                                              | 145 ms: 1.22x faster                                                   |
| scimark_fft             | 425 ms                                                              | 353 ms: 1.21x faster                                                   |
| nqueens                 | 98.8 ms                                                             | 82.8 ms: 1.19x faster                                                  |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.73 ms: 1.19x faster                                                  |
| deepcopy                | 438 us                                                              | 370 us: 1.18x faster                                                   |
| sqlglot_normalize       | 135 ms                                                              | 114 ms: 1.18x faster                                                   |
| sqlglot_optimize        | 65.3 ms                                                             | 55.5 ms: 1.18x faster                                                  |
| comprehensions          | 27.3 us                                                             | 23.2 us: 1.17x faster                                                  |
| docutils                | 3.19 sec                                                            | 2.73 sec: 1.17x faster                                                 |
| deepcopy_reduce         | 3.80 us                                                             | 3.28 us: 1.16x faster                                                  |
| bench_thread_pool       | 954 us                                                              | 836 us: 1.14x faster                                                   |
| json_loads              | 29.3 us                                                             | 25.7 us: 1.14x faster                                                  |
| sqlalchemy_declarative  | 166 ms                                                              | 146 ms: 1.14x faster                                                   |
| create_gc_cycles        | 1.64 ms                                                             | 1.46 ms: 1.13x faster                                                  |
| dulwich_log             | 76.3 ms                                                             | 67.8 ms: 1.13x faster                                                  |
| xml_etree_generate      | 94.9 ms                                                             | 84.3 ms: 1.13x faster                                                  |
| regex_v8                | 24.9 ms                                                             | 22.2 ms: 1.12x faster                                                  |
| sqlalchemy_imperative   | 21.2 ms                                                             | 19.0 ms: 1.11x faster                                                  |
| json                    | 5.41 ms                                                             | 4.91 ms: 1.10x faster                                                  |
| sqlite_synth            | 2.97 us                                                             | 2.70 us: 1.10x faster                                                  |
| xml_etree_iterparse     | 111 ms                                                              | 103 ms: 1.08x faster                                                   |
| xml_etree_parse         | 164 ms                                                              | 153 ms: 1.07x faster                                                   |
| pathlib                 | 19.8 ms                                                             | 18.5 ms: 1.07x faster                                                  |
| mdp                     | 2.75 sec                                                            | 2.61 sec: 1.06x faster                                                 |
| regex_dna               | 213 ms                                                              | 205 ms: 1.04x faster                                                   |
| pickle_list             | 4.73 us                                                             | 4.58 us: 1.03x faster                                                  |
| pidigits                | 190 ms                                                              | 189 ms: 1.00x faster                                                   |
| telco                   | 6.67 ms                                                             | 6.78 ms: 1.02x slower                                                  |
| meteor_contest          | 115 ms                                                              | 118 ms: 1.03x slower                                                   |
| pickle                  | 10.2 us                                                             | 10.5 us: 1.03x slower                                                  |
| gc_traversal            | 3.53 ms                                                             | 3.64 ms: 1.03x slower                                                  |
| unpickle_list           | 4.94 us                                                             | 5.10 us: 1.03x slower                                                  |
| regex_effbot            | 3.22 ms                                                             | 3.40 ms: 1.05x slower                                                  |
| async_generators        | 420 ms                                                              | 453 ms: 1.08x slower                                                   |
| pickle_dict             | 27.8 us                                                             | 31.8 us: 1.15x slower                                                  |
| python_startup_no_site  | 5.80 ms                                                             | 6.69 ms: 1.15x slower                                                  |
| dask                    | 437 ms                                                              | 542 ms: 1.24x slower                                                   |
| coverage                | 70.6 ms                                                             | 103 ms: 1.45x slower                                                   |
| Geometric mean          | (ref)                                                               | 1.24x faster                                                           |

Benchmark hidden because not significant (2): unpickle, bench_mp_pool
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
