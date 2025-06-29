# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_hot
- machine: linux-aarch64
- commit hash: a987be7
- commit date: 2025-06-23
- overall geometric mean: 1.328x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.19x faster
- Memory change: 1.39x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 312 ms: 1.22x faster                                                |
| docutils       | 3.53 sec                                                              | 3.09 sec: 1.14x faster                                              |
| html5lib       | 86.5 ms                                                               | 62.9 ms: 1.37x faster                                               |
| Geometric mean | (ref)                                                                 | 1.24x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 891 ms: 2.56x faster                                                |
| async_tree_memoization  | 1.13 sec                                                              | 465 ms: 2.44x faster                                                |
| async_tree_none         | 950 ms                                                                | 398 ms: 2.38x faster                                                |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 659 ms: 1.93x faster                                                |
| Geometric mean          | (ref)                                                                 | 2.32x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 135 ms                                                                | 82.3 ms: 1.64x faster                                               |
| nbody          | 166 ms                                                                | 116 ms: 1.43x faster                                                |
| Geometric mean | (ref)                                                                 | 1.33x faster                                                        |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 121 ms: 1.46x faster                                                |
| regex_v8       | 32.2 ms                                                               | 26.7 ms: 1.20x faster                                               |
| regex_dna      | 257 ms                                                                | 218 ms: 1.18x faster                                                |
| regex_effbot   | 4.25 ms                                                               | 3.95 ms: 1.08x faster                                               |
| Geometric mean | (ref)                                                                 | 1.22x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.35 sec: 1.43x faster                                              |
| unpickle_pure_python | 366 us                                                                | 257 us: 1.42x faster                                                |
| pickle_pure_python   | 529 us                                                                | 388 us: 1.36x faster                                                |
| xml_etree_process    | 99.5 ms                                                               | 78.1 ms: 1.27x faster                                               |
| json_dumps           | 16.7 ms                                                               | 13.3 ms: 1.26x faster                                               |
| xml_etree_parse      | 212 ms                                                                | 180 ms: 1.18x faster                                                |
| xml_etree_generate   | 123 ms                                                                | 111 ms: 1.11x faster                                                |
| xml_etree_iterparse  | 156 ms                                                                | 145 ms: 1.08x faster                                                |
| json_loads           | 30.9 us                                                               | 32.7 us: 1.06x slower                                               |
| Geometric mean       | (ref)                                                                 | 1.22x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.63 ms: 1.25x slower                                               |
| python_startup         | 11.2 ms                                                               | 15.2 ms: 1.36x slower                                               |
| Geometric mean         | (ref)                                                                 | 1.30x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 18.9 ms                                                               | 13.2 ms: 1.44x faster                                               |
| django_template | 53.3 ms                                                               | 39.7 ms: 1.34x faster                                               |
| genshi_text     | 35.2 ms                                                               | 26.9 ms: 1.31x faster                                               |
| genshi_xml      | 69.8 ms                                                               | 61.1 ms: 1.14x faster                                               |
| Geometric mean  | (ref)                                                                 | 1.30x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 212 us: 3.12x faster                                                |
| async_tree_io            | 2.28 sec                                                              | 891 ms: 2.56x faster                                                |
| async_tree_memoization   | 1.13 sec                                                              | 465 ms: 2.44x faster                                                |
| async_tree_none          | 950 ms                                                                | 398 ms: 2.38x faster                                                |
| deltablue                | 8.94 ms                                                               | 3.91 ms: 2.28x faster                                               |
| mdp                      | 3.70 sec                                                              | 1.67 sec: 2.22x faster                                              |
| richards_super           | 107 ms                                                                | 51.4 ms: 2.09x faster                                               |
| richards                 | 91.7 ms                                                               | 45.1 ms: 2.03x faster                                               |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 659 ms: 1.93x faster                                                |
| generators               | 68.1 ms                                                               | 36.6 ms: 1.86x faster                                               |
| raytrace                 | 573 ms                                                                | 329 ms: 1.74x faster                                                |
| chaos                    | 121 ms                                                                | 70.1 ms: 1.73x faster                                               |
| deepcopy_memo            | 61.7 us                                                               | 36.6 us: 1.69x faster                                               |
| scimark_sor              | 246 ms                                                                | 148 ms: 1.67x faster                                                |
| go                       | 264 ms                                                                | 159 ms: 1.66x faster                                                |
| float                    | 135 ms                                                                | 82.3 ms: 1.64x faster                                               |
| scimark_monte_carlo      | 128 ms                                                                | 82.0 ms: 1.56x faster                                               |
| scimark_lu               | 227 ms                                                                | 150 ms: 1.51x faster                                                |
| pylint                   | 485 ms                                                                | 323 ms: 1.50x faster                                                |
| deepcopy                 | 511 us                                                                | 340 us: 1.50x faster                                                |
| pyflate                  | 795 ms                                                                | 532 ms: 1.49x faster                                                |
| comprehensions           | 33.1 us                                                               | 22.2 us: 1.49x faster                                               |
| regex_compile            | 177 ms                                                                | 121 ms: 1.46x faster                                                |
| hexiom                   | 10.9 ms                                                               | 7.52 ms: 1.45x faster                                               |
| mako                     | 18.9 ms                                                               | 13.2 ms: 1.44x faster                                               |
| spectral_norm            | 186 ms                                                                | 130 ms: 1.43x faster                                                |
| tomli_loads              | 3.36 sec                                                              | 2.35 sec: 1.43x faster                                              |
| crypto_pyaes             | 134 ms                                                                | 93.9 ms: 1.43x faster                                               |
| nbody                    | 166 ms                                                                | 116 ms: 1.43x faster                                                |
| unpickle_pure_python     | 366 us                                                                | 257 us: 1.42x faster                                                |
| html5lib                 | 86.5 ms                                                               | 62.9 ms: 1.37x faster                                               |
| pickle_pure_python       | 529 us                                                                | 388 us: 1.36x faster                                                |
| dulwich_log              | 73.5 ms                                                               | 54.3 ms: 1.35x faster                                               |
| django_template          | 53.3 ms                                                               | 39.7 ms: 1.34x faster                                               |
| thrift                   | 1.26 ms                                                               | 938 us: 1.34x faster                                                |
| logging_simple           | 9.78 us                                                               | 7.46 us: 1.31x faster                                               |
| genshi_text              | 35.2 ms                                                               | 26.9 ms: 1.31x faster                                               |
| logging_format           | 10.6 us                                                               | 8.16 us: 1.30x faster                                               |
| deepcopy_reduce          | 4.60 us                                                               | 3.58 us: 1.29x faster                                               |
| xml_etree_process        | 99.5 ms                                                               | 78.1 ms: 1.27x faster                                               |
| coroutines               | 37.2 ms                                                               | 29.3 ms: 1.27x faster                                               |
| sympy_integrate          | 26.5 ms                                                               | 21.1 ms: 1.26x faster                                               |
| json_dumps               | 16.7 ms                                                               | 13.3 ms: 1.26x faster                                               |
| pycparser                | 1.69 sec                                                              | 1.38 sec: 1.23x faster                                              |
| 2to3                     | 381 ms                                                                | 312 ms: 1.22x faster                                                |
| regex_v8                 | 32.2 ms                                                               | 26.7 ms: 1.20x faster                                               |
| sympy_sum                | 184 ms                                                                | 155 ms: 1.19x faster                                                |
| xml_etree_parse          | 212 ms                                                                | 180 ms: 1.18x faster                                                |
| regex_dna                | 257 ms                                                                | 218 ms: 1.18x faster                                                |
| nqueens                  | 117 ms                                                                | 100.0 ms: 1.17x faster                                              |
| scimark_fft              | 500 ms                                                                | 428 ms: 1.17x faster                                                |
| sympy_str                | 329 ms                                                                | 281 ms: 1.17x faster                                                |
| pathlib                  | 26.3 ms                                                               | 22.8 ms: 1.16x faster                                               |
| genshi_xml               | 69.8 ms                                                               | 61.1 ms: 1.14x faster                                               |
| docutils                 | 3.53 sec                                                              | 3.09 sec: 1.14x faster                                              |
| fannkuch                 | 546 ms                                                                | 480 ms: 1.14x faster                                                |
| xml_etree_generate       | 123 ms                                                                | 111 ms: 1.11x faster                                                |
| sympy_expand             | 543 ms                                                                | 491 ms: 1.11x faster                                                |
| sqlite_synth             | 4.12 us                                                               | 3.77 us: 1.09x faster                                               |
| meteor_contest           | 126 ms                                                                | 116 ms: 1.09x faster                                                |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.01 ms: 1.09x faster                                               |
| xml_etree_iterparse      | 156 ms                                                                | 145 ms: 1.08x faster                                                |
| regex_effbot             | 4.25 ms                                                               | 3.95 ms: 1.08x faster                                               |
| asyncio_websockets       | 657 ms                                                                | 666 ms: 1.01x slower                                                |
| async_generators         | 452 ms                                                                | 476 ms: 1.05x slower                                                |
| json_loads               | 30.9 us                                                               | 32.7 us: 1.06x slower                                               |
| pprint_safe_repr         | 1.15 sec                                                              | 1.24 sec: 1.08x slower                                              |
| pprint_pformat           | 2.36 sec                                                              | 2.58 sec: 1.10x slower                                              |
| telco                    | 8.49 ms                                                               | 9.38 ms: 1.10x slower                                               |
| coverage                 | 83.6 ms                                                               | 101 ms: 1.20x slower                                                |
| python_startup_no_site   | 6.89 ms                                                               | 8.63 ms: 1.25x slower                                               |
| python_startup           | 11.2 ms                                                               | 15.2 ms: 1.36x slower                                               |
| gc_traversal             | 4.15 ms                                                               | 6.95 ms: 1.67x slower                                               |
| create_gc_cycles         | 2.26 ms                                                               | 3.87 ms: 1.71x slower                                               |
| logging_silent           | 222 ns                                                                | 618 ns: 2.78x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.29x faster                                                        |

Benchmark hidden because not significant (2): json, pidigits
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250623-3.15.0a0-a987be7-JIT/bm-20250623-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-a987be7.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.328x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.23x
- 95% likely to have a speedup of 1.22x
- 99% likely to have a speedup of 1.19x

# Memory
- memory change: 1.39x