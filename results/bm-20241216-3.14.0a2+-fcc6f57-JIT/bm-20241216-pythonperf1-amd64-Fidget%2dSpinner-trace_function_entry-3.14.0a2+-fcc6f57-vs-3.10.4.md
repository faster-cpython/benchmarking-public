# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: trace_function_entry
- machine: windows-amd64
- commit hash: fcc6f57
- commit date: 2024-12-16
- overall geometric mean: 1.253x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: unknown

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241216-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 246 ms                                                      | 218 ms: 1.13x faster                                                                  |
| docutils       | 1.92 sec                                                    | 1.75 sec: 1.09x faster                                                                |
| html5lib       | 51.0 ms                                                     | 38.6 ms: 1.32x faster                                                                 |
| Geometric mean | (ref)                                                       | 1.18x faster                                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241216-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|-------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_io           | 1.11 sec                                                    | 404 ms: 2.74x faster                                                                  |
| async_tree_none         | 435 ms                                                      | 179 ms: 2.43x faster                                                                  |
| async_tree_memoization  | 526 ms                                                      | 219 ms: 2.40x faster                                                                  |
| async_tree_cpu_io_mixed | 638 ms                                                      | 355 ms: 1.79x faster                                                                  |
| Geometric mean          | (ref)                                                       | 2.32x faster                                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241216-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 71.3 ms                                                     | 54.2 ms: 1.32x faster                                                                 |
| float          | 61.7 ms                                                     | 49.2 ms: 1.25x faster                                                                 |
| pidigits       | 149 ms                                                      | 147 ms: 1.01x faster                                                                  |
| Geometric mean | (ref)                                                       | 1.19x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241216-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_compile  | 106 ms                                                      | 80.7 ms: 1.31x faster                                                                 |
| regex_dna      | 136 ms                                                      | 118 ms: 1.16x faster                                                                  |
| regex_effbot   | 1.66 ms                                                     | 1.52 ms: 1.09x faster                                                                 |
| regex_v8       | 15.4 ms                                                     | 16.9 ms: 1.10x slower                                                                 |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241216-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| unpickle_pure_python | 183 us                                                      | 107 us: 1.71x faster                                                                  |
| json_dumps           | 9.16 ms                                                     | 6.39 ms: 1.43x faster                                                                 |
| tomli_loads          | 1.67 sec                                                    | 1.18 sec: 1.42x faster                                                                |
| pickle_pure_python   | 270 us                                                      | 192 us: 1.41x faster                                                                  |
| xml_etree_process    | 44.5 ms                                                     | 35.5 ms: 1.25x faster                                                                 |
| xml_etree_parse      | 96.8 ms                                                     | 86.8 ms: 1.12x faster                                                                 |
| xml_etree_generate   | 55.5 ms                                                     | 50.2 ms: 1.11x faster                                                                 |
| xml_etree_iterparse  | 65.0 ms                                                     | 61.2 ms: 1.06x faster                                                                 |
| json_loads           | 14.0 us                                                     | 14.2 us: 1.02x slower                                                                 |
| Geometric mean       | (ref)                                                       | 1.26x faster                                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241216-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup         | 20.6 ms                                                     | 23.4 ms: 1.14x slower                                                                 |
| python_startup_no_site | 15.5 ms                                                     | 17.7 ms: 1.14x slower                                                                 |
| Geometric mean         | (ref)                                                       | 1.14x slower                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241216-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|-----------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| mako            | 9.03 ms                                                     | 5.18 ms: 1.74x faster                                                                 |
| genshi_text     | 19.8 ms                                                     | 16.2 ms: 1.22x faster                                                                 |
| django_template | 28.9 ms                                                     | 25.9 ms: 1.12x faster                                                                 |
| genshi_xml      | 41.0 ms                                                     | 37.9 ms: 1.08x faster                                                                 |
| Geometric mean  | (ref)                                                       | 1.27x faster                                                                          |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120 | bm-20241216-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|--------------------------|:-----------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| typing_runtime_protocols | 336 us                                                      | 113 us: 2.97x faster                                                                  |
| async_tree_io            | 1.11 sec                                                    | 404 ms: 2.74x faster                                                                  |
| async_tree_none          | 435 ms                                                      | 179 ms: 2.43x faster                                                                  |
| async_tree_memoization   | 526 ms                                                      | 219 ms: 2.40x faster                                                                  |
| deltablue                | 4.19 ms                                                     | 2.30 ms: 1.82x faster                                                                 |
| async_tree_cpu_io_mixed  | 638 ms                                                      | 355 ms: 1.79x faster                                                                  |
| mako                     | 9.03 ms                                                     | 5.18 ms: 1.74x faster                                                                 |
| pylint                   | 350 ms                                                      | 202 ms: 1.74x faster                                                                  |
| unpickle_pure_python     | 183 us                                                      | 107 us: 1.71x faster                                                                  |
| go                       | 139 ms                                                      | 86.1 ms: 1.61x faster                                                                 |
| scimark_monte_carlo      | 57.3 ms                                                     | 35.8 ms: 1.60x faster                                                                 |
| crypto_pyaes             | 62.5 ms                                                     | 41.0 ms: 1.52x faster                                                                 |
| logging_silent           | 94.6 ns                                                     | 63.6 ns: 1.49x faster                                                                 |
| pyflate                  | 409 ms                                                      | 275 ms: 1.49x faster                                                                  |
| richards_super           | 52.2 ms                                                     | 35.4 ms: 1.47x faster                                                                 |
| chaos                    | 61.7 ms                                                     | 41.9 ms: 1.47x faster                                                                 |
| raytrace                 | 273 ms                                                      | 187 ms: 1.47x faster                                                                  |
| json_dumps               | 9.16 ms                                                     | 6.39 ms: 1.43x faster                                                                 |
| sqlglot_parse            | 1.22 ms                                                     | 856 us: 1.42x faster                                                                  |
| tomli_loads              | 1.67 sec                                                    | 1.18 sec: 1.42x faster                                                                |
| generators               | 32.4 ms                                                     | 23.0 ms: 1.41x faster                                                                 |
| pickle_pure_python       | 270 us                                                      | 192 us: 1.41x faster                                                                  |
| comprehensions           | 16.5 us                                                     | 11.7 us: 1.41x faster                                                                 |
| scimark_lu               | 85.8 ms                                                     | 61.9 ms: 1.39x faster                                                                 |
| deepcopy_memo            | 28.8 us                                                     | 20.8 us: 1.38x faster                                                                 |
| richards                 | 42.4 ms                                                     | 31.0 ms: 1.37x faster                                                                 |
| deepcopy                 | 255 us                                                      | 188 us: 1.36x faster                                                                  |
| scimark_sparse_mat_mult  | 2.72 ms                                                     | 2.03 ms: 1.34x faster                                                                 |
| sqlglot_transpile        | 1.48 ms                                                     | 1.11 ms: 1.33x faster                                                                 |
| scimark_fft              | 187 ms                                                      | 141 ms: 1.33x faster                                                                  |
| html5lib                 | 51.0 ms                                                     | 38.6 ms: 1.32x faster                                                                 |
| nbody                    | 71.3 ms                                                     | 54.2 ms: 1.32x faster                                                                 |
| regex_compile            | 106 ms                                                      | 80.7 ms: 1.31x faster                                                                 |
| pycparser                | 930 ms                                                      | 714 ms: 1.30x faster                                                                  |
| hexiom                   | 5.74 ms                                                     | 4.49 ms: 1.28x faster                                                                 |
| dulwich_log              | 50.5 ms                                                     | 39.8 ms: 1.27x faster                                                                 |
| pprint_pformat           | 1.22 sec                                                    | 971 ms: 1.26x faster                                                                  |
| float                    | 61.7 ms                                                     | 49.2 ms: 1.25x faster                                                                 |
| xml_etree_process        | 44.5 ms                                                     | 35.5 ms: 1.25x faster                                                                 |
| scimark_sor              | 106 ms                                                      | 86.1 ms: 1.23x faster                                                                 |
| sqlite_synth             | 1.91 us                                                     | 1.56 us: 1.23x faster                                                                 |
| genshi_text              | 19.8 ms                                                     | 16.2 ms: 1.22x faster                                                                 |
| spectral_norm            | 77.3 ms                                                     | 63.5 ms: 1.22x faster                                                                 |
| sympy_sum                | 107 ms                                                      | 89.0 ms: 1.20x faster                                                                 |
| pprint_safe_repr         | 592 ms                                                      | 495 ms: 1.20x faster                                                                  |
| bench_thread_pool        | 958 us                                                      | 808 us: 1.19x faster                                                                  |
| mdp                      | 1.78 sec                                                    | 1.50 sec: 1.18x faster                                                                |
| thrift                   | 617 us                                                      | 530 us: 1.16x faster                                                                  |
| regex_dna                | 136 ms                                                      | 118 ms: 1.16x faster                                                                  |
| deepcopy_reduce          | 2.20 us                                                     | 1.92 us: 1.15x faster                                                                 |
| sympy_integrate          | 15.3 ms                                                     | 13.5 ms: 1.14x faster                                                                 |
| 2to3                     | 246 ms                                                      | 218 ms: 1.13x faster                                                                  |
| coroutines               | 16.0 ms                                                     | 14.2 ms: 1.13x faster                                                                 |
| sympy_str                | 194 ms                                                      | 173 ms: 1.13x faster                                                                  |
| django_template          | 28.9 ms                                                     | 25.9 ms: 1.12x faster                                                                 |
| xml_etree_parse          | 96.8 ms                                                     | 86.8 ms: 1.12x faster                                                                 |
| xml_etree_generate       | 55.5 ms                                                     | 50.2 ms: 1.11x faster                                                                 |
| docutils                 | 1.92 sec                                                    | 1.75 sec: 1.09x faster                                                                |
| regex_effbot             | 1.66 ms                                                     | 1.52 ms: 1.09x faster                                                                 |
| genshi_xml               | 41.0 ms                                                     | 37.9 ms: 1.08x faster                                                                 |
| nqueens                  | 66.6 ms                                                     | 61.9 ms: 1.08x faster                                                                 |
| sqlglot_optimize         | 39.8 ms                                                     | 37.1 ms: 1.07x faster                                                                 |
| fannkuch                 | 256 ms                                                      | 239 ms: 1.07x faster                                                                  |
| json                     | 3.14 ms                                                     | 2.93 ms: 1.07x faster                                                                 |
| xml_etree_iterparse      | 65.0 ms                                                     | 61.2 ms: 1.06x faster                                                                 |
| sympy_expand             | 314 ms                                                      | 300 ms: 1.05x faster                                                                  |
| sqlglot_normalize        | 205 ms                                                      | 197 ms: 1.04x faster                                                                  |
| meteor_contest           | 75.9 ms                                                     | 73.4 ms: 1.03x faster                                                                 |
| logging_format           | 6.76 us                                                     | 6.65 us: 1.02x faster                                                                 |
| pidigits                 | 149 ms                                                      | 147 ms: 1.01x faster                                                                  |
| logging_simple           | 6.22 us                                                     | 6.18 us: 1.01x faster                                                                 |
| json_loads               | 14.0 us                                                     | 14.2 us: 1.02x slower                                                                 |
| regex_v8                 | 15.4 ms                                                     | 16.9 ms: 1.10x slower                                                                 |
| async_generators         | 222 ms                                                      | 245 ms: 1.11x slower                                                                  |
| telco                    | 3.94 ms                                                     | 4.37 ms: 1.11x slower                                                                 |
| mypy2                    | 555 ms                                                      | 630 ms: 1.13x slower                                                                  |
| python_startup           | 20.6 ms                                                     | 23.4 ms: 1.14x slower                                                                 |
| python_startup_no_site   | 15.5 ms                                                     | 17.7 ms: 1.14x slower                                                                 |
| coverage                 | 39.0 ms                                                     | 48.7 ms: 1.25x slower                                                                 |
| bench_mp_pool            | 62.0 ms                                                     | 82.4 ms: 1.33x slower                                                                 |
| gc_traversal             | 1.41 ms                                                     | 1.98 ms: 1.40x slower                                                                 |
| create_gc_cycles         | 800 us                                                      | 1.21 ms: 1.52x slower                                                                 |
| Geometric mean           | (ref)                                                       | 1.24x faster                                                                          |

Benchmark hidden because not significant (1): pathlib
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf1-amd64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20241216-3.14.0a2+-fcc6f57-JIT/bm-20241216-pythonperf1-amd64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, asyncio_websockets, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.253x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.18x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: unknown