# Results vs. 3.10.4

- fork: mdboom
- ref: aa_test_2025_2
- machine: windows-amd64
- commit hash: 8ffb2c1
- commit date: 2025-01-23
- overall geometric mean: 1.186x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.09x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf1-amd64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 233 ms: 1.06x faster                                                  |
| docutils       | 1.92 sec                                                    | 1.70 sec: 1.13x faster                                                |
| html5lib       | 51.0 ms                                                     | 40.7 ms: 1.25x faster                                                 |
| Geometric mean | (ref)                                                       | 1.14x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf1-amd64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 413 ms: 2.69x faster                                                  |
| async_tree_none         | 435 ms                                                      | 186 ms: 2.34x faster                                                  |
| async_tree_memoization  | 526 ms                                                      | 226 ms: 2.33x faster                                                  |
| async_tree_cpu_io_mixed | 638 ms                                                      | 347 ms: 1.84x faster                                                  |
| Geometric mean          | (ref)                                                       | 2.28x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf1-amd64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 51.4 ms: 1.20x faster                                                 |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                  |
| nbody          | 71.3 ms                                                     | 77.3 ms: 1.08x slower                                                 |
| Geometric mean | (ref)                                                       | 1.04x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf1-amd64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 88.2 ms: 1.20x faster                                                 |
| regex_dna      | 136 ms                                                      | 117 ms: 1.16x faster                                                  |
| regex_effbot   | 1.66 ms                                                     | 1.46 ms: 1.13x faster                                                 |
| regex_v8       | 15.4 ms                                                     | 16.5 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                       | 1.10x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf1-amd64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.82 ms: 1.34x faster                                                 |
| tomli_loads          | 1.67 sec                                                    | 1.39 sec: 1.21x faster                                                |
| unpickle_pure_python | 183 us                                                      | 159 us: 1.16x faster                                                  |
| pickle_pure_python   | 270 us                                                      | 239 us: 1.13x faster                                                  |
| xml_etree_parse      | 96.8 ms                                                     | 88.5 ms: 1.09x faster                                                 |
| xml_etree_process    | 44.5 ms                                                     | 43.7 ms: 1.02x faster                                                 |
| json_loads           | 14.0 us                                                     | 14.5 us: 1.03x slower                                                 |
| xml_etree_generate   | 55.5 ms                                                     | 59.4 ms: 1.07x slower                                                 |
| Geometric mean       | (ref)                                                       | 1.09x faster                                                          |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf1-amd64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 18.0 ms: 1.16x slower                                                 |
| python_startup         | 20.6 ms                                                     | 24.3 ms: 1.18x slower                                                 |
| Geometric mean         | (ref)                                                       | 1.17x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf1-amd64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.89 ms: 1.31x faster                                                 |
| genshi_text     | 19.8 ms                                                     | 16.6 ms: 1.19x faster                                                 |
| genshi_xml      | 41.0 ms                                                     | 35.1 ms: 1.17x faster                                                 |
| django_template | 28.9 ms                                                     | 25.9 ms: 1.11x faster                                                 |
| Geometric mean  | (ref)                                                       | 1.19x faster                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250123-pythonperf1-amd64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 111 us: 3.02x faster                                                  |
| async_tree_io            | 1.11 sec                                                    | 413 ms: 2.69x faster                                                  |
| async_tree_none          | 435 ms                                                      | 186 ms: 2.34x faster                                                  |
| async_tree_memoization   | 526 ms                                                      | 226 ms: 2.33x faster                                                  |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 347 ms: 1.84x faster                                                  |
| deltablue                | 4.19 ms                                                     | 2.38 ms: 1.76x faster                                                 |
| pylint                   | 350 ms                                                      | 202 ms: 1.74x faster                                                  |
| go                       | 139 ms                                                      | 88.5 ms: 1.57x faster                                                 |
| generators               | 32.4 ms                                                     | 21.6 ms: 1.50x faster                                                 |
| chaos                    | 61.7 ms                                                     | 41.7 ms: 1.48x faster                                                 |
| richards_super           | 52.2 ms                                                     | 35.8 ms: 1.46x faster                                                 |
| deepcopy_memo            | 28.8 us                                                     | 20.0 us: 1.44x faster                                                 |
| deepcopy                 | 255 us                                                      | 184 us: 1.39x faster                                                  |
| sqlglot_parse            | 1.22 ms                                                     | 890 us: 1.36x faster                                                  |
| json_dumps               | 9.16 ms                                                     | 6.82 ms: 1.34x faster                                                 |
| sqlglot_transpile        | 1.48 ms                                                     | 1.10 ms: 1.34x faster                                                 |
| richards                 | 42.4 ms                                                     | 31.8 ms: 1.33x faster                                                 |
| comprehensions           | 16.5 us                                                     | 12.4 us: 1.33x faster                                                 |
| scimark_lu               | 85.8 ms                                                     | 64.9 ms: 1.32x faster                                                 |
| pyflate                  | 409 ms                                                      | 310 ms: 1.32x faster                                                  |
| mako                     | 9.03 ms                                                     | 6.89 ms: 1.31x faster                                                 |
| logging_silent           | 94.6 ns                                                     | 72.5 ns: 1.31x faster                                                 |
| raytrace                 | 273 ms                                                      | 209 ms: 1.31x faster                                                  |
| crypto_pyaes             | 62.5 ms                                                     | 48.0 ms: 1.30x faster                                                 |
| hexiom                   | 5.74 ms                                                     | 4.54 ms: 1.27x faster                                                 |
| pycparser                | 930 ms                                                      | 737 ms: 1.26x faster                                                  |
| html5lib                 | 51.0 ms                                                     | 40.7 ms: 1.25x faster                                                 |
| spectral_norm            | 77.3 ms                                                     | 63.4 ms: 1.22x faster                                                 |
| scimark_monte_carlo      | 57.3 ms                                                     | 47.3 ms: 1.21x faster                                                 |
| scimark_sor              | 106 ms                                                      | 87.8 ms: 1.21x faster                                                 |
| tomli_loads              | 1.67 sec                                                    | 1.39 sec: 1.21x faster                                                |
| regex_compile            | 106 ms                                                      | 88.2 ms: 1.20x faster                                                 |
| float                    | 61.7 ms                                                     | 51.4 ms: 1.20x faster                                                 |
| genshi_text              | 19.8 ms                                                     | 16.6 ms: 1.19x faster                                                 |
| dulwich_log              | 50.5 ms                                                     | 42.5 ms: 1.19x faster                                                 |
| deepcopy_reduce          | 2.20 us                                                     | 1.86 us: 1.19x faster                                                 |
| thrift                   | 617 us                                                      | 524 us: 1.18x faster                                                  |
| sympy_sum                | 107 ms                                                      | 91.3 ms: 1.17x faster                                                 |
| genshi_xml               | 41.0 ms                                                     | 35.1 ms: 1.17x faster                                                 |
| regex_dna                | 136 ms                                                      | 117 ms: 1.16x faster                                                  |
| unpickle_pure_python     | 183 us                                                      | 159 us: 1.16x faster                                                  |
| bench_thread_pool        | 958 us                                                      | 834 us: 1.15x faster                                                  |
| mdp                      | 1.78 sec                                                    | 1.56 sec: 1.14x faster                                                |
| regex_effbot             | 1.66 ms                                                     | 1.46 ms: 1.13x faster                                                 |
| docutils                 | 1.92 sec                                                    | 1.70 sec: 1.13x faster                                                |
| pickle_pure_python       | 270 us                                                      | 239 us: 1.13x faster                                                  |
| sympy_integrate          | 15.3 ms                                                     | 13.6 ms: 1.12x faster                                                 |
| django_template          | 28.9 ms                                                     | 25.9 ms: 1.11x faster                                                 |
| pprint_pformat           | 1.22 sec                                                    | 1.10 sec: 1.11x faster                                                |
| pprint_safe_repr         | 592 ms                                                      | 536 ms: 1.10x faster                                                  |
| sqlite_synth             | 1.91 us                                                     | 1.74 us: 1.10x faster                                                 |
| xml_etree_parse          | 96.8 ms                                                     | 88.5 ms: 1.09x faster                                                 |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.50 ms: 1.09x faster                                                 |
| sympy_str                | 194 ms                                                      | 179 ms: 1.09x faster                                                  |
| sqlglot_optimize         | 39.8 ms                                                     | 36.7 ms: 1.08x faster                                                 |
| json                     | 3.14 ms                                                     | 2.95 ms: 1.06x faster                                                 |
| 2to3                     | 246 ms                                                      | 233 ms: 1.06x faster                                                  |
| coroutines               | 16.0 ms                                                     | 15.3 ms: 1.05x faster                                                 |
| sqlglot_normalize        | 205 ms                                                      | 199 ms: 1.03x faster                                                  |
| nqueens                  | 66.6 ms                                                     | 64.6 ms: 1.03x faster                                                 |
| sympy_expand             | 314 ms                                                      | 305 ms: 1.03x faster                                                  |
| xml_etree_process        | 44.5 ms                                                     | 43.7 ms: 1.02x faster                                                 |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                  |
| meteor_contest           | 75.9 ms                                                     | 75.5 ms: 1.01x faster                                                 |
| async_generators         | 222 ms                                                      | 225 ms: 1.02x slower                                                  |
| pathlib                  | 75.7 ms                                                     | 77.9 ms: 1.03x slower                                                 |
| logging_format           | 6.76 us                                                     | 6.99 us: 1.03x slower                                                 |
| json_loads               | 14.0 us                                                     | 14.5 us: 1.03x slower                                                 |
| logging_simple           | 6.22 us                                                     | 6.53 us: 1.05x slower                                                 |
| fannkuch                 | 256 ms                                                      | 269 ms: 1.05x slower                                                  |
| regex_v8                 | 15.4 ms                                                     | 16.5 ms: 1.07x slower                                                 |
| xml_etree_generate       | 55.5 ms                                                     | 59.4 ms: 1.07x slower                                                 |
| nbody                    | 71.3 ms                                                     | 77.3 ms: 1.08x slower                                                 |
| python_startup_no_site   | 15.5 ms                                                     | 18.0 ms: 1.16x slower                                                 |
| python_startup           | 20.6 ms                                                     | 24.3 ms: 1.18x slower                                                 |
| coverage                 | 39.0 ms                                                     | 49.4 ms: 1.27x slower                                                 |
| telco                    | 3.94 ms                                                     | 5.44 ms: 1.38x slower                                                 |
| bench_mp_pool            | 62.0 ms                                                     | 88.0 ms: 1.42x slower                                                 |
| gc_traversal             | 1.41 ms                                                     | 2.00 ms: 1.42x slower                                                 |
| create_gc_cycles         | 800 us                                                      | 1.22 ms: 1.52x slower                                                 |
| Geometric mean           | (ref)                                                       | 1.18x faster                                                          |

Benchmark hidden because not significant (2): scimark_fft, xml_etree_iterparse
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250123-3.14.0a4+-8ffb2c1/bm-20250123-pythonperf1-amd64-mdboom-aa_test_2025_2-3.14.0a4+-8ffb2c1.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.186x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.11x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.09x

# Memory
- memory change: unknown