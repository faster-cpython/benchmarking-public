# Results vs. 3.10.4

- fork: python
- ref: 2c1b1e7a07eba0138b98
- machine: linux-x86_64
- commit hash: 2c1b1e7
- commit date: 2024-07-23
- overall geometric mean: 1.35x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 287 ms: 1.22x faster                                                        |
| docutils       | 3.41 sec                                                     | 2.98 sec: 1.15x faster                                                      |
| html5lib       | 94.6 ms                                                      | 73.9 ms: 1.28x faster                                                       |
| tornado_http   | 157 ms                                                       | 119 ms: 1.32x faster                                                        |
| Geometric mean | (ref)                                                        | 1.24x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|-------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 333 ms: 2.08x faster                                                        |
| async_tree_memoization  | 819 ms                                                       | 401 ms: 2.04x faster                                                        |
| async_tree_io           | 1.60 sec                                                     | 813 ms: 1.97x faster                                                        |
| async_tree_cpu_io_mixed | 936 ms                                                       | 577 ms: 1.62x faster                                                        |
| Geometric mean          | (ref)                                                        | 1.92x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 85.1 ms: 1.58x faster                                                       |
| float          | 111 ms                                                       | 81.3 ms: 1.37x faster                                                       |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| Geometric mean | (ref)                                                        | 1.32x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 141 ms: 1.35x faster                                                        |
| regex_dna      | 261 ms                                                       | 237 ms: 1.10x faster                                                        |
| regex_v8       | 27.2 ms                                                      | 25.9 ms: 1.05x faster                                                       |
| regex_effbot   | 3.09 ms                                                      | 3.50 ms: 1.13x slower                                                       |
| Geometric mean | (ref)                                                        | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|----------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 216 us: 1.45x faster                                                        |
| pickle_pure_python   | 455 us                                                       | 317 us: 1.43x faster                                                        |
| json_dumps           | 14.5 ms                                                      | 10.9 ms: 1.34x faster                                                       |
| xml_etree_process    | 75.9 ms                                                      | 58.9 ms: 1.29x faster                                                       |
| json_loads           | 30.3 us                                                      | 25.0 us: 1.21x faster                                                       |
| tomli_loads          | 2.92 sec                                                     | 2.44 sec: 1.19x faster                                                      |
| xml_etree_parse      | 160 ms                                                       | 145 ms: 1.11x faster                                                        |
| xml_etree_generate   | 92.3 ms                                                      | 83.8 ms: 1.10x faster                                                       |
| xml_etree_iterparse  | 110 ms                                                       | 103 ms: 1.07x faster                                                        |
| Geometric mean       | (ref)                                                        | 1.24x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| python_startup_no_site | 7.33 ms                                                      | 9.07 ms: 1.24x slower                                                       |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|-----------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.4 ms: 1.41x faster                                                       |
| django_template | 50.2 ms                                                      | 39.7 ms: 1.26x faster                                                       |
| genshi_text     | 31.4 ms                                                      | 25.6 ms: 1.23x faster                                                       |
| genshi_xml      | 63.3 ms                                                      | 54.2 ms: 1.17x faster                                                       |
| Geometric mean  | (ref)                                                        | 1.26x faster                                                                |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7 |
|--------------------------|:------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 172 us: 3.12x faster                                                        |
| deltablue                | 7.50 ms                                                      | 3.43 ms: 2.19x faster                                                       |
| async_tree_none          | 692 ms                                                       | 333 ms: 2.08x faster                                                        |
| asyncio_tcp              | 779 ms                                                       | 377 ms: 2.07x faster                                                        |
| async_tree_memoization   | 819 ms                                                       | 401 ms: 2.04x faster                                                        |
| generators               | 57.3 ms                                                      | 28.3 ms: 2.03x faster                                                       |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.97x faster                                                      |
| async_tree_io            | 1.60 sec                                                     | 813 ms: 1.97x faster                                                        |
| chaos                    | 109 ms                                                       | 60.6 ms: 1.79x faster                                                       |
| raytrace                 | 489 ms                                                       | 273 ms: 1.79x faster                                                        |
| deepcopy_memo            | 49.8 us                                                      | 29.0 us: 1.72x faster                                                       |
| scimark_lu               | 167 ms                                                       | 97.3 ms: 1.71x faster                                                       |
| logging_silent           | 167 ns                                                       | 97.9 ns: 1.71x faster                                                       |
| scimark_sor              | 180 ms                                                       | 110 ms: 1.64x faster                                                        |
| crypto_pyaes             | 119 ms                                                       | 73.0 ms: 1.63x faster                                                       |
| deepcopy                 | 468 us                                                       | 288 us: 1.63x faster                                                        |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 577 ms: 1.62x faster                                                        |
| pylint                   | 566 ms                                                       | 350 ms: 1.62x faster                                                        |
| go                       | 262 ms                                                       | 162 ms: 1.61x faster                                                        |
| sqlglot_parse            | 2.24 ms                                                      | 1.40 ms: 1.59x faster                                                       |
| nbody                    | 134 ms                                                       | 85.1 ms: 1.58x faster                                                       |
| scimark_monte_carlo      | 107 ms                                                       | 68.9 ms: 1.56x faster                                                       |
| comprehensions           | 26.7 us                                                      | 17.3 us: 1.55x faster                                                       |
| richards_super           | 90.6 ms                                                      | 59.1 ms: 1.53x faster                                                       |
| sqlglot_transpile        | 2.68 ms                                                      | 1.79 ms: 1.50x faster                                                       |
| hexiom                   | 9.42 ms                                                      | 6.37 ms: 1.48x faster                                                       |
| spectral_norm            | 139 ms                                                       | 94.9 ms: 1.47x faster                                                       |
| pyflate                  | 733 ms                                                       | 504 ms: 1.46x faster                                                        |
| unpickle_pure_python     | 312 us                                                       | 216 us: 1.45x faster                                                        |
| pickle_pure_python       | 455 us                                                       | 317 us: 1.43x faster                                                        |
| richards                 | 75.1 ms                                                      | 52.5 ms: 1.43x faster                                                       |
| logging_simple           | 8.88 us                                                      | 6.26 us: 1.42x faster                                                       |
| mako                     | 14.7 ms                                                      | 10.4 ms: 1.41x faster                                                       |
| bench_mp_pool            | 6.37 ms                                                      | 4.58 ms: 1.39x faster                                                       |
| logging_format           | 9.64 us                                                      | 7.00 us: 1.38x faster                                                       |
| deepcopy_reduce          | 4.01 us                                                      | 2.92 us: 1.37x faster                                                       |
| coroutines               | 30.3 ms                                                      | 22.1 ms: 1.37x faster                                                       |
| float                    | 111 ms                                                       | 81.3 ms: 1.37x faster                                                       |
| regex_compile            | 190 ms                                                       | 141 ms: 1.35x faster                                                        |
| pathlib                  | 21.4 ms                                                      | 16.0 ms: 1.34x faster                                                       |
| json_dumps               | 14.5 ms                                                      | 10.9 ms: 1.34x faster                                                       |
| thrift                   | 1.18 ms                                                      | 882 us: 1.33x faster                                                        |
| tornado_http             | 157 ms                                                       | 119 ms: 1.32x faster                                                        |
| pycparser                | 1.67 sec                                                     | 1.27 sec: 1.31x faster                                                      |
| fannkuch                 | 483 ms                                                       | 367 ms: 1.31x faster                                                        |
| bench_thread_pool        | 1.14 ms                                                      | 872 us: 1.31x faster                                                        |
| pprint_pformat           | 2.15 sec                                                     | 1.66 sec: 1.30x faster                                                      |
| pprint_safe_repr         | 1.05 sec                                                     | 814 ms: 1.29x faster                                                        |
| xml_etree_process        | 75.9 ms                                                      | 58.9 ms: 1.29x faster                                                       |
| nqueens                  | 115 ms                                                       | 89.6 ms: 1.28x faster                                                       |
| html5lib                 | 94.6 ms                                                      | 73.9 ms: 1.28x faster                                                       |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.01 ms: 1.27x faster                                                       |
| django_template          | 50.2 ms                                                      | 39.7 ms: 1.26x faster                                                       |
| sympy_sum                | 193 ms                                                       | 156 ms: 1.24x faster                                                        |
| dask                     | 472 ms                                                       | 383 ms: 1.23x faster                                                        |
| dulwich_log              | 81.1 ms                                                      | 66.0 ms: 1.23x faster                                                       |
| scimark_fft              | 361 ms                                                       | 294 ms: 1.23x faster                                                        |
| genshi_text              | 31.4 ms                                                      | 25.6 ms: 1.23x faster                                                       |
| sympy_str                | 360 ms                                                       | 294 ms: 1.23x faster                                                        |
| 2to3                     | 350 ms                                                       | 287 ms: 1.22x faster                                                        |
| sqlglot_normalize        | 144 ms                                                       | 118 ms: 1.21x faster                                                        |
| json_loads               | 30.3 us                                                      | 25.0 us: 1.21x faster                                                       |
| sympy_integrate          | 28.2 ms                                                      | 23.5 ms: 1.20x faster                                                       |
| sympy_expand             | 600 ms                                                       | 501 ms: 1.20x faster                                                        |
| tomli_loads              | 2.92 sec                                                     | 2.44 sec: 1.19x faster                                                      |
| mdp                      | 3.01 sec                                                     | 2.52 sec: 1.19x faster                                                      |
| sqlglot_optimize         | 70.1 ms                                                      | 59.2 ms: 1.18x faster                                                       |
| genshi_xml               | 63.3 ms                                                      | 54.2 ms: 1.17x faster                                                       |
| async_generators         | 421 ms                                                       | 361 ms: 1.16x faster                                                        |
| docutils                 | 3.41 sec                                                     | 2.98 sec: 1.15x faster                                                      |
| xml_etree_parse          | 160 ms                                                       | 145 ms: 1.11x faster                                                        |
| xml_etree_generate       | 92.3 ms                                                      | 83.8 ms: 1.10x faster                                                       |
| regex_dna                | 261 ms                                                       | 237 ms: 1.10x faster                                                        |
| json                     | 5.86 ms                                                      | 5.41 ms: 1.08x faster                                                       |
| meteor_contest           | 138 ms                                                       | 128 ms: 1.08x faster                                                        |
| xml_etree_iterparse      | 110 ms                                                       | 103 ms: 1.07x faster                                                        |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                        |
| regex_v8                 | 27.2 ms                                                      | 25.9 ms: 1.05x faster                                                       |
| telco                    | 7.23 ms                                                      | 7.80 ms: 1.08x slower                                                       |
| regex_effbot             | 3.09 ms                                                      | 3.50 ms: 1.13x slower                                                       |
| create_gc_cycles         | 1.76 ms                                                      | 2.01 ms: 1.14x slower                                                       |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.16x slower                                                       |
| python_startup_no_site   | 7.33 ms                                                      | 9.07 ms: 1.24x slower                                                       |
| coverage                 | 63.3 ms                                                      | 78.7 ms: 1.24x slower                                                       |
| gc_traversal             | 3.42 ms                                                      | 4.72 ms: 1.38x slower                                                       |
| Geometric mean           | (ref)                                                        | 1.35x faster                                                                |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (14) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240723-3.14.0a0-2c1b1e7/bm-20240723-pythonperf2-x86_64-python-2c1b1e7a07eba0138b98-3.14.0a0-2c1b1e7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.13x