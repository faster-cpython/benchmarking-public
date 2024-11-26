# Results vs. 3.10.4

- fork: python
- ref: f6cc7c8bd01d8468af70
- machine: linux-x86_64
- commit hash: f6cc7c8
- commit date: 2024-10-26
- overall geometric mean: 1.320x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.26x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 283 ms: 1.24x faster                                                         |
| docutils       | 3.41 sec                                                     | 2.92 sec: 1.17x faster                                                       |
| html5lib       | 94.6 ms                                                      | 72.3 ms: 1.31x faster                                                        |
| tornado_http   | 157 ms                                                       | 117 ms: 1.34x faster                                                         |
| Geometric mean | (ref)                                                        | 1.26x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 333 ms: 2.08x faster                                                         |
| async_tree_memoization  | 819 ms                                                       | 417 ms: 1.97x faster                                                         |
| async_tree_io           | 1.60 sec                                                     | 837 ms: 1.91x faster                                                         |
| async_tree_cpu_io_mixed | 936 ms                                                       | 560 ms: 1.67x faster                                                         |
| Geometric mean          | (ref)                                                        | 1.90x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 91.1 ms: 1.47x faster                                                        |
| float          | 111 ms                                                       | 81.4 ms: 1.37x faster                                                        |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                         |
| Geometric mean | (ref)                                                        | 1.29x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 139 ms: 1.37x faster                                                         |
| regex_v8       | 27.2 ms                                                      | 25.4 ms: 1.07x faster                                                        |
| regex_dna      | 261 ms                                                       | 246 ms: 1.06x faster                                                         |
| regex_effbot   | 3.09 ms                                                      | 3.52 ms: 1.14x slower                                                        |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 220 us: 1.42x faster                                                         |
| pickle_pure_python   | 455 us                                                       | 325 us: 1.40x faster                                                         |
| xml_etree_process    | 75.9 ms                                                      | 59.3 ms: 1.28x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 11.4 ms: 1.28x faster                                                        |
| json_loads           | 30.3 us                                                      | 24.5 us: 1.24x faster                                                        |
| tomli_loads          | 2.92 sec                                                     | 2.47 sec: 1.18x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 146 ms: 1.09x faster                                                         |
| xml_etree_iterparse  | 110 ms                                                       | 101 ms: 1.09x faster                                                         |
| xml_etree_generate   | 92.3 ms                                                      | 85.0 ms: 1.09x faster                                                        |
| Geometric mean       | (ref)                                                        | 1.22x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.03 ms: 1.23x slower                                                        |
| python_startup         | 11.5 ms                                                      | 15.7 ms: 1.37x slower                                                        |
| Geometric mean         | (ref)                                                        | 1.30x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.7 ms: 1.37x faster                                                        |
| genshi_text     | 31.4 ms                                                      | 24.7 ms: 1.27x faster                                                        |
| django_template | 50.2 ms                                                      | 40.2 ms: 1.25x faster                                                        |
| genshi_xml      | 63.3 ms                                                      | 55.2 ms: 1.15x faster                                                        |
| Geometric mean  | (ref)                                                        | 1.26x faster                                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8 |
|--------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 178 us: 3.02x faster                                                         |
| deltablue                | 7.50 ms                                                      | 3.42 ms: 2.19x faster                                                        |
| async_tree_none          | 692 ms                                                       | 333 ms: 2.08x faster                                                         |
| generators               | 57.3 ms                                                      | 29.2 ms: 1.97x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 417 ms: 1.97x faster                                                         |
| go                       | 262 ms                                                       | 136 ms: 1.92x faster                                                         |
| async_tree_io            | 1.60 sec                                                     | 837 ms: 1.91x faster                                                         |
| raytrace                 | 489 ms                                                       | 279 ms: 1.76x faster                                                         |
| scimark_lu               | 167 ms                                                       | 96.4 ms: 1.73x faster                                                        |
| chaos                    | 109 ms                                                       | 63.5 ms: 1.71x faster                                                        |
| logging_silent           | 167 ns                                                       | 98.2 ns: 1.70x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 29.2 us: 1.70x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 560 ms: 1.67x faster                                                         |
| crypto_pyaes             | 119 ms                                                       | 72.3 ms: 1.65x faster                                                        |
| richards_super           | 90.6 ms                                                      | 55.4 ms: 1.63x faster                                                        |
| pylint                   | 566 ms                                                       | 349 ms: 1.62x faster                                                         |
| scimark_monte_carlo      | 107 ms                                                       | 66.5 ms: 1.62x faster                                                        |
| deepcopy                 | 468 us                                                       | 291 us: 1.61x faster                                                         |
| sqlglot_parse            | 2.24 ms                                                      | 1.41 ms: 1.59x faster                                                        |
| scimark_sor              | 180 ms                                                       | 117 ms: 1.54x faster                                                         |
| pyflate                  | 733 ms                                                       | 479 ms: 1.53x faster                                                         |
| richards                 | 75.1 ms                                                      | 49.5 ms: 1.52x faster                                                        |
| comprehensions           | 26.7 us                                                      | 17.6 us: 1.51x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.79 ms: 1.50x faster                                                        |
| nbody                    | 134 ms                                                       | 91.1 ms: 1.47x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.40 ms: 1.47x faster                                                        |
| coroutines               | 30.3 ms                                                      | 21.0 ms: 1.44x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 220 us: 1.42x faster                                                         |
| spectral_norm            | 139 ms                                                       | 99.3 ms: 1.40x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 325 us: 1.40x faster                                                         |
| thrift                   | 1.18 ms                                                      | 855 us: 1.37x faster                                                         |
| mako                     | 14.7 ms                                                      | 10.7 ms: 1.37x faster                                                        |
| fannkuch                 | 483 ms                                                       | 352 ms: 1.37x faster                                                         |
| regex_compile            | 190 ms                                                       | 139 ms: 1.37x faster                                                         |
| float                    | 111 ms                                                       | 81.4 ms: 1.37x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 2.95 us: 1.36x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 15.7 ms: 1.36x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.24 sec: 1.35x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.60 us: 1.34x faster                                                        |
| tornado_http             | 157 ms                                                       | 117 ms: 1.34x faster                                                         |
| pprint_pformat           | 2.15 sec                                                     | 1.61 sec: 1.34x faster                                                       |
| logging_format           | 9.64 us                                                      | 7.21 us: 1.34x faster                                                        |
| sqlalchemy_declarative   | 190 ms                                                       | 142 ms: 1.33x faster                                                         |
| pprint_safe_repr         | 1.05 sec                                                     | 796 ms: 1.32x faster                                                         |
| html5lib                 | 94.6 ms                                                      | 72.3 ms: 1.31x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 59.3 ms: 1.28x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 11.4 ms: 1.28x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 24.7 ms: 1.27x faster                                                        |
| nqueens                  | 115 ms                                                       | 90.4 ms: 1.27x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 901 us: 1.27x faster                                                         |
| sympy_sum                | 193 ms                                                       | 153 ms: 1.26x faster                                                         |
| django_template          | 50.2 ms                                                      | 40.2 ms: 1.25x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 65.2 ms: 1.24x faster                                                        |
| json_loads               | 30.3 us                                                      | 24.5 us: 1.24x faster                                                        |
| 2to3                     | 350 ms                                                       | 283 ms: 1.24x faster                                                         |
| sympy_str                | 360 ms                                                       | 292 ms: 1.23x faster                                                         |
| sqlalchemy_imperative    | 22.7 ms                                                      | 18.4 ms: 1.23x faster                                                        |
| scimark_fft              | 361 ms                                                       | 294 ms: 1.23x faster                                                         |
| sqlglot_normalize        | 144 ms                                                       | 118 ms: 1.21x faster                                                         |
| sympy_integrate          | 28.2 ms                                                      | 23.4 ms: 1.21x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.51 sec: 1.20x faster                                                       |
| sqlglot_optimize         | 70.1 ms                                                      | 58.7 ms: 1.20x faster                                                        |
| sympy_expand             | 600 ms                                                       | 502 ms: 1.19x faster                                                         |
| tomli_loads              | 2.92 sec                                                     | 2.47 sec: 1.18x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.32 ms: 1.17x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.92 sec: 1.17x faster                                                       |
| async_generators         | 421 ms                                                       | 365 ms: 1.15x faster                                                         |
| genshi_xml               | 63.3 ms                                                      | 55.2 ms: 1.15x faster                                                        |
| json                     | 5.86 ms                                                      | 5.17 ms: 1.13x faster                                                        |
| meteor_contest           | 138 ms                                                       | 126 ms: 1.10x faster                                                         |
| xml_etree_parse          | 160 ms                                                       | 146 ms: 1.09x faster                                                         |
| xml_etree_iterparse      | 110 ms                                                       | 101 ms: 1.09x faster                                                         |
| xml_etree_generate       | 92.3 ms                                                      | 85.0 ms: 1.09x faster                                                        |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                         |
| regex_v8                 | 27.2 ms                                                      | 25.4 ms: 1.07x faster                                                        |
| regex_dna                | 261 ms                                                       | 246 ms: 1.06x faster                                                         |
| asyncio_websockets       | 390 ms                                                       | 386 ms: 1.01x faster                                                         |
| telco                    | 7.23 ms                                                      | 7.94 ms: 1.10x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.52 ms: 1.14x slower                                                        |
| python_startup_no_site   | 7.33 ms                                                      | 9.03 ms: 1.23x slower                                                        |
| coverage                 | 63.3 ms                                                      | 79.3 ms: 1.25x slower                                                        |
| python_startup           | 11.5 ms                                                      | 15.7 ms: 1.37x slower                                                        |
| gc_traversal             | 3.42 ms                                                      | 5.31 ms: 1.56x slower                                                        |
| create_gc_cycles         | 1.76 ms                                                      | 2.98 ms: 1.69x slower                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 2.11 sec: 330.90x slower                                                     |
| Geometric mean           | (ref)                                                        | 1.23x faster                                                                 |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241026-3.14.0a1+-f6cc7c8/bm-20241026-pythonperf2-x86_64-python-f6cc7c8bd01d8468af70-3.14.0a1+-f6cc7c8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.320x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.26x