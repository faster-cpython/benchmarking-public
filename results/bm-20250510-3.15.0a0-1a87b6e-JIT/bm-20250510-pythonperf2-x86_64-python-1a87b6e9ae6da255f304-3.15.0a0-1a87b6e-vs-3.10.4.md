# Results vs. 3.10.4

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: linux-x86_64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.360x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.34x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 286 ms: 1.22x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.93 sec: 1.16x faster                                                      |
| html5lib       | 94.6 ms                                                      | 66.3 ms: 1.43x faster                                                       |
| Geometric mean | (ref)                                                        | 1.27x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 615 ms: 2.60x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 326 ms: 2.52x faster                                                        |
| async_tree_none         | 692 ms                                                       | 285 ms: 2.43x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 504 ms: 1.86x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.33x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 63.6 ms: 1.75x faster                                                       |
| nbody          | 134 ms                                                       | 96.5 ms: 1.39x faster                                                       |
| pidigits       | 271 ms                                                       | 257 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                        | 1.37x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 135 ms: 1.41x faster                                                        |
| regex_dna      | 261 ms                                                       | 227 ms: 1.15x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 23.7 ms: 1.14x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.33 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                        | 1.14x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 208 us: 1.50x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.02 sec: 1.44x faster                                                      |
| pickle_pure_python   | 455 us                                                       | 330 us: 1.38x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 56.7 ms: 1.34x faster                                                       |
| json_dumps           | 14.5 ms                                                      | 11.9 ms: 1.23x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 138 ms: 1.16x faster                                                        |
| json_loads           | 30.3 us                                                      | 26.5 us: 1.15x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 98.1 ms: 1.13x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 82.3 ms: 1.12x faster                                                       |
| unpickle_list        | 4.65 us                                                      | 5.00 us: 1.08x slower                                                       |
| unpickle             | 13.5 us                                                      | 14.5 us: 1.08x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 36.3 us: 1.23x slower                                                       |
| pickle_list          | 4.12 us                                                      | 5.10 us: 1.24x slower                                                       |
| pickle               | 9.89 us                                                      | 12.3 us: 1.24x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.10x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.6 ms: 1.18x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 8.80 ms: 1.20x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.4 ms: 1.41x faster                                                       |
| django_template | 50.2 ms                                                      | 36.2 ms: 1.39x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 23.6 ms: 1.33x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 53.8 ms: 1.18x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.32x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 177 us: 3.04x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 615 ms: 2.60x faster                                                        |
| deltablue                | 7.50 ms                                                      | 2.96 ms: 2.53x faster                                                       |
| async_tree_memoization   | 819 ms                                                       | 326 ms: 2.52x faster                                                        |
| async_tree_none          | 692 ms                                                       | 285 ms: 2.43x faster                                                        |
| mdp                      | 3.01 sec                                                     | 1.31 sec: 2.30x faster                                                      |
| richards_super           | 90.6 ms                                                      | 42.8 ms: 2.12x faster                                                       |
| asyncio_tcp              | 779 ms                                                       | 373 ms: 2.09x faster                                                        |
| generators               | 57.3 ms                                                      | 28.5 ms: 2.01x faster                                                       |
| richards                 | 75.1 ms                                                      | 37.4 ms: 2.01x faster                                                       |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                      |
| go                       | 262 ms                                                       | 138 ms: 1.89x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 504 ms: 1.86x faster                                                        |
| chaos                    | 109 ms                                                       | 61.4 ms: 1.77x faster                                                       |
| scimark_lu               | 167 ms                                                       | 94.7 ms: 1.76x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 28.3 us: 1.76x faster                                                       |
| float                    | 111 ms                                                       | 63.6 ms: 1.75x faster                                                       |
| pylint                   | 566 ms                                                       | 325 ms: 1.74x faster                                                        |
| scimark_sor              | 180 ms                                                       | 104 ms: 1.74x faster                                                        |
| deepcopy                 | 468 us                                                       | 274 us: 1.71x faster                                                        |
| raytrace                 | 489 ms                                                       | 288 ms: 1.70x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 66.7 ms: 1.61x faster                                                       |
| pyflate                  | 733 ms                                                       | 456 ms: 1.61x faster                                                        |
| spectral_norm            | 139 ms                                                       | 91.4 ms: 1.52x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 208 us: 1.50x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 80.4 ms: 1.48x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.02 sec: 1.44x faster                                                      |
| hexiom                   | 9.42 ms                                                      | 6.57 ms: 1.43x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 66.3 ms: 1.43x faster                                                       |
| mako                     | 14.7 ms                                                      | 10.4 ms: 1.41x faster                                                       |
| regex_compile            | 190 ms                                                       | 135 ms: 1.41x faster                                                        |
| comprehensions           | 26.7 us                                                      | 19.2 us: 1.39x faster                                                       |
| nbody                    | 134 ms                                                       | 96.5 ms: 1.39x faster                                                       |
| django_template          | 50.2 ms                                                      | 36.2 ms: 1.39x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 2.90 us: 1.38x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 330 us: 1.38x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.22 sec: 1.37x faster                                                      |
| logging_simple           | 8.88 us                                                      | 6.49 us: 1.37x faster                                                       |
| coroutines               | 30.3 ms                                                      | 22.3 ms: 1.36x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 59.9 ms: 1.35x faster                                                       |
| logging_format           | 9.64 us                                                      | 7.14 us: 1.35x faster                                                       |
| thrift                   | 1.18 ms                                                      | 877 us: 1.34x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 56.7 ms: 1.34x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 23.6 ms: 1.33x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.63 sec: 1.32x faster                                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 815 ms: 1.29x faster                                                        |
| sympy_sum                | 193 ms                                                       | 152 ms: 1.26x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 22.4 ms: 1.26x faster                                                       |
| nqueens                  | 115 ms                                                       | 92.7 ms: 1.24x faster                                                       |
| sympy_str                | 360 ms                                                       | 292 ms: 1.23x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 17.4 ms: 1.23x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 11.9 ms: 1.23x faster                                                       |
| 2to3                     | 350 ms                                                       | 286 ms: 1.22x faster                                                        |
| sympy_expand             | 600 ms                                                       | 505 ms: 1.19x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 53.8 ms: 1.18x faster                                                       |
| fannkuch                 | 483 ms                                                       | 412 ms: 1.17x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.93 sec: 1.16x faster                                                      |
| xml_etree_parse          | 160 ms                                                       | 138 ms: 1.16x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 988 us: 1.15x faster                                                        |
| regex_dna                | 261 ms                                                       | 227 ms: 1.15x faster                                                        |
| json_loads               | 30.3 us                                                      | 26.5 us: 1.15x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 23.7 ms: 1.14x faster                                                       |
| scimark_fft              | 361 ms                                                       | 319 ms: 1.13x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 98.1 ms: 1.13x faster                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 82.3 ms: 1.12x faster                                                       |
| json                     | 5.86 ms                                                      | 5.38 ms: 1.09x faster                                                       |
| pidigits                 | 271 ms                                                       | 257 ms: 1.05x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.86 us: 1.05x faster                                                       |
| meteor_contest           | 138 ms                                                       | 134 ms: 1.04x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.01 ms: 1.01x faster                                                       |
| asyncio_websockets       | 390 ms                                                       | 385 ms: 1.01x faster                                                        |
| unpack_sequence          | 59.9 ns                                                      | 63.3 ns: 1.06x slower                                                       |
| async_generators         | 421 ms                                                       | 446 ms: 1.06x slower                                                        |
| unpickle_list            | 4.65 us                                                      | 5.00 us: 1.08x slower                                                       |
| unpickle                 | 13.5 us                                                      | 14.5 us: 1.08x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.33 ms: 1.08x slower                                                       |
| telco                    | 7.23 ms                                                      | 7.94 ms: 1.10x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.6 ms: 1.18x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 8.80 ms: 1.20x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 36.3 us: 1.23x slower                                                       |
| pickle_list              | 4.12 us                                                      | 5.10 us: 1.24x slower                                                       |
| pickle                   | 9.89 us                                                      | 12.3 us: 1.24x slower                                                       |
| coverage                 | 63.3 ms                                                      | 79.6 ms: 1.26x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.81 ms: 1.60x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 6.47 ms: 1.89x slower                                                       |
| logging_silent           | 167 ns                                                       | 507 ns: 3.03x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 1.28 sec: 201.44x slower                                                    |
| Geometric mean           | (ref)                                                        | 1.23x faster                                                                |
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (8) of results/bm-20250510-3.15.0a0-1a87b6e-JIT/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: bpe_tokeniser, djangocms, many_optionals, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.360x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.29x
- 95% likely to have a speedup of 1.27x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.34x