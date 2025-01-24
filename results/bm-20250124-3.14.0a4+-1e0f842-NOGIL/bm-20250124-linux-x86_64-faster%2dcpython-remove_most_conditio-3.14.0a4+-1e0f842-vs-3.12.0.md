# Results vs. 3.12.0

- fork: faster-cpython
- ref: remove_most_conditio
- machine: linux-x86_64
- commit hash: 1e0f842
- commit date: 2025-01-24
- overall geometric mean: 1.041x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.02x slower
- Memory change: 1.31x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 311 ms: 1.13x slower                                                             |
| docutils       | 2.77 sec                                               | 2.84 sec: 1.03x slower                                                           |
| Geometric mean | (ref)                                                  | 1.08x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 556 ms: 2.13x faster                                                             |
| async_tree_io              | 1.16 sec                                               | 607 ms: 1.90x faster                                                             |
| async_tree_none_tg         | 450 ms                                                 | 245 ms: 1.83x faster                                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 327 ms: 1.76x faster                                                             |
| async_tree_none            | 472 ms                                                 | 289 ms: 1.63x faster                                                             |
| async_tree_memoization     | 578 ms                                                 | 368 ms: 1.57x faster                                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 480 ms: 1.51x faster                                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 527 ms: 1.38x faster                                                             |
| Geometric mean             | (ref)                                                  | 1.70x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 79.9 ms: 1.06x faster                                                            |
| pidigits       | 187 ms                                                 | 190 ms: 1.02x slower                                                             |
| nbody          | 97.0 ms                                                | 147 ms: 1.51x slower                                                             |
| Geometric mean | (ref)                                                  | 1.13x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.28 ms: 1.10x faster                                                            |
| regex_compile  | 148 ms                                                 | 151 ms: 1.02x slower                                                             |
| regex_dna      | 212 ms                                                 | 218 ms: 1.03x slower                                                             |
| regex_v8       | 23.1 ms                                                | 24.9 ms: 1.08x slower                                                            |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 107 ms                                                 | 95.3 ms: 1.12x faster                                                            |
| xml_etree_parse      | 159 ms                                                 | 148 ms: 1.08x faster                                                             |
| tomli_loads          | 2.33 sec                                               | 2.44 sec: 1.05x slower                                                           |
| xml_etree_generate   | 89.2 ms                                                | 96.2 ms: 1.08x slower                                                            |
| json_loads           | 28.5 us                                                | 31.6 us: 1.11x slower                                                            |
| xml_etree_process    | 61.7 ms                                                | 68.7 ms: 1.11x slower                                                            |
| unpickle_pure_python | 230 us                                                 | 258 us: 1.12x slower                                                             |
| pickle_pure_python   | 324 us                                                 | 374 us: 1.15x slower                                                             |
| json_dumps           | 10.4 ms                                                | 12.7 ms: 1.23x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.07x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 9.38 ms: 1.35x slower                                                            |
| python_startup         | 9.55 ms                                                | 15.1 ms: 1.58x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.46x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 41.7 ms: 1.20x slower                                                            |
| mako            | 11.9 ms                                                | 16.8 ms: 1.41x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.31x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 556 ms: 2.13x faster                                                             |
| async_tree_io              | 1.16 sec                                               | 607 ms: 1.90x faster                                                             |
| async_tree_none_tg         | 450 ms                                                 | 245 ms: 1.83x faster                                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 327 ms: 1.76x faster                                                             |
| async_tree_none            | 472 ms                                                 | 289 ms: 1.63x faster                                                             |
| async_tree_memoization     | 578 ms                                                 | 368 ms: 1.57x faster                                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 480 ms: 1.51x faster                                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 527 ms: 1.38x faster                                                             |
| deepcopy                   | 371 us                                                 | 313 us: 1.19x faster                                                             |
| pathlib                    | 19.3 ms                                                | 16.5 ms: 1.17x faster                                                            |
| xml_etree_iterparse        | 107 ms                                                 | 95.3 ms: 1.12x faster                                                            |
| regex_effbot               | 3.61 ms                                                | 3.28 ms: 1.10x faster                                                            |
| xml_etree_parse            | 159 ms                                                 | 148 ms: 1.08x faster                                                             |
| float                      | 84.7 ms                                                | 79.9 ms: 1.06x faster                                                            |
| async_generators           | 463 ms                                                 | 442 ms: 1.05x faster                                                             |
| sqlite_synth               | 2.83 us                                                | 2.71 us: 1.05x faster                                                            |
| comprehensions             | 21.8 us                                                | 21.1 us: 1.03x faster                                                            |
| deepcopy_memo              | 40.7 us                                                | 39.8 us: 1.02x faster                                                            |
| deepcopy_reduce            | 3.35 us                                                | 3.31 us: 1.01x faster                                                            |
| pycparser                  | 1.18 sec                                               | 1.19 sec: 1.01x slower                                                           |
| pidigits                   | 187 ms                                                 | 190 ms: 1.02x slower                                                             |
| dulwich_log                | 68.5 ms                                                | 69.7 ms: 1.02x slower                                                            |
| regex_compile              | 148 ms                                                 | 151 ms: 1.02x slower                                                             |
| generators                 | 31.2 ms                                                | 31.8 ms: 1.02x slower                                                            |
| spectral_norm              | 115 ms                                                 | 117 ms: 1.02x slower                                                             |
| regex_dna                  | 212 ms                                                 | 218 ms: 1.03x slower                                                             |
| docutils                   | 2.77 sec                                               | 2.84 sec: 1.03x slower                                                           |
| go                         | 139 ms                                                 | 144 ms: 1.03x slower                                                             |
| logging_format             | 7.23 us                                                | 7.52 us: 1.04x slower                                                            |
| logging_simple             | 6.46 us                                                | 6.74 us: 1.04x slower                                                            |
| tomli_loads                | 2.33 sec                                               | 2.44 sec: 1.05x slower                                                           |
| mdp                        | 2.63 sec                                               | 2.76 sec: 1.05x slower                                                           |
| json                       | 5.26 ms                                                | 5.56 ms: 1.06x slower                                                            |
| sympy_sum                  | 169 ms                                                 | 179 ms: 1.06x slower                                                             |
| sympy_str                  | 300 ms                                                 | 322 ms: 1.08x slower                                                             |
| regex_v8                   | 23.1 ms                                                | 24.9 ms: 1.08x slower                                                            |
| xml_etree_generate         | 89.2 ms                                                | 96.2 ms: 1.08x slower                                                            |
| sqlalchemy_imperative      | 18.7 ms                                                | 20.7 ms: 1.11x slower                                                            |
| sqlglot_normalize          | 110 ms                                                 | 122 ms: 1.11x slower                                                             |
| json_loads                 | 28.5 us                                                | 31.6 us: 1.11x slower                                                            |
| scimark_sor                | 129 ms                                                 | 143 ms: 1.11x slower                                                             |
| pprint_safe_repr           | 776 ms                                                 | 861 ms: 1.11x slower                                                             |
| xml_etree_process          | 61.7 ms                                                | 68.7 ms: 1.11x slower                                                            |
| crypto_pyaes               | 81.9 ms                                                | 91.1 ms: 1.11x slower                                                            |
| chaos                      | 67.0 ms                                                | 74.6 ms: 1.11x slower                                                            |
| sqlglot_optimize           | 54.8 ms                                                | 61.1 ms: 1.11x slower                                                            |
| sympy_expand               | 478 ms                                                 | 533 ms: 1.12x slower                                                             |
| scimark_fft                | 382 ms                                                 | 426 ms: 1.12x slower                                                             |
| coroutines                 | 23.2 ms                                                | 25.9 ms: 1.12x slower                                                            |
| unpickle_pure_python       | 230 us                                                 | 258 us: 1.12x slower                                                             |
| sympy_integrate            | 21.4 ms                                                | 24.1 ms: 1.12x slower                                                            |
| sqlalchemy_declarative     | 147 ms                                                 | 165 ms: 1.13x slower                                                             |
| pyflate                    | 482 ms                                                 | 545 ms: 1.13x slower                                                             |
| pprint_pformat             | 1.57 sec                                               | 1.77 sec: 1.13x slower                                                           |
| 2to3                       | 274 ms                                                 | 311 ms: 1.13x slower                                                             |
| logging_silent             | 104 ns                                                 | 119 ns: 1.14x slower                                                             |
| raytrace                   | 312 ms                                                 | 357 ms: 1.14x slower                                                             |
| create_gc_cycles           | 1.48 ms                                                | 1.70 ms: 1.15x slower                                                            |
| pickle_pure_python         | 324 us                                                 | 374 us: 1.15x slower                                                             |
| sqlglot_parse              | 1.36 ms                                                | 1.58 ms: 1.16x slower                                                            |
| scimark_monte_carlo        | 75.1 ms                                                | 87.8 ms: 1.17x slower                                                            |
| sqlglot_transpile          | 1.68 ms                                                | 1.98 ms: 1.18x slower                                                            |
| meteor_contest             | 112 ms                                                 | 134 ms: 1.19x slower                                                             |
| richards                   | 45.8 ms                                                | 54.6 ms: 1.19x slower                                                            |
| scimark_lu                 | 118 ms                                                 | 141 ms: 1.20x slower                                                             |
| nqueens                    | 83.3 ms                                                | 99.6 ms: 1.20x slower                                                            |
| django_template            | 34.6 ms                                                | 41.7 ms: 1.20x slower                                                            |
| gc_traversal               | 3.79 ms                                                | 4.61 ms: 1.21x slower                                                            |
| json_dumps                 | 10.4 ms                                                | 12.7 ms: 1.23x slower                                                            |
| hexiom                     | 6.41 ms                                                | 7.87 ms: 1.23x slower                                                            |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 6.27 ms: 1.24x slower                                                            |
| richards_super             | 51.5 ms                                                | 64.5 ms: 1.25x slower                                                            |
| fannkuch                   | 417 ms                                                 | 524 ms: 1.26x slower                                                             |
| deltablue                  | 3.72 ms                                                | 4.83 ms: 1.30x slower                                                            |
| telco                      | 7.10 ms                                                | 9.28 ms: 1.31x slower                                                            |
| typing_runtime_protocols   | 158 us                                                 | 211 us: 1.33x slower                                                             |
| python_startup_no_site     | 6.94 ms                                                | 9.38 ms: 1.35x slower                                                            |
| mako                       | 11.9 ms                                                | 16.8 ms: 1.41x slower                                                            |
| coverage                   | 72.7 ms                                                | 107 ms: 1.47x slower                                                             |
| nbody                      | 97.0 ms                                                | 147 ms: 1.51x slower                                                             |
| python_startup             | 9.55 ms                                                | 15.1 ms: 1.58x slower                                                            |
| bench_mp_pool              | 24.0 ms                                                | 89.6 ms: 3.73x slower                                                            |
| bench_thread_pool          | 842 us                                                 | 3.48 ms: 4.14x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.08x slower                                                                     |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250124-3.14.0a4+-1e0f842-NOGIL/bm-20250124-linux-x86_64-faster%2dcpython-remove_most_conditio-3.14.0a4+-1e0f842.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.041x slower

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 1.31x