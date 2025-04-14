# Results vs. 3.10.4

- fork: faster-cpython
- ref: trashcan_in_dealloc
- machine: linux-aarch64
- commit hash: 8aa20f2
- commit date: 2025-04-09
- overall geometric mean: 1.339x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 297 ms: 1.28x faster                                                              |
| docutils       | 3.53 sec                                                              | 2.94 sec: 1.20x faster                                                            |
| html5lib       | 86.5 ms                                                               | 63.0 ms: 1.37x faster                                                             |
| Geometric mean | (ref)                                                                 | 1.28x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 873 ms: 2.62x faster                                                              |
| async_tree_memoization  | 1.13 sec                                                              | 458 ms: 2.47x faster                                                              |
| async_tree_none         | 950 ms                                                                | 386 ms: 2.46x faster                                                              |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 658 ms: 1.93x faster                                                              |
| Geometric mean          | (ref)                                                                 | 2.35x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 86.0 ms: 1.57x faster                                                             |
| nbody          | 166 ms                                                                | 121 ms: 1.37x faster                                                              |
| pidigits       | 235 ms                                                                | 233 ms: 1.01x faster                                                              |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 124 ms: 1.42x faster                                                              |
| regex_v8       | 32.2 ms                                                               | 27.8 ms: 1.16x faster                                                             |
| regex_effbot   | 4.25 ms                                                               | 3.99 ms: 1.07x faster                                                             |
| regex_dna      | 257 ms                                                                | 242 ms: 1.06x faster                                                              |
| Geometric mean | (ref)                                                                 | 1.17x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 262 us: 1.40x faster                                                              |
| pickle_pure_python   | 529 us                                                                | 387 us: 1.37x faster                                                              |
| tomli_loads          | 3.36 sec                                                              | 2.48 sec: 1.36x faster                                                            |
| xml_etree_process    | 99.5 ms                                                               | 79.2 ms: 1.26x faster                                                             |
| xml_etree_parse      | 212 ms                                                                | 175 ms: 1.21x faster                                                              |
| json_dumps           | 16.7 ms                                                               | 14.1 ms: 1.18x faster                                                             |
| xml_etree_iterparse  | 156 ms                                                                | 140 ms: 1.11x faster                                                              |
| xml_etree_generate   | 123 ms                                                                | 112 ms: 1.10x faster                                                              |
| json_loads           | 30.9 us                                                               | 34.8 us: 1.13x slower                                                             |
| Geometric mean       | (ref)                                                                 | 1.20x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                             |
| python_startup_no_site | 6.89 ms                                                               | 10.2 ms: 1.47x slower                                                             |
| Geometric mean         | (ref)                                                                 | 1.46x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 14.0 ms: 1.35x faster                                                             |
| django_template | 53.3 ms                                                               | 40.7 ms: 1.31x faster                                                             |
| genshi_text     | 35.2 ms                                                               | 28.3 ms: 1.24x faster                                                             |
| genshi_xml      | 69.8 ms                                                               | 61.6 ms: 1.13x faster                                                             |
| Geometric mean  | (ref)                                                                 | 1.26x faster                                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 205 us: 3.23x faster                                                              |
| async_tree_io            | 2.28 sec                                                              | 873 ms: 2.62x faster                                                              |
| async_tree_memoization   | 1.13 sec                                                              | 458 ms: 2.47x faster                                                              |
| async_tree_none          | 950 ms                                                                | 386 ms: 2.46x faster                                                              |
| deltablue                | 8.94 ms                                                               | 3.82 ms: 2.34x faster                                                             |
| mdp                      | 3.70 sec                                                              | 1.64 sec: 2.25x faster                                                            |
| go                       | 264 ms                                                                | 131 ms: 2.01x faster                                                              |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 658 ms: 1.93x faster                                                              |
| richards_super           | 107 ms                                                                | 58.1 ms: 1.85x faster                                                             |
| generators               | 68.1 ms                                                               | 37.8 ms: 1.80x faster                                                             |
| chaos                    | 121 ms                                                                | 67.8 ms: 1.78x faster                                                             |
| richards                 | 91.7 ms                                                               | 52.2 ms: 1.76x faster                                                             |
| raytrace                 | 573 ms                                                                | 327 ms: 1.75x faster                                                              |
| logging_silent           | 222 ns                                                                | 132 ns: 1.68x faster                                                              |
| scimark_sor              | 246 ms                                                                | 148 ms: 1.66x faster                                                              |
| deepcopy_memo            | 61.7 us                                                               | 37.9 us: 1.63x faster                                                             |
| scimark_lu               | 227 ms                                                                | 143 ms: 1.59x faster                                                              |
| pylint                   | 485 ms                                                                | 309 ms: 1.57x faster                                                              |
| float                    | 135 ms                                                                | 86.0 ms: 1.57x faster                                                             |
| hexiom                   | 10.9 ms                                                               | 7.09 ms: 1.54x faster                                                             |
| scimark_monte_carlo      | 128 ms                                                                | 83.1 ms: 1.54x faster                                                             |
| deepcopy                 | 511 us                                                                | 333 us: 1.53x faster                                                              |
| crypto_pyaes             | 134 ms                                                                | 87.8 ms: 1.53x faster                                                             |
| comprehensions           | 33.1 us                                                               | 21.8 us: 1.52x faster                                                             |
| pyflate                  | 795 ms                                                                | 546 ms: 1.46x faster                                                              |
| spectral_norm            | 186 ms                                                                | 129 ms: 1.44x faster                                                              |
| regex_compile            | 177 ms                                                                | 124 ms: 1.42x faster                                                              |
| dulwich_log              | 73.5 ms                                                               | 52.5 ms: 1.40x faster                                                             |
| unpickle_pure_python     | 366 us                                                                | 262 us: 1.40x faster                                                              |
| html5lib                 | 86.5 ms                                                               | 63.0 ms: 1.37x faster                                                             |
| pycparser                | 1.69 sec                                                              | 1.24 sec: 1.37x faster                                                            |
| nbody                    | 166 ms                                                                | 121 ms: 1.37x faster                                                              |
| pickle_pure_python       | 529 us                                                                | 387 us: 1.37x faster                                                              |
| logging_simple           | 9.78 us                                                               | 7.17 us: 1.36x faster                                                             |
| tomli_loads              | 3.36 sec                                                              | 2.48 sec: 1.36x faster                                                            |
| mako                     | 18.9 ms                                                               | 14.0 ms: 1.35x faster                                                             |
| logging_format           | 10.6 us                                                               | 7.84 us: 1.35x faster                                                             |
| sqlalchemy_declarative   | 197 ms                                                                | 149 ms: 1.33x faster                                                              |
| deepcopy_reduce          | 4.60 us                                                               | 3.50 us: 1.31x faster                                                             |
| django_template          | 53.3 ms                                                               | 40.7 ms: 1.31x faster                                                             |
| sympy_integrate          | 26.5 ms                                                               | 20.4 ms: 1.30x faster                                                             |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.9 ms: 1.29x faster                                                             |
| sympy_sum                | 184 ms                                                                | 143 ms: 1.28x faster                                                              |
| 2to3                     | 381 ms                                                                | 297 ms: 1.28x faster                                                              |
| xml_etree_process        | 99.5 ms                                                               | 79.2 ms: 1.26x faster                                                             |
| genshi_text              | 35.2 ms                                                               | 28.3 ms: 1.24x faster                                                             |
| sympy_str                | 329 ms                                                                | 265 ms: 1.24x faster                                                              |
| pprint_pformat           | 2.36 sec                                                              | 1.91 sec: 1.23x faster                                                            |
| pprint_safe_repr         | 1.15 sec                                                              | 931 ms: 1.23x faster                                                              |
| coroutines               | 37.2 ms                                                               | 30.3 ms: 1.23x faster                                                             |
| xml_etree_parse          | 212 ms                                                                | 175 ms: 1.21x faster                                                              |
| docutils                 | 3.53 sec                                                              | 2.94 sec: 1.20x faster                                                            |
| json_dumps               | 16.7 ms                                                               | 14.1 ms: 1.18x faster                                                             |
| pathlib                  | 26.3 ms                                                               | 22.3 ms: 1.18x faster                                                             |
| sympy_expand             | 543 ms                                                                | 460 ms: 1.18x faster                                                              |
| bench_thread_pool        | 1.59 ms                                                               | 1.35 ms: 1.18x faster                                                             |
| regex_v8                 | 32.2 ms                                                               | 27.8 ms: 1.16x faster                                                             |
| nqueens                  | 117 ms                                                                | 102 ms: 1.15x faster                                                              |
| scimark_fft              | 500 ms                                                                | 437 ms: 1.15x faster                                                              |
| genshi_xml               | 69.8 ms                                                               | 61.6 ms: 1.13x faster                                                             |
| meteor_contest           | 126 ms                                                                | 112 ms: 1.13x faster                                                              |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.82 ms: 1.12x faster                                                             |
| xml_etree_iterparse      | 156 ms                                                                | 140 ms: 1.11x faster                                                              |
| fannkuch                 | 546 ms                                                                | 494 ms: 1.10x faster                                                              |
| xml_etree_generate       | 123 ms                                                                | 112 ms: 1.10x faster                                                              |
| regex_effbot             | 4.25 ms                                                               | 3.99 ms: 1.07x faster                                                             |
| sqlite_synth             | 4.12 us                                                               | 3.87 us: 1.06x faster                                                             |
| regex_dna                | 257 ms                                                                | 242 ms: 1.06x faster                                                              |
| pidigits                 | 235 ms                                                                | 233 ms: 1.01x faster                                                              |
| asyncio_websockets       | 657 ms                                                                | 667 ms: 1.02x slower                                                              |
| async_generators         | 452 ms                                                                | 462 ms: 1.02x slower                                                              |
| json                     | 5.88 ms                                                               | 6.03 ms: 1.03x slower                                                             |
| telco                    | 8.49 ms                                                               | 9.55 ms: 1.12x slower                                                             |
| json_loads               | 30.9 us                                                               | 34.8 us: 1.13x slower                                                             |
| coverage                 | 83.6 ms                                                               | 104 ms: 1.25x slower                                                              |
| python_startup           | 11.2 ms                                                               | 16.2 ms: 1.45x slower                                                             |
| python_startup_no_site   | 6.89 ms                                                               | 10.2 ms: 1.47x slower                                                             |
| create_gc_cycles         | 2.26 ms                                                               | 3.56 ms: 1.58x slower                                                             |
| gc_traversal             | 4.15 ms                                                               | 6.56 ms: 1.58x slower                                                             |
| bench_mp_pool            | 14.5 ms                                                               | 4.04 sec: 277.86x slower                                                          |
| Geometric mean           | (ref)                                                                 | 1.23x faster                                                                      |
Ignored benchmarks (19) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250409-3.14.0a7+-8aa20f2/bm-20250409-arminc-aarch64-faster%2dcpython-trashcan_in_dealloc-3.14.0a7+-8aa20f2.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.339x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.27x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.31x