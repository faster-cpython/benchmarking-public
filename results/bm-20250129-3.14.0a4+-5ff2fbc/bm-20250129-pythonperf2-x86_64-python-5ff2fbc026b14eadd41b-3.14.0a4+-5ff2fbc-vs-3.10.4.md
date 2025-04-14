# Results vs. 3.10.4

- fork: python
- ref: 5ff2fbc026b14eadd41b
- machine: linux-x86_64
- commit hash: 5ff2fbc
- commit date: 2025-01-29
- overall geometric mean: 1.364x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.27x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-pythonperf2-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 279 ms: 1.25x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.84 sec: 1.20x faster                                                       |
| html5lib       | 94.6 ms                                                      | 66.0 ms: 1.43x faster                                                        |
| Geometric mean | (ref)                                                        | 1.29x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-pythonperf2-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 649 ms: 2.46x faster                                                         |
| async_tree_none         | 692 ms                                                       | 289 ms: 2.39x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 349 ms: 2.35x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 520 ms: 1.80x faster                                                         |
| Geometric mean          | (ref)                                                        | 2.23x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-pythonperf2-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 69.1 ms: 1.61x faster                                                        |
| nbody          | 134 ms                                                       | 86.5 ms: 1.55x faster                                                        |
| pidigits       | 271 ms                                                       | 254 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                        | 1.38x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-pythonperf2-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 134 ms: 1.42x faster                                                         |
| regex_dna      | 261 ms                                                       | 236 ms: 1.11x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 25.9 ms: 1.05x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.04 ms: 1.02x faster                                                        |
| Geometric mean | (ref)                                                        | 1.14x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-pythonperf2-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 209 us: 1.49x faster                                                         |
| pickle_pure_python   | 455 us                                                       | 323 us: 1.41x faster                                                         |
| tomli_loads          | 2.92 sec                                                     | 2.08 sec: 1.40x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 58.5 ms: 1.30x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 11.7 ms: 1.25x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 136 ms: 1.18x faster                                                         |
| xml_etree_iterparse  | 110 ms                                                       | 97.6 ms: 1.13x faster                                                        |
| json_loads           | 30.3 us                                                      | 26.9 us: 1.13x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 83.5 ms: 1.11x faster                                                        |
| Geometric mean       | (ref)                                                        | 1.26x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-pythonperf2-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.02 ms: 1.23x slower                                                        |
| python_startup         | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.31x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-pythonperf2-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 35.1 ms: 1.43x faster                                                        |
| mako            | 14.7 ms                                                      | 10.8 ms: 1.36x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 24.5 ms: 1.28x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 55.0 ms: 1.15x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.30x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250129-pythonperf2-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 169 us: 3.18x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 649 ms: 2.46x faster                                                         |
| async_tree_none          | 692 ms                                                       | 289 ms: 2.39x faster                                                         |
| async_tree_memoization   | 819 ms                                                       | 349 ms: 2.35x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.25 ms: 2.30x faster                                                        |
| go                       | 262 ms                                                       | 123 ms: 2.12x faster                                                         |
| generators               | 57.3 ms                                                      | 28.4 ms: 2.02x faster                                                        |
| chaos                    | 109 ms                                                       | 58.5 ms: 1.86x faster                                                        |
| raytrace                 | 489 ms                                                       | 270 ms: 1.81x faster                                                         |
| pylint                   | 566 ms                                                       | 312 ms: 1.81x faster                                                         |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 520 ms: 1.80x faster                                                         |
| scimark_lu               | 167 ms                                                       | 93.7 ms: 1.78x faster                                                        |
| richards_super           | 90.6 ms                                                      | 51.3 ms: 1.77x faster                                                        |
| logging_silent           | 167 ns                                                       | 96.8 ns: 1.73x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 62.8 ms: 1.71x faster                                                        |
| pyflate                  | 733 ms                                                       | 430 ms: 1.71x faster                                                         |
| deepcopy_memo            | 49.8 us                                                      | 29.2 us: 1.70x faster                                                        |
| deepcopy                 | 468 us                                                       | 278 us: 1.68x faster                                                         |
| sqlglot_parse            | 2.24 ms                                                      | 1.33 ms: 1.68x faster                                                        |
| spectral_norm            | 139 ms                                                       | 83.4 ms: 1.67x faster                                                        |
| scimark_sor              | 180 ms                                                       | 108 ms: 1.67x faster                                                         |
| richards                 | 75.1 ms                                                      | 45.3 ms: 1.66x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 72.7 ms: 1.64x faster                                                        |
| float                    | 111 ms                                                       | 69.1 ms: 1.61x faster                                                        |
| comprehensions           | 26.7 us                                                      | 16.8 us: 1.58x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.71 ms: 1.57x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.06 ms: 1.55x faster                                                        |
| nbody                    | 134 ms                                                       | 86.5 ms: 1.55x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 209 us: 1.49x faster                                                         |
| coroutines               | 30.3 ms                                                      | 20.8 ms: 1.46x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.17 us: 1.44x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 66.0 ms: 1.43x faster                                                        |
| django_template          | 50.2 ms                                                      | 35.1 ms: 1.43x faster                                                        |
| logging_format           | 9.64 us                                                      | 6.75 us: 1.43x faster                                                        |
| regex_compile            | 190 ms                                                       | 134 ms: 1.42x faster                                                         |
| pickle_pure_python       | 455 us                                                       | 323 us: 1.41x faster                                                         |
| tomli_loads              | 2.92 sec                                                     | 2.08 sec: 1.40x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 2.90 us: 1.38x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.22 sec: 1.37x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 15.7 ms: 1.36x faster                                                        |
| mako                     | 14.7 ms                                                      | 10.8 ms: 1.36x faster                                                        |
| thrift                   | 1.18 ms                                                      | 864 us: 1.36x faster                                                         |
| fannkuch                 | 483 ms                                                       | 355 ms: 1.36x faster                                                         |
| sqlalchemy_declarative   | 190 ms                                                       | 141 ms: 1.35x faster                                                         |
| pprint_pformat           | 2.15 sec                                                     | 1.61 sec: 1.34x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 785 ms: 1.34x faster                                                         |
| xml_etree_process        | 75.9 ms                                                      | 58.5 ms: 1.30x faster                                                        |
| nqueens                  | 115 ms                                                       | 88.8 ms: 1.29x faster                                                        |
| sympy_sum                | 193 ms                                                       | 150 ms: 1.29x faster                                                         |
| genshi_text              | 31.4 ms                                                      | 24.5 ms: 1.28x faster                                                        |
| sqlalchemy_imperative    | 22.7 ms                                                      | 17.7 ms: 1.28x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 114 ms: 1.26x faster                                                         |
| sympy_str                | 360 ms                                                       | 286 ms: 1.26x faster                                                         |
| 2to3                     | 350 ms                                                       | 279 ms: 1.25x faster                                                         |
| json_dumps               | 14.5 ms                                                      | 11.7 ms: 1.25x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 65.4 ms: 1.24x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 56.6 ms: 1.24x faster                                                        |
| sympy_expand             | 600 ms                                                       | 487 ms: 1.23x faster                                                         |
| sympy_integrate          | 28.2 ms                                                      | 22.9 ms: 1.23x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.47 sec: 1.21x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 940 us: 1.21x faster                                                         |
| docutils                 | 3.41 sec                                                     | 2.84 sec: 1.20x faster                                                       |
| scimark_fft              | 361 ms                                                       | 305 ms: 1.18x faster                                                         |
| xml_etree_parse          | 160 ms                                                       | 136 ms: 1.18x faster                                                         |
| genshi_xml               | 63.3 ms                                                      | 55.0 ms: 1.15x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 97.6 ms: 1.13x faster                                                        |
| json_loads               | 30.3 us                                                      | 26.9 us: 1.13x faster                                                        |
| meteor_contest           | 138 ms                                                       | 124 ms: 1.12x faster                                                         |
| regex_dna                | 261 ms                                                       | 236 ms: 1.11x faster                                                         |
| xml_etree_generate       | 92.3 ms                                                      | 83.5 ms: 1.11x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.66 ms: 1.09x faster                                                        |
| pidigits                 | 271 ms                                                       | 254 ms: 1.07x faster                                                         |
| sqlite_synth             | 2.99 us                                                      | 2.81 us: 1.06x faster                                                        |
| json                     | 5.86 ms                                                      | 5.56 ms: 1.06x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 25.9 ms: 1.05x faster                                                        |
| async_generators         | 421 ms                                                       | 410 ms: 1.03x faster                                                         |
| regex_effbot             | 3.09 ms                                                      | 3.04 ms: 1.02x faster                                                        |
| asyncio_websockets       | 390 ms                                                       | 387 ms: 1.01x faster                                                         |
| telco                    | 7.23 ms                                                      | 7.93 ms: 1.10x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 9.02 ms: 1.23x slower                                                        |
| coverage                 | 63.3 ms                                                      | 79.3 ms: 1.25x slower                                                        |
| python_startup           | 11.5 ms                                                      | 16.0 ms: 1.39x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.68 ms: 1.52x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 6.10 ms: 1.79x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 1.29 sec: 202.96x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.28x faster                                                                 |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (11) of results/bm-20250129-3.14.0a4+-5ff2fbc/bm-20250129-pythonperf2-x86_64-python-5ff2fbc026b14eadd41b-3.14.0a4+-5ff2fbc.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.364x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.27x