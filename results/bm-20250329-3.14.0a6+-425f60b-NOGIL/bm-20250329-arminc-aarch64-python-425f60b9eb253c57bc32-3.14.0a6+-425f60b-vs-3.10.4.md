# Results vs. 3.10.4

- fork: python
- ref: 425f60b9eb253c57bc32
- machine: linux-aarch64
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.147x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.61x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 359 ms: 1.06x faster                                                     |
| docutils       | 3.53 sec                                                              | 3.31 sec: 1.07x faster                                                   |
| html5lib       | 86.5 ms                                                               | 74.7 ms: 1.16x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.09x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 904 ms: 2.53x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 497 ms: 2.28x faster                                                     |
| async_tree_none         | 950 ms                                                                | 418 ms: 2.27x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 683 ms: 1.86x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.22x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 101 ms: 1.34x faster                                                     |
| nbody          | 166 ms                                                                | 182 ms: 1.10x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 32.2 ms                                                               | 27.5 ms: 1.17x faster                                                    |
| regex_compile  | 177 ms                                                                | 160 ms: 1.10x faster                                                     |
| regex_effbot   | 4.25 ms                                                               | 3.95 ms: 1.08x faster                                                    |
| regex_dna      | 257 ms                                                                | 253 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.09x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 303 us: 1.21x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 130 ms: 1.20x faster                                                     |
| xml_etree_parse      | 212 ms                                                                | 177 ms: 1.19x faster                                                     |
| pickle_pure_python   | 529 us                                                                | 448 us: 1.18x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 3.05 sec: 1.10x faster                                                   |
| pickle_list          | 5.24 us                                                               | 5.67 us: 1.08x slower                                                    |
| pickle_dict          | 35.1 us                                                               | 39.3 us: 1.12x slower                                                    |
| unpickle             | 17.5 us                                                               | 19.6 us: 1.12x slower                                                    |
| xml_etree_generate   | 123 ms                                                                | 139 ms: 1.13x slower                                                     |
| json_loads           | 30.9 us                                                               | 38.4 us: 1.24x slower                                                    |
| pickle               | 12.5 us                                                               | 15.6 us: 1.25x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                             |

Benchmark hidden because not significant (3): json_dumps, xml_etree_process, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 19.6 ms: 1.75x slower                                                    |
| python_startup_no_site | 6.89 ms                                                               | 14.0 ms: 2.03x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.89x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text    | 35.2 ms                                                               | 36.5 ms: 1.04x slower                                                    |
| genshi_xml     | 69.8 ms                                                               | 74.0 ms: 1.06x slower                                                    |
| mako           | 18.9 ms                                                               | 22.3 ms: 1.18x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                             |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io            | 2.28 sec                                                              | 904 ms: 2.53x faster                                                     |
| typing_runtime_protocols | 661 us                                                                | 265 us: 2.50x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 497 ms: 2.28x faster                                                     |
| async_tree_none          | 950 ms                                                                | 418 ms: 2.27x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 683 ms: 1.86x faster                                                     |
| mdp                      | 3.70 sec                                                              | 1.99 sec: 1.86x faster                                                   |
| deltablue                | 8.94 ms                                                               | 5.01 ms: 1.78x faster                                                    |
| generators               | 68.1 ms                                                               | 38.8 ms: 1.76x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 579 ms: 1.63x faster                                                     |
| gc_traversal             | 4.15 ms                                                               | 2.69 ms: 1.55x faster                                                    |
| go                       | 264 ms                                                                | 171 ms: 1.54x faster                                                     |
| logging_silent           | 222 ns                                                                | 148 ns: 1.51x faster                                                     |
| scimark_sor              | 246 ms                                                                | 170 ms: 1.45x faster                                                     |
| chaos                    | 121 ms                                                                | 85.1 ms: 1.42x faster                                                    |
| raytrace                 | 573 ms                                                                | 405 ms: 1.41x faster                                                     |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.44 sec: 1.35x faster                                                   |
| float                    | 135 ms                                                                | 101 ms: 1.34x faster                                                     |
| spectral_norm            | 186 ms                                                                | 140 ms: 1.33x faster                                                     |
| pylint                   | 485 ms                                                                | 374 ms: 1.30x faster                                                     |
| richards_super           | 107 ms                                                                | 83.8 ms: 1.28x faster                                                    |
| deepcopy                 | 511 us                                                                | 401 us: 1.27x faster                                                     |
| hexiom                   | 10.9 ms                                                               | 8.61 ms: 1.27x faster                                                    |
| pyflate                  | 795 ms                                                                | 627 ms: 1.27x faster                                                     |
| dulwich_log              | 73.5 ms                                                               | 59.1 ms: 1.24x faster                                                    |
| richards                 | 91.7 ms                                                               | 73.9 ms: 1.24x faster                                                    |
| comprehensions           | 33.1 us                                                               | 26.8 us: 1.24x faster                                                    |
| scimark_lu               | 227 ms                                                                | 186 ms: 1.22x faster                                                     |
| pycparser                | 1.69 sec                                                              | 1.39 sec: 1.22x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 50.7 us: 1.22x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 303 us: 1.21x faster                                                     |
| coroutines               | 37.2 ms                                                               | 30.9 ms: 1.20x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 130 ms: 1.20x faster                                                     |
| xml_etree_parse          | 212 ms                                                                | 177 ms: 1.19x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 113 ms: 1.19x faster                                                     |
| pickle_pure_python       | 529 us                                                                | 448 us: 1.18x faster                                                     |
| regex_v8                 | 32.2 ms                                                               | 27.5 ms: 1.17x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 74.7 ms: 1.16x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.59 us: 1.15x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 23.1 ms: 1.14x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 113 ms: 1.13x faster                                                     |
| logging_simple           | 9.78 us                                                               | 8.80 us: 1.11x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 3.05 sec: 1.10x faster                                                   |
| regex_compile            | 177 ms                                                                | 160 ms: 1.10x faster                                                     |
| logging_format           | 10.6 us                                                               | 9.75 us: 1.09x faster                                                    |
| regex_effbot             | 4.25 ms                                                               | 3.95 ms: 1.08x faster                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 2.12 ms: 1.07x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.31 sec: 1.07x faster                                                   |
| 2to3                     | 381 ms                                                                | 359 ms: 1.06x faster                                                     |
| scimark_fft              | 500 ms                                                                | 480 ms: 1.04x faster                                                     |
| deepcopy_reduce          | 4.60 us                                                               | 4.42 us: 1.04x faster                                                    |
| pprint_safe_repr         | 1.15 sec                                                              | 1.10 sec: 1.04x faster                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.29 sec: 1.03x faster                                                   |
| regex_dna                | 257 ms                                                                | 253 ms: 1.02x faster                                                     |
| asyncio_websockets       | 657 ms                                                                | 669 ms: 1.02x slower                                                     |
| nqueens                  | 117 ms                                                                | 121 ms: 1.03x slower                                                     |
| sqlalchemy_imperative    | 20.5 ms                                                               | 21.2 ms: 1.03x slower                                                    |
| genshi_text              | 35.2 ms                                                               | 36.5 ms: 1.04x slower                                                    |
| genshi_xml               | 69.8 ms                                                               | 74.0 ms: 1.06x slower                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 8.11 ms: 1.06x slower                                                    |
| sympy_str                | 329 ms                                                                | 353 ms: 1.07x slower                                                     |
| pickle_list              | 5.24 us                                                               | 5.67 us: 1.08x slower                                                    |
| nbody                    | 166 ms                                                                | 182 ms: 1.10x slower                                                     |
| json                     | 5.88 ms                                                               | 6.47 ms: 1.10x slower                                                    |
| sympy_expand             | 543 ms                                                                | 603 ms: 1.11x slower                                                     |
| pickle_dict              | 35.1 us                                                               | 39.3 us: 1.12x slower                                                    |
| unpickle                 | 17.5 us                                                               | 19.6 us: 1.12x slower                                                    |
| xml_etree_generate       | 123 ms                                                                | 139 ms: 1.13x slower                                                     |
| bench_thread_pool        | 1.59 ms                                                               | 1.82 ms: 1.14x slower                                                    |
| fannkuch                 | 546 ms                                                                | 625 ms: 1.15x slower                                                     |
| async_generators         | 452 ms                                                                | 519 ms: 1.15x slower                                                     |
| mako                     | 18.9 ms                                                               | 22.3 ms: 1.18x slower                                                    |
| meteor_contest           | 126 ms                                                                | 150 ms: 1.18x slower                                                     |
| json_loads               | 30.9 us                                                               | 38.4 us: 1.24x slower                                                    |
| pickle                   | 12.5 us                                                               | 15.6 us: 1.25x slower                                                    |
| telco                    | 8.49 ms                                                               | 11.5 ms: 1.36x slower                                                    |
| python_startup           | 11.2 ms                                                               | 19.6 ms: 1.75x slower                                                    |
| coverage                 | 83.6 ms                                                               | 149 ms: 1.78x slower                                                     |
| python_startup_no_site   | 6.89 ms                                                               | 14.0 ms: 2.03x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 57.2 ms: 3.94x slower                                                    |
| Geometric mean           | (ref)                                                                 | 1.11x faster                                                             |

Benchmark hidden because not significant (8): sqlalchemy_declarative, json_dumps, pidigits, xml_etree_process, django_template, unpickle_list, sympy_integrate, sympy_sum
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (16) of results/bm-20250329-3.14.0a6+-425f60b-NOGIL/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.147x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.61x