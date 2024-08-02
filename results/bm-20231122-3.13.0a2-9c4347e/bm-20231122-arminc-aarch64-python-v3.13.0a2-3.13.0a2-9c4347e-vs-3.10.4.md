# Results vs. 3.10.4

- fork: python
- ref: v3.13.0a2
- machine: linux-aarch64
- commit hash: 9c4347e
- commit date: 2023-11-22
- overall geometric mean: 1.30x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.24x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 303 ms: 1.26x faster                                         |
| chameleon      | 10.8 ms                                                               | 8.96 ms: 1.21x faster                                        |
| docutils       | 3.53 sec                                                              | 2.88 sec: 1.23x faster                                       |
| html5lib       | 86.5 ms                                                               | 65.7 ms: 1.32x faster                                        |
| tornado_http   | 178 ms                                                                | 135 ms: 1.32x faster                                         |
| Geometric mean | (ref)                                                                 | 1.26x faster                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 572 ms: 1.66x faster                                         |
| async_tree_io           | 2.28 sec                                                              | 1.44 sec: 1.58x faster                                       |
| async_tree_memoization  | 1.13 sec                                                              | 736 ms: 1.54x faster                                         |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 882 ms: 1.44x faster                                         |
| Geometric mean          | (ref)                                                                 | 1.56x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 105 ms: 1.58x faster                                         |
| float          | 135 ms                                                                | 90.6 ms: 1.49x faster                                        |
| pidigits       | 235 ms                                                                | 234 ms: 1.00x faster                                         |
| Geometric mean | (ref)                                                                 | 1.33x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 129 ms: 1.37x faster                                         |
| regex_v8       | 32.2 ms                                                               | 30.0 ms: 1.07x faster                                        |
| regex_dna      | 257 ms                                                                | 246 ms: 1.04x faster                                         |
| regex_effbot   | 4.25 ms                                                               | 4.61 ms: 1.09x slower                                        |
| Geometric mean | (ref)                                                                 | 1.09x faster                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 346 us: 1.53x faster                                         |
| unpickle_pure_python | 366 us                                                                | 253 us: 1.45x faster                                         |
| json_dumps           | 16.7 ms                                                               | 12.4 ms: 1.34x faster                                        |
| tomli_loads          | 3.36 sec                                                              | 2.57 sec: 1.31x faster                                       |
| xml_etree_process    | 99.5 ms                                                               | 79.5 ms: 1.25x faster                                        |
| unpickle_list        | 6.99 us                                                               | 6.12 us: 1.14x faster                                        |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.09x faster                                         |
| xml_etree_parse      | 212 ms                                                                | 196 ms: 1.08x faster                                         |
| xml_etree_iterparse  | 156 ms                                                                | 149 ms: 1.04x faster                                         |
| pickle_list          | 5.24 us                                                               | 5.19 us: 1.01x faster                                        |
| json_loads           | 30.9 us                                                               | 30.8 us: 1.00x faster                                        |
| pickle_dict          | 35.1 us                                                               | 37.5 us: 1.07x slower                                        |
| unpickle             | 17.5 us                                                               | 18.7 us: 1.07x slower                                        |
| pickle               | 12.5 us                                                               | 13.5 us: 1.08x slower                                        |
| Geometric mean       | (ref)                                                                 | 1.13x faster                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 12.6 ms: 1.12x slower                                        |
| python_startup_no_site | 6.89 ms                                                               | 10.9 ms: 1.58x slower                                        |
| Geometric mean         | (ref)                                                                 | 1.33x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 12.8 ms: 1.47x faster                                        |
| django_template | 53.3 ms                                                               | 40.9 ms: 1.31x faster                                        |
| genshi_text     | 35.2 ms                                                               | 27.9 ms: 1.26x faster                                        |
| genshi_xml      | 69.8 ms                                                               | 60.7 ms: 1.15x faster                                        |
| Geometric mean  | (ref)                                                                 | 1.29x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 138 us: 4.78x faster                                         |
| deltablue                | 8.94 ms                                                               | 4.00 ms: 2.24x faster                                        |
| bench_mp_pool            | 14.5 ms                                                               | 6.91 ms: 2.10x faster                                        |
| raytrace                 | 573 ms                                                                | 299 ms: 1.92x faster                                         |
| chaos                    | 121 ms                                                                | 66.9 ms: 1.81x faster                                        |
| richards_super           | 107 ms                                                                | 60.7 ms: 1.77x faster                                        |
| sqlglot_parse            | 2.40 ms                                                               | 1.37 ms: 1.76x faster                                        |
| richards                 | 91.7 ms                                                               | 52.2 ms: 1.76x faster                                        |
| crypto_pyaes             | 134 ms                                                                | 77.5 ms: 1.73x faster                                        |
| generators               | 68.1 ms                                                               | 39.5 ms: 1.72x faster                                        |
| asyncio_tcp              | 944 ms                                                                | 551 ms: 1.71x faster                                         |
| logging_silent           | 222 ns                                                                | 130 ns: 1.71x faster                                         |
| comprehensions           | 33.1 us                                                               | 19.7 us: 1.68x faster                                        |
| async_tree_none          | 950 ms                                                                | 572 ms: 1.66x faster                                         |
| sqlglot_transpile        | 2.84 ms                                                               | 1.72 ms: 1.66x faster                                        |
| go                       | 264 ms                                                                | 160 ms: 1.65x faster                                         |
| scimark_lu               | 227 ms                                                                | 141 ms: 1.61x faster                                         |
| async_tree_io            | 2.28 sec                                                              | 1.44 sec: 1.58x faster                                       |
| nbody                    | 166 ms                                                                | 105 ms: 1.58x faster                                         |
| scimark_monte_carlo      | 128 ms                                                                | 81.1 ms: 1.58x faster                                        |
| hexiom                   | 10.9 ms                                                               | 7.03 ms: 1.55x faster                                        |
| async_tree_memoization   | 1.13 sec                                                              | 736 ms: 1.54x faster                                         |
| pickle_pure_python       | 529 us                                                                | 346 us: 1.53x faster                                         |
| scimark_sor              | 246 ms                                                                | 162 ms: 1.52x faster                                         |
| float                    | 135 ms                                                                | 90.6 ms: 1.49x faster                                        |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.21 sec: 1.49x faster                                       |
| mako                     | 18.9 ms                                                               | 12.8 ms: 1.47x faster                                        |
| spectral_norm            | 186 ms                                                                | 129 ms: 1.45x faster                                         |
| unpickle_pure_python     | 366 us                                                                | 253 us: 1.45x faster                                         |
| pylint                   | 485 ms                                                                | 336 ms: 1.45x faster                                         |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 882 ms: 1.44x faster                                         |
| pyflate                  | 795 ms                                                                | 565 ms: 1.41x faster                                         |
| logging_simple           | 9.78 us                                                               | 7.12 us: 1.37x faster                                        |
| logging_format           | 10.6 us                                                               | 7.74 us: 1.37x faster                                        |
| regex_compile            | 177 ms                                                                | 129 ms: 1.37x faster                                         |
| thrift                   | 1.26 ms                                                               | 923 us: 1.37x faster                                         |
| json_dumps               | 16.7 ms                                                               | 12.4 ms: 1.34x faster                                        |
| pycparser                | 1.69 sec                                                              | 1.26 sec: 1.34x faster                                       |
| tornado_http             | 178 ms                                                                | 135 ms: 1.32x faster                                         |
| html5lib                 | 86.5 ms                                                               | 65.7 ms: 1.32x faster                                        |
| sympy_sum                | 184 ms                                                                | 140 ms: 1.31x faster                                         |
| tomli_loads              | 3.36 sec                                                              | 2.57 sec: 1.31x faster                                       |
| django_template          | 53.3 ms                                                               | 40.9 ms: 1.31x faster                                        |
| sympy_integrate          | 26.5 ms                                                               | 20.4 ms: 1.30x faster                                        |
| deepcopy_memo            | 61.7 us                                                               | 48.2 us: 1.28x faster                                        |
| coroutines               | 37.2 ms                                                               | 29.2 ms: 1.27x faster                                        |
| sqlglot_normalize        | 156 ms                                                                | 123 ms: 1.26x faster                                         |
| sympy_str                | 329 ms                                                                | 260 ms: 1.26x faster                                         |
| genshi_text              | 35.2 ms                                                               | 27.9 ms: 1.26x faster                                        |
| 2to3                     | 381 ms                                                                | 303 ms: 1.26x faster                                         |
| pprint_pformat           | 2.36 sec                                                              | 1.88 sec: 1.26x faster                                       |
| pprint_safe_repr         | 1.15 sec                                                              | 916 ms: 1.25x faster                                         |
| xml_etree_process        | 99.5 ms                                                               | 79.5 ms: 1.25x faster                                        |
| aiohttp                  | 1.39 ms                                                               | 1.11 ms: 1.25x faster                                        |
| sqlglot_optimize         | 75.4 ms                                                               | 60.6 ms: 1.24x faster                                        |
| dulwich_log              | 73.5 ms                                                               | 59.4 ms: 1.24x faster                                        |
| docutils                 | 3.53 sec                                                              | 2.88 sec: 1.23x faster                                       |
| bench_thread_pool        | 1.59 ms                                                               | 1.31 ms: 1.22x faster                                        |
| gunicorn                 | 1.45 ms                                                               | 1.19 ms: 1.21x faster                                        |
| sympy_expand             | 543 ms                                                                | 448 ms: 1.21x faster                                         |
| chameleon                | 10.8 ms                                                               | 8.96 ms: 1.21x faster                                        |
| nqueens                  | 117 ms                                                                | 97.6 ms: 1.20x faster                                        |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.34 ms: 1.20x faster                                        |
| create_gc_cycles         | 2.26 ms                                                               | 1.89 ms: 1.20x faster                                        |
| fannkuch                 | 546 ms                                                                | 458 ms: 1.19x faster                                         |
| deepcopy                 | 511 us                                                                | 433 us: 1.18x faster                                         |
| deepcopy_reduce          | 4.60 us                                                               | 3.93 us: 1.17x faster                                        |
| scimark_fft              | 500 ms                                                                | 428 ms: 1.17x faster                                         |
| genshi_xml               | 69.8 ms                                                               | 60.7 ms: 1.15x faster                                        |
| unpickle_list            | 6.99 us                                                               | 6.12 us: 1.14x faster                                        |
| mdp                      | 3.70 sec                                                              | 3.33 sec: 1.11x faster                                       |
| meteor_contest           | 126 ms                                                                | 114 ms: 1.10x faster                                         |
| pathlib                  | 26.3 ms                                                               | 23.9 ms: 1.10x faster                                        |
| sqlite_synth             | 4.12 us                                                               | 3.77 us: 1.09x faster                                        |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.09x faster                                         |
| xml_etree_parse          | 212 ms                                                                | 196 ms: 1.08x faster                                         |
| json                     | 5.88 ms                                                               | 5.49 ms: 1.07x faster                                        |
| regex_v8                 | 32.2 ms                                                               | 30.0 ms: 1.07x faster                                        |
| flaskblogging            | 4.83 ms                                                               | 4.57 ms: 1.06x faster                                        |
| regex_dna                | 257 ms                                                                | 246 ms: 1.04x faster                                         |
| xml_etree_iterparse      | 156 ms                                                                | 149 ms: 1.04x faster                                         |
| pickle_list              | 5.24 us                                                               | 5.19 us: 1.01x faster                                        |
| pidigits                 | 235 ms                                                                | 234 ms: 1.00x faster                                         |
| json_loads               | 30.9 us                                                               | 30.8 us: 1.00x faster                                        |
| async_generators         | 452 ms                                                                | 480 ms: 1.06x slower                                         |
| gc_traversal             | 4.15 ms                                                               | 4.44 ms: 1.07x slower                                        |
| pickle_dict              | 35.1 us                                                               | 37.5 us: 1.07x slower                                        |
| unpickle                 | 17.5 us                                                               | 18.7 us: 1.07x slower                                        |
| pickle                   | 12.5 us                                                               | 13.5 us: 1.08x slower                                        |
| regex_effbot             | 4.25 ms                                                               | 4.61 ms: 1.09x slower                                        |
| python_startup           | 11.2 ms                                                               | 12.6 ms: 1.12x slower                                        |
| telco                    | 8.49 ms                                                               | 9.69 ms: 1.14x slower                                        |
| coverage                 | 83.6 ms                                                               | 99.8 ms: 1.19x slower                                        |
| python_startup_no_site   | 6.89 ms                                                               | 10.9 ms: 1.58x slower                                        |
| Geometric mean           | (ref)                                                                 | 1.30x faster                                                 |

Benchmark hidden because not significant (2): mypy2, asyncio_websockets
Ignored benchmarks (3) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: dask, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20231122-3.13.0a2-9c4347e/bm-20231122-arminc-aarch64-python-v3.13.0a2-3.13.0a2-9c4347e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.24x

# Memory
- memory change: 1.07x