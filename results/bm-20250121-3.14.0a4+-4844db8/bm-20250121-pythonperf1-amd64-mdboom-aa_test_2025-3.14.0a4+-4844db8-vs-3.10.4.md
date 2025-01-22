# Results vs. 3.10.4

- fork: mdboom
- ref: aa_test_2025
- machine: windows-amd64
- commit hash: 4844db8
- commit date: 2025-01-21
- overall geometric mean: 1.183x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-pythonperf1-amd64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 232 ms: 1.06x faster                                                |
| docutils       | 1.92 sec                                                    | 1.69 sec: 1.14x faster                                              |
| html5lib       | 51.0 ms                                                     | 40.6 ms: 1.26x faster                                               |
| Geometric mean | (ref)                                                       | 1.15x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-pythonperf1-amd64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|-------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 414 ms: 2.68x faster                                                |
| async_tree_none         | 435 ms                                                      | 186 ms: 2.34x faster                                                |
| async_tree_memoization  | 526 ms                                                      | 226 ms: 2.33x faster                                                |
| async_tree_cpu_io_mixed | 638 ms                                                      | 348 ms: 1.83x faster                                                |
| Geometric mean          | (ref)                                                       | 2.27x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-pythonperf1-amd64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 51.6 ms: 1.20x faster                                               |
| pidigits       | 149 ms                                                      | 146 ms: 1.02x faster                                                |
| nbody          | 71.3 ms                                                     | 74.5 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                       | 1.05x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-pythonperf1-amd64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 87.9 ms: 1.21x faster                                               |
| regex_dna      | 136 ms                                                      | 115 ms: 1.19x faster                                                |
| regex_effbot   | 1.66 ms                                                     | 1.47 ms: 1.13x faster                                               |
| regex_v8       | 15.4 ms                                                     | 14.8 ms: 1.05x faster                                               |
| Geometric mean | (ref)                                                       | 1.14x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-pythonperf1-amd64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.89 ms: 1.33x faster                                               |
| tomli_loads          | 1.67 sec                                                    | 1.40 sec: 1.19x faster                                              |
| unpickle_pure_python | 183 us                                                      | 162 us: 1.13x faster                                                |
| pickle_pure_python   | 270 us                                                      | 238 us: 1.13x faster                                                |
| xml_etree_parse      | 96.8 ms                                                     | 89.4 ms: 1.08x faster                                               |
| xml_etree_process    | 44.5 ms                                                     | 43.3 ms: 1.03x faster                                               |
| json_loads           | 14.0 us                                                     | 14.4 us: 1.03x slower                                               |
| xml_etree_generate   | 55.5 ms                                                     | 60.3 ms: 1.09x slower                                               |
| Geometric mean       | (ref)                                                       | 1.08x faster                                                        |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-pythonperf1-amd64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 18.2 ms: 1.17x slower                                               |
| python_startup         | 20.6 ms                                                     | 24.4 ms: 1.19x slower                                               |
| Geometric mean         | (ref)                                                       | 1.18x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-pythonperf1-amd64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.97 ms: 1.30x faster                                               |
| genshi_text     | 19.8 ms                                                     | 16.5 ms: 1.20x faster                                               |
| genshi_xml      | 41.0 ms                                                     | 35.7 ms: 1.15x faster                                               |
| django_template | 28.9 ms                                                     | 25.9 ms: 1.11x faster                                               |
| Geometric mean  | (ref)                                                       | 1.19x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250121-pythonperf1-amd64-mdboom-aa_test_2025-3.14.0a4+-4844db8 |
|--------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 115 us: 2.91x faster                                                |
| async_tree_io            | 1.11 sec                                                    | 414 ms: 2.68x faster                                                |
| async_tree_none          | 435 ms                                                      | 186 ms: 2.34x faster                                                |
| async_tree_memoization   | 526 ms                                                      | 226 ms: 2.33x faster                                                |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 348 ms: 1.83x faster                                                |
| deltablue                | 4.19 ms                                                     | 2.37 ms: 1.77x faster                                               |
| pylint                   | 350 ms                                                      | 202 ms: 1.74x faster                                                |
| go                       | 139 ms                                                      | 88.3 ms: 1.57x faster                                               |
| generators               | 32.4 ms                                                     | 21.5 ms: 1.51x faster                                               |
| chaos                    | 61.7 ms                                                     | 42.9 ms: 1.44x faster                                               |
| richards_super           | 52.2 ms                                                     | 36.3 ms: 1.44x faster                                               |
| deepcopy_memo            | 28.8 us                                                     | 20.3 us: 1.42x faster                                               |
| sqlglot_parse            | 1.22 ms                                                     | 891 us: 1.36x faster                                                |
| logging_silent           | 94.6 ns                                                     | 69.9 ns: 1.35x faster                                               |
| deepcopy                 | 255 us                                                      | 189 us: 1.35x faster                                                |
| sqlglot_transpile        | 1.48 ms                                                     | 1.10 ms: 1.34x faster                                               |
| json_dumps               | 9.16 ms                                                     | 6.89 ms: 1.33x faster                                               |
| comprehensions           | 16.5 us                                                     | 12.6 us: 1.31x faster                                               |
| richards                 | 42.4 ms                                                     | 32.3 ms: 1.31x faster                                               |
| pyflate                  | 409 ms                                                      | 312 ms: 1.31x faster                                                |
| mako                     | 9.03 ms                                                     | 6.97 ms: 1.30x faster                                               |
| crypto_pyaes             | 62.5 ms                                                     | 48.7 ms: 1.28x faster                                               |
| raytrace                 | 273 ms                                                      | 214 ms: 1.28x faster                                                |
| pycparser                | 930 ms                                                      | 736 ms: 1.26x faster                                                |
| html5lib                 | 51.0 ms                                                     | 40.6 ms: 1.26x faster                                               |
| hexiom                   | 5.74 ms                                                     | 4.60 ms: 1.25x faster                                               |
| scimark_lu               | 85.8 ms                                                     | 69.8 ms: 1.23x faster                                               |
| spectral_norm            | 77.3 ms                                                     | 63.7 ms: 1.21x faster                                               |
| regex_compile            | 106 ms                                                      | 87.9 ms: 1.21x faster                                               |
| genshi_text              | 19.8 ms                                                     | 16.5 ms: 1.20x faster                                               |
| sqlite_synth             | 1.91 us                                                     | 1.60 us: 1.20x faster                                               |
| float                    | 61.7 ms                                                     | 51.6 ms: 1.20x faster                                               |
| tomli_loads              | 1.67 sec                                                    | 1.40 sec: 1.19x faster                                              |
| thrift                   | 617 us                                                      | 519 us: 1.19x faster                                                |
| regex_dna                | 136 ms                                                      | 115 ms: 1.19x faster                                                |
| scimark_sor              | 106 ms                                                      | 89.6 ms: 1.19x faster                                               |
| dulwich_log              | 50.5 ms                                                     | 42.6 ms: 1.18x faster                                               |
| sympy_sum                | 107 ms                                                      | 91.2 ms: 1.17x faster                                               |
| deepcopy_reduce          | 2.20 us                                                     | 1.89 us: 1.17x faster                                               |
| genshi_xml               | 41.0 ms                                                     | 35.7 ms: 1.15x faster                                               |
| scimark_monte_carlo      | 57.3 ms                                                     | 49.9 ms: 1.15x faster                                               |
| mdp                      | 1.78 sec                                                    | 1.56 sec: 1.14x faster                                              |
| docutils                 | 1.92 sec                                                    | 1.69 sec: 1.14x faster                                              |
| unpickle_pure_python     | 183 us                                                      | 162 us: 1.13x faster                                                |
| pickle_pure_python       | 270 us                                                      | 238 us: 1.13x faster                                                |
| regex_effbot             | 1.66 ms                                                     | 1.47 ms: 1.13x faster                                               |
| sympy_integrate          | 15.3 ms                                                     | 13.6 ms: 1.12x faster                                               |
| bench_thread_pool        | 958 us                                                      | 856 us: 1.12x faster                                                |
| pprint_pformat           | 1.22 sec                                                    | 1.09 sec: 1.12x faster                                              |
| django_template          | 28.9 ms                                                     | 25.9 ms: 1.11x faster                                               |
| pprint_safe_repr         | 592 ms                                                      | 535 ms: 1.11x faster                                                |
| sqlglot_optimize         | 39.8 ms                                                     | 36.3 ms: 1.10x faster                                               |
| coroutines               | 16.0 ms                                                     | 14.8 ms: 1.08x faster                                               |
| xml_etree_parse          | 96.8 ms                                                     | 89.4 ms: 1.08x faster                                               |
| sympy_str                | 194 ms                                                      | 180 ms: 1.08x faster                                                |
| json                     | 3.14 ms                                                     | 2.93 ms: 1.07x faster                                               |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.56 ms: 1.06x faster                                               |
| 2to3                     | 246 ms                                                      | 232 ms: 1.06x faster                                                |
| regex_v8                 | 15.4 ms                                                     | 14.8 ms: 1.05x faster                                               |
| sqlglot_normalize        | 205 ms                                                      | 197 ms: 1.04x faster                                                |
| xml_etree_process        | 44.5 ms                                                     | 43.3 ms: 1.03x faster                                               |
| nqueens                  | 66.6 ms                                                     | 65.2 ms: 1.02x faster                                               |
| pidigits                 | 149 ms                                                      | 146 ms: 1.02x faster                                                |
| sympy_expand             | 314 ms                                                      | 310 ms: 1.01x faster                                                |
| logging_format           | 6.76 us                                                     | 6.81 us: 1.01x slower                                               |
| json_loads               | 14.0 us                                                     | 14.4 us: 1.03x slower                                               |
| logging_simple           | 6.22 us                                                     | 6.43 us: 1.03x slower                                               |
| pathlib                  | 75.7 ms                                                     | 78.3 ms: 1.03x slower                                               |
| async_generators         | 222 ms                                                      | 231 ms: 1.04x slower                                                |
| nbody                    | 71.3 ms                                                     | 74.5 ms: 1.04x slower                                               |
| scimark_fft              | 187 ms                                                      | 198 ms: 1.05x slower                                                |
| fannkuch                 | 256 ms                                                      | 277 ms: 1.08x slower                                                |
| xml_etree_generate       | 55.5 ms                                                     | 60.3 ms: 1.09x slower                                               |
| python_startup_no_site   | 15.5 ms                                                     | 18.2 ms: 1.17x slower                                               |
| python_startup           | 20.6 ms                                                     | 24.4 ms: 1.19x slower                                               |
| telco                    | 3.94 ms                                                     | 4.81 ms: 1.22x slower                                               |
| coverage                 | 39.0 ms                                                     | 48.3 ms: 1.24x slower                                               |
| gc_traversal             | 1.41 ms                                                     | 1.99 ms: 1.41x slower                                               |
| bench_mp_pool            | 62.0 ms                                                     | 88.2 ms: 1.42x slower                                               |
| create_gc_cycles         | 800 us                                                      | 1.21 ms: 1.51x slower                                               |
| Geometric mean           | (ref)                                                       | 1.18x faster                                                        |

Benchmark hidden because not significant (2): xml_etree_iterparse, meteor_contest
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250121-3.14.0a4+-4844db8/bm-20250121-pythonperf1-amd64-mdboom-aa_test_2025-3.14.0a4+-4844db8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.183x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown