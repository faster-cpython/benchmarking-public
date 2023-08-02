
# Results vs. 3.10.4

- fork: faster-cpython
- ref: gc_stats
- machine: linux-x86_64
- commit hash: 8bc0926
- commit date: 2023-07-30
- overall geometric mean: 1.29x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230730-linux-x86_64-faster%2dcpython-gc_stats-3.13.0a0-8bc0926 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.66 sec: 1.19x faster                                              |
| tornado_http   | 127 ms                                                 | 95.3 ms: 1.34x faster                                               |
| Geometric mean | (ref)                                                  | 1.26x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230730-linux-x86_64-faster%2dcpython-gc_stats-3.13.0a0-8bc0926 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 96.2 ms: 1.47x faster                                               |
| float          | 111 ms                                                 | 79.2 ms: 1.40x faster                                               |
| pidigits       | 190 ms                                                 | 201 ms: 1.06x slower                                                |
| Geometric mean | (ref)                                                  | 1.25x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230730-linux-x86_64-faster%2dcpython-gc_stats-3.13.0a0-8bc0926 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 137 ms: 1.29x faster                                                |
| regex_v8       | 25.0 ms                                                | 22.3 ms: 1.12x faster                                               |
| regex_dna      | 222 ms                                                 | 215 ms: 1.03x faster                                                |
| regex_effbot   | 3.23 ms                                                | 3.56 ms: 1.10x slower                                               |
| Geometric mean | (ref)                                                  | 1.08x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230730-linux-x86_64-faster%2dcpython-gc_stats-3.13.0a0-8bc0926 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 297 us: 1.53x faster                                                |
| unpickle_pure_python | 300 us                                                 | 214 us: 1.41x faster                                                |
| json_dumps           | 13.5 ms                                                | 9.74 ms: 1.39x faster                                               |
| xml_etree_process    | 74.9 ms                                                | 57.7 ms: 1.30x faster                                               |
| tomli_loads          | 2.92 sec                                               | 2.30 sec: 1.27x faster                                              |
| xml_etree_generate   | 94.2 ms                                                | 83.8 ms: 1.12x faster                                               |
| json_loads           | 28.8 us                                                | 25.9 us: 1.11x faster                                               |
| xml_etree_iterparse  | 111 ms                                                 | 103 ms: 1.08x faster                                                |
| xml_etree_parse      | 163 ms                                                 | 153 ms: 1.07x faster                                                |
| pickle_list          | 4.56 us                                                | 4.58 us: 1.01x slower                                               |
| pickle               | 10.3 us                                                | 10.5 us: 1.02x slower                                               |
| unpickle             | 14.1 us                                                | 15.1 us: 1.07x slower                                               |
| unpickle_list        | 4.82 us                                                | 5.16 us: 1.07x slower                                               |
| pickle_dict          | 27.3 us                                                | 31.3 us: 1.15x slower                                               |
| Geometric mean       | (ref)                                                  | 1.13x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230730-linux-x86_64-faster%2dcpython-gc_stats-3.13.0a0-8bc0926 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.35 ms: 1.51x faster                                               |
| python_startup_no_site | 5.82 ms                                                | 6.83 ms: 1.17x slower                                               |
| Geometric mean         | (ref)                                                  | 1.14x faster                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230730-linux-x86_64-faster%2dcpython-gc_stats-3.13.0a0-8bc0926 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.9 ms: 1.35x faster                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230730-linux-x86_64-faster%2dcpython-gc_stats-3.13.0a0-8bc0926 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 146 us: 3.49x faster                                                |
| generators               | 76.8 ms                                                | 28.2 ms: 2.72x faster                                               |
| deltablue                | 7.42 ms                                                | 3.31 ms: 2.24x faster                                               |
| asyncio_tcp              | 925 ms                                                 | 489 ms: 1.89x faster                                                |
| chaos                    | 106 ms                                                 | 59.9 ms: 1.78x faster                                               |
| richards_super           | 90.7 ms                                                | 52.8 ms: 1.72x faster                                               |
| raytrace                 | 464 ms                                                 | 273 ms: 1.70x faster                                                |
| crypto_pyaes             | 118 ms                                                 | 70.1 ms: 1.69x faster                                               |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.78 sec: 1.68x faster                                              |
| go                       | 229 ms                                                 | 137 ms: 1.67x faster                                                |
| scimark_sor              | 197 ms                                                 | 119 ms: 1.65x faster                                                |
| logging_silent           | 175 ns                                                 | 106 ns: 1.65x faster                                                |
| richards                 | 74.9 ms                                                | 46.2 ms: 1.62x faster                                               |
| scimark_monte_carlo      | 108 ms                                                 | 67.6 ms: 1.60x faster                                               |
| sqlglot_parse            | 2.06 ms                                                | 1.30 ms: 1.58x faster                                               |
| hexiom                   | 9.53 ms                                                | 6.08 ms: 1.57x faster                                               |
| pickle_pure_python       | 455 us                                                 | 297 us: 1.53x faster                                                |
| sqlglot_transpile        | 2.45 ms                                                | 1.61 ms: 1.52x faster                                               |
| python_startup           | 14.2 ms                                                | 9.35 ms: 1.51x faster                                               |
| pyflate                  | 673 ms                                                 | 448 ms: 1.50x faster                                                |
| async_tree_io            | 1.77 sec                                               | 1.19 sec: 1.49x faster                                              |
| scimark_lu               | 163 ms                                                 | 110 ms: 1.49x faster                                                |
| async_tree_none          | 717 ms                                                 | 483 ms: 1.49x faster                                                |
| nbody                    | 142 ms                                                 | 96.2 ms: 1.47x faster                                               |
| async_tree_memoization   | 854 ms                                                 | 586 ms: 1.46x faster                                                |
| coroutines               | 31.8 ms                                                | 21.9 ms: 1.45x faster                                               |
| unpack_sequence          | 64.7 ns                                                | 45.7 ns: 1.41x faster                                               |
| unpickle_pure_python     | 300 us                                                 | 214 us: 1.41x faster                                                |
| spectral_norm            | 150 ms                                                 | 107 ms: 1.40x faster                                                |
| float                    | 111 ms                                                 | 79.2 ms: 1.40x faster                                               |
| json_dumps               | 13.5 ms                                                | 9.74 ms: 1.39x faster                                               |
| deepcopy_memo            | 52.3 us                                                | 38.0 us: 1.38x faster                                               |
| logging_format           | 8.91 us                                                | 6.54 us: 1.36x faster                                               |
| logging_simple           | 8.07 us                                                | 5.97 us: 1.35x faster                                               |
| pprint_pformat           | 1.99 sec                                               | 1.47 sec: 1.35x faster                                              |
| mako                     | 14.8 ms                                                | 10.9 ms: 1.35x faster                                               |
| tornado_http             | 127 ms                                                 | 95.3 ms: 1.34x faster                                               |
| pprint_safe_repr         | 955 ms                                                 | 717 ms: 1.33x faster                                                |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 722 ms: 1.32x faster                                                |
| comprehensions           | 26.8 us                                                | 20.4 us: 1.32x faster                                               |
| pycparser                | 1.50 sec                                               | 1.15 sec: 1.31x faster                                              |
| xml_etree_process        | 74.9 ms                                                | 57.7 ms: 1.30x faster                                               |
| regex_compile            | 177 ms                                                 | 137 ms: 1.29x faster                                                |
| sqlglot_normalize        | 135 ms                                                 | 106 ms: 1.28x faster                                                |
| mypy2                    | 428 ms                                                 | 338 ms: 1.27x faster                                                |
| tomli_loads              | 2.92 sec                                               | 2.30 sec: 1.27x faster                                              |
| deepcopy                 | 442 us                                                 | 357 us: 1.24x faster                                                |
| fannkuch                 | 486 ms                                                 | 395 ms: 1.23x faster                                                |
| sqlglot_optimize         | 65.3 ms                                                | 53.3 ms: 1.23x faster                                               |
| nqueens                  | 100 ms                                                 | 82.8 ms: 1.21x faster                                               |
| deepcopy_reduce          | 3.82 us                                                | 3.18 us: 1.20x faster                                               |
| scimark_fft              | 424 ms                                                 | 354 ms: 1.20x faster                                                |
| docutils                 | 3.17 sec                                               | 2.66 sec: 1.19x faster                                              |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.70 ms: 1.16x faster                                               |
| bench_thread_pool        | 947 us                                                 | 817 us: 1.16x faster                                                |
| dulwich_log              | 75.9 ms                                                | 66.3 ms: 1.15x faster                                               |
| xml_etree_generate       | 94.2 ms                                                | 83.8 ms: 1.12x faster                                               |
| regex_v8                 | 25.0 ms                                                | 22.3 ms: 1.12x faster                                               |
| create_gc_cycles         | 1.67 ms                                                | 1.49 ms: 1.12x faster                                               |
| json_loads               | 28.8 us                                                | 25.9 us: 1.11x faster                                               |
| json                     | 5.42 ms                                                | 4.89 ms: 1.11x faster                                               |
| mdp                      | 2.82 sec                                               | 2.59 sec: 1.09x faster                                              |
| xml_etree_iterparse      | 111 ms                                                 | 103 ms: 1.08x faster                                                |
| meteor_contest           | 115 ms                                                 | 106 ms: 1.08x faster                                                |
| pathlib                  | 20.0 ms                                                | 18.8 ms: 1.07x faster                                               |
| sqlite_synth             | 2.93 us                                                | 2.75 us: 1.07x faster                                               |
| xml_etree_parse          | 163 ms                                                 | 153 ms: 1.07x faster                                                |
| regex_dna                | 222 ms                                                 | 215 ms: 1.03x faster                                                |
| pickle_list              | 4.56 us                                                | 4.58 us: 1.01x slower                                               |
| pickle                   | 10.3 us                                                | 10.5 us: 1.02x slower                                               |
| async_generators         | 425 ms                                                 | 446 ms: 1.05x slower                                                |
| pidigits                 | 190 ms                                                 | 201 ms: 1.06x slower                                                |
| unpickle                 | 14.1 us                                                | 15.1 us: 1.07x slower                                               |
| unpickle_list            | 4.82 us                                                | 5.16 us: 1.07x slower                                               |
| gc_traversal             | 3.84 ms                                                | 4.19 ms: 1.09x slower                                               |
| regex_effbot             | 3.23 ms                                                | 3.56 ms: 1.10x slower                                               |
| pickle_dict              | 27.3 us                                                | 31.3 us: 1.15x slower                                               |
| python_startup_no_site   | 5.82 ms                                                | 6.83 ms: 1.17x slower                                               |
| telco                    | 6.54 ms                                                | 7.79 ms: 1.19x slower                                               |
| dask                     | 423 ms                                                 | 520 ms: 1.23x slower                                                |
| coverage                 | 72.8 ms                                                | 93.2 ms: 1.28x slower                                               |
| Geometric mean           | (ref)                                                  | 1.29x faster                                                        |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift
