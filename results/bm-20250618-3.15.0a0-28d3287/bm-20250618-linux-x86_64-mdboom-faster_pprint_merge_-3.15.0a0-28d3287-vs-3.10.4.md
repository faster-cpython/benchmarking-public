# Results vs. 3.10.4

- fork: mdboom
- ref: faster_pprint_merge_
- machine: linux-x86_64
- commit hash: 28d3287
- commit date: 2025-06-18
- overall geometric mean: 1.283x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250618-linux-x86_64-mdboom-faster_pprint_merge_-3.15.0a0-28d3287 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 292 ms: 1.19x faster                                                  |
| docutils       | 3.30 sec                                               | 2.85 sec: 1.16x faster                                                |
| html5lib       | 88.9 ms                                                | 64.8 ms: 1.37x faster                                                 |
| Geometric mean | (ref)                                                  | 1.24x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250618-linux-x86_64-mdboom-faster_pprint_merge_-3.15.0a0-28d3287 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 663 ms: 2.67x faster                                                  |
| async_tree_none         | 728 ms                                                 | 289 ms: 2.52x faster                                                  |
| async_tree_memoization  | 870 ms                                                 | 346 ms: 2.51x faster                                                  |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 602 ms: 1.69x faster                                                  |
| Geometric mean          | (ref)                                                  | 2.31x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250618-linux-x86_64-mdboom-faster_pprint_merge_-3.15.0a0-28d3287 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 117 ms                                                 | 75.5 ms: 1.55x faster                                                 |
| nbody          | 154 ms                                                 | 106 ms: 1.45x faster                                                  |
| pidigits       | 191 ms                                                 | 205 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                  | 1.28x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250618-linux-x86_64-mdboom-faster_pprint_merge_-3.15.0a0-28d3287 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 144 ms: 1.30x faster                                                  |
| regex_effbot   | 3.63 ms                                                | 2.93 ms: 1.24x faster                                                 |
| regex_v8       | 27.8 ms                                                | 23.9 ms: 1.16x faster                                                 |
| regex_dna      | 227 ms                                                 | 196 ms: 1.15x faster                                                  |
| Geometric mean | (ref)                                                  | 1.21x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250618-linux-x86_64-mdboom-faster_pprint_merge_-3.15.0a0-28d3287 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 2.22 sec: 1.41x faster                                                |
| pickle_pure_python   | 484 us                                                 | 374 us: 1.30x faster                                                  |
| unpickle_pure_python | 331 us                                                 | 256 us: 1.29x faster                                                  |
| xml_etree_process    | 79.1 ms                                                | 74.3 ms: 1.07x faster                                                 |
| json_dumps           | 14.2 ms                                                | 13.4 ms: 1.05x faster                                                 |
| xml_etree_parse      | 168 ms                                                 | 162 ms: 1.04x faster                                                  |
| xml_etree_iterparse  | 115 ms                                                 | 112 ms: 1.03x faster                                                  |
| json_loads           | 31.2 us                                                | 33.9 us: 1.09x slower                                                 |
| xml_etree_generate   | 99.4 ms                                                | 108 ms: 1.09x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250618-linux-x86_64-mdboom-faster_pprint_merge_-3.15.0a0-28d3287 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.11x faster                                                 |
| python_startup_no_site | 5.93 ms                                                | 7.39 ms: 1.25x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250618-linux-x86_64-mdboom-faster_pprint_merge_-3.15.0a0-28d3287 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 25.6 ms: 1.24x faster                                                 |
| mako            | 16.3 ms                                                | 13.6 ms: 1.20x faster                                                 |
| django_template | 48.2 ms                                                | 41.0 ms: 1.17x faster                                                 |
| genshi_xml      | 66.0 ms                                                | 57.3 ms: 1.15x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.19x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250618-linux-x86_64-mdboom-faster_pprint_merge_-3.15.0a0-28d3287 |
|--------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 198 us: 2.74x faster                                                  |
| async_tree_io            | 1.77 sec                                               | 663 ms: 2.67x faster                                                  |
| async_tree_none          | 728 ms                                                 | 289 ms: 2.52x faster                                                  |
| async_tree_memoization   | 870 ms                                                 | 346 ms: 2.51x faster                                                  |
| generators               | 80.1 ms                                                | 33.0 ms: 2.43x faster                                                 |
| deltablue                | 7.91 ms                                                | 3.85 ms: 2.06x faster                                                 |
| go                       | 240 ms                                                 | 119 ms: 2.02x faster                                                  |
| mdp                      | 2.85 sec                                               | 1.47 sec: 1.94x faster                                                |
| pylint                   | 551 ms                                                 | 311 ms: 1.77x faster                                                  |
| deepcopy_memo            | 58.5 us                                                | 34.0 us: 1.72x faster                                                 |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 602 ms: 1.69x faster                                                  |
| chaos                    | 115 ms                                                 | 68.7 ms: 1.68x faster                                                 |
| scimark_sor              | 220 ms                                                 | 134 ms: 1.64x faster                                                  |
| djangocms                | 38.4 us                                                | 24.3 us: 1.58x faster                                                 |
| raytrace                 | 507 ms                                                 | 321 ms: 1.58x faster                                                  |
| hexiom                   | 10.4 ms                                                | 6.64 ms: 1.57x faster                                                 |
| float                    | 117 ms                                                 | 75.5 ms: 1.55x faster                                                 |
| pyflate                  | 716 ms                                                 | 464 ms: 1.54x faster                                                  |
| scimark_monte_carlo      | 118 ms                                                 | 76.8 ms: 1.54x faster                                                 |
| richards_super           | 94.7 ms                                                | 61.8 ms: 1.53x faster                                                 |
| deepcopy                 | 479 us                                                 | 316 us: 1.52x faster                                                  |
| spectral_norm            | 170 ms                                                 | 113 ms: 1.51x faster                                                  |
| crypto_pyaes             | 128 ms                                                 | 85.6 ms: 1.49x faster                                                 |
| comprehensions           | 28.8 us                                                | 19.3 us: 1.49x faster                                                 |
| richards                 | 79.3 ms                                                | 54.8 ms: 1.45x faster                                                 |
| nbody                    | 154 ms                                                 | 106 ms: 1.45x faster                                                  |
| tomli_loads              | 3.14 sec                                               | 2.22 sec: 1.41x faster                                                |
| html5lib                 | 88.9 ms                                                | 64.8 ms: 1.37x faster                                                 |
| dulwich_log              | 84.3 ms                                                | 63.6 ms: 1.33x faster                                                 |
| scimark_lu               | 176 ms                                                 | 133 ms: 1.32x faster                                                  |
| coroutines               | 35.1 ms                                                | 26.8 ms: 1.31x faster                                                 |
| regex_compile            | 188 ms                                                 | 144 ms: 1.30x faster                                                  |
| pickle_pure_python       | 484 us                                                 | 374 us: 1.30x faster                                                  |
| unpickle_pure_python     | 331 us                                                 | 256 us: 1.29x faster                                                  |
| pycparser                | 1.58 sec                                               | 1.26 sec: 1.25x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 3.34 us: 1.25x faster                                                 |
| genshi_text              | 31.8 ms                                                | 25.6 ms: 1.24x faster                                                 |
| regex_effbot             | 3.63 ms                                                | 2.93 ms: 1.24x faster                                                 |
| sympy_integrate          | 25.8 ms                                                | 20.9 ms: 1.23x faster                                                 |
| mako                     | 16.3 ms                                                | 13.6 ms: 1.20x faster                                                 |
| 2to3                     | 348 ms                                                 | 292 ms: 1.19x faster                                                  |
| sympy_sum                | 196 ms                                                 | 166 ms: 1.18x faster                                                  |
| django_template          | 48.2 ms                                                | 41.0 ms: 1.17x faster                                                 |
| regex_v8                 | 27.8 ms                                                | 23.9 ms: 1.16x faster                                                 |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.59 ms: 1.16x faster                                                 |
| docutils                 | 3.30 sec                                               | 2.85 sec: 1.16x faster                                                |
| scimark_fft              | 466 ms                                                 | 404 ms: 1.15x faster                                                  |
| regex_dna                | 227 ms                                                 | 196 ms: 1.15x faster                                                  |
| genshi_xml               | 66.0 ms                                                | 57.3 ms: 1.15x faster                                                 |
| thrift                   | 1.07 ms                                                | 954 us: 1.12x faster                                                  |
| sympy_str                | 346 ms                                                 | 308 ms: 1.12x faster                                                  |
| fannkuch                 | 532 ms                                                 | 478 ms: 1.11x faster                                                  |
| logging_simple           | 8.30 us                                                | 7.47 us: 1.11x faster                                                 |
| pathlib                  | 20.5 ms                                                | 18.4 ms: 1.11x faster                                                 |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.11x faster                                                 |
| logging_format           | 9.09 us                                                | 8.41 us: 1.08x faster                                                 |
| async_generators         | 444 ms                                                 | 412 ms: 1.08x faster                                                  |
| nqueens                  | 106 ms                                                 | 98.9 ms: 1.07x faster                                                 |
| xml_etree_process        | 79.1 ms                                                | 74.3 ms: 1.07x faster                                                 |
| sympy_expand             | 566 ms                                                 | 535 ms: 1.06x faster                                                  |
| json_dumps               | 14.2 ms                                                | 13.4 ms: 1.05x faster                                                 |
| pprint_pformat           | 2.10 sec                                               | 2.00 sec: 1.05x faster                                                |
| xml_etree_parse          | 168 ms                                                 | 162 ms: 1.04x faster                                                  |
| pprint_safe_repr         | 1.02 sec                                               | 987 ms: 1.03x faster                                                  |
| xml_etree_iterparse      | 115 ms                                                 | 112 ms: 1.03x faster                                                  |
| meteor_contest           | 120 ms                                                 | 116 ms: 1.03x faster                                                  |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                                  |
| sqlite_synth             | 3.02 us                                                | 3.20 us: 1.06x slower                                                 |
| pidigits                 | 191 ms                                                 | 205 ms: 1.07x slower                                                  |
| json                     | 5.69 ms                                                | 6.12 ms: 1.08x slower                                                 |
| json_loads               | 31.2 us                                                | 33.9 us: 1.09x slower                                                 |
| xml_etree_generate       | 99.4 ms                                                | 108 ms: 1.09x slower                                                  |
| python_startup_no_site   | 5.93 ms                                                | 7.39 ms: 1.25x slower                                                 |
| coverage                 | 79.4 ms                                                | 102 ms: 1.28x slower                                                  |
| telco                    | 7.27 ms                                                | 9.42 ms: 1.30x slower                                                 |
| gc_traversal             | 3.62 ms                                                | 5.14 ms: 1.42x slower                                                 |
| create_gc_cycles         | 1.62 ms                                                | 2.64 ms: 1.63x slower                                                 |
| logging_silent           | 190 ns                                                 | 626 ns: 3.30x slower                                                  |
| Geometric mean           | (ref)                                                  | 1.26x faster                                                          |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250618-3.15.0a0-28d3287/bm-20250618-linux-x86_64-mdboom-faster_pprint_merge_-3.15.0a0-28d3287.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.283x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: 1.31x