# Results vs. 3.10.4

- fork: python
- ref: v3.13.2
- machine: windows-amd64
- commit hash: 4f8bb39
- commit date: 2025-02-04
- overall geometric mean: 1.230x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.20x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-pythonperf1-amd64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 217 ms: 1.13x faster                                        |
| chameleon      | 5.79 ms                                                     | 4.72 ms: 1.23x faster                                       |
| docutils       | 1.92 sec                                                    | 1.54 sec: 1.25x faster                                      |
| html5lib       | 51.0 ms                                                     | 37.8 ms: 1.35x faster                                       |
| tornado_http   | 108 ms                                                      | 100 ms: 1.08x faster                                        |
| Geometric mean | (ref)                                                       | 1.20x faster                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-pythonperf1-amd64-python-v3.13.2-3.13.2-4f8bb39 |
|-------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 519 ms: 2.14x faster                                        |
| async_tree_memoization  | 526 ms                                                      | 270 ms: 1.95x faster                                        |
| async_tree_none         | 435 ms                                                      | 224 ms: 1.94x faster                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 381 ms: 1.67x faster                                        |
| Geometric mean          | (ref)                                                       | 1.92x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-pythonperf1-amd64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| float          | 61.7 ms                                                     | 47.7 ms: 1.29x faster                                       |
| nbody          | 71.3 ms                                                     | 65.1 ms: 1.10x faster                                       |
| pidigits       | 149 ms                                                      | 147 ms: 1.01x faster                                        |
| Geometric mean | (ref)                                                       | 1.13x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-pythonperf1-amd64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 79.8 ms: 1.33x faster                                       |
| regex_dna      | 136 ms                                                      | 113 ms: 1.20x faster                                        |
| regex_effbot   | 1.66 ms                                                     | 1.41 ms: 1.17x faster                                       |
| regex_v8       | 15.4 ms                                                     | 15.0 ms: 1.03x faster                                       |
| Geometric mean | (ref)                                                       | 1.18x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-pythonperf1-amd64-python-v3.13.2-3.13.2-4f8bb39 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 9.16 ms                                                     | 5.84 ms: 1.57x faster                                       |
| pickle_pure_python   | 270 us                                                      | 189 us: 1.42x faster                                        |
| unpickle_pure_python | 183 us                                                      | 130 us: 1.41x faster                                        |
| xml_etree_process    | 44.5 ms                                                     | 36.4 ms: 1.22x faster                                       |
| tomli_loads          | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                      |
| xml_etree_parse      | 96.8 ms                                                     | 91.4 ms: 1.06x faster                                       |
| xml_etree_generate   | 55.5 ms                                                     | 53.8 ms: 1.03x faster                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.5 ms: 1.02x faster                                       |
| json_loads           | 14.0 us                                                     | 14.5 us: 1.04x slower                                       |
| Geometric mean       | (ref)                                                       | 1.20x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-pythonperf1-amd64-python-v3.13.2-3.13.2-4f8bb39 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 18.6 ms: 1.20x slower                                       |
| python_startup         | 20.6 ms                                                     | 26.5 ms: 1.28x slower                                       |
| Geometric mean         | (ref)                                                       | 1.24x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-pythonperf1-amd64-python-v3.13.2-3.13.2-4f8bb39 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| django_template | 28.9 ms                                                     | 19.9 ms: 1.45x faster                                       |
| mako            | 9.03 ms                                                     | 6.35 ms: 1.42x faster                                       |
| genshi_text     | 19.8 ms                                                     | 15.1 ms: 1.31x faster                                       |
| genshi_xml      | 41.0 ms                                                     | 32.6 ms: 1.26x faster                                       |
| Geometric mean  | (ref)                                                       | 1.36x faster                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250204-pythonperf1-amd64-python-v3.13.2-3.13.2-4f8bb39 |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 104 us: 3.25x faster                                        |
| deltablue                | 4.19 ms                                                     | 1.89 ms: 2.21x faster                                       |
| async_tree_io            | 1.11 sec                                                    | 519 ms: 2.14x faster                                        |
| async_tree_memoization   | 526 ms                                                      | 270 ms: 1.95x faster                                        |
| async_tree_none          | 435 ms                                                      | 224 ms: 1.94x faster                                        |
| generators               | 32.4 ms                                                     | 18.2 ms: 1.78x faster                                       |
| raytrace                 | 273 ms                                                      | 156 ms: 1.76x faster                                        |
| logging_silent           | 94.6 ns                                                     | 55.0 ns: 1.72x faster                                       |
| richards_super           | 52.2 ms                                                     | 30.5 ms: 1.71x faster                                       |
| chaos                    | 61.7 ms                                                     | 36.8 ms: 1.68x faster                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 381 ms: 1.67x faster                                        |
| pylint                   | 350 ms                                                      | 213 ms: 1.65x faster                                        |
| go                       | 139 ms                                                      | 85.4 ms: 1.63x faster                                       |
| sqlglot_parse            | 1.22 ms                                                     | 757 us: 1.60x faster                                        |
| comprehensions           | 16.5 us                                                     | 10.5 us: 1.57x faster                                       |
| richards                 | 42.4 ms                                                     | 27.0 ms: 1.57x faster                                       |
| json_dumps               | 9.16 ms                                                     | 5.84 ms: 1.57x faster                                       |
| sqlglot_transpile        | 1.48 ms                                                     | 955 us: 1.55x faster                                        |
| hexiom                   | 5.74 ms                                                     | 3.79 ms: 1.51x faster                                       |
| scimark_lu               | 85.8 ms                                                     | 58.3 ms: 1.47x faster                                       |
| django_template          | 28.9 ms                                                     | 19.9 ms: 1.45x faster                                       |
| pyflate                  | 409 ms                                                      | 284 ms: 1.44x faster                                        |
| pickle_pure_python       | 270 us                                                      | 189 us: 1.42x faster                                        |
| mako                     | 9.03 ms                                                     | 6.35 ms: 1.42x faster                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.3 ms: 1.42x faster                                       |
| unpickle_pure_python     | 183 us                                                      | 130 us: 1.41x faster                                        |
| crypto_pyaes             | 62.5 ms                                                     | 44.8 ms: 1.40x faster                                       |
| scimark_sor              | 106 ms                                                      | 77.2 ms: 1.37x faster                                       |
| pycparser                | 930 ms                                                      | 687 ms: 1.35x faster                                        |
| html5lib                 | 51.0 ms                                                     | 37.8 ms: 1.35x faster                                       |
| regex_compile            | 106 ms                                                      | 79.8 ms: 1.33x faster                                       |
| sqlalchemy_declarative   | 103 ms                                                      | 78.8 ms: 1.31x faster                                       |
| genshi_text              | 19.8 ms                                                     | 15.1 ms: 1.31x faster                                       |
| float                    | 61.7 ms                                                     | 47.7 ms: 1.29x faster                                       |
| spectral_norm            | 77.3 ms                                                     | 60.4 ms: 1.28x faster                                       |
| genshi_xml               | 41.0 ms                                                     | 32.6 ms: 1.26x faster                                       |
| coroutines               | 16.0 ms                                                     | 12.7 ms: 1.26x faster                                       |
| mdp                      | 1.78 sec                                                    | 1.43 sec: 1.25x faster                                      |
| docutils                 | 1.92 sec                                                    | 1.54 sec: 1.25x faster                                      |
| sympy_sum                | 107 ms                                                      | 86.0 ms: 1.24x faster                                       |
| deepcopy_memo            | 28.8 us                                                     | 23.3 us: 1.23x faster                                       |
| sympy_integrate          | 15.3 ms                                                     | 12.4 ms: 1.23x faster                                       |
| sqlite_synth             | 1.91 us                                                     | 1.55 us: 1.23x faster                                       |
| pprint_pformat           | 1.22 sec                                                    | 994 ms: 1.23x faster                                        |
| chameleon                | 5.79 ms                                                     | 4.72 ms: 1.23x faster                                       |
| pathlib                  | 75.7 ms                                                     | 61.8 ms: 1.22x faster                                       |
| dulwich_log              | 50.5 ms                                                     | 41.3 ms: 1.22x faster                                       |
| xml_etree_process        | 44.5 ms                                                     | 36.4 ms: 1.22x faster                                       |
| tomli_loads              | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                      |
| sqlglot_optimize         | 39.8 ms                                                     | 32.8 ms: 1.21x faster                                       |
| pprint_safe_repr         | 592 ms                                                      | 488 ms: 1.21x faster                                        |
| sqlglot_normalize        | 205 ms                                                      | 171 ms: 1.20x faster                                        |
| regex_dna                | 136 ms                                                      | 113 ms: 1.20x faster                                        |
| sqlalchemy_imperative    | 11.4 ms                                                     | 9.52 ms: 1.20x faster                                       |
| sympy_str                | 194 ms                                                      | 166 ms: 1.17x faster                                        |
| regex_effbot             | 1.66 ms                                                     | 1.41 ms: 1.17x faster                                       |
| nqueens                  | 66.6 ms                                                     | 57.1 ms: 1.17x faster                                       |
| bench_thread_pool        | 958 us                                                      | 831 us: 1.15x faster                                        |
| 2to3                     | 246 ms                                                      | 217 ms: 1.13x faster                                        |
| deepcopy                 | 255 us                                                      | 228 us: 1.12x faster                                        |
| sympy_expand             | 314 ms                                                      | 281 ms: 1.12x faster                                        |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.46 ms: 1.11x faster                                       |
| nbody                    | 71.3 ms                                                     | 65.1 ms: 1.10x faster                                       |
| logging_format           | 6.76 us                                                     | 6.21 us: 1.09x faster                                       |
| tornado_http             | 108 ms                                                      | 100 ms: 1.08x faster                                        |
| logging_simple           | 6.22 us                                                     | 5.79 us: 1.07x faster                                       |
| xml_etree_parse          | 96.8 ms                                                     | 91.4 ms: 1.06x faster                                       |
| meteor_contest           | 75.9 ms                                                     | 71.7 ms: 1.06x faster                                       |
| deepcopy_reduce          | 2.20 us                                                     | 2.09 us: 1.05x faster                                       |
| async_generators         | 222 ms                                                      | 211 ms: 1.05x faster                                        |
| fannkuch                 | 256 ms                                                      | 245 ms: 1.04x faster                                        |
| xml_etree_generate       | 55.5 ms                                                     | 53.8 ms: 1.03x faster                                       |
| regex_v8                 | 15.4 ms                                                     | 15.0 ms: 1.03x faster                                       |
| scimark_fft              | 187 ms                                                      | 183 ms: 1.02x faster                                        |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.5 ms: 1.02x faster                                       |
| pidigits                 | 149 ms                                                      | 147 ms: 1.01x faster                                        |
| json_loads               | 14.0 us                                                     | 14.5 us: 1.04x slower                                       |
| coverage                 | 39.0 ms                                                     | 45.8 ms: 1.17x slower                                       |
| python_startup_no_site   | 15.5 ms                                                     | 18.6 ms: 1.20x slower                                       |
| telco                    | 3.94 ms                                                     | 4.86 ms: 1.23x slower                                       |
| python_startup           | 20.6 ms                                                     | 26.5 ms: 1.28x slower                                       |
| bench_mp_pool            | 62.0 ms                                                     | 86.6 ms: 1.40x slower                                       |
| gc_traversal             | 1.41 ms                                                     | 1.97 ms: 1.40x slower                                       |
| create_gc_cycles         | 800 us                                                      | 1.26 ms: 1.57x slower                                       |
| thrift                   | 617 us                                                      | 8.01 ms: 12.97x slower                                      |
| Geometric mean           | (ref)                                                       | 1.22x faster                                                |

Benchmark hidden because not significant (1): json
Ignored benchmarks (12) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20250204-3.13.2-4f8bb39/bm-20250204-pythonperf1-amd64-python-v3.13.2-3.13.2-4f8bb39.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, djangocms, gevent_hub, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.230x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.22x
- 95% likely to have a speedup of 1.21x
- 99% likely to have a speedup of 1.20x

# Memory
- memory change: unknown