# Results vs. 3.10.4

- fork: python
- ref: c8db0e817e7e0db50153
- machine: linux-x86_64
- commit hash: c8db0e8
- commit date: 2024-10-03
- overall geometric mean: 1.25x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 282 ms: 1.24x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.88 sec: 1.18x faster                                                      |
| html5lib       | 94.6 ms                                                      | 70.4 ms: 1.34x faster                                                       |
| tornado_http   | 157 ms                                                       | 116 ms: 1.36x faster                                                        |
| Geometric mean | (ref)                                                        | 1.28x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 320 ms: 2.16x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 403 ms: 2.03x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 819 ms: 1.95x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 574 ms: 1.63x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.93x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 90.6 ms: 1.48x faster                                                       |
| float          | 111 ms                                                       | 78.0 ms: 1.43x faster                                                       |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.31x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 140 ms: 1.36x faster                                                        |
| regex_dna      | 261 ms                                                       | 248 ms: 1.05x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 26.2 ms: 1.04x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.48 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 312 us: 1.46x faster                                                        |
| unpickle_pure_python | 312 us                                                       | 217 us: 1.43x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 10.8 ms: 1.34x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 59.2 ms: 1.28x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.0 us: 1.21x faster                                                       |
| tomli_loads          | 2.92 sec                                                     | 2.56 sec: 1.14x faster                                                      |
| xml_etree_generate   | 92.3 ms                                                      | 84.7 ms: 1.09x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 102 ms: 1.08x faster                                                        |
| xml_etree_parse      | 160 ms                                                       | 150 ms: 1.07x faster                                                        |
| unpickle_list        | 4.65 us                                                      | 4.74 us: 1.02x slower                                                       |
| pickle               | 9.89 us                                                      | 10.4 us: 1.05x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 31.6 us: 1.07x slower                                                       |
| pickle_list          | 4.12 us                                                      | 4.55 us: 1.11x slower                                                       |
| unpickle             | 13.5 us                                                      | 15.4 us: 1.14x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.11x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 8.95 ms: 1.22x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.3 ms: 1.43x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 24.7 ms: 1.27x faster                                                       |
| django_template | 50.2 ms                                                      | 40.6 ms: 1.24x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 54.2 ms: 1.17x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.27x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 170 us: 3.16x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.34 ms: 2.25x faster                                                       |
| async_tree_none          | 692 ms                                                       | 320 ms: 2.16x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 374 ms: 2.09x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 403 ms: 2.03x faster                                                        |
| generators               | 57.3 ms                                                      | 28.8 ms: 1.99x faster                                                       |
| go                       | 262 ms                                                       | 132 ms: 1.98x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.97x faster                                                      |
| async_tree_io            | 1.60 sec                                                     | 819 ms: 1.95x faster                                                        |
| raytrace                 | 489 ms                                                       | 269 ms: 1.82x faster                                                        |
| scimark_lu               | 167 ms                                                       | 93.7 ms: 1.78x faster                                                       |
| chaos                    | 109 ms                                                       | 62.3 ms: 1.74x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 28.8 us: 1.73x faster                                                       |
| logging_silent           | 167 ns                                                       | 98.6 ns: 1.70x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 71.9 ms: 1.66x faster                                                       |
| deepcopy                 | 468 us                                                       | 282 us: 1.66x faster                                                        |
| pylint                   | 566 ms                                                       | 345 ms: 1.64x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 574 ms: 1.63x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 65.9 ms: 1.63x faster                                                       |
| richards_super           | 90.6 ms                                                      | 56.4 ms: 1.61x faster                                                       |
| sqlglot_parse            | 2.24 ms                                                      | 1.40 ms: 1.59x faster                                                       |
| comprehensions           | 26.7 us                                                      | 17.2 us: 1.55x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 6.19 ms: 1.52x faster                                                       |
| scimark_sor              | 180 ms                                                       | 120 ms: 1.50x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.79 ms: 1.50x faster                                                       |
| richards                 | 75.1 ms                                                      | 50.2 ms: 1.50x faster                                                       |
| pyflate                  | 733 ms                                                       | 490 ms: 1.49x faster                                                        |
| nbody                    | 134 ms                                                       | 90.6 ms: 1.48x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 312 us: 1.46x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.13 us: 1.45x faster                                                       |
| coroutines               | 30.3 ms                                                      | 21.1 ms: 1.44x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 217 us: 1.43x faster                                                        |
| logging_format           | 9.64 us                                                      | 6.74 us: 1.43x faster                                                       |
| spectral_norm            | 139 ms                                                       | 97.2 ms: 1.43x faster                                                       |
| mako                     | 14.7 ms                                                      | 10.3 ms: 1.43x faster                                                       |
| float                    | 111 ms                                                       | 78.0 ms: 1.43x faster                                                       |
| thrift                   | 1.18 ms                                                      | 852 us: 1.38x faster                                                        |
| deepcopy_reduce          | 4.01 us                                                      | 2.92 us: 1.38x faster                                                       |
| fannkuch                 | 483 ms                                                       | 352 ms: 1.37x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.23 sec: 1.37x faster                                                      |
| regex_compile            | 190 ms                                                       | 140 ms: 1.36x faster                                                        |
| tornado_http             | 157 ms                                                       | 116 ms: 1.36x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 15.8 ms: 1.35x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 70.4 ms: 1.34x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 10.8 ms: 1.34x faster                                                       |
| nqueens                  | 115 ms                                                       | 88.9 ms: 1.29x faster                                                       |
| pprint_safe_repr         | 1.05 sec                                                     | 814 ms: 1.29x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.67 sec: 1.29x faster                                                      |
| xml_etree_process        | 75.9 ms                                                      | 59.2 ms: 1.28x faster                                                       |
| sympy_sum                | 193 ms                                                       | 151 ms: 1.28x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 24.7 ms: 1.27x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 904 us: 1.26x faster                                                        |
| sympy_str                | 360 ms                                                       | 289 ms: 1.25x faster                                                        |
| scimark_fft              | 361 ms                                                       | 290 ms: 1.25x faster                                                        |
| 2to3                     | 350 ms                                                       | 282 ms: 1.24x faster                                                        |
| django_template          | 50.2 ms                                                      | 40.6 ms: 1.24x faster                                                       |
| sympy_expand             | 600 ms                                                       | 488 ms: 1.23x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 117 ms: 1.23x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 66.1 ms: 1.23x faster                                                       |
| mdp                      | 3.01 sec                                                     | 2.46 sec: 1.22x faster                                                      |
| sympy_integrate          | 28.2 ms                                                      | 23.2 ms: 1.22x faster                                                       |
| json_loads               | 30.3 us                                                      | 25.0 us: 1.21x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.22 ms: 1.20x faster                                                       |
| sqlglot_optimize         | 70.1 ms                                                      | 58.7 ms: 1.20x faster                                                       |
| docutils                 | 3.41 sec                                                     | 2.88 sec: 1.18x faster                                                      |
| async_generators         | 421 ms                                                       | 357 ms: 1.18x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 54.2 ms: 1.17x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.56 sec: 1.14x faster                                                      |
| json                     | 5.86 ms                                                      | 5.34 ms: 1.10x faster                                                       |
| meteor_contest           | 138 ms                                                       | 126 ms: 1.09x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.74 us: 1.09x faster                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 84.7 ms: 1.09x faster                                                       |
| unpack_sequence          | 59.9 ns                                                      | 55.3 ns: 1.08x faster                                                       |
| xml_etree_iterparse      | 110 ms                                                       | 102 ms: 1.08x faster                                                        |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 150 ms: 1.07x faster                                                        |
| regex_dna                | 261 ms                                                       | 248 ms: 1.05x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 26.2 ms: 1.04x faster                                                       |
| unpickle_list            | 4.65 us                                                      | 4.74 us: 1.02x slower                                                       |
| pickle                   | 9.89 us                                                      | 10.4 us: 1.05x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 31.6 us: 1.07x slower                                                       |
| pickle_list              | 4.12 us                                                      | 4.55 us: 1.11x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 1.97 ms: 1.12x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.48 ms: 1.13x slower                                                       |
| telco                    | 7.23 ms                                                      | 8.20 ms: 1.13x slower                                                       |
| unpickle                 | 13.5 us                                                      | 15.4 us: 1.14x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 8.95 ms: 1.22x slower                                                       |
| coverage                 | 63.3 ms                                                      | 82.0 ms: 1.30x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.45 ms: 1.30x slower                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 1.40 sec: 219.89x slower                                                    |
| Geometric mean           | (ref)                                                        | 1.25x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20241003-3.14.0a0-c8db0e8/bm-20241003-pythonperf2-x86_64-python-c8db0e817e7e0db50153-3.14.0a0-c8db0e8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.12x