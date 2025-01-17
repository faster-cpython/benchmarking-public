# Results vs. 3.10.4

- fork: mdboom
- ref: pysequence_tuple
- machine: linux-aarch64
- commit hash: 3b5fdc8
- commit date: 2024-09-11
- overall geometric mean: 1.331x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.22x faster
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 297 ms: 1.28x faster                                                |
| docutils       | 3.53 sec                                                              | 3.03 sec: 1.16x faster                                              |
| html5lib       | 86.5 ms                                                               | 65.5 ms: 1.32x faster                                               |
| tornado_http   | 178 ms                                                                | 126 ms: 1.41x faster                                                |
| Geometric mean | (ref)                                                                 | 1.29x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_none         | 950 ms                                                                | 427 ms: 2.22x faster                                                |
| async_tree_memoization  | 1.13 sec                                                              | 562 ms: 2.02x faster                                                |
| async_tree_io           | 2.28 sec                                                              | 1.14 sec: 2.01x faster                                              |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 734 ms: 1.73x faster                                                |
| Geometric mean          | (ref)                                                                 | 1.99x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 166 ms                                                                | 109 ms: 1.53x faster                                                |
| float          | 135 ms                                                                | 94.2 ms: 1.43x faster                                               |
| Geometric mean | (ref)                                                                 | 1.30x faster                                                        |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 124 ms: 1.42x faster                                                |
| regex_v8       | 32.2 ms                                                               | 30.7 ms: 1.05x faster                                               |
| regex_dna      | 257 ms                                                                | 253 ms: 1.02x faster                                                |
| regex_effbot   | 4.25 ms                                                               | 5.01 ms: 1.18x slower                                               |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_pure_python | 366 us                                                                | 252 us: 1.45x faster                                                |
| pickle_pure_python   | 529 us                                                                | 368 us: 1.44x faster                                                |
| tomli_loads          | 3.36 sec                                                              | 2.61 sec: 1.29x faster                                              |
| json_dumps           | 16.7 ms                                                               | 13.3 ms: 1.26x faster                                               |
| xml_etree_process    | 99.5 ms                                                               | 79.1 ms: 1.26x faster                                               |
| xml_etree_parse      | 212 ms                                                                | 191 ms: 1.11x faster                                                |
| unpickle_list        | 6.99 us                                                               | 6.38 us: 1.10x faster                                               |
| xml_etree_generate   | 123 ms                                                                | 113 ms: 1.09x faster                                                |
| pickle_list          | 5.24 us                                                               | 5.19 us: 1.01x faster                                               |
| json_loads           | 30.9 us                                                               | 31.4 us: 1.02x slower                                               |
| pickle_dict          | 35.1 us                                                               | 37.9 us: 1.08x slower                                               |
| pickle               | 12.5 us                                                               | 13.7 us: 1.10x slower                                               |
| unpickle             | 17.5 us                                                               | 19.3 us: 1.11x slower                                               |
| Geometric mean       | (ref)                                                                 | 1.11x faster                                                        |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 13.0 ms: 1.17x slower                                               |
| python_startup_no_site | 6.89 ms                                                               | 8.65 ms: 1.26x slower                                               |
| Geometric mean         | (ref)                                                                 | 1.21x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.3 ms: 1.42x faster                                               |
| genshi_text     | 35.2 ms                                                               | 27.6 ms: 1.27x faster                                               |
| django_template | 53.3 ms                                                               | 42.6 ms: 1.25x faster                                               |
| genshi_xml      | 69.8 ms                                                               | 60.4 ms: 1.16x faster                                               |
| Geometric mean  | (ref)                                                                 | 1.27x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 193 us: 3.42x faster                                                |
| deltablue                | 8.94 ms                                                               | 3.89 ms: 2.30x faster                                               |
| async_tree_none          | 950 ms                                                                | 427 ms: 2.22x faster                                                |
| bench_mp_pool            | 14.5 ms                                                               | 7.11 ms: 2.04x faster                                               |
| async_tree_memoization   | 1.13 sec                                                              | 562 ms: 2.02x faster                                                |
| async_tree_io            | 2.28 sec                                                              | 1.14 sec: 2.01x faster                                              |
| generators               | 68.1 ms                                                               | 34.8 ms: 1.95x faster                                               |
| go                       | 264 ms                                                                | 137 ms: 1.93x faster                                                |
| raytrace                 | 573 ms                                                                | 301 ms: 1.90x faster                                                |
| richards_super           | 107 ms                                                                | 59.5 ms: 1.80x faster                                               |
| chaos                    | 121 ms                                                                | 68.1 ms: 1.78x faster                                               |
| richards                 | 91.7 ms                                                               | 52.7 ms: 1.74x faster                                               |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 734 ms: 1.73x faster                                                |
| sqlglot_parse            | 2.40 ms                                                               | 1.41 ms: 1.70x faster                                               |
| scimark_lu               | 227 ms                                                                | 134 ms: 1.70x faster                                                |
| logging_silent           | 222 ns                                                                | 131 ns: 1.69x faster                                                |
| asyncio_tcp              | 944 ms                                                                | 566 ms: 1.67x faster                                                |
| deepcopy_memo            | 61.7 us                                                               | 37.3 us: 1.65x faster                                               |
| sqlglot_transpile        | 2.84 ms                                                               | 1.74 ms: 1.64x faster                                               |
| comprehensions           | 33.1 us                                                               | 20.3 us: 1.63x faster                                               |
| crypto_pyaes             | 134 ms                                                                | 82.9 ms: 1.62x faster                                               |
| scimark_monte_carlo      | 128 ms                                                                | 80.7 ms: 1.58x faster                                               |
| scimark_sor              | 246 ms                                                                | 156 ms: 1.58x faster                                                |
| hexiom                   | 10.9 ms                                                               | 7.06 ms: 1.55x faster                                               |
| nbody                    | 166 ms                                                                | 109 ms: 1.53x faster                                                |
| deepcopy                 | 511 us                                                                | 337 us: 1.51x faster                                                |
| asyncio_tcp_ssl          | 3.28 sec                                                              | 2.21 sec: 1.48x faster                                              |
| unpickle_pure_python     | 366 us                                                                | 252 us: 1.45x faster                                                |
| pickle_pure_python       | 529 us                                                                | 368 us: 1.44x faster                                                |
| float                    | 135 ms                                                                | 94.2 ms: 1.43x faster                                               |
| regex_compile            | 177 ms                                                                | 124 ms: 1.42x faster                                                |
| mako                     | 18.9 ms                                                               | 13.3 ms: 1.42x faster                                               |
| tornado_http             | 178 ms                                                                | 126 ms: 1.41x faster                                                |
| pycparser                | 1.69 sec                                                              | 1.21 sec: 1.39x faster                                              |
| logging_format           | 10.6 us                                                               | 7.72 us: 1.37x faster                                               |
| pyflate                  | 795 ms                                                                | 579 ms: 1.37x faster                                                |
| logging_simple           | 9.78 us                                                               | 7.15 us: 1.37x faster                                               |
| pylint                   | 485 ms                                                                | 362 ms: 1.34x faster                                                |
| thrift                   | 1.26 ms                                                               | 943 us: 1.34x faster                                                |
| spectral_norm            | 186 ms                                                                | 141 ms: 1.33x faster                                                |
| html5lib                 | 86.5 ms                                                               | 65.5 ms: 1.32x faster                                               |
| coroutines               | 37.2 ms                                                               | 28.4 ms: 1.31x faster                                               |
| sympy_sum                | 184 ms                                                                | 142 ms: 1.30x faster                                                |
| sympy_integrate          | 26.5 ms                                                               | 20.5 ms: 1.29x faster                                               |
| deepcopy_reduce          | 4.60 us                                                               | 3.57 us: 1.29x faster                                               |
| bench_thread_pool        | 1.59 ms                                                               | 1.24 ms: 1.29x faster                                               |
| tomli_loads              | 3.36 sec                                                              | 2.61 sec: 1.29x faster                                              |
| 2to3                     | 381 ms                                                                | 297 ms: 1.28x faster                                                |
| genshi_text              | 35.2 ms                                                               | 27.6 ms: 1.27x faster                                               |
| dulwich_log              | 73.5 ms                                                               | 58.4 ms: 1.26x faster                                               |
| pathlib                  | 26.3 ms                                                               | 20.9 ms: 1.26x faster                                               |
| json_dumps               | 16.7 ms                                                               | 13.3 ms: 1.26x faster                                               |
| xml_etree_process        | 99.5 ms                                                               | 79.1 ms: 1.26x faster                                               |
| django_template          | 53.3 ms                                                               | 42.6 ms: 1.25x faster                                               |
| sympy_str                | 329 ms                                                                | 264 ms: 1.24x faster                                                |
| pprint_safe_repr         | 1.15 sec                                                              | 923 ms: 1.24x faster                                                |
| pprint_pformat           | 2.36 sec                                                              | 1.91 sec: 1.24x faster                                              |
| sqlglot_normalize        | 156 ms                                                                | 129 ms: 1.21x faster                                                |
| sqlglot_optimize         | 75.4 ms                                                               | 62.9 ms: 1.20x faster                                               |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 6.39 ms: 1.19x faster                                               |
| sympy_expand             | 543 ms                                                                | 460 ms: 1.18x faster                                                |
| docutils                 | 3.53 sec                                                              | 3.03 sec: 1.16x faster                                              |
| nqueens                  | 117 ms                                                                | 101 ms: 1.16x faster                                                |
| fannkuch                 | 546 ms                                                                | 471 ms: 1.16x faster                                                |
| genshi_xml               | 69.8 ms                                                               | 60.4 ms: 1.16x faster                                               |
| scimark_fft              | 500 ms                                                                | 440 ms: 1.14x faster                                                |
| meteor_contest           | 126 ms                                                                | 112 ms: 1.13x faster                                                |
| mdp                      | 3.70 sec                                                              | 3.33 sec: 1.11x faster                                              |
| xml_etree_parse          | 212 ms                                                                | 191 ms: 1.11x faster                                                |
| unpickle_list            | 6.99 us                                                               | 6.38 us: 1.10x faster                                               |
| xml_etree_generate       | 123 ms                                                                | 113 ms: 1.09x faster                                                |
| sqlite_synth             | 4.12 us                                                               | 3.82 us: 1.08x faster                                               |
| json                     | 5.88 ms                                                               | 5.54 ms: 1.06x faster                                               |
| regex_v8                 | 32.2 ms                                                               | 30.7 ms: 1.05x faster                                               |
| regex_dna                | 257 ms                                                                | 253 ms: 1.02x faster                                                |
| pickle_list              | 5.24 us                                                               | 5.19 us: 1.01x faster                                               |
| json_loads               | 30.9 us                                                               | 31.4 us: 1.02x slower                                               |
| create_gc_cycles         | 2.26 ms                                                               | 2.37 ms: 1.05x slower                                               |
| async_generators         | 452 ms                                                                | 482 ms: 1.06x slower                                                |
| pickle_dict              | 35.1 us                                                               | 37.9 us: 1.08x slower                                               |
| pickle                   | 12.5 us                                                               | 13.7 us: 1.10x slower                                               |
| unpickle                 | 17.5 us                                                               | 19.3 us: 1.11x slower                                               |
| coverage                 | 83.6 ms                                                               | 97.0 ms: 1.16x slower                                               |
| python_startup           | 11.2 ms                                                               | 13.0 ms: 1.17x slower                                               |
| regex_effbot             | 4.25 ms                                                               | 5.01 ms: 1.18x slower                                               |
| telco                    | 8.49 ms                                                               | 10.3 ms: 1.21x slower                                               |
| gc_traversal             | 4.15 ms                                                               | 5.13 ms: 1.23x slower                                               |
| python_startup_no_site   | 6.89 ms                                                               | 8.65 ms: 1.26x slower                                               |
| Geometric mean           | (ref)                                                                 | 1.32x faster                                                        |

Benchmark hidden because not significant (3): xml_etree_iterparse, pidigits, asyncio_websockets
Ignored benchmarks (8) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, chameleon, dask, flaskblogging, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240911-3.14.0a0-3b5fdc8/bm-20240911-arminc-aarch64-mdboom-pysequence_tuple-3.14.0a0-3b5fdc8.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, unpack_sequence

- Geometric mean (including insignificant results): 1.331x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.25x
- 95% likely to have a speedup of 1.24x
- 99% likely to have a speedup of 1.22x

# Memory
- memory change: 1.14x