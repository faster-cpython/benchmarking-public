# Results vs. 3.10.4

- fork: Fidget-Spinner
- ref: tail_call
- machine: linux-x86_64
- commit hash: df5d01c
- commit date: 2025-01-16
- overall geometric mean: 1.397x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.33x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-pythonperf2-x86_64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 274 ms: 1.28x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.85 sec: 1.20x faster                                                      |
| html5lib       | 94.6 ms                                                      | 66.0 ms: 1.43x faster                                                       |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-pythonperf2-x86_64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 610 ms: 2.62x faster                                                        |
| async_tree_none         | 692 ms                                                       | 271 ms: 2.55x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 334 ms: 2.45x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 532 ms: 1.76x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.32x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-pythonperf2-x86_64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 66.9 ms: 1.66x faster                                                       |
| nbody          | 134 ms                                                       | 101 ms: 1.33x faster                                                        |
| pidigits       | 271 ms                                                       | 285 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                        | 1.28x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-pythonperf2-x86_64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 134 ms: 1.41x faster                                                        |
| regex_dna      | 261 ms                                                       | 226 ms: 1.15x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 2.98 ms: 1.04x faster                                                       |
| regex_v8       | 27.2 ms                                                      | 26.5 ms: 1.02x faster                                                       |
| Geometric mean | (ref)                                                        | 1.15x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-pythonperf2-x86_64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 202 us: 1.55x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 1.99 sec: 1.47x faster                                                      |
| pickle_pure_python   | 455 us                                                       | 311 us: 1.46x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 55.6 ms: 1.37x faster                                                       |
| json_dumps           | 14.5 ms                                                      | 11.6 ms: 1.26x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.2 us: 1.20x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 79.0 ms: 1.17x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 102 ms: 1.09x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 162 ms: 1.01x slower                                                        |
| Geometric mean       | (ref)                                                        | 1.27x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-pythonperf2-x86_64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.02 ms: 1.23x slower                                                       |
| python_startup         | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-pythonperf2-x86_64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 34.0 ms: 1.48x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 22.0 ms: 1.43x faster                                                       |
| mako            | 14.7 ms                                                      | 10.9 ms: 1.34x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 52.6 ms: 1.20x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.36x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250116-pythonperf2-x86_64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 165 us: 3.26x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 610 ms: 2.62x faster                                                        |
| async_tree_none          | 692 ms                                                       | 271 ms: 2.55x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 334 ms: 2.45x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.12 ms: 2.41x faster                                                       |
| go                       | 262 ms                                                       | 117 ms: 2.23x faster                                                        |
| scimark_lu               | 167 ms                                                       | 82.5 ms: 2.02x faster                                                       |
| logging_silent           | 167 ns                                                       | 82.8 ns: 2.02x faster                                                       |
| generators               | 57.3 ms                                                      | 28.5 ms: 2.01x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 54.8 ms: 1.96x faster                                                       |
| raytrace                 | 489 ms                                                       | 254 ms: 1.92x faster                                                        |
| scimark_sor              | 180 ms                                                       | 95.1 ms: 1.90x faster                                                       |
| richards_super           | 90.6 ms                                                      | 48.4 ms: 1.87x faster                                                       |
| chaos                    | 109 ms                                                       | 58.1 ms: 1.87x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 27.0 us: 1.84x faster                                                       |
| pyflate                  | 733 ms                                                       | 405 ms: 1.81x faster                                                        |
| pylint                   | 566 ms                                                       | 317 ms: 1.79x faster                                                        |
| richards                 | 75.1 ms                                                      | 42.1 ms: 1.79x faster                                                       |
| sqlglot_parse            | 2.24 ms                                                      | 1.26 ms: 1.78x faster                                                       |
| deepcopy                 | 468 us                                                       | 263 us: 1.78x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 532 ms: 1.76x faster                                                        |
| spectral_norm            | 139 ms                                                       | 80.7 ms: 1.72x faster                                                       |
| comprehensions           | 26.7 us                                                      | 15.8 us: 1.69x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 5.65 ms: 1.67x faster                                                       |
| float                    | 111 ms                                                       | 66.9 ms: 1.66x faster                                                       |
| sqlglot_transpile        | 2.68 ms                                                      | 1.65 ms: 1.62x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 75.1 ms: 1.59x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 202 us: 1.55x faster                                                        |
| django_template          | 50.2 ms                                                      | 34.0 ms: 1.48x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.05 us: 1.47x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 1.99 sec: 1.47x faster                                                      |
| pickle_pure_python       | 455 us                                                       | 311 us: 1.46x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 2.75 us: 1.46x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.71 us: 1.44x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 66.0 ms: 1.43x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 22.0 ms: 1.43x faster                                                       |
| thrift                   | 1.18 ms                                                      | 827 us: 1.42x faster                                                        |
| regex_compile            | 190 ms                                                       | 134 ms: 1.41x faster                                                        |
| scimark_fft              | 361 ms                                                       | 258 ms: 1.40x faster                                                        |
| coroutines               | 30.3 ms                                                      | 21.6 ms: 1.40x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.21 sec: 1.38x faster                                                      |
| pprint_pformat           | 2.15 sec                                                     | 1.57 sec: 1.37x faster                                                      |
| pathlib                  | 21.4 ms                                                      | 15.6 ms: 1.37x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 767 ms: 1.37x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 55.6 ms: 1.37x faster                                                       |
| mako                     | 14.7 ms                                                      | 10.9 ms: 1.34x faster                                                       |
| fannkuch                 | 483 ms                                                       | 359 ms: 1.34x faster                                                        |
| nbody                    | 134 ms                                                       | 101 ms: 1.33x faster                                                        |
| sqlalchemy_declarative   | 190 ms                                                       | 143 ms: 1.33x faster                                                        |
| nqueens                  | 115 ms                                                       | 86.9 ms: 1.32x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 3.88 ms: 1.31x faster                                                       |
| sympy_sum                | 193 ms                                                       | 148 ms: 1.31x faster                                                        |
| sqlalchemy_imperative    | 22.7 ms                                                      | 17.5 ms: 1.30x faster                                                       |
| sympy_str                | 360 ms                                                       | 282 ms: 1.28x faster                                                        |
| 2to3                     | 350 ms                                                       | 274 ms: 1.28x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 901 us: 1.27x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 11.6 ms: 1.26x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 22.5 ms: 1.25x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 64.9 ms: 1.25x faster                                                       |
| sqlglot_normalize        | 144 ms                                                       | 115 ms: 1.25x faster                                                        |
| sympy_expand             | 600 ms                                                       | 483 ms: 1.24x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 57.3 ms: 1.23x faster                                                       |
| json_loads               | 30.3 us                                                      | 25.2 us: 1.20x faster                                                       |
| genshi_xml               | 63.3 ms                                                      | 52.6 ms: 1.20x faster                                                       |
| docutils                 | 3.41 sec                                                     | 2.85 sec: 1.20x faster                                                      |
| xml_etree_generate       | 92.3 ms                                                      | 79.0 ms: 1.17x faster                                                       |
| mdp                      | 3.01 sec                                                     | 2.60 sec: 1.16x faster                                                      |
| regex_dna                | 261 ms                                                       | 226 ms: 1.15x faster                                                        |
| json                     | 5.86 ms                                                      | 5.24 ms: 1.12x faster                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 102 ms: 1.09x faster                                                        |
| meteor_contest           | 138 ms                                                       | 128 ms: 1.08x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.79 us: 1.07x faster                                                       |
| regex_effbot             | 3.09 ms                                                      | 2.98 ms: 1.04x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 26.5 ms: 1.02x faster                                                       |
| asyncio_websockets       | 390 ms                                                       | 383 ms: 1.02x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 162 ms: 1.01x slower                                                        |
| telco                    | 7.23 ms                                                      | 7.54 ms: 1.04x slower                                                       |
| pidigits                 | 271 ms                                                       | 285 ms: 1.05x slower                                                        |
| coverage                 | 63.3 ms                                                      | 73.2 ms: 1.16x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.02 ms: 1.23x slower                                                       |
| python_startup           | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.87 ms: 1.63x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 5.72 ms: 1.68x slower                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 1.54 sec: 242.14x slower                                                    |
| Geometric mean           | (ref)                                                        | 1.31x faster                                                                |

Benchmark hidden because not significant (1): async_generators
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250116-3.14.0a4+-df5d01c-CLANG/bm-20250116-pythonperf2-x86_64-Fidget%2dSpinner-tail_call-3.14.0a4+-df5d01c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.397x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.31x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.33x