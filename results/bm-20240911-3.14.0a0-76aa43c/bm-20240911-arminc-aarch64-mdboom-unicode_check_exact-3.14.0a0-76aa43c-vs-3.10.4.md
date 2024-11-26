# Results vs. 3.10.4

- fork: mdboom
- ref: unicode_check_exact
- machine: linux-aarch64
- commit hash: 76aa43c
- commit date: 2024-09-11
- overall geometric mean: 1.341x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 298 ms: 1.28x faster                                                   |
| docutils       | 3.53 sec                                                              | 3.00 sec: 1.18x faster                                                 |
| html5lib       | 86.5 ms                                                               | 64.1 ms: 1.35x faster                                                  |
| tornado_http   | 178 ms                                                                | 127 ms: 1.41x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|-------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 424 ms: 2.24x faster                                                   |
| async_tree_memoization  | 1.13 sec                                                              | 555 ms: 2.04x faster                                                   |
| async_tree_io           | 2.28 sec                                                              | 1.15 sec: 1.99x faster                                                 |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 727 ms: 1.75x faster                                                   |
| Geometric mean          | (ref)                                                                 | 2.00x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 109 ms: 1.52x faster                                                   |
| float          | 135 ms                                                                | 92.1 ms: 1.46x faster                                                  |
| Geometric mean | (ref)                                                                 | 1.31x faster                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 124 ms: 1.43x faster                                                   |
| regex_dna      | 257 ms                                                                | 246 ms: 1.05x faster                                                   |
| regex_v8       | 32.2 ms                                                               | 31.0 ms: 1.04x faster                                                  |
| regex_effbot   | 4.25 ms                                                               | 4.93 ms: 1.16x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.07x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 358 us: 1.48x faster                                                   |
| unpickle_pure_python | 366 us                                                                | 250 us: 1.46x faster                                                   |
| tomli_loads          | 3.36 sec                                                              | 2.61 sec: 1.28x faster                                                 |
| xml_etree_process    | 99.5 ms                                                               | 79.4 ms: 1.25x faster                                                  |
| json_dumps           | 16.7 ms                                                               | 13.5 ms: 1.24x faster                                                  |
| xml_etree_parse      | 212 ms                                                                | 187 ms: 1.13x faster                                                   |
| xml_etree_generate   | 123 ms                                                                | 111 ms: 1.11x faster                                                   |
| unpickle_list        | 6.99 us                                                               | 6.39 us: 1.09x faster                                                  |
| xml_etree_iterparse  | 156 ms                                                                | 148 ms: 1.05x faster                                                   |
| json_loads           | 30.9 us                                                               | 31.6 us: 1.02x slower                                                  |
| pickle_dict          | 35.1 us                                                               | 37.9 us: 1.08x slower                                                  |
| pickle               | 12.5 us                                                               | 13.7 us: 1.10x slower                                                  |
| unpickle             | 17.5 us                                                               | 19.4 us: 1.11x slower                                                  |
| Geometric mean       | (ref)                                                                 | 1.12x faster                                                           |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                                  |
| python_startup_no_site | 6.89 ms                                                               | 8.62 ms: 1.25x slower                                                  |
| Geometric mean         | (ref)                                                                 | 1.21x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.3 ms: 1.42x faster                                                  |
| genshi_text     | 35.2 ms                                                               | 27.3 ms: 1.29x faster                                                  |
| django_template | 53.3 ms                                                               | 42.7 ms: 1.25x faster                                                  |
| genshi_xml      | 69.8 ms                                                               | 59.4 ms: 1.18x faster                                                  |
| Geometric mean  | (ref)                                                                 | 1.28x faster                                                           |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c |
|--------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 191 us: 3.47x faster                                                   |
| deltablue                | 8.94 ms                                                               | 3.89 ms: 2.30x faster                                                  |
| async_tree_none          | 950 ms                                                                | 424 ms: 2.24x faster                                                   |
| bench_mp_pool            | 14.5 ms                                                               | 7.05 ms: 2.06x faster                                                  |
| async_tree_memoization   | 1.13 sec                                                              | 555 ms: 2.04x faster                                                   |
| async_tree_io            | 2.28 sec                                                              | 1.15 sec: 1.99x faster                                                 |
| generators               | 68.1 ms                                                               | 34.7 ms: 1.96x faster                                                  |
| go                       | 264 ms                                                                | 136 ms: 1.94x faster                                                   |
| raytrace                 | 573 ms                                                                | 302 ms: 1.90x faster                                                   |
| richards_super           | 107 ms                                                                | 59.4 ms: 1.81x faster                                                  |
| chaos                    | 121 ms                                                                | 68.5 ms: 1.77x faster                                                  |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 727 ms: 1.75x faster                                                   |
| richards                 | 91.7 ms                                                               | 52.8 ms: 1.74x faster                                                  |
| sqlglot_parse            | 2.40 ms                                                               | 1.42 ms: 1.70x faster                                                  |
| logging_silent           | 222 ns                                                                | 132 ns: 1.68x faster                                                   |
| scimark_lu               | 227 ms                                                                | 135 ms: 1.67x faster                                                   |
| asyncio_tcp              | 944 ms                                                                | 568 ms: 1.66x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 37.3 us: 1.65x faster                                                  |
| sqlglot_transpile        | 2.84 ms                                                               | 1.73 ms: 1.64x faster                                                  |
| crypto_pyaes             | 134 ms                                                                | 81.9 ms: 1.64x faster                                                  |
| comprehensions           | 33.1 us                                                               | 20.4 us: 1.62x faster                                                  |
| scimark_sor              | 246 ms                                                                | 155 ms: 1.59x faster                                                   |
| deepcopy                 | 511 us                                                                | 328 us: 1.56x faster                                                   |
| scimark_monte_carlo      | 128 ms                                                                | 82.4 ms: 1.55x faster                                                  |
| hexiom                   | 10.9 ms                                                               | 7.11 ms: 1.53x faster                                                  |
| nbody                    | 166 ms                                                                | 109 ms: 1.52x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.21 sec: 1.49x faster                                                 |
| pickle_pure_python       | 529 us                                                                | 358 us: 1.48x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 250 us: 1.46x faster                                                   |
| float                    | 135 ms                                                                | 92.1 ms: 1.46x faster                                                  |
| regex_compile            | 177 ms                                                                | 124 ms: 1.43x faster                                                   |
| pyflate                  | 795 ms                                                                | 559 ms: 1.42x faster                                                   |
| mako                     | 18.9 ms                                                               | 13.3 ms: 1.42x faster                                                  |
| logging_simple           | 9.78 us                                                               | 6.92 us: 1.41x faster                                                  |
| pycparser                | 1.69 sec                                                              | 1.20 sec: 1.41x faster                                                 |
| tornado_http             | 178 ms                                                                | 127 ms: 1.41x faster                                                   |
| logging_format           | 10.6 us                                                               | 7.62 us: 1.39x faster                                                  |
| thrift                   | 1.26 ms                                                               | 921 us: 1.37x faster                                                   |
| pylint                   | 485 ms                                                                | 359 ms: 1.35x faster                                                   |
| html5lib                 | 86.5 ms                                                               | 64.1 ms: 1.35x faster                                                  |
| sympy_sum                | 184 ms                                                                | 139 ms: 1.32x faster                                                   |
| deepcopy_reduce          | 4.60 us                                                               | 3.49 us: 1.32x faster                                                  |
| spectral_norm            | 186 ms                                                                | 142 ms: 1.32x faster                                                   |
| coroutines               | 37.2 ms                                                               | 28.3 ms: 1.31x faster                                                  |
| bench_thread_pool        | 1.59 ms                                                               | 1.22 ms: 1.30x faster                                                  |
| sympy_integrate          | 26.5 ms                                                               | 20.6 ms: 1.29x faster                                                  |
| genshi_text              | 35.2 ms                                                               | 27.3 ms: 1.29x faster                                                  |
| tomli_loads              | 3.36 sec                                                              | 2.61 sec: 1.28x faster                                                 |
| 2to3                     | 381 ms                                                                | 298 ms: 1.28x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 57.9 ms: 1.27x faster                                                  |
| pprint_safe_repr         | 1.15 sec                                                              | 904 ms: 1.27x faster                                                   |
| pprint_pformat           | 2.36 sec                                                              | 1.86 sec: 1.27x faster                                                 |
| sympy_str                | 329 ms                                                                | 261 ms: 1.26x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 79.4 ms: 1.25x faster                                                  |
| django_template          | 53.3 ms                                                               | 42.7 ms: 1.25x faster                                                  |
| pathlib                  | 26.3 ms                                                               | 21.2 ms: 1.24x faster                                                  |
| json_dumps               | 16.7 ms                                                               | 13.5 ms: 1.24x faster                                                  |
| sqlglot_normalize        | 156 ms                                                                | 127 ms: 1.23x faster                                                   |
| nqueens                  | 117 ms                                                                | 97.0 ms: 1.21x faster                                                  |
| sqlglot_optimize         | 75.4 ms                                                               | 62.4 ms: 1.21x faster                                                  |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.39 ms: 1.19x faster                                                  |
| fannkuch                 | 546 ms                                                                | 459 ms: 1.19x faster                                                   |
| sympy_expand             | 543 ms                                                                | 457 ms: 1.19x faster                                                   |
| genshi_xml               | 69.8 ms                                                               | 59.4 ms: 1.18x faster                                                  |
| docutils                 | 3.53 sec                                                              | 3.00 sec: 1.18x faster                                                 |
| scimark_fft              | 500 ms                                                                | 439 ms: 1.14x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 187 ms: 1.13x faster                                                   |
| meteor_contest           | 126 ms                                                                | 112 ms: 1.13x faster                                                   |
| mdp                      | 3.70 sec                                                              | 3.29 sec: 1.12x faster                                                 |
| xml_etree_generate       | 123 ms                                                                | 111 ms: 1.11x faster                                                   |
| unpickle_list            | 6.99 us                                                               | 6.39 us: 1.09x faster                                                  |
| sqlite_synth             | 4.12 us                                                               | 3.88 us: 1.06x faster                                                  |
| json                     | 5.88 ms                                                               | 5.54 ms: 1.06x faster                                                  |
| xml_etree_iterparse      | 156 ms                                                                | 148 ms: 1.05x faster                                                   |
| regex_dna                | 257 ms                                                                | 246 ms: 1.05x faster                                                   |
| regex_v8                 | 32.2 ms                                                               | 31.0 ms: 1.04x faster                                                  |
| json_loads               | 30.9 us                                                               | 31.6 us: 1.02x slower                                                  |
| async_generators         | 452 ms                                                                | 476 ms: 1.05x slower                                                   |
| pickle_dict              | 35.1 us                                                               | 37.9 us: 1.08x slower                                                  |
| pickle                   | 12.5 us                                                               | 13.7 us: 1.10x slower                                                  |
| unpickle                 | 17.5 us                                                               | 19.4 us: 1.11x slower                                                  |
| regex_effbot             | 4.25 ms                                                               | 4.93 ms: 1.16x slower                                                  |
| python_startup           | 11.2 ms                                                               | 13.0 ms: 1.16x slower                                                  |
| coverage                 | 83.6 ms                                                               | 97.7 ms: 1.17x slower                                                  |
| telco                    | 8.49 ms                                                               | 10.2 ms: 1.20x slower                                                  |
| gc_traversal             | 4.15 ms                                                               | 5.02 ms: 1.21x slower                                                  |
| python_startup_no_site   | 6.89 ms                                                               | 8.62 ms: 1.25x slower                                                  |
| Geometric mean           | (ref)                                                                 | 1.32x faster                                                           |

Benchmark hidden because not significant (4): pidigits, pickle_list, asyncio_websockets, create_gc_cycles
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240911-3.14.0a0-76aa43c/bm-20240911-arminc-aarch64-mdboom-unicode_check_exact-3.14.0a0-76aa43c.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence

- Geometric mean (including insignificant results): 1.341x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.14x