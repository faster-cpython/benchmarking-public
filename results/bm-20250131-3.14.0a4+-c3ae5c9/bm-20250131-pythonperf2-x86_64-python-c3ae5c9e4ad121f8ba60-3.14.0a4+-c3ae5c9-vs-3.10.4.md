# Results vs. 3.10.4

- fork: python
- ref: c3ae5c9e4ad121f8ba60
- machine: linux-x86_64
- commit hash: c3ae5c9
- commit date: 2025-01-31
- overall geometric mean: 1.365x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250131-pythonperf2-x86_64-python-c3ae5c9e4ad121f8ba60-3.14.0a4+-c3ae5c9 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 279 ms: 1.26x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.85 sec: 1.20x faster                                                       |
| html5lib       | 94.6 ms                                                      | 66.3 ms: 1.43x faster                                                        |
| Geometric mean | (ref)                                                        | 1.29x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250131-pythonperf2-x86_64-python-c3ae5c9e4ad121f8ba60-3.14.0a4+-c3ae5c9 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 651 ms: 2.45x faster                                                         |
| async_tree_none         | 692 ms                                                       | 286 ms: 2.41x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 349 ms: 2.35x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 517 ms: 1.81x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.24x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250131-pythonperf2-x86_64-python-c3ae5c9e4ad121f8ba60-3.14.0a4+-c3ae5c9 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 69.7 ms: 1.59x faster                                                        |
| nbody          | 134 ms                                                       | 87.2 ms: 1.54x faster                                                        |
| pidigits       | 271 ms                                                       | 254 ms: 1.06x faster                                                         |
| Geometric mean | (ref)                                                        | 1.38x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250131-pythonperf2-x86_64-python-c3ae5c9e4ad121f8ba60-3.14.0a4+-c3ae5c9 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 134 ms: 1.42x faster                                                         |
| regex_dna      | 261 ms                                                       | 238 ms: 1.10x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 26.0 ms: 1.04x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.20 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                        | 1.12x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250131-pythonperf2-x86_64-python-c3ae5c9e4ad121f8ba60-3.14.0a4+-c3ae5c9 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 205 us: 1.52x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 1.99 sec: 1.47x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 327 us: 1.39x faster                                                         |
| xml_etree_process    | 75.9 ms                                                      | 57.9 ms: 1.31x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 11.6 ms: 1.26x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 136 ms: 1.17x faster                                                         |
| json_loads           | 30.3 us                                                      | 26.4 us: 1.15x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 97.2 ms: 1.14x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 82.9 ms: 1.11x faster                                                        |
| Geometric mean       | (ref)                                                        | 1.27x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250131-pythonperf2-x86_64-python-c3ae5c9e4ad121f8ba60-3.14.0a4+-c3ae5c9 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.00 ms: 1.23x slower                                                        |
| python_startup         | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250131-pythonperf2-x86_64-python-c3ae5c9e4ad121f8ba60-3.14.0a4+-c3ae5c9 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 34.9 ms: 1.44x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 22.6 ms: 1.39x faster                                                        |
| mako            | 14.7 ms                                                      | 10.7 ms: 1.37x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 53.0 ms: 1.19x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.35x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250131-pythonperf2-x86_64-python-c3ae5c9e4ad121f8ba60-3.14.0a4+-c3ae5c9 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 167 us: 3.21x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 651 ms: 2.45x faster                                                         |
| async_tree_none          | 692 ms                                                       | 286 ms: 2.41x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 349 ms: 2.35x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.27 ms: 2.29x faster                                                        |
| go                       | 262 ms                                                       | 124 ms: 2.12x faster                                                         |
| generators               | 57.3 ms                                                      | 29.0 ms: 1.97x faster                                                        |
| chaos                    | 109 ms                                                       | 59.0 ms: 1.84x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 517 ms: 1.81x faster                                                         |
| pylint                   | 566 ms                                                       | 313 ms: 1.81x faster                                                         |
| raytrace                 | 489 ms                                                       | 271 ms: 1.81x faster                                                         |
| scimark_lu               | 167 ms                                                       | 94.6 ms: 1.76x faster                                                        |
| richards_super           | 90.6 ms                                                      | 51.5 ms: 1.76x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 62.0 ms: 1.73x faster                                                        |
| logging_silent           | 167 ns                                                       | 96.8 ns: 1.73x faster                                                        |
| pyflate                  | 733 ms                                                       | 429 ms: 1.71x faster                                                         |
| sqlglot_parse            | 2.24 ms                                                      | 1.32 ms: 1.69x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 29.7 us: 1.68x faster                                                        |
| scimark_sor              | 180 ms                                                       | 108 ms: 1.67x faster                                                         |
| deepcopy                 | 468 us                                                       | 281 us: 1.66x faster                                                         |
| richards                 | 75.1 ms                                                      | 45.5 ms: 1.65x faster                                                        |
| spectral_norm            | 139 ms                                                       | 84.5 ms: 1.65x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 73.6 ms: 1.62x faster                                                        |
| comprehensions           | 26.7 us                                                      | 16.6 us: 1.61x faster                                                        |
| float                    | 111 ms                                                       | 69.7 ms: 1.59x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 5.97 ms: 1.58x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.71 ms: 1.57x faster                                                        |
| nbody                    | 134 ms                                                       | 87.2 ms: 1.54x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 205 us: 1.52x faster                                                         |
| tomli_loads              | 2.92 sec                                                     | 1.99 sec: 1.47x faster                                                       |
| coroutines               | 30.3 ms                                                      | 20.8 ms: 1.46x faster                                                        |
| django_template          | 50.2 ms                                                      | 34.9 ms: 1.44x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 66.3 ms: 1.43x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.23 us: 1.43x faster                                                        |
| regex_compile            | 190 ms                                                       | 134 ms: 1.42x faster                                                         |
| logging_format           | 9.64 us                                                      | 6.84 us: 1.41x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 22.6 ms: 1.39x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 327 us: 1.39x faster                                                         |
| deepcopy_reduce          | 4.01 us                                                      | 2.90 us: 1.38x faster                                                        |
| mako                     | 14.7 ms                                                      | 10.7 ms: 1.37x faster                                                        |
| thrift                   | 1.18 ms                                                      | 860 us: 1.37x faster                                                         |
| pathlib                  | 21.4 ms                                                      | 15.6 ms: 1.37x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.24 sec: 1.35x faster                                                       |
| sqlalchemy_declarative   | 190 ms                                                       | 141 ms: 1.35x faster                                                         |
| pprint_pformat           | 2.15 sec                                                     | 1.60 sec: 1.34x faster                                                       |
| nqueens                  | 115 ms                                                       | 85.7 ms: 1.34x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 783 ms: 1.34x faster                                                         |
| fannkuch                 | 483 ms                                                       | 365 ms: 1.32x faster                                                         |
| xml_etree_process        | 75.9 ms                                                      | 57.9 ms: 1.31x faster                                                        |
| sympy_sum                | 193 ms                                                       | 149 ms: 1.29x faster                                                         |
| sqlalchemy_imperative    | 22.7 ms                                                      | 17.7 ms: 1.28x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 113 ms: 1.27x faster                                                         |
| sympy_str                | 360 ms                                                       | 286 ms: 1.26x faster                                                         |
| json_dumps               | 14.5 ms                                                      | 11.6 ms: 1.26x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 907 us: 1.26x faster                                                         |
| 2to3                     | 350 ms                                                       | 279 ms: 1.26x faster                                                         |
| sqlglot_optimize         | 70.1 ms                                                      | 56.2 ms: 1.25x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 22.8 ms: 1.23x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.44 sec: 1.23x faster                                                       |
| sympy_expand             | 600 ms                                                       | 489 ms: 1.23x faster                                                         |
| dulwich_log              | 81.1 ms                                                      | 66.3 ms: 1.22x faster                                                        |
| scimark_fft              | 361 ms                                                       | 302 ms: 1.20x faster                                                         |
| docutils                 | 3.41 sec                                                     | 2.85 sec: 1.20x faster                                                       |
| genshi_xml               | 63.3 ms                                                      | 53.0 ms: 1.19x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 136 ms: 1.17x faster                                                         |
| json_loads               | 30.3 us                                                      | 26.4 us: 1.15x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 97.2 ms: 1.14x faster                                                        |
| meteor_contest           | 138 ms                                                       | 124 ms: 1.12x faster                                                         |
| xml_etree_generate       | 92.3 ms                                                      | 82.9 ms: 1.11x faster                                                        |
| regex_dna                | 261 ms                                                       | 238 ms: 1.10x faster                                                         |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.65 ms: 1.09x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.81 us: 1.07x faster                                                        |
| pidigits                 | 271 ms                                                       | 254 ms: 1.06x faster                                                         |
| json                     | 5.86 ms                                                      | 5.53 ms: 1.06x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 26.0 ms: 1.04x faster                                                        |
| async_generators         | 421 ms                                                       | 404 ms: 1.04x faster                                                         |
| regex_effbot             | 3.09 ms                                                      | 3.20 ms: 1.04x slower                                                        |
| telco                    | 7.23 ms                                                      | 7.86 ms: 1.09x slower                                                        |
| coverage                 | 63.3 ms                                                      | 76.7 ms: 1.21x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 9.00 ms: 1.23x slower                                                        |
| python_startup           | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.82 ms: 1.60x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 6.55 ms: 1.92x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 993 ms: 155.78x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.28x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250131-3.14.0a4+-c3ae5c9/bm-20250131-pythonperf2-x86_64-python-c3ae5c9e4ad121f8ba60-3.14.0a4+-c3ae5c9.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.365x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.27x