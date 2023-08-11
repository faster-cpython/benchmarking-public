
# Results vs. 3.10.4

- fork: faster-cpython
- ref: gc_threshold_2000
- machine: linux-x86_64
- commit hash: b32b56c
- commit date: 2023-08-10
- overall geometric mean: 1.32x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230810-linux-x86_64-faster%2dcpython-gc_threshold_2000-3.13.0a0-b32b56c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.57 sec: 1.23x faster                                                       |
| tornado_http   | 127 ms                                                 | 92.4 ms: 1.38x faster                                                        |
| Geometric mean | (ref)                                                  | 1.30x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230810-linux-x86_64-faster%2dcpython-gc_threshold_2000-3.13.0a0-b32b56c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 89.8 ms: 1.58x faster                                                        |
| float          | 111 ms                                                 | 78.3 ms: 1.41x faster                                                        |
| pidigits       | 190 ms                                                 | 189 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.31x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230810-linux-x86_64-faster%2dcpython-gc_threshold_2000-3.13.0a0-b32b56c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 135 ms: 1.31x faster                                                         |
| regex_v8       | 25.0 ms                                                | 23.6 ms: 1.06x faster                                                        |
| regex_dna      | 222 ms                                                 | 220 ms: 1.01x faster                                                         |
| regex_effbot   | 3.23 ms                                                | 3.72 ms: 1.15x slower                                                        |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230810-linux-x86_64-faster%2dcpython-gc_threshold_2000-3.13.0a0-b32b56c |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 299 us: 1.52x faster                                                         |
| unpickle_pure_python | 300 us                                                 | 212 us: 1.42x faster                                                         |
| json_dumps           | 13.5 ms                                                | 9.79 ms: 1.38x faster                                                        |
| tomli_loads          | 2.92 sec                                               | 2.12 sec: 1.37x faster                                                       |
| xml_etree_process    | 74.9 ms                                                | 56.5 ms: 1.33x faster                                                        |
| xml_etree_generate   | 94.2 ms                                                | 81.2 ms: 1.16x faster                                                        |
| xml_etree_iterparse  | 111 ms                                                 | 98.8 ms: 1.13x faster                                                        |
| json_loads           | 28.8 us                                                | 25.6 us: 1.13x faster                                                        |
| xml_etree_parse      | 163 ms                                                 | 150 ms: 1.09x faster                                                         |
| unpickle_list        | 4.82 us                                                | 4.85 us: 1.01x slower                                                        |
| pickle               | 10.3 us                                                | 10.5 us: 1.02x slower                                                        |
| pickle_list          | 4.56 us                                                | 4.66 us: 1.02x slower                                                        |
| unpickle             | 14.1 us                                                | 14.9 us: 1.05x slower                                                        |
| pickle_dict          | 27.3 us                                                | 31.9 us: 1.17x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.15x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230810-linux-x86_64-faster%2dcpython-gc_threshold_2000-3.13.0a0-b32b56c |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.27 ms: 1.53x faster                                                        |
| python_startup_no_site | 5.82 ms                                                | 6.76 ms: 1.16x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.15x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230810-linux-x86_64-faster%2dcpython-gc_threshold_2000-3.13.0a0-b32b56c |
|-----------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.5 ms: 1.41x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230810-linux-x86_64-faster%2dcpython-gc_threshold_2000-3.13.0a0-b32b56c |
|--------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 147 us: 3.46x faster                                                         |
| generators               | 76.8 ms                                                | 28.3 ms: 2.71x faster                                                        |
| deltablue                | 7.42 ms                                                | 3.33 ms: 2.23x faster                                                        |
| async_tree_io            | 1.77 sec                                               | 853 ms: 2.08x faster                                                         |
| async_tree_none          | 717 ms                                                 | 355 ms: 2.02x faster                                                         |
| async_tree_memoization   | 854 ms                                                 | 447 ms: 1.91x faster                                                         |
| asyncio_tcp              | 925 ms                                                 | 484 ms: 1.91x faster                                                         |
| chaos                    | 106 ms                                                 | 59.8 ms: 1.78x faster                                                        |
| crypto_pyaes             | 118 ms                                                 | 68.5 ms: 1.73x faster                                                        |
| raytrace                 | 464 ms                                                 | 273 ms: 1.70x faster                                                         |
| richards_super           | 90.7 ms                                                | 53.5 ms: 1.70x faster                                                        |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.79 sec: 1.68x faster                                                       |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 570 ms: 1.67x faster                                                         |
| logging_silent           | 175 ns                                                 | 106 ns: 1.65x faster                                                         |
| go                       | 229 ms                                                 | 140 ms: 1.64x faster                                                         |
| sqlglot_parse            | 2.06 ms                                                | 1.26 ms: 1.64x faster                                                        |
| scimark_sor              | 197 ms                                                 | 121 ms: 1.62x faster                                                         |
| scimark_monte_carlo      | 108 ms                                                 | 67.2 ms: 1.61x faster                                                        |
| hexiom                   | 9.53 ms                                                | 6.00 ms: 1.59x faster                                                        |
| nbody                    | 142 ms                                                 | 89.8 ms: 1.58x faster                                                        |
| richards                 | 74.9 ms                                                | 47.7 ms: 1.57x faster                                                        |
| sqlglot_transpile        | 2.45 ms                                                | 1.57 ms: 1.56x faster                                                        |
| python_startup           | 14.2 ms                                                | 9.27 ms: 1.53x faster                                                        |
| pickle_pure_python       | 455 us                                                 | 299 us: 1.52x faster                                                         |
| pyflate                  | 673 ms                                                 | 445 ms: 1.51x faster                                                         |
| scimark_lu               | 163 ms                                                 | 110 ms: 1.49x faster                                                         |
| spectral_norm            | 150 ms                                                 | 105 ms: 1.44x faster                                                         |
| coroutines               | 31.8 ms                                                | 22.2 ms: 1.43x faster                                                        |
| unpickle_pure_python     | 300 us                                                 | 212 us: 1.42x faster                                                         |
| float                    | 111 ms                                                 | 78.3 ms: 1.41x faster                                                        |
| mako                     | 14.8 ms                                                | 10.5 ms: 1.41x faster                                                        |
| deepcopy_memo            | 52.3 us                                                | 37.8 us: 1.38x faster                                                        |
| json_dumps               | 13.5 ms                                                | 9.79 ms: 1.38x faster                                                        |
| tornado_http             | 127 ms                                                 | 92.4 ms: 1.38x faster                                                        |
| tomli_loads              | 2.92 sec                                               | 2.12 sec: 1.37x faster                                                       |
| logging_simple           | 8.07 us                                                | 5.89 us: 1.37x faster                                                        |
| logging_format           | 8.91 us                                                | 6.53 us: 1.36x faster                                                        |
| unpack_sequence          | 64.7 ns                                                | 48.0 ns: 1.35x faster                                                        |
| pprint_pformat           | 1.99 sec                                               | 1.48 sec: 1.34x faster                                                       |
| xml_etree_process        | 74.9 ms                                                | 56.5 ms: 1.33x faster                                                        |
| pprint_safe_repr         | 955 ms                                                 | 730 ms: 1.31x faster                                                         |
| regex_compile            | 177 ms                                                 | 135 ms: 1.31x faster                                                         |
| comprehensions           | 26.8 us                                                | 20.5 us: 1.31x faster                                                        |
| sqlglot_normalize        | 135 ms                                                 | 104 ms: 1.29x faster                                                         |
| pycparser                | 1.50 sec                                               | 1.17 sec: 1.29x faster                                                       |
| nqueens                  | 100 ms                                                 | 78.5 ms: 1.27x faster                                                        |
| mypy2                    | 428 ms                                                 | 337 ms: 1.27x faster                                                         |
| deepcopy                 | 442 us                                                 | 352 us: 1.26x faster                                                         |
| fannkuch                 | 486 ms                                                 | 388 ms: 1.25x faster                                                         |
| sqlglot_optimize         | 65.3 ms                                                | 52.8 ms: 1.24x faster                                                        |
| docutils                 | 3.17 sec                                               | 2.57 sec: 1.23x faster                                                       |
| deepcopy_reduce          | 3.82 us                                                | 3.18 us: 1.20x faster                                                        |
| scimark_fft              | 424 ms                                                 | 353 ms: 1.20x faster                                                         |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.63 ms: 1.18x faster                                                        |
| xml_etree_generate       | 94.2 ms                                                | 81.2 ms: 1.16x faster                                                        |
| bench_thread_pool        | 947 us                                                 | 819 us: 1.16x faster                                                         |
| dulwich_log              | 75.9 ms                                                | 66.6 ms: 1.14x faster                                                        |
| xml_etree_iterparse      | 111 ms                                                 | 98.8 ms: 1.13x faster                                                        |
| json_loads               | 28.8 us                                                | 25.6 us: 1.13x faster                                                        |
| json                     | 5.42 ms                                                | 4.85 ms: 1.12x faster                                                        |
| create_gc_cycles         | 1.67 ms                                                | 1.52 ms: 1.10x faster                                                        |
| meteor_contest           | 115 ms                                                 | 105 ms: 1.09x faster                                                         |
| xml_etree_parse          | 163 ms                                                 | 150 ms: 1.09x faster                                                         |
| pathlib                  | 20.0 ms                                                | 18.8 ms: 1.07x faster                                                        |
| regex_v8                 | 25.0 ms                                                | 23.6 ms: 1.06x faster                                                        |
| sqlite_synth             | 2.93 us                                                | 2.78 us: 1.06x faster                                                        |
| mdp                      | 2.82 sec                                               | 2.68 sec: 1.05x faster                                                       |
| gc_traversal             | 3.84 ms                                                | 3.80 ms: 1.01x faster                                                        |
| regex_dna                | 222 ms                                                 | 220 ms: 1.01x faster                                                         |
| pidigits                 | 190 ms                                                 | 189 ms: 1.01x faster                                                         |
| unpickle_list            | 4.82 us                                                | 4.85 us: 1.01x slower                                                        |
| pickle                   | 10.3 us                                                | 10.5 us: 1.02x slower                                                        |
| pickle_list              | 4.56 us                                                | 4.66 us: 1.02x slower                                                        |
| async_generators         | 425 ms                                                 | 441 ms: 1.04x slower                                                         |
| unpickle                 | 14.1 us                                                | 14.9 us: 1.05x slower                                                        |
| regex_effbot             | 3.23 ms                                                | 3.72 ms: 1.15x slower                                                        |
| python_startup_no_site   | 5.82 ms                                                | 6.76 ms: 1.16x slower                                                        |
| pickle_dict              | 27.3 us                                                | 31.9 us: 1.17x slower                                                        |
| coverage                 | 72.8 ms                                                | 85.3 ms: 1.17x slower                                                        |
| dask                     | 423 ms                                                 | 498 ms: 1.18x slower                                                         |
| telco                    | 6.54 ms                                                | 7.93 ms: 1.21x slower                                                        |
| Geometric mean           | (ref)                                                  | 1.32x faster                                                                 |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
