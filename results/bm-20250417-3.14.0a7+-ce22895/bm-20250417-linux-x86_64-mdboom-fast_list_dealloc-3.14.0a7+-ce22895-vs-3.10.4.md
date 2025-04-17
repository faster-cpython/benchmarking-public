# Results vs. 3.10.4

- fork: mdboom
- ref: fast_list_dealloc
- machine: linux-x86_64
- commit hash: ce22895
- commit date: 2025-04-17
- overall geometric mean: 1.467x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.33x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250417-linux-x86_64-mdboom-fast_list_dealloc-3.14.0a7+-ce22895 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 255 ms: 1.37x faster                                                |
| docutils       | 3.30 sec                                               | 2.59 sec: 1.27x faster                                              |
| html5lib       | 88.9 ms                                                | 60.7 ms: 1.46x faster                                               |
| Geometric mean | (ref)                                                  | 1.37x faster                                                        |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250417-linux-x86_64-mdboom-fast_list_dealloc-3.14.0a7+-ce22895 |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 606 ms: 2.92x faster                                                |
| async_tree_none         | 728 ms                                                 | 256 ms: 2.85x faster                                                |
| async_tree_memoization  | 870 ms                                                 | 308 ms: 2.83x faster                                                |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 481 ms: 2.11x faster                                                |
| Geometric mean          | (ref)                                                  | 2.65x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250417-linux-x86_64-mdboom-fast_list_dealloc-3.14.0a7+-ce22895 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 117 ms                                                 | 67.5 ms: 1.73x faster                                               |
| nbody          | 154 ms                                                 | 95.8 ms: 1.60x faster                                               |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.42x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250417-linux-x86_64-mdboom-fast_list_dealloc-3.14.0a7+-ce22895 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 124 ms: 1.52x faster                                                |
| regex_v8       | 27.8 ms                                                | 23.1 ms: 1.20x faster                                               |
| regex_effbot   | 3.63 ms                                                | 3.09 ms: 1.17x faster                                               |
| regex_dna      | 227 ms                                                 | 206 ms: 1.10x faster                                                |
| Geometric mean | (ref)                                                  | 1.24x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250417-linux-x86_64-mdboom-fast_list_dealloc-3.14.0a7+-ce22895 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.97 sec: 1.60x faster                                              |
| pickle_pure_python   | 484 us                                                 | 311 us: 1.56x faster                                                |
| unpickle_pure_python | 331 us                                                 | 216 us: 1.53x faster                                                |
| xml_etree_process    | 79.1 ms                                                | 58.2 ms: 1.36x faster                                               |
| json_dumps           | 14.2 ms                                                | 11.5 ms: 1.23x faster                                               |
| xml_etree_parse      | 168 ms                                                 | 142 ms: 1.19x faster                                                |
| xml_etree_generate   | 99.4 ms                                                | 83.8 ms: 1.19x faster                                               |
| xml_etree_iterparse  | 115 ms                                                 | 99.1 ms: 1.17x faster                                               |
| json_loads           | 31.2 us                                                | 30.0 us: 1.04x faster                                               |
| Geometric mean       | (ref)                                                  | 1.30x faster                                                        |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250417-linux-x86_64-mdboom-fast_list_dealloc-3.14.0a7+-ce22895 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.2 ms: 1.10x faster                                               |
| python_startup_no_site | 5.93 ms                                                | 8.23 ms: 1.39x slower                                               |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250417-linux-x86_64-mdboom-fast_list_dealloc-3.14.0a7+-ce22895 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.4 ms: 1.54x faster                                               |
| genshi_text     | 31.8 ms                                                | 20.8 ms: 1.53x faster                                               |
| mako            | 16.3 ms                                                | 11.5 ms: 1.42x faster                                               |
| genshi_xml      | 66.0 ms                                                | 49.0 ms: 1.35x faster                                               |
| Geometric mean  | (ref)                                                  | 1.46x faster                                                        |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250417-linux-x86_64-mdboom-fast_list_dealloc-3.14.0a7+-ce22895 |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 165 us: 3.30x faster                                                |
| async_tree_io            | 1.77 sec                                               | 606 ms: 2.92x faster                                                |
| async_tree_none          | 728 ms                                                 | 256 ms: 2.85x faster                                                |
| async_tree_memoization   | 870 ms                                                 | 308 ms: 2.83x faster                                                |
| generators               | 80.1 ms                                                | 29.3 ms: 2.74x faster                                               |
| deltablue                | 7.91 ms                                                | 3.31 ms: 2.39x faster                                               |
| mdp                      | 2.85 sec                                               | 1.20 sec: 2.37x faster                                              |
| go                       | 240 ms                                                 | 110 ms: 2.18x faster                                                |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 481 ms: 2.11x faster                                                |
| deepcopy_memo            | 58.5 us                                                | 28.3 us: 2.07x faster                                               |
| chaos                    | 115 ms                                                 | 57.0 ms: 2.02x faster                                               |
| logging_silent           | 190 ns                                                 | 94.2 ns: 2.01x faster                                               |
| pylint                   | 551 ms                                                 | 278 ms: 1.99x faster                                                |
| richards_super           | 94.7 ms                                                | 49.4 ms: 1.92x faster                                               |
| raytrace                 | 507 ms                                                 | 267 ms: 1.90x faster                                                |
| deepcopy                 | 479 us                                                 | 253 us: 1.89x faster                                                |
| scimark_sor              | 220 ms                                                 | 117 ms: 1.87x faster                                                |
| richards                 | 79.3 ms                                                | 42.9 ms: 1.85x faster                                               |
| scimark_monte_carlo      | 118 ms                                                 | 66.3 ms: 1.78x faster                                               |
| comprehensions           | 28.8 us                                                | 16.5 us: 1.75x faster                                               |
| crypto_pyaes             | 128 ms                                                 | 73.4 ms: 1.74x faster                                               |
| float                    | 117 ms                                                 | 67.5 ms: 1.73x faster                                               |
| hexiom                   | 10.4 ms                                                | 6.13 ms: 1.70x faster                                               |
| pyflate                  | 716 ms                                                 | 425 ms: 1.68x faster                                                |
| nbody                    | 154 ms                                                 | 95.8 ms: 1.60x faster                                               |
| spectral_norm            | 170 ms                                                 | 106 ms: 1.60x faster                                                |
| tomli_loads              | 3.14 sec                                               | 1.97 sec: 1.60x faster                                              |
| pickle_pure_python       | 484 us                                                 | 311 us: 1.56x faster                                                |
| deepcopy_reduce          | 4.17 us                                                | 2.69 us: 1.55x faster                                               |
| django_template          | 48.2 ms                                                | 31.4 ms: 1.54x faster                                               |
| unpickle_pure_python     | 331 us                                                 | 216 us: 1.53x faster                                                |
| genshi_text              | 31.8 ms                                                | 20.8 ms: 1.53x faster                                               |
| regex_compile            | 188 ms                                                 | 124 ms: 1.52x faster                                                |
| logging_simple           | 8.30 us                                                | 5.48 us: 1.51x faster                                               |
| scimark_lu               | 176 ms                                                 | 118 ms: 1.49x faster                                                |
| coroutines               | 35.1 ms                                                | 23.6 ms: 1.48x faster                                               |
| logging_format           | 9.09 us                                                | 6.13 us: 1.48x faster                                               |
| html5lib                 | 88.9 ms                                                | 60.7 ms: 1.46x faster                                               |
| pprint_pformat           | 2.10 sec                                               | 1.46 sec: 1.44x faster                                              |
| mako                     | 16.3 ms                                                | 11.5 ms: 1.42x faster                                               |
| pprint_safe_repr         | 1.02 sec                                               | 716 ms: 1.42x faster                                                |
| dulwich_log              | 84.3 ms                                                | 59.6 ms: 1.41x faster                                               |
| pycparser                | 1.58 sec                                               | 1.12 sec: 1.40x faster                                              |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.9 ms: 1.38x faster                                               |
| 2to3                     | 348 ms                                                 | 255 ms: 1.37x faster                                                |
| xml_etree_process        | 79.1 ms                                                | 58.2 ms: 1.36x faster                                               |
| sympy_integrate          | 25.8 ms                                                | 19.0 ms: 1.35x faster                                               |
| genshi_xml               | 66.0 ms                                                | 49.0 ms: 1.35x faster                                               |
| sympy_sum                | 196 ms                                                 | 148 ms: 1.33x faster                                                |
| nqueens                  | 106 ms                                                 | 80.4 ms: 1.32x faster                                               |
| sqlalchemy_declarative   | 172 ms                                                 | 132 ms: 1.31x faster                                                |
| fannkuch                 | 532 ms                                                 | 406 ms: 1.31x faster                                                |
| scimark_fft              | 466 ms                                                 | 358 ms: 1.30x faster                                                |
| sympy_str                | 346 ms                                                 | 266 ms: 1.30x faster                                                |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 5.01 ms: 1.29x faster                                               |
| docutils                 | 3.30 sec                                               | 2.59 sec: 1.27x faster                                              |
| sympy_expand             | 566 ms                                                 | 453 ms: 1.25x faster                                                |
| json_dumps               | 14.2 ms                                                | 11.5 ms: 1.23x faster                                               |
| pathlib                  | 20.5 ms                                                | 16.9 ms: 1.21x faster                                               |
| regex_v8                 | 27.8 ms                                                | 23.1 ms: 1.20x faster                                               |
| xml_etree_parse          | 168 ms                                                 | 142 ms: 1.19x faster                                                |
| xml_etree_generate       | 99.4 ms                                                | 83.8 ms: 1.19x faster                                               |
| regex_effbot             | 3.63 ms                                                | 3.09 ms: 1.17x faster                                               |
| xml_etree_iterparse      | 115 ms                                                 | 99.1 ms: 1.17x faster                                               |
| meteor_contest           | 120 ms                                                 | 104 ms: 1.15x faster                                                |
| async_generators         | 444 ms                                                 | 388 ms: 1.14x faster                                                |
| bench_thread_pool        | 986 us                                                 | 888 us: 1.11x faster                                                |
| python_startup           | 14.6 ms                                                | 13.2 ms: 1.10x faster                                               |
| regex_dna                | 227 ms                                                 | 206 ms: 1.10x faster                                                |
| sqlite_synth             | 3.02 us                                                | 2.80 us: 1.08x faster                                               |
| json                     | 5.69 ms                                                | 5.38 ms: 1.06x faster                                               |
| json_loads               | 31.2 us                                                | 30.0 us: 1.04x faster                                               |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                                |
| asyncio_websockets       | 559 ms                                                 | 552 ms: 1.01x faster                                                |
| telco                    | 7.27 ms                                                | 7.70 ms: 1.06x slower                                               |
| coverage                 | 79.4 ms                                                | 88.6 ms: 1.11x slower                                               |
| gc_traversal             | 3.62 ms                                                | 4.80 ms: 1.33x slower                                               |
| python_startup_no_site   | 5.93 ms                                                | 8.23 ms: 1.39x slower                                               |
| create_gc_cycles         | 1.62 ms                                                | 2.47 ms: 1.52x slower                                               |
| bench_mp_pool            | 24.0 ms                                                | 82.1 ms: 3.42x slower                                               |
| Geometric mean           | (ref)                                                  | 1.44x faster                                                        |
Ignored benchmarks (21) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, thrift, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250417-3.14.0a7+-ce22895/bm-20250417-linux-x86_64-mdboom-fast_list_dealloc-3.14.0a7+-ce22895.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.467x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.36x
- 95% likely to have a speedup of 1.36x
- 99% likely to have a speedup of 1.33x

# Memory
- memory change: 1.28x