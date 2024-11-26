# Results vs. 3.10.4

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: linux-aarch64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.334x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.23x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 294 ms: 1.30x faster                                                    |
| docutils       | 3.53 sec                                                              | 3.01 sec: 1.17x faster                                                  |
| html5lib       | 86.5 ms                                                               | 64.8 ms: 1.34x faster                                                   |
| tornado_http   | 178 ms                                                                | 129 ms: 1.39x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 424 ms: 2.24x faster                                                    |
| async_tree_memoization  | 1.13 sec                                                              | 555 ms: 2.04x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.15 sec: 1.98x faster                                                  |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 728 ms: 1.75x faster                                                    |
| Geometric mean          | (ref)                                                                 | 2.00x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 110 ms: 1.50x faster                                                    |
| float          | 135 ms                                                                | 93.0 ms: 1.45x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 126 ms: 1.40x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 30.7 ms: 1.05x faster                                                   |
| regex_dna      | 257 ms                                                                | 259 ms: 1.01x slower                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.99 ms: 1.18x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 362 us: 1.46x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 254 us: 1.44x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.63 sec: 1.28x faster                                                  |
| json_dumps           | 16.7 ms                                                               | 13.2 ms: 1.26x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 80.1 ms: 1.24x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 186 ms: 1.14x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 112 ms: 1.09x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 6.59 us: 1.06x faster                                                   |
| xml_etree_iterparse  | 156 ms                                                                | 148 ms: 1.05x faster                                                    |
| pickle_list          | 5.24 us                                                               | 5.27 us: 1.01x slower                                                   |
| json_loads           | 30.9 us                                                               | 31.2 us: 1.01x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 37.4 us: 1.06x slower                                                   |
| pickle               | 12.5 us                                                               | 13.7 us: 1.10x slower                                                   |
| unpickle             | 17.5 us                                                               | 19.5 us: 1.11x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.11x faster                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 12.9 ms: 1.15x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.61 ms: 1.25x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.20x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.8 ms: 1.37x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 27.5 ms: 1.28x faster                                                   |
| django_template | 53.3 ms                                                               | 42.2 ms: 1.26x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 60.6 ms: 1.15x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.26x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 193 us: 3.42x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.92 ms: 2.28x faster                                                   |
| async_tree_none          | 950 ms                                                                | 424 ms: 2.24x faster                                                    |
| async_tree_memoization   | 1.13 sec                                                              | 555 ms: 2.04x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.15 sec: 1.98x faster                                                  |
| generators               | 68.1 ms                                                               | 34.7 ms: 1.96x faster                                                   |
| go                       | 264 ms                                                                | 138 ms: 1.91x faster                                                    |
| raytrace                 | 573 ms                                                                | 305 ms: 1.88x faster                                                    |
| richards_super           | 107 ms                                                                | 59.3 ms: 1.81x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 728 ms: 1.75x faster                                                    |
| chaos                    | 121 ms                                                                | 69.4 ms: 1.74x faster                                                   |
| richards                 | 91.7 ms                                                               | 53.0 ms: 1.73x faster                                                   |
| logging_silent           | 222 ns                                                                | 130 ns: 1.71x faster                                                    |
| scimark_lu               | 227 ms                                                                | 133 ms: 1.70x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 559 ms: 1.69x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.43 ms: 1.68x faster                                                   |
| sqlglot_transpile        | 2.84 ms                                                               | 1.73 ms: 1.64x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 82.0 ms: 1.64x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 38.1 us: 1.62x faster                                                   |
| comprehensions           | 33.1 us                                                               | 20.6 us: 1.61x faster                                                   |
| scimark_sor              | 246 ms                                                                | 157 ms: 1.56x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 82.8 ms: 1.54x faster                                                   |
| hexiom                   | 10.9 ms                                                               | 7.11 ms: 1.53x faster                                                   |
| deepcopy                 | 511 us                                                                | 335 us: 1.52x faster                                                    |
| nbody                    | 166 ms                                                                | 110 ms: 1.50x faster                                                    |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.20 sec: 1.50x faster                                                  |
| pickle_pure_python       | 529 us                                                                | 362 us: 1.46x faster                                                    |
| float                    | 135 ms                                                                | 93.0 ms: 1.45x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 254 us: 1.44x faster                                                    |
| regex_compile            | 177 ms                                                                | 126 ms: 1.40x faster                                                    |
| tornado_http             | 178 ms                                                                | 129 ms: 1.39x faster                                                    |
| logging_simple           | 9.78 us                                                               | 7.11 us: 1.37x faster                                                   |
| pycparser                | 1.69 sec                                                              | 1.23 sec: 1.37x faster                                                  |
| logging_format           | 10.6 us                                                               | 7.72 us: 1.37x faster                                                   |
| pyflate                  | 795 ms                                                                | 579 ms: 1.37x faster                                                    |
| pylint                   | 485 ms                                                                | 354 ms: 1.37x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.8 ms: 1.37x faster                                                   |
| thrift                   | 1.26 ms                                                               | 920 us: 1.37x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 64.8 ms: 1.34x faster                                                   |
| sympy_sum                | 184 ms                                                                | 140 ms: 1.32x faster                                                    |
| spectral_norm            | 186 ms                                                                | 142 ms: 1.31x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 3.52 us: 1.30x faster                                                   |
| coroutines               | 37.2 ms                                                               | 28.5 ms: 1.30x faster                                                   |
| 2to3                     | 381 ms                                                                | 294 ms: 1.30x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 27.5 ms: 1.28x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.63 sec: 1.28x faster                                                  |
| sympy_integrate          | 26.5 ms                                                               | 20.9 ms: 1.27x faster                                                   |
| pprint_safe_repr         | 1.15 sec                                                              | 907 ms: 1.26x faster                                                    |
| django_template          | 53.3 ms                                                               | 42.2 ms: 1.26x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 13.2 ms: 1.26x faster                                                   |
| dulwich_log              | 73.5 ms                                                               | 58.6 ms: 1.25x faster                                                   |
| pprint_pformat           | 2.36 sec                                                              | 1.89 sec: 1.25x faster                                                  |
| sympy_str                | 329 ms                                                                | 263 ms: 1.25x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 21.2 ms: 1.24x faster                                                   |
| xml_etree_process        | 99.5 ms                                                               | 80.1 ms: 1.24x faster                                                   |
| sqlglot_normalize        | 156 ms                                                                | 127 ms: 1.23x faster                                                    |
| bench_thread_pool        | 1.59 ms                                                               | 1.30 ms: 1.23x faster                                                   |
| nqueens                  | 117 ms                                                                | 98.0 ms: 1.20x faster                                                   |
| sqlglot_optimize         | 75.4 ms                                                               | 62.9 ms: 1.20x faster                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.37 ms: 1.20x faster                                                   |
| sympy_expand             | 543 ms                                                                | 457 ms: 1.19x faster                                                    |
| docutils                 | 3.53 sec                                                              | 3.01 sec: 1.17x faster                                                  |
| scimark_fft              | 500 ms                                                                | 427 ms: 1.17x faster                                                    |
| fannkuch                 | 546 ms                                                                | 468 ms: 1.17x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 60.6 ms: 1.15x faster                                                   |
| xml_etree_parse          | 212 ms                                                                | 186 ms: 1.14x faster                                                    |
| meteor_contest           | 126 ms                                                                | 112 ms: 1.12x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.33 sec: 1.11x faster                                                  |
| xml_etree_generate       | 123 ms                                                                | 112 ms: 1.09x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.81 us: 1.08x faster                                                   |
| json                     | 5.88 ms                                                               | 5.53 ms: 1.06x faster                                                   |
| unpickle_list            | 6.99 us                                                               | 6.59 us: 1.06x faster                                                   |
| xml_etree_iterparse      | 156 ms                                                                | 148 ms: 1.05x faster                                                    |
| regex_v8                 | 32.2 ms                                                               | 30.7 ms: 1.05x faster                                                   |
| pickle_list              | 5.24 us                                                               | 5.27 us: 1.01x slower                                                   |
| regex_dna                | 257 ms                                                                | 259 ms: 1.01x slower                                                    |
| json_loads               | 30.9 us                                                               | 31.2 us: 1.01x slower                                                   |
| async_generators         | 452 ms                                                                | 476 ms: 1.05x slower                                                    |
| pickle_dict              | 35.1 us                                                               | 37.4 us: 1.06x slower                                                   |
| pickle                   | 12.5 us                                                               | 13.7 us: 1.10x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.45 ms: 1.11x slower                                                   |
| unpickle                 | 17.5 us                                                               | 19.5 us: 1.11x slower                                                   |
| python_startup           | 11.2 ms                                                               | 12.9 ms: 1.15x slower                                                   |
| regex_effbot             | 4.25 ms                                                               | 4.99 ms: 1.18x slower                                                   |
| coverage                 | 83.6 ms                                                               | 99.3 ms: 1.19x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 5.02 ms: 1.21x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.61 ms: 1.25x slower                                                   |
| bench_mp_pool            | 14.5 ms                                                               | 4.42 sec: 304.43x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.23x faster                                                            |

Benchmark hidden because not significant (3): pidigits, asyncio_websockets, create_gc_cycles
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20241005-3.14.0a0-16cd6cc/bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence

- Geometric mean (including insignificant results): 1.334x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.26x
- 95% likely to have a speedup of 1.25x
- 99% likely to have a speedup of 1.23x

# Memory
- memory change: 1.14x