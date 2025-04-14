# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: baseline_jit
- machine: windows-amd64
- commit hash: e55b89a
- commit date: 2025-03-19
- overall geometric mean: 1.191x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-pythonperf1-amd64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 231 ms: 1.06x faster                                                          |
| docutils       | 1.92 sec                                                    | 1.74 sec: 1.10x faster                                                        |
| html5lib       | 51.0 ms                                                     | 41.6 ms: 1.23x faster                                                         |
| Geometric mean | (ref)                                                       | 1.13x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-pythonperf1-amd64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|-------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 435 ms: 2.55x faster                                                          |
| async_tree_memoization  | 526 ms                                                      | 227 ms: 2.32x faster                                                          |
| async_tree_none         | 435 ms                                                      | 193 ms: 2.26x faster                                                          |
| async_tree_cpu_io_mixed | 638 ms                                                      | 348 ms: 1.83x faster                                                          |
| Geometric mean          | (ref)                                                       | 2.22x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-pythonperf1-amd64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 47.6 ms: 1.30x faster                                                         |
| nbody          | 71.3 ms                                                     | 57.9 ms: 1.23x faster                                                         |
| pidigits       | 149 ms                                                      | 148 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                       | 1.17x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-pythonperf1-amd64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 88.3 ms: 1.20x faster                                                         |
| regex_dna      | 136 ms                                                      | 117 ms: 1.17x faster                                                          |
| regex_effbot   | 1.66 ms                                                     | 1.48 ms: 1.12x faster                                                         |
| regex_v8       | 15.4 ms                                                     | 14.1 ms: 1.10x faster                                                         |
| Geometric mean | (ref)                                                       | 1.15x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-pythonperf1-amd64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 1.67 sec                                                    | 1.28 sec: 1.31x faster                                                        |
| json_dumps           | 9.16 ms                                                     | 7.01 ms: 1.31x faster                                                         |
| pickle_pure_python   | 270 us                                                      | 228 us: 1.18x faster                                                          |
| unpickle_pure_python | 183 us                                                      | 157 us: 1.17x faster                                                          |
| xml_etree_parse      | 96.8 ms                                                     | 90.2 ms: 1.07x faster                                                         |
| xml_etree_process    | 44.5 ms                                                     | 43.0 ms: 1.03x faster                                                         |
| xml_etree_iterparse  | 65.0 ms                                                     | 63.6 ms: 1.02x faster                                                         |
| xml_etree_generate   | 55.5 ms                                                     | 59.7 ms: 1.08x slower                                                         |
| json_loads           | 14.0 us                                                     | 15.1 us: 1.08x slower                                                         |
| Geometric mean       | (ref)                                                       | 1.10x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-pythonperf1-amd64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 26.6 ms: 1.29x slower                                                         |
| python_startup_no_site | 15.5 ms                                                     | 20.8 ms: 1.34x slower                                                         |
| Geometric mean         | (ref)                                                       | 1.32x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-pythonperf1-amd64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 7.06 ms: 1.28x faster                                                         |
| genshi_text     | 19.8 ms                                                     | 17.1 ms: 1.16x faster                                                         |
| django_template | 28.9 ms                                                     | 26.1 ms: 1.11x faster                                                         |
| genshi_xml      | 41.0 ms                                                     | 38.4 ms: 1.07x faster                                                         |
| Geometric mean  | (ref)                                                       | 1.15x faster                                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250319-pythonperf1-amd64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a |
|--------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 120 us: 2.80x faster                                                          |
| async_tree_io            | 1.11 sec                                                    | 435 ms: 2.55x faster                                                          |
| pathlib                  | 75.7 ms                                                     | 32.5 ms: 2.33x faster                                                         |
| async_tree_memoization   | 526 ms                                                      | 227 ms: 2.32x faster                                                          |
| async_tree_none          | 435 ms                                                      | 193 ms: 2.26x faster                                                          |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 348 ms: 1.83x faster                                                          |
| deltablue                | 4.19 ms                                                     | 2.37 ms: 1.77x faster                                                         |
| pylint                   | 350 ms                                                      | 206 ms: 1.70x faster                                                          |
| logging_silent           | 94.6 ns                                                     | 59.7 ns: 1.58x faster                                                         |
| generators               | 32.4 ms                                                     | 20.8 ms: 1.56x faster                                                         |
| richards_super           | 52.2 ms                                                     | 34.1 ms: 1.53x faster                                                         |
| go                       | 139 ms                                                      | 92.3 ms: 1.51x faster                                                         |
| richards                 | 42.4 ms                                                     | 29.9 ms: 1.42x faster                                                         |
| scimark_lu               | 85.8 ms                                                     | 61.2 ms: 1.40x faster                                                         |
| raytrace                 | 273 ms                                                      | 196 ms: 1.40x faster                                                          |
| chaos                    | 61.7 ms                                                     | 45.2 ms: 1.36x faster                                                         |
| deepcopy_memo            | 28.8 us                                                     | 22.0 us: 1.31x faster                                                         |
| tomli_loads              | 1.67 sec                                                    | 1.28 sec: 1.31x faster                                                        |
| json_dumps               | 9.16 ms                                                     | 7.01 ms: 1.31x faster                                                         |
| scimark_sor              | 106 ms                                                      | 81.3 ms: 1.31x faster                                                         |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.09 ms: 1.30x faster                                                         |
| float                    | 61.7 ms                                                     | 47.6 ms: 1.30x faster                                                         |
| pyflate                  | 409 ms                                                      | 318 ms: 1.29x faster                                                          |
| scimark_monte_carlo      | 57.3 ms                                                     | 44.6 ms: 1.28x faster                                                         |
| mako                     | 9.03 ms                                                     | 7.06 ms: 1.28x faster                                                         |
| spectral_norm            | 77.3 ms                                                     | 60.8 ms: 1.27x faster                                                         |
| nbody                    | 71.3 ms                                                     | 57.9 ms: 1.23x faster                                                         |
| pycparser                | 930 ms                                                      | 758 ms: 1.23x faster                                                          |
| html5lib                 | 51.0 ms                                                     | 41.6 ms: 1.23x faster                                                         |
| deepcopy                 | 255 us                                                      | 211 us: 1.21x faster                                                          |
| regex_compile            | 106 ms                                                      | 88.3 ms: 1.20x faster                                                         |
| thrift                   | 617 us                                                      | 522 us: 1.18x faster                                                          |
| scimark_fft              | 187 ms                                                      | 159 ms: 1.18x faster                                                          |
| pickle_pure_python       | 270 us                                                      | 228 us: 1.18x faster                                                          |
| regex_dna                | 136 ms                                                      | 117 ms: 1.17x faster                                                          |
| unpickle_pure_python     | 183 us                                                      | 157 us: 1.17x faster                                                          |
| genshi_text              | 19.8 ms                                                     | 17.1 ms: 1.16x faster                                                         |
| sympy_sum                | 107 ms                                                      | 92.4 ms: 1.16x faster                                                         |
| dulwich_log              | 50.5 ms                                                     | 44.0 ms: 1.15x faster                                                         |
| coroutines               | 16.0 ms                                                     | 14.1 ms: 1.14x faster                                                         |
| mdp                      | 1.78 sec                                                    | 1.58 sec: 1.13x faster                                                        |
| sympy_integrate          | 15.3 ms                                                     | 13.6 ms: 1.12x faster                                                         |
| regex_effbot             | 1.66 ms                                                     | 1.48 ms: 1.12x faster                                                         |
| crypto_pyaes             | 62.5 ms                                                     | 55.9 ms: 1.12x faster                                                         |
| django_template          | 28.9 ms                                                     | 26.1 ms: 1.11x faster                                                         |
| docutils                 | 1.92 sec                                                    | 1.74 sec: 1.10x faster                                                        |
| sqlite_synth             | 1.91 us                                                     | 1.74 us: 1.10x faster                                                         |
| regex_v8                 | 15.4 ms                                                     | 14.1 ms: 1.10x faster                                                         |
| bench_thread_pool        | 958 us                                                      | 879 us: 1.09x faster                                                          |
| xml_etree_parse          | 96.8 ms                                                     | 90.2 ms: 1.07x faster                                                         |
| pprint_pformat           | 1.22 sec                                                    | 1.14 sec: 1.07x faster                                                        |
| sympy_str                | 194 ms                                                      | 182 ms: 1.07x faster                                                          |
| comprehensions           | 16.5 us                                                     | 15.5 us: 1.07x faster                                                         |
| genshi_xml               | 41.0 ms                                                     | 38.4 ms: 1.07x faster                                                         |
| hexiom                   | 5.74 ms                                                     | 5.39 ms: 1.07x faster                                                         |
| 2to3                     | 246 ms                                                      | 231 ms: 1.06x faster                                                          |
| pprint_safe_repr         | 592 ms                                                      | 562 ms: 1.05x faster                                                          |
| deepcopy_reduce          | 2.20 us                                                     | 2.10 us: 1.05x faster                                                         |
| xml_etree_process        | 44.5 ms                                                     | 43.0 ms: 1.03x faster                                                         |
| nqueens                  | 66.6 ms                                                     | 64.8 ms: 1.03x faster                                                         |
| xml_etree_iterparse      | 65.0 ms                                                     | 63.6 ms: 1.02x faster                                                         |
| json                     | 3.14 ms                                                     | 3.10 ms: 1.01x faster                                                         |
| pidigits                 | 149 ms                                                      | 148 ms: 1.01x faster                                                          |
| meteor_contest           | 75.9 ms                                                     | 76.3 ms: 1.01x slower                                                         |
| sympy_expand             | 314 ms                                                      | 318 ms: 1.01x slower                                                          |
| fannkuch                 | 256 ms                                                      | 265 ms: 1.04x slower                                                          |
| logging_simple           | 6.22 us                                                     | 6.55 us: 1.05x slower                                                         |
| logging_format           | 6.76 us                                                     | 7.14 us: 1.06x slower                                                         |
| xml_etree_generate       | 55.5 ms                                                     | 59.7 ms: 1.08x slower                                                         |
| json_loads               | 14.0 us                                                     | 15.1 us: 1.08x slower                                                         |
| async_generators         | 222 ms                                                      | 254 ms: 1.15x slower                                                          |
| coverage                 | 39.0 ms                                                     | 49.8 ms: 1.28x slower                                                         |
| telco                    | 3.94 ms                                                     | 5.05 ms: 1.28x slower                                                         |
| python_startup           | 20.6 ms                                                     | 26.6 ms: 1.29x slower                                                         |
| python_startup_no_site   | 15.5 ms                                                     | 20.8 ms: 1.34x slower                                                         |
| bench_mp_pool            | 62.0 ms                                                     | 89.4 ms: 1.44x slower                                                         |
| gc_traversal             | 1.41 ms                                                     | 2.04 ms: 1.45x slower                                                         |
| create_gc_cycles         | 800 us                                                      | 1.27 ms: 1.59x slower                                                         |
| Geometric mean           | (ref)                                                       | 1.18x faster                                                                  |
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250319-3.14.0a6+-e55b89a-JIT/bm-20250319-pythonperf1-amd64-Fidget%2dSpinner-baseline_jit-3.14.0a6+-e55b89a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.191x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.12x
- 95% likely to have a speedup of 1.11x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown