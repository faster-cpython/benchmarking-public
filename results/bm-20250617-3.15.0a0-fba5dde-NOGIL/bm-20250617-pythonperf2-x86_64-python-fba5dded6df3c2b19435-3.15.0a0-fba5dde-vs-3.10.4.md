# Results vs. 3.10.4

- fork: python
- ref: fba5dded6df3c2b19435
- machine: linux-x86_64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.025x faster
- HPT reliability: 91.68%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.69x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 364 ms: 1.04x slower                                                        |
| docutils       | 3.41 sec                                                     | 3.27 sec: 1.04x faster                                                      |
| html5lib       | 94.6 ms                                                      | 75.3 ms: 1.26x faster                                                       |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 639 ms: 2.50x faster                                                        |
| async_tree_none         | 692 ms                                                       | 293 ms: 2.36x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 357 ms: 2.30x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 645 ms: 1.45x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.11x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 80.0 ms: 1.39x faster                                                       |
| pidigits       | 271 ms                                                       | 254 ms: 1.07x faster                                                        |
| nbody          | 134 ms                                                       | 135 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                        | 1.14x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 176 ms: 1.08x faster                                                        |
| regex_dna      | 261 ms                                                       | 249 ms: 1.05x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 26.8 ms: 1.01x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.44 ms: 1.11x slower                                                       |
| Geometric mean | (ref)                                                        | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.92 sec                                                     | 2.71 sec: 1.07x faster                                                      |
| unpickle_pure_python | 312 us                                                       | 295 us: 1.06x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 448 us: 1.02x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 109 ms: 1.01x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 169 ms: 1.05x slower                                                        |
| json_dumps           | 14.5 ms                                                      | 15.5 ms: 1.07x slower                                                       |
| xml_etree_process    | 75.9 ms                                                      | 88.3 ms: 1.16x slower                                                       |
| json_loads           | 30.3 us                                                      | 35.6 us: 1.17x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 37.1 us: 1.26x slower                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 124 ms: 1.35x slower                                                        |
| unpickle_list        | 4.65 us                                                      | 6.31 us: 1.36x slower                                                       |
| pickle_list          | 4.12 us                                                      | 6.14 us: 1.49x slower                                                       |
| unpickle             | 13.5 us                                                      | 21.1 us: 1.56x slower                                                       |
| pickle               | 9.89 us                                                      | 15.7 us: 1.59x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.19x slower                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 12.6 ms: 1.72x slower                                                       |
| python_startup         | 11.5 ms                                                      | 21.2 ms: 1.85x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.78x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 51.9 ms: 1.03x slower                                                       |
| genshi_text     | 31.4 ms                                                      | 36.5 ms: 1.16x slower                                                       |
| genshi_xml      | 63.3 ms                                                      | 76.6 ms: 1.21x slower                                                       |
| mako            | 14.7 ms                                                      | 19.7 ms: 1.34x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.18x slower                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io            | 1.60 sec                                                     | 639 ms: 2.50x faster                                                        |
| async_tree_none          | 692 ms                                                       | 293 ms: 2.36x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 357 ms: 2.30x faster                                                        |
| typing_runtime_protocols | 537 us                                                       | 257 us: 2.09x faster                                                        |
| deltablue                | 7.50 ms                                                      | 4.04 ms: 1.86x faster                                                       |
| asyncio_tcp              | 779 ms                                                       | 425 ms: 1.83x faster                                                        |
| go                       | 262 ms                                                       | 151 ms: 1.74x faster                                                        |
| mdp                      | 3.01 sec                                                     | 1.81 sec: 1.66x faster                                                      |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.90 sec: 1.63x faster                                                      |
| generators               | 57.3 ms                                                      | 35.9 ms: 1.59x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 645 ms: 1.45x faster                                                        |
| pylint                   | 566 ms                                                       | 394 ms: 1.44x faster                                                        |
| pyflate                  | 733 ms                                                       | 522 ms: 1.41x faster                                                        |
| float                    | 111 ms                                                       | 80.0 ms: 1.39x faster                                                       |
| chaos                    | 109 ms                                                       | 81.5 ms: 1.33x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 38.9 us: 1.28x faster                                                       |
| raytrace                 | 489 ms                                                       | 389 ms: 1.26x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 75.3 ms: 1.26x faster                                                       |
| deepcopy                 | 468 us                                                       | 374 us: 1.25x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 7.53 ms: 1.25x faster                                                       |
| coroutines               | 30.3 ms                                                      | 24.5 ms: 1.23x faster                                                       |
| scimark_sor              | 180 ms                                                       | 147 ms: 1.23x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.38 sec: 1.22x faster                                                      |
| dulwich_log              | 81.1 ms                                                      | 67.9 ms: 1.20x faster                                                       |
| scimark_lu               | 167 ms                                                       | 142 ms: 1.17x faster                                                        |
| richards_super           | 90.6 ms                                                      | 77.6 ms: 1.17x faster                                                       |
| richards                 | 75.1 ms                                                      | 65.8 ms: 1.14x faster                                                       |
| comprehensions           | 26.7 us                                                      | 23.6 us: 1.13x faster                                                       |
| gc_traversal             | 3.42 ms                                                      | 3.02 ms: 1.13x faster                                                       |
| regex_compile            | 190 ms                                                       | 176 ms: 1.08x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.71 sec: 1.07x faster                                                      |
| scimark_monte_carlo      | 107 ms                                                       | 100 ms: 1.07x faster                                                        |
| pidigits                 | 271 ms                                                       | 254 ms: 1.07x faster                                                        |
| unpack_sequence          | 59.9 ns                                                      | 56.4 ns: 1.06x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 295 us: 1.06x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 20.3 ms: 1.05x faster                                                       |
| regex_dna                | 261 ms                                                       | 249 ms: 1.05x faster                                                        |
| docutils                 | 3.41 sec                                                     | 3.27 sec: 1.04x faster                                                      |
| asyncio_websockets       | 390 ms                                                       | 377 ms: 1.04x faster                                                        |
| logging_simple           | 8.88 us                                                      | 8.62 us: 1.03x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 117 ms: 1.02x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 448 us: 1.02x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 27.8 ms: 1.01x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 26.8 ms: 1.01x faster                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 109 ms: 1.01x faster                                                        |
| spectral_norm            | 139 ms                                                       | 138 ms: 1.01x faster                                                        |
| logging_format           | 9.64 us                                                      | 9.59 us: 1.00x faster                                                       |
| nbody                    | 134 ms                                                       | 135 ms: 1.01x slower                                                        |
| sqlite_synth             | 2.99 us                                                      | 3.08 us: 1.03x slower                                                       |
| sympy_sum                | 193 ms                                                       | 198 ms: 1.03x slower                                                        |
| django_template          | 50.2 ms                                                      | 51.9 ms: 1.03x slower                                                       |
| thrift                   | 1.18 ms                                                      | 1.22 ms: 1.04x slower                                                       |
| 2to3                     | 350 ms                                                       | 364 ms: 1.04x slower                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 4.17 us: 1.04x slower                                                       |
| xml_etree_parse          | 160 ms                                                       | 169 ms: 1.05x slower                                                        |
| json_dumps               | 14.5 ms                                                      | 15.5 ms: 1.07x slower                                                       |
| nqueens                  | 115 ms                                                       | 123 ms: 1.07x slower                                                        |
| sympy_str                | 360 ms                                                       | 387 ms: 1.07x slower                                                        |
| sympy_expand             | 600 ms                                                       | 664 ms: 1.11x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.44 ms: 1.11x slower                                                       |
| meteor_contest           | 138 ms                                                       | 155 ms: 1.12x slower                                                        |
| fannkuch                 | 483 ms                                                       | 544 ms: 1.13x slower                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 1.20 sec: 1.15x slower                                                      |
| pprint_pformat           | 2.15 sec                                                     | 2.48 sec: 1.15x slower                                                      |
| json                     | 5.86 ms                                                      | 6.76 ms: 1.15x slower                                                       |
| genshi_text              | 31.4 ms                                                      | 36.5 ms: 1.16x slower                                                       |
| xml_etree_process        | 75.9 ms                                                      | 88.3 ms: 1.16x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.06 ms: 1.17x slower                                                       |
| json_loads               | 30.3 us                                                      | 35.6 us: 1.17x slower                                                       |
| genshi_xml               | 63.3 ms                                                      | 76.6 ms: 1.21x slower                                                       |
| scimark_fft              | 361 ms                                                       | 445 ms: 1.23x slower                                                        |
| pickle_dict              | 29.5 us                                                      | 37.1 us: 1.26x slower                                                       |
| async_generators         | 421 ms                                                       | 536 ms: 1.27x slower                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 1.50 ms: 1.31x slower                                                       |
| mako                     | 14.7 ms                                                      | 19.7 ms: 1.34x slower                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 124 ms: 1.35x slower                                                        |
| unpickle_list            | 4.65 us                                                      | 6.31 us: 1.36x slower                                                       |
| pickle_list              | 4.12 us                                                      | 6.14 us: 1.49x slower                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 7.78 ms: 1.53x slower                                                       |
| unpickle                 | 13.5 us                                                      | 21.1 us: 1.56x slower                                                       |
| pickle                   | 9.89 us                                                      | 15.7 us: 1.59x slower                                                       |
| telco                    | 7.23 ms                                                      | 12.0 ms: 1.66x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 12.6 ms: 1.72x slower                                                       |
| python_startup           | 11.5 ms                                                      | 21.2 ms: 1.85x slower                                                       |
| coverage                 | 63.3 ms                                                      | 135 ms: 2.14x slower                                                        |
| logging_silent           | 167 ns                                                       | 780 ns: 4.66x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 61.7 ms: 9.69x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.00x slower                                                                |
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (15) of results/bm-20250617-3.15.0a0-fba5dde-NOGIL/bm-20250617-pythonperf2-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.025x faster

# HPT report

- Reliability score: 91.68% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.69x