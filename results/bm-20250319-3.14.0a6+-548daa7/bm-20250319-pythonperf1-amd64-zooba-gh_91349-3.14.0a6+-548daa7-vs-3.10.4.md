# Results vs. 3.10.4

- fork: zooba
- ref: gh_91349
- machine: windows-amd64
- commit hash: 548daa7
- commit date: 2025-03-19
- overall geometric mean: 1.201x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 230 ms: 1.07x faster                                           |
| docutils       | 1.92 sec                                                    | 1.71 sec: 1.12x faster                                         |
| html5lib       | 51.0 ms                                                     | 41.8 ms: 1.22x faster                                          |
| Geometric mean | (ref)                                                       | 1.14x faster                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6+-548daa7 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 430 ms: 2.58x faster                                           |
| async_tree_memoization  | 526 ms                                                      | 224 ms: 2.35x faster                                           |
| async_tree_none         | 435 ms                                                      | 192 ms: 2.27x faster                                           |
| async_tree_cpu_io_mixed | 638 ms                                                      | 347 ms: 1.84x faster                                           |
| Geometric mean          | (ref)                                                       | 2.24x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 46.8 ms: 1.32x faster                                          |
| nbody          | 71.3 ms                                                     | 72.9 ms: 1.02x slower                                          |
| Geometric mean | (ref)                                                       | 1.09x faster                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 89.0 ms: 1.19x faster                                          |
| regex_dna      | 136 ms                                                      | 117 ms: 1.16x faster                                           |
| regex_effbot   | 1.66 ms                                                     | 1.44 ms: 1.15x faster                                          |
| regex_v8       | 15.4 ms                                                     | 13.9 ms: 1.11x faster                                          |
| Geometric mean | (ref)                                                       | 1.15x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6+-548daa7 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.99 ms: 1.31x faster                                          |
| unpickle_pure_python | 183 us                                                      | 152 us: 1.20x faster                                           |
| pickle_pure_python   | 270 us                                                      | 236 us: 1.14x faster                                           |
| tomli_loads          | 1.67 sec                                                    | 1.49 sec: 1.12x faster                                         |
| xml_etree_parse      | 96.8 ms                                                     | 90.3 ms: 1.07x faster                                          |
| xml_etree_process    | 44.5 ms                                                     | 42.3 ms: 1.05x faster                                          |
| xml_etree_generate   | 55.5 ms                                                     | 58.9 ms: 1.06x slower                                          |
| json_loads           | 14.0 us                                                     | 15.4 us: 1.10x slower                                          |
| Geometric mean       | (ref)                                                       | 1.08x faster                                                   |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6+-548daa7 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 26.4 ms: 1.28x slower                                          |
| python_startup_no_site | 15.5 ms                                                     | 20.4 ms: 1.32x slower                                          |
| Geometric mean         | (ref)                                                       | 1.30x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6+-548daa7 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.86 ms: 1.32x faster                                          |
| genshi_text     | 19.8 ms                                                     | 17.3 ms: 1.14x faster                                          |
| django_template | 28.9 ms                                                     | 26.7 ms: 1.08x faster                                          |
| genshi_xml      | 41.0 ms                                                     | 38.1 ms: 1.08x faster                                          |
| Geometric mean  | (ref)                                                       | 1.15x faster                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6+-548daa7 |
|--------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 114 us: 2.96x faster                                           |
| async_tree_io            | 1.11 sec                                                    | 430 ms: 2.58x faster                                           |
| async_tree_memoization   | 526 ms                                                      | 224 ms: 2.35x faster                                           |
| pathlib                  | 75.7 ms                                                     | 32.8 ms: 2.30x faster                                          |
| async_tree_none          | 435 ms                                                      | 192 ms: 2.27x faster                                           |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 347 ms: 1.84x faster                                           |
| deltablue                | 4.19 ms                                                     | 2.28 ms: 1.84x faster                                          |
| pylint                   | 350 ms                                                      | 205 ms: 1.71x faster                                           |
| generators               | 32.4 ms                                                     | 19.3 ms: 1.68x faster                                          |
| logging_silent           | 94.6 ns                                                     | 59.2 ns: 1.60x faster                                          |
| richards_super           | 52.2 ms                                                     | 33.9 ms: 1.54x faster                                          |
| go                       | 139 ms                                                      | 90.4 ms: 1.54x faster                                          |
| deepcopy_memo            | 28.8 us                                                     | 19.7 us: 1.46x faster                                          |
| scimark_lu               | 85.8 ms                                                     | 61.4 ms: 1.40x faster                                          |
| chaos                    | 61.7 ms                                                     | 44.4 ms: 1.39x faster                                          |
| richards                 | 42.4 ms                                                     | 30.8 ms: 1.38x faster                                          |
| deepcopy                 | 255 us                                                      | 187 us: 1.37x faster                                           |
| comprehensions           | 16.5 us                                                     | 12.1 us: 1.36x faster                                          |
| raytrace                 | 273 ms                                                      | 204 ms: 1.34x faster                                           |
| spectral_norm            | 77.3 ms                                                     | 57.9 ms: 1.33x faster                                          |
| float                    | 61.7 ms                                                     | 46.8 ms: 1.32x faster                                          |
| mako                     | 9.03 ms                                                     | 6.86 ms: 1.32x faster                                          |
| json_dumps               | 9.16 ms                                                     | 6.99 ms: 1.31x faster                                          |
| scimark_monte_carlo      | 57.3 ms                                                     | 43.9 ms: 1.31x faster                                          |
| hexiom                   | 5.74 ms                                                     | 4.48 ms: 1.28x faster                                          |
| pyflate                  | 409 ms                                                      | 321 ms: 1.28x faster                                           |
| scimark_sor              | 106 ms                                                      | 84.7 ms: 1.25x faster                                          |
| crypto_pyaes             | 62.5 ms                                                     | 49.9 ms: 1.25x faster                                          |
| html5lib                 | 51.0 ms                                                     | 41.8 ms: 1.22x faster                                          |
| pycparser                | 930 ms                                                      | 765 ms: 1.22x faster                                           |
| unpickle_pure_python     | 183 us                                                      | 152 us: 1.20x faster                                           |
| sqlite_synth             | 1.91 us                                                     | 1.60 us: 1.20x faster                                          |
| regex_compile            | 106 ms                                                      | 89.0 ms: 1.19x faster                                          |
| coroutines               | 16.0 ms                                                     | 13.5 ms: 1.19x faster                                          |
| sympy_sum                | 107 ms                                                      | 91.1 ms: 1.17x faster                                          |
| dulwich_log              | 50.5 ms                                                     | 43.1 ms: 1.17x faster                                          |
| regex_dna                | 136 ms                                                      | 117 ms: 1.16x faster                                           |
| mdp                      | 1.78 sec                                                    | 1.54 sec: 1.16x faster                                         |
| regex_effbot             | 1.66 ms                                                     | 1.44 ms: 1.15x faster                                          |
| pickle_pure_python       | 270 us                                                      | 236 us: 1.14x faster                                           |
| genshi_text              | 19.8 ms                                                     | 17.3 ms: 1.14x faster                                          |
| thrift                   | 617 us                                                      | 541 us: 1.14x faster                                           |
| sympy_integrate          | 15.3 ms                                                     | 13.4 ms: 1.14x faster                                          |
| docutils                 | 1.92 sec                                                    | 1.71 sec: 1.12x faster                                         |
| tomli_loads              | 1.67 sec                                                    | 1.49 sec: 1.12x faster                                         |
| regex_v8                 | 15.4 ms                                                     | 13.9 ms: 1.11x faster                                          |
| bench_thread_pool        | 958 us                                                      | 869 us: 1.10x faster                                           |
| deepcopy_reduce          | 2.20 us                                                     | 2.00 us: 1.10x faster                                          |
| pprint_pformat           | 1.22 sec                                                    | 1.11 sec: 1.10x faster                                         |
| sympy_str                | 194 ms                                                      | 179 ms: 1.08x faster                                           |
| django_template          | 28.9 ms                                                     | 26.7 ms: 1.08x faster                                          |
| pprint_safe_repr         | 592 ms                                                      | 548 ms: 1.08x faster                                           |
| genshi_xml               | 41.0 ms                                                     | 38.1 ms: 1.08x faster                                          |
| xml_etree_parse          | 96.8 ms                                                     | 90.3 ms: 1.07x faster                                          |
| 2to3                     | 246 ms                                                      | 230 ms: 1.07x faster                                           |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.55 ms: 1.07x faster                                          |
| xml_etree_process        | 44.5 ms                                                     | 42.3 ms: 1.05x faster                                          |
| sympy_expand             | 314 ms                                                      | 308 ms: 1.02x faster                                           |
| json                     | 3.14 ms                                                     | 3.11 ms: 1.01x faster                                          |
| nqueens                  | 66.6 ms                                                     | 67.8 ms: 1.02x slower                                          |
| nbody                    | 71.3 ms                                                     | 72.9 ms: 1.02x slower                                          |
| meteor_contest           | 75.9 ms                                                     | 77.8 ms: 1.02x slower                                          |
| async_generators         | 222 ms                                                      | 232 ms: 1.05x slower                                           |
| xml_etree_generate       | 55.5 ms                                                     | 58.9 ms: 1.06x slower                                          |
| logging_format           | 6.76 us                                                     | 7.22 us: 1.07x slower                                          |
| logging_simple           | 6.22 us                                                     | 6.66 us: 1.07x slower                                          |
| fannkuch                 | 256 ms                                                      | 275 ms: 1.08x slower                                           |
| json_loads               | 14.0 us                                                     | 15.4 us: 1.10x slower                                          |
| coverage                 | 39.0 ms                                                     | 49.1 ms: 1.26x slower                                          |
| telco                    | 3.94 ms                                                     | 5.03 ms: 1.28x slower                                          |
| python_startup           | 20.6 ms                                                     | 26.4 ms: 1.28x slower                                          |
| python_startup_no_site   | 15.5 ms                                                     | 20.4 ms: 1.32x slower                                          |
| bench_mp_pool            | 62.0 ms                                                     | 89.3 ms: 1.44x slower                                          |
| gc_traversal             | 1.41 ms                                                     | 2.08 ms: 1.47x slower                                          |
| create_gc_cycles         | 800 us                                                      | 1.23 ms: 1.54x slower                                          |
| Geometric mean           | (ref)                                                       | 1.19x faster                                                   |

Benchmark hidden because not significant (3): scimark_fft, pidigits, xml_etree_iterparse
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250319-3.14.0a6+-548daa7/bm-20250319-pythonperf1-amd64-zooba-gh_91349-3.14.0a6+-548daa7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.201x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown