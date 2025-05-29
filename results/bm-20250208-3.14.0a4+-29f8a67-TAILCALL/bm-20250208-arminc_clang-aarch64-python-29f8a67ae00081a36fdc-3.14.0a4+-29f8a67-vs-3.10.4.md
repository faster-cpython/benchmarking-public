# Results vs. 3.10.4

- fork: python
- ref: 29f8a67ae00081a36fdc
- machine: linux-aarch64
- commit hash: 29f8a67
- commit date: 2025-02-08
- overall geometric mean: 1.364x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.35x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 294 ms: 1.29x faster                                                     |
| docutils       | 3.53 sec                                                              | 2.99 sec: 1.18x faster                                                   |
| html5lib       | 86.5 ms                                                               | 59.3 ms: 1.46x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.31x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 908 ms: 2.52x faster                                                     |
| async_tree_none         | 950 ms                                                                | 387 ms: 2.45x faster                                                     |
| async_tree_memoization  | 1.13 sec                                                              | 480 ms: 2.36x faster                                                     |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 758 ms: 1.68x faster                                                     |
| Geometric mean          | (ref)                                                                 | 2.22x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 135 ms                                                                | 82.9 ms: 1.63x faster                                                    |
| nbody          | 166 ms                                                                | 114 ms: 1.45x faster                                                     |
| pidigits       | 235 ms                                                                | 303 ms: 1.29x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.22x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 120 ms: 1.47x faster                                                     |
| regex_dna      | 257 ms                                                                | 250 ms: 1.03x faster                                                     |
| regex_v8       | 32.2 ms                                                               | 34.5 ms: 1.07x slower                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.62 ms: 1.09x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 252 us: 1.45x faster                                                     |
| pickle_pure_python   | 529 us                                                                | 379 us: 1.40x faster                                                     |
| tomli_loads          | 3.36 sec                                                              | 2.46 sec: 1.37x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 74.6 ms: 1.33x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 103 ms: 1.20x faster                                                     |
| json_dumps           | 16.7 ms                                                               | 14.8 ms: 1.13x faster                                                    |
| json_loads           | 30.9 us                                                               | 36.5 us: 1.18x slower                                                    |
| Geometric mean       | (ref)                                                                 | 1.18x faster                                                             |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 9.30 ms: 1.35x slower                                                    |
| python_startup         | 11.2 ms                                                               | 16.5 ms: 1.47x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.41x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 35.2 ms                                                               | 25.7 ms: 1.37x faster                                                    |
| mako            | 18.9 ms                                                               | 13.9 ms: 1.36x faster                                                    |
| django_template | 53.3 ms                                                               | 39.2 ms: 1.36x faster                                                    |
| genshi_xml      | 69.8 ms                                                               | 58.8 ms: 1.19x faster                                                    |
| Geometric mean  | (ref)                                                                 | 1.32x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 181 us: 3.64x faster                                                     |
| async_tree_io            | 2.28 sec                                                              | 908 ms: 2.52x faster                                                     |
| async_tree_none          | 950 ms                                                                | 387 ms: 2.45x faster                                                     |
| async_tree_memoization   | 1.13 sec                                                              | 480 ms: 2.36x faster                                                     |
| deltablue                | 8.94 ms                                                               | 3.86 ms: 2.31x faster                                                    |
| go                       | 264 ms                                                                | 133 ms: 1.98x faster                                                     |
| richards_super           | 107 ms                                                                | 55.7 ms: 1.93x faster                                                    |
| logging_silent           | 222 ns                                                                | 118 ns: 1.89x faster                                                     |
| richards                 | 91.7 ms                                                               | 49.6 ms: 1.85x faster                                                    |
| generators               | 68.1 ms                                                               | 37.0 ms: 1.84x faster                                                    |
| raytrace                 | 573 ms                                                                | 312 ms: 1.84x faster                                                     |
| chaos                    | 121 ms                                                                | 67.9 ms: 1.78x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.35 ms: 1.78x faster                                                    |
| deepcopy_memo            | 61.7 us                                                               | 35.4 us: 1.74x faster                                                    |
| spectral_norm            | 186 ms                                                                | 109 ms: 1.71x faster                                                     |
| comprehensions           | 33.1 us                                                               | 19.4 us: 1.71x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.69 ms: 1.68x faster                                                    |
| scimark_sor              | 246 ms                                                                | 147 ms: 1.68x faster                                                     |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 758 ms: 1.68x faster                                                     |
| scimark_monte_carlo      | 128 ms                                                                | 77.1 ms: 1.66x faster                                                    |
| scimark_lu               | 227 ms                                                                | 139 ms: 1.63x faster                                                     |
| float                    | 135 ms                                                                | 82.9 ms: 1.63x faster                                                    |
| deepcopy                 | 511 us                                                                | 316 us: 1.62x faster                                                     |
| pylint                   | 485 ms                                                                | 306 ms: 1.59x faster                                                     |
| hexiom                   | 10.9 ms                                                               | 7.21 ms: 1.51x faster                                                    |
| crypto_pyaes             | 134 ms                                                                | 88.9 ms: 1.51x faster                                                    |
| pyflate                  | 795 ms                                                                | 532 ms: 1.49x faster                                                     |
| regex_compile            | 177 ms                                                                | 120 ms: 1.47x faster                                                     |
| html5lib                 | 86.5 ms                                                               | 59.3 ms: 1.46x faster                                                    |
| nbody                    | 166 ms                                                                | 114 ms: 1.45x faster                                                     |
| unpickle_pure_python     | 366 us                                                                | 252 us: 1.45x faster                                                     |
| logging_format           | 10.6 us                                                               | 7.37 us: 1.44x faster                                                    |
| logging_simple           | 9.78 us                                                               | 6.81 us: 1.44x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 379 us: 1.40x faster                                                     |
| genshi_text              | 35.2 ms                                                               | 25.7 ms: 1.37x faster                                                    |
| tomli_loads              | 3.36 sec                                                              | 2.46 sec: 1.37x faster                                                   |
| mako                     | 18.9 ms                                                               | 13.9 ms: 1.36x faster                                                    |
| django_template          | 53.3 ms                                                               | 39.2 ms: 1.36x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.39 us: 1.36x faster                                                    |
| sqlalchemy_imperative    | 20.5 ms                                                               | 15.3 ms: 1.35x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.26 sec: 1.34x faster                                                   |
| scimark_fft              | 500 ms                                                                | 375 ms: 1.34x faster                                                     |
| xml_etree_process        | 99.5 ms                                                               | 74.6 ms: 1.33x faster                                                    |
| sqlalchemy_declarative   | 197 ms                                                                | 148 ms: 1.33x faster                                                     |
| sympy_sum                | 184 ms                                                                | 138 ms: 1.33x faster                                                     |
| thrift                   | 1.26 ms                                                               | 955 us: 1.32x faster                                                     |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 5.83 ms: 1.31x faster                                                    |
| 2to3                     | 381 ms                                                                | 294 ms: 1.29x faster                                                     |
| coroutines               | 37.2 ms                                                               | 28.8 ms: 1.29x faster                                                    |
| sympy_integrate          | 26.5 ms                                                               | 20.9 ms: 1.27x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.26 ms: 1.26x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 58.5 ms: 1.26x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 60.1 ms: 1.25x faster                                                    |
| sqlglot_normalize        | 156 ms                                                                | 125 ms: 1.25x faster                                                     |
| pprint_pformat           | 2.36 sec                                                              | 1.89 sec: 1.25x faster                                                   |
| pathlib                  | 26.3 ms                                                               | 21.2 ms: 1.24x faster                                                    |
| sympy_str                | 329 ms                                                                | 268 ms: 1.23x faster                                                     |
| pprint_safe_repr         | 1.15 sec                                                              | 939 ms: 1.22x faster                                                     |
| xml_etree_generate       | 123 ms                                                                | 103 ms: 1.20x faster                                                     |
| nqueens                  | 117 ms                                                                | 98.3 ms: 1.19x faster                                                    |
| sympy_expand             | 543 ms                                                                | 456 ms: 1.19x faster                                                     |
| genshi_xml               | 69.8 ms                                                               | 58.8 ms: 1.19x faster                                                    |
| docutils                 | 3.53 sec                                                              | 2.99 sec: 1.18x faster                                                   |
| mdp                      | 3.70 sec                                                              | 3.23 sec: 1.15x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 14.8 ms: 1.13x faster                                                    |
| fannkuch                 | 546 ms                                                                | 494 ms: 1.11x faster                                                     |
| meteor_contest           | 126 ms                                                                | 116 ms: 1.09x faster                                                     |
| async_generators         | 452 ms                                                                | 419 ms: 1.08x faster                                                     |
| regex_dna                | 257 ms                                                                | 250 ms: 1.03x faster                                                     |
| asyncio_websockets       | 657 ms                                                                | 676 ms: 1.03x slower                                                     |
| regex_v8                 | 32.2 ms                                                               | 34.5 ms: 1.07x slower                                                    |
| regex_effbot             | 4.25 ms                                                               | 4.62 ms: 1.09x slower                                                    |
| telco                    | 8.49 ms                                                               | 9.57 ms: 1.13x slower                                                    |
| coverage                 | 83.6 ms                                                               | 94.4 ms: 1.13x slower                                                    |
| json_loads               | 30.9 us                                                               | 36.5 us: 1.18x slower                                                    |
| pidigits                 | 235 ms                                                                | 303 ms: 1.29x slower                                                     |
| python_startup_no_site   | 6.89 ms                                                               | 9.30 ms: 1.35x slower                                                    |
| python_startup           | 11.2 ms                                                               | 16.5 ms: 1.47x slower                                                    |
| create_gc_cycles         | 2.26 ms                                                               | 3.70 ms: 1.64x slower                                                    |
| gc_traversal             | 4.15 ms                                                               | 6.82 ms: 1.64x slower                                                    |
| bench_mp_pool            | 14.5 ms                                                               | 7.51 sec: 516.48x slower                                                 |
| Geometric mean           | (ref)                                                                 | 1.24x faster                                                             |

Benchmark hidden because not significant (4): xml_etree_iterparse, xml_etree_parse, sqlite_synth, json
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250208-3.14.0a4+-29f8a67-CLANG/bm-20250208-arminc-aarch64-python-29f8a67ae00081a36fdc-3.14.0a4+-29f8a67.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.364x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.31x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.35x