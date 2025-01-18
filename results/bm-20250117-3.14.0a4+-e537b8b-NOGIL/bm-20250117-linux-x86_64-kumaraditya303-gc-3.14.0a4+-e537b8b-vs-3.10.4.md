# Results vs. 3.10.4

- fork: kumaraditya303
- ref: gc
- machine: linux-x86_64
- commit hash: e537b8b
- commit date: 2025-01-17
- overall geometric mean: 1.241x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: 1.51x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 309 ms: 1.13x faster                                         |
| docutils       | 3.30 sec                                               | 2.83 sec: 1.16x faster                                       |
| html5lib       | 88.9 ms                                                | 69.5 ms: 1.28x faster                                        |
| Geometric mean | (ref)                                                  | 1.19x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 597 ms: 2.96x faster                                         |
| async_tree_none         | 728 ms                                                 | 290 ms: 2.51x faster                                         |
| async_tree_memoization  | 870 ms                                                 | 367 ms: 2.37x faster                                         |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 522 ms: 1.95x faster                                         |
| Geometric mean          | (ref)                                                  | 2.42x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| float          | 117 ms                                                 | 78.2 ms: 1.50x faster                                        |
| nbody          | 154 ms                                                 | 141 ms: 1.09x faster                                         |
| pidigits       | 191 ms                                                 | 190 ms: 1.01x faster                                         |
| Geometric mean | (ref)                                                  | 1.18x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 149 ms: 1.27x faster                                         |
| regex_v8       | 27.8 ms                                                | 24.8 ms: 1.12x faster                                        |
| regex_effbot   | 3.63 ms                                                | 3.36 ms: 1.08x faster                                        |
| regex_dna      | 227 ms                                                 | 222 ms: 1.02x faster                                         |
| Geometric mean | (ref)                                                  | 1.12x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 484 us                                                 | 368 us: 1.32x faster                                         |
| tomli_loads          | 3.14 sec                                               | 2.41 sec: 1.30x faster                                       |
| unpickle_pure_python | 331 us                                                 | 256 us: 1.29x faster                                         |
| xml_etree_iterparse  | 115 ms                                                 | 96.2 ms: 1.20x faster                                        |
| xml_etree_process    | 79.1 ms                                                | 68.0 ms: 1.16x faster                                        |
| xml_etree_parse      | 168 ms                                                 | 149 ms: 1.13x faster                                         |
| json_dumps           | 14.2 ms                                                | 12.7 ms: 1.11x faster                                        |
| xml_etree_generate   | 99.4 ms                                                | 96.1 ms: 1.03x faster                                        |
| json_loads           | 31.2 us                                                | 31.8 us: 1.02x slower                                        |
| Geometric mean       | (ref)                                                  | 1.16x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 15.0 ms: 1.03x slower                                        |
| python_startup_no_site | 5.93 ms                                                | 9.35 ms: 1.58x slower                                        |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 41.7 ms: 1.15x faster                                        |
| genshi_text     | 31.8 ms                                                | 28.4 ms: 1.12x faster                                        |
| genshi_xml      | 66.0 ms                                                | 60.1 ms: 1.10x faster                                        |
| mako            | 16.3 ms                                                | 16.2 ms: 1.01x faster                                        |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b |
|--------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_io            | 1.77 sec                                               | 597 ms: 2.96x faster                                         |
| typing_runtime_protocols | 544 us                                                 | 211 us: 2.58x faster                                         |
| generators               | 80.1 ms                                                | 31.1 ms: 2.58x faster                                        |
| async_tree_none          | 728 ms                                                 | 290 ms: 2.51x faster                                         |
| async_tree_memoization   | 870 ms                                                 | 367 ms: 2.37x faster                                         |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 522 ms: 1.95x faster                                         |
| pylint                   | 551 ms                                                 | 316 ms: 1.75x faster                                         |
| go                       | 240 ms                                                 | 141 ms: 1.71x faster                                         |
| deltablue                | 7.91 ms                                                | 4.72 ms: 1.67x faster                                        |
| logging_silent           | 190 ns                                                 | 120 ns: 1.58x faster                                         |
| scimark_sor              | 220 ms                                                 | 139 ms: 1.58x faster                                         |
| chaos                    | 115 ms                                                 | 74.5 ms: 1.55x faster                                        |
| deepcopy                 | 479 us                                                 | 311 us: 1.54x faster                                         |
| float                    | 117 ms                                                 | 78.2 ms: 1.50x faster                                        |
| richards_super           | 94.7 ms                                                | 64.3 ms: 1.47x faster                                        |
| deepcopy_memo            | 58.5 us                                                | 39.7 us: 1.47x faster                                        |
| richards                 | 79.3 ms                                                | 54.0 ms: 1.47x faster                                        |
| spectral_norm            | 170 ms                                                 | 119 ms: 1.43x faster                                         |
| raytrace                 | 507 ms                                                 | 356 ms: 1.42x faster                                         |
| crypto_pyaes             | 128 ms                                                 | 90.4 ms: 1.41x faster                                        |
| comprehensions           | 28.8 us                                                | 20.8 us: 1.38x faster                                        |
| coroutines               | 35.1 ms                                                | 25.5 ms: 1.38x faster                                        |
| sqlglot_parse            | 2.17 ms                                                | 1.59 ms: 1.37x faster                                        |
| scimark_monte_carlo      | 118 ms                                                 | 87.2 ms: 1.35x faster                                        |
| pyflate                  | 716 ms                                                 | 532 ms: 1.35x faster                                         |
| hexiom                   | 10.4 ms                                                | 7.76 ms: 1.34x faster                                        |
| sqlglot_transpile        | 2.57 ms                                                | 1.93 ms: 1.34x faster                                        |
| pycparser                | 1.58 sec                                               | 1.18 sec: 1.33x faster                                       |
| pickle_pure_python       | 484 us                                                 | 368 us: 1.32x faster                                         |
| tomli_loads              | 3.14 sec                                               | 2.41 sec: 1.30x faster                                       |
| unpickle_pure_python     | 331 us                                                 | 256 us: 1.29x faster                                         |
| deepcopy_reduce          | 4.17 us                                                | 3.26 us: 1.28x faster                                        |
| html5lib                 | 88.9 ms                                                | 69.5 ms: 1.28x faster                                        |
| regex_compile            | 188 ms                                                 | 149 ms: 1.27x faster                                         |
| pathlib                  | 20.5 ms                                                | 16.4 ms: 1.25x faster                                        |
| scimark_lu               | 176 ms                                                 | 142 ms: 1.24x faster                                         |
| logging_simple           | 8.30 us                                                | 6.73 us: 1.23x faster                                        |
| dulwich_log              | 84.3 ms                                                | 68.7 ms: 1.23x faster                                        |
| xml_etree_iterparse      | 115 ms                                                 | 96.2 ms: 1.20x faster                                        |
| pprint_pformat           | 2.10 sec                                               | 1.75 sec: 1.20x faster                                       |
| logging_format           | 9.09 us                                                | 7.58 us: 1.20x faster                                        |
| pprint_safe_repr         | 1.02 sec                                               | 852 ms: 1.19x faster                                         |
| sqlglot_normalize        | 143 ms                                                 | 120 ms: 1.19x faster                                         |
| docutils                 | 3.30 sec                                               | 2.83 sec: 1.16x faster                                       |
| xml_etree_process        | 79.1 ms                                                | 68.0 ms: 1.16x faster                                        |
| django_template          | 48.2 ms                                                | 41.7 ms: 1.15x faster                                        |
| sqlglot_optimize         | 69.2 ms                                                | 61.1 ms: 1.13x faster                                        |
| sqlalchemy_imperative    | 23.3 ms                                                | 20.6 ms: 1.13x faster                                        |
| thrift                   | 1.07 ms                                                | 948 us: 1.13x faster                                         |
| xml_etree_parse          | 168 ms                                                 | 149 ms: 1.13x faster                                         |
| 2to3                     | 348 ms                                                 | 309 ms: 1.13x faster                                         |
| genshi_text              | 31.8 ms                                                | 28.4 ms: 1.12x faster                                        |
| regex_v8                 | 27.8 ms                                                | 24.8 ms: 1.12x faster                                        |
| json_dumps               | 14.2 ms                                                | 12.7 ms: 1.11x faster                                        |
| sympy_sum                | 196 ms                                                 | 177 ms: 1.11x faster                                         |
| sqlite_synth             | 3.02 us                                                | 2.73 us: 1.11x faster                                        |
| genshi_xml               | 66.0 ms                                                | 60.1 ms: 1.10x faster                                        |
| scimark_fft              | 466 ms                                                 | 426 ms: 1.09x faster                                         |
| sympy_integrate          | 25.8 ms                                                | 23.7 ms: 1.09x faster                                        |
| nbody                    | 154 ms                                                 | 141 ms: 1.09x faster                                         |
| sympy_str                | 346 ms                                                 | 319 ms: 1.09x faster                                         |
| regex_effbot             | 3.63 ms                                                | 3.36 ms: 1.08x faster                                        |
| sympy_expand             | 566 ms                                                 | 527 ms: 1.07x faster                                         |
| sqlalchemy_declarative   | 172 ms                                                 | 162 ms: 1.06x faster                                         |
| nqueens                  | 106 ms                                                 | 100 ms: 1.06x faster                                         |
| mdp                      | 2.85 sec                                               | 2.74 sec: 1.04x faster                                       |
| xml_etree_generate       | 99.4 ms                                                | 96.1 ms: 1.03x faster                                        |
| fannkuch                 | 532 ms                                                 | 516 ms: 1.03x faster                                         |
| regex_dna                | 227 ms                                                 | 222 ms: 1.02x faster                                         |
| json                     | 5.69 ms                                                | 5.60 ms: 1.02x faster                                        |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                         |
| mako                     | 16.3 ms                                                | 16.2 ms: 1.01x faster                                        |
| pidigits                 | 191 ms                                                 | 190 ms: 1.01x faster                                         |
| async_generators         | 444 ms                                                 | 445 ms: 1.00x slower                                         |
| json_loads               | 31.2 us                                                | 31.8 us: 1.02x slower                                        |
| python_startup           | 14.6 ms                                                | 15.0 ms: 1.03x slower                                        |
| create_gc_cycles         | 1.62 ms                                                | 1.71 ms: 1.06x slower                                        |
| meteor_contest           | 120 ms                                                 | 133 ms: 1.11x slower                                         |
| telco                    | 7.27 ms                                                | 9.09 ms: 1.25x slower                                        |
| gc_traversal             | 3.62 ms                                                | 4.56 ms: 1.26x slower                                        |
| coverage                 | 79.4 ms                                                | 108 ms: 1.36x slower                                         |
| python_startup_no_site   | 5.93 ms                                                | 9.35 ms: 1.58x slower                                        |
| bench_thread_pool        | 986 us                                                 | 3.49 ms: 3.54x slower                                        |
| bench_mp_pool            | 24.0 ms                                                | 89.3 ms: 3.72x slower                                        |
| Geometric mean           | (ref)                                                  | 1.20x faster                                                 |

Benchmark hidden because not significant (1): scimark_sparse_mat_mult
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250117-3.14.0a4+-e537b8b-NOGIL/bm-20250117-linux-x86_64-kumaraditya303-gc-3.14.0a4+-e537b8b.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.241x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.15x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: 1.51x