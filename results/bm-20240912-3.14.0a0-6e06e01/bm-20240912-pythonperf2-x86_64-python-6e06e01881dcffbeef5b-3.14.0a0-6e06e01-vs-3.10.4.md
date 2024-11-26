# Results vs. 3.10.4

- fork: python
- ref: 6e06e01881dcffbeef5b
- machine: linux-x86_64
- commit hash: 6e06e01
- commit date: 2024-09-12
- overall geometric mean: 1.335x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 281 ms: 1.25x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                                      |
| html5lib       | 94.6 ms                                                      | 71.5 ms: 1.32x faster                                                       |
| tornado_http   | 157 ms                                                       | 116 ms: 1.36x faster                                                        |
| Geometric mean | (ref)                                                        | 1.27x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 322 ms: 2.15x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 400 ms: 2.05x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 803 ms: 1.99x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 575 ms: 1.63x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.94x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 87.2 ms: 1.54x faster                                                       |
| float          | 111 ms                                                       | 78.3 ms: 1.42x faster                                                       |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.33x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 140 ms: 1.36x faster                                                        |
| regex_dna      | 261 ms                                                       | 241 ms: 1.08x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 25.5 ms: 1.06x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.64 ms: 1.18x slower                                                       |
| Geometric mean | (ref)                                                        | 1.07x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 317 us: 1.43x faster                                                        |
| unpickle_pure_python | 312 us                                                       | 220 us: 1.42x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 10.8 ms: 1.34x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 59.9 ms: 1.27x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.1 us: 1.21x faster                                                       |
| tomli_loads          | 2.92 sec                                                     | 2.53 sec: 1.15x faster                                                      |
| xml_etree_parse      | 160 ms                                                       | 143 ms: 1.12x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 102 ms: 1.08x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 85.6 ms: 1.08x faster                                                       |
| unpickle_list        | 4.65 us                                                      | 4.56 us: 1.02x faster                                                       |
| pickle               | 9.89 us                                                      | 10.5 us: 1.06x slower                                                       |
| pickle_list          | 4.12 us                                                      | 4.50 us: 1.09x slower                                                       |
| pickle_dict          | 29.5 us                                                      | 32.4 us: 1.10x slower                                                       |
| unpickle             | 13.5 us                                                      | 15.5 us: 1.15x slower                                                       |
| Geometric mean       | (ref)                                                        | 1.11x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.3 ms: 1.16x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 8.94 ms: 1.22x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.19x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                                       |
| django_template | 50.2 ms                                                      | 38.3 ms: 1.31x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 24.9 ms: 1.26x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 54.6 ms: 1.16x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.28x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 175 us: 3.06x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.38 ms: 2.22x faster                                                       |
| async_tree_none          | 692 ms                                                       | 322 ms: 2.15x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 372 ms: 2.10x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 400 ms: 2.05x faster                                                        |
| async_tree_io            | 1.60 sec                                                     | 803 ms: 1.99x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.57 sec: 1.97x faster                                                      |
| generators               | 57.3 ms                                                      | 29.3 ms: 1.95x faster                                                       |
| go                       | 262 ms                                                       | 134 ms: 1.95x faster                                                        |
| raytrace                 | 489 ms                                                       | 272 ms: 1.80x faster                                                        |
| scimark_lu               | 167 ms                                                       | 95.7 ms: 1.74x faster                                                       |
| chaos                    | 109 ms                                                       | 62.7 ms: 1.73x faster                                                       |
| logging_silent           | 167 ns                                                       | 99.3 ns: 1.68x faster                                                       |
| deepcopy_memo            | 49.8 us                                                      | 30.2 us: 1.65x faster                                                       |
| deepcopy                 | 468 us                                                       | 286 us: 1.63x faster                                                        |
| pylint                   | 566 ms                                                       | 347 ms: 1.63x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 575 ms: 1.63x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 73.8 ms: 1.62x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 66.8 ms: 1.61x faster                                                       |
| richards_super           | 90.6 ms                                                      | 56.5 ms: 1.60x faster                                                       |
| sqlglot_parse            | 2.24 ms                                                      | 1.41 ms: 1.59x faster                                                       |
| comprehensions           | 26.7 us                                                      | 17.0 us: 1.57x faster                                                       |
| nbody                    | 134 ms                                                       | 87.2 ms: 1.54x faster                                                       |
| scimark_sor              | 180 ms                                                       | 117 ms: 1.53x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 6.21 ms: 1.52x faster                                                       |
| sqlglot_transpile        | 2.68 ms                                                      | 1.79 ms: 1.50x faster                                                       |
| richards                 | 75.1 ms                                                      | 50.3 ms: 1.49x faster                                                       |
| pyflate                  | 733 ms                                                       | 492 ms: 1.49x faster                                                        |
| spectral_norm            | 139 ms                                                       | 96.6 ms: 1.44x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 317 us: 1.43x faster                                                        |
| mako                     | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                                       |
| float                    | 111 ms                                                       | 78.3 ms: 1.42x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 220 us: 1.42x faster                                                        |
| coroutines               | 30.3 ms                                                      | 21.4 ms: 1.41x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.87 us: 1.40x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.37 us: 1.39x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.21 sec: 1.38x faster                                                      |
| deepcopy_reduce          | 4.01 us                                                      | 2.90 us: 1.38x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 15.6 ms: 1.37x faster                                                       |
| thrift                   | 1.18 ms                                                      | 859 us: 1.37x faster                                                        |
| tornado_http             | 157 ms                                                       | 116 ms: 1.36x faster                                                        |
| regex_compile            | 190 ms                                                       | 140 ms: 1.36x faster                                                        |
| fannkuch                 | 483 ms                                                       | 356 ms: 1.35x faster                                                        |
| json_dumps               | 14.5 ms                                                      | 10.8 ms: 1.34x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 71.5 ms: 1.32x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 865 us: 1.32x faster                                                        |
| bench_mp_pool            | 6.37 ms                                                      | 4.85 ms: 1.32x faster                                                       |
| django_template          | 50.2 ms                                                      | 38.3 ms: 1.31x faster                                                       |
| nqueens                  | 115 ms                                                       | 88.5 ms: 1.30x faster                                                       |
| pprint_pformat           | 2.15 sec                                                     | 1.66 sec: 1.29x faster                                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 815 ms: 1.29x faster                                                        |
| sympy_sum                | 193 ms                                                       | 152 ms: 1.27x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 59.9 ms: 1.27x faster                                                       |
| genshi_text              | 31.4 ms                                                      | 24.9 ms: 1.26x faster                                                       |
| 2to3                     | 350 ms                                                       | 281 ms: 1.25x faster                                                        |
| sympy_str                | 360 ms                                                       | 291 ms: 1.24x faster                                                        |
| unpack_sequence          | 59.9 ns                                                      | 48.7 ns: 1.23x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 23.0 ms: 1.23x faster                                                       |
| sqlglot_normalize        | 144 ms                                                       | 118 ms: 1.22x faster                                                        |
| json_loads               | 30.3 us                                                      | 25.1 us: 1.21x faster                                                       |
| dulwich_log              | 81.1 ms                                                      | 67.3 ms: 1.21x faster                                                       |
| scimark_fft              | 361 ms                                                       | 300 ms: 1.20x faster                                                        |
| mdp                      | 3.01 sec                                                     | 2.50 sec: 1.20x faster                                                      |
| sympy_expand             | 600 ms                                                       | 500 ms: 1.20x faster                                                        |
| sqlglot_optimize         | 70.1 ms                                                      | 59.0 ms: 1.19x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.29 ms: 1.18x faster                                                       |
| docutils                 | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                                      |
| async_generators         | 421 ms                                                       | 361 ms: 1.17x faster                                                        |
| genshi_xml               | 63.3 ms                                                      | 54.6 ms: 1.16x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.53 sec: 1.15x faster                                                      |
| json                     | 5.86 ms                                                      | 5.24 ms: 1.12x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 143 ms: 1.12x faster                                                        |
| sqlite_synth             | 2.99 us                                                      | 2.73 us: 1.09x faster                                                       |
| meteor_contest           | 138 ms                                                       | 127 ms: 1.09x faster                                                        |
| regex_dna                | 261 ms                                                       | 241 ms: 1.08x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 102 ms: 1.08x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 85.6 ms: 1.08x faster                                                       |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 25.5 ms: 1.06x faster                                                       |
| unpickle_list            | 4.65 us                                                      | 4.56 us: 1.02x faster                                                       |
| asyncio_websockets       | 390 ms                                                       | 396 ms: 1.01x slower                                                        |
| pickle                   | 9.89 us                                                      | 10.5 us: 1.06x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 1.92 ms: 1.09x slower                                                       |
| pickle_list              | 4.12 us                                                      | 4.50 us: 1.09x slower                                                       |
| pickle_dict              | 29.5 us                                                      | 32.4 us: 1.10x slower                                                       |
| unpickle                 | 13.5 us                                                      | 15.5 us: 1.15x slower                                                       |
| telco                    | 7.23 ms                                                      | 8.33 ms: 1.15x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.3 ms: 1.16x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.64 ms: 1.18x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 8.94 ms: 1.22x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.45 ms: 1.30x slower                                                       |
| coverage                 | 63.3 ms                                                      | 82.8 ms: 1.31x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.32x faster                                                                |
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (5) of results/bm-20240912-3.14.0a0-6e06e01/bm-20240912-pythonperf2-x86_64-python-6e06e01881dcffbeef5b-3.14.0a0-6e06e01.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.335x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.13x