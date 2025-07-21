# Results vs. 3.10.4

- fork: python
- ref: 800d37feca2e0ea33439
- machine: linux-x86_64
- commit hash: 800d37f
- commit date: 2025-07-19
- overall geometric mean: 1.192x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.12x faster
- Memory change: 1.66x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 319 ms: 1.10x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.92 sec: 1.17x faster                                                      |
| html5lib       | 94.6 ms                                                      | 70.5 ms: 1.34x faster                                                       |
| Geometric mean | (ref)                                                        | 1.20x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 560 ms: 2.85x faster                                                        |
| async_tree_none         | 692 ms                                                       | 264 ms: 2.62x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 323 ms: 2.54x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 495 ms: 1.89x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.45x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 71.7 ms: 1.55x faster                                                       |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| nbody          | 134 ms                                                       | 127 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                        | 1.21x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 154 ms: 1.24x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 23.8 ms: 1.14x faster                                                       |
| regex_dna      | 261 ms                                                       | 246 ms: 1.06x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.46 ms: 1.12x slower                                                       |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 239 us: 1.30x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.31 sec: 1.26x faster                                                      |
| xml_etree_iterparse  | 110 ms                                                       | 88.3 ms: 1.25x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 368 us: 1.24x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 12.0 ms: 1.21x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 136 ms: 1.18x faster                                                        |
| json_loads           | 30.3 us                                                      | 28.0 us: 1.08x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 70.2 ms: 1.08x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 99.4 ms: 1.08x slower                                                       |
| unpickle_list        | 4.65 us                                                      | 5.56 us: 1.20x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 35.6 us: 1.21x slower                                                       |
| unpickle             | 13.5 us                                                      | 16.5 us: 1.22x slower                                                       |
| pickle               | 9.89 us                                                      | 12.3 us: 1.24x slower                                                       |
| pickle_list          | 4.12 us                                                      | 5.25 us: 1.27x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 11.6 ms: 1.59x slower                                                       |
| python_startup         | 11.5 ms                                                      | 19.5 ms: 1.70x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.64x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 43.1 ms: 1.16x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 30.1 ms: 1.04x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 66.8 ms: 1.06x slower                                                       |
| mako            | 14.7 ms                                                      | 17.2 ms: 1.17x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.00x slower                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io            | 1.60 sec                                                     | 560 ms: 2.85x faster                                                        |
| async_tree_none          | 692 ms                                                       | 264 ms: 2.62x faster                                                        |
| typing_runtime_protocols | 537 us                                                       | 208 us: 2.58x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 323 ms: 2.54x faster                                                        |
| mdp                      | 3.01 sec                                                     | 1.45 sec: 2.07x faster                                                      |
| deltablue                | 7.50 ms                                                      | 3.65 ms: 2.05x faster                                                       |
| asyncio_tcp              | 779 ms                                                       | 384 ms: 2.03x faster                                                        |
| go                       | 262 ms                                                       | 138 ms: 1.90x faster                                                        |
| generators               | 57.3 ms                                                      | 30.3 ms: 1.89x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 495 ms: 1.89x faster                                                        |
| logging_silent           | 167 ns                                                       | 96.8 ns: 1.73x faster                                                       |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.89 sec: 1.64x faster                                                      |
| chaos                    | 109 ms                                                       | 66.3 ms: 1.64x faster                                                       |
| pylint                   | 566 ms                                                       | 349 ms: 1.62x faster                                                        |
| float                    | 111 ms                                                       | 71.7 ms: 1.55x faster                                                       |
| pyflate                  | 733 ms                                                       | 474 ms: 1.55x faster                                                        |
| scimark_sor              | 180 ms                                                       | 117 ms: 1.54x faster                                                        |
| raytrace                 | 489 ms                                                       | 322 ms: 1.52x faster                                                        |
| gc_traversal             | 3.42 ms                                                      | 2.26 ms: 1.51x faster                                                       |
| comprehensions           | 26.7 us                                                      | 18.0 us: 1.48x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 33.9 us: 1.47x faster                                                       |
| deepcopy                 | 468 us                                                       | 321 us: 1.46x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.53 ms: 1.44x faster                                                       |
| richards_super           | 90.6 ms                                                      | 63.2 ms: 1.43x faster                                                       |
| scimark_lu               | 167 ms                                                       | 117 ms: 1.43x faster                                                        |
| richards                 | 75.1 ms                                                      | 54.7 ms: 1.37x faster                                                       |
| spectral_norm            | 139 ms                                                       | 102 ms: 1.36x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 70.5 ms: 1.34x faster                                                       |
| coroutines               | 30.3 ms                                                      | 22.8 ms: 1.33x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 61.6 ms: 1.32x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 81.8 ms: 1.31x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.27 sec: 1.31x faster                                                      |
| unpickle_pure_python     | 312 us                                                       | 239 us: 1.30x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 92.6 ms: 1.29x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.94 us: 1.28x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.31 sec: 1.26x faster                                                      |
| xml_etree_iterparse      | 110 ms                                                       | 88.3 ms: 1.25x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 17.1 ms: 1.25x faster                                                       |
| logging_format           | 9.64 us                                                      | 7.78 us: 1.24x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 368 us: 1.24x faster                                                        |
| regex_compile            | 190 ms                                                       | 154 ms: 1.24x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 12.0 ms: 1.21x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 884 ms: 1.19x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.82 sec: 1.18x faster                                                      |
| xml_etree_parse          | 160 ms                                                       | 136 ms: 1.18x faster                                                        |
| thrift                   | 1.18 ms                                                      | 1.00 ms: 1.17x faster                                                       |
| docutils                 | 3.41 sec                                                     | 2.92 sec: 1.17x faster                                                      |
| django_template          | 50.2 ms                                                      | 43.1 ms: 1.16x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 3.51 us: 1.14x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 23.8 ms: 1.14x faster                                                       |
| sqlite_synth             | 2.99 us                                                      | 2.66 us: 1.13x faster                                                       |
| sympy_sum                | 193 ms                                                       | 172 ms: 1.12x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 25.2 ms: 1.12x faster                                                       |
| sympy_str                | 360 ms                                                       | 326 ms: 1.11x faster                                                        |
| 2to3                     | 350 ms                                                       | 319 ms: 1.10x faster                                                        |
| nqueens                  | 115 ms                                                       | 105 ms: 1.09x faster                                                        |
| sympy_expand             | 600 ms                                                       | 551 ms: 1.09x faster                                                        |
| json_loads               | 30.3 us                                                      | 28.0 us: 1.08x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 70.2 ms: 1.08x faster                                                       |
| pidigits                 | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| unpack_sequence          | 59.9 ns                                                      | 55.7 ns: 1.08x faster                                                       |
| json                     | 5.86 ms                                                      | 5.50 ms: 1.07x faster                                                       |
| regex_dna                | 261 ms                                                       | 246 ms: 1.06x faster                                                        |
| nbody                    | 134 ms                                                       | 127 ms: 1.06x faster                                                        |
| fannkuch                 | 483 ms                                                       | 460 ms: 1.05x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 30.1 ms: 1.04x faster                                                       |
| scimark_fft              | 361 ms                                                       | 357 ms: 1.01x faster                                                        |
| meteor_contest           | 138 ms                                                       | 144 ms: 1.04x slower                                                        |
| genshi_xml               | 63.3 ms                                                      | 66.8 ms: 1.06x slower                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 99.4 ms: 1.08x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 1.97 ms: 1.12x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.46 ms: 1.12x slower                                                       |
| async_generators         | 421 ms                                                       | 475 ms: 1.13x slower                                                        |
| mako                     | 14.7 ms                                                      | 17.2 ms: 1.17x slower                                                       |
| unpickle_list            | 4.65 us                                                      | 5.56 us: 1.20x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 35.6 us: 1.21x slower                                                       |
| unpickle                 | 13.5 us                                                      | 16.5 us: 1.22x slower                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 6.25 ms: 1.23x slower                                                       |
| pickle                   | 9.89 us                                                      | 12.3 us: 1.24x slower                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 1.42 ms: 1.25x slower                                                       |
| pickle_list              | 4.12 us                                                      | 5.25 us: 1.27x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 11.6 ms: 1.59x slower                                                       |
| python_startup           | 11.5 ms                                                      | 19.5 ms: 1.70x slower                                                       |
| coverage                 | 63.3 ms                                                      | 116 ms: 1.83x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 57.3 ms: 9.00x slower                                                       |
| telco                    | 7.23 ms                                                      | 175 ms: 24.27x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.15x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (15) of results/bm-20250719-3.15.0a0-800d37f-NOGIL/bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.192x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.16x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.12x

# Memory
- memory change: 1.66x