# Results vs. 3.12.0

- fork: iritkatriel
- ref: cmq_mdboom
- machine: linux-x86_64
- commit hash: 6cacd2b
- commit date: 2024-12-04
- overall geometric mean: 1.079x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241204-linux-x86_64-iritkatriel-cmq_mdboom-3.14.0a0-6cacd2b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 255 ms: 1.08x faster                                             |
| docutils       | 2.77 sec                                               | 2.65 sec: 1.04x faster                                           |
| tornado_http   | 103 ms                                                 | 90.7 ms: 1.13x faster                                            |
| Geometric mean | (ref)                                                  | 1.08x faster                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241204-linux-x86_64-iritkatriel-cmq_mdboom-3.14.0a0-6cacd2b |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 388 ms: 1.48x faster                                             |
| async_tree_none_tg         | 450 ms                                                 | 307 ms: 1.46x faster                                             |
| async_tree_none            | 472 ms                                                 | 328 ms: 1.44x faster                                             |
| async_tree_memoization     | 578 ms                                                 | 425 ms: 1.36x faster                                             |
| async_tree_io_tg           | 1.18 sec                                               | 885 ms: 1.34x faster                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 554 ms: 1.31x faster                                             |
| async_tree_io              | 1.16 sec                                               | 891 ms: 1.30x faster                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 562 ms: 1.29x faster                                             |
| Geometric mean             | (ref)                                                  | 1.37x faster                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241204-linux-x86_64-iritkatriel-cmq_mdboom-3.14.0a0-6cacd2b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 84.7 ms                                                | 75.3 ms: 1.13x faster                                            |
| nbody          | 97.0 ms                                                | 89.4 ms: 1.08x faster                                            |
| Geometric mean | (ref)                                                  | 1.07x faster                                                     |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241204-linux-x86_64-iritkatriel-cmq_mdboom-3.14.0a0-6cacd2b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                             |
| regex_dna      | 212 ms                                                 | 220 ms: 1.04x slower                                             |
| regex_v8       | 23.1 ms                                                | 24.7 ms: 1.07x slower                                            |
| Geometric mean | (ref)                                                  | 1.01x faster                                                     |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241204-linux-x86_64-iritkatriel-cmq_mdboom-3.14.0a0-6cacd2b |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.08 sec: 1.12x faster                                           |
| unpickle_pure_python | 230 us                                                 | 214 us: 1.07x faster                                             |
| pickle_pure_python   | 324 us                                                 | 305 us: 1.06x faster                                             |
| xml_etree_process    | 61.7 ms                                                | 59.0 ms: 1.05x faster                                            |
| json_loads           | 28.5 us                                                | 27.3 us: 1.05x faster                                            |
| xml_etree_generate   | 89.2 ms                                                | 85.7 ms: 1.04x faster                                            |
| xml_etree_iterparse  | 107 ms                                                 | 105 ms: 1.02x faster                                             |
| json_dumps           | 10.4 ms                                                | 10.3 ms: 1.01x faster                                            |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                     |

Benchmark hidden because not significant (1): xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241204-linux-x86_64-iritkatriel-cmq_mdboom-3.14.0a0-6cacd2b |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.97 ms: 1.00x slower                                            |
| python_startup         | 9.55 ms                                                | 12.6 ms: 1.32x slower                                            |
| Geometric mean         | (ref)                                                  | 1.15x slower                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241204-linux-x86_64-iritkatriel-cmq_mdboom-3.14.0a0-6cacd2b |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.7 ms: 1.09x faster                                            |
| mako            | 11.9 ms                                                | 11.1 ms: 1.07x faster                                            |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241204-linux-x86_64-iritkatriel-cmq_mdboom-3.14.0a0-6cacd2b |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 575 ms                                                 | 388 ms: 1.48x faster                                             |
| async_tree_none_tg         | 450 ms                                                 | 307 ms: 1.46x faster                                             |
| async_tree_none            | 472 ms                                                 | 328 ms: 1.44x faster                                             |
| deepcopy                   | 371 us                                                 | 261 us: 1.42x faster                                             |
| deepcopy_memo              | 40.7 us                                                | 29.4 us: 1.39x faster                                            |
| async_tree_memoization     | 578 ms                                                 | 425 ms: 1.36x faster                                             |
| async_tree_io_tg           | 1.18 sec                                               | 885 ms: 1.34x faster                                             |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 554 ms: 1.31x faster                                             |
| async_tree_io              | 1.16 sec                                               | 891 ms: 1.30x faster                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 562 ms: 1.29x faster                                             |
| deepcopy_reduce            | 3.35 us                                                | 2.74 us: 1.22x faster                                            |
| pathlib                    | 19.3 ms                                                | 16.0 ms: 1.21x faster                                            |
| go                         | 139 ms                                                 | 117 ms: 1.19x faster                                             |
| chaos                      | 67.0 ms                                                | 57.0 ms: 1.17x faster                                            |
| deltablue                  | 3.72 ms                                                | 3.19 ms: 1.17x faster                                            |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                             |
| sympy_sum                  | 169 ms                                                 | 146 ms: 1.16x faster                                             |
| logging_format             | 7.23 us                                                | 6.27 us: 1.15x faster                                            |
| sqlalchemy_declarative     | 147 ms                                                 | 128 ms: 1.15x faster                                             |
| logging_simple             | 6.46 us                                                | 5.68 us: 1.14x faster                                            |
| crypto_pyaes               | 81.9 ms                                                | 72.0 ms: 1.14x faster                                            |
| tornado_http               | 103 ms                                                 | 90.7 ms: 1.13x faster                                            |
| sympy_str                  | 300 ms                                                 | 265 ms: 1.13x faster                                             |
| float                      | 84.7 ms                                                | 75.3 ms: 1.13x faster                                            |
| tomli_loads                | 2.33 sec                                               | 2.08 sec: 1.12x faster                                           |
| scimark_monte_carlo        | 75.1 ms                                                | 67.7 ms: 1.11x faster                                            |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.9 ms: 1.10x faster                                            |
| generators                 | 31.2 ms                                                | 28.4 ms: 1.10x faster                                            |
| django_template            | 34.6 ms                                                | 31.7 ms: 1.09x faster                                            |
| nbody                      | 97.0 ms                                                | 89.4 ms: 1.08x faster                                            |
| sympy_integrate            | 21.4 ms                                                | 19.8 ms: 1.08x faster                                            |
| 2to3                       | 274 ms                                                 | 255 ms: 1.08x faster                                             |
| pprint_safe_repr           | 776 ms                                                 | 720 ms: 1.08x faster                                             |
| unpickle_pure_python       | 230 us                                                 | 214 us: 1.07x faster                                             |
| sqlglot_transpile          | 1.68 ms                                                | 1.57 ms: 1.07x faster                                            |
| mako                       | 11.9 ms                                                | 11.1 ms: 1.07x faster                                            |
| pprint_pformat             | 1.57 sec                                               | 1.47 sec: 1.07x faster                                           |
| scimark_fft                | 382 ms                                                 | 358 ms: 1.07x faster                                             |
| pickle_pure_python         | 324 us                                                 | 305 us: 1.06x faster                                             |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.06x faster                                            |
| json                       | 5.26 ms                                                | 4.96 ms: 1.06x faster                                            |
| dulwich_log                | 68.5 ms                                                | 64.6 ms: 1.06x faster                                            |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                             |
| sympy_expand               | 478 ms                                                 | 453 ms: 1.06x faster                                             |
| async_generators           | 463 ms                                                 | 439 ms: 1.05x faster                                             |
| scimark_lu                 | 118 ms                                                 | 112 ms: 1.05x faster                                             |
| pycparser                  | 1.18 sec                                               | 1.12 sec: 1.05x faster                                           |
| xml_etree_process          | 61.7 ms                                                | 59.0 ms: 1.05x faster                                            |
| nqueens                    | 83.3 ms                                                | 79.7 ms: 1.05x faster                                            |
| json_loads                 | 28.5 us                                                | 27.3 us: 1.05x faster                                            |
| docutils                   | 2.77 sec                                               | 2.65 sec: 1.04x faster                                           |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.85 ms: 1.04x faster                                            |
| xml_etree_generate         | 89.2 ms                                                | 85.7 ms: 1.04x faster                                            |
| hexiom                     | 6.41 ms                                                | 6.18 ms: 1.04x faster                                            |
| sqlglot_normalize          | 110 ms                                                 | 106 ms: 1.04x faster                                             |
| scimark_sor                | 129 ms                                                 | 126 ms: 1.03x faster                                             |
| logging_silent             | 104 ns                                                 | 102 ns: 1.03x faster                                             |
| sqlglot_optimize           | 54.8 ms                                                | 53.5 ms: 1.02x faster                                            |
| xml_etree_iterparse        | 107 ms                                                 | 105 ms: 1.02x faster                                             |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.02x faster                                             |
| pyflate                    | 482 ms                                                 | 474 ms: 1.02x faster                                             |
| fannkuch                   | 417 ms                                                 | 410 ms: 1.02x faster                                             |
| json_dumps                 | 10.4 ms                                                | 10.3 ms: 1.01x faster                                            |
| sqlite_synth               | 2.83 us                                                | 2.81 us: 1.01x faster                                            |
| python_startup_no_site     | 6.94 ms                                                | 6.97 ms: 1.00x slower                                            |
| richards_super             | 51.5 ms                                                | 51.8 ms: 1.01x slower                                            |
| coroutines                 | 23.2 ms                                                | 23.4 ms: 1.01x slower                                            |
| asyncio_websockets         | 551 ms                                                 | 557 ms: 1.01x slower                                             |
| bench_thread_pool          | 842 us                                                 | 860 us: 1.02x slower                                             |
| mdp                        | 2.63 sec                                               | 2.70 sec: 1.03x slower                                           |
| regex_dna                  | 212 ms                                                 | 220 ms: 1.04x slower                                             |
| regex_v8                   | 23.1 ms                                                | 24.7 ms: 1.07x slower                                            |
| telco                      | 7.10 ms                                                | 8.06 ms: 1.14x slower                                            |
| coverage                   | 72.7 ms                                                | 84.1 ms: 1.16x slower                                            |
| gc_traversal               | 3.79 ms                                                | 4.45 ms: 1.17x slower                                            |
| python_startup             | 9.55 ms                                                | 12.6 ms: 1.32x slower                                            |
| create_gc_cycles           | 1.48 ms                                                | 2.61 ms: 1.77x slower                                            |
| bench_mp_pool              | 24.0 ms                                                | 77.9 ms: 3.25x slower                                            |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                     |

Benchmark hidden because not significant (5): xml_etree_parse, richards, pidigits, regex_effbot, typing_runtime_protocols
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, raytrace, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241204-3.14.0a0-6cacd2b/bm-20241204-linux-x86_64-iritkatriel-cmq_mdboom-3.14.0a0-6cacd2b.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.079x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.08x