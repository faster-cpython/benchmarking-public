# Results vs. 3.10.4

- fork: mdboom
- ref: dict_lookup
- machine: linux-x86_64
- commit hash: 8c2f03e
- commit date: 2025-03-24
- overall geometric mean: 1.433x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.30x faster
- Memory change: 1.28x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250324-linux-x86_64-mdboom-dict_lookup-3.14.0a6+-8c2f03e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 348 ms                                                 | 258 ms: 1.35x faster                                          |
| docutils       | 3.30 sec                                               | 2.60 sec: 1.27x faster                                        |
| html5lib       | 88.9 ms                                                | 63.4 ms: 1.40x faster                                         |
| Geometric mean | (ref)                                                  | 1.34x faster                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250324-linux-x86_64-mdboom-dict_lookup-3.14.0a6+-8c2f03e |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_io           | 1.77 sec                                               | 615 ms: 2.87x faster                                          |
| async_tree_none         | 728 ms                                                 | 259 ms: 2.82x faster                                          |
| async_tree_memoization  | 870 ms                                                 | 313 ms: 2.78x faster                                          |
| async_tree_cpu_io_mixed | 1.02 sec                                               | 487 ms: 2.08x faster                                          |
| Geometric mean          | (ref)                                                  | 2.62x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250324-linux-x86_64-mdboom-dict_lookup-3.14.0a6+-8c2f03e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 117 ms                                                 | 71.1 ms: 1.65x faster                                         |
| nbody          | 154 ms                                                 | 101 ms: 1.52x faster                                          |
| pidigits       | 191 ms                                                 | 187 ms: 1.02x faster                                          |
| Geometric mean | (ref)                                                  | 1.37x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250324-linux-x86_64-mdboom-dict_lookup-3.14.0a6+-8c2f03e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 188 ms                                                 | 127 ms: 1.48x faster                                          |
| regex_v8       | 27.8 ms                                                | 23.6 ms: 1.18x faster                                         |
| regex_effbot   | 3.63 ms                                                | 3.20 ms: 1.13x faster                                         |
| regex_dna      | 227 ms                                                 | 216 ms: 1.05x faster                                          |
| Geometric mean | (ref)                                                  | 1.20x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250324-linux-x86_64-mdboom-dict_lookup-3.14.0a6+-8c2f03e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 3.14 sec                                               | 1.99 sec: 1.57x faster                                        |
| pickle_pure_python   | 484 us                                                 | 316 us: 1.53x faster                                          |
| unpickle_pure_python | 331 us                                                 | 221 us: 1.49x faster                                          |
| xml_etree_process    | 79.1 ms                                                | 59.2 ms: 1.34x faster                                         |
| json_dumps           | 14.2 ms                                                | 11.6 ms: 1.22x faster                                         |
| xml_etree_parse      | 168 ms                                                 | 140 ms: 1.20x faster                                          |
| xml_etree_generate   | 99.4 ms                                                | 84.8 ms: 1.17x faster                                         |
| xml_etree_iterparse  | 115 ms                                                 | 98.7 ms: 1.17x faster                                         |
| json_loads           | 31.2 us                                                | 29.9 us: 1.04x faster                                         |
| Geometric mean       | (ref)                                                  | 1.29x faster                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250324-linux-x86_64-mdboom-dict_lookup-3.14.0a6+-8c2f03e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 14.6 ms                                                | 13.1 ms: 1.11x faster                                         |
| python_startup_no_site | 5.93 ms                                                | 8.20 ms: 1.38x slower                                         |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250324-linux-x86_64-mdboom-dict_lookup-3.14.0a6+-8c2f03e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| django_template | 48.2 ms                                                | 31.8 ms: 1.51x faster                                         |
| genshi_text     | 31.8 ms                                                | 21.4 ms: 1.49x faster                                         |
| mako            | 16.3 ms                                                | 11.5 ms: 1.43x faster                                         |
| genshi_xml      | 66.0 ms                                                | 49.0 ms: 1.35x faster                                         |
| Geometric mean  | (ref)                                                  | 1.44x faster                                                  |

All benchmarks:
===============

| Benchmark                | bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120 | bm-20250324-linux-x86_64-mdboom-dict_lookup-3.14.0a6+-8c2f03e |
|--------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| typing_runtime_protocols | 544 us                                                 | 160 us: 3.41x faster                                          |
| async_tree_io            | 1.77 sec                                               | 615 ms: 2.87x faster                                          |
| async_tree_none          | 728 ms                                                 | 259 ms: 2.82x faster                                          |
| generators               | 80.1 ms                                                | 28.7 ms: 2.79x faster                                         |
| async_tree_memoization   | 870 ms                                                 | 313 ms: 2.78x faster                                          |
| deltablue                | 7.91 ms                                                | 3.13 ms: 2.53x faster                                         |
| go                       | 240 ms                                                 | 115 ms: 2.09x faster                                          |
| async_tree_cpu_io_mixed  | 1.02 sec                                               | 487 ms: 2.08x faster                                          |
| pylint                   | 551 ms                                                 | 278 ms: 1.99x faster                                          |
| chaos                    | 115 ms                                                 | 59.0 ms: 1.96x faster                                         |
| deepcopy_memo            | 58.5 us                                                | 29.9 us: 1.95x faster                                         |
| logging_silent           | 190 ns                                                 | 98.4 ns: 1.93x faster                                         |
| richards_super           | 94.7 ms                                                | 49.4 ms: 1.92x faster                                         |
| raytrace                 | 507 ms                                                 | 266 ms: 1.90x faster                                          |
| deepcopy                 | 479 us                                                 | 261 us: 1.83x faster                                          |
| richards                 | 79.3 ms                                                | 43.3 ms: 1.83x faster                                         |
| scimark_sor              | 220 ms                                                 | 120 ms: 1.83x faster                                          |
| scimark_monte_carlo      | 118 ms                                                 | 68.4 ms: 1.73x faster                                         |
| comprehensions           | 28.8 us                                                | 16.8 us: 1.71x faster                                         |
| spectral_norm            | 170 ms                                                 | 99.4 ms: 1.71x faster                                         |
| crypto_pyaes             | 128 ms                                                 | 76.7 ms: 1.67x faster                                         |
| hexiom                   | 10.4 ms                                                | 6.24 ms: 1.67x faster                                         |
| float                    | 117 ms                                                 | 71.1 ms: 1.65x faster                                         |
| pyflate                  | 716 ms                                                 | 450 ms: 1.59x faster                                          |
| tomli_loads              | 3.14 sec                                               | 1.99 sec: 1.57x faster                                        |
| deepcopy_reduce          | 4.17 us                                                | 2.71 us: 1.54x faster                                         |
| pickle_pure_python       | 484 us                                                 | 316 us: 1.53x faster                                          |
| nbody                    | 154 ms                                                 | 101 ms: 1.52x faster                                          |
| django_template          | 48.2 ms                                                | 31.8 ms: 1.51x faster                                         |
| logging_simple           | 8.30 us                                                | 5.54 us: 1.50x faster                                         |
| unpickle_pure_python     | 331 us                                                 | 221 us: 1.49x faster                                          |
| genshi_text              | 31.8 ms                                                | 21.4 ms: 1.49x faster                                         |
| regex_compile            | 188 ms                                                 | 127 ms: 1.48x faster                                          |
| scimark_lu               | 176 ms                                                 | 119 ms: 1.48x faster                                          |
| logging_format           | 9.09 us                                                | 6.16 us: 1.48x faster                                         |
| coroutines               | 35.1 ms                                                | 23.9 ms: 1.47x faster                                         |
| dulwich_log              | 84.3 ms                                                | 59.0 ms: 1.43x faster                                         |
| mako                     | 16.3 ms                                                | 11.5 ms: 1.43x faster                                         |
| pprint_pformat           | 2.10 sec                                               | 1.49 sec: 1.41x faster                                        |
| html5lib                 | 88.9 ms                                                | 63.4 ms: 1.40x faster                                         |
| thrift                   | 1.07 ms                                                | 765 us: 1.40x faster                                          |
| sqlalchemy_imperative    | 23.3 ms                                                | 16.7 ms: 1.40x faster                                         |
| pprint_safe_repr         | 1.02 sec                                               | 731 ms: 1.39x faster                                          |
| pycparser                | 1.58 sec                                               | 1.14 sec: 1.38x faster                                        |
| 2to3                     | 348 ms                                                 | 258 ms: 1.35x faster                                          |
| genshi_xml               | 66.0 ms                                                | 49.0 ms: 1.35x faster                                         |
| scimark_sparse_mat_mult  | 6.47 ms                                                | 4.82 ms: 1.34x faster                                         |
| xml_etree_process        | 79.1 ms                                                | 59.2 ms: 1.34x faster                                         |
| sqlalchemy_declarative   | 172 ms                                                 | 131 ms: 1.32x faster                                          |
| scimark_fft              | 466 ms                                                 | 354 ms: 1.31x faster                                          |
| sympy_integrate          | 25.8 ms                                                | 19.6 ms: 1.31x faster                                         |
| sympy_sum                | 196 ms                                                 | 150 ms: 1.31x faster                                          |
| sympy_str                | 346 ms                                                 | 268 ms: 1.29x faster                                          |
| docutils                 | 3.30 sec                                               | 2.60 sec: 1.27x faster                                        |
| nqueens                  | 106 ms                                                 | 85.3 ms: 1.24x faster                                         |
| sympy_expand             | 566 ms                                                 | 457 ms: 1.24x faster                                          |
| fannkuch                 | 532 ms                                                 | 434 ms: 1.22x faster                                          |
| json_dumps               | 14.2 ms                                                | 11.6 ms: 1.22x faster                                         |
| xml_etree_parse          | 168 ms                                                 | 140 ms: 1.20x faster                                          |
| pathlib                  | 20.5 ms                                                | 17.0 ms: 1.20x faster                                         |
| regex_v8                 | 27.8 ms                                                | 23.6 ms: 1.18x faster                                         |
| xml_etree_generate       | 99.4 ms                                                | 84.8 ms: 1.17x faster                                         |
| xml_etree_iterparse      | 115 ms                                                 | 98.7 ms: 1.17x faster                                         |
| mdp                      | 2.85 sec                                               | 2.50 sec: 1.14x faster                                        |
| regex_effbot             | 3.63 ms                                                | 3.20 ms: 1.13x faster                                         |
| meteor_contest           | 120 ms                                                 | 106 ms: 1.13x faster                                          |
| async_generators         | 444 ms                                                 | 392 ms: 1.13x faster                                          |
| bench_thread_pool        | 986 us                                                 | 872 us: 1.13x faster                                          |
| python_startup           | 14.6 ms                                                | 13.1 ms: 1.11x faster                                         |
| sqlite_synth             | 3.02 us                                                | 2.75 us: 1.10x faster                                         |
| json                     | 5.69 ms                                                | 5.37 ms: 1.06x faster                                         |
| regex_dna                | 227 ms                                                 | 216 ms: 1.05x faster                                          |
| json_loads               | 31.2 us                                                | 29.9 us: 1.04x faster                                         |
| pidigits                 | 191 ms                                                 | 187 ms: 1.02x faster                                          |
| asyncio_websockets       | 559 ms                                                 | 553 ms: 1.01x faster                                          |
| telco                    | 7.27 ms                                                | 7.93 ms: 1.09x slower                                         |
| coverage                 | 79.4 ms                                                | 93.5 ms: 1.18x slower                                         |
| python_startup_no_site   | 5.93 ms                                                | 8.20 ms: 1.38x slower                                         |
| gc_traversal             | 3.62 ms                                                | 5.06 ms: 1.40x slower                                         |
| create_gc_cycles         | 1.62 ms                                                | 2.49 ms: 1.54x slower                                         |
| bench_mp_pool            | 24.0 ms                                                | 83.1 ms: 3.46x slower                                         |
| Geometric mean           | (ref)                                                  | 1.41x faster                                                  |
Ignored benchmarks (20) of results/bm-20220323-3.10.4-9d38120/bm-20220323-linux-x86_64-python-v3.10.4-3.10.4-9d38120.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250324-3.14.0a6+-8c2f03e/bm-20250324-linux-x86_64-mdboom-dict_lookup-3.14.0a6+-8c2f03e.json: async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.433x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.34x
- 95% likely to have a speedup of 1.33x
- 99% likely to have a speedup of 1.30x

# Memory
- memory change: 1.28x