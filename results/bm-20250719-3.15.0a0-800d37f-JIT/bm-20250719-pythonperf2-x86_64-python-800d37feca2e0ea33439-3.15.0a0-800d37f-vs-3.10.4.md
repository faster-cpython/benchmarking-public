# Results vs. 3.10.4

- fork: python
- ref: 800d37feca2e0ea33439
- machine: linux-x86_64
- commit hash: 800d37f
- commit date: 2025-07-19
- overall geometric mean: 1.329x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.25x faster
- Memory change: 1.41x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 286 ms: 1.22x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.92 sec: 1.17x faster                                                      |
| html5lib       | 94.6 ms                                                      | 66.2 ms: 1.43x faster                                                       |
| Geometric mean | (ref)                                                        | 1.27x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 624 ms: 2.56x faster                                                        |
| async_tree_none         | 692 ms                                                       | 274 ms: 2.53x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 330 ms: 2.48x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 502 ms: 1.86x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.34x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 64.3 ms: 1.73x faster                                                       |
| nbody          | 134 ms                                                       | 103 ms: 1.30x faster                                                        |
| pidigits       | 271 ms                                                       | 255 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                        | 1.34x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 133 ms: 1.43x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 23.0 ms: 1.18x faster                                                       |
| regex_dna      | 261 ms                                                       | 223 ms: 1.17x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.57 ms: 1.16x slower                                                       |
| Geometric mean | (ref)                                                        | 1.14x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 197 us: 1.58x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 1.91 sec: 1.52x faster                                                      |
| xml_etree_process    | 75.9 ms                                                      | 55.6 ms: 1.37x faster                                                       |
| pickle_pure_python   | 455 us                                                       | 333 us: 1.36x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.1 us: 1.21x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 79.2 ms: 1.16x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 138 ms: 1.16x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 96.7 ms: 1.14x faster                                                       |
| unpickle             | 13.5 us                                                      | 14.9 us: 1.10x slower                                                       |
| unpickle_list        | 4.65 us                                                      | 5.16 us: 1.11x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 35.0 us: 1.19x slower                                                       |
| pickle_list          | 4.12 us                                                      | 5.04 us: 1.22x slower                                                       |
| pickle               | 9.89 us                                                      | 12.5 us: 1.26x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.12x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 8.71 ms: 1.19x slower                                                       |
| python_startup         | 11.5 ms                                                      | 15.2 ms: 1.32x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.25x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.96 ms: 1.48x faster                                                       |
| django_template | 50.2 ms                                                      | 35.6 ms: 1.41x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 23.1 ms: 1.36x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 53.9 ms: 1.17x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.35x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 171 us: 3.14x faster                                                        |
| deltablue                | 7.50 ms                                                      | 2.91 ms: 2.58x faster                                                       |
| async_tree_io            | 1.60 sec                                                     | 624 ms: 2.56x faster                                                        |
| async_tree_none          | 692 ms                                                       | 274 ms: 2.53x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 330 ms: 2.48x faster                                                        |
| mdp                      | 3.01 sec                                                     | 1.28 sec: 2.35x faster                                                      |
| richards_super           | 90.6 ms                                                      | 41.1 ms: 2.21x faster                                                       |
| richards                 | 75.1 ms                                                      | 34.9 ms: 2.15x faster                                                       |
| asyncio_tcp              | 779 ms                                                       | 370 ms: 2.11x faster                                                        |
| go                       | 262 ms                                                       | 127 ms: 2.05x faster                                                        |
| generators               | 57.3 ms                                                      | 29.2 ms: 1.97x faster                                                       |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                      |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 502 ms: 1.86x faster                                                        |
| chaos                    | 109 ms                                                       | 60.5 ms: 1.79x faster                                                       |
| pyflate                  | 733 ms                                                       | 411 ms: 1.78x faster                                                        |
| logging_silent           | 167 ns                                                       | 93.8 ns: 1.78x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 28.0 us: 1.77x faster                                                       |
| pylint                   | 566 ms                                                       | 324 ms: 1.75x faster                                                        |
| float                    | 111 ms                                                       | 64.3 ms: 1.73x faster                                                       |
| spectral_norm            | 139 ms                                                       | 80.6 ms: 1.73x faster                                                       |
| scimark_lu               | 167 ms                                                       | 96.7 ms: 1.73x faster                                                       |
| scimark_sor              | 180 ms                                                       | 105 ms: 1.72x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 63.3 ms: 1.70x faster                                                       |
| deepcopy                 | 468 us                                                       | 280 us: 1.67x faster                                                        |
| raytrace                 | 489 ms                                                       | 293 ms: 1.67x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 197 us: 1.58x faster                                                        |
| comprehensions           | 26.7 us                                                      | 17.2 us: 1.55x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 77.1 ms: 1.55x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 6.18 ms: 1.52x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 1.91 sec: 1.52x faster                                                      |
| mako                     | 14.7 ms                                                      | 9.96 ms: 1.48x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.61 us: 1.46x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.12 us: 1.45x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.49 sec: 1.44x faster                                                      |
| html5lib                 | 94.6 ms                                                      | 66.2 ms: 1.43x faster                                                       |
| regex_compile            | 190 ms                                                       | 133 ms: 1.43x faster                                                        |
| pprint_safe_repr         | 1.05 sec                                                     | 737 ms: 1.42x faster                                                        |
| django_template          | 50.2 ms                                                      | 35.6 ms: 1.41x faster                                                       |
| thrift                   | 1.18 ms                                                      | 850 us: 1.38x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 59.2 ms: 1.37x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 55.6 ms: 1.37x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 333 us: 1.36x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 23.1 ms: 1.36x faster                                                       |
| coroutines               | 30.3 ms                                                      | 22.3 ms: 1.36x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 3.01 us: 1.33x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.26 sec: 1.33x faster                                                      |
| nbody                    | 134 ms                                                       | 103 ms: 1.30x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                                       |
| sympy_sum                | 193 ms                                                       | 151 ms: 1.27x faster                                                        |
| fannkuch                 | 483 ms                                                       | 380 ms: 1.27x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 17.0 ms: 1.26x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 22.5 ms: 1.25x faster                                                       |
| nqueens                  | 115 ms                                                       | 92.5 ms: 1.24x faster                                                       |
| sympy_str                | 360 ms                                                       | 290 ms: 1.24x faster                                                        |
| 2to3                     | 350 ms                                                       | 286 ms: 1.22x faster                                                        |
| unpack_sequence          | 59.9 ns                                                      | 49.1 ns: 1.22x faster                                                       |
| sympy_expand             | 600 ms                                                       | 495 ms: 1.21x faster                                                        |
| json_loads               | 30.3 us                                                      | 25.1 us: 1.21x faster                                                       |
| scimark_fft              | 361 ms                                                       | 303 ms: 1.19x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 23.0 ms: 1.18x faster                                                       |
| regex_dna                | 261 ms                                                       | 223 ms: 1.17x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 53.9 ms: 1.17x faster                                                       |
| docutils                 | 3.41 sec                                                     | 2.92 sec: 1.17x faster                                                      |
| xml_etree_generate       | 92.3 ms                                                      | 79.2 ms: 1.16x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 138 ms: 1.16x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 96.7 ms: 1.14x faster                                                       |
| meteor_contest           | 138 ms                                                       | 121 ms: 1.14x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 1.00 ms: 1.14x faster                                                       |
| json                     | 5.86 ms                                                      | 5.35 ms: 1.10x faster                                                       |
| pidigits                 | 271 ms                                                       | 255 ms: 1.06x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.84 us: 1.05x faster                                                       |
| asyncio_websockets       | 390 ms                                                       | 382 ms: 1.02x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.04 ms: 1.01x faster                                                       |
| async_generators         | 421 ms                                                       | 458 ms: 1.09x slower                                                        |
| unpickle                 | 13.5 us                                                      | 14.9 us: 1.10x slower                                                       |
| unpickle_list            | 4.65 us                                                      | 5.16 us: 1.11x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.57 ms: 1.16x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 35.0 us: 1.19x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 8.71 ms: 1.19x slower                                                       |
| pickle_list              | 4.12 us                                                      | 5.04 us: 1.22x slower                                                       |
| pickle                   | 9.89 us                                                      | 12.5 us: 1.26x slower                                                       |
| coverage                 | 63.3 ms                                                      | 83.7 ms: 1.32x slower                                                       |
| python_startup           | 11.5 ms                                                      | 15.2 ms: 1.32x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.86 ms: 1.62x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 6.47 ms: 1.89x slower                                                       |
| telco                    | 7.23 ms                                                      | 161 ms: 22.30x slower                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 1.51 sec: 237.03x slower                                                    |
| Geometric mean           | (ref)                                                        | 1.23x faster                                                                |
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250719-3.15.0a0-800d37f-JIT/bm-20250719-pythonperf2-x86_64-python-800d37feca2e0ea33439-3.15.0a0-800d37f.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.329x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.28x
- 99% likely to have a speedup of 1.25x

# Memory
- memory change: 1.41x