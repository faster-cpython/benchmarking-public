# Results vs. 3.10.4

- fork: python
- ref: 359c7dde3bb074e02968
- machine: linux-aarch64
- commit hash: 359c7dd
- commit date: 2025-02-16
- overall geometric mean: 1.273x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: 1.32x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 322 ms: 1.18x faster                                                     |
| docutils       | 3.53 sec                                                              | 3.23 sec: 1.09x faster                                                   |
| html5lib       | 86.5 ms                                                               | 64.8 ms: 1.33x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.20x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 948 ms: 2.41x faster                                                     |
| async_tree_none         | 950 ms                                                                | 411 ms: 2.31x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 514 ms: 2.20x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 704 ms: 1.81x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.17x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 88.8 ms: 1.52x faster                                                    |
| nbody          | 166 ms                                                                | 124 ms: 1.33x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.25x faster                                                             |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 127 ms: 1.39x faster                                                     |
| regex_effbot   | 4.25 ms                                                               | 3.92 ms: 1.08x faster                                                    |
| regex_dna      | 257 ms                                                                | 246 ms: 1.04x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.11x faster                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.50 sec: 1.34x faster                                                   |
| unpickle_pure_python | 366 us                                                                | 282 us: 1.30x faster                                                     |
| pickle_pure_python   | 529 us                                                                | 416 us: 1.27x faster                                                     |
| xml_etree_process    | 99.5 ms                                                               | 83.9 ms: 1.19x faster                                                    |
| xml_etree_parse      | 212 ms                                                                | 182 ms: 1.17x faster                                                     |
| json_dumps           | 16.7 ms                                                               | 14.9 ms: 1.12x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 116 ms: 1.06x faster                                                     |
| unpickle_list        | 6.99 us                                                               | 6.59 us: 1.06x faster                                                    |
| json_loads           | 30.9 us                                                               | 34.7 us: 1.12x slower                                                    |
| pickle_list          | 5.24 us                                                               | 6.07 us: 1.16x slower                                                    |
| pickle_dict          | 35.1 us                                                               | 41.1 us: 1.17x slower                                                    |
| pickle               | 12.5 us                                                               | 16.9 us: 1.35x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.05x faster                                                             |

Benchmark hidden because not significant (2): xml_etree_iterparse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.11 ms: 1.32x slower                                                    |
| python_startup         | 11.2 ms                                                               | 16.4 ms: 1.46x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.39x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.1 ms: 1.34x faster                                                    |
| genshi_text     | 35.2 ms                                                               | 27.5 ms: 1.28x faster                                                    |
| django_template | 53.3 ms                                                               | 42.1 ms: 1.27x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 62.7 ms: 1.11x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.25x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 222 us: 2.98x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 948 ms: 2.41x faster                                                     |
| async_tree_none          | 950 ms                                                                | 411 ms: 2.31x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 514 ms: 2.20x faster                                                     |
| deltablue                | 8.94 ms                                                               | 4.18 ms: 2.14x faster                                                    |
| generators               | 68.1 ms                                                               | 37.0 ms: 1.84x faster                                                    |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 704 ms: 1.81x faster                                                     |
| chaos                    | 121 ms                                                                | 69.8 ms: 1.73x faster                                                    |
| raytrace                 | 573 ms                                                                | 333 ms: 1.72x faster                                                     |
| richards_super           | 107 ms                                                                | 62.4 ms: 1.72x faster                                                    |
| richards                 | 91.7 ms                                                               | 53.9 ms: 1.70x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 560 ms: 1.68x faster                                                     |
| go                       | 264 ms                                                                | 160 ms: 1.65x faster                                                     |
| logging_silent           | 222 ns                                                                | 135 ns: 1.64x faster                                                     |
| scimark_lu               | 227 ms                                                                | 140 ms: 1.62x faster                                                     |
| scimark_sor              | 246 ms                                                                | 156 ms: 1.58x faster                                                     |
| spectral_norm            | 186 ms                                                                | 121 ms: 1.54x faster                                                     |
| pylint                   | 485 ms                                                                | 319 ms: 1.52x faster                                                     |
| deepcopy_memo            | 61.7 us                                                               | 40.5 us: 1.52x faster                                                    |
| float                    | 135 ms                                                                | 88.8 ms: 1.52x faster                                                    |
| deepcopy                 | 511 us                                                                | 341 us: 1.50x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 86.3 ms: 1.48x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.64 ms: 1.46x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.95 ms: 1.46x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.28 sec: 1.44x faster                                                   |
| pyflate                  | 795 ms                                                                | 567 ms: 1.40x faster                                                     |
| regex_compile            | 177 ms                                                                | 127 ms: 1.39x faster                                                     |
| logging_format           | 10.6 us                                                               | 7.80 us: 1.36x faster                                                    |
| logging_simple           | 9.78 us                                                               | 7.25 us: 1.35x faster                                                    |
| comprehensions           | 33.1 us                                                               | 24.6 us: 1.35x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.50 sec: 1.34x faster                                                   |
| mako                     | 18.9 ms                                                               | 14.1 ms: 1.34x faster                                                    |
| thrift                   | 1.26 ms                                                               | 942 us: 1.34x faster                                                     |
| html5lib                 | 86.5 ms                                                               | 64.8 ms: 1.33x faster                                                    |
| nbody                    | 166 ms                                                                | 124 ms: 1.33x faster                                                     |
| crypto_pyaes             | 134 ms                                                                | 101 ms: 1.32x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 282 us: 1.30x faster                                                     |
| sqlalchemy_declarative   | 197 ms                                                                | 154 ms: 1.29x faster                                                     |
| genshi_text              | 35.2 ms                                                               | 27.5 ms: 1.28x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.60 us: 1.28x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 416 us: 1.27x faster                                                     |
| hexiom                   | 10.9 ms                                                               | 8.60 ms: 1.27x faster                                                    |
| django_template          | 53.3 ms                                                               | 42.1 ms: 1.27x faster                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 16.3 ms: 1.26x faster                                                    |
| coroutines               | 37.2 ms                                                               | 29.8 ms: 1.25x faster                                                    |
| sympy_sum                | 184 ms                                                                | 149 ms: 1.23x faster                                                     |
| sqlglot_normalize        | 156 ms                                                                | 131 ms: 1.19x faster                                                     |
| xml_etree_process        | 99.5 ms                                                               | 83.9 ms: 1.19x faster                                                    |
| 2to3                     | 381 ms                                                                | 322 ms: 1.18x faster                                                     |
| bench_thread_pool        | 1.59 ms                                                               | 1.36 ms: 1.17x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.45 sec: 1.17x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 182 ms: 1.17x faster                                                     |
| pathlib                  | 26.3 ms                                                               | 22.8 ms: 1.16x faster                                                    |
| sympy_str                | 329 ms                                                                | 286 ms: 1.15x faster                                                     |
| sympy_integrate          | 26.5 ms                                                               | 23.2 ms: 1.15x faster                                                    |
| scimark_fft              | 500 ms                                                                | 438 ms: 1.14x faster                                                     |
| dulwich_log              | 73.5 ms                                                               | 64.5 ms: 1.14x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 66.6 ms: 1.13x faster                                                    |
| json_dumps               | 16.7 ms                                                               | 14.9 ms: 1.12x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 62.7 ms: 1.11x faster                                                    |
| nqueens                  | 117 ms                                                                | 106 ms: 1.11x faster                                                     |
| docutils                 | 3.53 sec                                                              | 3.23 sec: 1.09x faster                                                   |
| sympy_expand             | 543 ms                                                                | 500 ms: 1.08x faster                                                     |
| regex_effbot             | 4.25 ms                                                               | 3.92 ms: 1.08x faster                                                    |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.07 ms: 1.08x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.46 sec: 1.07x faster                                                   |
| xml_etree_generate       | 123 ms                                                                | 116 ms: 1.06x faster                                                     |
| unpickle_list            | 6.99 us                                                               | 6.59 us: 1.06x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.93 us: 1.05x faster                                                    |
| regex_dna                | 257 ms                                                                | 246 ms: 1.04x faster                                                     |
| asyncio_websockets       | 657 ms                                                                | 673 ms: 1.02x slower                                                     |
| async_generators         | 452 ms                                                                | 485 ms: 1.07x slower                                                     |
| pprint_safe_repr         | 1.15 sec                                                              | 1.27 sec: 1.10x slower                                                   |
| pprint_pformat           | 2.36 sec                                                              | 2.64 sec: 1.12x slower                                                   |
| json_loads               | 30.9 us                                                               | 34.7 us: 1.12x slower                                                    |
| telco                    | 8.49 ms                                                               | 9.74 ms: 1.15x slower                                                    |
| pickle_list              | 5.24 us                                                               | 6.07 us: 1.16x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 41.1 us: 1.17x slower                                                    |
| coverage                 | 83.6 ms                                                               | 103 ms: 1.23x slower                                                     |
| python_startup_no_site   | 6.89 ms                                                               | 9.11 ms: 1.32x slower                                                    |
| pickle                   | 12.5 us                                                               | 16.9 us: 1.35x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.4 ms: 1.46x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.72 ms: 1.65x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.98 ms: 1.68x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 2.72 sec: 187.01x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.16x faster                                                             |

Benchmark hidden because not significant (7): xml_etree_iterparse, meteor_contest, json, fannkuch, regex_v8, unpickle, pidigits
Ignored benchmarks (7) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, tornado_http
Ignored benchmarks (12) of results/bm-20250216-3.14.0a5+-359c7dd-JIT/bm-20250216-arminc-aarch64-python-359c7dde3bb074e02968-3.14.0a5+-359c7dd.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers, unpack_sequence

- Geometric mean (including insignificant results): 1.273x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.18x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: 1.32x