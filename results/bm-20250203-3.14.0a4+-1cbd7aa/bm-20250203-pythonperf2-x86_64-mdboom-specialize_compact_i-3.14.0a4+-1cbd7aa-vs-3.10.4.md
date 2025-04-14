# Results vs. 3.10.4

- fork: mdboom
- ref: specialize_compact_i
- machine: linux-x86_64
- commit hash: 1cbd7aa
- commit date: 2025-02-03
- overall geometric mean: 1.367x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4+-1cbd7aa |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 279 ms: 1.26x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.85 sec: 1.20x faster                                                       |
| html5lib       | 94.6 ms                                                      | 66.0 ms: 1.43x faster                                                        |
| Geometric mean | (ref)                                                        | 1.29x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4+-1cbd7aa |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 651 ms: 2.45x faster                                                         |
| async_tree_none         | 692 ms                                                       | 290 ms: 2.39x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 350 ms: 2.34x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 520 ms: 1.80x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.23x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4+-1cbd7aa |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 69.1 ms: 1.61x faster                                                        |
| nbody          | 134 ms                                                       | 87.9 ms: 1.53x faster                                                        |
| pidigits       | 271 ms                                                       | 254 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                        | 1.38x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4+-1cbd7aa |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 135 ms: 1.41x faster                                                         |
| regex_dna      | 261 ms                                                       | 233 ms: 1.12x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 25.6 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                        | 1.13x faster                                                                 |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4+-1cbd7aa |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 209 us: 1.49x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 2.05 sec: 1.42x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 324 us: 1.40x faster                                                         |
| xml_etree_process    | 75.9 ms                                                      | 59.0 ms: 1.29x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 11.6 ms: 1.25x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 132 ms: 1.21x faster                                                         |
| xml_etree_iterparse  | 110 ms                                                       | 95.6 ms: 1.16x faster                                                        |
| json_loads           | 30.3 us                                                      | 26.3 us: 1.15x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 83.7 ms: 1.10x faster                                                        |
| Geometric mean       | (ref)                                                        | 1.27x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4+-1cbd7aa |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.97 ms: 1.22x slower                                                        |
| python_startup         | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.30x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4+-1cbd7aa |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 35.4 ms: 1.42x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 22.9 ms: 1.37x faster                                                        |
| mako            | 14.7 ms                                                      | 10.8 ms: 1.36x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 51.8 ms: 1.22x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.34x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4+-1cbd7aa |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 167 us: 3.22x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 651 ms: 2.45x faster                                                         |
| async_tree_none          | 692 ms                                                       | 290 ms: 2.39x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 350 ms: 2.34x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.23 ms: 2.32x faster                                                        |
| go                       | 262 ms                                                       | 123 ms: 2.13x faster                                                         |
| generators               | 57.3 ms                                                      | 28.7 ms: 2.00x faster                                                        |
| raytrace                 | 489 ms                                                       | 269 ms: 1.82x faster                                                         |
| pylint                   | 566 ms                                                       | 313 ms: 1.81x faster                                                         |
| chaos                    | 109 ms                                                       | 60.0 ms: 1.81x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 520 ms: 1.80x faster                                                         |
| scimark_lu               | 167 ms                                                       | 94.0 ms: 1.77x faster                                                        |
| richards_super           | 90.6 ms                                                      | 51.3 ms: 1.77x faster                                                        |
| spectral_norm            | 139 ms                                                       | 79.9 ms: 1.74x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 62.0 ms: 1.73x faster                                                        |
| logging_silent           | 167 ns                                                       | 96.7 ns: 1.73x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.32 ms: 1.70x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 29.3 us: 1.70x faster                                                        |
| scimark_sor              | 180 ms                                                       | 107 ms: 1.69x faster                                                         |
| deepcopy                 | 468 us                                                       | 278 us: 1.68x faster                                                         |
| richards                 | 75.1 ms                                                      | 45.1 ms: 1.66x faster                                                        |
| pyflate                  | 733 ms                                                       | 442 ms: 1.66x faster                                                         |
| crypto_pyaes             | 119 ms                                                       | 72.0 ms: 1.66x faster                                                        |
| float                    | 111 ms                                                       | 69.1 ms: 1.61x faster                                                        |
| comprehensions           | 26.7 us                                                      | 16.9 us: 1.58x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.01 ms: 1.57x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.71 ms: 1.56x faster                                                        |
| nbody                    | 134 ms                                                       | 87.9 ms: 1.53x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 209 us: 1.49x faster                                                         |
| coroutines               | 30.3 ms                                                      | 20.7 ms: 1.46x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 66.0 ms: 1.43x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.05 sec: 1.42x faster                                                       |
| django_template          | 50.2 ms                                                      | 35.4 ms: 1.42x faster                                                        |
| regex_compile            | 190 ms                                                       | 135 ms: 1.41x faster                                                         |
| pickle_pure_python       | 455 us                                                       | 324 us: 1.40x faster                                                         |
| logging_simple           | 8.88 us                                                      | 6.35 us: 1.40x faster                                                        |
| logging_format           | 9.64 us                                                      | 6.97 us: 1.38x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 2.90 us: 1.38x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 22.9 ms: 1.37x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 15.6 ms: 1.37x faster                                                        |
| mako                     | 14.7 ms                                                      | 10.8 ms: 1.36x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.59 sec: 1.36x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.23 sec: 1.36x faster                                                       |
| thrift                   | 1.18 ms                                                      | 868 us: 1.35x faster                                                         |
| pprint_safe_repr         | 1.05 sec                                                     | 781 ms: 1.34x faster                                                         |
| fannkuch                 | 483 ms                                                       | 361 ms: 1.34x faster                                                         |
| sqlalchemy_declarative   | 190 ms                                                       | 142 ms: 1.33x faster                                                         |
| sqlalchemy_imperative    | 22.7 ms                                                      | 17.6 ms: 1.29x faster                                                        |
| nqueens                  | 115 ms                                                       | 88.9 ms: 1.29x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 59.0 ms: 1.29x faster                                                        |
| sympy_sum                | 193 ms                                                       | 150 ms: 1.29x faster                                                         |
| sqlglot_normalize        | 144 ms                                                       | 114 ms: 1.26x faster                                                         |
| 2to3                     | 350 ms                                                       | 279 ms: 1.26x faster                                                         |
| sympy_str                | 360 ms                                                       | 287 ms: 1.25x faster                                                         |
| json_dumps               | 14.5 ms                                                      | 11.6 ms: 1.25x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 56.5 ms: 1.24x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 920 us: 1.24x faster                                                         |
| sympy_expand             | 600 ms                                                       | 485 ms: 1.24x faster                                                         |
| dulwich_log              | 81.1 ms                                                      | 66.2 ms: 1.23x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.45 sec: 1.23x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 23.0 ms: 1.22x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 51.8 ms: 1.22x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 132 ms: 1.21x faster                                                         |
| docutils                 | 3.41 sec                                                     | 2.85 sec: 1.20x faster                                                       |
| scimark_fft              | 361 ms                                                       | 305 ms: 1.19x faster                                                         |
| xml_etree_iterparse      | 110 ms                                                       | 95.6 ms: 1.16x faster                                                        |
| json_loads               | 30.3 us                                                      | 26.3 us: 1.15x faster                                                        |
| regex_dna                | 261 ms                                                       | 233 ms: 1.12x faster                                                         |
| meteor_contest           | 138 ms                                                       | 124 ms: 1.12x faster                                                         |
| xml_etree_generate       | 92.3 ms                                                      | 83.7 ms: 1.10x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.64 ms: 1.10x faster                                                        |
| pidigits                 | 271 ms                                                       | 254 ms: 1.07x faster                                                         |
| sqlite_synth             | 2.99 us                                                      | 2.81 us: 1.06x faster                                                        |
| json                     | 5.86 ms                                                      | 5.52 ms: 1.06x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 25.6 ms: 1.06x faster                                                        |
| async_generators         | 421 ms                                                       | 408 ms: 1.03x faster                                                         |
| asyncio_websockets       | 390 ms                                                       | 384 ms: 1.02x faster                                                         |
| telco                    | 7.23 ms                                                      | 7.86 ms: 1.09x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 8.97 ms: 1.22x slower                                                        |
| coverage                 | 63.3 ms                                                      | 78.8 ms: 1.25x slower                                                        |
| python_startup           | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.71 ms: 1.54x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 6.33 ms: 1.85x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 1.26 sec: 197.75x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.28x faster                                                                 |

Benchmark hidden because not significant (1): regex_effbot
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250203-3.14.0a4+-1cbd7aa/bm-20250203-pythonperf2-x86_64-mdboom-specialize_compact_i-3.14.0a4+-1cbd7aa.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.367x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.27x