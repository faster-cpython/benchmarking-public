# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: disable_tailcall
- machine: windows-amd64
- commit hash: da5ad58
- commit date: 2025-02-25
- overall geometric mean: 1.234x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.10x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-pythonperf1-amd64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 226 ms: 1.09x faster                                                              |
| docutils       | 1.92 sec                                                    | 1.74 sec: 1.10x faster                                                            |
| html5lib       | 51.0 ms                                                     | 39.1 ms: 1.30x faster                                                             |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                      |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-pythonperf1-amd64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 400 ms: 2.77x faster                                                              |
| async_tree_memoization  | 526 ms                                                      | 203 ms: 2.59x faster                                                              |
| async_tree_none         | 435 ms                                                      | 173 ms: 2.51x faster                                                              |
| async_tree_cpu_io_mixed | 638 ms                                                      | 356 ms: 1.79x faster                                                              |
| Geometric mean          | (ref)                                                       | 2.38x faster                                                                      |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-pythonperf1-amd64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| float          | 61.7 ms                                                     | 43.6 ms: 1.42x faster                                                             |
| nbody          | 71.3 ms                                                     | 62.8 ms: 1.14x faster                                                             |
| pidigits       | 149 ms                                                      | 155 ms: 1.04x slower                                                              |
| Geometric mean | (ref)                                                       | 1.16x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-pythonperf1-amd64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 83.3 ms: 1.27x faster                                                             |
| regex_dna      | 136 ms                                                      | 133 ms: 1.03x faster                                                              |
| regex_v8       | 15.4 ms                                                     | 16.7 ms: 1.08x slower                                                             |
| regex_effbot   | 1.66 ms                                                     | 1.95 ms: 1.17x slower                                                             |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-pythonperf1-amd64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python   | 270 us                                                      | 210 us: 1.29x faster                                                              |
| tomli_loads          | 1.67 sec                                                    | 1.32 sec: 1.27x faster                                                            |
| unpickle_pure_python | 183 us                                                      | 146 us: 1.26x faster                                                              |
| json_dumps           | 9.16 ms                                                     | 7.80 ms: 1.17x faster                                                             |
| xml_etree_parse      | 96.8 ms                                                     | 102 ms: 1.06x slower                                                              |
| xml_etree_iterparse  | 65.0 ms                                                     | 68.8 ms: 1.06x slower                                                             |
| xml_etree_generate   | 55.5 ms                                                     | 63.9 ms: 1.15x slower                                                             |
| json_loads           | 14.0 us                                                     | 19.7 us: 1.40x slower                                                             |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                                      |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-pythonperf1-amd64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 15.5 ms                                                     | 19.8 ms: 1.28x slower                                                             |
| python_startup         | 20.6 ms                                                     | 26.9 ms: 1.31x slower                                                             |
| Geometric mean         | (ref)                                                       | 1.29x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-pythonperf1-amd64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_text     | 19.8 ms                                                     | 14.5 ms: 1.37x faster                                                             |
| genshi_xml      | 41.0 ms                                                     | 32.0 ms: 1.28x faster                                                             |
| mako            | 9.03 ms                                                     | 7.58 ms: 1.19x faster                                                             |
| django_template | 28.9 ms                                                     | 24.2 ms: 1.19x faster                                                             |
| Geometric mean  | (ref)                                                       | 1.26x faster                                                                      |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20250225-pythonperf1-amd64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|--------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 112 us: 3.00x faster                                                              |
| async_tree_io            | 1.11 sec                                                    | 400 ms: 2.77x faster                                                              |
| async_tree_memoization   | 526 ms                                                      | 203 ms: 2.59x faster                                                              |
| pathlib                  | 75.7 ms                                                     | 29.7 ms: 2.55x faster                                                             |
| async_tree_none          | 435 ms                                                      | 173 ms: 2.51x faster                                                              |
| deltablue                | 4.19 ms                                                     | 1.79 ms: 2.33x faster                                                             |
| go                       | 139 ms                                                      | 70.3 ms: 1.98x faster                                                             |
| generators               | 32.4 ms                                                     | 17.1 ms: 1.90x faster                                                             |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 356 ms: 1.79x faster                                                              |
| pylint                   | 350 ms                                                      | 201 ms: 1.74x faster                                                              |
| logging_silent           | 94.6 ns                                                     | 56.6 ns: 1.67x faster                                                             |
| raytrace                 | 273 ms                                                      | 166 ms: 1.64x faster                                                              |
| richards_super           | 52.2 ms                                                     | 31.8 ms: 1.64x faster                                                             |
| chaos                    | 61.7 ms                                                     | 38.8 ms: 1.59x faster                                                             |
| scimark_sor              | 106 ms                                                      | 67.2 ms: 1.58x faster                                                             |
| deepcopy_memo            | 28.8 us                                                     | 18.7 us: 1.54x faster                                                             |
| richards                 | 42.4 ms                                                     | 28.0 ms: 1.52x faster                                                             |
| sqlglot_parse            | 1.22 ms                                                     | 808 us: 1.50x faster                                                              |
| hexiom                   | 5.74 ms                                                     | 3.87 ms: 1.48x faster                                                             |
| scimark_monte_carlo      | 57.3 ms                                                     | 38.9 ms: 1.47x faster                                                             |
| comprehensions           | 16.5 us                                                     | 11.4 us: 1.45x faster                                                             |
| sqlglot_transpile        | 1.48 ms                                                     | 1.02 ms: 1.45x faster                                                             |
| deepcopy                 | 255 us                                                      | 177 us: 1.44x faster                                                              |
| pyflate                  | 409 ms                                                      | 285 ms: 1.43x faster                                                              |
| float                    | 61.7 ms                                                     | 43.6 ms: 1.42x faster                                                             |
| spectral_norm            | 77.3 ms                                                     | 56.4 ms: 1.37x faster                                                             |
| genshi_text              | 19.8 ms                                                     | 14.5 ms: 1.37x faster                                                             |
| scimark_lu               | 85.8 ms                                                     | 63.0 ms: 1.36x faster                                                             |
| html5lib                 | 51.0 ms                                                     | 39.1 ms: 1.30x faster                                                             |
| pycparser                | 930 ms                                                      | 715 ms: 1.30x faster                                                              |
| pickle_pure_python       | 270 us                                                      | 210 us: 1.29x faster                                                              |
| genshi_xml               | 41.0 ms                                                     | 32.0 ms: 1.28x faster                                                             |
| regex_compile            | 106 ms                                                      | 83.3 ms: 1.27x faster                                                             |
| tomli_loads              | 1.67 sec                                                    | 1.32 sec: 1.27x faster                                                            |
| unpickle_pure_python     | 183 us                                                      | 146 us: 1.26x faster                                                              |
| crypto_pyaes             | 62.5 ms                                                     | 50.7 ms: 1.23x faster                                                             |
| coroutines               | 16.0 ms                                                     | 13.1 ms: 1.22x faster                                                             |
| dulwich_log              | 50.5 ms                                                     | 41.8 ms: 1.21x faster                                                             |
| mako                     | 9.03 ms                                                     | 7.58 ms: 1.19x faster                                                             |
| django_template          | 28.9 ms                                                     | 24.2 ms: 1.19x faster                                                             |
| sqlite_synth             | 1.91 us                                                     | 1.61 us: 1.19x faster                                                             |
| sympy_sum                | 107 ms                                                      | 91.0 ms: 1.18x faster                                                             |
| json_dumps               | 9.16 ms                                                     | 7.80 ms: 1.17x faster                                                             |
| pprint_pformat           | 1.22 sec                                                    | 1.04 sec: 1.17x faster                                                            |
| deepcopy_reduce          | 2.20 us                                                     | 1.89 us: 1.17x faster                                                             |
| sympy_integrate          | 15.3 ms                                                     | 13.3 ms: 1.15x faster                                                             |
| pprint_safe_repr         | 592 ms                                                      | 516 ms: 1.15x faster                                                              |
| nbody                    | 71.3 ms                                                     | 62.8 ms: 1.14x faster                                                             |
| sqlglot_optimize         | 39.8 ms                                                     | 35.4 ms: 1.13x faster                                                             |
| thrift                   | 617 us                                                      | 554 us: 1.11x faster                                                              |
| mdp                      | 1.78 sec                                                    | 1.61 sec: 1.10x faster                                                            |
| sympy_str                | 194 ms                                                      | 176 ms: 1.10x faster                                                              |
| docutils                 | 1.92 sec                                                    | 1.74 sec: 1.10x faster                                                            |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.49 ms: 1.09x faster                                                             |
| 2to3                     | 246 ms                                                      | 226 ms: 1.09x faster                                                              |
| bench_thread_pool        | 958 us                                                      | 879 us: 1.09x faster                                                              |
| sqlglot_normalize        | 205 ms                                                      | 190 ms: 1.08x faster                                                              |
| nqueens                  | 66.6 ms                                                     | 62.1 ms: 1.07x faster                                                             |
| meteor_contest           | 75.9 ms                                                     | 72.1 ms: 1.05x faster                                                             |
| sympy_expand             | 314 ms                                                      | 302 ms: 1.04x faster                                                              |
| regex_dna                | 136 ms                                                      | 133 ms: 1.03x faster                                                              |
| scimark_fft              | 187 ms                                                      | 183 ms: 1.03x faster                                                              |
| async_generators         | 222 ms                                                      | 219 ms: 1.01x faster                                                              |
| logging_simple           | 6.22 us                                                     | 6.32 us: 1.02x slower                                                             |
| pidigits                 | 149 ms                                                      | 155 ms: 1.04x slower                                                              |
| xml_etree_parse          | 96.8 ms                                                     | 102 ms: 1.06x slower                                                              |
| xml_etree_iterparse      | 65.0 ms                                                     | 68.8 ms: 1.06x slower                                                             |
| fannkuch                 | 256 ms                                                      | 272 ms: 1.06x slower                                                              |
| regex_v8                 | 15.4 ms                                                     | 16.7 ms: 1.08x slower                                                             |
| xml_etree_generate       | 55.5 ms                                                     | 63.9 ms: 1.15x slower                                                             |
| json                     | 3.14 ms                                                     | 3.65 ms: 1.16x slower                                                             |
| regex_effbot             | 1.66 ms                                                     | 1.95 ms: 1.17x slower                                                             |
| python_startup_no_site   | 15.5 ms                                                     | 19.8 ms: 1.28x slower                                                             |
| telco                    | 3.94 ms                                                     | 5.14 ms: 1.30x slower                                                             |
| python_startup           | 20.6 ms                                                     | 26.9 ms: 1.31x slower                                                             |
| coverage                 | 39.0 ms                                                     | 52.3 ms: 1.34x slower                                                             |
| json_loads               | 14.0 us                                                     | 19.7 us: 1.40x slower                                                             |
| bench_mp_pool            | 62.0 ms                                                     | 90.1 ms: 1.45x slower                                                             |
| create_gc_cycles         | 800 us                                                      | 1.32 ms: 1.65x slower                                                             |
| gc_traversal             | 1.41 ms                                                     | 2.71 ms: 1.93x slower                                                             |
| Geometric mean           | (ref)                                                       | 1.23x faster                                                                      |

Benchmark hidden because not significant (2): xml_etree_process, logging_format
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250225-3.14.0a5+-da5ad58-CLANG/bm-20250225-pythonperf1-amd64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.234x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.14x
- 95% likely to have a speedup of 1.13x
- 99% likely to have a speedup of 1.10x

# Memory
- memory change: unknown