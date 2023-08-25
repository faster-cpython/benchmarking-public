
# Results vs. 3.11.0

- fork: faster-cpython
- ref: incremental_gc
- machine: linux-x86_64
- commit hash: af24cd7
- commit date: 2023-08-12
- overall geometric mean: 1.07x faster
- HPT reliability: 67.70%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark    | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-af24cd7 |
|--------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tornado_http | 96.3 ms                                                | 92.9 ms: 1.04x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-af24cd7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 88.8 ms: 1.05x faster                                                     |
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                      |
| float          | 77.2 ms                                                | 76.8 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.03x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-af24cd7 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.73 ms: 1.07x faster                                                     |
| regex_compile  | 138 ms                                                 | 136 ms: 1.01x faster                                                      |
| regex_v8       | 22.0 ms                                                | 22.3 ms: 1.01x slower                                                     |
| regex_dna      | 204 ms                                                 | 209 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                  | 1.01x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-af24cd7 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 10.0 ms: 1.26x faster                                                     |
| unpickle_pure_python | 228 us                                                 | 215 us: 1.06x faster                                                      |
| pickle_pure_python   | 306 us                                                 | 293 us: 1.04x faster                                                      |
| json_loads           | 26.5 us                                                | 25.4 us: 1.04x faster                                                     |
| xml_etree_iterparse  | 104 ms                                                 | 105 ms: 1.01x slower                                                      |
| unpickle_list        | 4.91 us                                                | 5.08 us: 1.03x slower                                                     |
| pickle               | 10.1 us                                                | 10.5 us: 1.04x slower                                                     |
| pickle_dict          | 31.1 us                                                | 32.7 us: 1.05x slower                                                     |
| xml_etree_parse      | 158 ms                                                 | 168 ms: 1.06x slower                                                      |
| xml_etree_process    | 53.9 ms                                                | 57.3 ms: 1.06x slower                                                     |
| unpickle             | 13.7 us                                                | 14.9 us: 1.09x slower                                                     |
| xml_etree_generate   | 76.2 ms                                                | 83.3 ms: 1.09x slower                                                     |
| pickle_list          | 4.11 us                                                | 4.70 us: 1.14x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-af24cd7 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.29 ms: 1.09x slower                                                     |
| python_startup_no_site | 6.01 ms                                                | 6.75 ms: 1.12x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.11x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-af24cd7 |
|-----------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako      | 10.1 ms                                                | 10.7 ms: 1.06x slower                                                     |

All benchmarks:
===============

| Benchmark                | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230812-linux-x86_64-faster%2dcpython-incremental_gc-3.13.0a0-af24cd7 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 486 us                                                 | 145 us: 3.34x faster                                                      |
| generators               | 73.5 ms                                                | 28.2 ms: 2.61x faster                                                     |
| asyncio_tcp              | 922 ms                                                 | 485 ms: 1.90x faster                                                      |
| async_tree_io            | 1.30 sec                                               | 717 ms: 1.81x faster                                                      |
| asyncio_tcp_ssl          | 3.14 sec                                               | 1.78 sec: 1.76x faster                                                    |
| async_tree_memoization   | 627 ms                                                 | 406 ms: 1.55x faster                                                      |
| async_tree_none          | 526 ms                                                 | 341 ms: 1.54x faster                                                      |
| async_tree_cpu_io_mixed  | 739 ms                                                 | 575 ms: 1.29x faster                                                      |
| json_dumps               | 12.6 ms                                                | 10.0 ms: 1.26x faster                                                     |
| mypy2                    | 420 ms                                                 | 359 ms: 1.17x faster                                                      |
| chaos                    | 69.2 ms                                                | 59.4 ms: 1.16x faster                                                     |
| deltablue                | 3.67 ms                                                | 3.16 ms: 1.16x faster                                                     |
| coroutines               | 25.5 ms                                                | 22.2 ms: 1.15x faster                                                     |
| gc_traversal             | 4.02 ms                                                | 3.60 ms: 1.12x faster                                                     |
| raytrace                 | 297 ms                                                 | 266 ms: 1.12x faster                                                      |
| comprehensions           | 22.4 us                                                | 20.2 us: 1.11x faster                                                     |
| sqlglot_parse            | 1.40 ms                                                | 1.28 ms: 1.10x faster                                                     |
| coverage                 | 100 ms                                                 | 92.6 ms: 1.08x faster                                                     |
| sqlglot_transpile        | 1.70 ms                                                | 1.58 ms: 1.08x faster                                                     |
| crypto_pyaes             | 74.7 ms                                                | 69.6 ms: 1.07x faster                                                     |
| regex_effbot             | 3.99 ms                                                | 3.73 ms: 1.07x faster                                                     |
| richards_super           | 56.8 ms                                                | 53.3 ms: 1.07x faster                                                     |
| hexiom                   | 6.37 ms                                                | 6.01 ms: 1.06x faster                                                     |
| unpickle_pure_python     | 228 us                                                 | 215 us: 1.06x faster                                                      |
| nbody                    | 93.1 ms                                                | 88.8 ms: 1.05x faster                                                     |
| pidigits                 | 198 ms                                                 | 189 ms: 1.05x faster                                                      |
| nqueens                  | 83.4 ms                                                | 79.6 ms: 1.05x faster                                                     |
| pickle_pure_python       | 306 us                                                 | 293 us: 1.04x faster                                                      |
| json_loads               | 26.5 us                                                | 25.4 us: 1.04x faster                                                     |
| logging_format           | 6.68 us                                                | 6.44 us: 1.04x faster                                                     |
| tornado_http             | 96.3 ms                                                | 92.9 ms: 1.04x faster                                                     |
| create_gc_cycles         | 1.49 ms                                                | 1.44 ms: 1.03x faster                                                     |
| logging_silent           | 101 ns                                                 | 98.1 ns: 1.03x faster                                                     |
| scimark_monte_carlo      | 68.1 ms                                                | 66.1 ms: 1.03x faster                                                     |
| logging_simple           | 6.03 us                                                | 5.89 us: 1.02x faster                                                     |
| json                     | 4.94 ms                                                | 4.83 ms: 1.02x faster                                                     |
| go                       | 140 ms                                                 | 138 ms: 1.02x faster                                                      |
| sqlglot_normalize        | 108 ms                                                 | 106 ms: 1.02x faster                                                      |
| regex_compile            | 138 ms                                                 | 136 ms: 1.01x faster                                                      |
| float                    | 77.2 ms                                                | 76.8 ms: 1.01x faster                                                     |
| sqlglot_optimize         | 53.1 ms                                                | 53.4 ms: 1.01x slower                                                     |
| bench_thread_pool        | 819 us                                                 | 824 us: 1.01x slower                                                      |
| pprint_pformat           | 1.46 sec                                               | 1.47 sec: 1.01x slower                                                    |
| xml_etree_iterparse      | 104 ms                                                 | 105 ms: 1.01x slower                                                      |
| regex_v8                 | 22.0 ms                                                | 22.3 ms: 1.01x slower                                                     |
| scimark_lu               | 110 ms                                                 | 111 ms: 1.01x slower                                                      |
| mdp                      | 2.62 sec                                               | 2.65 sec: 1.01x slower                                                    |
| deepcopy_memo            | 37.0 us                                                | 37.8 us: 1.02x slower                                                     |
| pprint_safe_repr         | 701 ms                                                 | 716 ms: 1.02x slower                                                      |
| fannkuch                 | 388 ms                                                 | 396 ms: 1.02x slower                                                      |
| scimark_sor              | 118 ms                                                 | 121 ms: 1.02x slower                                                      |
| pathlib                  | 18.2 ms                                                | 18.7 ms: 1.02x slower                                                     |
| regex_dna                | 204 ms                                                 | 209 ms: 1.02x slower                                                      |
| richards                 | 45.7 ms                                                | 47.2 ms: 1.03x slower                                                     |
| unpickle_list            | 4.91 us                                                | 5.08 us: 1.03x slower                                                     |
| deepcopy                 | 342 us                                                 | 356 us: 1.04x slower                                                      |
| pickle                   | 10.1 us                                                | 10.5 us: 1.04x slower                                                     |
| dulwich_log              | 63.7 ms                                                | 66.5 ms: 1.05x slower                                                     |
| scimark_sparse_mat_mult  | 4.50 ms                                                | 4.73 ms: 1.05x slower                                                     |
| pickle_dict              | 31.1 us                                                | 32.7 us: 1.05x slower                                                     |
| pyflate                  | 418 ms                                                 | 440 ms: 1.05x slower                                                      |
| mako                     | 10.1 ms                                                | 10.7 ms: 1.06x slower                                                     |
| xml_etree_parse          | 158 ms                                                 | 168 ms: 1.06x slower                                                      |
| spectral_norm            | 100 ms                                                 | 106 ms: 1.06x slower                                                      |
| xml_etree_process        | 53.9 ms                                                | 57.3 ms: 1.06x slower                                                     |
| unpack_sequence          | 43.1 ns                                                | 46.0 ns: 1.07x slower                                                     |
| scimark_fft              | 328 ms                                                 | 353 ms: 1.07x slower                                                      |
| deepcopy_reduce          | 2.94 us                                                | 3.19 us: 1.09x slower                                                     |
| python_startup           | 8.52 ms                                                | 9.29 ms: 1.09x slower                                                     |
| unpickle                 | 13.7 us                                                | 14.9 us: 1.09x slower                                                     |
| xml_etree_generate       | 76.2 ms                                                | 83.3 ms: 1.09x slower                                                     |
| sqlite_synth             | 2.52 us                                                | 2.76 us: 1.10x slower                                                     |
| python_startup_no_site   | 6.01 ms                                                | 6.75 ms: 1.12x slower                                                     |
| pickle_list              | 4.11 us                                                | 4.70 us: 1.14x slower                                                     |
| async_generators         | 368 ms                                                 | 437 ms: 1.18x slower                                                      |
| telco                    | 6.58 ms                                                | 7.95 ms: 1.21x slower                                                     |
| dask                     | 360 ms                                                 | 499 ms: 1.39x slower                                                      |
| Geometric mean           | (ref)                                                  | 1.07x faster                                                              |

Benchmark hidden because not significant (2): meteor_contest, bench_mp_pool
Ignored benchmarks (21) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: 2to3, aiohttp, chameleon, django_template, djangocms, docutils, flaskblogging, genshi_text, genshi_xml, gunicorn, html5lib, pycparser, pylint, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads


# HPT report

- Reliability score: 67.70% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
