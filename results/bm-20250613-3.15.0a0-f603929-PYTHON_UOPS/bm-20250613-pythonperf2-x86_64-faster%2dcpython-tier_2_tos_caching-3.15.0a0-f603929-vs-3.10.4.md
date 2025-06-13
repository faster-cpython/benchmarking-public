# Results vs. 3.10.4

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: f603929
- commit date: 2025-06-13
- overall geometric mean: 1.108x faster
- HPT reliability: 99.73%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.36x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 331 ms: 1.06x faster                                                                |
| docutils       | 3.41 sec                                                     | 3.19 sec: 1.07x faster                                                              |
| html5lib       | 94.6 ms                                                      | 70.9 ms: 1.33x faster                                                               |
| Geometric mean | (ref)                                                        | 1.15x faster                                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|-------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 679 ms: 2.36x faster                                                                |
| async_tree_memoization  | 819 ms                                                       | 364 ms: 2.25x faster                                                                |
| async_tree_none         | 692 ms                                                       | 315 ms: 2.20x faster                                                                |
| async_tree_cpu_io_mixed | 936 ms                                                       | 540 ms: 1.73x faster                                                                |
| Geometric mean          | (ref)                                                        | 2.12x faster                                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| pidigits       | 271 ms                                                       | 260 ms: 1.04x faster                                                                |
| nbody          | 134 ms                                                       | 216 ms: 1.61x slower                                                                |
| Geometric mean | (ref)                                                        | 1.16x slower                                                                        |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_dna      | 261 ms                                                       | 222 ms: 1.18x faster                                                                |
| regex_compile  | 190 ms                                                       | 164 ms: 1.16x faster                                                                |
| regex_v8       | 27.2 ms                                                      | 25.2 ms: 1.08x faster                                                               |
| regex_effbot   | 3.09 ms                                                      | 3.75 ms: 1.22x slower                                                               |
| Geometric mean | (ref)                                                        | 1.05x faster                                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|----------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| json_dumps           | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                                               |
| json_loads           | 30.3 us                                                      | 24.9 us: 1.22x faster                                                               |
| xml_etree_parse      | 160 ms                                                       | 145 ms: 1.10x faster                                                                |
| pickle_pure_python   | 455 us                                                       | 432 us: 1.05x faster                                                                |
| xml_etree_process    | 75.9 ms                                                      | 80.7 ms: 1.06x slower                                                               |
| tomli_loads          | 2.92 sec                                                     | 3.34 sec: 1.14x slower                                                              |
| xml_etree_generate   | 92.3 ms                                                      | 115 ms: 1.25x slower                                                                |
| unpickle_pure_python | 312 us                                                       | 425 us: 1.36x slower                                                                |
| Geometric mean       | (ref)                                                        | 1.01x slower                                                                        |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.82 ms: 1.20x slower                                                               |
| python_startup         | 11.5 ms                                                      | 15.3 ms: 1.33x slower                                                               |
| Geometric mean         | (ref)                                                        | 1.26x slower                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|-----------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 35.6 ms: 1.41x faster                                                               |
| genshi_text     | 31.4 ms                                                      | 23.3 ms: 1.35x faster                                                               |
| genshi_xml      | 63.3 ms                                                      | 56.4 ms: 1.12x faster                                                               |
| mako            | 14.7 ms                                                      | 19.9 ms: 1.36x slower                                                               |
| Geometric mean  | (ref)                                                        | 1.12x faster                                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250613-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929 |
|--------------------------|:------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 215 us: 2.49x faster                                                                |
| async_tree_io            | 1.60 sec                                                     | 679 ms: 2.36x faster                                                                |
| async_tree_memoization   | 819 ms                                                       | 364 ms: 2.25x faster                                                                |
| async_tree_none          | 692 ms                                                       | 315 ms: 2.20x faster                                                                |
| generators               | 57.3 ms                                                      | 27.9 ms: 2.06x faster                                                               |
| mdp                      | 3.01 sec                                                     | 1.51 sec: 1.99x faster                                                              |
| deepcopy_memo            | 49.8 us                                                      | 27.3 us: 1.82x faster                                                               |
| scimark_lu               | 167 ms                                                       | 93.3 ms: 1.79x faster                                                               |
| scimark_sor              | 180 ms                                                       | 104 ms: 1.73x faster                                                                |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 540 ms: 1.73x faster                                                                |
| deepcopy                 | 468 us                                                       | 278 us: 1.68x faster                                                                |
| pylint                   | 566 ms                                                       | 337 ms: 1.68x faster                                                                |
| chaos                    | 109 ms                                                       | 65.3 ms: 1.66x faster                                                               |
| raytrace                 | 489 ms                                                       | 339 ms: 1.44x faster                                                                |
| django_template          | 50.2 ms                                                      | 35.6 ms: 1.41x faster                                                               |
| richards_super           | 90.6 ms                                                      | 64.5 ms: 1.40x faster                                                               |
| thrift                   | 1.18 ms                                                      | 841 us: 1.40x faster                                                                |
| logging_simple           | 8.88 us                                                      | 6.42 us: 1.38x faster                                                               |
| logging_format           | 9.64 us                                                      | 7.04 us: 1.37x faster                                                               |
| deepcopy_reduce          | 4.01 us                                                      | 2.94 us: 1.36x faster                                                               |
| genshi_text              | 31.4 ms                                                      | 23.3 ms: 1.35x faster                                                               |
| coroutines               | 30.3 ms                                                      | 22.6 ms: 1.34x faster                                                               |
| html5lib                 | 94.6 ms                                                      | 70.9 ms: 1.33x faster                                                               |
| json_dumps               | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                                               |
| richards                 | 75.1 ms                                                      | 57.9 ms: 1.30x faster                                                               |
| dulwich_log              | 81.1 ms                                                      | 63.6 ms: 1.28x faster                                                               |
| pathlib                  | 21.4 ms                                                      | 17.5 ms: 1.22x faster                                                               |
| json_loads               | 30.3 us                                                      | 24.9 us: 1.22x faster                                                               |
| sympy_integrate          | 28.2 ms                                                      | 23.9 ms: 1.18x faster                                                               |
| regex_dna                | 261 ms                                                       | 222 ms: 1.18x faster                                                                |
| sympy_sum                | 193 ms                                                       | 164 ms: 1.17x faster                                                                |
| regex_compile            | 190 ms                                                       | 164 ms: 1.16x faster                                                                |
| deltablue                | 7.50 ms                                                      | 6.51 ms: 1.15x faster                                                               |
| genshi_xml               | 63.3 ms                                                      | 56.4 ms: 1.12x faster                                                               |
| sympy_str                | 360 ms                                                       | 321 ms: 1.12x faster                                                                |
| xml_etree_parse          | 160 ms                                                       | 145 ms: 1.10x faster                                                                |
| scimark_monte_carlo      | 107 ms                                                       | 97.8 ms: 1.10x faster                                                               |
| json                     | 5.86 ms                                                      | 5.38 ms: 1.09x faster                                                               |
| pycparser                | 1.67 sec                                                     | 1.55 sec: 1.08x faster                                                              |
| regex_v8                 | 27.2 ms                                                      | 25.2 ms: 1.08x faster                                                               |
| docutils                 | 3.41 sec                                                     | 3.19 sec: 1.07x faster                                                              |
| sympy_expand             | 600 ms                                                       | 562 ms: 1.07x faster                                                                |
| pyflate                  | 733 ms                                                       | 691 ms: 1.06x faster                                                                |
| 2to3                     | 350 ms                                                       | 331 ms: 1.06x faster                                                                |
| pickle_pure_python       | 455 us                                                       | 432 us: 1.05x faster                                                                |
| go                       | 262 ms                                                       | 249 ms: 1.05x faster                                                                |
| nqueens                  | 115 ms                                                       | 110 ms: 1.05x faster                                                                |
| pidigits                 | 271 ms                                                       | 260 ms: 1.04x faster                                                                |
| crypto_pyaes             | 119 ms                                                       | 117 ms: 1.02x faster                                                                |
| asyncio_websockets       | 390 ms                                                       | 385 ms: 1.01x faster                                                                |
| sqlite_synth             | 2.99 us                                                      | 3.07 us: 1.03x slower                                                               |
| xml_etree_process        | 75.9 ms                                                      | 80.7 ms: 1.06x slower                                                               |
| async_generators         | 421 ms                                                       | 462 ms: 1.10x slower                                                                |
| tomli_loads              | 2.92 sec                                                     | 3.34 sec: 1.14x slower                                                              |
| python_startup_no_site   | 7.33 ms                                                      | 8.82 ms: 1.20x slower                                                               |
| regex_effbot             | 3.09 ms                                                      | 3.75 ms: 1.22x slower                                                               |
| coverage                 | 63.3 ms                                                      | 77.5 ms: 1.23x slower                                                               |
| pprint_pformat           | 2.15 sec                                                     | 2.67 sec: 1.24x slower                                                              |
| hexiom                   | 9.42 ms                                                      | 11.7 ms: 1.24x slower                                                               |
| comprehensions           | 26.7 us                                                      | 33.2 us: 1.24x slower                                                               |
| xml_etree_generate       | 92.3 ms                                                      | 115 ms: 1.25x slower                                                                |
| pprint_safe_repr         | 1.05 sec                                                     | 1.31 sec: 1.25x slower                                                              |
| meteor_contest           | 138 ms                                                       | 174 ms: 1.26x slower                                                                |
| python_startup           | 11.5 ms                                                      | 15.3 ms: 1.33x slower                                                               |
| telco                    | 7.23 ms                                                      | 9.67 ms: 1.34x slower                                                               |
| mako                     | 14.7 ms                                                      | 19.9 ms: 1.36x slower                                                               |
| unpickle_pure_python     | 312 us                                                       | 425 us: 1.36x slower                                                                |
| scimark_fft              | 361 ms                                                       | 538 ms: 1.49x slower                                                                |
| fannkuch                 | 483 ms                                                       | 725 ms: 1.50x slower                                                                |
| spectral_norm            | 139 ms                                                       | 214 ms: 1.54x slower                                                                |
| create_gc_cycles         | 1.76 ms                                                      | 2.80 ms: 1.59x slower                                                               |
| nbody                    | 134 ms                                                       | 216 ms: 1.61x slower                                                                |
| gc_traversal             | 3.42 ms                                                      | 6.38 ms: 1.87x slower                                                               |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 9.65 ms: 1.90x slower                                                               |
| logging_silent           | 167 ns                                                       | 501 ns: 2.99x slower                                                                |
| Geometric mean           | (ref)                                                        | 1.09x faster                                                                        |

Benchmark hidden because not significant (2): xml_etree_iterparse, float
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250613-3.15.0a0-f603929-PYTHON_UOPS/bm-20250613-pythonperf2-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-f603929.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.108x faster

# HPT report

- Reliability score: 99.73% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.36x