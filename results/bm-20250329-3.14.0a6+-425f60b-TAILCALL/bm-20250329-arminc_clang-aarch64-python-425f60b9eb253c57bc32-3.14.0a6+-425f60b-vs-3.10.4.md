# Results vs. 3.10.4

- fork: python
- ref: 425f60b9eb253c57bc32
- machine: linux-aarch64
- commit hash: 425f60b
- commit date: 2025-03-29
- overall geometric mean: 1.368x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 292 ms: 1.30x faster                                                     |
| docutils       | 3.53 sec                                                              | 2.93 sec: 1.21x faster                                                   |
| html5lib       | 86.5 ms                                                               | 59.7 ms: 1.45x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.31x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 870 ms: 2.63x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 455 ms: 2.49x faster                                                     |
| async_tree_none         | 950 ms                                                                | 382 ms: 2.49x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 721 ms: 1.77x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.32x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 83.2 ms: 1.62x faster                                                    |
| nbody          | 166 ms                                                                | 113 ms: 1.46x faster                                                     |
| pidigits       | 235 ms                                                                | 293 ms: 1.25x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.24x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 123 ms: 1.43x faster                                                     |
| regex_v8       | 32.2 ms                                                               | 30.3 ms: 1.06x faster                                                    |
| regex_dna      | 257 ms                                                                | 243 ms: 1.06x faster                                                     |
| regex_effbot   | 4.25 ms                                                               | 4.17 ms: 1.02x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.13x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 256 us: 1.43x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.39 sec: 1.41x faster                                                   |
| pickle_pure_python   | 529 us                                                                | 381 us: 1.39x faster                                                     |
| xml_etree_process    | 99.5 ms                                                               | 74.2 ms: 1.34x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 5.71 us: 1.23x faster                                                    |
| json_dumps           | 16.7 ms                                                               | 13.9 ms: 1.20x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 107 ms: 1.15x faster                                                     |
| xml_etree_iterparse  | 156 ms                                                                | 148 ms: 1.05x faster                                                     |
| xml_etree_parse      | 212 ms                                                                | 202 ms: 1.05x faster                                                     |
| unpickle             | 17.5 us                                                               | 16.9 us: 1.03x faster                                                    |
| pickle_dict          | 35.1 us                                                               | 37.1 us: 1.06x slower                                                    |
| pickle_list          | 5.24 us                                                               | 5.60 us: 1.07x slower                                                    |
| json_loads           | 30.9 us                                                               | 33.3 us: 1.08x slower                                                    |
| pickle               | 12.5 us                                                               | 15.0 us: 1.20x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.12x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                    |
| python_startup_no_site | 6.89 ms                                                               | 10.2 ms: 1.48x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.47x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 38.9 ms: 1.37x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 26.3 ms: 1.34x faster                                                    |
| mako            | 18.9 ms                                                               | 14.3 ms: 1.32x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 58.9 ms: 1.19x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.30x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 189 us: 3.49x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 870 ms: 2.63x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 455 ms: 2.49x faster                                                     |
| async_tree_none          | 950 ms                                                                | 382 ms: 2.49x faster                                                     |
| deltablue                | 8.94 ms                                                               | 3.81 ms: 2.35x faster                                                    |
| mdp                      | 3.70 sec                                                              | 1.59 sec: 2.32x faster                                                   |
| generators               | 68.1 ms                                                               | 34.7 ms: 1.96x faster                                                    |
| richards_super           | 107 ms                                                                | 54.9 ms: 1.95x faster                                                    |
| go                       | 264 ms                                                                | 136 ms: 1.94x faster                                                     |
| logging_silent           | 222 ns                                                                | 115 ns: 1.94x faster                                                     |
| richards                 | 91.7 ms                                                               | 48.3 ms: 1.90x faster                                                    |
| raytrace                 | 573 ms                                                                | 306 ms: 1.87x faster                                                     |
| chaos                    | 121 ms                                                                | 65.8 ms: 1.84x faster                                                    |
| scimark_sor              | 246 ms                                                                | 138 ms: 1.78x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 721 ms: 1.77x faster                                                     |
| asyncio_tcp              | 944 ms                                                                | 552 ms: 1.71x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 36.2 us: 1.71x faster                                                    |
| scimark_lu               | 227 ms                                                                | 134 ms: 1.69x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 76.5 ms: 1.67x faster                                                    |
| spectral_norm            | 186 ms                                                                | 112 ms: 1.66x faster                                                     |
| comprehensions           | 33.1 us                                                               | 20.0 us: 1.66x faster                                                    |
| deepcopy                 | 511 us                                                                | 309 us: 1.65x faster                                                     |
| float                    | 135 ms                                                                | 83.2 ms: 1.62x faster                                                    |
| pylint                   | 485 ms                                                                | 303 ms: 1.60x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 87.5 ms: 1.53x faster                                                    |
| pyflate                  | 795 ms                                                                | 521 ms: 1.53x faster                                                     |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.15 sec: 1.52x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 7.20 ms: 1.52x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 49.7 ms: 1.48x faster                                                    |
| nbody                    | 166 ms                                                                | 113 ms: 1.46x faster                                                     |
| html5lib                 | 86.5 ms                                                               | 59.7 ms: 1.45x faster                                                    |
| regex_compile            | 177 ms                                                                | 123 ms: 1.43x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 256 us: 1.43x faster                                                     |
| tomli_loads              | 3.36 sec                                                              | 2.39 sec: 1.41x faster                                                   |
| logging_format           | 10.6 us                                                               | 7.55 us: 1.40x faster                                                    |
| logging_simple           | 9.78 us                                                               | 7.00 us: 1.40x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 381 us: 1.39x faster                                                     |
| django_template          | 53.3 ms                                                               | 38.9 ms: 1.37x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.25 sec: 1.35x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.40 us: 1.35x faster                                                    |
| sqlalchemy_declarative   | 197 ms                                                                | 146 ms: 1.35x faster                                                     |
| xml_etree_process        | 99.5 ms                                                               | 74.2 ms: 1.34x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 26.3 ms: 1.34x faster                                                    |
| mako                     | 18.9 ms                                                               | 14.3 ms: 1.32x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 20.2 ms: 1.31x faster                                                    |
| scimark_fft              | 500 ms                                                                | 382 ms: 1.31x faster                                                     |
| sympy_sum                | 184 ms                                                                | 141 ms: 1.30x faster                                                     |
| 2to3                     | 381 ms                                                                | 292 ms: 1.30x faster                                                     |
| coroutines               | 37.2 ms                                                               | 28.6 ms: 1.30x faster                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 16.1 ms: 1.28x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.02 ms: 1.27x faster                                                    |
| sympy_str                | 329 ms                                                                | 264 ms: 1.24x faster                                                     |
| pathlib                  | 26.3 ms                                                               | 21.2 ms: 1.24x faster                                                    |
| pprint_pformat           | 2.36 sec                                                              | 1.90 sec: 1.24x faster                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 934 ms: 1.23x faster                                                     |
| unpickle_list            | 6.99 us                                                               | 5.71 us: 1.23x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.31 ms: 1.21x faster                                                    |
| docutils                 | 3.53 sec                                                              | 2.93 sec: 1.21x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 13.9 ms: 1.20x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 58.9 ms: 1.19x faster                                                    |
| sympy_expand             | 543 ms                                                                | 461 ms: 1.18x faster                                                     |
| nqueens                  | 117 ms                                                                | 101 ms: 1.16x faster                                                     |
| xml_etree_generate       | 123 ms                                                                | 107 ms: 1.15x faster                                                     |
| meteor_contest           | 126 ms                                                                | 114 ms: 1.11x faster                                                     |
| fannkuch                 | 546 ms                                                                | 496 ms: 1.10x faster                                                     |
| async_generators         | 452 ms                                                                | 414 ms: 1.09x faster                                                     |
| sqlite_synth             | 4.12 us                                                               | 3.85 us: 1.07x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 30.3 ms: 1.06x faster                                                    |
| regex_dna                | 257 ms                                                                | 243 ms: 1.06x faster                                                     |
| xml_etree_iterparse      | 156 ms                                                                | 148 ms: 1.05x faster                                                     |
| xml_etree_parse          | 212 ms                                                                | 202 ms: 1.05x faster                                                     |
| unpickle                 | 17.5 us                                                               | 16.9 us: 1.03x faster                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.17 ms: 1.02x faster                                                    |
| asyncio_websockets       | 657 ms                                                                | 669 ms: 1.02x slower                                                     |
| pickle_dict              | 35.1 us                                                               | 37.1 us: 1.06x slower                                                    |
| telco                    | 8.49 ms                                                               | 9.05 ms: 1.07x slower                                                    |
| pickle_list              | 5.24 us                                                               | 5.60 us: 1.07x slower                                                    |
| json_loads               | 30.9 us                                                               | 33.3 us: 1.08x slower                                                    |
| coverage                 | 83.6 ms                                                               | 95.6 ms: 1.14x slower                                                    |
| pickle                   | 12.5 us                                                               | 15.0 us: 1.20x slower                                                    |
| pidigits                 | 235 ms                                                                | 293 ms: 1.25x slower                                                     |
| python_startup           | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 10.2 ms: 1.48x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.69 ms: 1.61x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.80 ms: 1.68x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 2.90 sec: 199.52x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.26x faster                                                             |

Benchmark hidden because not significant (1): json
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http
Ignored benchmarks (16) of results/bm-20250329-3.14.0a6+-425f60b-CLANG/bm-20250329-arminc-aarch64-python-425f60b9eb253c57bc32-3.14.0a6+-425f60b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.368x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.37x