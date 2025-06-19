# Results vs. 3.10.4

- fork: python
- ref: 9731dd2c8df3509095ea
- machine: windows-amd64
- commit hash: 9731dd2
- commit date: 2025-06-19
- overall geometric mean: 1.298x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-pythonperf1-amd64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 221 ms: 1.11x faster                                                       |
| docutils       | 1.92 sec                                                    | 1.69 sec: 1.14x faster                                                     |
| html5lib       | 51.0 ms                                                     | 38.2 ms: 1.34x faster                                                      |
| Geometric mean | (ref)                                                       | 1.19x faster                                                               |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-pythonperf1-amd64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 395 ms: 2.81x faster                                                       |
| async_tree_none         | 435 ms                                                      | 169 ms: 2.57x faster                                                       |
| async_tree_memoization  | 526 ms                                                      | 207 ms: 2.54x faster                                                       |
| async_tree_cpu_io_mixed | 638 ms                                                      | 327 ms: 1.95x faster                                                       |
| Geometric mean          | (ref)                                                       | 2.44x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-pythonperf1-amd64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.8 ms: 1.41x faster                                                      |
| nbody          | 71.3 ms                                                     | 52.4 ms: 1.36x faster                                                      |
| Geometric mean | (ref)                                                       | 1.24x faster                                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-pythonperf1-amd64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 78.2 ms: 1.36x faster                                                      |
| regex_dna      | 136 ms                                                      | 118 ms: 1.16x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 14.2 ms: 1.09x faster                                                      |
| regex_effbot   | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                                      |
| Geometric mean | (ref)                                                       | 1.15x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-pythonperf1-amd64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 112 us: 1.63x faster                                                       |
| json_dumps           | 9.16 ms                                                     | 6.15 ms: 1.49x faster                                                      |
| tomli_loads          | 1.67 sec                                                    | 1.16 sec: 1.44x faster                                                     |
| pickle_pure_python   | 270 us                                                      | 207 us: 1.30x faster                                                       |
| xml_etree_process    | 44.5 ms                                                     | 36.2 ms: 1.23x faster                                                      |
| xml_etree_parse      | 96.8 ms                                                     | 88.8 ms: 1.09x faster                                                      |
| xml_etree_generate   | 55.5 ms                                                     | 51.1 ms: 1.09x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.8 ms: 1.02x faster                                                      |
| json_loads           | 14.0 us                                                     | 14.5 us: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                       | 1.23x faster                                                               |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-pythonperf1-amd64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.4 ms: 1.25x slower                                                      |
| python_startup         | 20.6 ms                                                     | 26.2 ms: 1.27x slower                                                      |
| Geometric mean         | (ref)                                                       | 1.26x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-pythonperf1-amd64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.67 ms: 1.59x faster                                                      |
| genshi_text     | 19.8 ms                                                     | 15.1 ms: 1.31x faster                                                      |
| django_template | 28.9 ms                                                     | 24.1 ms: 1.20x faster                                                      |
| genshi_xml      | 41.0 ms                                                     | 34.6 ms: 1.19x faster                                                      |
| Geometric mean  | (ref)                                                       | 1.31x faster                                                               |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250619-pythonperf1-amd64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 105 us: 3.20x faster                                                       |
| async_tree_io            | 1.11 sec                                                    | 395 ms: 2.81x faster                                                       |
| async_tree_none          | 435 ms                                                      | 169 ms: 2.57x faster                                                       |
| async_tree_memoization   | 526 ms                                                      | 207 ms: 2.54x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 33.1 ms: 2.29x faster                                                      |
| mdp                      | 1.78 sec                                                    | 812 ms: 2.19x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 327 ms: 1.95x faster                                                       |
| deltablue                | 4.19 ms                                                     | 2.18 ms: 1.92x faster                                                      |
| go                       | 139 ms                                                      | 77.0 ms: 1.81x faster                                                      |
| pylint                   | 350 ms                                                      | 200 ms: 1.75x faster                                                       |
| richards_super           | 52.2 ms                                                     | 30.8 ms: 1.70x faster                                                      |
| generators               | 32.4 ms                                                     | 19.8 ms: 1.64x faster                                                      |
| unpickle_pure_python     | 183 us                                                      | 112 us: 1.63x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 18.0 us: 1.60x faster                                                      |
| mako                     | 9.03 ms                                                     | 5.67 ms: 1.59x faster                                                      |
| pyflate                  | 409 ms                                                      | 258 ms: 1.58x faster                                                       |
| richards                 | 42.4 ms                                                     | 27.3 ms: 1.55x faster                                                      |
| raytrace                 | 273 ms                                                      | 177 ms: 1.54x faster                                                       |
| chaos                    | 61.7 ms                                                     | 40.5 ms: 1.52x faster                                                      |
| deepcopy                 | 255 us                                                      | 169 us: 1.51x faster                                                       |
| comprehensions           | 16.5 us                                                     | 10.9 us: 1.51x faster                                                      |
| json_dumps               | 9.16 ms                                                     | 6.15 ms: 1.49x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 39.8 ms: 1.44x faster                                                      |
| tomli_loads              | 1.67 sec                                                    | 1.16 sec: 1.44x faster                                                     |
| scimark_lu               | 85.8 ms                                                     | 60.6 ms: 1.41x faster                                                      |
| float                    | 61.7 ms                                                     | 43.8 ms: 1.41x faster                                                      |
| scimark_sor              | 106 ms                                                      | 75.9 ms: 1.40x faster                                                      |
| hexiom                   | 5.74 ms                                                     | 4.21 ms: 1.37x faster                                                      |
| nbody                    | 71.3 ms                                                     | 52.4 ms: 1.36x faster                                                      |
| regex_compile            | 106 ms                                                      | 78.2 ms: 1.36x faster                                                      |
| html5lib                 | 51.0 ms                                                     | 38.2 ms: 1.34x faster                                                      |
| crypto_pyaes             | 62.5 ms                                                     | 47.2 ms: 1.32x faster                                                      |
| pycparser                | 930 ms                                                      | 704 ms: 1.32x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.1 ms: 1.31x faster                                                      |
| pickle_pure_python       | 270 us                                                      | 207 us: 1.30x faster                                                       |
| thrift                   | 617 us                                                      | 489 us: 1.26x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.54 us: 1.24x faster                                                      |
| xml_etree_process        | 44.5 ms                                                     | 36.2 ms: 1.23x faster                                                      |
| scimark_fft              | 187 ms                                                      | 153 ms: 1.23x faster                                                       |
| deepcopy_reduce          | 2.20 us                                                     | 1.80 us: 1.22x faster                                                      |
| dulwich_log              | 50.5 ms                                                     | 41.4 ms: 1.22x faster                                                      |
| sympy_sum                | 107 ms                                                      | 87.8 ms: 1.22x faster                                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.7 ms: 1.20x faster                                                      |
| django_template          | 28.9 ms                                                     | 24.1 ms: 1.20x faster                                                      |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.29 ms: 1.19x faster                                                      |
| genshi_xml               | 41.0 ms                                                     | 34.6 ms: 1.19x faster                                                      |
| spectral_norm            | 77.3 ms                                                     | 66.5 ms: 1.16x faster                                                      |
| regex_dna                | 136 ms                                                      | 118 ms: 1.16x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.06 sec: 1.15x faster                                                     |
| pprint_safe_repr         | 592 ms                                                      | 516 ms: 1.15x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.69 sec: 1.14x faster                                                     |
| sympy_str                | 194 ms                                                      | 172 ms: 1.13x faster                                                       |
| nqueens                  | 66.6 ms                                                     | 59.9 ms: 1.11x faster                                                      |
| 2to3                     | 246 ms                                                      | 221 ms: 1.11x faster                                                       |
| coroutines               | 16.0 ms                                                     | 14.4 ms: 1.11x faster                                                      |
| regex_v8                 | 15.4 ms                                                     | 14.2 ms: 1.09x faster                                                      |
| xml_etree_parse          | 96.8 ms                                                     | 88.8 ms: 1.09x faster                                                      |
| xml_etree_generate       | 55.5 ms                                                     | 51.1 ms: 1.09x faster                                                      |
| sympy_expand             | 314 ms                                                      | 296 ms: 1.06x faster                                                       |
| fannkuch                 | 256 ms                                                      | 243 ms: 1.05x faster                                                       |
| regex_effbot             | 1.66 ms                                                     | 1.60 ms: 1.04x faster                                                      |
| meteor_contest           | 75.9 ms                                                     | 73.5 ms: 1.03x faster                                                      |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.8 ms: 1.02x faster                                                      |
| json                     | 3.14 ms                                                     | 3.10 ms: 1.01x faster                                                      |
| logging_simple           | 6.22 us                                                     | 6.38 us: 1.03x slower                                                      |
| logging_format           | 6.76 us                                                     | 6.95 us: 1.03x slower                                                      |
| json_loads               | 14.0 us                                                     | 14.5 us: 1.03x slower                                                      |
| async_generators         | 222 ms                                                      | 242 ms: 1.09x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.36 ms: 1.11x slower                                                      |
| python_startup_no_site   | 15.5 ms                                                     | 19.4 ms: 1.25x slower                                                      |
| python_startup           | 20.6 ms                                                     | 26.2 ms: 1.27x slower                                                      |
| coverage                 | 39.0 ms                                                     | 51.8 ms: 1.33x slower                                                      |
| gc_traversal             | 1.41 ms                                                     | 2.22 ms: 1.57x slower                                                      |
| create_gc_cycles         | 800 us                                                      | 1.32 ms: 1.66x slower                                                      |
| logging_silent           | 94.6 ns                                                     | 319 ns: 3.37x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.27x faster                                                               |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250619-3.15.0a0-9731dd2-JIT/bm-20250619-pythonperf1-amd64-python-9731dd2c8df3509095ea-3.15.0a0-9731dd2.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.298x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: unknown