# Results vs. 3.10.4

- fork: python
- ref: 44e4c479fbf2c28605bd
- machine: windows-amd64
- commit hash: 44e4c47
- commit date: 2025-04-30
- overall geometric mean: 1.288x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.17x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-pythonperf1-amd64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 219 ms: 1.12x faster                                                        |
| docutils       | 1.92 sec                                                    | 1.64 sec: 1.17x faster                                                      |
| html5lib       | 51.0 ms                                                     | 37.4 ms: 1.37x faster                                                       |
| Geometric mean | (ref)                                                       | 1.22x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-pythonperf1-amd64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 412 ms: 2.69x faster                                                        |
| async_tree_memoization  | 526 ms                                                      | 206 ms: 2.56x faster                                                        |
| async_tree_none         | 435 ms                                                      | 181 ms: 2.40x faster                                                        |
| async_tree_cpu_io_mixed | 638 ms                                                      | 337 ms: 1.89x faster                                                        |
| Geometric mean          | (ref)                                                       | 2.36x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-pythonperf1-amd64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.5 ms: 1.42x faster                                                       |
| nbody          | 71.3 ms                                                     | 62.9 ms: 1.13x faster                                                       |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-pythonperf1-amd64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 79.8 ms: 1.33x faster                                                       |
| regex_effbot   | 1.66 ms                                                     | 1.46 ms: 1.13x faster                                                       |
| regex_dna      | 136 ms                                                      | 121 ms: 1.13x faster                                                        |
| regex_v8       | 15.4 ms                                                     | 14.8 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-pythonperf1-amd64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 132 us: 1.39x faster                                                        |
| json_dumps           | 9.16 ms                                                     | 6.83 ms: 1.34x faster                                                       |
| pickle_pure_python   | 270 us                                                      | 209 us: 1.29x faster                                                        |
| tomli_loads          | 1.67 sec                                                    | 1.38 sec: 1.21x faster                                                      |
| xml_etree_process    | 44.5 ms                                                     | 39.3 ms: 1.13x faster                                                       |
| xml_etree_parse      | 96.8 ms                                                     | 89.6 ms: 1.08x faster                                                       |
| xml_etree_iterparse  | 65.0 ms                                                     | 62.7 ms: 1.04x faster                                                       |
| json_loads           | 14.0 us                                                     | 15.3 us: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.15x faster                                                                |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-pythonperf1-amd64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.8 ms: 1.27x slower                                                       |
| python_startup         | 20.6 ms                                                     | 26.5 ms: 1.29x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.28x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-pythonperf1-amd64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 6.49 ms: 1.39x faster                                                       |
| genshi_text     | 19.8 ms                                                     | 15.0 ms: 1.32x faster                                                       |
| genshi_xml      | 41.0 ms                                                     | 33.6 ms: 1.22x faster                                                       |
| django_template | 28.9 ms                                                     | 24.2 ms: 1.20x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.28x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250430-pythonperf1-amd64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 109 us: 3.07x faster                                                        |
| async_tree_io            | 1.11 sec                                                    | 412 ms: 2.69x faster                                                        |
| async_tree_memoization   | 526 ms                                                      | 206 ms: 2.56x faster                                                        |
| async_tree_none          | 435 ms                                                      | 181 ms: 2.40x faster                                                        |
| pathlib                  | 75.7 ms                                                     | 32.6 ms: 2.32x faster                                                       |
| mdp                      | 1.78 sec                                                    | 790 ms: 2.25x faster                                                        |
| deltablue                | 4.19 ms                                                     | 2.08 ms: 2.01x faster                                                       |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 337 ms: 1.89x faster                                                        |
| go                       | 139 ms                                                      | 76.3 ms: 1.82x faster                                                       |
| pylint                   | 350 ms                                                      | 200 ms: 1.76x faster                                                        |
| logging_silent           | 94.6 ns                                                     | 55.1 ns: 1.72x faster                                                       |
| richards_super           | 52.2 ms                                                     | 30.7 ms: 1.70x faster                                                       |
| generators               | 32.4 ms                                                     | 19.6 ms: 1.66x faster                                                       |
| chaos                    | 61.7 ms                                                     | 38.7 ms: 1.60x faster                                                       |
| richards                 | 42.4 ms                                                     | 27.0 ms: 1.57x faster                                                       |
| deepcopy_memo            | 28.8 us                                                     | 18.4 us: 1.56x faster                                                       |
| scimark_lu               | 85.8 ms                                                     | 55.7 ms: 1.54x faster                                                       |
| raytrace                 | 273 ms                                                      | 178 ms: 1.54x faster                                                        |
| pyflate                  | 409 ms                                                      | 272 ms: 1.50x faster                                                        |
| comprehensions           | 16.5 us                                                     | 11.1 us: 1.49x faster                                                       |
| deepcopy                 | 255 us                                                      | 172 us: 1.48x faster                                                        |
| hexiom                   | 5.74 ms                                                     | 3.97 ms: 1.45x faster                                                       |
| scimark_sor              | 106 ms                                                      | 74.4 ms: 1.43x faster                                                       |
| float                    | 61.7 ms                                                     | 43.5 ms: 1.42x faster                                                       |
| scimark_monte_carlo      | 57.3 ms                                                     | 40.7 ms: 1.41x faster                                                       |
| unpickle_pure_python     | 183 us                                                      | 132 us: 1.39x faster                                                        |
| mako                     | 9.03 ms                                                     | 6.49 ms: 1.39x faster                                                       |
| html5lib                 | 51.0 ms                                                     | 37.4 ms: 1.37x faster                                                       |
| spectral_norm            | 77.3 ms                                                     | 57.2 ms: 1.35x faster                                                       |
| json_dumps               | 9.16 ms                                                     | 6.83 ms: 1.34x faster                                                       |
| regex_compile            | 106 ms                                                      | 79.8 ms: 1.33x faster                                                       |
| genshi_text              | 19.8 ms                                                     | 15.0 ms: 1.32x faster                                                       |
| pycparser                | 930 ms                                                      | 707 ms: 1.32x faster                                                        |
| crypto_pyaes             | 62.5 ms                                                     | 47.8 ms: 1.31x faster                                                       |
| pickle_pure_python       | 270 us                                                      | 209 us: 1.29x faster                                                        |
| sympy_integrate          | 15.3 ms                                                     | 12.5 ms: 1.22x faster                                                       |
| sqlite_synth             | 1.91 us                                                     | 1.56 us: 1.22x faster                                                       |
| genshi_xml               | 41.0 ms                                                     | 33.6 ms: 1.22x faster                                                       |
| sympy_sum                | 107 ms                                                      | 88.1 ms: 1.21x faster                                                       |
| tomli_loads              | 1.67 sec                                                    | 1.38 sec: 1.21x faster                                                      |
| deepcopy_reduce          | 2.20 us                                                     | 1.82 us: 1.21x faster                                                       |
| pprint_pformat           | 1.22 sec                                                    | 1.01 sec: 1.21x faster                                                      |
| pprint_safe_repr         | 592 ms                                                      | 491 ms: 1.21x faster                                                        |
| dulwich_log              | 50.5 ms                                                     | 42.0 ms: 1.20x faster                                                       |
| django_template          | 28.9 ms                                                     | 24.2 ms: 1.20x faster                                                       |
| coroutines               | 16.0 ms                                                     | 13.6 ms: 1.18x faster                                                       |
| docutils                 | 1.92 sec                                                    | 1.64 sec: 1.17x faster                                                      |
| sympy_str                | 194 ms                                                      | 171 ms: 1.14x faster                                                        |
| regex_effbot             | 1.66 ms                                                     | 1.46 ms: 1.13x faster                                                       |
| nbody                    | 71.3 ms                                                     | 62.9 ms: 1.13x faster                                                       |
| xml_etree_process        | 44.5 ms                                                     | 39.3 ms: 1.13x faster                                                       |
| regex_dna                | 136 ms                                                      | 121 ms: 1.13x faster                                                        |
| 2to3                     | 246 ms                                                      | 219 ms: 1.12x faster                                                        |
| bench_thread_pool        | 958 us                                                      | 860 us: 1.11x faster                                                        |
| nqueens                  | 66.6 ms                                                     | 60.2 ms: 1.11x faster                                                       |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.50 ms: 1.09x faster                                                       |
| xml_etree_parse          | 96.8 ms                                                     | 89.6 ms: 1.08x faster                                                       |
| scimark_fft              | 187 ms                                                      | 174 ms: 1.08x faster                                                        |
| sympy_expand             | 314 ms                                                      | 293 ms: 1.07x faster                                                        |
| meteor_contest           | 75.9 ms                                                     | 72.2 ms: 1.05x faster                                                       |
| regex_v8                 | 15.4 ms                                                     | 14.8 ms: 1.04x faster                                                       |
| xml_etree_iterparse      | 65.0 ms                                                     | 62.7 ms: 1.04x faster                                                       |
| fannkuch                 | 256 ms                                                      | 250 ms: 1.02x faster                                                        |
| logging_format           | 6.76 us                                                     | 6.65 us: 1.02x faster                                                       |
| logging_simple           | 6.22 us                                                     | 6.16 us: 1.01x faster                                                       |
| async_generators         | 222 ms                                                      | 228 ms: 1.03x slower                                                        |
| json_loads               | 14.0 us                                                     | 15.3 us: 1.09x slower                                                       |
| telco                    | 3.94 ms                                                     | 4.60 ms: 1.17x slower                                                       |
| coverage                 | 39.0 ms                                                     | 49.3 ms: 1.27x slower                                                       |
| python_startup_no_site   | 15.5 ms                                                     | 19.8 ms: 1.27x slower                                                       |
| python_startup           | 20.6 ms                                                     | 26.5 ms: 1.29x slower                                                       |
| bench_mp_pool            | 62.0 ms                                                     | 90.0 ms: 1.45x slower                                                       |
| gc_traversal             | 1.41 ms                                                     | 2.08 ms: 1.48x slower                                                       |
| create_gc_cycles         | 800 us                                                      | 1.25 ms: 1.57x slower                                                       |
| Geometric mean           | (ref)                                                       | 1.28x faster                                                                |

Benchmark hidden because not significant (3): pidigits, json, xml_etree_generate
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250430-3.14.0a7+-44e4c47/bm-20250430-pythonperf1-amd64-python-44e4c479fbf2c28605bd-3.14.0a7+-44e4c47.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.288x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.20x
- 95% likely to have a speedup of 1.19x
- 99% likely to have a speedup of 1.17x

# Memory
- memory change: unknown