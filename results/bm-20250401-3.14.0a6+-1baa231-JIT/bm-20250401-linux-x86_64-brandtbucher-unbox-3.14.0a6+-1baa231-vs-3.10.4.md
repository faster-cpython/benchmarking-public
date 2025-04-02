# Results vs. 3.10.4

- fork: brandtbucher
- ref: unbox
- machine: linux-x86_64
- commit hash: 1baa231
- commit date: 2025-04-01
- overall geometric mean: 1.417x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.27x faster
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 270 ms: 1.29x faster                                          |
| docutils       | 3.30 sec                                               | 2.73 sec: 1.21x faster                                        |
| html5lib       | 88.9 ms                                                | 63.9 ms: 1.39x faster                                         |
| Geometric mean | (ref)                                                  | 1.29x faster                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 634 ms: 2.79x faster                                          |
| async_tree_none         | 728 ms                                                 | 267 ms: 2.73x faster                                          |
| async_tree_memoization  | 870 ms                                                 | 323 ms: 2.70x faster                                          |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 497 ms: 2.04x faster                                          |
| Geometric mean          | (ref)                                                  | 2.54x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| nbody          | 154 ms                                                 | 91.3 ms: 1.68x faster                                         |
| float          | 117 ms                                                 | 69.7 ms: 1.68x faster                                         |
| pidigits       | 191 ms                                                 | 188 ms: 1.02x faster                                          |
| Geometric mean | (ref)                                                  | 1.42x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 133 ms: 1.42x faster                                          |
| regex_v8       | 27.8 ms                                                | 22.5 ms: 1.24x faster                                         |
| regex_effbot   | 3.63 ms                                                | 3.19 ms: 1.14x faster                                         |
| regex_dna      | 227 ms                                                 | 215 ms: 1.05x faster                                          |
| Geometric mean | (ref)                                                  | 1.20x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.79 sec: 1.75x faster                                        |
| pickle_pure_python   | 484 us                                                 | 334 us: 1.45x faster                                          |
| unpickle_pure_python | 331 us                                                 | 231 us: 1.43x faster                                          |
| xml_etree_process    | 79.1 ms                                                | 58.8 ms: 1.35x faster                                         |
| json_dumps           | 14.2 ms                                                | 11.5 ms: 1.24x faster                                         |
| xml_etree_generate   | 99.4 ms                                                | 83.5 ms: 1.19x faster                                         |
| xml_etree_parse      | 168 ms                                                 | 142 ms: 1.18x faster                                          |
| xml_etree_iterparse  | 115 ms                                                 | 100 ms: 1.15x faster                                          |
| json_loads           | 31.2 us                                                | 31.9 us: 1.02x slower                                         |
| Geometric mean       | (ref)                                                  | 1.29x faster                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.11x faster                                         |
| python_startup_no_site | 5.93 ms                                                | 8.21 ms: 1.38x slower                                         |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| genshi_text     | 31.8 ms                                                | 21.9 ms: 1.45x faster                                         |
| django_template | 48.2 ms                                                | 33.1 ms: 1.45x faster                                         |
| mako            | 16.3 ms                                                | 11.8 ms: 1.39x faster                                         |
| genshi_xml      | 66.0 ms                                                | 50.5 ms: 1.31x faster                                         |
| Geometric mean  | (ref)                                                  | 1.40x faster                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 174 us: 3.13x faster                                          |
| generators               | 80.1 ms                                                | 28.5 ms: 2.81x faster                                         |
| async_tree_io            | 1.77 sec                                               | 634 ms: 2.79x faster                                          |
| async_tree_none          | 728 ms                                                 | 267 ms: 2.73x faster                                          |
| async_tree_memoization   | 870 ms                                                 | 323 ms: 2.70x faster                                          |
| deltablue                | 7.91 ms                                                | 3.34 ms: 2.37x faster                                         |
| mdp                      | 2.85 sec                                               | 1.27 sec: 2.24x faster                                        |
| richards_super           | 94.7 ms                                                | 44.1 ms: 2.15x faster                                         |
| richards                 | 79.3 ms                                                | 38.0 ms: 2.08x faster                                         |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 497 ms: 2.04x faster                                          |
| chaos                    | 115 ms                                                 | 58.9 ms: 1.96x faster                                         |
| deepcopy_memo            | 58.5 us                                                | 29.9 us: 1.96x faster                                         |
| pylint                   | 551 ms                                                 | 287 ms: 1.92x faster                                          |
| logging_silent           | 190 ns                                                 | 103 ns: 1.83x faster                                          |
| raytrace                 | 507 ms                                                 | 281 ms: 1.81x faster                                          |
| deepcopy                 | 479 us                                                 | 266 us: 1.80x faster                                          |
| tomli_loads              | 3.14 sec                                               | 1.79 sec: 1.75x faster                                        |
| go                       | 240 ms                                                 | 138 ms: 1.74x faster                                          |
| spectral_norm            | 170 ms                                                 | 99.5 ms: 1.71x faster                                         |
| scimark_monte_carlo      | 118 ms                                                 | 69.8 ms: 1.69x faster                                         |
| coroutines               | 35.1 ms                                                | 20.7 ms: 1.69x faster                                         |
| nbody                    | 154 ms                                                 | 91.3 ms: 1.68x faster                                         |
| float                    | 117 ms                                                 | 69.7 ms: 1.68x faster                                         |
| scimark_sor              | 220 ms                                                 | 141 ms: 1.55x faster                                          |
| pyflate                  | 716 ms                                                 | 470 ms: 1.53x faster                                          |
| hexiom                   | 10.4 ms                                                | 6.96 ms: 1.49x faster                                         |
| logging_simple           | 8.30 us                                                | 5.56 us: 1.49x faster                                         |
| logging_format           | 9.09 us                                                | 6.12 us: 1.49x faster                                         |
| deepcopy_reduce          | 4.17 us                                                | 2.82 us: 1.48x faster                                         |
| comprehensions           | 28.8 us                                                | 19.6 us: 1.46x faster                                         |
| crypto_pyaes             | 128 ms                                                 | 87.4 ms: 1.46x faster                                         |
| genshi_text              | 31.8 ms                                                | 21.9 ms: 1.45x faster                                         |
| django_template          | 48.2 ms                                                | 33.1 ms: 1.45x faster                                         |
| pickle_pure_python       | 484 us                                                 | 334 us: 1.45x faster                                          |
| unpickle_pure_python     | 331 us                                                 | 231 us: 1.43x faster                                          |
| scimark_lu               | 176 ms                                                 | 124 ms: 1.42x faster                                          |
| regex_compile            | 188 ms                                                 | 133 ms: 1.42x faster                                          |
| scimark_fft              | 466 ms                                                 | 329 ms: 1.41x faster                                          |
| html5lib                 | 88.9 ms                                                | 63.9 ms: 1.39x faster                                         |
| mako                     | 16.3 ms                                                | 11.8 ms: 1.39x faster                                         |
| dulwich_log              | 84.3 ms                                                | 61.9 ms: 1.36x faster                                         |
| xml_etree_process        | 79.1 ms                                                | 58.8 ms: 1.35x faster                                         |
| sqlalchemy_imperative    | 23.3 ms                                                | 17.5 ms: 1.34x faster                                         |
| genshi_xml               | 66.0 ms                                                | 50.5 ms: 1.31x faster                                         |
| 2to3                     | 348 ms                                                 | 270 ms: 1.29x faster                                          |
| pprint_pformat           | 2.10 sec                                               | 1.63 sec: 1.29x faster                                        |
| sqlalchemy_declarative   | 172 ms                                                 | 135 ms: 1.28x faster                                          |
| sympy_sum                | 196 ms                                                 | 154 ms: 1.28x faster                                          |
| sympy_integrate          | 25.8 ms                                                | 20.4 ms: 1.27x faster                                         |
| pprint_safe_repr         | 1.02 sec                                               | 805 ms: 1.26x faster                                          |
| pycparser                | 1.58 sec                                               | 1.25 sec: 1.26x faster                                        |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.21 ms: 1.24x faster                                         |
| json_dumps               | 14.2 ms                                                | 11.5 ms: 1.24x faster                                         |
| regex_v8                 | 27.8 ms                                                | 22.5 ms: 1.24x faster                                         |
| fannkuch                 | 532 ms                                                 | 431 ms: 1.23x faster                                          |
| sympy_str                | 346 ms                                                 | 281 ms: 1.23x faster                                          |
| nqueens                  | 106 ms                                                 | 86.4 ms: 1.22x faster                                         |
| pathlib                  | 20.5 ms                                                | 16.8 ms: 1.22x faster                                         |
| docutils                 | 3.30 sec                                               | 2.73 sec: 1.21x faster                                        |
| xml_etree_generate       | 99.4 ms                                                | 83.5 ms: 1.19x faster                                         |
| xml_etree_parse          | 168 ms                                                 | 142 ms: 1.18x faster                                          |
| sympy_expand             | 566 ms                                                 | 487 ms: 1.16x faster                                          |
| xml_etree_iterparse      | 115 ms                                                 | 100 ms: 1.15x faster                                          |
| regex_effbot             | 3.63 ms                                                | 3.19 ms: 1.14x faster                                         |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.11x faster                                         |
| bench_thread_pool        | 986 us                                                 | 897 us: 1.10x faster                                          |
| sqlite_synth             | 3.02 us                                                | 2.79 us: 1.08x faster                                         |
| meteor_contest           | 120 ms                                                 | 112 ms: 1.07x faster                                          |
| regex_dna                | 227 ms                                                 | 215 ms: 1.05x faster                                          |
| async_generators         | 444 ms                                                 | 426 ms: 1.04x faster                                          |
| json                     | 5.69 ms                                                | 5.46 ms: 1.04x faster                                         |
| pidigits                 | 191 ms                                                 | 188 ms: 1.02x faster                                          |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                          |
| json_loads               | 31.2 us                                                | 31.9 us: 1.02x slower                                         |
| coverage                 | 79.4 ms                                                | 85.2 ms: 1.07x slower                                         |
| telco                    | 7.27 ms                                                | 8.06 ms: 1.11x slower                                         |
| python_startup_no_site   | 5.93 ms                                                | 8.21 ms: 1.38x slower                                         |
| gc_traversal             | 3.62 ms                                                | 5.06 ms: 1.39x slower                                         |
| create_gc_cycles         | 1.62 ms                                                | 2.49 ms: 1.54x slower                                         |
| bench_mp_pool            | 24.0 ms                                                | 83.7 ms: 3.49x slower                                         |
| Geometric mean           | (ref)                                                  | 1.39x faster                                                  |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250401-3.14.0a6+-1baa231-JIT/bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-1baa231.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.417x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.30x
- 95% likely to have a speedup of 1.29x
- 99% likely to have a speedup of 1.27x

# Memory
- memory change: 1.30x