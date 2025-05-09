# Results vs. 3.10.4

- fork: python
- ref: 4617d68d73409e83d6ab
- machine: windows-amd64
- commit hash: 4617d68
- commit date: 2025-05-08
- overall geometric mean: 1.156x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-pythonperf1-amd64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 228 ms: 1.08x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.66 sec: 1.16x faster                                                     |
| html5lib       | 51.0 ms                                                     | 38.7 ms: 1.32x faster                                                      |
| Geometric mean | (ref)                                                       | 1.18x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-pythonperf1-amd64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 404 ms: 2.75x faster                                                       |
| async_tree_none         | 435 ms                                                      | 174 ms: 2.50x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 223 ms: 2.36x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 333 ms: 1.92x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.36x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-pythonperf1-amd64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.9 ms: 1.40x faster                                                      |
| nbody          | 71.3 ms                                                     | 62.7 ms: 1.14x faster                                                      |
| Geometric mean | (ref)                                                       | 1.17x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-pythonperf1-amd64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 81.4 ms: 1.30x faster                                                      |
| regex_dna      | 136 ms                                                      | 121 ms: 1.13x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.1 ms: 1.10x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.63 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.13x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-pythonperf1-amd64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 134 us: 1.37x faster                                                       |
| json_dumps           | 9.16 ms                                                     | 6.78 ms: 1.35x faster                                                      |
| pickle_pure_python   | 270 us                                                      | 213 us: 1.26x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.41 sec: 1.19x faster                                                     |
| xml_etree_process    | 44.5 ms                                                     | 39.9 ms: 1.12x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 92.5 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 65.6 ms: 1.01x slower                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 56.7 ms: 1.02x slower                                                      |
| json_loads           | 14.0 us                                                     | 15.1 us: 1.07x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.13x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-pythonperf1-amd64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.6 ms: 1.26x slower                                                      |
| python_startup         | 20.6 ms                                                     | 26.6 ms: 1.29x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.28x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-pythonperf1-amd64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.77 ms: 1.33x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.4 ms: 1.29x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.2 ms: 1.20x faster                                                      |
| django_template | 28.9 ms                                                     | 24.6 ms: 1.18x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.25x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250508-pythonperf1-amd64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 110 us: 3.06x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 404 ms: 2.75x faster                                                       |
| async_tree_none          | 435 ms                                                      | 174 ms: 2.50x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 223 ms: 2.36x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 32.1 ms: 2.36x faster                                                      |
| mdp                      | 1.78 sec                                                    | 795 ms: 2.24x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.14 ms: 1.96x faster                                                      |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 333 ms: 1.92x faster                                                       |
| go                       | 139 ms                                                      | 78.3 ms: 1.77x faster                                                      |
| pylint                   | 350 ms                                                      | 201 ms: 1.74x faster                                                       |
| logging_silent           | 94.6 ns                                                     | 55.4 ns: 1.71x faster                                                      |
| generators               | 32.4 ms                                                     | 19.2 ms: 1.68x faster                                                      |
| richards_super           | 52.2 ms                                                     | 31.7 ms: 1.65x faster                                                      |
| chaos                    | 61.7 ms                                                     | 38.4 ms: 1.61x faster                                                      |
| deepcopy_memo            | 28.8 us                                                     | 18.3 us: 1.57x faster                                                      |
| richards                 | 42.4 ms                                                     | 27.9 ms: 1.52x faster                                                      |
| raytrace                 | 273 ms                                                      | 181 ms: 1.51x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 57.1 ms: 1.50x faster                                                      |
| deepcopy                 | 255 us                                                      | 171 us: 1.49x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 39.7 ms: 1.44x faster                                                      |
| pyflate                  | 409 ms                                                      | 284 ms: 1.44x faster                                                       |
| comprehensions           | 16.5 us                                                     | 11.5 us: 1.43x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.07 ms: 1.41x faster                                                      |
| scimark_sor              | 106 ms                                                      | 75.5 ms: 1.41x faster                                                      |
| float                    | 61.7 ms                                                     | 43.9 ms: 1.40x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 134 us: 1.37x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.78 ms: 1.35x faster                                                      |
| mako                     | 9.03 ms                                                     | 6.77 ms: 1.33x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 47.0 ms: 1.33x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 38.7 ms: 1.32x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 58.8 ms: 1.31x faster                                                      |
| regex_compile            | 106 ms                                                      | 81.4 ms: 1.30x faster                                                      |
| pycparser                | 930 ms                                                      | 717 ms: 1.30x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.4 ms: 1.29x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 213 us: 1.26x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.4 ms: 1.23x faster                                                      |
| sympy_sum                | 107 ms                                                      | 88.8 ms: 1.21x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 34.2 ms: 1.20x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.84 us: 1.20x faster                                                      |
| pprint_pformat           | 1.22 sec                                                    | 1.02 sec: 1.20x faster                                                     |
| dulwich_log              | 50.5 ms                                                     | 42.2 ms: 1.20x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 495 ms: 1.19x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.60 us: 1.19x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.41 sec: 1.19x faster                                                     |
| django_template          | 28.9 ms                                                     | 24.6 ms: 1.18x faster                                                      |
| coroutines               | 16.0 ms                                                     | 13.6 ms: 1.17x faster                                                      |
| docutils                 | 1.92 sec                                                    | 1.66 sec: 1.16x faster                                                     |
| nbody                    | 71.3 ms                                                     | 62.7 ms: 1.14x faster                                                      |
| sympy_str                | 194 ms                                                      | 171 ms: 1.14x faster                                                       |
| regex_dna                | 136 ms                                                      | 121 ms: 1.13x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 39.9 ms: 1.12x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.48 ms: 1.10x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 14.1 ms: 1.10x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 60.7 ms: 1.10x faster                                                      |
| scimark_fft              | 187 ms                                                      | 172 ms: 1.09x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 883 us: 1.08x faster                                                       |
| 2to3                     | 246 ms                                                      | 228 ms: 1.08x faster                                                       |
| sympy_expand             | 314 ms                                                      | 292 ms: 1.08x faster                                                       |
| json                     | 3.14 ms                                                     | 2.99 ms: 1.05x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 92.5 ms: 1.05x faster                                                      |
| fannkuch                 | 256 ms                                                      | 251 ms: 1.02x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.63 ms: 1.02x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 74.7 ms: 1.02x faster                                                      |
| logging_format           | 6.76 us                                                     | 6.69 us: 1.01x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 65.6 ms: 1.01x slower                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 56.7 ms: 1.02x slower                                                      |
| async_generators         | 222 ms                                                      | 233 ms: 1.05x slower                                                       |
| json_loads               | 14.0 us                                                     | 15.1 us: 1.07x slower                                                      |
| telco                    | 3.94 ms                                                     | 4.67 ms: 1.18x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.6 ms: 1.26x slower                                                      |
| python_startup           | 20.6 ms                                                     | 26.6 ms: 1.29x slower                                                      |
| bench_mp_pool            | 62.0 ms                                                     | 97.6 ms: 1.57x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.23 ms: 1.58x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.31 ms: 1.64x slower                                                      |
| coverage                 | 39.0 ms                                                     | 294 ms: 7.53x slower                                                       |
| thrift                   | 617 us                                                      | 103 ms: 166.12x slower                                                     |
| Geometric mean           | (ref)                                                       | 1.15x faster                                                               |

Benchmark hidden because not significant (2): pidigits, logging_simple
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250508-3.15.0a0-4617d68/bm-20250508-pythonperf1-amd64-python-4617d68d73409e83d6ab-3.15.0a0-4617d68.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.156x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: unknown