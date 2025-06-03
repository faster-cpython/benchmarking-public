# Results vs. 3.10.4

- fork: faster-cpython
- ref: specialize_for_iter_
- machine: linux-aarch64
- commit hash: 06c1680
- commit date: 2025-06-03
- overall geometric mean: 1.228x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.35x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250603-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 304 ms: 1.25x faster                                                              |
| docutils       | 3.53 sec                                                              | 2.92 sec: 1.21x faster                                                            |
| html5lib       | 86.5 ms                                                               | 61.2 ms: 1.41x faster                                                             |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250603-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 877 ms: 2.60x faster                                                              |
| async_tree_memoization  | 1.13 sec                                                              | 463 ms: 2.45x faster                                                              |
| async_tree_none         | 950 ms                                                                | 390 ms: 2.44x faster                                                              |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 659 ms: 1.93x faster                                                              |
| Geometric mean          | (ref)                                                                 | 2.34x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250603-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 86.0 ms: 1.57x faster                                                             |
| nbody          | 166 ms                                                                | 123 ms: 1.35x faster                                                              |
| Geometric mean | (ref)                                                                 | 1.27x faster                                                                      |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250603-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 123 ms: 1.44x faster                                                              |
| regex_v8       | 32.2 ms                                                               | 27.8 ms: 1.16x faster                                                             |
| regex_dna      | 257 ms                                                                | 229 ms: 1.12x faster                                                              |
| regex_effbot   | 4.25 ms                                                               | 3.92 ms: 1.08x faster                                                             |
| Geometric mean | (ref)                                                                 | 1.19x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250603-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 263 us: 1.39x faster                                                              |
| tomli_loads          | 3.36 sec                                                              | 2.46 sec: 1.37x faster                                                            |
| pickle_pure_python   | 529 us                                                                | 396 us: 1.34x faster                                                              |
| xml_etree_process    | 99.5 ms                                                               | 80.0 ms: 1.24x faster                                                             |
| json_dumps           | 16.7 ms                                                               | 13.5 ms: 1.24x faster                                                             |
| xml_etree_parse      | 212 ms                                                                | 180 ms: 1.18x faster                                                              |
| xml_etree_iterparse  | 156 ms                                                                | 141 ms: 1.11x faster                                                              |
| xml_etree_generate   | 123 ms                                                                | 116 ms: 1.06x faster                                                              |
| json_loads           | 30.9 us                                                               | 32.5 us: 1.05x slower                                                             |
| Geometric mean       | (ref)                                                                 | 1.20x faster                                                                      |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250603-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.59 ms: 1.25x slower                                                             |
| python_startup         | 11.2 ms                                                               | 15.0 ms: 1.34x slower                                                             |
| Geometric mean         | (ref)                                                                 | 1.29x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250603-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.9 ms: 1.36x faster                                                             |
| django_template | 53.3 ms                                                               | 39.8 ms: 1.34x faster                                                             |
| genshi_text     | 35.2 ms                                                               | 27.8 ms: 1.27x faster                                                             |
| genshi_xml      | 69.8 ms                                                               | 61.0 ms: 1.15x faster                                                             |
| Geometric mean  | (ref)                                                                 | 1.28x faster                                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250603-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680 |
|--------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 203 us: 3.26x faster                                                              |
| async_tree_io            | 2.28 sec                                                              | 877 ms: 2.60x faster                                                              |
| async_tree_memoization   | 1.13 sec                                                              | 463 ms: 2.45x faster                                                              |
| async_tree_none          | 950 ms                                                                | 390 ms: 2.44x faster                                                              |
| deltablue                | 8.94 ms                                                               | 3.93 ms: 2.28x faster                                                             |
| mdp                      | 3.70 sec                                                              | 1.65 sec: 2.25x faster                                                            |
| go                       | 264 ms                                                                | 127 ms: 2.09x faster                                                              |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 659 ms: 1.93x faster                                                              |
| generators               | 68.1 ms                                                               | 35.8 ms: 1.90x faster                                                             |
| richards_super           | 107 ms                                                                | 60.0 ms: 1.79x faster                                                             |
| richards                 | 91.7 ms                                                               | 51.7 ms: 1.77x faster                                                             |
| raytrace                 | 573 ms                                                                | 327 ms: 1.75x faster                                                              |
| chaos                    | 121 ms                                                                | 69.2 ms: 1.75x faster                                                             |
| scimark_sor              | 246 ms                                                                | 146 ms: 1.69x faster                                                              |
| scimark_monte_carlo      | 128 ms                                                                | 79.0 ms: 1.62x faster                                                             |
| crypto_pyaes             | 134 ms                                                                | 82.8 ms: 1.62x faster                                                             |
| deepcopy_memo            | 61.7 us                                                               | 38.2 us: 1.61x faster                                                             |
| comprehensions           | 33.1 us                                                               | 20.6 us: 1.60x faster                                                             |
| hexiom                   | 10.9 ms                                                               | 6.84 ms: 1.59x faster                                                             |
| float                    | 135 ms                                                                | 86.0 ms: 1.57x faster                                                             |
| deepcopy                 | 511 us                                                                | 328 us: 1.56x faster                                                              |
| pylint                   | 485 ms                                                                | 313 ms: 1.55x faster                                                              |
| pyflate                  | 795 ms                                                                | 526 ms: 1.51x faster                                                              |
| scimark_lu               | 227 ms                                                                | 151 ms: 1.50x faster                                                              |
| regex_compile            | 177 ms                                                                | 123 ms: 1.44x faster                                                              |
| spectral_norm            | 186 ms                                                                | 132 ms: 1.42x faster                                                              |
| html5lib                 | 86.5 ms                                                               | 61.2 ms: 1.41x faster                                                             |
| unpickle_pure_python     | 366 us                                                                | 263 us: 1.39x faster                                                              |
| tomli_loads              | 3.36 sec                                                              | 2.46 sec: 1.37x faster                                                            |
| pycparser                | 1.69 sec                                                              | 1.24 sec: 1.37x faster                                                            |
| dulwich_log              | 73.5 ms                                                               | 53.9 ms: 1.36x faster                                                             |
| mako                     | 18.9 ms                                                               | 13.9 ms: 1.36x faster                                                             |
| nbody                    | 166 ms                                                                | 123 ms: 1.35x faster                                                              |
| django_template          | 53.3 ms                                                               | 39.8 ms: 1.34x faster                                                             |
| pickle_pure_python       | 529 us                                                                | 396 us: 1.34x faster                                                              |
| sympy_integrate          | 26.5 ms                                                               | 20.3 ms: 1.31x faster                                                             |
| deepcopy_reduce          | 4.60 us                                                               | 3.52 us: 1.30x faster                                                             |
| logging_simple           | 9.78 us                                                               | 7.59 us: 1.29x faster                                                             |
| logging_format           | 10.6 us                                                               | 8.25 us: 1.29x faster                                                             |
| sympy_sum                | 184 ms                                                                | 143 ms: 1.29x faster                                                              |
| genshi_text              | 35.2 ms                                                               | 27.8 ms: 1.27x faster                                                             |
| 2to3                     | 381 ms                                                                | 304 ms: 1.25x faster                                                              |
| coroutines               | 37.2 ms                                                               | 29.7 ms: 1.25x faster                                                             |
| xml_etree_process        | 99.5 ms                                                               | 80.0 ms: 1.24x faster                                                             |
| json_dumps               | 16.7 ms                                                               | 13.5 ms: 1.24x faster                                                             |
| nqueens                  | 117 ms                                                                | 97.2 ms: 1.21x faster                                                             |
| docutils                 | 3.53 sec                                                              | 2.92 sec: 1.21x faster                                                            |
| sympy_str                | 329 ms                                                                | 277 ms: 1.19x faster                                                              |
| pathlib                  | 26.3 ms                                                               | 22.3 ms: 1.18x faster                                                             |
| xml_etree_parse          | 212 ms                                                                | 180 ms: 1.18x faster                                                              |
| pprint_pformat           | 2.36 sec                                                              | 2.01 sec: 1.18x faster                                                            |
| pprint_safe_repr         | 1.15 sec                                                              | 983 ms: 1.17x faster                                                              |
| sympy_expand             | 543 ms                                                                | 467 ms: 1.16x faster                                                              |
| fannkuch                 | 546 ms                                                                | 472 ms: 1.16x faster                                                              |
| regex_v8                 | 32.2 ms                                                               | 27.8 ms: 1.16x faster                                                             |
| scimark_fft              | 500 ms                                                                | 435 ms: 1.15x faster                                                              |
| genshi_xml               | 69.8 ms                                                               | 61.0 ms: 1.15x faster                                                             |
| regex_dna                | 257 ms                                                                | 229 ms: 1.12x faster                                                              |
| meteor_contest           | 126 ms                                                                | 113 ms: 1.12x faster                                                              |
| xml_etree_iterparse      | 156 ms                                                                | 141 ms: 1.11x faster                                                              |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.92 ms: 1.10x faster                                                             |
| regex_effbot             | 4.25 ms                                                               | 3.92 ms: 1.08x faster                                                             |
| sqlite_synth             | 4.12 us                                                               | 3.83 us: 1.08x faster                                                             |
| xml_etree_generate       | 123 ms                                                                | 116 ms: 1.06x faster                                                              |
| asyncio_websockets       | 657 ms                                                                | 667 ms: 1.02x slower                                                              |
| json_loads               | 30.9 us                                                               | 32.5 us: 1.05x slower                                                             |
| telco                    | 8.49 ms                                                               | 9.47 ms: 1.12x slower                                                             |
| python_startup_no_site   | 6.89 ms                                                               | 8.59 ms: 1.25x slower                                                             |
| python_startup           | 11.2 ms                                                               | 15.0 ms: 1.34x slower                                                             |
| gc_traversal             | 4.15 ms                                                               | 6.84 ms: 1.65x slower                                                             |
| create_gc_cycles         | 2.26 ms                                                               | 3.74 ms: 1.66x slower                                                             |
| logging_silent           | 222 ns                                                                | 634 ns: 2.86x slower                                                              |
| coverage                 | 83.6 ms                                                               | 568 ms: 6.80x slower                                                              |
| thrift                   | 1.26 ms                                                               | 191 ms: 151.42x slower                                                            |
| Geometric mean           | (ref)                                                                 | 1.19x faster                                                                      |

Benchmark hidden because not significant (3): json, async_generators, pidigits
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250603-3.15.0a0-06c1680/bm-20250603-arminc-aarch64-faster%2dcpython-specialize_for_iter_-3.15.0a0-06c1680.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.228x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.35x