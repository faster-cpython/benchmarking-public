# Results vs. 3.10.4

- fork: savannahostrowski
- ref: poptimize
- machine: linux-x86_64
- commit hash: c6edbf9
- commit date: 2025-09-15
- overall geometric mean: 1.334x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.26x faster
- Memory change: 1.40x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250915-pythonperf2-x86_64-savannahostrowski-poptimize-3.15.0a0-c6edbf9 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 286 ms: 1.22x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                                      |
| html5lib       | 94.6 ms                                                      | 66.4 ms: 1.43x faster                                                       |
| Geometric mean | (ref)                                                        | 1.27x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250915-pythonperf2-x86_64-savannahostrowski-poptimize-3.15.0a0-c6edbf9 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 616 ms: 2.60x faster                                                        |
| async_tree_none         | 692 ms                                                       | 273 ms: 2.53x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 330 ms: 2.48x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 503 ms: 1.86x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.35x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250915-pythonperf2-x86_64-savannahostrowski-poptimize-3.15.0a0-c6edbf9 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 67.7 ms: 1.64x faster                                                       |
| nbody          | 134 ms                                                       | 96.6 ms: 1.39x faster                                                       |
| pidigits       | 271 ms                                                       | 255 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                        | 1.34x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250915-pythonperf2-x86_64-savannahostrowski-poptimize-3.15.0a0-c6edbf9 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 132 ms: 1.44x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 23.4 ms: 1.16x faster                                                       |
| regex_dna      | 261 ms                                                       | 226 ms: 1.16x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.64 ms: 1.18x slower                                                       |
| Geometric mean | (ref)                                                        | 1.13x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250915-pythonperf2-x86_64-savannahostrowski-poptimize-3.15.0a0-c6edbf9 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 192 us: 1.62x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 1.89 sec: 1.54x faster                                                      |
| json_dumps           | 14.5 ms                                                      | 10.1 ms: 1.44x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 324 us: 1.41x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 56.0 ms: 1.36x faster                                                       |
| json_loads           | 30.3 us                                                      | 26.0 us: 1.16x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 79.7 ms: 1.16x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 97.4 ms: 1.13x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 141 ms: 1.13x faster                                                        |
| Geometric mean       | (ref)                                                        | 1.32x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250915-pythonperf2-x86_64-savannahostrowski-poptimize-3.15.0a0-c6edbf9 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.85 ms: 1.21x slower                                                       |
| python_startup         | 11.5 ms                                                      | 15.3 ms: 1.33x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.27x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250915-pythonperf2-x86_64-savannahostrowski-poptimize-3.15.0a0-c6edbf9 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.62 ms: 1.53x faster                                                       |
| django_template | 50.2 ms                                                      | 35.5 ms: 1.42x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 23.4 ms: 1.34x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 53.7 ms: 1.18x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.36x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250915-pythonperf2-x86_64-savannahostrowski-poptimize-3.15.0a0-c6edbf9 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 171 us: 3.15x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 616 ms: 2.60x faster                                                        |
| async_tree_none          | 692 ms                                                       | 273 ms: 2.53x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 330 ms: 2.48x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.18 ms: 2.36x faster                                                       |
| mdp                      | 3.01 sec                                                     | 1.29 sec: 2.32x faster                                                      |
| go                       | 262 ms                                                       | 120 ms: 2.19x faster                                                        |
| generators               | 57.3 ms                                                      | 29.5 ms: 1.94x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 26.1 us: 1.91x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 503 ms: 1.86x faster                                                        |
| pyflate                  | 733 ms                                                       | 397 ms: 1.85x faster                                                        |
| chaos                    | 109 ms                                                       | 59.2 ms: 1.83x faster                                                       |
| logging_silent           | 167 ns                                                       | 91.9 ns: 1.82x faster                                                       |
| richards_super           | 90.6 ms                                                      | 50.5 ms: 1.79x faster                                                       |
| deepcopy                 | 468 us                                                       | 262 us: 1.79x faster                                                        |
| scimark_lu               | 167 ms                                                       | 94.1 ms: 1.77x faster                                                       |
| scimark_sor              | 180 ms                                                       | 102 ms: 1.76x faster                                                        |
| raytrace                 | 489 ms                                                       | 278 ms: 1.76x faster                                                        |
| pylint                   | 566 ms                                                       | 322 ms: 1.76x faster                                                        |
| spectral_norm            | 139 ms                                                       | 79.6 ms: 1.75x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 62.2 ms: 1.73x faster                                                       |
| richards                 | 75.1 ms                                                      | 44.3 ms: 1.69x faster                                                       |
| float                    | 111 ms                                                       | 67.7 ms: 1.64x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 192 us: 1.62x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 5.90 ms: 1.60x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 77.1 ms: 1.55x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 1.89 sec: 1.54x faster                                                      |
| comprehensions           | 26.7 us                                                      | 17.4 us: 1.53x faster                                                       |
| mako                     | 14.7 ms                                                      | 9.62 ms: 1.53x faster                                                       |
| logging_simple           | 8.88 us                                                      | 5.86 us: 1.51x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.44 us: 1.50x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.49 sec: 1.44x faster                                                      |
| json_dumps               | 14.5 ms                                                      | 10.1 ms: 1.44x faster                                                       |
| regex_compile            | 190 ms                                                       | 132 ms: 1.44x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 734 ms: 1.43x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 66.4 ms: 1.43x faster                                                       |
| django_template          | 50.2 ms                                                      | 35.5 ms: 1.42x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 324 us: 1.41x faster                                                        |
| nbody                    | 134 ms                                                       | 96.6 ms: 1.39x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 58.5 ms: 1.39x faster                                                       |
| thrift                   | 1.18 ms                                                      | 854 us: 1.38x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 2.94 us: 1.37x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.23 sec: 1.36x faster                                                      |
| xml_etree_process        | 75.9 ms                                                      | 56.0 ms: 1.36x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 15.8 ms: 1.35x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 23.4 ms: 1.34x faster                                                       |
| coroutines               | 30.3 ms                                                      | 22.6 ms: 1.34x faster                                                       |
| sympy_sum                | 193 ms                                                       | 152 ms: 1.27x faster                                                        |
| fannkuch                 | 483 ms                                                       | 380 ms: 1.27x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 22.4 ms: 1.26x faster                                                       |
| sympy_str                | 360 ms                                                       | 291 ms: 1.24x faster                                                        |
| nqueens                  | 115 ms                                                       | 93.3 ms: 1.23x faster                                                       |
| 2to3                     | 350 ms                                                       | 286 ms: 1.22x faster                                                        |
| scimark_fft              | 361 ms                                                       | 298 ms: 1.21x faster                                                        |
| sympy_expand             | 600 ms                                                       | 498 ms: 1.21x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 53.7 ms: 1.18x faster                                                       |
| docutils                 | 3.41 sec                                                     | 2.91 sec: 1.17x faster                                                      |
| json_loads               | 30.3 us                                                      | 26.0 us: 1.16x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 23.4 ms: 1.16x faster                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 79.7 ms: 1.16x faster                                                       |
| regex_dna                | 261 ms                                                       | 226 ms: 1.16x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 97.4 ms: 1.13x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 141 ms: 1.13x faster                                                        |
| meteor_contest           | 138 ms                                                       | 123 ms: 1.13x faster                                                        |
| json                     | 5.86 ms                                                      | 5.45 ms: 1.08x faster                                                       |
| sqlite_synth             | 2.99 us                                                      | 2.80 us: 1.07x faster                                                       |
| pidigits                 | 271 ms                                                       | 255 ms: 1.06x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.87 ms: 1.04x faster                                                       |
| asyncio_websockets       | 390 ms                                                       | 384 ms: 1.02x faster                                                        |
| async_generators         | 421 ms                                                       | 445 ms: 1.06x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.64 ms: 1.18x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 8.85 ms: 1.21x slower                                                       |
| coverage                 | 63.3 ms                                                      | 82.6 ms: 1.31x slower                                                       |
| python_startup           | 11.5 ms                                                      | 15.3 ms: 1.33x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.95 ms: 1.67x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 6.68 ms: 1.96x slower                                                       |
| telco                    | 7.23 ms                                                      | 160 ms: 22.10x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.34x faster                                                                |
Ignored benchmarks (23) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250915-3.15.0a0-c6edbf9-JIT/bm-20250915-pythonperf2-x86_64-savannahostrowski-poptimize-3.15.0a0-c6edbf9.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.334x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.26x

# Memory
- memory change: 1.40x