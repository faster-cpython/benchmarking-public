# Results vs. 3.10.4

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: linux-x86_64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.320x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.18x faster
- Memory change: 1.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 310 ms: 1.13x faster                                                        |
| docutils       | 3.41 sec                                                     | 3.16 sec: 1.08x faster                                                      |
| html5lib       | 94.6 ms                                                      | 68.9 ms: 1.37x faster                                                       |
| tornado_http   | 157 ms                                                       | 121 ms: 1.30x faster                                                        |
| Geometric mean | (ref)                                                        | 1.21x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 330 ms: 2.10x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 401 ms: 2.05x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 840 ms: 1.90x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 567 ms: 1.65x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.92x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 89.1 ms: 1.50x faster                                                       |
| float          | 111 ms                                                       | 75.7 ms: 1.47x faster                                                       |
| pidigits       | 271 ms                                                       | 250 ms: 1.08x faster                                                        |
| Geometric mean | (ref)                                                        | 1.34x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 147 ms: 1.29x faster                                                        |
| regex_dna      | 261 ms                                                       | 234 ms: 1.12x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 25.9 ms: 1.05x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.33 ms: 1.08x slower                                                       |
| Geometric mean | (ref)                                                        | 1.09x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 212 us: 1.47x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 320 us: 1.42x faster                                                        |
| xml_etree_process    | 75.9 ms                                                      | 55.3 ms: 1.37x faster                                                       |
| json_dumps           | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                       |
| tomli_loads          | 2.92 sec                                                     | 2.15 sec: 1.36x faster                                                      |
| json_loads           | 30.3 us                                                      | 25.1 us: 1.21x faster                                                       |
| xml_etree_generate   | 92.3 ms                                                      | 79.0 ms: 1.17x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 98.6 ms: 1.12x faster                                                       |
| xml_etree_parse      | 160 ms                                                       | 144 ms: 1.12x faster                                                        |
| Geometric mean       | (ref)                                                        | 1.28x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 9.09 ms: 1.24x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.23 ms: 1.59x faster                                                       |
| django_template | 50.2 ms                                                      | 42.4 ms: 1.19x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 29.4 ms: 1.07x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 61.3 ms: 1.03x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.20x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 182 us: 2.94x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.18 ms: 2.36x faster                                                       |
| async_tree_none          | 692 ms                                                       | 330 ms: 2.10x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 372 ms: 2.09x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 401 ms: 2.05x faster                                                        |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.96x faster                                                      |
| async_tree_io            | 1.60 sec                                                     | 840 ms: 1.90x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 26.7 us: 1.87x faster                                                       |
| richards_super           | 90.6 ms                                                      | 50.3 ms: 1.80x faster                                                       |
| scimark_lu               | 167 ms                                                       | 96.7 ms: 1.72x faster                                                       |
| scimark_sor              | 180 ms                                                       | 105 ms: 1.72x faster                                                        |
| go                       | 262 ms                                                       | 152 ms: 1.72x faster                                                        |
| richards                 | 75.1 ms                                                      | 43.7 ms: 1.72x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 69.7 ms: 1.71x faster                                                       |
| spectral_norm            | 139 ms                                                       | 81.4 ms: 1.71x faster                                                       |
| logging_silent           | 167 ns                                                       | 100 ns: 1.67x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 567 ms: 1.65x faster                                                        |
| chaos                    | 109 ms                                                       | 67.6 ms: 1.61x faster                                                       |
| mako                     | 14.7 ms                                                      | 9.23 ms: 1.59x faster                                                       |
| raytrace                 | 489 ms                                                       | 309 ms: 1.58x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 68.6 ms: 1.57x faster                                                       |
| pyflate                  | 733 ms                                                       | 468 ms: 1.57x faster                                                        |
| deepcopy                 | 468 us                                                       | 303 us: 1.54x faster                                                        |
| generators               | 57.3 ms                                                      | 37.2 ms: 1.54x faster                                                       |
| nbody                    | 134 ms                                                       | 89.1 ms: 1.50x faster                                                       |
| sqlglot_parse            | 2.24 ms                                                      | 1.50 ms: 1.49x faster                                                       |
| unpickle_pure_python     | 312 us                                                       | 212 us: 1.47x faster                                                        |
| float                    | 111 ms                                                       | 75.7 ms: 1.47x faster                                                       |
| comprehensions           | 26.7 us                                                      | 18.5 us: 1.44x faster                                                       |
| pickle_pure_python       | 455 us                                                       | 320 us: 1.42x faster                                                        |
| logging_simple           | 8.88 us                                                      | 6.36 us: 1.39x faster                                                       |
| pylint                   | 566 ms                                                       | 409 ms: 1.38x faster                                                        |
| sqlglot_transpile        | 2.68 ms                                                      | 1.94 ms: 1.38x faster                                                       |
| logging_format           | 9.64 us                                                      | 7.00 us: 1.38x faster                                                       |
| fannkuch                 | 483 ms                                                       | 350 ms: 1.38x faster                                                        |
| html5lib                 | 94.6 ms                                                      | 68.9 ms: 1.37x faster                                                       |
| xml_etree_process        | 75.9 ms                                                      | 55.3 ms: 1.37x faster                                                       |
| coroutines               | 30.3 ms                                                      | 22.1 ms: 1.37x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 2.94 us: 1.37x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 10.7 ms: 1.36x faster                                                       |
| tomli_loads              | 2.92 sec                                                     | 2.15 sec: 1.36x faster                                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 780 ms: 1.35x faster                                                        |
| hexiom                   | 9.42 ms                                                      | 7.00 ms: 1.34x faster                                                       |
| pathlib                  | 21.4 ms                                                      | 15.9 ms: 1.34x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.25 sec: 1.33x faster                                                      |
| pprint_pformat           | 2.15 sec                                                     | 1.63 sec: 1.32x faster                                                      |
| thrift                   | 1.18 ms                                                      | 894 us: 1.31x faster                                                        |
| tornado_http             | 157 ms                                                       | 121 ms: 1.30x faster                                                        |
| regex_compile            | 190 ms                                                       | 147 ms: 1.29x faster                                                        |
| scimark_fft              | 361 ms                                                       | 291 ms: 1.24x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 925 us: 1.23x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 65.8 ms: 1.23x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.14 ms: 1.23x faster                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 5.20 ms: 1.23x faster                                                       |
| json_loads               | 30.3 us                                                      | 25.1 us: 1.21x faster                                                       |
| django_template          | 50.2 ms                                                      | 42.4 ms: 1.19x faster                                                       |
| nqueens                  | 115 ms                                                       | 98.2 ms: 1.17x faster                                                       |
| xml_etree_generate       | 92.3 ms                                                      | 79.0 ms: 1.17x faster                                                       |
| mdp                      | 3.01 sec                                                     | 2.59 sec: 1.16x faster                                                      |
| sympy_str                | 360 ms                                                       | 311 ms: 1.16x faster                                                        |
| sympy_expand             | 600 ms                                                       | 528 ms: 1.14x faster                                                        |
| sympy_sum                | 193 ms                                                       | 170 ms: 1.14x faster                                                        |
| 2to3                     | 350 ms                                                       | 310 ms: 1.13x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 98.6 ms: 1.12x faster                                                       |
| regex_dna                | 261 ms                                                       | 234 ms: 1.12x faster                                                        |
| xml_etree_parse          | 160 ms                                                       | 144 ms: 1.12x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 130 ms: 1.11x faster                                                        |
| async_generators         | 421 ms                                                       | 382 ms: 1.10x faster                                                        |
| json                     | 5.86 ms                                                      | 5.37 ms: 1.09x faster                                                       |
| meteor_contest           | 138 ms                                                       | 128 ms: 1.08x faster                                                        |
| pidigits                 | 271 ms                                                       | 250 ms: 1.08x faster                                                        |
| docutils                 | 3.41 sec                                                     | 3.16 sec: 1.08x faster                                                      |
| genshi_text              | 31.4 ms                                                      | 29.4 ms: 1.07x faster                                                       |
| sqlglot_optimize         | 70.1 ms                                                      | 65.6 ms: 1.07x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 26.4 ms: 1.07x faster                                                       |
| regex_v8                 | 27.2 ms                                                      | 25.9 ms: 1.05x faster                                                       |
| genshi_xml               | 63.3 ms                                                      | 61.3 ms: 1.03x faster                                                       |
| asyncio_websockets       | 390 ms                                                       | 396 ms: 1.01x slower                                                        |
| regex_effbot             | 3.09 ms                                                      | 3.33 ms: 1.08x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 1.91 ms: 1.08x slower                                                       |
| telco                    | 7.23 ms                                                      | 8.11 ms: 1.12x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.09 ms: 1.24x slower                                                       |
| coverage                 | 63.3 ms                                                      | 79.2 ms: 1.25x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.38 ms: 1.28x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.33x faster                                                                |
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240831-3.14.0a0-34ddb64-JIT/bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.320x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.18x

# Memory
- memory change: 1.23x