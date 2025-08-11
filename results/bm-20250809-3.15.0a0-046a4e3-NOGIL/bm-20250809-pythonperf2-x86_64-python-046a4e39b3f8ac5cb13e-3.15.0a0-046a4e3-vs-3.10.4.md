# Results vs. 3.10.4

- fork: python
- ref: 046a4e39b3f8ac5cb13e
- machine: linux-x86_64
- commit hash: 046a4e3
- commit date: 2025-08-09
- overall geometric mean: 1.196x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: 1.66x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 316 ms: 1.11x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.87 sec: 1.19x faster                                                      |
| html5lib       | 94.6 ms                                                      | 70.7 ms: 1.34x faster                                                       |
| Geometric mean | (ref)                                                        | 1.21x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io           | 1.60 sec                                                     | 561 ms: 2.85x faster                                                        |
| async_tree_none         | 692 ms                                                       | 263 ms: 2.63x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 320 ms: 2.56x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 496 ms: 1.89x faster                                                        |
| Geometric mean          | (ref)                                                        | 2.45x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 111 ms                                                       | 71.7 ms: 1.55x faster                                                       |
| pidigits       | 271 ms                                                       | 252 ms: 1.08x faster                                                        |
| nbody          | 134 ms                                                       | 125 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.21x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 153 ms: 1.24x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 22.8 ms: 1.19x faster                                                       |
| regex_dna      | 261 ms                                                       | 222 ms: 1.18x faster                                                        |
| regex_effbot   | 3.09 ms                                                      | 3.53 ms: 1.14x slower                                                       |
| Geometric mean | (ref)                                                        | 1.11x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                                       |
| unpickle_pure_python | 312 us                                                       | 241 us: 1.30x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 86.1 ms: 1.28x faster                                                       |
| tomli_loads          | 2.92 sec                                                     | 2.33 sec: 1.25x faster                                                      |
| pickle_pure_python   | 455 us                                                       | 364 us: 1.25x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 132 ms: 1.21x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 69.7 ms: 1.09x faster                                                       |
| json_loads           | 30.3 us                                                      | 29.0 us: 1.05x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 97.5 ms: 1.06x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 35.1 us: 1.19x slower                                                       |
| unpickle_list        | 4.65 us                                                      | 5.54 us: 1.19x slower                                                       |
| pickle_list          | 4.12 us                                                      | 4.96 us: 1.20x slower                                                       |
| pickle               | 9.89 us                                                      | 12.2 us: 1.24x slower                                                       |
| unpickle             | 13.5 us                                                      | 16.7 us: 1.24x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 11.8 ms: 1.61x slower                                                       |
| python_startup         | 11.5 ms                                                      | 19.2 ms: 1.67x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.64x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 50.2 ms                                                      | 42.9 ms: 1.17x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 30.6 ms: 1.03x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 65.2 ms: 1.03x slower                                                       |
| mako            | 14.7 ms                                                      | 17.6 ms: 1.20x slower                                                       |
| Geometric mean  | (ref)                                                        | 1.01x slower                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io            | 1.60 sec                                                     | 561 ms: 2.85x faster                                                        |
| async_tree_none          | 692 ms                                                       | 263 ms: 2.63x faster                                                        |
| typing_runtime_protocols | 537 us                                                       | 206 us: 2.60x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 320 ms: 2.56x faster                                                        |
| mdp                      | 3.01 sec                                                     | 1.45 sec: 2.08x faster                                                      |
| deltablue                | 7.50 ms                                                      | 3.70 ms: 2.02x faster                                                       |
| asyncio_tcp              | 779 ms                                                       | 386 ms: 2.02x faster                                                        |
| generators               | 57.3 ms                                                      | 29.3 ms: 1.95x faster                                                       |
| go                       | 262 ms                                                       | 137 ms: 1.91x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 496 ms: 1.89x faster                                                        |
| logging_silent           | 167 ns                                                       | 96.6 ns: 1.73x faster                                                       |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.89 sec: 1.64x faster                                                      |
| pylint                   | 566 ms                                                       | 345 ms: 1.64x faster                                                        |
| chaos                    | 109 ms                                                       | 66.5 ms: 1.63x faster                                                       |
| float                    | 111 ms                                                       | 71.7 ms: 1.55x faster                                                       |
| pyflate                  | 733 ms                                                       | 477 ms: 1.54x faster                                                        |
| scimark_sor              | 180 ms                                                       | 117 ms: 1.54x faster                                                        |
| gc_traversal             | 3.42 ms                                                      | 2.24 ms: 1.53x faster                                                       |
| comprehensions           | 26.7 us                                                      | 18.0 us: 1.48x faster                                                       |
| deepcopy                 | 468 us                                                       | 319 us: 1.47x faster                                                        |
| raytrace                 | 489 ms                                                       | 335 ms: 1.46x faster                                                        |
| scimark_lu               | 167 ms                                                       | 116 ms: 1.44x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.57 ms: 1.43x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 34.8 us: 1.43x faster                                                       |
| richards_super           | 90.6 ms                                                      | 63.6 ms: 1.43x faster                                                       |
| richards                 | 75.1 ms                                                      | 55.4 ms: 1.36x faster                                                       |
| coroutines               | 30.3 ms                                                      | 22.6 ms: 1.34x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 80.2 ms: 1.34x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 70.7 ms: 1.34x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 61.8 ms: 1.31x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.28 sec: 1.31x faster                                                      |
| logging_simple           | 8.88 us                                                      | 6.82 us: 1.30x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 241 us: 1.30x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 86.1 ms: 1.28x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 93.0 ms: 1.28x faster                                                       |
| logging_format           | 9.64 us                                                      | 7.60 us: 1.27x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 16.9 ms: 1.26x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.33 sec: 1.25x faster                                                      |
| pickle_pure_python       | 455 us                                                       | 364 us: 1.25x faster                                                        |
| regex_compile            | 190 ms                                                       | 153 ms: 1.24x faster                                                        |
| spectral_norm            | 139 ms                                                       | 114 ms: 1.22x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 132 ms: 1.21x faster                                                        |
| thrift                   | 1.18 ms                                                      | 979 us: 1.20x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.87 sec: 1.19x faster                                                      |
| regex_v8                 | 27.2 ms                                                      | 22.8 ms: 1.19x faster                                                       |
| regex_dna                | 261 ms                                                       | 222 ms: 1.18x faster                                                        |
| django_template          | 50.2 ms                                                      | 42.9 ms: 1.17x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 906 ms: 1.16x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.88 sec: 1.15x faster                                                      |
| sqlite_synth             | 2.99 us                                                      | 2.61 us: 1.14x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 3.50 us: 1.14x faster                                                       |
| sympy_sum                | 193 ms                                                       | 171 ms: 1.13x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 25.1 ms: 1.12x faster                                                       |
| 2to3                     | 350 ms                                                       | 316 ms: 1.11x faster                                                        |
| sympy_str                | 360 ms                                                       | 327 ms: 1.10x faster                                                        |
| unpack_sequence          | 59.9 ns                                                      | 54.7 ns: 1.10x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 69.7 ms: 1.09x faster                                                       |
| nqueens                  | 115 ms                                                       | 106 ms: 1.08x faster                                                        |
| sympy_expand             | 600 ms                                                       | 554 ms: 1.08x faster                                                        |
| pidigits                 | 271 ms                                                       | 252 ms: 1.08x faster                                                        |
| nbody                    | 134 ms                                                       | 125 ms: 1.07x faster                                                        |
| json                     | 5.86 ms                                                      | 5.48 ms: 1.07x faster                                                       |
| json_loads               | 30.3 us                                                      | 29.0 us: 1.05x faster                                                       |
| scimark_fft              | 361 ms                                                       | 348 ms: 1.04x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 30.6 ms: 1.03x faster                                                       |
| fannkuch                 | 483 ms                                                       | 475 ms: 1.02x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 65.2 ms: 1.03x slower                                                       |
| meteor_contest           | 138 ms                                                       | 145 ms: 1.05x slower                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 97.5 ms: 1.06x slower                                                       |
| async_generators         | 421 ms                                                       | 468 ms: 1.11x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.53 ms: 1.14x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.02 ms: 1.14x slower                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 5.83 ms: 1.15x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 35.1 us: 1.19x slower                                                       |
| unpickle_list            | 4.65 us                                                      | 5.54 us: 1.19x slower                                                       |
| mako                     | 14.7 ms                                                      | 17.6 ms: 1.20x slower                                                       |
| pickle_list              | 4.12 us                                                      | 4.96 us: 1.20x slower                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 1.41 ms: 1.24x slower                                                       |
| pickle                   | 9.89 us                                                      | 12.2 us: 1.24x slower                                                       |
| unpickle                 | 13.5 us                                                      | 16.7 us: 1.24x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 11.8 ms: 1.61x slower                                                       |
| python_startup           | 11.5 ms                                                      | 19.2 ms: 1.67x slower                                                       |
| coverage                 | 63.3 ms                                                      | 119 ms: 1.87x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 57.7 ms: 9.05x slower                                                       |
| telco                    | 7.23 ms                                                      | 174 ms: 24.02x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.15x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (13) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (15) of results/bm-20250809-3.15.0a0-046a4e3-NOGIL/bm-20250809-pythonperf2-x86_64-python-046a4e39b3f8ac5cb13e-3.15.0a0-046a4e3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.196x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.15x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: 1.66x