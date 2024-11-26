# Results vs. 3.10.4

- fork: nick-arm
- ref: codecache
- machine: linux-aarch64
- commit hash: aa18ec3
- commit date: 2024-10-07
- overall geometric mean: 1.188x faster
- HPT reliability: 99.99%
- HPT 99th percentile: 1.03x faster
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 374 ms: 1.02x faster                                             |
| docutils       | 3.53 sec                                                              | 3.63 sec: 1.03x slower                                           |
| html5lib       | 86.5 ms                                                               | 71.3 ms: 1.21x faster                                            |
| tornado_http   | 178 ms                                                                | 142 ms: 1.26x faster                                             |
| Geometric mean | (ref)                                                                 | 1.11x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|-------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 448 ms: 2.12x faster                                             |
| async_tree_io           | 2.28 sec                                                              | 1.15 sec: 1.99x faster                                           |
| async_tree_memoization  | 1.13 sec                                                              | 591 ms: 1.92x faster                                             |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 752 ms: 1.69x faster                                             |
| Geometric mean          | (ref)                                                                 | 1.92x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 135 ms                                                                | 90.0 ms: 1.50x faster                                            |
| nbody          | 166 ms                                                                | 113 ms: 1.47x faster                                             |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                     |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_dna      | 257 ms                                                                | 247 ms: 1.04x faster                                             |
| regex_v8       | 32.2 ms                                                               | 31.4 ms: 1.02x faster                                            |
| regex_compile  | 177 ms                                                                | 181 ms: 1.02x slower                                             |
| regex_effbot   | 4.25 ms                                                               | 4.90 ms: 1.15x slower                                            |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 384 us: 1.38x faster                                             |
| unpickle_pure_python | 366 us                                                                | 267 us: 1.37x faster                                             |
| tomli_loads          | 3.36 sec                                                              | 2.61 sec: 1.29x faster                                           |
| json_dumps           | 16.7 ms                                                               | 13.2 ms: 1.26x faster                                            |
| xml_etree_process    | 99.5 ms                                                               | 80.0 ms: 1.24x faster                                            |
| xml_etree_generate   | 123 ms                                                                | 110 ms: 1.11x faster                                             |
| xml_etree_parse      | 212 ms                                                                | 192 ms: 1.11x faster                                             |
| unpickle_list        | 6.99 us                                                               | 6.40 us: 1.09x faster                                            |
| xml_etree_iterparse  | 156 ms                                                                | 152 ms: 1.03x faster                                             |
| pickle_list          | 5.24 us                                                               | 5.21 us: 1.00x faster                                            |
| pickle_dict          | 35.1 us                                                               | 38.1 us: 1.08x slower                                            |
| pickle               | 12.5 us                                                               | 13.6 us: 1.09x slower                                            |
| unpickle             | 17.5 us                                                               | 19.2 us: 1.10x slower                                            |
| Geometric mean       | (ref)                                                                 | 1.11x faster                                                     |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.1 ms: 1.17x slower                                            |
| python_startup_no_site | 6.89 ms                                                               | 8.81 ms: 1.28x slower                                            |
| Geometric mean         | (ref)                                                                 | 1.22x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.2 ms: 1.44x faster                                            |
| django_template | 53.3 ms                                                               | 51.9 ms: 1.03x faster                                            |
| genshi_xml      | 69.8 ms                                                               | 83.0 ms: 1.19x slower                                            |
| Geometric mean  | (ref)                                                                 | 1.06x faster                                                     |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|--------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 211 us: 3.14x faster                                             |
| async_tree_none          | 950 ms                                                                | 448 ms: 2.12x faster                                             |
| deltablue                | 8.94 ms                                                               | 4.38 ms: 2.04x faster                                            |
| async_tree_io            | 2.28 sec                                                              | 1.15 sec: 1.99x faster                                           |
| async_tree_memoization   | 1.13 sec                                                              | 591 ms: 1.92x faster                                             |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 752 ms: 1.69x faster                                             |
| logging_silent           | 222 ns                                                                | 133 ns: 1.67x faster                                             |
| raytrace                 | 573 ms                                                                | 347 ms: 1.65x faster                                             |
| deepcopy_memo            | 61.7 us                                                               | 37.4 us: 1.65x faster                                            |
| crypto_pyaes             | 134 ms                                                                | 88.1 ms: 1.52x faster                                            |
| richards                 | 91.7 ms                                                               | 60.3 ms: 1.52x faster                                            |
| asyncio_tcp              | 944 ms                                                                | 622 ms: 1.52x faster                                             |
| richards_super           | 107 ms                                                                | 70.7 ms: 1.52x faster                                            |
| scimark_lu               | 227 ms                                                                | 150 ms: 1.51x faster                                             |
| float                    | 135 ms                                                                | 90.0 ms: 1.50x faster                                            |
| scimark_sor              | 246 ms                                                                | 167 ms: 1.47x faster                                             |
| nbody                    | 166 ms                                                                | 113 ms: 1.47x faster                                             |
| scimark_monte_carlo      | 128 ms                                                                | 87.5 ms: 1.46x faster                                            |
| mako                     | 18.9 ms                                                               | 13.2 ms: 1.44x faster                                            |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.29 sec: 1.44x faster                                           |
| sqlglot_parse            | 2.40 ms                                                               | 1.68 ms: 1.43x faster                                            |
| go                       | 264 ms                                                                | 189 ms: 1.40x faster                                             |
| pickle_pure_python       | 529 us                                                                | 384 us: 1.38x faster                                             |
| chaos                    | 121 ms                                                                | 88.3 ms: 1.37x faster                                            |
| unpickle_pure_python     | 366 us                                                                | 267 us: 1.37x faster                                             |
| comprehensions           | 33.1 us                                                               | 24.5 us: 1.35x faster                                            |
| logging_format           | 10.6 us                                                               | 8.02 us: 1.32x faster                                            |
| logging_simple           | 9.78 us                                                               | 7.40 us: 1.32x faster                                            |
| thrift                   | 1.26 ms                                                               | 960 us: 1.31x faster                                             |
| coroutines               | 37.2 ms                                                               | 28.7 ms: 1.30x faster                                            |
| pyflate                  | 795 ms                                                                | 617 ms: 1.29x faster                                             |
| tomli_loads              | 3.36 sec                                                              | 2.61 sec: 1.29x faster                                           |
| spectral_norm            | 186 ms                                                                | 145 ms: 1.28x faster                                             |
| sqlglot_transpile        | 2.84 ms                                                               | 2.22 ms: 1.28x faster                                            |
| json_dumps               | 16.7 ms                                                               | 13.2 ms: 1.26x faster                                            |
| deepcopy                 | 511 us                                                                | 405 us: 1.26x faster                                             |
| tornado_http             | 178 ms                                                                | 142 ms: 1.26x faster                                             |
| xml_etree_process        | 99.5 ms                                                               | 80.0 ms: 1.24x faster                                            |
| pathlib                  | 26.3 ms                                                               | 21.5 ms: 1.22x faster                                            |
| html5lib                 | 86.5 ms                                                               | 71.3 ms: 1.21x faster                                            |
| deepcopy_reduce          | 4.60 us                                                               | 3.85 us: 1.19x faster                                            |
| bench_thread_pool        | 1.59 ms                                                               | 1.37 ms: 1.16x faster                                            |
| pycparser                | 1.69 sec                                                              | 1.47 sec: 1.15x faster                                           |
| generators               | 68.1 ms                                                               | 59.3 ms: 1.15x faster                                            |
| scimark_fft              | 500 ms                                                                | 444 ms: 1.13x faster                                             |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.79 ms: 1.12x faster                                            |
| xml_etree_generate       | 123 ms                                                                | 110 ms: 1.11x faster                                             |
| xml_etree_parse          | 212 ms                                                                | 192 ms: 1.11x faster                                             |
| unpickle_list            | 6.99 us                                                               | 6.40 us: 1.09x faster                                            |
| fannkuch                 | 546 ms                                                                | 503 ms: 1.08x faster                                             |
| sqlite_synth             | 4.12 us                                                               | 3.81 us: 1.08x faster                                            |
| hexiom                   | 10.9 ms                                                               | 10.1 ms: 1.08x faster                                            |
| mdp                      | 3.70 sec                                                              | 3.50 sec: 1.06x faster                                           |
| json                     | 5.88 ms                                                               | 5.57 ms: 1.06x faster                                            |
| regex_dna                | 257 ms                                                                | 247 ms: 1.04x faster                                             |
| django_template          | 53.3 ms                                                               | 51.9 ms: 1.03x faster                                            |
| xml_etree_iterparse      | 156 ms                                                                | 152 ms: 1.03x faster                                             |
| regex_v8                 | 32.2 ms                                                               | 31.4 ms: 1.02x faster                                            |
| 2to3                     | 381 ms                                                                | 374 ms: 1.02x faster                                             |
| meteor_contest           | 126 ms                                                                | 125 ms: 1.01x faster                                             |
| sqlglot_normalize        | 156 ms                                                                | 155 ms: 1.01x faster                                             |
| pickle_list              | 5.24 us                                                               | 5.21 us: 1.00x faster                                            |
| asyncio_websockets       | 657 ms                                                                | 663 ms: 1.01x slower                                             |
| regex_compile            | 177 ms                                                                | 181 ms: 1.02x slower                                             |
| create_gc_cycles         | 2.26 ms                                                               | 2.31 ms: 1.02x slower                                            |
| docutils                 | 3.53 sec                                                              | 3.63 sec: 1.03x slower                                           |
| dulwich_log              | 73.5 ms                                                               | 76.0 ms: 1.03x slower                                            |
| nqueens                  | 117 ms                                                                | 122 ms: 1.04x slower                                             |
| pprint_safe_repr         | 1.15 sec                                                              | 1.20 sec: 1.05x slower                                           |
| pprint_pformat           | 2.36 sec                                                              | 2.50 sec: 1.06x slower                                           |
| sqlglot_optimize         | 75.4 ms                                                               | 80.2 ms: 1.06x slower                                            |
| pickle_dict              | 35.1 us                                                               | 38.1 us: 1.08x slower                                            |
| sympy_integrate          | 26.5 ms                                                               | 28.8 ms: 1.09x slower                                            |
| sympy_expand             | 543 ms                                                                | 591 ms: 1.09x slower                                             |
| sympy_str                | 329 ms                                                                | 358 ms: 1.09x slower                                             |
| pickle                   | 12.5 us                                                               | 13.6 us: 1.09x slower                                            |
| unpickle                 | 17.5 us                                                               | 19.2 us: 1.10x slower                                            |
| async_generators         | 452 ms                                                                | 507 ms: 1.12x slower                                             |
| regex_effbot             | 4.25 ms                                                               | 4.90 ms: 1.15x slower                                            |
| telco                    | 8.49 ms                                                               | 9.86 ms: 1.16x slower                                            |
| sympy_sum                | 184 ms                                                                | 214 ms: 1.16x slower                                             |
| python_startup           | 11.2 ms                                                               | 13.1 ms: 1.17x slower                                            |
| coverage                 | 83.6 ms                                                               | 99.2 ms: 1.19x slower                                            |
| genshi_xml               | 69.8 ms                                                               | 83.0 ms: 1.19x slower                                            |
| gc_traversal             | 4.15 ms                                                               | 5.21 ms: 1.25x slower                                            |
| python_startup_no_site   | 6.89 ms                                                               | 8.81 ms: 1.28x slower                                            |
| bench_mp_pool            | 14.5 ms                                                               | 1.89 sec: 130.32x slower                                         |
| Geometric mean           | (ref)                                                                 | 1.12x faster                                                     |

Benchmark hidden because not significant (4): pylint, genshi_text, pidigits, json_loads
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241007-3.14.0a0-aa18ec3-JIT/bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence

- Geometric mean (including insignificant results): 1.188x faster
# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.03x

# Memory
- memory change: 1.24x