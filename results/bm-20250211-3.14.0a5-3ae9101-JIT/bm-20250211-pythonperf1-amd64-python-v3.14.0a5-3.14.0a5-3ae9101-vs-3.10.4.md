# Results vs. 3.10.4

- fork: python
- ref: v3.14.0a5
- machine: windows-amd64
- commit hash: 3ae9101
- commit date: 2025-02-11
- overall geometric mean: 1.248x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.14x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250211-pythonperf1-amd64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 222 ms: 1.11x faster                                            |
| docutils       | 1.92 sec                                                    | 1.75 sec: 1.09x faster                                          |
| html5lib       | 51.0 ms                                                     | 37.7 ms: 1.35x faster                                           |
| Geometric mean | (ref)                                                       | 1.18x faster                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250211-pythonperf1-amd64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 417 ms: 2.66x faster                                            |
| async_tree_memoization  | 526 ms                                                      | 224 ms: 2.35x faster                                            |
| async_tree_none         | 435 ms                                                      | 189 ms: 2.31x faster                                            |
| async_tree_cpu_io_mixed | 638 ms                                                      | 341 ms: 1.87x faster                                            |
| Geometric mean          | (ref)                                                       | 2.28x faster                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250211-pythonperf1-amd64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 48.4 ms: 1.28x faster                                           |
| nbody          | 71.3 ms                                                     | 60.5 ms: 1.18x faster                                           |
| pidigits       | 149 ms                                                      | 150 ms: 1.01x slower                                            |
| Geometric mean | (ref)                                                       | 1.14x faster                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250211-pythonperf1-amd64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 81.0 ms: 1.31x faster                                           |
| regex_dna      | 136 ms                                                      | 114 ms: 1.19x faster                                            |
| regex_effbot   | 1.66 ms                                                     | 1.42 ms: 1.16x faster                                           |
| regex_v8       | 15.4 ms                                                     | 14.7 ms: 1.05x faster                                           |
| Geometric mean | (ref)                                                       | 1.18x faster                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250211-pythonperf1-amd64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 115 us: 1.60x faster                                            |
| tomli_loads          | 1.67 sec                                                    | 1.18 sec: 1.42x faster                                          |
| json_dumps           | 9.16 ms                                                     | 6.66 ms: 1.37x faster                                           |
| pickle_pure_python   | 270 us                                                      | 211 us: 1.28x faster                                            |
| xml_etree_process    | 44.5 ms                                                     | 36.7 ms: 1.21x faster                                           |
| xml_etree_generate   | 55.5 ms                                                     | 51.1 ms: 1.09x faster                                           |
| xml_etree_parse      | 96.8 ms                                                     | 90.5 ms: 1.07x faster                                           |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.0 ms: 1.06x faster                                           |
| json_loads           | 14.0 us                                                     | 16.2 us: 1.15x slower                                           |
| Geometric mean       | (ref)                                                       | 1.20x faster                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250211-pythonperf1-amd64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 25.1 ms: 1.22x slower                                           |
| python_startup_no_site | 15.5 ms                                                     | 18.9 ms: 1.22x slower                                           |
| Geometric mean         | (ref)                                                       | 1.22x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250211-pythonperf1-amd64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.26 ms: 1.72x faster                                           |
| genshi_text     | 19.8 ms                                                     | 16.7 ms: 1.19x faster                                           |
| django_template | 28.9 ms                                                     | 25.5 ms: 1.13x faster                                           |
| genshi_xml      | 41.0 ms                                                     | 36.4 ms: 1.13x faster                                           |
| Geometric mean  | (ref)                                                       | 1.27x faster                                                    |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250211-pythonperf1-amd64-python-v3.14.0a5-3.14.0a5-3ae9101 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 110 us: 3.05x faster                                            |
| async_tree_io            | 1.11 sec                                                    | 417 ms: 2.66x faster                                            |
| pathlib                  | 75.7 ms                                                     | 29.5 ms: 2.57x faster                                           |
| async_tree_memoization   | 526 ms                                                      | 224 ms: 2.35x faster                                            |
| async_tree_none          | 435 ms                                                      | 189 ms: 2.31x faster                                            |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 341 ms: 1.87x faster                                            |
| deltablue                | 4.19 ms                                                     | 2.42 ms: 1.73x faster                                           |
| pylint                   | 350 ms                                                      | 203 ms: 1.73x faster                                            |
| mako                     | 9.03 ms                                                     | 5.26 ms: 1.72x faster                                           |
| unpickle_pure_python     | 183 us                                                      | 115 us: 1.60x faster                                            |
| generators               | 32.4 ms                                                     | 20.4 ms: 1.59x faster                                           |
| go                       | 139 ms                                                      | 88.1 ms: 1.58x faster                                           |
| pyflate                  | 409 ms                                                      | 278 ms: 1.47x faster                                            |
| chaos                    | 61.7 ms                                                     | 42.2 ms: 1.46x faster                                           |
| sqlglot_parse            | 1.22 ms                                                     | 839 us: 1.45x faster                                            |
| richards_super           | 52.2 ms                                                     | 36.2 ms: 1.44x faster                                           |
| comprehensions           | 16.5 us                                                     | 11.5 us: 1.44x faster                                           |
| logging_silent           | 94.6 ns                                                     | 66.1 ns: 1.43x faster                                           |
| tomli_loads              | 1.67 sec                                                    | 1.18 sec: 1.42x faster                                          |
| sqlglot_transpile        | 1.48 ms                                                     | 1.07 ms: 1.38x faster                                           |
| json_dumps               | 9.16 ms                                                     | 6.66 ms: 1.37x faster                                           |
| crypto_pyaes             | 62.5 ms                                                     | 45.9 ms: 1.36x faster                                           |
| deepcopy                 | 255 us                                                      | 188 us: 1.36x faster                                            |
| html5lib                 | 51.0 ms                                                     | 37.7 ms: 1.35x faster                                           |
| deepcopy_memo            | 28.8 us                                                     | 21.3 us: 1.35x faster                                           |
| pycparser                | 930 ms                                                      | 706 ms: 1.32x faster                                            |
| raytrace                 | 273 ms                                                      | 208 ms: 1.32x faster                                            |
| regex_compile            | 106 ms                                                      | 81.0 ms: 1.31x faster                                           |
| richards                 | 42.4 ms                                                     | 32.5 ms: 1.31x faster                                           |
| scimark_lu               | 85.8 ms                                                     | 66.1 ms: 1.30x faster                                           |
| pickle_pure_python       | 270 us                                                      | 211 us: 1.28x faster                                            |
| float                    | 61.7 ms                                                     | 48.4 ms: 1.28x faster                                           |
| scimark_fft              | 187 ms                                                      | 148 ms: 1.27x faster                                            |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.15 ms: 1.27x faster                                           |
| dulwich_log              | 50.5 ms                                                     | 39.8 ms: 1.27x faster                                           |
| hexiom                   | 5.74 ms                                                     | 4.54 ms: 1.27x faster                                           |
| sqlite_synth             | 1.91 us                                                     | 1.53 us: 1.25x faster                                           |
| spectral_norm            | 77.3 ms                                                     | 62.3 ms: 1.24x faster                                           |
| thrift                   | 617 us                                                      | 498 us: 1.24x faster                                            |
| scimark_monte_carlo      | 57.3 ms                                                     | 46.6 ms: 1.23x faster                                           |
| pprint_pformat           | 1.22 sec                                                    | 995 ms: 1.22x faster                                            |
| xml_etree_process        | 44.5 ms                                                     | 36.7 ms: 1.21x faster                                           |
| regex_dna                | 136 ms                                                      | 114 ms: 1.19x faster                                            |
| genshi_text              | 19.8 ms                                                     | 16.7 ms: 1.19x faster                                           |
| sympy_sum                | 107 ms                                                      | 90.1 ms: 1.19x faster                                           |
| mdp                      | 1.78 sec                                                    | 1.51 sec: 1.18x faster                                          |
| nbody                    | 71.3 ms                                                     | 60.5 ms: 1.18x faster                                           |
| pprint_safe_repr         | 592 ms                                                      | 506 ms: 1.17x faster                                            |
| regex_effbot             | 1.66 ms                                                     | 1.42 ms: 1.16x faster                                           |
| scimark_sor              | 106 ms                                                      | 92.5 ms: 1.15x faster                                           |
| django_template          | 28.9 ms                                                     | 25.5 ms: 1.13x faster                                           |
| genshi_xml               | 41.0 ms                                                     | 36.4 ms: 1.13x faster                                           |
| fannkuch                 | 256 ms                                                      | 229 ms: 1.12x faster                                            |
| deepcopy_reduce          | 2.20 us                                                     | 1.97 us: 1.12x faster                                           |
| bench_thread_pool        | 958 us                                                      | 858 us: 1.12x faster                                            |
| sympy_str                | 194 ms                                                      | 175 ms: 1.11x faster                                            |
| 2to3                     | 246 ms                                                      | 222 ms: 1.11x faster                                            |
| sympy_integrate          | 15.3 ms                                                     | 13.8 ms: 1.10x faster                                           |
| docutils                 | 1.92 sec                                                    | 1.75 sec: 1.09x faster                                          |
| xml_etree_generate       | 55.5 ms                                                     | 51.1 ms: 1.09x faster                                           |
| coroutines               | 16.0 ms                                                     | 14.9 ms: 1.07x faster                                           |
| xml_etree_parse          | 96.8 ms                                                     | 90.5 ms: 1.07x faster                                           |
| sqlglot_optimize         | 39.8 ms                                                     | 37.3 ms: 1.07x faster                                           |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.0 ms: 1.06x faster                                           |
| nqueens                  | 66.6 ms                                                     | 63.0 ms: 1.06x faster                                           |
| regex_v8                 | 15.4 ms                                                     | 14.7 ms: 1.05x faster                                           |
| sympy_expand             | 314 ms                                                      | 303 ms: 1.04x faster                                            |
| sqlglot_normalize        | 205 ms                                                      | 203 ms: 1.01x faster                                            |
| pidigits                 | 149 ms                                                      | 150 ms: 1.01x slower                                            |
| meteor_contest           | 75.9 ms                                                     | 77.0 ms: 1.01x slower                                           |
| logging_format           | 6.76 us                                                     | 6.88 us: 1.02x slower                                           |
| json                     | 3.14 ms                                                     | 3.22 ms: 1.03x slower                                           |
| logging_simple           | 6.22 us                                                     | 6.48 us: 1.04x slower                                           |
| telco                    | 3.94 ms                                                     | 4.39 ms: 1.11x slower                                           |
| async_generators         | 222 ms                                                      | 251 ms: 1.13x slower                                            |
| json_loads               | 14.0 us                                                     | 16.2 us: 1.15x slower                                           |
| python_startup           | 20.6 ms                                                     | 25.1 ms: 1.22x slower                                           |
| python_startup_no_site   | 15.5 ms                                                     | 18.9 ms: 1.22x slower                                           |
| coverage                 | 39.0 ms                                                     | 48.2 ms: 1.24x slower                                           |
| bench_mp_pool            | 62.0 ms                                                     | 84.2 ms: 1.36x slower                                           |
| gc_traversal             | 1.41 ms                                                     | 1.99 ms: 1.41x slower                                           |
| create_gc_cycles         | 800 us                                                      | 1.21 ms: 1.52x slower                                           |
| Geometric mean           | (ref)                                                       | 1.24x faster                                                    |
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250211-3.14.0a5-3ae9101-JIT/bm-20250211-pythonperf1-amd64-python-v3.14.0a5-3.14.0a5-3ae9101.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.248x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.14x

# Memory
- memory change: unknown