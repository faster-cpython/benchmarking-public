# Results vs. 3.10.4

- fork: brandtbucher
- ref: nojit
- machine: linux-aarch64
- commit hash: a6f1035
- commit date: 2024-09-21
- overall geometric mean: 1.329x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 297 ms: 1.28x faster                                           |
| docutils       | 3.53 sec                                                              | 3.01 sec: 1.17x faster                                         |
| html5lib       | 86.5 ms                                                               | 64.5 ms: 1.34x faster                                          |
| tornado_http   | 178 ms                                                                | 126 ms: 1.41x faster                                           |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|-------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 417 ms: 2.28x faster                                           |
| async_tree_memoization  | 1.13 sec                                                              | 553 ms: 2.05x faster                                           |
| async_tree_io           | 2.28 sec                                                              | 1.15 sec: 1.99x faster                                         |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 736 ms: 1.73x faster                                           |
| Geometric mean          | (ref)                                                                 | 2.00x faster                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 111 ms: 1.50x faster                                           |
| float          | 135 ms                                                                | 94.9 ms: 1.42x faster                                          |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 127 ms: 1.39x faster                                           |
| regex_v8       | 32.2 ms                                                               | 30.4 ms: 1.06x faster                                          |
| regex_dna      | 257 ms                                                                | 251 ms: 1.03x faster                                           |
| regex_effbot   | 4.25 ms                                                               | 4.92 ms: 1.16x slower                                          |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 360 us: 1.47x faster                                           |
| unpickle_pure_python | 366 us                                                                | 254 us: 1.44x faster                                           |
| tomli_loads          | 3.36 sec                                                              | 2.66 sec: 1.26x faster                                         |
| json_dumps           | 16.7 ms                                                               | 13.3 ms: 1.25x faster                                          |
| xml_etree_process    | 99.5 ms                                                               | 79.8 ms: 1.25x faster                                          |
| xml_etree_parse      | 212 ms                                                                | 187 ms: 1.13x faster                                           |
| xml_etree_generate   | 123 ms                                                                | 112 ms: 1.10x faster                                           |
| unpickle_list        | 6.99 us                                                               | 6.42 us: 1.09x faster                                          |
| xml_etree_iterparse  | 156 ms                                                                | 149 ms: 1.05x faster                                           |
| json_loads           | 30.9 us                                                               | 31.8 us: 1.03x slower                                          |
| pickle_dict          | 35.1 us                                                               | 37.7 us: 1.07x slower                                          |
| pickle               | 12.5 us                                                               | 13.6 us: 1.09x slower                                          |
| unpickle             | 17.5 us                                                               | 19.4 us: 1.11x slower                                          |
| Geometric mean       | (ref)                                                                 | 1.11x faster                                                   |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.1 ms: 1.17x slower                                          |
| python_startup_no_site | 6.89 ms                                                               | 8.69 ms: 1.26x slower                                          |
| Geometric mean         | (ref)                                                                 | 1.21x slower                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|-----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.3 ms: 1.42x faster                                          |
| genshi_text     | 35.2 ms                                                               | 27.5 ms: 1.28x faster                                          |
| django_template | 53.3 ms                                                               | 41.9 ms: 1.27x faster                                          |
| genshi_xml      | 69.8 ms                                                               | 61.9 ms: 1.13x faster                                          |
| Geometric mean  | (ref)                                                                 | 1.27x faster                                                   |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035 |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 192 us: 3.44x faster                                           |
| async_tree_none          | 950 ms                                                                | 417 ms: 2.28x faster                                           |
| deltablue                | 8.94 ms                                                               | 3.94 ms: 2.27x faster                                          |
| async_tree_memoization   | 1.13 sec                                                              | 553 ms: 2.05x faster                                           |
| bench_mp_pool            | 14.5 ms                                                               | 7.12 ms: 2.04x faster                                          |
| async_tree_io            | 2.28 sec                                                              | 1.15 sec: 1.99x faster                                         |
| generators               | 68.1 ms                                                               | 35.4 ms: 1.92x faster                                          |
| go                       | 264 ms                                                                | 138 ms: 1.92x faster                                           |
| raytrace                 | 573 ms                                                                | 302 ms: 1.90x faster                                           |
| richards_super           | 107 ms                                                                | 59.4 ms: 1.81x faster                                          |
| chaos                    | 121 ms                                                                | 69.2 ms: 1.75x faster                                          |
| richards                 | 91.7 ms                                                               | 52.8 ms: 1.74x faster                                          |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 736 ms: 1.73x faster                                           |
| sqlglot_parse            | 2.40 ms                                                               | 1.41 ms: 1.70x faster                                          |
| asyncio_tcp              | 944 ms                                                                | 560 ms: 1.69x faster                                           |
| scimark_lu               | 227 ms                                                                | 135 ms: 1.68x faster                                           |
| logging_silent           | 222 ns                                                                | 133 ns: 1.67x faster                                           |
| sqlglot_transpile        | 2.84 ms                                                               | 1.73 ms: 1.64x faster                                          |
| crypto_pyaes             | 134 ms                                                                | 82.4 ms: 1.63x faster                                          |
| comprehensions           | 33.1 us                                                               | 20.6 us: 1.61x faster                                          |
| scimark_sor              | 246 ms                                                                | 156 ms: 1.58x faster                                           |
| deepcopy_memo            | 61.7 us                                                               | 39.2 us: 1.57x faster                                          |
| scimark_monte_carlo      | 128 ms                                                                | 82.0 ms: 1.56x faster                                          |
| deepcopy                 | 511 us                                                                | 335 us: 1.52x faster                                           |
| hexiom                   | 10.9 ms                                                               | 7.18 ms: 1.52x faster                                          |
| nbody                    | 166 ms                                                                | 111 ms: 1.50x faster                                           |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.21 sec: 1.49x faster                                         |
| pickle_pure_python       | 529 us                                                                | 360 us: 1.47x faster                                           |
| unpickle_pure_python     | 366 us                                                                | 254 us: 1.44x faster                                           |
| float                    | 135 ms                                                                | 94.9 ms: 1.42x faster                                          |
| mako                     | 18.9 ms                                                               | 13.3 ms: 1.42x faster                                          |
| pyflate                  | 795 ms                                                                | 563 ms: 1.41x faster                                           |
| tornado_http             | 178 ms                                                                | 126 ms: 1.41x faster                                           |
| regex_compile            | 177 ms                                                                | 127 ms: 1.39x faster                                           |
| logging_simple           | 9.78 us                                                               | 7.11 us: 1.38x faster                                          |
| logging_format           | 10.6 us                                                               | 7.71 us: 1.38x faster                                          |
| pycparser                | 1.69 sec                                                              | 1.24 sec: 1.37x faster                                         |
| thrift                   | 1.26 ms                                                               | 926 us: 1.36x faster                                           |
| html5lib                 | 86.5 ms                                                               | 64.5 ms: 1.34x faster                                          |
| pylint                   | 485 ms                                                                | 362 ms: 1.34x faster                                           |
| spectral_norm            | 186 ms                                                                | 142 ms: 1.31x faster                                           |
| coroutines               | 37.2 ms                                                               | 28.8 ms: 1.29x faster                                          |
| sympy_sum                | 184 ms                                                                | 143 ms: 1.29x faster                                           |
| deepcopy_reduce          | 4.60 us                                                               | 3.58 us: 1.29x faster                                          |
| 2to3                     | 381 ms                                                                | 297 ms: 1.28x faster                                           |
| genshi_text              | 35.2 ms                                                               | 27.5 ms: 1.28x faster                                          |
| django_template          | 53.3 ms                                                               | 41.9 ms: 1.27x faster                                          |
| sympy_integrate          | 26.5 ms                                                               | 21.0 ms: 1.26x faster                                          |
| tomli_loads              | 3.36 sec                                                              | 2.66 sec: 1.26x faster                                         |
| pprint_safe_repr         | 1.15 sec                                                              | 911 ms: 1.26x faster                                           |
| bench_thread_pool        | 1.59 ms                                                               | 1.26 ms: 1.26x faster                                          |
| pprint_pformat           | 2.36 sec                                                              | 1.88 sec: 1.25x faster                                         |
| json_dumps               | 16.7 ms                                                               | 13.3 ms: 1.25x faster                                          |
| xml_etree_process        | 99.5 ms                                                               | 79.8 ms: 1.25x faster                                          |
| dulwich_log              | 73.5 ms                                                               | 59.1 ms: 1.24x faster                                          |
| sqlglot_normalize        | 156 ms                                                                | 126 ms: 1.24x faster                                           |
| pathlib                  | 26.3 ms                                                               | 21.4 ms: 1.23x faster                                          |
| sympy_str                | 329 ms                                                                | 267 ms: 1.23x faster                                           |
| sqlglot_optimize         | 75.4 ms                                                               | 62.3 ms: 1.21x faster                                          |
| nqueens                  | 117 ms                                                                | 99.3 ms: 1.18x faster                                          |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.45 ms: 1.18x faster                                          |
| sympy_expand             | 543 ms                                                                | 460 ms: 1.18x faster                                           |
| fannkuch                 | 546 ms                                                                | 465 ms: 1.17x faster                                           |
| docutils                 | 3.53 sec                                                              | 3.01 sec: 1.17x faster                                         |
| xml_etree_parse          | 212 ms                                                                | 187 ms: 1.13x faster                                           |
| genshi_xml               | 69.8 ms                                                               | 61.9 ms: 1.13x faster                                          |
| scimark_fft              | 500 ms                                                                | 444 ms: 1.13x faster                                           |
| meteor_contest           | 126 ms                                                                | 114 ms: 1.11x faster                                           |
| mdp                      | 3.70 sec                                                              | 3.35 sec: 1.10x faster                                         |
| xml_etree_generate       | 123 ms                                                                | 112 ms: 1.10x faster                                           |
| unpickle_list            | 6.99 us                                                               | 6.42 us: 1.09x faster                                          |
| sqlite_synth             | 4.12 us                                                               | 3.88 us: 1.06x faster                                          |
| regex_v8                 | 32.2 ms                                                               | 30.4 ms: 1.06x faster                                          |
| xml_etree_iterparse      | 156 ms                                                                | 149 ms: 1.05x faster                                           |
| json                     | 5.88 ms                                                               | 5.68 ms: 1.03x faster                                          |
| regex_dna                | 257 ms                                                                | 251 ms: 1.03x faster                                           |
| create_gc_cycles         | 2.26 ms                                                               | 2.29 ms: 1.01x slower                                          |
| json_loads               | 30.9 us                                                               | 31.8 us: 1.03x slower                                          |
| async_generators         | 452 ms                                                                | 480 ms: 1.06x slower                                           |
| pickle_dict              | 35.1 us                                                               | 37.7 us: 1.07x slower                                          |
| pickle                   | 12.5 us                                                               | 13.6 us: 1.09x slower                                          |
| unpickle                 | 17.5 us                                                               | 19.4 us: 1.11x slower                                          |
| regex_effbot             | 4.25 ms                                                               | 4.92 ms: 1.16x slower                                          |
| python_startup           | 11.2 ms                                                               | 13.1 ms: 1.17x slower                                          |
| coverage                 | 83.6 ms                                                               | 97.9 ms: 1.17x slower                                          |
| gc_traversal             | 4.15 ms                                                               | 5.04 ms: 1.21x slower                                          |
| telco                    | 8.49 ms                                                               | 10.3 ms: 1.22x slower                                          |
| python_startup_no_site   | 6.89 ms                                                               | 8.69 ms: 1.26x slower                                          |
| Geometric mean           | (ref)                                                                 | 1.31x faster                                                   |

Benchmark hidden because not significant (3): pickle_list, pidigits, asyncio_websockets
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240921-3.14.0a0-a6f1035/bm-20240921-arminc-aarch64-brandtbucher-nojit-3.14.0a0-a6f1035.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence

- Geometric mean (including insignificant results): 1.329x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.15x