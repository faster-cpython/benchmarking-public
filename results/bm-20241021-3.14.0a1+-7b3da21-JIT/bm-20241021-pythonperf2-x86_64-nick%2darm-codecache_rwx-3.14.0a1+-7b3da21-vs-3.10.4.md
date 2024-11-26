# Results vs. 3.10.4

- fork: nick-arm
- ref: codecache_rwx
- machine: linux-x86_64
- commit hash: 7b3da21
- commit date: 2024-10-21
- overall geometric mean: 1.280x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.16x faster
- Memory change: 1.35x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 313 ms: 1.12x faster                                                      |
| docutils       | 3.41 sec                                                     | 3.16 sec: 1.08x faster                                                    |
| html5lib       | 94.6 ms                                                      | 70.7 ms: 1.34x faster                                                     |
| tornado_http   | 157 ms                                                       | 123 ms: 1.27x faster                                                      |
| Geometric mean | (ref)                                                        | 1.20x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|-------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 342 ms: 2.02x faster                                                      |
| async_tree_memoization  | 819 ms                                                       | 410 ms: 2.00x faster                                                      |
| async_tree_io           | 1.60 sec                                                     | 844 ms: 1.89x faster                                                      |
| async_tree_cpu_io_mixed | 936 ms                                                       | 576 ms: 1.62x faster                                                      |
| Geometric mean          | (ref)                                                        | 1.88x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 85.2 ms: 1.57x faster                                                     |
| float          | 111 ms                                                       | 78.6 ms: 1.41x faster                                                     |
| pidigits       | 271 ms                                                       | 251 ms: 1.08x faster                                                      |
| Geometric mean | (ref)                                                        | 1.34x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 147 ms: 1.29x faster                                                      |
| regex_dna      | 261 ms                                                       | 241 ms: 1.09x faster                                                      |
| regex_v8       | 27.2 ms                                                      | 25.7 ms: 1.06x faster                                                     |
| regex_effbot   | 3.09 ms                                                      | 3.68 ms: 1.19x slower                                                     |
| Geometric mean | (ref)                                                        | 1.06x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|----------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_pure_python | 312 us                                                       | 217 us: 1.43x faster                                                      |
| tomli_loads          | 2.92 sec                                                     | 2.09 sec: 1.40x faster                                                    |
| pickle_pure_python   | 455 us                                                       | 344 us: 1.32x faster                                                      |
| xml_etree_process    | 75.9 ms                                                      | 58.0 ms: 1.31x faster                                                     |
| json_dumps           | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                                     |
| json_loads           | 30.3 us                                                      | 25.0 us: 1.21x faster                                                     |
| xml_etree_generate   | 92.3 ms                                                      | 81.3 ms: 1.13x faster                                                     |
| xml_etree_iterparse  | 110 ms                                                       | 101 ms: 1.09x faster                                                      |
| xml_etree_parse      | 160 ms                                                       | 148 ms: 1.09x faster                                                      |
| Geometric mean       | (ref)                                                        | 1.25x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 7.33 ms                                                      | 9.00 ms: 1.23x slower                                                     |
| python_startup         | 11.5 ms                                                      | 14.9 ms: 1.29x slower                                                     |
| Geometric mean         | (ref)                                                        | 1.26x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|-----------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 9.43 ms: 1.56x faster                                                     |
| django_template | 50.2 ms                                                      | 44.0 ms: 1.14x faster                                                     |
| genshi_text     | 31.4 ms                                                      | 32.0 ms: 1.02x slower                                                     |
| genshi_xml      | 63.3 ms                                                      | 70.9 ms: 1.12x slower                                                     |
| Geometric mean  | (ref)                                                        | 1.12x faster                                                              |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21 |
|--------------------------|:------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 182 us: 2.94x faster                                                      |
| deltablue                | 7.50 ms                                                      | 3.31 ms: 2.27x faster                                                     |
| async_tree_none          | 692 ms                                                       | 342 ms: 2.02x faster                                                      |
| async_tree_memoization   | 819 ms                                                       | 410 ms: 2.00x faster                                                      |
| async_tree_io            | 1.60 sec                                                     | 844 ms: 1.89x faster                                                      |
| logging_silent           | 167 ns                                                       | 92.2 ns: 1.82x faster                                                     |
| scimark_lu               | 167 ms                                                       | 96.2 ms: 1.73x faster                                                     |
| scimark_sor              | 180 ms                                                       | 104 ms: 1.73x faster                                                      |
| deepcopy_memo            | 49.8 us                                                      | 29.2 us: 1.71x faster                                                     |
| go                       | 262 ms                                                       | 154 ms: 1.70x faster                                                      |
| crypto_pyaes             | 119 ms                                                       | 73.0 ms: 1.63x faster                                                     |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 576 ms: 1.62x faster                                                      |
| pyflate                  | 733 ms                                                       | 459 ms: 1.60x faster                                                      |
| scimark_monte_carlo      | 107 ms                                                       | 68.1 ms: 1.58x faster                                                     |
| nbody                    | 134 ms                                                       | 85.2 ms: 1.57x faster                                                     |
| raytrace                 | 489 ms                                                       | 313 ms: 1.56x faster                                                      |
| mako                     | 14.7 ms                                                      | 9.43 ms: 1.56x faster                                                     |
| richards_super           | 90.6 ms                                                      | 58.2 ms: 1.56x faster                                                     |
| richards                 | 75.1 ms                                                      | 48.8 ms: 1.54x faster                                                     |
| generators               | 57.3 ms                                                      | 37.3 ms: 1.54x faster                                                     |
| chaos                    | 109 ms                                                       | 70.8 ms: 1.53x faster                                                     |
| deepcopy                 | 468 us                                                       | 308 us: 1.52x faster                                                      |
| sqlglot_parse            | 2.24 ms                                                      | 1.49 ms: 1.50x faster                                                     |
| spectral_norm            | 139 ms                                                       | 93.3 ms: 1.49x faster                                                     |
| unpickle_pure_python     | 312 us                                                       | 217 us: 1.43x faster                                                      |
| coroutines               | 30.3 ms                                                      | 21.2 ms: 1.43x faster                                                     |
| float                    | 111 ms                                                       | 78.6 ms: 1.41x faster                                                     |
| comprehensions           | 26.7 us                                                      | 18.9 us: 1.41x faster                                                     |
| tomli_loads              | 2.92 sec                                                     | 2.09 sec: 1.40x faster                                                    |
| pylint                   | 566 ms                                                       | 407 ms: 1.39x faster                                                      |
| sqlglot_transpile        | 2.68 ms                                                      | 1.95 ms: 1.38x faster                                                     |
| pathlib                  | 21.4 ms                                                      | 15.9 ms: 1.35x faster                                                     |
| logging_simple           | 8.88 us                                                      | 6.60 us: 1.35x faster                                                     |
| html5lib                 | 94.6 ms                                                      | 70.7 ms: 1.34x faster                                                     |
| logging_format           | 9.64 us                                                      | 7.29 us: 1.32x faster                                                     |
| pickle_pure_python       | 455 us                                                       | 344 us: 1.32x faster                                                      |
| hexiom                   | 9.42 ms                                                      | 7.12 ms: 1.32x faster                                                     |
| deepcopy_reduce          | 4.01 us                                                      | 3.03 us: 1.32x faster                                                     |
| pprint_safe_repr         | 1.05 sec                                                     | 801 ms: 1.31x faster                                                      |
| xml_etree_process        | 75.9 ms                                                      | 58.0 ms: 1.31x faster                                                     |
| thrift                   | 1.18 ms                                                      | 899 us: 1.31x faster                                                      |
| pprint_pformat           | 2.15 sec                                                     | 1.65 sec: 1.31x faster                                                    |
| fannkuch                 | 483 ms                                                       | 371 ms: 1.30x faster                                                      |
| pycparser                | 1.67 sec                                                     | 1.29 sec: 1.30x faster                                                    |
| json_dumps               | 14.5 ms                                                      | 11.2 ms: 1.30x faster                                                     |
| regex_compile            | 190 ms                                                       | 147 ms: 1.29x faster                                                      |
| scimark_fft              | 361 ms                                                       | 283 ms: 1.28x faster                                                      |
| dulwich_log              | 81.1 ms                                                      | 63.7 ms: 1.27x faster                                                     |
| tornado_http             | 157 ms                                                       | 123 ms: 1.27x faster                                                      |
| json_loads               | 30.3 us                                                      | 25.0 us: 1.21x faster                                                     |
| bench_thread_pool        | 1.14 ms                                                      | 941 us: 1.21x faster                                                      |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.26 ms: 1.19x faster                                                     |
| django_template          | 50.2 ms                                                      | 44.0 ms: 1.14x faster                                                     |
| sympy_str                | 360 ms                                                       | 317 ms: 1.14x faster                                                      |
| sympy_expand             | 600 ms                                                       | 529 ms: 1.13x faster                                                      |
| xml_etree_generate       | 92.3 ms                                                      | 81.3 ms: 1.13x faster                                                     |
| mdp                      | 3.01 sec                                                     | 2.65 sec: 1.13x faster                                                    |
| sympy_sum                | 193 ms                                                       | 171 ms: 1.13x faster                                                      |
| nqueens                  | 115 ms                                                       | 102 ms: 1.12x faster                                                      |
| 2to3                     | 350 ms                                                       | 313 ms: 1.12x faster                                                      |
| json                     | 5.86 ms                                                      | 5.25 ms: 1.12x faster                                                     |
| async_generators         | 421 ms                                                       | 377 ms: 1.12x faster                                                      |
| xml_etree_iterparse      | 110 ms                                                       | 101 ms: 1.09x faster                                                      |
| regex_dna                | 261 ms                                                       | 241 ms: 1.09x faster                                                      |
| xml_etree_parse          | 160 ms                                                       | 148 ms: 1.09x faster                                                      |
| docutils                 | 3.41 sec                                                     | 3.16 sec: 1.08x faster                                                    |
| pidigits                 | 271 ms                                                       | 251 ms: 1.08x faster                                                      |
| sqlglot_normalize        | 144 ms                                                       | 134 ms: 1.07x faster                                                      |
| regex_v8                 | 27.2 ms                                                      | 25.7 ms: 1.06x faster                                                     |
| meteor_contest           | 138 ms                                                       | 131 ms: 1.06x faster                                                      |
| sympy_integrate          | 28.2 ms                                                      | 26.8 ms: 1.05x faster                                                     |
| sqlglot_optimize         | 70.1 ms                                                      | 68.2 ms: 1.03x faster                                                     |
| asyncio_websockets       | 390 ms                                                       | 383 ms: 1.02x faster                                                      |
| genshi_text              | 31.4 ms                                                      | 32.0 ms: 1.02x slower                                                     |
| telco                    | 7.23 ms                                                      | 7.69 ms: 1.06x slower                                                     |
| genshi_xml               | 63.3 ms                                                      | 70.9 ms: 1.12x slower                                                     |
| regex_effbot             | 3.09 ms                                                      | 3.68 ms: 1.19x slower                                                     |
| python_startup_no_site   | 7.33 ms                                                      | 9.00 ms: 1.23x slower                                                     |
| coverage                 | 63.3 ms                                                      | 81.1 ms: 1.28x slower                                                     |
| python_startup           | 11.5 ms                                                      | 14.9 ms: 1.29x slower                                                     |
| gc_traversal             | 3.42 ms                                                      | 5.53 ms: 1.62x slower                                                     |
| create_gc_cycles         | 1.76 ms                                                      | 2.88 ms: 1.63x slower                                                     |
| bench_mp_pool            | 6.37 ms                                                      | 2.82 sec: 441.88x slower                                                  |
| Geometric mean           | (ref)                                                        | 1.19x faster                                                              |
Ignored benchmarks (17) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (6) of results/bm-20241021-3.14.0a1+-7b3da21-JIT/bm-20241021-pythonperf2-x86_64-nick%2darm-codecache_rwx-3.14.0a1+-7b3da21.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, sphinx

- Geometric mean (including insignificant results): 1.280x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.20x
- 99% likely to have a speedup of 1.16x

# Memory
- memory change: 1.35x