# Results vs. 3.12.0

- fork: faster-cpython
- ref: tagged_ints_lasti
- machine: linux-x86_64
- commit hash: 33b1fe4
- commit date: 2025-04-11
- overall geometric mean: 1.127x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250411-linux-x86_64-faster%2dcpython-tagged_ints_lasti-3.14.0a7+-33b1fe4 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 251 ms: 1.09x faster                                                          |
| docutils       | 2.77 sec                                               | 2.60 sec: 1.06x faster                                                        |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250411-linux-x86_64-faster%2dcpython-tagged_ints_lasti-3.14.0a7+-33b1fe4 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 614 ms: 1.93x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 612 ms: 1.89x faster                                                          |
| async_tree_memoization     | 578 ms                                                 | 309 ms: 1.87x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 312 ms: 1.84x faster                                                          |
| async_tree_none            | 472 ms                                                 | 258 ms: 1.83x faster                                                          |
| async_tree_none_tg         | 450 ms                                                 | 247 ms: 1.82x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 474 ms: 1.53x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 478 ms: 1.52x faster                                                          |
| Geometric mean             | (ref)                                                  | 1.77x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250411-linux-x86_64-faster%2dcpython-tagged_ints_lasti-3.14.0a7+-33b1fe4 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 68.7 ms: 1.23x faster                                                         |
| nbody          | 97.0 ms                                                | 94.6 ms: 1.03x faster                                                         |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                          |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250411-linux-x86_64-faster%2dcpython-tagged_ints_lasti-3.14.0a7+-33b1fe4 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 125 ms: 1.19x faster                                                          |
| regex_effbot   | 3.61 ms                                                | 3.26 ms: 1.11x faster                                                         |
| regex_dna      | 212 ms                                                 | 210 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                  |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250411-linux-x86_64-faster%2dcpython-tagged_ints_lasti-3.14.0a7+-33b1fe4 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.93 sec: 1.21x faster                                                        |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                                          |
| xml_etree_iterparse  | 107 ms                                                 | 98.6 ms: 1.08x faster                                                         |
| xml_etree_generate   | 89.2 ms                                                | 84.6 ms: 1.05x faster                                                         |
| xml_etree_process    | 61.7 ms                                                | 58.6 ms: 1.05x faster                                                         |
| unpickle_pure_python | 230 us                                                 | 220 us: 1.04x faster                                                          |
| pickle_pure_python   | 324 us                                                 | 318 us: 1.02x faster                                                          |
| json_loads           | 28.5 us                                                | 29.8 us: 1.04x slower                                                         |
| json_dumps           | 10.4 ms                                                | 11.6 ms: 1.12x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250411-linux-x86_64-faster%2dcpython-tagged_ints_lasti-3.14.0a7+-33b1fe4 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.19 ms: 1.18x slower                                                         |
| python_startup         | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250411-linux-x86_64-faster%2dcpython-tagged_ints_lasti-3.14.0a7+-33b1fe4 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.1 ms: 1.08x faster                                                         |
| mako            | 11.9 ms                                                | 11.4 ms: 1.05x faster                                                         |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250411-linux-x86_64-faster%2dcpython-tagged_ints_lasti-3.14.0a7+-33b1fe4 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.21 sec: 2.18x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 614 ms: 1.93x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 612 ms: 1.89x faster                                                          |
| async_tree_memoization     | 578 ms                                                 | 309 ms: 1.87x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 312 ms: 1.84x faster                                                          |
| async_tree_none            | 472 ms                                                 | 258 ms: 1.83x faster                                                          |
| async_tree_none_tg         | 450 ms                                                 | 247 ms: 1.82x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 474 ms: 1.53x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 478 ms: 1.52x faster                                                          |
| deepcopy                   | 371 us                                                 | 250 us: 1.48x faster                                                          |
| deepcopy_memo              | 40.7 us                                                | 28.5 us: 1.43x faster                                                         |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                         |
| deepcopy_reduce            | 3.35 us                                                | 2.67 us: 1.25x faster                                                         |
| go                         | 139 ms                                                 | 112 ms: 1.25x faster                                                          |
| float                      | 84.7 ms                                                | 68.7 ms: 1.23x faster                                                         |
| tomli_loads                | 2.33 sec                                               | 1.93 sec: 1.21x faster                                                        |
| chaos                      | 67.0 ms                                                | 55.7 ms: 1.20x faster                                                         |
| regex_compile              | 148 ms                                                 | 125 ms: 1.19x faster                                                          |
| logging_format             | 7.23 us                                                | 6.13 us: 1.18x faster                                                         |
| raytrace                   | 312 ms                                                 | 265 ms: 1.18x faster                                                          |
| async_generators           | 463 ms                                                 | 393 ms: 1.18x faster                                                          |
| logging_simple             | 6.46 us                                                | 5.53 us: 1.17x faster                                                         |
| dulwich_log                | 68.5 ms                                                | 59.4 ms: 1.15x faster                                                         |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                                          |
| scimark_monte_carlo        | 75.1 ms                                                | 66.0 ms: 1.14x faster                                                         |
| sympy_integrate            | 21.4 ms                                                | 18.9 ms: 1.14x faster                                                         |
| sympy_str                  | 300 ms                                                 | 265 ms: 1.13x faster                                                          |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                          |
| pathlib                    | 19.3 ms                                                | 17.2 ms: 1.13x faster                                                         |
| spectral_norm              | 115 ms                                                 | 102 ms: 1.13x faster                                                          |
| crypto_pyaes               | 81.9 ms                                                | 73.2 ms: 1.12x faster                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.8 ms: 1.11x faster                                                         |
| sqlalchemy_declarative     | 147 ms                                                 | 132 ms: 1.11x faster                                                          |
| regex_effbot               | 3.61 ms                                                | 3.26 ms: 1.11x faster                                                         |
| logging_silent             | 104 ns                                                 | 94.9 ns: 1.10x faster                                                         |
| scimark_fft                | 382 ms                                                 | 348 ms: 1.10x faster                                                          |
| 2to3                       | 274 ms                                                 | 251 ms: 1.09x faster                                                          |
| deltablue                  | 3.72 ms                                                | 3.41 ms: 1.09x faster                                                         |
| xml_etree_iterparse        | 107 ms                                                 | 98.6 ms: 1.08x faster                                                         |
| pprint_safe_repr           | 776 ms                                                 | 717 ms: 1.08x faster                                                          |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.08x faster                                                          |
| django_template            | 34.6 ms                                                | 32.1 ms: 1.08x faster                                                         |
| pyflate                    | 482 ms                                                 | 448 ms: 1.08x faster                                                          |
| pprint_pformat             | 1.57 sec                                               | 1.46 sec: 1.07x faster                                                        |
| sympy_expand               | 478 ms                                                 | 448 ms: 1.07x faster                                                          |
| docutils                   | 2.77 sec                                               | 2.60 sec: 1.06x faster                                                        |
| richards                   | 45.8 ms                                                | 43.2 ms: 1.06x faster                                                         |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                          |
| xml_etree_generate         | 89.2 ms                                                | 84.6 ms: 1.05x faster                                                         |
| xml_etree_process          | 61.7 ms                                                | 58.6 ms: 1.05x faster                                                         |
| mako                       | 11.9 ms                                                | 11.4 ms: 1.05x faster                                                         |
| unpickle_pure_python       | 230 us                                                 | 220 us: 1.04x faster                                                          |
| richards_super             | 51.5 ms                                                | 49.4 ms: 1.04x faster                                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.85 ms: 1.04x faster                                                         |
| nqueens                    | 83.3 ms                                                | 80.2 ms: 1.04x faster                                                         |
| nbody                      | 97.0 ms                                                | 94.6 ms: 1.03x faster                                                         |
| generators                 | 31.2 ms                                                | 30.5 ms: 1.02x faster                                                         |
| hexiom                     | 6.41 ms                                                | 6.27 ms: 1.02x faster                                                         |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.02x faster                                                        |
| pickle_pure_python         | 324 us                                                 | 318 us: 1.02x faster                                                          |
| fannkuch                   | 417 ms                                                 | 413 ms: 1.01x faster                                                          |
| sqlite_synth               | 2.83 us                                                | 2.81 us: 1.01x faster                                                         |
| regex_dna                  | 212 ms                                                 | 210 ms: 1.01x faster                                                          |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                          |
| scimark_lu                 | 118 ms                                                 | 119 ms: 1.01x slower                                                          |
| json                       | 5.26 ms                                                | 5.32 ms: 1.01x slower                                                         |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                          |
| json_loads                 | 28.5 us                                                | 29.8 us: 1.04x slower                                                         |
| bench_thread_pool          | 842 us                                                 | 887 us: 1.05x slower                                                          |
| coroutines                 | 23.2 ms                                                | 24.6 ms: 1.06x slower                                                         |
| telco                      | 7.10 ms                                                | 7.80 ms: 1.10x slower                                                         |
| json_dumps                 | 10.4 ms                                                | 11.6 ms: 1.12x slower                                                         |
| python_startup_no_site     | 6.94 ms                                                | 8.19 ms: 1.18x slower                                                         |
| coverage                   | 72.7 ms                                                | 87.5 ms: 1.20x slower                                                         |
| gc_traversal               | 3.79 ms                                                | 4.78 ms: 1.26x slower                                                         |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                         |
| create_gc_cycles           | 1.48 ms                                                | 2.45 ms: 1.66x slower                                                         |
| bench_mp_pool              | 24.0 ms                                                | 81.5 ms: 3.39x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.11x faster                                                                  |

Benchmark hidden because not significant (2): asyncio_websockets, regex_v8
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250411-3.14.0a7+-33b1fe4/bm-20250411-linux-x86_64-faster%2dcpython-tagged_ints_lasti-3.14.0a7+-33b1fe4.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.127x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.10x