# Results vs. 3.10.4

- fork: mdboom
- ref: initialize_locals
- machine: linux-x86_64
- commit hash: 1021191
- commit date: 2024-08-29
- overall geometric mean: 1.334x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.21x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 350 ms                                                       | 284 ms: 1.23x faster                                                     |
| docutils       | 3.41 sec                                                     | 2.93 sec: 1.16x faster                                                   |
| html5lib       | 94.6 ms                                                      | 71.2 ms: 1.33x faster                                                    |
| tornado_http   | 157 ms                                                       | 117 ms: 1.35x faster                                                     |
| Geometric mean | (ref)                                                        | 1.27x faster                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|-------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none         | 692 ms                                                       | 323 ms: 2.14x faster                                                     |
| async_tree_memoization  | 819 ms                                                       | 402 ms: 2.04x faster                                                     |
| async_tree_io           | 1.60 sec                                                     | 806 ms: 1.98x faster                                                     |
| async_tree_cpu_io_mixed | 936 ms                                                       | 575 ms: 1.63x faster                                                     |
| Geometric mean          | (ref)                                                        | 1.94x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 134 ms                                                       | 84.8 ms: 1.58x faster                                                    |
| float          | 111 ms                                                       | 78.4 ms: 1.42x faster                                                    |
| pidigits       | 271 ms                                                       | 253 ms: 1.07x faster                                                     |
| Geometric mean | (ref)                                                        | 1.34x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 190 ms                                                       | 142 ms: 1.34x faster                                                     |
| regex_dna      | 261 ms                                                       | 235 ms: 1.11x faster                                                     |
| regex_effbot   | 3.09 ms                                                      | 3.50 ms: 1.13x slower                                                    |
| Geometric mean | (ref)                                                        | 1.07x faster                                                             |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|----------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python   | 455 us                                                       | 318 us: 1.43x faster                                                     |
| unpickle_pure_python | 312 us                                                       | 219 us: 1.43x faster                                                     |
| json_dumps           | 14.5 ms                                                      | 11.0 ms: 1.33x faster                                                    |
| xml_etree_process    | 75.9 ms                                                      | 59.5 ms: 1.28x faster                                                    |
| json_loads           | 30.3 us                                                      | 24.9 us: 1.22x faster                                                    |
| tomli_loads          | 2.92 sec                                                     | 2.58 sec: 1.13x faster                                                   |
| xml_etree_parse      | 160 ms                                                       | 144 ms: 1.11x faster                                                     |
| xml_etree_iterparse  | 110 ms                                                       | 101 ms: 1.09x faster                                                     |
| xml_etree_generate   | 92.3 ms                                                      | 85.7 ms: 1.08x faster                                                    |
| Geometric mean       | (ref)                                                        | 1.22x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                      | 13.4 ms: 1.17x slower                                                    |
| python_startup_no_site | 7.33 ms                                                      | 9.09 ms: 1.24x slower                                                    |
| Geometric mean         | (ref)                                                        | 1.20x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|-----------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                                    |
| genshi_text     | 31.4 ms                                                      | 24.9 ms: 1.26x faster                                                    |
| django_template | 50.2 ms                                                      | 41.2 ms: 1.22x faster                                                    |
| genshi_xml      | 63.3 ms                                                      | 53.6 ms: 1.18x faster                                                    |
| Geometric mean  | (ref)                                                        | 1.27x faster                                                             |

All benchmarks:
===============

| Benchmark                | bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191 |
|--------------------------|:------------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols | 537 us                                                       | 175 us: 3.07x faster                                                     |
| deltablue                | 7.50 ms                                                      | 3.42 ms: 2.19x faster                                                    |
| async_tree_none          | 692 ms                                                       | 323 ms: 2.14x faster                                                     |
| asyncio_tcp              | 779 ms                                                       | 369 ms: 2.11x faster                                                     |
| async_tree_memoization   | 819 ms                                                       | 402 ms: 2.04x faster                                                     |
| async_tree_io            | 1.60 sec                                                     | 806 ms: 1.98x faster                                                     |
| generators               | 57.3 ms                                                      | 29.1 ms: 1.97x faster                                                    |
| asyncio_tcp_ssl          | 3.10 sec                                                     | 1.58 sec: 1.97x faster                                                   |
| go                       | 262 ms                                                       | 137 ms: 1.92x faster                                                     |
| chaos                    | 109 ms                                                       | 61.8 ms: 1.76x faster                                                    |
| scimark_lu               | 167 ms                                                       | 95.6 ms: 1.75x faster                                                    |
| raytrace                 | 489 ms                                                       | 285 ms: 1.72x faster                                                     |
| deepcopy_memo            | 49.8 us                                                      | 29.9 us: 1.66x faster                                                    |
| logging_silent           | 167 ns                                                       | 101 ns: 1.65x faster                                                     |
| deepcopy                 | 468 us                                                       | 287 us: 1.63x faster                                                     |
| async_tree_cpu_io_mixed  | 936 ms                                                       | 575 ms: 1.63x faster                                                     |
| pylint                   | 566 ms                                                       | 350 ms: 1.62x faster                                                     |
| crypto_pyaes             | 119 ms                                                       | 73.9 ms: 1.61x faster                                                    |
| scimark_monte_carlo      | 107 ms                                                       | 66.7 ms: 1.61x faster                                                    |
| richards_super           | 90.6 ms                                                      | 56.5 ms: 1.60x faster                                                    |
| nbody                    | 134 ms                                                       | 84.8 ms: 1.58x faster                                                    |
| pyflate                  | 733 ms                                                       | 469 ms: 1.56x faster                                                     |
| sqlglot_parse            | 2.24 ms                                                      | 1.44 ms: 1.56x faster                                                    |
| comprehensions           | 26.7 us                                                      | 17.6 us: 1.52x faster                                                    |
| hexiom                   | 9.42 ms                                                      | 6.20 ms: 1.52x faster                                                    |
| scimark_sor              | 180 ms                                                       | 119 ms: 1.52x faster                                                     |
| richards                 | 75.1 ms                                                      | 50.0 ms: 1.50x faster                                                    |
| sqlglot_transpile        | 2.68 ms                                                      | 1.83 ms: 1.47x faster                                                    |
| spectral_norm            | 139 ms                                                       | 96.5 ms: 1.44x faster                                                    |
| pickle_pure_python       | 455 us                                                       | 318 us: 1.43x faster                                                     |
| unpickle_pure_python     | 312 us                                                       | 219 us: 1.43x faster                                                     |
| logging_format           | 9.64 us                                                      | 6.78 us: 1.42x faster                                                    |
| mako                     | 14.7 ms                                                      | 10.4 ms: 1.42x faster                                                    |
| float                    | 111 ms                                                       | 78.4 ms: 1.42x faster                                                    |
| logging_simple           | 8.88 us                                                      | 6.27 us: 1.42x faster                                                    |
| coroutines               | 30.3 ms                                                      | 21.4 ms: 1.42x faster                                                    |
| bench_mp_pool            | 6.37 ms                                                      | 4.53 ms: 1.41x faster                                                    |
| deepcopy_reduce          | 4.01 us                                                      | 2.91 us: 1.38x faster                                                    |
| fannkuch                 | 483 ms                                                       | 351 ms: 1.38x faster                                                     |
| thrift                   | 1.18 ms                                                      | 872 us: 1.35x faster                                                     |
| tornado_http             | 157 ms                                                       | 117 ms: 1.35x faster                                                     |
| pathlib                  | 21.4 ms                                                      | 15.9 ms: 1.34x faster                                                    |
| regex_compile            | 190 ms                                                       | 142 ms: 1.34x faster                                                     |
| pycparser                | 1.67 sec                                                     | 1.25 sec: 1.33x faster                                                   |
| html5lib                 | 94.6 ms                                                      | 71.2 ms: 1.33x faster                                                    |
| json_dumps               | 14.5 ms                                                      | 11.0 ms: 1.33x faster                                                    |
| pprint_pformat           | 2.15 sec                                                     | 1.62 sec: 1.33x faster                                                   |
| pprint_safe_repr         | 1.05 sec                                                     | 795 ms: 1.32x faster                                                     |
| bench_thread_pool        | 1.14 ms                                                      | 866 us: 1.32x faster                                                     |
| nqueens                  | 115 ms                                                       | 89.9 ms: 1.28x faster                                                    |
| xml_etree_process        | 75.9 ms                                                      | 59.5 ms: 1.28x faster                                                    |
| genshi_text              | 31.4 ms                                                      | 24.9 ms: 1.26x faster                                                    |
| sympy_sum                | 193 ms                                                       | 153 ms: 1.26x faster                                                     |
| 2to3                     | 350 ms                                                       | 284 ms: 1.23x faster                                                     |
| sympy_str                | 360 ms                                                       | 295 ms: 1.22x faster                                                     |
| json_loads               | 30.3 us                                                      | 24.9 us: 1.22x faster                                                    |
| django_template          | 50.2 ms                                                      | 41.2 ms: 1.22x faster                                                    |
| sympy_integrate          | 28.2 ms                                                      | 23.2 ms: 1.22x faster                                                    |
| sqlglot_normalize        | 144 ms                                                       | 120 ms: 1.20x faster                                                     |
| mdp                      | 3.01 sec                                                     | 2.53 sec: 1.19x faster                                                   |
| sympy_expand             | 600 ms                                                       | 506 ms: 1.19x faster                                                     |
| genshi_xml               | 63.3 ms                                                      | 53.6 ms: 1.18x faster                                                    |
| scimark_sparse_mat_mult  | 5.08 ms                                                      | 4.30 ms: 1.18x faster                                                    |
| sqlglot_optimize         | 70.1 ms                                                      | 59.7 ms: 1.17x faster                                                    |
| docutils                 | 3.41 sec                                                     | 2.93 sec: 1.16x faster                                                   |
| scimark_fft              | 361 ms                                                       | 313 ms: 1.16x faster                                                     |
| async_generators         | 421 ms                                                       | 371 ms: 1.13x faster                                                     |
| tomli_loads              | 2.92 sec                                                     | 2.58 sec: 1.13x faster                                                   |
| regex_dna                | 261 ms                                                       | 235 ms: 1.11x faster                                                     |
| xml_etree_parse          | 160 ms                                                       | 144 ms: 1.11x faster                                                     |
| json                     | 5.86 ms                                                      | 5.30 ms: 1.11x faster                                                    |
| xml_etree_iterparse      | 110 ms                                                       | 101 ms: 1.09x faster                                                     |
| meteor_contest           | 138 ms                                                       | 127 ms: 1.09x faster                                                     |
| xml_etree_generate       | 92.3 ms                                                      | 85.7 ms: 1.08x faster                                                    |
| pidigits                 | 271 ms                                                       | 253 ms: 1.07x faster                                                     |
| asyncio_websockets       | 390 ms                                                       | 387 ms: 1.01x faster                                                     |
| create_gc_cycles         | 1.76 ms                                                      | 1.99 ms: 1.13x slower                                                    |
| regex_effbot             | 3.09 ms                                                      | 3.50 ms: 1.13x slower                                                    |
| telco                    | 7.23 ms                                                      | 8.37 ms: 1.16x slower                                                    |
| python_startup           | 11.5 ms                                                      | 13.4 ms: 1.17x slower                                                    |
| python_startup_no_site   | 7.33 ms                                                      | 9.09 ms: 1.24x slower                                                    |
| coverage                 | 63.3 ms                                                      | 80.1 ms: 1.27x slower                                                    |
| gc_traversal             | 3.42 ms                                                      | 4.47 ms: 1.31x slower                                                    |
| Geometric mean           | (ref)                                                        | 1.35x faster                                                             |

Benchmark hidden because not significant (1): regex_v8
Ignored benchmarks (16) of results/bm-20220323-3.10.4-9d38120/bm-20220323-pythonperf2-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, chameleon, dask, dulwich_log, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlite_synth, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (5) of results/bm-20240829-3.14.0a0-1021191/bm-20240829-pythonperf2-x86_64-mdboom-initialize_locals-3.14.0a0-1021191.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser

- Geometric mean (including insignificant results): 1.334x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.21x

# Memory
- memory change: 1.13x