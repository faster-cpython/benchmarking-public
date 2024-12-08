# Results vs. 3.10.4

- fork: python
- ref: 79b7cab50a3292a1c014
- machine: windows-amd64
- commit hash: 79b7cab
- commit date: 2024-12-07
- overall geometric mean: 1.176x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 224 ms: 1.10x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.66 sec: 1.16x faster                                                      |
| html5lib       | 51.0 ms                                                     | 40.4 ms: 1.26x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 407 ms: 2.73x faster                                                        |
| async_tree_none         | 435 ms                                                      | 185 ms: 2.36x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 230 ms: 2.29x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 361 ms: 1.77x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.26x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 54.8 ms: 1.13x faster                                                       |
| pidigits       | 149 ms                                                      | 147 ms: 1.01x faster                                                        |
| nbody          | 71.3 ms                                                     | 76.5 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 89.9 ms: 1.18x faster                                                       |
| regex_dna      | 136 ms                                                      | 119 ms: 1.15x faster                                                        |
| regex_effbot   | 1.66 ms                                                     | 1.53 ms: 1.08x faster                                                       |
| regex_v8       | 15.4 ms                                                     | 26.0 ms: 1.69x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 7.18 ms: 1.28x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 227 us: 1.19x faster                                                        |
| unpickle_pure_python | 183 us                                                      | 157 us: 1.17x faster                                                        |
| xml_etree_process    | 44.5 ms                                                     | 41.5 ms: 1.07x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 90.6 ms: 1.07x faster                                                       |
| tomli_loads          | 1.67 sec                                                    | 1.59 sec: 1.05x faster                                                      |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.6 ms: 1.02x faster                                                       |
| xml_etree_generate   | 55.5 ms                                                     | 58.5 ms: 1.05x slower                                                       |
| json_loads           | 14.0 us                                                     | 15.3 us: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 17.5 ms: 1.13x slower                                                       |
| python_startup         | 20.6 ms                                                     | 23.4 ms: 1.14x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.13x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.15 ms: 1.26x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 16.9 ms: 1.17x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 36.3 ms: 1.13x faster                                                       |
| django_template | 28.9 ms                                                     | 25.7 ms: 1.13x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.17x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 112 us: 3.01x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 407 ms: 2.73x faster                                                        |
| async_tree_none          | 435 ms                                                      | 185 ms: 2.36x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 230 ms: 2.29x faster                                                        |
| pylint                   | 350 ms                                                      | 191 ms: 1.84x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.32 ms: 1.81x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 361 ms: 1.77x faster                                                        |
| go                       | 139 ms                                                      | 87.6 ms: 1.59x faster                                                       |
| generators               | 32.4 ms                                                     | 21.9 ms: 1.48x faster                                                       |
| richards_super           | 52.2 ms                                                     | 36.1 ms: 1.45x faster                                                       |
| chaos                    | 61.7 ms                                                     | 42.9 ms: 1.44x faster                                                       |
| raytrace                 | 273 ms                                                      | 193 ms: 1.42x faster                                                        |
| logging_silent           | 94.6 ns                                                     | 67.3 ns: 1.41x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 20.9 us: 1.37x faster                                                       |
| comprehensions           | 16.5 us                                                     | 12.1 us: 1.36x faster                                                       |
| sqlglot_parse            | 1.22 ms                                                     | 903 us: 1.35x faster                                                        |
| deepcopy                 | 255 us                                                      | 192 us: 1.33x faster                                                        |
| sqlglot_transpile        | 1.48 ms                                                     | 1.12 ms: 1.31x faster                                                       |
| richards                 | 42.4 ms                                                     | 32.4 ms: 1.31x faster                                                       |
| crypto_pyaes             | 62.5 ms                                                     | 47.8 ms: 1.31x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 66.2 ms: 1.30x faster                                                       |
| pycparser                | 930 ms                                                      | 722 ms: 1.29x faster                                                        |
| json_dumps               | 9.16 ms                                                     | 7.18 ms: 1.28x faster                                                       |
| hexiom                   | 5.74 ms                                                     | 4.52 ms: 1.27x faster                                                       |
| pyflate                  | 409 ms                                                      | 323 ms: 1.26x faster                                                        |
| html5lib                 | 51.0 ms                                                     | 40.4 ms: 1.26x faster                                                       |
| mako                     | 9.03 ms                                                     | 7.15 ms: 1.26x faster                                                       |
| mdp                      | 1.78 sec                                                    | 1.47 sec: 1.21x faster                                                      |
| scimark_monte_carlo      | 57.3 ms                                                     | 48.1 ms: 1.19x faster                                                       |
| sympy_sum                | 107 ms                                                      | 90.0 ms: 1.19x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 227 us: 1.19x faster                                                        |
| regex_compile            | 106 ms                                                      | 89.9 ms: 1.18x faster                                                       |
| bench_thread_pool        | 958 us                                                      | 812 us: 1.18x faster                                                        |
| thrift                   | 617 us                                                      | 526 us: 1.17x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.63 us: 1.17x faster                                                       |
| dulwich_log              | 50.5 ms                                                     | 43.0 ms: 1.17x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 16.9 ms: 1.17x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 157 us: 1.17x faster                                                        |
| deepcopy_reduce          | 2.20 us                                                     | 1.90 us: 1.16x faster                                                       |
| scimark_sor              | 106 ms                                                      | 91.8 ms: 1.16x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.66 sec: 1.16x faster                                                      |
| regex_dna                | 136 ms                                                      | 119 ms: 1.15x faster                                                        |
| coroutines               | 16.0 ms                                                     | 14.0 ms: 1.14x faster                                                       |
| sympy_integrate          | 15.3 ms                                                     | 13.4 ms: 1.14x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 36.3 ms: 1.13x faster                                                       |
| float                    | 61.7 ms                                                     | 54.8 ms: 1.13x faster                                                       |
| django_template          | 28.9 ms                                                     | 25.7 ms: 1.13x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 69.1 ms: 1.12x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.11 sec: 1.10x faster                                                      |
| 2to3                     | 246 ms                                                      | 224 ms: 1.10x faster                                                        |
| sympy_str                | 194 ms                                                      | 179 ms: 1.09x faster                                                        |
| regex_effbot             | 1.66 ms                                                     | 1.53 ms: 1.08x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 41.5 ms: 1.07x faster                                                       |
| pprint_safe_repr         | 592 ms                                                      | 553 ms: 1.07x faster                                                        |
| xml_etree_parse          | 96.8 ms                                                     | 90.6 ms: 1.07x faster                                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 37.3 ms: 1.07x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.59 sec: 1.05x faster                                                      |
| nqueens                  | 66.6 ms                                                     | 64.3 ms: 1.04x faster                                                       |
| sympy_expand             | 314 ms                                                      | 307 ms: 1.02x faster                                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.6 ms: 1.02x faster                                                       |
| pathlib                  | 75.7 ms                                                     | 74.6 ms: 1.01x faster                                                       |
| pidigits                 | 149 ms                                                      | 147 ms: 1.01x faster                                                        |
| logging_simple           | 6.22 us                                                     | 6.32 us: 1.02x slower                                                       |
| meteor_contest           | 75.9 ms                                                     | 77.2 ms: 1.02x slower                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.80 ms: 1.03x slower                                                       |
| json                     | 3.14 ms                                                     | 3.23 ms: 1.03x slower                                                       |
| xml_etree_generate       | 55.5 ms                                                     | 58.5 ms: 1.05x slower                                                       |
| nbody                    | 71.3 ms                                                     | 76.5 ms: 1.07x slower                                                       |
| json_loads               | 14.0 us                                                     | 15.3 us: 1.09x slower                                                       |
| scimark_fft              | 187 ms                                                      | 205 ms: 1.09x slower                                                        |
| fannkuch                 | 256 ms                                                      | 282 ms: 1.10x slower                                                        |
| async_generators         | 222 ms                                                      | 244 ms: 1.10x slower                                                        |
| python_startup_no_site   | 15.5 ms                                                     | 17.5 ms: 1.13x slower                                                       |
| python_startup           | 20.6 ms                                                     | 23.4 ms: 1.14x slower                                                       |
| coverage                 | 39.0 ms                                                     | 45.5 ms: 1.17x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.75 ms: 1.21x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 81.6 ms: 1.31x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 1.92 ms: 1.36x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.09 ms: 1.37x slower                                                       |
| regex_v8                 | 15.4 ms                                                     | 26.0 ms: 1.69x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.17x faster                                                                |

Benchmark hidden because not significant (2): sqlglot_normalize, logging_format
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241207-3.14.0a2+-79b7cab/bm-20241207-pythonperf1-amd64-python-79b7cab50a3292a1c014-3.14.0a2+-79b7cab.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.176x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: unknown