# Results vs. 3.10.4

- fork: python
- ref: v3.13.0
- machine: windows-amd64
- commit hash: 60403a5
- commit date: 2024-10-07
- overall geometric mean: 1.222x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 215 ms: 1.14x faster                                        |
| chameleon      | 5.79 ms                                                     | 4.74 ms: 1.22x faster                                       |
| docutils       | 1.92 sec                                                    | 1.53 sec: 1.25x faster                                      |
| html5lib       | 51.0 ms                                                     | 38.2 ms: 1.34x faster                                       |
| tornado_http   | 108 ms                                                      | 81.2 ms: 1.33x faster                                       |
| Geometric mean | (ref)                                                       | 1.26x faster                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|-------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 513 ms: 2.16x faster                                        |
| async_tree_memoization  | 526 ms                                                      | 265 ms: 1.99x faster                                        |
| async_tree_none         | 435 ms                                                      | 219 ms: 1.99x faster                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 380 ms: 1.68x faster                                        |
| Geometric mean          | (ref)                                                       | 1.95x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 61.7 ms                                                     | 50.8 ms: 1.21x faster                                       |
| nbody          | 71.3 ms                                                     | 66.3 ms: 1.08x faster                                       |
| pidigits       | 149 ms                                                      | 146 ms: 1.02x faster                                        |
| Geometric mean | (ref)                                                       | 1.10x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 80.7 ms: 1.31x faster                                       |
| regex_dna      | 136 ms                                                      | 115 ms: 1.18x faster                                        |
| regex_effbot   | 1.66 ms                                                     | 1.69 ms: 1.02x slower                                       |
| regex_v8       | 15.4 ms                                                     | 23.8 ms: 1.54x slower                                       |
| Geometric mean | (ref)                                                       | 1.00x slower                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 6.19 ms: 1.48x faster                                       |
| pickle_pure_python   | 270 us                                                      | 186 us: 1.45x faster                                        |
| unpickle_pure_python | 183 us                                                      | 130 us: 1.41x faster                                        |
| tomli_loads          | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                      |
| xml_etree_process    | 44.5 ms                                                     | 36.5 ms: 1.22x faster                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 60.5 ms: 1.07x faster                                       |
| xml_etree_parse      | 96.8 ms                                                     | 92.2 ms: 1.05x faster                                       |
| xml_etree_generate   | 55.5 ms                                                     | 53.5 ms: 1.04x faster                                       |
| json_loads           | 14.0 us                                                     | 15.1 us: 1.08x slower                                       |
| Geometric mean       | (ref)                                                       | 1.19x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 16.9 ms: 1.09x slower                                       |
| python_startup         | 20.6 ms                                                     | 24.4 ms: 1.18x slower                                       |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| django_template | 28.9 ms                                                     | 20.3 ms: 1.42x faster                                       |
| mako            | 9.03 ms                                                     | 6.56 ms: 1.38x faster                                       |
| genshi_text     | 19.8 ms                                                     | 15.2 ms: 1.30x faster                                       |
| genshi_xml      | 41.0 ms                                                     | 33.9 ms: 1.21x faster                                       |
| Geometric mean  | (ref)                                                       | 1.33x faster                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5 |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 103 us: 3.26x faster                                        |
| deltablue                | 4.19 ms                                                     | 1.89 ms: 2.21x faster                                       |
| async_tree_io            | 1.11 sec                                                    | 513 ms: 2.16x faster                                        |
| async_tree_memoization   | 526 ms                                                      | 265 ms: 1.99x faster                                        |
| async_tree_none          | 435 ms                                                      | 219 ms: 1.99x faster                                        |
| raytrace                 | 273 ms                                                      | 153 ms: 1.78x faster                                        |
| richards_super           | 52.2 ms                                                     | 29.8 ms: 1.75x faster                                       |
| logging_silent           | 94.6 ns                                                     | 54.6 ns: 1.73x faster                                       |
| generators               | 32.4 ms                                                     | 19.0 ms: 1.71x faster                                       |
| pylint                   | 350 ms                                                      | 205 ms: 1.71x faster                                        |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 380 ms: 1.68x faster                                        |
| go                       | 139 ms                                                      | 84.7 ms: 1.64x faster                                       |
| chaos                    | 61.7 ms                                                     | 37.9 ms: 1.63x faster                                       |
| richards                 | 42.4 ms                                                     | 26.3 ms: 1.62x faster                                       |
| comprehensions           | 16.5 us                                                     | 10.4 us: 1.59x faster                                       |
| sqlglot_parse            | 1.22 ms                                                     | 764 us: 1.59x faster                                        |
| sqlglot_transpile        | 1.48 ms                                                     | 953 us: 1.55x faster                                        |
| scimark_lu               | 85.8 ms                                                     | 56.7 ms: 1.51x faster                                       |
| hexiom                   | 5.74 ms                                                     | 3.84 ms: 1.49x faster                                       |
| json_dumps               | 9.16 ms                                                     | 6.19 ms: 1.48x faster                                       |
| pickle_pure_python       | 270 us                                                      | 186 us: 1.45x faster                                        |
| pyflate                  | 409 ms                                                      | 283 ms: 1.45x faster                                        |
| django_template          | 28.9 ms                                                     | 20.3 ms: 1.42x faster                                       |
| unpickle_pure_python     | 183 us                                                      | 130 us: 1.41x faster                                        |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.7 ms: 1.41x faster                                       |
| scimark_sor              | 106 ms                                                      | 76.2 ms: 1.39x faster                                       |
| mako                     | 9.03 ms                                                     | 6.56 ms: 1.38x faster                                       |
| crypto_pyaes             | 62.5 ms                                                     | 45.6 ms: 1.37x faster                                       |
| pycparser                | 930 ms                                                      | 695 ms: 1.34x faster                                        |
| html5lib                 | 51.0 ms                                                     | 38.2 ms: 1.34x faster                                       |
| sqlalchemy_declarative   | 103 ms                                                      | 77.4 ms: 1.34x faster                                       |
| tornado_http             | 108 ms                                                      | 81.2 ms: 1.33x faster                                       |
| regex_compile            | 106 ms                                                      | 80.7 ms: 1.31x faster                                       |
| genshi_text              | 19.8 ms                                                     | 15.2 ms: 1.30x faster                                       |
| coroutines               | 16.0 ms                                                     | 12.5 ms: 1.28x faster                                       |
| dulwich_log              | 50.5 ms                                                     | 40.1 ms: 1.26x faster                                       |
| sympy_sum                | 107 ms                                                      | 85.2 ms: 1.26x faster                                       |
| docutils                 | 1.92 sec                                                    | 1.53 sec: 1.25x faster                                      |
| pprint_pformat           | 1.22 sec                                                    | 977 ms: 1.25x faster                                        |
| deepcopy_memo            | 28.8 us                                                     | 23.1 us: 1.25x faster                                       |
| mdp                      | 1.78 sec                                                    | 1.43 sec: 1.24x faster                                      |
| sympy_integrate          | 15.3 ms                                                     | 12.3 ms: 1.24x faster                                       |
| sqlalchemy_imperative    | 11.4 ms                                                     | 9.30 ms: 1.23x faster                                       |
| sqlglot_optimize         | 39.8 ms                                                     | 32.5 ms: 1.22x faster                                       |
| chameleon                | 5.79 ms                                                     | 4.74 ms: 1.22x faster                                       |
| pprint_safe_repr         | 592 ms                                                      | 485 ms: 1.22x faster                                        |
| tomli_loads              | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                      |
| spectral_norm            | 77.3 ms                                                     | 63.4 ms: 1.22x faster                                       |
| xml_etree_process        | 44.5 ms                                                     | 36.5 ms: 1.22x faster                                       |
| float                    | 61.7 ms                                                     | 50.8 ms: 1.21x faster                                       |
| genshi_xml               | 41.0 ms                                                     | 33.9 ms: 1.21x faster                                       |
| sqlite_synth             | 1.91 us                                                     | 1.59 us: 1.21x faster                                       |
| sqlglot_normalize        | 205 ms                                                      | 172 ms: 1.20x faster                                        |
| nqueens                  | 66.6 ms                                                     | 56.1 ms: 1.19x faster                                       |
| regex_dna                | 136 ms                                                      | 115 ms: 1.18x faster                                        |
| bench_thread_pool        | 958 us                                                      | 810 us: 1.18x faster                                        |
| sympy_str                | 194 ms                                                      | 167 ms: 1.17x faster                                        |
| deepcopy                 | 255 us                                                      | 223 us: 1.14x faster                                        |
| 2to3                     | 246 ms                                                      | 215 ms: 1.14x faster                                        |
| sympy_expand             | 314 ms                                                      | 286 ms: 1.10x faster                                        |
| logging_format           | 6.76 us                                                     | 6.18 us: 1.09x faster                                       |
| deepcopy_reduce          | 2.20 us                                                     | 2.02 us: 1.09x faster                                       |
| logging_simple           | 6.22 us                                                     | 5.77 us: 1.08x faster                                       |
| nbody                    | 71.3 ms                                                     | 66.3 ms: 1.08x faster                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 60.5 ms: 1.07x faster                                       |
| scimark_fft              | 187 ms                                                      | 175 ms: 1.07x faster                                        |
| meteor_contest           | 75.9 ms                                                     | 72.0 ms: 1.06x faster                                       |
| xml_etree_parse          | 96.8 ms                                                     | 92.2 ms: 1.05x faster                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.60 ms: 1.05x faster                                       |
| xml_etree_generate       | 55.5 ms                                                     | 53.5 ms: 1.04x faster                                       |
| pidigits                 | 149 ms                                                      | 146 ms: 1.02x faster                                        |
| fannkuch                 | 256 ms                                                      | 252 ms: 1.02x faster                                        |
| async_generators         | 222 ms                                                      | 223 ms: 1.01x slower                                        |
| regex_effbot             | 1.66 ms                                                     | 1.69 ms: 1.02x slower                                       |
| json                     | 3.14 ms                                                     | 3.30 ms: 1.05x slower                                       |
| json_loads               | 14.0 us                                                     | 15.1 us: 1.08x slower                                       |
| python_startup_no_site   | 15.5 ms                                                     | 16.9 ms: 1.09x slower                                       |
| coverage                 | 39.0 ms                                                     | 45.3 ms: 1.16x slower                                       |
| python_startup           | 20.6 ms                                                     | 24.4 ms: 1.18x slower                                       |
| telco                    | 3.94 ms                                                     | 4.85 ms: 1.23x slower                                       |
| bench_mp_pool            | 62.0 ms                                                     | 84.2 ms: 1.36x slower                                       |
| gc_traversal             | 1.41 ms                                                     | 1.96 ms: 1.39x slower                                       |
| create_gc_cycles         | 800 us                                                      | 1.22 ms: 1.53x slower                                       |
| regex_v8                 | 15.4 ms                                                     | 23.8 ms: 1.54x slower                                       |
| thrift                   | 617 us                                                      | 8.47 ms: 13.71x slower                                      |
| Geometric mean           | (ref)                                                       | 1.21x faster                                                |

Benchmark hidden because not significant (1): pathlib
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20241007-3.13.0-60403a5/bm-20241007-pythonperf1-amd64-python-v3.13.0-3.13.0-60403a5.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.222x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: unknown