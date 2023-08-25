
# Results vs. 3.10.4

- fork: faster-cpython
- ref: incremental_gc
- machine: linux-x86_64
- commit hash: 13cce66
- commit date: 2023-08-12
- overall geometric mean: 1.34x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-13cce66 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| docutils       | 3.17 sec                                               | 2.40 sec: 1.32x faster                                                    |
| tornado_http   | 127 ms                                                 | 94.4 ms: 1.35x faster                                                     |
| Geometric mean | (ref)                                                  | 1.34x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-13cce66 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 142 ms                                                 | 89.9 ms: 1.58x faster                                                     |
| float          | 111 ms                                                 | 72.7 ms: 1.52x faster                                                     |
| pidigits       | 190 ms                                                 | 189 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                  | 1.34x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-13cce66 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                 | 137 ms: 1.29x faster                                                      |
| regex_v8       | 25.0 ms                                                | 22.5 ms: 1.12x faster                                                     |
| regex_dna      | 222 ms                                                 | 209 ms: 1.06x faster                                                      |
| regex_effbot   | 3.23 ms                                                | 3.72 ms: 1.15x slower                                                     |
| Geometric mean | (ref)                                                  | 1.07x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-13cce66 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                 | 298 us: 1.53x faster                                                      |
| unpickle_pure_python | 300 us                                                 | 214 us: 1.41x faster                                                      |
| json_dumps           | 13.5 ms                                                | 9.84 ms: 1.38x faster                                                     |
| xml_etree_process    | 74.9 ms                                                | 56.7 ms: 1.32x faster                                                     |
| tomli_loads          | 2.92 sec                                               | 2.34 sec: 1.25x faster                                                    |
| xml_etree_iterparse  | 111 ms                                                 | 94.5 ms: 1.18x faster                                                     |
| xml_etree_parse      | 163 ms                                                 | 140 ms: 1.16x faster                                                      |
| xml_etree_generate   | 94.2 ms                                                | 81.8 ms: 1.15x faster                                                     |
| json_loads           | 28.8 us                                                | 26.1 us: 1.11x faster                                                     |
| pickle_list          | 4.56 us                                                | 4.58 us: 1.00x slower                                                     |
| pickle               | 10.3 us                                                | 10.5 us: 1.02x slower                                                     |
| unpickle_list        | 4.82 us                                                | 4.94 us: 1.03x slower                                                     |
| unpickle             | 14.1 us                                                | 15.4 us: 1.09x slower                                                     |
| pickle_dict          | 27.3 us                                                | 31.8 us: 1.17x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.14x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-13cce66 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 14.2 ms                                                | 9.36 ms: 1.51x faster                                                     |
| python_startup_no_site | 5.82 ms                                                | 6.84 ms: 1.18x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.13x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-13cce66 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 14.8 ms                                                | 10.9 ms: 1.35x faster                                                     |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-13cce66 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 510 us                                                 | 146 us: 3.48x faster                                                      |
| async_tree_io            | 1.77 sec                                               | 563 ms: 3.15x faster                                                      |
| generators               | 76.8 ms                                                | 28.5 ms: 2.70x faster                                                     |
| async_tree_none          | 717 ms                                                 | 276 ms: 2.60x faster                                                      |
| async_tree_memoization   | 854 ms                                                 | 342 ms: 2.50x faster                                                      |
| deltablue                | 7.42 ms                                                | 3.14 ms: 2.36x faster                                                     |
| asyncio_tcp              | 925 ms                                                 | 482 ms: 1.92x faster                                                      |
| async_tree_cpu_io_mixed  | 951 ms                                                 | 500 ms: 1.90x faster                                                      |
| chaos                    | 106 ms                                                 | 59.3 ms: 1.79x faster                                                     |
| crypto_pyaes             | 118 ms                                                 | 68.4 ms: 1.73x faster                                                     |
| raytrace                 | 464 ms                                                 | 269 ms: 1.73x faster                                                      |
| richards_super           | 90.7 ms                                                | 52.7 ms: 1.72x faster                                                     |
| asyncio_tcp_ssl          | 3.01 sec                                               | 1.78 sec: 1.69x faster                                                    |
| go                       | 229 ms                                                 | 137 ms: 1.67x faster                                                      |
| logging_silent           | 175 ns                                                 | 105 ns: 1.67x faster                                                      |
| scimark_sor              | 197 ms                                                 | 121 ms: 1.63x faster                                                      |
| richards                 | 74.9 ms                                                | 46.2 ms: 1.62x faster                                                     |
| scimark_monte_carlo      | 108 ms                                                 | 67.2 ms: 1.61x faster                                                     |
| sqlglot_parse            | 2.06 ms                                                | 1.28 ms: 1.61x faster                                                     |
| nbody                    | 142 ms                                                 | 89.9 ms: 1.58x faster                                                     |
| hexiom                   | 9.53 ms                                                | 6.09 ms: 1.56x faster                                                     |
| sqlglot_transpile        | 2.45 ms                                                | 1.59 ms: 1.53x faster                                                     |
| pickle_pure_python       | 455 us                                                 | 298 us: 1.53x faster                                                      |
| float                    | 111 ms                                                 | 72.7 ms: 1.52x faster                                                     |
| pyflate                  | 673 ms                                                 | 444 ms: 1.52x faster                                                      |
| python_startup           | 14.2 ms                                                | 9.36 ms: 1.51x faster                                                     |
| unpack_sequence          | 64.7 ns                                                | 44.0 ns: 1.47x faster                                                     |
| scimark_lu               | 163 ms                                                 | 113 ms: 1.45x faster                                                      |
| coroutines               | 31.8 ms                                                | 22.0 ms: 1.44x faster                                                     |
| spectral_norm            | 150 ms                                                 | 107 ms: 1.41x faster                                                      |
| unpickle_pure_python     | 300 us                                                 | 214 us: 1.41x faster                                                      |
| pycparser                | 1.50 sec                                               | 1.08 sec: 1.39x faster                                                    |
| deepcopy_memo            | 52.3 us                                                | 37.9 us: 1.38x faster                                                     |
| json_dumps               | 13.5 ms                                                | 9.84 ms: 1.38x faster                                                     |
| logging_simple           | 8.07 us                                                | 5.89 us: 1.37x faster                                                     |
| logging_format           | 8.91 us                                                | 6.52 us: 1.37x faster                                                     |
| mako                     | 14.8 ms                                                | 10.9 ms: 1.35x faster                                                     |
| tornado_http             | 127 ms                                                 | 94.4 ms: 1.35x faster                                                     |
| pprint_pformat           | 1.99 sec                                               | 1.48 sec: 1.34x faster                                                    |
| docutils                 | 3.17 sec                                               | 2.40 sec: 1.32x faster                                                    |
| xml_etree_process        | 74.9 ms                                                | 56.7 ms: 1.32x faster                                                     |
| pprint_safe_repr         | 955 ms                                                 | 723 ms: 1.32x faster                                                      |
| comprehensions           | 26.8 us                                                | 20.5 us: 1.31x faster                                                     |
| regex_compile            | 177 ms                                                 | 137 ms: 1.29x faster                                                      |
| sqlglot_normalize        | 135 ms                                                 | 106 ms: 1.27x faster                                                      |
| deepcopy                 | 442 us                                                 | 351 us: 1.26x faster                                                      |
| mypy2                    | 428 ms                                                 | 340 ms: 1.26x faster                                                      |
| tomli_loads              | 2.92 sec                                               | 2.34 sec: 1.25x faster                                                    |
| sqlglot_optimize         | 65.3 ms                                                | 52.9 ms: 1.24x faster                                                     |
| fannkuch                 | 486 ms                                                 | 394 ms: 1.23x faster                                                      |
| nqueens                  | 100 ms                                                 | 81.1 ms: 1.23x faster                                                     |
| deepcopy_reduce          | 3.82 us                                                | 3.15 us: 1.21x faster                                                     |
| scimark_fft              | 424 ms                                                 | 355 ms: 1.19x faster                                                      |
| create_gc_cycles         | 1.67 ms                                                | 1.42 ms: 1.18x faster                                                     |
| xml_etree_iterparse      | 111 ms                                                 | 94.5 ms: 1.18x faster                                                     |
| xml_etree_parse          | 163 ms                                                 | 140 ms: 1.16x faster                                                      |
| scimark_sparse_mat_mult  | 5.45 ms                                                | 4.69 ms: 1.16x faster                                                     |
| xml_etree_generate       | 94.2 ms                                                | 81.8 ms: 1.15x faster                                                     |
| bench_thread_pool        | 947 us                                                 | 829 us: 1.14x faster                                                      |
| dulwich_log              | 75.9 ms                                                | 66.8 ms: 1.14x faster                                                     |
| json                     | 5.42 ms                                                | 4.85 ms: 1.12x faster                                                     |
| regex_v8                 | 25.0 ms                                                | 22.5 ms: 1.12x faster                                                     |
| json_loads               | 28.8 us                                                | 26.1 us: 1.11x faster                                                     |
| gc_traversal             | 3.84 ms                                                | 3.51 ms: 1.10x faster                                                     |
| pathlib                  | 20.0 ms                                                | 18.6 ms: 1.08x faster                                                     |
| meteor_contest           | 115 ms                                                 | 107 ms: 1.07x faster                                                      |
| sqlite_synth             | 2.93 us                                                | 2.74 us: 1.07x faster                                                     |
| regex_dna                | 222 ms                                                 | 209 ms: 1.06x faster                                                      |
| mdp                      | 2.82 sec                                               | 2.69 sec: 1.05x faster                                                    |
| pidigits                 | 190 ms                                                 | 189 ms: 1.00x faster                                                      |
| pickle_list              | 4.56 us                                                | 4.58 us: 1.00x slower                                                     |
| pickle                   | 10.3 us                                                | 10.5 us: 1.02x slower                                                     |
| async_generators         | 425 ms                                                 | 433 ms: 1.02x slower                                                      |
| unpickle_list            | 4.82 us                                                | 4.94 us: 1.03x slower                                                     |
| unpickle                 | 14.1 us                                                | 15.4 us: 1.09x slower                                                     |
| dask                     | 423 ms                                                 | 485 ms: 1.15x slower                                                      |
| regex_effbot             | 3.23 ms                                                | 3.72 ms: 1.15x slower                                                     |
| pickle_dict              | 27.3 us                                                | 31.8 us: 1.17x slower                                                     |
| python_startup_no_site   | 5.82 ms                                                | 6.84 ms: 1.18x slower                                                     |
| telco                    | 6.54 ms                                                | 7.89 ms: 1.21x slower                                                     |
| coverage                 | 72.8 ms                                                | 93.4 ms: 1.28x slower                                                     |
| Geometric mean           | (ref)                                                  | 1.34x faster                                                              |

Benchmark hidden because not significant (1): bench_mp_pool
Ignored benchmarks (18) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: 2to3, aiohttp, chameleon, django_template, djangocms, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.28x
- 95% likely to have a speedup of 1.26x
- 99% likely to have a speedup of 1.24x
