# Results vs. 3.10.4

- fork: python
- ref: 34ddb64d088dd7ccc321
- machine: linux-x86_64
- commit hash: 34ddb64
- commit date: 2024-08-31
- overall geometric mean: 1.345x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 281 ms: 1.24x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                                      |
| html5lib       | 94.6 ms                                                      | 70.4 ms: 1.34x faster                                                       |
| tornado_http   | 157 ms                                                       | 115 ms: 1.36x faster                                                        |
| Geometric mean | (ref)                                                        | 1.28x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 320 ms: 2.16x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 396 ms: 2.07x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 816 ms: 1.96x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 568 ms: 1.65x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.95x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 84.9 ms: 1.58x faster                                                       |
| float          | 111 ms                                                       | 79.4 ms: 1.40x faster                                                       |
| pidigits       | 271 ms                                                       | 252 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.33x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 139 ms: 1.37x faster                                                        |
| regex_dna      | 261 ms                                                       | 239 ms: 1.09x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 26.6 ms: 1.02x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.49 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 213 us: 1.46x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 314 us: 1.45x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 10.9 ms: 1.34x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 58.9 ms: 1.29x faster                                                       |
| json_loads           | 30.3 us                                                      | 24.6 us: 1.24x faster                                                       |
| tomli_loads          | 2.92 sec                                                     | 2.59 sec: 1.13x faster                                                      |
| xml_etree_parse      | 160 ms                                                       | 143 ms: 1.12x faster                                                        |
| xml_etree_iterparse  | 110 ms                                                       | 100.0 ms: 1.11x faster                                                      |
| xml_etree_generate   | 92.3 ms                                                      | 84.5 ms: 1.09x faster                                                       |
| Geometric mean       | (ref)                                                        | 1.24x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 9.06 ms: 1.24x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 24.8 ms: 1.27x faster                                                       |
| django_template | 50.2 ms                                                      | 39.7 ms: 1.26x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 53.4 ms: 1.19x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.28x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 170 us: 3.15x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.39 ms: 2.21x faster                                                       |
| async_tree_none          | 692 ms                                                       | 320 ms: 2.16x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 369 ms: 2.11x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 396 ms: 2.07x faster                                                        |
| generators               | 57.3 ms                                                      | 28.3 ms: 2.02x faster                                                       |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.97x faster                                                      |
| async_tree_io            | 1.60 sec                                                     | 816 ms: 1.96x faster                                                        |
| go                       | 262 ms                                                       | 135 ms: 1.94x faster                                                        |
| raytrace                 | 489 ms                                                       | 271 ms: 1.80x faster                                                        |
| scimark_lu               | 167 ms                                                       | 93.9 ms: 1.78x faster                                                       |
| chaos                    | 109 ms                                                       | 61.8 ms: 1.76x faster                                                       |
| logging_silent           | 167 ns                                                       | 97.6 ns: 1.71x faster                                                       |
| scimark_sor              | 180 ms                                                       | 108 ms: 1.67x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 29.8 us: 1.67x faster                                                       |
| crypto_pyaes             | 119 ms                                                       | 72.1 ms: 1.65x faster                                                       |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 568 ms: 1.65x faster                                                        |
| scimark_monte_carlo      | 107 ms                                                       | 65.8 ms: 1.63x faster                                                       |
| deepcopy                 | 468 us                                                       | 287 us: 1.63x faster                                                        |
| pylint                   | 566 ms                                                       | 347 ms: 1.63x faster                                                        |
| richards_super           | 90.6 ms                                                      | 56.3 ms: 1.61x faster                                                       |
| sqlglot_parse            | 2.24 ms                                                      | 1.41 ms: 1.59x faster                                                       |
| nbody                    | 134 ms                                                       | 84.9 ms: 1.58x faster                                                       |
| comprehensions           | 26.7 us                                                      | 17.2 us: 1.55x faster                                                       |
| sqlglot_transpile        | 2.68 ms                                                      | 1.78 ms: 1.51x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 6.27 ms: 1.50x faster                                                       |
| richards                 | 75.1 ms                                                      | 50.1 ms: 1.50x faster                                                       |
| pyflate                  | 733 ms                                                       | 496 ms: 1.48x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 213 us: 1.46x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 314 us: 1.45x faster                                                        |
| spectral_norm            | 139 ms                                                       | 96.3 ms: 1.44x faster                                                       |
| mako                     | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                                       |
| logging_format           | 9.64 us                                                      | 6.80 us: 1.42x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.27 us: 1.42x faster                                                       |
| float                    | 111 ms                                                       | 79.4 ms: 1.40x faster                                                       |
| coroutines               | 30.3 ms                                                      | 21.8 ms: 1.39x faster                                                       |
| pycparser                | 1.67 sec                                                     | 1.21 sec: 1.39x faster                                                      |
| deepcopy_reduce          | 4.01 us                                                      | 2.89 us: 1.39x faster                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 4.62 ms: 1.38x faster                                                       |
| thrift                   | 1.18 ms                                                      | 852 us: 1.38x faster                                                        |
| regex_compile            | 190 ms                                                       | 139 ms: 1.37x faster                                                        |
| tornado_http             | 157 ms                                                       | 115 ms: 1.36x faster                                                        |
| fannkuch                 | 483 ms                                                       | 354 ms: 1.36x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 15.7 ms: 1.36x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 70.4 ms: 1.34x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 10.9 ms: 1.34x faster                                                       |
| bench_thread_pool        | 1.14 ms                                                      | 861 us: 1.33x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.64 sec: 1.31x faster                                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 806 ms: 1.30x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 58.9 ms: 1.29x faster                                                       |
| nqueens                  | 115 ms                                                       | 89.3 ms: 1.29x faster                                                       |
| sympy_sum                | 193 ms                                                       | 152 ms: 1.27x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 24.8 ms: 1.27x faster                                                       |
| django_template          | 50.2 ms                                                      | 39.7 ms: 1.26x faster                                                       |
| 2to3                     | 350 ms                                                       | 281 ms: 1.24x faster                                                        |
| sympy_str                | 360 ms                                                       | 291 ms: 1.24x faster                                                        |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.11 ms: 1.24x faster                                                       |
| json_loads               | 30.3 us                                                      | 24.6 us: 1.24x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 22.9 ms: 1.23x faster                                                       |
| mdp                      | 3.01 sec                                                     | 2.49 sec: 1.21x faster                                                      |
| scimark_fft              | 361 ms                                                       | 300 ms: 1.20x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 119 ms: 1.20x faster                                                        |
| sympy_expand             | 600 ms                                                       | 499 ms: 1.20x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 68.2 ms: 1.19x faster                                                       |
| sqlglot_optimize         | 70.1 ms                                                      | 59.0 ms: 1.19x faster                                                       |
| genshi_xml               | 63.3 ms                                                      | 53.4 ms: 1.19x faster                                                       |
| docutils                 | 3.41 sec                                                     | 2.90 sec: 1.18x faster                                                      |
| async_generators         | 421 ms                                                       | 359 ms: 1.17x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.59 sec: 1.13x faster                                                      |
| json                     | 5.86 ms                                                      | 5.21 ms: 1.12x faster                                                       |
| xml_etree_parse          | 160 ms                                                       | 143 ms: 1.12x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 100.0 ms: 1.11x faster                                                      |
| regex_dna                | 261 ms                                                       | 239 ms: 1.09x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 84.5 ms: 1.09x faster                                                       |
| meteor_contest           | 138 ms                                                       | 127 ms: 1.09x faster                                                        |
| pidigits                 | 271 ms                                                       | 252 ms: 1.07x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 26.6 ms: 1.02x faster                                                       |
| telco                    | 7.23 ms                                                      | 8.13 ms: 1.12x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.49 ms: 1.13x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.01 ms: 1.14x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.06 ms: 1.24x slower                                                       |
| coverage                 | 63.3 ms                                                      | 81.1 ms: 1.28x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.49 ms: 1.31x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.36x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (15) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240831-3.14.0a0-34ddb64/bm-20240831-pythonperf2-x86_64-python-34ddb64d088dd7ccc321-3.14.0a0-34ddb64.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.345x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.13x