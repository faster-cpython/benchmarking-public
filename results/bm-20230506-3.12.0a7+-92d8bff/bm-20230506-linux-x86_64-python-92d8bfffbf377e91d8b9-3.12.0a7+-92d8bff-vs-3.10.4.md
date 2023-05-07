
# Results vs. 3.10.4

- fork: python
- ref: 92d8bfffbf377e91d8b9
- machine: linux-x86_64
- commit hash: 92d8bff
- commit date: 2023-05-06
- overall geometric mean: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230506-linux-x86_64-python-92d8bfffbf377e91d8b9-3.12.0a7+-92d8bff |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 336 ms                                                              | 270 ms: 1.25x faster                                                   |
| docutils       | 3.19 sec                                                            | 2.73 sec: 1.17x faster                                                 |
| tornado_http   | 129 ms                                                              | 103 ms: 1.26x faster                                                   |
| Geometric mean | (ref)                                                               | 1.22x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230506-linux-x86_64-python-92d8bfffbf377e91d8b9-3.12.0a7+-92d8bff |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 146 ms                                                              | 90.6 ms: 1.61x faster                                                  |
| float          | 110 ms                                                              | 81.2 ms: 1.35x faster                                                  |
| pidigits       | 190 ms                                                              | 189 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                               | 1.30x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230506-linux-x86_64-python-92d8bfffbf377e91d8b9-3.12.0a7+-92d8bff |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                              | 146 ms: 1.22x faster                                                   |
| regex_v8       | 24.9 ms                                                             | 22.0 ms: 1.14x faster                                                  |
| regex_dna      | 213 ms                                                              | 207 ms: 1.03x faster                                                   |
| regex_effbot   | 3.22 ms                                                             | 3.60 ms: 1.12x slower                                                  |
| Geometric mean | (ref)                                                               | 1.06x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230506-linux-x86_64-python-92d8bfffbf377e91d8b9-3.12.0a7+-92d8bff |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 457 us                                                              | 316 us: 1.44x faster                                                   |
| json_dumps           | 13.7 ms                                                             | 9.87 ms: 1.39x faster                                                  |
| unpickle_pure_python | 300 us                                                              | 220 us: 1.36x faster                                                   |
| xml_etree_process    | 74.8 ms                                                             | 59.3 ms: 1.26x faster                                                  |
| json_loads           | 29.3 us                                                             | 25.3 us: 1.16x faster                                                  |
| xml_etree_generate   | 94.9 ms                                                             | 84.9 ms: 1.12x faster                                                  |
| xml_etree_iterparse  | 111 ms                                                              | 104 ms: 1.07x faster                                                   |
| xml_etree_parse      | 164 ms                                                              | 156 ms: 1.05x faster                                                   |
| pickle_list          | 4.73 us                                                             | 4.54 us: 1.04x faster                                                  |
| unpickle_list        | 4.94 us                                                             | 4.99 us: 1.01x slower                                                  |
| pickle               | 10.2 us                                                             | 10.5 us: 1.03x slower                                                  |
| pickle_dict          | 27.8 us                                                             | 31.6 us: 1.14x slower                                                  |
| Geometric mean       | (ref)                                                               | 1.12x faster                                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230506-linux-x86_64-python-92d8bfffbf377e91d8b9-3.12.0a7+-92d8bff |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 14.1 ms                                                             | 9.15 ms: 1.55x faster                                                  |
| python_startup_no_site | 5.80 ms                                                             | 6.69 ms: 1.15x slower                                                  |
| Geometric mean         | (ref)                                                               | 1.16x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230506-linux-x86_64-python-92d8bfffbf377e91d8b9-3.12.0a7+-92d8bff |
|-----------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako      | 14.7 ms                                                             | 10.7 ms: 1.37x faster                                                  |

All benchmarks:
===============

| Benchmark               | bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20230506-linux-x86_64-python-92d8bfffbf377e91d8b9-3.12.0a7+-92d8bff |
|-------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 75.7 ms                                                             | 30.9 ms: 2.45x faster                                                  |
| deltablue               | 7.30 ms                                                             | 3.57 ms: 2.04x faster                                                  |
| asyncio_tcp             | 922 ms                                                              | 507 ms: 1.82x faster                                                   |
| richards                | 74.2 ms                                                             | 44.8 ms: 1.66x faster                                                  |
| go                      | 226 ms                                                              | 136 ms: 1.66x faster                                                   |
| logging_silent          | 169 ns                                                              | 102 ns: 1.65x faster                                                   |
| scimark_sor             | 198 ms                                                              | 123 ms: 1.61x faster                                                   |
| nbody                   | 146 ms                                                              | 90.6 ms: 1.61x faster                                                  |
| hexiom                  | 9.50 ms                                                             | 6.11 ms: 1.55x faster                                                  |
| chaos                   | 106 ms                                                              | 68.2 ms: 1.55x faster                                                  |
| sqlglot_parse           | 2.07 ms                                                             | 1.33 ms: 1.55x faster                                                  |
| python_startup          | 14.1 ms                                                             | 9.15 ms: 1.55x faster                                                  |
| raytrace                | 470 ms                                                              | 310 ms: 1.52x faster                                                   |
| pyflate                 | 671 ms                                                              | 442 ms: 1.52x faster                                                   |
| crypto_pyaes            | 117 ms                                                              | 77.8 ms: 1.50x faster                                                  |
| scimark_monte_carlo     | 109 ms                                                              | 72.9 ms: 1.49x faster                                                  |
| sqlglot_transpile       | 2.45 ms                                                             | 1.66 ms: 1.48x faster                                                  |
| async_tree_io           | 1.78 sec                                                            | 1.23 sec: 1.45x faster                                                 |
| pickle_pure_python      | 457 us                                                              | 316 us: 1.44x faster                                                   |
| scimark_lu              | 160 ms                                                              | 113 ms: 1.41x faster                                                   |
| async_tree_none         | 713 ms                                                              | 505 ms: 1.41x faster                                                   |
| spectral_norm           | 150 ms                                                              | 107 ms: 1.41x faster                                                   |
| coroutines              | 31.8 ms                                                             | 22.7 ms: 1.40x faster                                                  |
| async_tree_memoization  | 853 ms                                                              | 613 ms: 1.39x faster                                                   |
| json_dumps              | 13.7 ms                                                             | 9.87 ms: 1.39x faster                                                  |
| mako                    | 14.7 ms                                                             | 10.7 ms: 1.37x faster                                                  |
| deepcopy_memo           | 51.8 us                                                             | 37.7 us: 1.37x faster                                                  |
| unpickle_pure_python    | 300 us                                                              | 220 us: 1.36x faster                                                   |
| float                   | 110 ms                                                              | 81.2 ms: 1.35x faster                                                  |
| pycparser               | 1.53 sec                                                            | 1.16 sec: 1.32x faster                                                 |
| pprint_pformat          | 1.98 sec                                                            | 1.50 sec: 1.32x faster                                                 |
| pprint_safe_repr        | 953 ms                                                              | 734 ms: 1.30x faster                                                   |
| async_tree_cpu_io_mixed | 944 ms                                                              | 727 ms: 1.30x faster                                                   |
| logging_simple          | 8.21 us                                                             | 6.35 us: 1.29x faster                                                  |
| logging_format          | 9.07 us                                                             | 7.05 us: 1.29x faster                                                  |
| fannkuch                | 485 ms                                                              | 377 ms: 1.29x faster                                                   |
| xml_etree_process       | 74.8 ms                                                             | 59.3 ms: 1.26x faster                                                  |
| tornado_http            | 129 ms                                                              | 103 ms: 1.26x faster                                                   |
| 2to3                    | 336 ms                                                              | 270 ms: 1.25x faster                                                   |
| nqueens                 | 98.8 ms                                                             | 79.5 ms: 1.24x faster                                                  |
| mypy2                   | 432 ms                                                              | 353 ms: 1.22x faster                                                   |
| regex_compile           | 177 ms                                                              | 146 ms: 1.22x faster                                                   |
| deepcopy                | 438 us                                                              | 362 us: 1.21x faster                                                   |
| sqlglot_normalize       | 135 ms                                                              | 112 ms: 1.20x faster                                                   |
| scimark_fft             | 425 ms                                                              | 358 ms: 1.19x faster                                                   |
| sqlglot_optimize        | 65.3 ms                                                             | 55.1 ms: 1.19x faster                                                  |
| deepcopy_reduce         | 3.80 us                                                             | 3.21 us: 1.19x faster                                                  |
| scimark_sparse_mat_mult | 5.62 ms                                                             | 4.75 ms: 1.18x faster                                                  |
| comprehensions          | 27.3 us                                                             | 23.2 us: 1.17x faster                                                  |
| docutils                | 3.19 sec                                                            | 2.73 sec: 1.17x faster                                                 |
| json_loads              | 29.3 us                                                             | 25.3 us: 1.16x faster                                                  |
| bench_thread_pool       | 954 us                                                              | 831 us: 1.15x faster                                                   |
| sqlalchemy_declarative  | 166 ms                                                              | 146 ms: 1.14x faster                                                   |
| regex_v8                | 24.9 ms                                                             | 22.0 ms: 1.14x faster                                                  |
| json                    | 5.41 ms                                                             | 4.77 ms: 1.13x faster                                                  |
| dulwich_log             | 76.3 ms                                                             | 68.1 ms: 1.12x faster                                                  |
| unpack_sequence         | 65.6 ns                                                             | 58.6 ns: 1.12x faster                                                  |
| xml_etree_generate      | 94.9 ms                                                             | 84.9 ms: 1.12x faster                                                  |
| create_gc_cycles        | 1.64 ms                                                             | 1.49 ms: 1.10x faster                                                  |
| sqlalchemy_imperative   | 21.2 ms                                                             | 19.4 ms: 1.09x faster                                                  |
| meteor_contest          | 115 ms                                                              | 105 ms: 1.09x faster                                                   |
| sqlite_synth            | 2.97 us                                                             | 2.74 us: 1.09x faster                                                  |
| xml_etree_iterparse     | 111 ms                                                              | 104 ms: 1.07x faster                                                   |
| xml_etree_parse         | 164 ms                                                              | 156 ms: 1.05x faster                                                   |
| pathlib                 | 19.8 ms                                                             | 18.8 ms: 1.05x faster                                                  |
| pickle_list             | 4.73 us                                                             | 4.54 us: 1.04x faster                                                  |
| regex_dna               | 213 ms                                                              | 207 ms: 1.03x faster                                                   |
| mdp                     | 2.75 sec                                                            | 2.68 sec: 1.03x faster                                                 |
| pidigits                | 190 ms                                                              | 189 ms: 1.01x faster                                                   |
| bench_mp_pool           | 24.0 ms                                                             | 24.0 ms: 1.00x slower                                                  |
| unpickle_list           | 4.94 us                                                             | 4.99 us: 1.01x slower                                                  |
| telco                   | 6.67 ms                                                             | 6.77 ms: 1.01x slower                                                  |
| pickle                  | 10.2 us                                                             | 10.5 us: 1.03x slower                                                  |
| async_generators        | 420 ms                                                              | 448 ms: 1.07x slower                                                   |
| regex_effbot            | 3.22 ms                                                             | 3.60 ms: 1.12x slower                                                  |
| pickle_dict             | 27.8 us                                                             | 31.6 us: 1.14x slower                                                  |
| python_startup_no_site  | 5.80 ms                                                             | 6.69 ms: 1.15x slower                                                  |
| dask                    | 437 ms                                                              | 539 ms: 1.23x slower                                                   |
| gc_traversal            | 3.53 ms                                                             | 4.37 ms: 1.24x slower                                                  |
| coverage                | 70.6 ms                                                             | 102 ms: 1.45x slower                                                   |
| Geometric mean          | (ref)                                                               | 1.24x faster                                                           |

Benchmark hidden because not significant (1): unpickle
Ignored benchmarks (15) of /home/runner/work/benchmarking/benchmarking/results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
