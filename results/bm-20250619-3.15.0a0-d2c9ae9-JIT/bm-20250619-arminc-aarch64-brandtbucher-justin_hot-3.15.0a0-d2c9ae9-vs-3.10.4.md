# Results vs. 3.10.4

- fork: brandtbucher
- ref: justin_hot
- machine: linux-aarch64
- commit hash: d2c9ae9
- commit date: 2025-06-19
- overall geometric mean: 1.268x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.15x faster
- Memory change: 1.40x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 381 ms                                                                | 317 ms: 1.20x faster                                                |
| docutils       | 3.53 sec                                                              | 3.15 sec: 1.12x faster                                              |
| html5lib       | 86.5 ms                                                               | 63.2 ms: 1.37x faster                                               |
| Geometric mean | (ref)                                                                 | 1.23x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io           | 2.28 sec                                                              | 900 ms: 2.54x faster                                                |
| async_tree_memoization  | 1.13 sec                                                              | 473 ms: 2.40x faster                                                |
| async_tree_none         | 950 ms                                                                | 403 ms: 2.36x faster                                                |
| async_tree_cpu_io_mixed | 1.27 sec                                                              | 665 ms: 1.91x faster                                                |
| Geometric mean          | (ref)                                                                 | 2.29x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 135 ms                                                                | 88.6 ms: 1.52x faster                                               |
| nbody          | 166 ms                                                                | 147 ms: 1.13x faster                                                |
| pidigits       | 235 ms                                                                | 236 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                 | 1.20x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 177 ms                                                                | 130 ms: 1.36x faster                                                |
| regex_v8       | 32.2 ms                                                               | 26.9 ms: 1.20x faster                                               |
| regex_dna      | 257 ms                                                                | 223 ms: 1.15x faster                                                |
| regex_effbot   | 4.25 ms                                                               | 3.94 ms: 1.08x faster                                               |
| Geometric mean | (ref)                                                                 | 1.19x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 3.36 sec                                                              | 2.55 sec: 1.31x faster                                              |
| pickle_pure_python   | 529 us                                                                | 404 us: 1.31x faster                                                |
| unpickle_pure_python | 366 us                                                                | 295 us: 1.24x faster                                                |
| xml_etree_process    | 99.5 ms                                                               | 80.9 ms: 1.23x faster                                               |
| json_dumps           | 16.7 ms                                                               | 13.8 ms: 1.21x faster                                               |
| xml_etree_parse      | 212 ms                                                                | 180 ms: 1.18x faster                                                |
| xml_etree_generate   | 123 ms                                                                | 112 ms: 1.09x faster                                                |
| xml_etree_iterparse  | 156 ms                                                                | 144 ms: 1.09x faster                                                |
| json_loads           | 30.9 us                                                               | 32.3 us: 1.04x slower                                               |
| Geometric mean       | (ref)                                                                 | 1.17x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.89 ms                                                               | 8.60 ms: 1.25x slower                                               |
| python_startup         | 11.2 ms                                                               | 15.0 ms: 1.34x slower                                               |
| Geometric mean         | (ref)                                                                 | 1.29x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 53.3 ms                                                               | 39.0 ms: 1.37x faster                                               |
| genshi_text     | 35.2 ms                                                               | 27.1 ms: 1.30x faster                                               |
| mako            | 18.9 ms                                                               | 15.1 ms: 1.25x faster                                               |
| genshi_xml      | 69.8 ms                                                               | 64.2 ms: 1.09x faster                                               |
| Geometric mean  | (ref)                                                                 | 1.25x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120 | bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9 |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 661 us                                                                | 210 us: 3.14x faster                                                |
| async_tree_io            | 2.28 sec                                                              | 900 ms: 2.54x faster                                                |
| async_tree_memoization   | 1.13 sec                                                              | 473 ms: 2.40x faster                                                |
| async_tree_none          | 950 ms                                                                | 403 ms: 2.36x faster                                                |
| mdp                      | 3.70 sec                                                              | 1.72 sec: 2.15x faster                                              |
| deltablue                | 8.94 ms                                                               | 4.57 ms: 1.96x faster                                               |
| richards_super           | 107 ms                                                                | 55.7 ms: 1.93x faster                                               |
| async_tree_cpu_io_mixed  | 1.27 sec                                                              | 665 ms: 1.91x faster                                                |
| generators               | 68.1 ms                                                               | 36.4 ms: 1.87x faster                                               |
| richards                 | 91.7 ms                                                               | 52.1 ms: 1.76x faster                                               |
| chaos                    | 121 ms                                                                | 69.7 ms: 1.74x faster                                               |
| scimark_sor              | 246 ms                                                                | 147 ms: 1.68x faster                                                |
| raytrace                 | 573 ms                                                                | 343 ms: 1.67x faster                                                |
| deepcopy_memo            | 61.7 us                                                               | 37.2 us: 1.66x faster                                               |
| deepcopy                 | 511 us                                                                | 331 us: 1.54x faster                                                |
| float                    | 135 ms                                                                | 88.6 ms: 1.52x faster                                               |
| scimark_lu               | 227 ms                                                                | 152 ms: 1.50x faster                                                |
| scimark_monte_carlo      | 128 ms                                                                | 86.9 ms: 1.47x faster                                               |
| pylint                   | 485 ms                                                                | 332 ms: 1.46x faster                                                |
| html5lib                 | 86.5 ms                                                               | 63.2 ms: 1.37x faster                                               |
| go                       | 264 ms                                                                | 193 ms: 1.37x faster                                                |
| django_template          | 53.3 ms                                                               | 39.0 ms: 1.37x faster                                               |
| regex_compile            | 177 ms                                                                | 130 ms: 1.36x faster                                                |
| thrift                   | 1.26 ms                                                               | 940 us: 1.34x faster                                                |
| comprehensions           | 33.1 us                                                               | 25.1 us: 1.32x faster                                               |
| tomli_loads              | 3.36 sec                                                              | 2.55 sec: 1.31x faster                                              |
| pyflate                  | 795 ms                                                                | 606 ms: 1.31x faster                                                |
| pickle_pure_python       | 529 us                                                                | 404 us: 1.31x faster                                                |
| dulwich_log              | 73.5 ms                                                               | 56.1 ms: 1.31x faster                                               |
| crypto_pyaes             | 134 ms                                                                | 102 ms: 1.31x faster                                                |
| logging_simple           | 9.78 us                                                               | 7.49 us: 1.31x faster                                               |
| genshi_text              | 35.2 ms                                                               | 27.1 ms: 1.30x faster                                               |
| deepcopy_reduce          | 4.60 us                                                               | 3.56 us: 1.29x faster                                               |
| logging_format           | 10.6 us                                                               | 8.29 us: 1.28x faster                                               |
| sympy_integrate          | 26.5 ms                                                               | 21.0 ms: 1.26x faster                                               |
| mako                     | 18.9 ms                                                               | 15.1 ms: 1.25x faster                                               |
| unpickle_pure_python     | 366 us                                                                | 295 us: 1.24x faster                                                |
| sympy_sum                | 184 ms                                                                | 149 ms: 1.24x faster                                                |
| coroutines               | 37.2 ms                                                               | 30.1 ms: 1.24x faster                                               |
| xml_etree_process        | 99.5 ms                                                               | 80.9 ms: 1.23x faster                                               |
| spectral_norm            | 186 ms                                                                | 152 ms: 1.23x faster                                                |
| hexiom                   | 10.9 ms                                                               | 8.91 ms: 1.23x faster                                               |
| json_dumps               | 16.7 ms                                                               | 13.8 ms: 1.21x faster                                               |
| 2to3                     | 381 ms                                                                | 317 ms: 1.20x faster                                                |
| regex_v8                 | 32.2 ms                                                               | 26.9 ms: 1.20x faster                                               |
| xml_etree_parse          | 212 ms                                                                | 180 ms: 1.18x faster                                                |
| sympy_str                | 329 ms                                                                | 282 ms: 1.16x faster                                                |
| pycparser                | 1.69 sec                                                              | 1.46 sec: 1.16x faster                                              |
| regex_dna                | 257 ms                                                                | 223 ms: 1.15x faster                                                |
| pathlib                  | 26.3 ms                                                               | 23.1 ms: 1.14x faster                                               |
| nbody                    | 166 ms                                                                | 147 ms: 1.13x faster                                                |
| docutils                 | 3.53 sec                                                              | 3.15 sec: 1.12x faster                                              |
| nqueens                  | 117 ms                                                                | 106 ms: 1.10x faster                                                |
| sympy_expand             | 543 ms                                                                | 493 ms: 1.10x faster                                                |
| xml_etree_generate       | 123 ms                                                                | 112 ms: 1.09x faster                                                |
| sqlite_synth             | 4.12 us                                                               | 3.77 us: 1.09x faster                                               |
| genshi_xml               | 69.8 ms                                                               | 64.2 ms: 1.09x faster                                               |
| xml_etree_iterparse      | 156 ms                                                                | 144 ms: 1.09x faster                                                |
| regex_effbot             | 4.25 ms                                                               | 3.94 ms: 1.08x faster                                               |
| scimark_fft              | 500 ms                                                                | 466 ms: 1.07x faster                                                |
| json                     | 5.88 ms                                                               | 5.76 ms: 1.02x faster                                               |
| pidigits                 | 235 ms                                                                | 236 ms: 1.01x slower                                                |
| meteor_contest           | 126 ms                                                                | 127 ms: 1.01x slower                                                |
| asyncio_websockets       | 657 ms                                                                | 666 ms: 1.01x slower                                                |
| fannkuch                 | 546 ms                                                                | 557 ms: 1.02x slower                                                |
| json_loads               | 30.9 us                                                               | 32.3 us: 1.04x slower                                               |
| async_generators         | 452 ms                                                                | 479 ms: 1.06x slower                                                |
| telco                    | 8.49 ms                                                               | 10.1 ms: 1.19x slower                                               |
| coverage                 | 83.6 ms                                                               | 101 ms: 1.21x slower                                                |
| python_startup_no_site   | 6.89 ms                                                               | 8.60 ms: 1.25x slower                                               |
| python_startup           | 11.2 ms                                                               | 15.0 ms: 1.34x slower                                               |
| pprint_safe_repr         | 1.15 sec                                                              | 1.54 sec: 1.34x slower                                              |
| pprint_pformat           | 2.36 sec                                                              | 3.25 sec: 1.38x slower                                              |
| create_gc_cycles         | 2.26 ms                                                               | 3.78 ms: 1.67x slower                                               |
| gc_traversal             | 4.15 ms                                                               | 7.06 ms: 1.70x slower                                               |
| logging_silent           | 222 ns                                                                | 609 ns: 2.74x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.24x faster                                                        |

Benchmark hidden because not significant (1): scimark_sparse_mat_mult
Ignored benchmarks (22) of results/bm-20220323-3.10.4-9d38120/bm-20220323-arminc-aarch64-python-9d38120e335357a3b294-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250619-3.15.0a0-d2c9ae9-JIT/bm-20250619-arminc-aarch64-brandtbucher-justin_hot-3.15.0a0-d2c9ae9.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.268x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.19x
- 95% likely to have a speedup of 1.17x
- 99% likely to have a speedup of 1.15x

# Memory
- memory change: 1.40x