# Results vs. 3.10.4

- fork: python
- ref: 359c7dde3bb074e02968
- machine: linux-aarch64
- commit hash: 359c7dd
- commit date: 2025-02-16
- overall geometric mean: 1.322x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 304 ms: 1.25x faster                                                     |
| docutils       | 3.53 sec                                                              | 3.01 sec: 1.17x faster                                                   |
| html5lib       | 86.5 ms                                                               | 62.1 ms: 1.39x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.27x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 942 ms: 2.42x faster                                                     |
| async_tree_none         | 950 ms                                                                | 401 ms: 2.37x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 502 ms: 2.26x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 686 ms: 1.85x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.21x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 88.3 ms: 1.53x faster                                                    |
| nbody          | 166 ms                                                                | 121 ms: 1.37x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 129 ms: 1.37x faster                                                     |
| regex_dna      | 257 ms                                                                | 267 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                             |

Benchmark hidden because not significant (2): regex_effbot, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 263 us: 1.39x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.58 sec: 1.30x faster                                                   |
| pickle_pure_python   | 529 us                                                                | 409 us: 1.29x faster                                                     |
| xml_etree_process    | 99.5 ms                                                               | 83.2 ms: 1.20x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 184 ms: 1.15x faster                                                     |
| json_dumps           | 16.7 ms                                                               | 15.2 ms: 1.09x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.09x faster                                                     |
| unpickle_list        | 6.99 us                                                               | 6.44 us: 1.09x faster                                                    |
| xml_etree_iterparse  | 156 ms                                                                | 145 ms: 1.07x faster                                                     |
| pickle_dict          | 35.1 us                                                               | 39.5 us: 1.12x slower                                                    |
| pickle_list          | 5.24 us                                                               | 6.06 us: 1.16x slower                                                    |
| json_loads           | 30.9 us                                                               | 36.5 us: 1.18x slower                                                    |
| pickle               | 12.5 us                                                               | 16.3 us: 1.30x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.06x faster                                                             |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.08 ms: 1.32x slower                                                    |
| python_startup         | 11.2 ms                                                               | 16.3 ms: 1.45x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.38x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 39.0 ms: 1.37x faster                                                    |
| mako            | 18.9 ms                                                               | 14.1 ms: 1.34x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 27.3 ms: 1.29x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 61.9 ms: 1.13x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.28x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 201 us: 3.29x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 942 ms: 2.42x faster                                                     |
| async_tree_none          | 950 ms                                                                | 401 ms: 2.37x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 502 ms: 2.26x faster                                                     |
| deltablue                | 8.94 ms                                                               | 3.98 ms: 2.24x faster                                                    |
| go                       | 264 ms                                                                | 141 ms: 1.88x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 686 ms: 1.85x faster                                                     |
| generators               | 68.1 ms                                                               | 36.7 ms: 1.85x faster                                                    |
| raytrace                 | 573 ms                                                                | 325 ms: 1.76x faster                                                     |
| richards                 | 91.7 ms                                                               | 52.1 ms: 1.76x faster                                                    |
| chaos                    | 121 ms                                                                | 69.0 ms: 1.75x faster                                                    |
| richards_super           | 107 ms                                                                | 62.0 ms: 1.73x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 550 ms: 1.72x faster                                                     |
| sqlglot_parse            | 2.40 ms                                                               | 1.47 ms: 1.63x faster                                                    |
| scimark_lu               | 227 ms                                                                | 141 ms: 1.61x faster                                                     |
| logging_silent           | 222 ns                                                                | 139 ns: 1.60x faster                                                     |
| pylint                   | 485 ms                                                                | 305 ms: 1.59x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 85.2 ms: 1.57x faster                                                    |
| scimark_sor              | 246 ms                                                                | 157 ms: 1.57x faster                                                     |
| comprehensions           | 33.1 us                                                               | 21.2 us: 1.56x faster                                                    |
| float                    | 135 ms                                                                | 88.3 ms: 1.53x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.86 ms: 1.52x faster                                                    |
| spectral_norm            | 186 ms                                                                | 123 ms: 1.52x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 41.0 us: 1.51x faster                                                    |
| deepcopy                 | 511 us                                                                | 345 us: 1.48x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 86.9 ms: 1.47x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.24 sec: 1.46x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 7.47 ms: 1.46x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 62.1 ms: 1.39x faster                                                    |
| unpickle_pure_python     | 366 us                                                                | 263 us: 1.39x faster                                                     |
| regex_compile            | 177 ms                                                                | 129 ms: 1.37x faster                                                     |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.0 ms: 1.37x faster                                                    |
| nbody                    | 166 ms                                                                | 121 ms: 1.37x faster                                                     |
| django_template          | 53.3 ms                                                               | 39.0 ms: 1.37x faster                                                    |
| logging_simple           | 9.78 us                                                               | 7.25 us: 1.35x faster                                                    |
| pyflate                  | 795 ms                                                                | 590 ms: 1.35x faster                                                     |
| sqlalchemy_declarative   | 197 ms                                                                | 147 ms: 1.34x faster                                                     |
| mako                     | 18.9 ms                                                               | 14.1 ms: 1.34x faster                                                    |
| logging_format           | 10.6 us                                                               | 7.96 us: 1.33x faster                                                    |
| thrift                   | 1.26 ms                                                               | 949 us: 1.33x faster                                                     |
| pycparser                | 1.69 sec                                                              | 1.29 sec: 1.31x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.58 sec: 1.30x faster                                                   |
| pickle_pure_python       | 529 us                                                                | 409 us: 1.29x faster                                                     |
| genshi_text              | 35.2 ms                                                               | 27.3 ms: 1.29x faster                                                    |
| sympy_sum                | 184 ms                                                                | 144 ms: 1.28x faster                                                     |
| coroutines               | 37.2 ms                                                               | 29.4 ms: 1.26x faster                                                    |
| 2to3                     | 381 ms                                                                | 304 ms: 1.25x faster                                                     |
| deepcopy_reduce          | 4.60 us                                                               | 3.71 us: 1.24x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 127 ms: 1.23x faster                                                     |
| sqlglot_optimize         | 75.4 ms                                                               | 61.3 ms: 1.23x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 21.7 ms: 1.22x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.31 ms: 1.21x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 61.1 ms: 1.20x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 83.2 ms: 1.20x faster                                                    |
| scimark_fft              | 500 ms                                                                | 420 ms: 1.19x faster                                                     |
| pprint_pformat           | 2.36 sec                                                              | 1.98 sec: 1.19x faster                                                   |
| sympy_str                | 329 ms                                                                | 276 ms: 1.19x faster                                                     |
| pprint_safe_repr         | 1.15 sec                                                              | 969 ms: 1.18x faster                                                     |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.45 ms: 1.18x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.01 sec: 1.17x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 22.4 ms: 1.17x faster                                                    |
| sympy_expand             | 543 ms                                                                | 466 ms: 1.16x faster                                                     |
| nqueens                  | 117 ms                                                                | 101 ms: 1.16x faster                                                     |
| xml_etree_parse          | 212 ms                                                                | 184 ms: 1.15x faster                                                     |
| genshi_xml               | 69.8 ms                                                               | 61.9 ms: 1.13x faster                                                    |
| fannkuch                 | 546 ms                                                                | 494 ms: 1.10x faster                                                     |
| json_dumps               | 16.7 ms                                                               | 15.2 ms: 1.09x faster                                                    |
| meteor_contest           | 126 ms                                                                | 116 ms: 1.09x faster                                                     |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.09x faster                                                     |
| unpickle_list            | 6.99 us                                                               | 6.44 us: 1.09x faster                                                    |
| xml_etree_iterparse      | 156 ms                                                                | 145 ms: 1.07x faster                                                     |
| mdp                      | 3.70 sec                                                              | 3.46 sec: 1.07x faster                                                   |
| asyncio_websockets       | 657 ms                                                                | 674 ms: 1.03x slower                                                     |
| regex_dna                | 257 ms                                                                | 267 ms: 1.04x slower                                                     |
| telco                    | 8.49 ms                                                               | 9.51 ms: 1.12x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 39.5 us: 1.12x slower                                                    |
| pickle_list              | 5.24 us                                                               | 6.06 us: 1.16x slower                                                    |
| json_loads               | 30.9 us                                                               | 36.5 us: 1.18x slower                                                    |
| coverage                 | 83.6 ms                                                               | 99.5 ms: 1.19x slower                                                    |
| pickle                   | 12.5 us                                                               | 16.3 us: 1.30x slower                                                    |
| python_startup_no_site   | 6.89 ms                                                               | 9.08 ms: 1.32x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.3 ms: 1.45x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.57 ms: 1.58x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 7.03 ms: 1.69x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 5.29 sec: 363.88x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.19x faster                                                             |

Benchmark hidden because not significant (7): regex_effbot, sqlite_synth, async_generators, regex_v8, unpickle, json, pidigits
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
Ignored benchmarks (12) of results/bm-20250216-3.14.0a5+-359c7dd/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.322x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.30x