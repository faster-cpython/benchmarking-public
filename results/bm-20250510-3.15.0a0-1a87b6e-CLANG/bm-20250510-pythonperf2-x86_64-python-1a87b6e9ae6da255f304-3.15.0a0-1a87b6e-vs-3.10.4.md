# Results vs. 3.10.4

- fork: python
- ref: 1a87b6e9ae6da255f304
- machine: linux-x86_64
- commit hash: 1a87b6e
- commit date: 2025-05-10
- overall geometric mean: 1.395x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.28x faster
- Memory change: 1.37x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 279 ms: 1.26x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.89 sec: 1.18x faster                                                      |
| html5lib       | 94.6 ms                                                      | 65.6 ms: 1.44x faster                                                       |
| Geometric mean | (ref)                                                        | 1.29x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 604 ms: 2.65x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 313 ms: 2.62x faster                                                        |
| async_tree_none         | 692 ms                                                       | 272 ms: 2.54x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 518 ms: 1.81x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.38x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 65.8 ms: 1.69x faster                                                       |
| nbody          | 134 ms                                                       | 94.6 ms: 1.42x faster                                                       |
| pidigits       | 271 ms                                                       | 292 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 131 ms: 1.45x faster                                                        |
| regex_dna      | 261 ms                                                       | 242 ms: 1.08x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 28.3 ms: 1.04x slower                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.52 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 202 us: 1.54x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 313 us: 1.46x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.01 sec: 1.45x faster                                                      |
| xml_etree_process    | 75.9 ms                                                      | 56.3 ms: 1.35x faster                                                       |
| json_dumps           | 14.5 ms                                                      | 12.0 ms: 1.21x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 80.0 ms: 1.15x faster                                                       |
| json_loads           | 30.3 us                                                      | 26.3 us: 1.15x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 103 ms: 1.07x faster                                                        |
| unpickle             | 13.5 us                                                      | 13.7 us: 1.02x slower                                                       |
| xml_etree_parse      | 160 ms                                                       | 167 ms: 1.04x slower                                                        |
| unpickle_list        | 4.65 us                                                      | 4.92 us: 1.06x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 31.3 us: 1.06x slower                                                       |
| pickle_list          | 4.12 us                                                      | 4.48 us: 1.09x slower                                                       |
| pickle               | 9.89 us                                                      | 12.0 us: 1.22x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.12x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.7 ms: 1.19x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 8.90 ms: 1.22x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 34.4 ms: 1.46x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 22.1 ms: 1.42x faster                                                       |
| mako            | 14.7 ms                                                      | 11.1 ms: 1.33x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 52.2 ms: 1.21x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.35x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 164 us: 3.28x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 604 ms: 2.65x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 313 ms: 2.62x faster                                                        |
| async_tree_none          | 692 ms                                                       | 272 ms: 2.54x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.05 ms: 2.46x faster                                                       |
| mdp                      | 3.01 sec                                                     | 1.27 sec: 2.36x faster                                                      |
| go                       | 262 ms                                                       | 121 ms: 2.16x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 371 ms: 2.10x faster                                                        |
| scimark_sor              | 180 ms                                                       | 91.5 ms: 1.97x faster                                                       |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                      |
| raytrace                 | 489 ms                                                       | 253 ms: 1.94x faster                                                        |
| chaos                    | 109 ms                                                       | 56.9 ms: 1.91x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 26.2 us: 1.90x faster                                                       |
| scimark_lu               | 167 ms                                                       | 88.1 ms: 1.89x faster                                                       |
| generators               | 57.3 ms                                                      | 30.4 ms: 1.89x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 57.5 ms: 1.87x faster                                                       |
| richards_super           | 90.6 ms                                                      | 48.5 ms: 1.87x faster                                                       |
| deepcopy                 | 468 us                                                       | 257 us: 1.82x faster                                                        |
| pyflate                  | 733 ms                                                       | 405 ms: 1.81x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 518 ms: 1.81x faster                                                        |
| pylint                   | 566 ms                                                       | 317 ms: 1.78x faster                                                        |
| richards                 | 75.1 ms                                                      | 42.3 ms: 1.78x faster                                                       |
| float                    | 111 ms                                                       | 65.8 ms: 1.69x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 5.62 ms: 1.68x faster                                                       |
| comprehensions           | 26.7 us                                                      | 16.5 us: 1.62x faster                                                       |
| spectral_norm            | 139 ms                                                       | 86.0 ms: 1.62x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 76.3 ms: 1.56x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 202 us: 1.54x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 2.70 us: 1.48x faster                                                       |
| django_template          | 50.2 ms                                                      | 34.4 ms: 1.46x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 313 us: 1.46x faster                                                        |
| thrift                   | 1.18 ms                                                      | 809 us: 1.45x faster                                                        |
| coroutines               | 30.3 ms                                                      | 20.9 ms: 1.45x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.01 sec: 1.45x faster                                                      |
| regex_compile            | 190 ms                                                       | 131 ms: 1.45x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 65.6 ms: 1.44x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 22.1 ms: 1.42x faster                                                       |
| nbody                    | 134 ms                                                       | 94.6 ms: 1.42x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.54 sec: 1.39x faster                                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 758 ms: 1.38x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 58.9 ms: 1.38x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.45 us: 1.38x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 56.3 ms: 1.35x faster                                                       |
| logging_format           | 9.64 us                                                      | 7.19 us: 1.34x faster                                                       |
| mako                     | 14.7 ms                                                      | 11.1 ms: 1.33x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.26 sec: 1.33x faster                                                      |
| scimark_fft              | 361 ms                                                       | 279 ms: 1.29x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 21.8 ms: 1.29x faster                                                       |
| sympy_sum                | 193 ms                                                       | 149 ms: 1.29x faster                                                        |
| nqueens                  | 115 ms                                                       | 89.4 ms: 1.29x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 16.6 ms: 1.28x faster                                                       |
| fannkuch                 | 483 ms                                                       | 379 ms: 1.27x faster                                                        |
| sympy_str                | 360 ms                                                       | 285 ms: 1.26x faster                                                        |
| 2to3                     | 350 ms                                                       | 279 ms: 1.26x faster                                                        |
| sympy_expand             | 600 ms                                                       | 485 ms: 1.24x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 940 us: 1.21x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 52.2 ms: 1.21x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 12.0 ms: 1.21x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.30 ms: 1.18x faster                                                       |
| docutils                 | 3.41 sec                                                     | 2.89 sec: 1.18x faster                                                      |
| xml_etree_generate       | 92.3 ms                                                      | 80.0 ms: 1.15x faster                                                       |
| json_loads               | 30.3 us                                                      | 26.3 us: 1.15x faster                                                       |
| json                     | 5.86 ms                                                      | 5.32 ms: 1.10x faster                                                       |
| regex_dna                | 261 ms                                                       | 242 ms: 1.08x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.80 us: 1.07x faster                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 103 ms: 1.07x faster                                                        |
| meteor_contest           | 138 ms                                                       | 135 ms: 1.02x faster                                                        |
| asyncio_websockets       | 390 ms                                                       | 386 ms: 1.01x faster                                                        |
| unpickle                 | 13.5 us                                                      | 13.7 us: 1.02x slower                                                       |
| xml_etree_parse          | 160 ms                                                       | 167 ms: 1.04x slower                                                        |
| regex_v8                 | 27.2 ms                                                      | 28.3 ms: 1.04x slower                                                       |
| unpickle_list            | 4.65 us                                                      | 4.92 us: 1.06x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 31.3 us: 1.06x slower                                                       |
| async_generators         | 421 ms                                                       | 447 ms: 1.06x slower                                                        |
| pidigits                 | 271 ms                                                       | 292 ms: 1.08x slower                                                        |
| pickle_list              | 4.12 us                                                      | 4.48 us: 1.09x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.52 ms: 1.14x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.7 ms: 1.19x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 8.90 ms: 1.22x slower                                                       |
| pickle                   | 9.89 us                                                      | 12.0 us: 1.22x slower                                                       |
| coverage                 | 63.3 ms                                                      | 77.6 ms: 1.23x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 5.42 ms: 1.59x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.90 ms: 1.64x slower                                                       |
| logging_silent           | 167 ns                                                       | 504 ns: 3.01x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 1.22 sec: 192.01x slower                                                    |
| Geometric mean           | (ref)                                                        | 1.26x faster                                                                |

Benchmark hidden because not significant (2): unpack_sequence, telco
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (8) of results/bm-20250510-3.15.0a0-1a87b6e-CLANG/bm-20250510-pythonperf2-x86_64-python-1a87b6e9ae6da255f304-3.15.0a0-1a87b6e.json: bpe_tokeniser, djangocms, many_optionals, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.395x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.32x
- 95% likely to have a speedup of 1.30x
- 99% likely to have a speedup of 1.28x

# Memory
- memory change: 1.37x