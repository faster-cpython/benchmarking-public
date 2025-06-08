# Results vs. 3.10.4

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: linux-x86_64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.125x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.38x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 320 ms: 1.09x faster                                                        |
| docutils       | 3.41 sec                                                     | 3.14 sec: 1.09x faster                                                      |
| html5lib       | 94.6 ms                                                      | 70.7 ms: 1.34x faster                                                       |
| Geometric mean | (ref)                                                        | 1.17x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 694 ms: 2.30x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 364 ms: 2.25x faster                                                        |
| async_tree_none         | 692 ms                                                       | 313 ms: 2.21x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 672 ms: 1.39x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.00x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 72.3 ms: 1.54x faster                                                       |
| nbody          | 134 ms                                                       | 108 ms: 1.24x faster                                                        |
| pidigits       | 271 ms                                                       | 254 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.27x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 156 ms: 1.22x faster                                                        |
| regex_dna      | 261 ms                                                       | 239 ms: 1.09x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 26.1 ms: 1.04x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.29 ms: 1.06x slower                                                       |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 238 us: 1.31x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.33 sec: 1.25x faster                                                      |
| pickle_pure_python   | 455 us                                                       | 385 us: 1.18x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 71.4 ms: 1.06x faster                                                       |
| json_loads           | 30.3 us                                                      | 29.2 us: 1.04x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 115 ms: 1.04x slower                                                        |
| xml_etree_parse      | 160 ms                                                       | 170 ms: 1.06x slower                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 105 ms: 1.14x slower                                                        |
| unpickle_list        | 4.65 us                                                      | 5.58 us: 1.20x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 36.1 us: 1.22x slower                                                       |
| unpickle             | 13.5 us                                                      | 17.8 us: 1.32x slower                                                       |
| pickle_list          | 4.12 us                                                      | 5.90 us: 1.43x slower                                                       |
| pickle               | 9.89 us                                                      | 14.7 us: 1.49x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.06x slower                                                                |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.43 ms: 1.29x slower                                                       |
| python_startup         | 11.5 ms                                                      | 16.5 ms: 1.43x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.36x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 43.0 ms: 1.17x faster                                                       |
| mako            | 14.7 ms                                                      | 13.4 ms: 1.10x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 28.9 ms: 1.09x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 64.1 ms: 1.01x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.08x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 216 us: 2.48x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 694 ms: 2.30x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 364 ms: 2.25x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.34 ms: 2.25x faster                                                       |
| async_tree_none          | 692 ms                                                       | 313 ms: 2.21x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 375 ms: 2.08x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.59 sec: 1.95x faster                                                      |
| mdp                      | 3.01 sec                                                     | 1.59 sec: 1.89x faster                                                      |
| richards_super           | 90.6 ms                                                      | 48.6 ms: 1.87x faster                                                       |
| go                       | 262 ms                                                       | 143 ms: 1.83x faster                                                        |
| richards                 | 75.1 ms                                                      | 41.1 ms: 1.83x faster                                                       |
| generators               | 57.3 ms                                                      | 34.8 ms: 1.65x faster                                                       |
| pylint                   | 566 ms                                                       | 355 ms: 1.59x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 31.5 us: 1.58x faster                                                       |
| pyflate                  | 733 ms                                                       | 466 ms: 1.57x faster                                                        |
| float                    | 111 ms                                                       | 72.3 ms: 1.54x faster                                                       |
| chaos                    | 109 ms                                                       | 71.7 ms: 1.52x faster                                                       |
| raytrace                 | 489 ms                                                       | 337 ms: 1.45x faster                                                        |
| deepcopy                 | 468 us                                                       | 326 us: 1.43x faster                                                        |
| scimark_lu               | 167 ms                                                       | 119 ms: 1.41x faster                                                        |
| scimark_sor              | 180 ms                                                       | 129 ms: 1.40x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 77.0 ms: 1.40x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 672 ms: 1.39x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 7.03 ms: 1.34x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 70.7 ms: 1.34x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 238 us: 1.31x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 93.4 ms: 1.28x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 63.7 ms: 1.27x faster                                                       |
| coroutines               | 30.3 ms                                                      | 24.0 ms: 1.27x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.33 sec: 1.26x faster                                                      |
| comprehensions           | 26.7 us                                                      | 21.3 us: 1.25x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.33 sec: 1.25x faster                                                      |
| nbody                    | 134 ms                                                       | 108 ms: 1.24x faster                                                        |
| regex_compile            | 190 ms                                                       | 156 ms: 1.22x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 385 us: 1.18x faster                                                        |
| django_template          | 50.2 ms                                                      | 43.0 ms: 1.17x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 24.4 ms: 1.15x faster                                                       |
| logging_simple           | 8.88 us                                                      | 7.69 us: 1.15x faster                                                       |
| spectral_norm            | 139 ms                                                       | 122 ms: 1.14x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 3.53 us: 1.13x faster                                                       |
| logging_format           | 9.64 us                                                      | 8.51 us: 1.13x faster                                                       |
| sympy_sum                | 193 ms                                                       | 172 ms: 1.12x faster                                                        |
| thrift                   | 1.18 ms                                                      | 1.06 ms: 1.11x faster                                                       |
| mako                     | 14.7 ms                                                      | 13.4 ms: 1.10x faster                                                       |
| 2to3                     | 350 ms                                                       | 320 ms: 1.09x faster                                                        |
| regex_dna                | 261 ms                                                       | 239 ms: 1.09x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 28.9 ms: 1.09x faster                                                       |
| docutils                 | 3.41 sec                                                     | 3.14 sec: 1.09x faster                                                      |
| bench_thread_pool        | 1.14 ms                                                      | 1.06 ms: 1.08x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 20.0 ms: 1.07x faster                                                       |
| pidigits                 | 271 ms                                                       | 254 ms: 1.07x faster                                                        |
| sympy_str                | 360 ms                                                       | 338 ms: 1.07x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 71.4 ms: 1.06x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 26.1 ms: 1.04x faster                                                       |
| json_loads               | 30.3 us                                                      | 29.2 us: 1.04x faster                                                       |
| nqueens                  | 115 ms                                                       | 111 ms: 1.04x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 2.10 sec: 1.03x faster                                                      |
| sympy_expand             | 600 ms                                                       | 588 ms: 1.02x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 64.1 ms: 1.01x slower                                                       |
| json                     | 5.86 ms                                                      | 6.04 ms: 1.03x slower                                                       |
| meteor_contest           | 138 ms                                                       | 144 ms: 1.04x slower                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 115 ms: 1.04x slower                                                        |
| xml_etree_parse          | 160 ms                                                       | 170 ms: 1.06x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.29 ms: 1.06x slower                                                       |
| scimark_fft              | 361 ms                                                       | 392 ms: 1.08x slower                                                        |
| unpack_sequence          | 59.9 ns                                                      | 67.1 ns: 1.12x slower                                                       |
| sqlite_synth             | 2.99 us                                                      | 3.35 us: 1.12x slower                                                       |
| async_generators         | 421 ms                                                       | 475 ms: 1.13x slower                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 105 ms: 1.14x slower                                                        |
| unpickle_list            | 4.65 us                                                      | 5.58 us: 1.20x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 36.1 us: 1.22x slower                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 6.34 ms: 1.25x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.43 ms: 1.29x slower                                                       |
| unpickle                 | 13.5 us                                                      | 17.8 us: 1.32x slower                                                       |
| telco                    | 7.23 ms                                                      | 9.72 ms: 1.34x slower                                                       |
| python_startup           | 11.5 ms                                                      | 16.5 ms: 1.43x slower                                                       |
| pickle_list              | 4.12 us                                                      | 5.90 us: 1.43x slower                                                       |
| pickle                   | 9.89 us                                                      | 14.7 us: 1.49x slower                                                       |
| coverage                 | 63.3 ms                                                      | 101 ms: 1.59x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 5.59 ms: 1.64x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.92 ms: 1.65x slower                                                       |
| logging_silent           | 167 ns                                                       | 677 ns: 4.05x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 2.14 sec: 335.83x slower                                                    |
| Geometric mean           | (ref)                                                        | 1.07x faster                                                                |

Benchmark hidden because not significant (4): asyncio_websockets, json_dumps, pprint_safe_repr, fannkuch
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250607-3.15.0a0-8fdbbf8-JIT/bm-20250607-pythonperf2-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.125x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.38x