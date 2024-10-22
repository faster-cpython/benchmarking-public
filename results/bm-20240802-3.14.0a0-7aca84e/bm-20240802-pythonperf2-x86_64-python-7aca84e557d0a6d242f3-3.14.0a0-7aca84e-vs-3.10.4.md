# Results vs. 3.10.4

- fork: python
- ref: 7aca84e557d0a6d242f3
- machine: linux-x86_64
- commit hash: 7aca84e
- commit date: 2024-08-02
- overall geometric mean: 1.34x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 287 ms: 1.22x faster                                                        |
| docutils       | 3.41 sec                                                     | 3.00 sec: 1.14x faster                                                      |
| html5lib       | 94.6 ms                                                      | 74.1 ms: 1.28x faster                                                       |
| tornado_http   | 157 ms                                                       | 116 ms: 1.35x faster                                                        |
| Geometric mean | (ref)                                                        | 1.24x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 332 ms: 2.08x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 399 ms: 2.05x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 799 ms: 2.00x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 572 ms: 1.64x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.94x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 90.6 ms: 1.48x faster                                                       |
| float          | 111 ms                                                       | 81.0 ms: 1.37x faster                                                       |
| pidigits       | 271 ms                                                       | 252 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.30x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 143 ms: 1.33x faster                                                        |
| regex_dna      | 261 ms                                                       | 254 ms: 1.03x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 26.9 ms: 1.01x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.57 ms: 1.16x slower                                                       |
| Geometric mean | (ref)                                                        | 1.04x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 213 us: 1.47x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 312 us: 1.46x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 10.8 ms: 1.35x faster                                                       |
| tomli_loads          | 2.92 sec                                                     | 2.28 sec: 1.28x faster                                                      |
| xml_etree_process    | 75.9 ms                                                      | 59.5 ms: 1.28x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.5 us: 1.19x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 143 ms: 1.12x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 102 ms: 1.09x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 85.5 ms: 1.08x faster                                                       |
| Geometric mean       | (ref)                                                        | 1.25x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.3 ms: 1.16x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 9.04 ms: 1.23x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.4 ms: 1.41x faster                                                       |
| django_template | 50.2 ms                                                      | 38.6 ms: 1.30x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 25.4 ms: 1.24x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 54.0 ms: 1.17x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.28x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 174 us: 3.09x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.45 ms: 2.17x faster                                                       |
| async_tree_none          | 692 ms                                                       | 332 ms: 2.08x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 376 ms: 2.07x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 399 ms: 2.05x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 799 ms: 2.00x faster                                                        |
| generators               | 57.3 ms                                                      | 28.7 ms: 2.00x faster                                                       |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                      |
| scimark_lu               | 167 ms                                                       | 93.5 ms: 1.79x faster                                                       |
| chaos                    | 109 ms                                                       | 61.1 ms: 1.78x faster                                                       |
| raytrace                 | 489 ms                                                       | 276 ms: 1.77x faster                                                        |
| logging_silent           | 167 ns                                                       | 97.8 ns: 1.71x faster                                                       |
| scimark_sor              | 180 ms                                                       | 108 ms: 1.67x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 29.9 us: 1.67x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 72.6 ms: 1.64x faster                                                       |
| deepcopy                 | 468 us                                                       | 286 us: 1.64x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 572 ms: 1.64x faster                                                        |
| pylint                   | 566 ms                                                       | 347 ms: 1.63x faster                                                        |
| go                       | 262 ms                                                       | 163 ms: 1.61x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 67.2 ms: 1.60x faster                                                       |
| richards_super           | 90.6 ms                                                      | 57.2 ms: 1.58x faster                                                       |
| sqlglot_parse            | 2.24 ms                                                      | 1.41 ms: 1.58x faster                                                       |
| comprehensions           | 26.7 us                                                      | 17.5 us: 1.53x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 6.27 ms: 1.50x faster                                                       |
| sqlglot_transpile        | 2.68 ms                                                      | 1.79 ms: 1.50x faster                                                       |
| pyflate                  | 733 ms                                                       | 492 ms: 1.49x faster                                                        |
| nbody                    | 134 ms                                                       | 90.6 ms: 1.48x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 213 us: 1.47x faster                                                        |
| richards                 | 75.1 ms                                                      | 51.2 ms: 1.47x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 312 us: 1.46x faster                                                        |
| spectral_norm            | 139 ms                                                       | 96.4 ms: 1.44x faster                                                       |
| mako                     | 14.7 ms                                                      | 10.4 ms: 1.41x faster                                                       |
| coroutines               | 30.3 ms                                                      | 21.8 ms: 1.39x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 2.91 us: 1.38x faster                                                       |
| logging_format           | 9.64 us                                                      | 7.02 us: 1.37x faster                                                       |
| float                    | 111 ms                                                       | 81.0 ms: 1.37x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.47 us: 1.37x faster                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 4.69 ms: 1.36x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.24 sec: 1.35x faster                                                      |
| json_dumps               | 14.5 ms                                                      | 10.8 ms: 1.35x faster                                                       |
| thrift                   | 1.18 ms                                                      | 871 us: 1.35x faster                                                        |
| tornado_http             | 157 ms                                                       | 116 ms: 1.35x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 16.0 ms: 1.34x faster                                                       |
| regex_compile            | 190 ms                                                       | 143 ms: 1.33x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 870 us: 1.31x faster                                                        |
| fannkuch                 | 483 ms                                                       | 370 ms: 1.31x faster                                                        |
| django_template          | 50.2 ms                                                      | 38.6 ms: 1.30x faster                                                       |
| nqueens                  | 115 ms                                                       | 89.4 ms: 1.29x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.28 sec: 1.28x faster                                                      |
| html5lib                 | 94.6 ms                                                      | 74.1 ms: 1.28x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 59.5 ms: 1.28x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.71 sec: 1.26x faster                                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 837 ms: 1.25x faster                                                        |
| sympy_sum                | 193 ms                                                       | 154 ms: 1.25x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 25.4 ms: 1.24x faster                                                       |
| dask                     | 472 ms                                                       | 383 ms: 1.23x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 118 ms: 1.22x faster                                                        |
| 2to3                     | 350 ms                                                       | 287 ms: 1.22x faster                                                        |
| sympy_str                | 360 ms                                                       | 296 ms: 1.22x faster                                                        |
| sympy_integrate          | 28.2 ms                                                      | 23.3 ms: 1.21x faster                                                       |
| sqlglot_optimize         | 70.1 ms                                                      | 58.3 ms: 1.20x faster                                                       |
| mdp                      | 3.01 sec                                                     | 2.50 sec: 1.20x faster                                                      |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.23 ms: 1.20x faster                                                       |
| scimark_fft              | 361 ms                                                       | 302 ms: 1.20x faster                                                        |
| json_loads               | 30.3 us                                                      | 25.5 us: 1.19x faster                                                       |
| sympy_expand             | 600 ms                                                       | 507 ms: 1.18x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 54.0 ms: 1.17x faster                                                       |
| async_generators         | 421 ms                                                       | 359 ms: 1.17x faster                                                        |
| docutils                 | 3.41 sec                                                     | 3.00 sec: 1.14x faster                                                      |
| xml_etree_parse          | 160 ms                                                       | 143 ms: 1.12x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 102 ms: 1.09x faster                                                        |
| meteor_contest           | 138 ms                                                       | 128 ms: 1.08x faster                                                        |
| json                     | 5.86 ms                                                      | 5.42 ms: 1.08x faster                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 85.5 ms: 1.08x faster                                                       |
| pidigits                 | 271 ms                                                       | 252 ms: 1.07x faster                                                        |
| regex_dna                | 261 ms                                                       | 254 ms: 1.03x faster                                                        |
| asyncio_websockets       | 390 ms                                                       | 386 ms: 1.01x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 26.9 ms: 1.01x faster                                                       |
| telco                    | 7.23 ms                                                      | 7.98 ms: 1.10x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.04 ms: 1.16x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.57 ms: 1.16x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.3 ms: 1.16x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.04 ms: 1.23x slower                                                       |
| coverage                 | 63.3 ms                                                      | 87.3 ms: 1.38x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.74 ms: 1.39x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.34x faster                                                                |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240802-3.14.0a0-7aca84e/bm-20240802-pythonperf2-x86_64-python-7aca84e557d0a6d242f3-3.14.0a0-7aca84e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.13x