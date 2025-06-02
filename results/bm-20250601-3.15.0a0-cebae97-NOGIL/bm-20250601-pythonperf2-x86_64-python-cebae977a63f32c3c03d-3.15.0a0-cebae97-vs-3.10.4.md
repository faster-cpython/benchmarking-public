# Results vs. 3.10.4

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-x86_64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.014x faster
- HPT reliability: 87.91%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.67x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 365 ms: 1.04x slower                                                        |
| docutils       | 3.41 sec                                                     | 3.29 sec: 1.04x faster                                                      |
| html5lib       | 94.6 ms                                                      | 76.6 ms: 1.24x faster                                                       |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 642 ms: 2.49x faster                                                        |
| async_tree_none         | 692 ms                                                       | 296 ms: 2.34x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 360 ms: 2.28x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 638 ms: 1.47x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.10x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 81.7 ms: 1.36x faster                                                       |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| nbody          | 134 ms                                                       | 136 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                        | 1.13x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_dna      | 261 ms                                                       | 242 ms: 1.08x faster                                                        |
| regex_compile  | 190 ms                                                       | 178 ms: 1.07x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 26.0 ms: 1.04x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.40 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                        | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.92 sec                                                     | 2.78 sec: 1.05x faster                                                      |
| unpickle_pure_python | 312 us                                                       | 299 us: 1.04x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 167 ms: 1.04x slower                                                        |
| json_dumps           | 14.5 ms                                                      | 15.6 ms: 1.08x slower                                                       |
| xml_etree_process    | 75.9 ms                                                      | 87.2 ms: 1.15x slower                                                       |
| json_loads           | 30.3 us                                                      | 35.6 us: 1.17x slower                                                       |
| unpickle_list        | 4.65 us                                                      | 6.08 us: 1.31x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 39.9 us: 1.35x slower                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 126 ms: 1.37x slower                                                        |
| pickle_list          | 4.12 us                                                      | 6.10 us: 1.48x slower                                                       |
| unpickle             | 13.5 us                                                      | 21.2 us: 1.57x slower                                                       |
| pickle               | 9.89 us                                                      | 15.8 us: 1.59x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.20x slower                                                                |

Benchmark hidden because not significant (2): xml_etree_iterparse, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 12.7 ms: 1.73x slower                                                       |
| python_startup         | 11.5 ms                                                      | 21.3 ms: 1.85x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.79x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 52.7 ms: 1.05x slower                                                       |
| genshi_text     | 31.4 ms                                                      | 35.7 ms: 1.14x slower                                                       |
| genshi_xml      | 63.3 ms                                                      | 72.9 ms: 1.15x slower                                                       |
| mako            | 14.7 ms                                                      | 19.8 ms: 1.35x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.17x slower                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io            | 1.60 sec                                                     | 642 ms: 2.49x faster                                                        |
| async_tree_none          | 692 ms                                                       | 296 ms: 2.34x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 360 ms: 2.28x faster                                                        |
| typing_runtime_protocols | 537 us                                                       | 261 us: 2.05x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 426 ms: 1.83x faster                                                        |
| deltablue                | 7.50 ms                                                      | 4.14 ms: 1.81x faster                                                       |
| go                       | 262 ms                                                       | 154 ms: 1.70x faster                                                        |
| mdp                      | 3.01 sec                                                     | 1.83 sec: 1.64x faster                                                      |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.90 sec: 1.63x faster                                                      |
| generators               | 57.3 ms                                                      | 36.1 ms: 1.59x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 638 ms: 1.47x faster                                                        |
| pylint                   | 566 ms                                                       | 396 ms: 1.43x faster                                                        |
| pyflate                  | 733 ms                                                       | 535 ms: 1.37x faster                                                        |
| float                    | 111 ms                                                       | 81.7 ms: 1.36x faster                                                       |
| chaos                    | 109 ms                                                       | 82.7 ms: 1.31x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 7.57 ms: 1.24x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 76.6 ms: 1.24x faster                                                       |
| raytrace                 | 489 ms                                                       | 396 ms: 1.23x faster                                                        |
| deepcopy                 | 468 us                                                       | 383 us: 1.22x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 66.7 ms: 1.22x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 41.1 us: 1.21x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.40 sec: 1.20x faster                                                      |
| scimark_sor              | 180 ms                                                       | 153 ms: 1.18x faster                                                        |
| comprehensions           | 26.7 us                                                      | 23.2 us: 1.15x faster                                                       |
| coroutines               | 30.3 ms                                                      | 26.4 ms: 1.15x faster                                                       |
| richards_super           | 90.6 ms                                                      | 79.4 ms: 1.14x faster                                                       |
| scimark_lu               | 167 ms                                                       | 149 ms: 1.12x faster                                                        |
| richards                 | 75.1 ms                                                      | 67.6 ms: 1.11x faster                                                       |
| regex_dna                | 261 ms                                                       | 242 ms: 1.08x faster                                                        |
| pidigits                 | 271 ms                                                       | 251 ms: 1.08x faster                                                        |
| regex_compile            | 190 ms                                                       | 178 ms: 1.07x faster                                                        |
| gc_traversal             | 3.42 ms                                                      | 3.22 ms: 1.06x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 101 ms: 1.06x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 20.2 ms: 1.06x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.78 sec: 1.05x faster                                                      |
| unpack_sequence          | 59.9 ns                                                      | 57.3 ns: 1.05x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 299 us: 1.04x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 26.0 ms: 1.04x faster                                                       |
| docutils                 | 3.41 sec                                                     | 3.29 sec: 1.04x faster                                                      |
| asyncio_websockets       | 390 ms                                                       | 377 ms: 1.03x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 116 ms: 1.03x faster                                                        |
| logging_simple           | 8.88 us                                                      | 8.75 us: 1.01x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 27.9 ms: 1.01x faster                                                       |
| logging_format           | 9.64 us                                                      | 9.76 us: 1.01x slower                                                       |
| nbody                    | 134 ms                                                       | 136 ms: 1.02x slower                                                        |
| sqlite_synth             | 2.99 us                                                      | 3.07 us: 1.03x slower                                                       |
| sympy_sum                | 193 ms                                                       | 198 ms: 1.03x slower                                                        |
| 2to3                     | 350 ms                                                       | 365 ms: 1.04x slower                                                        |
| xml_etree_parse          | 160 ms                                                       | 167 ms: 1.04x slower                                                        |
| thrift                   | 1.18 ms                                                      | 1.23 ms: 1.05x slower                                                       |
| spectral_norm            | 139 ms                                                       | 146 ms: 1.05x slower                                                        |
| django_template          | 50.2 ms                                                      | 52.7 ms: 1.05x slower                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 4.25 us: 1.06x slower                                                       |
| json_dumps               | 14.5 ms                                                      | 15.6 ms: 1.08x slower                                                       |
| sympy_str                | 360 ms                                                       | 389 ms: 1.08x slower                                                        |
| nqueens                  | 115 ms                                                       | 126 ms: 1.10x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.40 ms: 1.10x slower                                                       |
| sympy_expand             | 600 ms                                                       | 674 ms: 1.12x slower                                                        |
| genshi_text              | 31.4 ms                                                      | 35.7 ms: 1.14x slower                                                       |
| meteor_contest           | 138 ms                                                       | 158 ms: 1.14x slower                                                        |
| fannkuch                 | 483 ms                                                       | 554 ms: 1.15x slower                                                        |
| xml_etree_process        | 75.9 ms                                                      | 87.2 ms: 1.15x slower                                                       |
| genshi_xml               | 63.3 ms                                                      | 72.9 ms: 1.15x slower                                                       |
| json                     | 5.86 ms                                                      | 6.77 ms: 1.15x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.05 ms: 1.16x slower                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 1.23 sec: 1.17x slower                                                      |
| json_loads               | 30.3 us                                                      | 35.6 us: 1.17x slower                                                       |
| pprint_pformat           | 2.15 sec                                                     | 2.53 sec: 1.18x slower                                                      |
| async_generators         | 421 ms                                                       | 529 ms: 1.26x slower                                                        |
| scimark_fft              | 361 ms                                                       | 459 ms: 1.27x slower                                                        |
| unpickle_list            | 4.65 us                                                      | 6.08 us: 1.31x slower                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 1.50 ms: 1.31x slower                                                       |
| mako                     | 14.7 ms                                                      | 19.8 ms: 1.35x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 39.9 us: 1.35x slower                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 126 ms: 1.37x slower                                                        |
| pickle_list              | 4.12 us                                                      | 6.10 us: 1.48x slower                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 7.83 ms: 1.54x slower                                                       |
| unpickle                 | 13.5 us                                                      | 21.2 us: 1.57x slower                                                       |
| pickle                   | 9.89 us                                                      | 15.8 us: 1.59x slower                                                       |
| telco                    | 7.23 ms                                                      | 12.2 ms: 1.69x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 12.7 ms: 1.73x slower                                                       |
| python_startup           | 11.5 ms                                                      | 21.3 ms: 1.85x slower                                                       |
| coverage                 | 63.3 ms                                                      | 135 ms: 2.14x slower                                                        |
| logging_silent           | 167 ns                                                       | 791 ns: 4.73x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 62.1 ms: 9.75x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.01x slower                                                                |

Benchmark hidden because not significant (2): xml_etree_iterparse, pickle_pure_python
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (15) of results/bm-20250601-3.15.0a0-cebae97-NOGIL/bm-20250601-pythonperf2-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.014x faster

# HPT report

- Reliability score: 87.91% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.67x