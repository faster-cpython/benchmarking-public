# Results vs. 3.10.4

- fork: python
- ref: e418fc3a6e7bade68ab5
- machine: linux-aarch64
- commit hash: e418fc3
- commit date: 2024-05-25
- overall geometric mean: 1.29x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 306 ms: 1.25x faster                                                    |
| chameleon      | 10.8 ms                                                               | 9.16 ms: 1.18x faster                                                   |
| docutils       | 3.53 sec                                                              | 3.09 sec: 1.14x faster                                                  |
| html5lib       | 86.5 ms                                                               | 65.8 ms: 1.31x faster                                                   |
| tornado_http   | 178 ms                                                                | 130 ms: 1.37x faster                                                    |
| Geometric mean | (ref)                                                                 | 1.25x faster                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 490 ms: 1.94x faster                                                    |
| async_tree_io           | 2.28 sec                                                              | 1.20 sec: 1.90x faster                                                  |
| async_tree_memoization  | 1.13 sec                                                              | 647 ms: 1.75x faster                                                    |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 784 ms: 1.62x faster                                                    |
| Geometric mean          | (ref)                                                                 | 1.80x faster                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 113 ms: 1.47x faster                                                    |
| float          | 135 ms                                                                | 91.9 ms: 1.47x faster                                                   |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 129 ms: 1.36x faster                                                    |
| regex_v8       | 32.2 ms                                                               | 30.9 ms: 1.04x faster                                                   |
| regex_dna      | 257 ms                                                                | 250 ms: 1.03x faster                                                    |
| regex_effbot   | 4.25 ms                                                               | 4.89 ms: 1.15x slower                                                   |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|----------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| pickle_pure_python   | 529 us                                                                | 361 us: 1.47x faster                                                    |
| unpickle_pure_python | 366 us                                                                | 252 us: 1.45x faster                                                    |
| tomli_loads          | 3.36 sec                                                              | 2.53 sec: 1.33x faster                                                  |
| json_dumps           | 16.7 ms                                                               | 13.3 ms: 1.26x faster                                                   |
| xml_etree_process    | 99.5 ms                                                               | 81.2 ms: 1.23x faster                                                   |
| xml_etree_parse      | 212 ms                                                                | 190 ms: 1.11x faster                                                    |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.09x faster                                                    |
| unpickle_list        | 6.99 us                                                               | 6.59 us: 1.06x faster                                                   |
| json_loads           | 30.9 us                                                               | 32.2 us: 1.04x slower                                                   |
| pickle_dict          | 35.1 us                                                               | 37.3 us: 1.06x slower                                                   |
| pickle               | 12.5 us                                                               | 13.6 us: 1.09x slower                                                   |
| unpickle             | 17.5 us                                                               | 19.5 us: 1.12x slower                                                   |
| Geometric mean       | (ref)                                                                 | 1.11x faster                                                            |

Benchmark hidden because not significant (2): xml_etree_iterparse, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 12.6 ms: 1.13x slower                                                   |
| python_startup_no_site | 6.89 ms                                                               | 8.41 ms: 1.22x slower                                                   |
| Geometric mean         | (ref)                                                                 | 1.17x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.2 ms: 1.43x faster                                                   |
| django_template | 53.3 ms                                                               | 41.6 ms: 1.28x faster                                                   |
| genshi_text     | 35.2 ms                                                               | 27.9 ms: 1.26x faster                                                   |
| genshi_xml      | 69.8 ms                                                               | 60.8 ms: 1.15x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.28x faster                                                            |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 200 us: 3.31x faster                                                    |
| deltablue                | 8.94 ms                                                               | 3.90 ms: 2.30x faster                                                   |
| bench_mp_pool            | 14.5 ms                                                               | 7.02 ms: 2.07x faster                                                   |
| async_tree_none          | 950 ms                                                                | 490 ms: 1.94x faster                                                    |
| raytrace                 | 573 ms                                                                | 297 ms: 1.93x faster                                                    |
| async_tree_io            | 2.28 sec                                                              | 1.20 sec: 1.90x faster                                                  |
| generators               | 68.1 ms                                                               | 37.6 ms: 1.81x faster                                                   |
| chaos                    | 121 ms                                                                | 67.9 ms: 1.78x faster                                                   |
| richards_super           | 107 ms                                                                | 60.4 ms: 1.78x faster                                                   |
| async_tree_memoization   | 1.13 sec                                                              | 647 ms: 1.75x faster                                                    |
| sqlglot_parse            | 2.40 ms                                                               | 1.40 ms: 1.71x faster                                                   |
| richards                 | 91.7 ms                                                               | 53.7 ms: 1.71x faster                                                   |
| scimark_lu               | 227 ms                                                                | 137 ms: 1.65x faster                                                    |
| logging_silent           | 222 ns                                                                | 134 ns: 1.65x faster                                                    |
| go                       | 264 ms                                                                | 160 ms: 1.65x faster                                                    |
| asyncio_tcp              | 944 ms                                                                | 573 ms: 1.65x faster                                                    |
| sqlglot_transpile        | 2.84 ms                                                               | 1.73 ms: 1.65x faster                                                   |
| crypto_pyaes             | 134 ms                                                                | 82.0 ms: 1.63x faster                                                   |
| comprehensions           | 33.1 us                                                               | 20.4 us: 1.63x faster                                                   |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 784 ms: 1.62x faster                                                    |
| scimark_monte_carlo      | 128 ms                                                                | 81.1 ms: 1.58x faster                                                   |
| scimark_sor              | 246 ms                                                                | 159 ms: 1.55x faster                                                    |
| hexiom                   | 10.9 ms                                                               | 7.07 ms: 1.54x faster                                                   |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.21 sec: 1.49x faster                                                  |
| nbody                    | 166 ms                                                                | 113 ms: 1.47x faster                                                    |
| pickle_pure_python       | 529 us                                                                | 361 us: 1.47x faster                                                    |
| float                    | 135 ms                                                                | 91.9 ms: 1.47x faster                                                   |
| unpickle_pure_python     | 366 us                                                                | 252 us: 1.45x faster                                                    |
| mako                     | 18.9 ms                                                               | 13.2 ms: 1.43x faster                                                   |
| pyflate                  | 795 ms                                                                | 557 ms: 1.43x faster                                                    |
| pylint                   | 485 ms                                                                | 342 ms: 1.42x faster                                                    |
| pycparser                | 1.69 sec                                                              | 1.23 sec: 1.38x faster                                                  |
| logging_simple           | 9.78 us                                                               | 7.11 us: 1.37x faster                                                   |
| tornado_http             | 178 ms                                                                | 130 ms: 1.37x faster                                                    |
| regex_compile            | 177 ms                                                                | 129 ms: 1.36x faster                                                    |
| logging_format           | 10.6 us                                                               | 7.78 us: 1.36x faster                                                   |
| tomli_loads              | 3.36 sec                                                              | 2.53 sec: 1.33x faster                                                  |
| spectral_norm            | 186 ms                                                                | 141 ms: 1.33x faster                                                    |
| html5lib                 | 86.5 ms                                                               | 65.8 ms: 1.31x faster                                                   |
| thrift                   | 1.26 ms                                                               | 967 us: 1.30x faster                                                    |
| coroutines               | 37.2 ms                                                               | 29.0 ms: 1.28x faster                                                   |
| django_template          | 53.3 ms                                                               | 41.6 ms: 1.28x faster                                                   |
| sympy_sum                | 184 ms                                                                | 144 ms: 1.27x faster                                                    |
| genshi_text              | 35.2 ms                                                               | 27.9 ms: 1.26x faster                                                   |
| json_dumps               | 16.7 ms                                                               | 13.3 ms: 1.26x faster                                                   |
| bench_thread_pool        | 1.59 ms                                                               | 1.27 ms: 1.26x faster                                                   |
| sympy_integrate          | 26.5 ms                                                               | 21.3 ms: 1.25x faster                                                   |
| 2to3                     | 381 ms                                                                | 306 ms: 1.25x faster                                                    |
| dulwich_log              | 73.5 ms                                                               | 59.4 ms: 1.24x faster                                                   |
| pprint_pformat           | 2.36 sec                                                              | 1.91 sec: 1.24x faster                                                  |
| pprint_safe_repr         | 1.15 sec                                                              | 930 ms: 1.23x faster                                                    |
| pathlib                  | 26.3 ms                                                               | 21.4 ms: 1.23x faster                                                   |
| deepcopy_memo            | 61.7 us                                                               | 50.1 us: 1.23x faster                                                   |
| sympy_str                | 329 ms                                                                | 268 ms: 1.23x faster                                                    |
| xml_etree_process        | 99.5 ms                                                               | 81.2 ms: 1.23x faster                                                   |
| sqlglot_normalize        | 156 ms                                                                | 128 ms: 1.22x faster                                                    |
| dask                     | 450 ms                                                                | 368 ms: 1.22x faster                                                    |
| sqlglot_optimize         | 75.4 ms                                                               | 62.1 ms: 1.21x faster                                                   |
| nqueens                  | 117 ms                                                                | 98.0 ms: 1.20x faster                                                   |
| fannkuch                 | 546 ms                                                                | 460 ms: 1.19x faster                                                    |
| chameleon                | 10.8 ms                                                               | 9.16 ms: 1.18x faster                                                   |
| sympy_expand             | 543 ms                                                                | 461 ms: 1.18x faster                                                    |
| genshi_xml               | 69.8 ms                                                               | 60.8 ms: 1.15x faster                                                   |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.65 ms: 1.15x faster                                                   |
| deepcopy                 | 511 us                                                                | 445 us: 1.15x faster                                                    |
| deepcopy_reduce          | 4.60 us                                                               | 4.02 us: 1.14x faster                                                   |
| docutils                 | 3.53 sec                                                              | 3.09 sec: 1.14x faster                                                  |
| meteor_contest           | 126 ms                                                                | 112 ms: 1.12x faster                                                    |
| scimark_fft              | 500 ms                                                                | 446 ms: 1.12x faster                                                    |
| mdp                      | 3.70 sec                                                              | 3.32 sec: 1.11x faster                                                  |
| xml_etree_parse          | 212 ms                                                                | 190 ms: 1.11x faster                                                    |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.09x faster                                                    |
| sqlite_synth             | 4.12 us                                                               | 3.84 us: 1.07x faster                                                   |
| unpickle_list            | 6.99 us                                                               | 6.59 us: 1.06x faster                                                   |
| regex_v8                 | 32.2 ms                                                               | 30.9 ms: 1.04x faster                                                   |
| json                     | 5.88 ms                                                               | 5.68 ms: 1.04x faster                                                   |
| regex_dna                | 257 ms                                                                | 250 ms: 1.03x faster                                                    |
| flaskblogging            | 4.83 ms                                                               | 4.74 ms: 1.02x faster                                                   |
| asyncio_websockets       | 657 ms                                                                | 666 ms: 1.01x slower                                                    |
| json_loads               | 30.9 us                                                               | 32.2 us: 1.04x slower                                                   |
| create_gc_cycles         | 2.26 ms                                                               | 2.39 ms: 1.06x slower                                                   |
| pickle_dict              | 35.1 us                                                               | 37.3 us: 1.06x slower                                                   |
| async_generators         | 452 ms                                                                | 483 ms: 1.07x slower                                                    |
| pickle                   | 12.5 us                                                               | 13.6 us: 1.09x slower                                                   |
| unpickle                 | 17.5 us                                                               | 19.5 us: 1.12x slower                                                   |
| python_startup           | 11.2 ms                                                               | 12.6 ms: 1.13x slower                                                   |
| regex_effbot             | 4.25 ms                                                               | 4.89 ms: 1.15x slower                                                   |
| telco                    | 8.49 ms                                                               | 9.85 ms: 1.16x slower                                                   |
| coverage                 | 83.6 ms                                                               | 97.9 ms: 1.17x slower                                                   |
| python_startup_no_site   | 6.89 ms                                                               | 8.41 ms: 1.22x slower                                                   |
| gc_traversal             | 4.15 ms                                                               | 5.22 ms: 1.26x slower                                                   |
| Geometric mean           | (ref)                                                                 | 1.29x faster                                                            |

Benchmark hidden because not significant (3): xml_etree_iterparse, pidigits, pickle_list
Ignored benchmarks (5) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (4) of results/bm-20240525-3.14.0a0-e418fc3/bm-20240525-arminc-aarch64-python-e418fc3a6e7bade68ab5-3.14.0a0-e418fc3.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.24x
- 95% likely to have a speedup of 1.23x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.13x