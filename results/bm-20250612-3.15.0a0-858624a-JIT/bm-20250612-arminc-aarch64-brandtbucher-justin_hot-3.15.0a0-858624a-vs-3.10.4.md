# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_hot
- machine: linux-aarch64
- commit hash: 858624a
- commit date: 2025-06-12
- overall geometric mean: 1.149x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.13x faster
- Memory change: 1.40x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 320 ms: 1.19x faster                                                |
| docutils       | 3.53 sec                                                              | 3.15 sec: 1.12x faster                                              |
| html5lib       | 86.5 ms                                                               | 62.5 ms: 1.38x faster                                               |
| Geometric mean | (ref)                                                                 | 1.23x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 929 ms: 2.46x faster                                                |
| async_tree_memoization  | 1.13 sec                                                              | 481 ms: 2.36x faster                                                |
| async_tree_none         | 950 ms                                                                | 406 ms: 2.34x faster                                                |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 672 ms: 1.89x faster                                                |
| Geometric mean          | (ref)                                                                 | 2.25x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 135 ms                                                                | 89.6 ms: 1.50x faster                                               |
| nbody          | 166 ms                                                                | 145 ms: 1.14x faster                                                |
| Geometric mean | (ref)                                                                 | 1.20x faster                                                        |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 125 ms: 1.41x faster                                                |
| regex_dna      | 257 ms                                                                | 224 ms: 1.15x faster                                                |
| regex_v8       | 32.2 ms                                                               | 28.1 ms: 1.14x faster                                               |
| regex_effbot   | 4.25 ms                                                               | 3.85 ms: 1.10x faster                                               |
| Geometric mean | (ref)                                                                 | 1.20x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.54 sec: 1.32x faster                                              |
| pickle_pure_python   | 529 us                                                                | 407 us: 1.30x faster                                                |
| unpickle_pure_python | 366 us                                                                | 289 us: 1.26x faster                                                |
| json_dumps           | 16.7 ms                                                               | 13.3 ms: 1.25x faster                                               |
| xml_etree_process    | 99.5 ms                                                               | 83.0 ms: 1.20x faster                                               |
| xml_etree_parse      | 212 ms                                                                | 179 ms: 1.18x faster                                                |
| xml_etree_iterparse  | 156 ms                                                                | 143 ms: 1.09x faster                                                |
| xml_etree_generate   | 123 ms                                                                | 116 ms: 1.06x faster                                                |
| json_loads           | 30.9 us                                                               | 32.3 us: 1.05x slower                                               |
| Geometric mean       | (ref)                                                                 | 1.17x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.64 ms: 1.25x slower                                               |
| python_startup         | 11.2 ms                                                               | 15.2 ms: 1.36x slower                                               |
| Geometric mean         | (ref)                                                                 | 1.30x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 40.0 ms: 1.33x faster                                               |
| genshi_text     | 35.2 ms                                                               | 27.4 ms: 1.28x faster                                               |
| mako            | 18.9 ms                                                               | 15.2 ms: 1.25x faster                                               |
| genshi_xml      | 69.8 ms                                                               | 63.0 ms: 1.11x faster                                               |
| Geometric mean  | (ref)                                                                 | 1.24x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 214 us: 3.09x faster                                                |
| async_tree_io            | 2.28 sec                                                              | 929 ms: 2.46x faster                                                |
| async_tree_memoization   | 1.13 sec                                                              | 481 ms: 2.36x faster                                                |
| async_tree_none          | 950 ms                                                                | 406 ms: 2.34x faster                                                |
| mdp                      | 3.70 sec                                                              | 1.71 sec: 2.16x faster                                              |
| deltablue                | 8.94 ms                                                               | 4.59 ms: 1.95x faster                                               |
| richards_super           | 107 ms                                                                | 56.2 ms: 1.91x faster                                               |
| generators               | 68.1 ms                                                               | 35.7 ms: 1.91x faster                                               |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 672 ms: 1.89x faster                                                |
| richards                 | 91.7 ms                                                               | 51.7 ms: 1.77x faster                                               |
| chaos                    | 121 ms                                                                | 71.3 ms: 1.70x faster                                               |
| scimark_sor              | 246 ms                                                                | 146 ms: 1.69x faster                                                |
| raytrace                 | 573 ms                                                                | 343 ms: 1.67x faster                                                |
| deepcopy_memo            | 61.7 us                                                               | 37.3 us: 1.65x faster                                               |
| deepcopy                 | 511 us                                                                | 333 us: 1.53x faster                                                |
| float                    | 135 ms                                                                | 89.6 ms: 1.50x faster                                               |
| scimark_lu               | 227 ms                                                                | 152 ms: 1.49x faster                                                |
| pylint                   | 485 ms                                                                | 327 ms: 1.48x faster                                                |
| scimark_monte_carlo      | 128 ms                                                                | 86.5 ms: 1.48x faster                                               |
| regex_compile            | 177 ms                                                                | 125 ms: 1.41x faster                                                |
| html5lib                 | 86.5 ms                                                               | 62.5 ms: 1.38x faster                                               |
| go                       | 264 ms                                                                | 195 ms: 1.36x faster                                                |
| pyflate                  | 795 ms                                                                | 587 ms: 1.35x faster                                                |
| django_template          | 53.3 ms                                                               | 40.0 ms: 1.33x faster                                               |
| comprehensions           | 33.1 us                                                               | 25.1 us: 1.32x faster                                               |
| tomli_loads              | 3.36 sec                                                              | 2.54 sec: 1.32x faster                                              |
| crypto_pyaes             | 134 ms                                                                | 103 ms: 1.31x faster                                                |
| pickle_pure_python       | 529 us                                                                | 407 us: 1.30x faster                                                |
| genshi_text              | 35.2 ms                                                               | 27.4 ms: 1.28x faster                                               |
| logging_simple           | 9.78 us                                                               | 7.66 us: 1.28x faster                                               |
| coroutines               | 37.2 ms                                                               | 29.3 ms: 1.27x faster                                               |
| unpickle_pure_python     | 366 us                                                                | 289 us: 1.26x faster                                                |
| logging_format           | 10.6 us                                                               | 8.41 us: 1.26x faster                                               |
| deepcopy_reduce          | 4.60 us                                                               | 3.67 us: 1.25x faster                                               |
| json_dumps               | 16.7 ms                                                               | 13.3 ms: 1.25x faster                                               |
| mako                     | 18.9 ms                                                               | 15.2 ms: 1.25x faster                                               |
| dulwich_log              | 73.5 ms                                                               | 59.1 ms: 1.24x faster                                               |
| sympy_integrate          | 26.5 ms                                                               | 21.5 ms: 1.24x faster                                               |
| spectral_norm            | 186 ms                                                                | 152 ms: 1.23x faster                                                |
| sympy_sum                | 184 ms                                                                | 150 ms: 1.23x faster                                                |
| hexiom                   | 10.9 ms                                                               | 8.98 ms: 1.21x faster                                               |
| xml_etree_process        | 99.5 ms                                                               | 83.0 ms: 1.20x faster                                               |
| 2to3                     | 381 ms                                                                | 320 ms: 1.19x faster                                                |
| xml_etree_parse          | 212 ms                                                                | 179 ms: 1.18x faster                                                |
| pycparser                | 1.69 sec                                                              | 1.44 sec: 1.17x faster                                              |
| sympy_str                | 329 ms                                                                | 281 ms: 1.17x faster                                                |
| regex_dna                | 257 ms                                                                | 224 ms: 1.15x faster                                                |
| regex_v8                 | 32.2 ms                                                               | 28.1 ms: 1.14x faster                                               |
| nbody                    | 166 ms                                                                | 145 ms: 1.14x faster                                                |
| pathlib                  | 26.3 ms                                                               | 23.3 ms: 1.13x faster                                               |
| docutils                 | 3.53 sec                                                              | 3.15 sec: 1.12x faster                                              |
| genshi_xml               | 69.8 ms                                                               | 63.0 ms: 1.11x faster                                               |
| regex_effbot             | 4.25 ms                                                               | 3.85 ms: 1.10x faster                                               |
| nqueens                  | 117 ms                                                                | 107 ms: 1.10x faster                                                |
| xml_etree_iterparse      | 156 ms                                                                | 143 ms: 1.09x faster                                                |
| scimark_fft              | 500 ms                                                                | 464 ms: 1.08x faster                                                |
| scimark_sparse_mat_mult  | 7.62 ms                                                               | 7.08 ms: 1.08x faster                                               |
| sympy_expand             | 543 ms                                                                | 507 ms: 1.07x faster                                                |
| xml_etree_generate       | 123 ms                                                                | 116 ms: 1.06x faster                                                |
| sqlite_synth             | 4.12 us                                                               | 3.87 us: 1.06x faster                                               |
| json                     | 5.88 ms                                                               | 5.64 ms: 1.04x faster                                               |
| asyncio_websockets       | 657 ms                                                                | 670 ms: 1.02x slower                                                |
| json_loads               | 30.9 us                                                               | 32.3 us: 1.05x slower                                               |
| fannkuch                 | 546 ms                                                                | 582 ms: 1.07x slower                                                |
| async_generators         | 452 ms                                                                | 485 ms: 1.07x slower                                                |
| telco                    | 8.49 ms                                                               | 10.2 ms: 1.20x slower                                               |
| python_startup_no_site   | 6.89 ms                                                               | 8.64 ms: 1.25x slower                                               |
| pprint_safe_repr         | 1.15 sec                                                              | 1.55 sec: 1.35x slower                                              |
| python_startup           | 11.2 ms                                                               | 15.2 ms: 1.36x slower                                               |
| pprint_pformat           | 2.36 sec                                                              | 3.30 sec: 1.40x slower                                              |
| gc_traversal             | 4.15 ms                                                               | 6.75 ms: 1.62x slower                                               |
| create_gc_cycles         | 2.26 ms                                                               | 3.74 ms: 1.66x slower                                               |
| logging_silent           | 222 ns                                                                | 614 ns: 2.77x slower                                                |
| coverage                 | 83.6 ms                                                               | 578 ms: 6.92x slower                                                |
| thrift                   | 1.26 ms                                                               | 193 ms: 153.01x slower                                              |
| Geometric mean           | (ref)                                                                 | 1.12x faster                                                        |

Benchmark hidden because not significant (2): pidigits, meteor_contest
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250612-3.15.0a0-858624a-JIT/bm-20250612-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-858624a.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.149x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.17x
- 95% likely to have a speedup of 1.16x
- 99% likely to have a speedup of 1.13x

# Memory
- memory change: 1.40x