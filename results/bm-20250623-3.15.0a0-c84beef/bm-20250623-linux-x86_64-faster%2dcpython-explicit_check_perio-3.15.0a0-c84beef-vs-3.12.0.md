# Results vs. 3.12.0

- fork: faster-cpython
- ref: explicit_check_perio
- machine: linux-x86_64
- commit hash: c84beef
- commit date: 2025-06-23
- overall geometric mean: 1.113x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 255 ms: 1.08x faster                                                            |
| docutils       | 2.77 sec                                               | 2.59 sec: 1.07x faster                                                          |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 601 ms: 1.92x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 638 ms: 1.85x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 316 ms: 1.83x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                            |
| async_tree_none            | 472 ms                                                 | 264 ms: 1.78x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.78x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 501 ms: 1.45x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 508 ms: 1.43x faster                                                            |
| Geometric mean             | (ref)                                                  | 1.72x faster                                                                    |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 72.5 ms: 1.17x faster                                                           |
| nbody          | 97.0 ms                                                | 95.5 ms: 1.02x faster                                                           |
| pidigits       | 187 ms                                                 | 193 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.16x faster                                                            |
| regex_effbot   | 3.61 ms                                                | 3.33 ms: 1.08x faster                                                           |
| regex_dna      | 212 ms                                                 | 210 ms: 1.01x faster                                                            |
| regex_v8       | 23.1 ms                                                | 23.5 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.00 sec: 1.16x faster                                                          |
| xml_etree_parse      | 159 ms                                                 | 144 ms: 1.11x faster                                                            |
| xml_etree_iterparse  | 107 ms                                                 | 99.6 ms: 1.07x faster                                                           |
| xml_etree_generate   | 89.2 ms                                                | 85.6 ms: 1.04x faster                                                           |
| unpickle_pure_python | 230 us                                                 | 222 us: 1.04x faster                                                            |
| xml_etree_process    | 61.7 ms                                                | 60.0 ms: 1.03x faster                                                           |
| pickle_pure_python   | 324 us                                                 | 321 us: 1.01x faster                                                            |
| json_loads           | 28.5 us                                                | 28.3 us: 1.01x faster                                                           |
| json_dumps           | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                    |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.95 ms: 1.00x slower                                                           |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.28x slower                                                           |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.4 ms: 1.07x faster                                                           |
| mako            | 11.9 ms                                                | 11.5 ms: 1.03x faster                                                           |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250623-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.23 sec: 2.15x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 601 ms: 1.92x faster                                                            |
| async_tree_io_tg           | 1.18 sec                                               | 638 ms: 1.85x faster                                                            |
| async_tree_memoization     | 578 ms                                                 | 316 ms: 1.83x faster                                                            |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                            |
| async_tree_none            | 472 ms                                                 | 264 ms: 1.78x faster                                                            |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.78x faster                                                            |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 501 ms: 1.45x faster                                                            |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 508 ms: 1.43x faster                                                            |
| deepcopy                   | 371 us                                                 | 261 us: 1.42x faster                                                            |
| comprehensions             | 21.8 us                                                | 16.1 us: 1.35x faster                                                           |
| deepcopy_memo              | 40.7 us                                                | 30.3 us: 1.34x faster                                                           |
| go                         | 139 ms                                                 | 111 ms: 1.26x faster                                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.70 us: 1.24x faster                                                           |
| float                      | 84.7 ms                                                | 72.5 ms: 1.17x faster                                                           |
| tomli_loads                | 2.33 sec                                               | 2.00 sec: 1.16x faster                                                          |
| regex_compile              | 148 ms                                                 | 127 ms: 1.16x faster                                                            |
| raytrace                   | 312 ms                                                 | 268 ms: 1.16x faster                                                            |
| dulwich_log                | 68.5 ms                                                | 59.0 ms: 1.16x faster                                                           |
| scimark_monte_carlo        | 75.1 ms                                                | 65.7 ms: 1.14x faster                                                           |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.14x faster                                                            |
| spectral_norm              | 115 ms                                                 | 101 ms: 1.13x faster                                                            |
| pyflate                    | 482 ms                                                 | 425 ms: 1.13x faster                                                            |
| async_generators           | 463 ms                                                 | 410 ms: 1.13x faster                                                            |
| sympy_integrate            | 21.4 ms                                                | 19.0 ms: 1.13x faster                                                           |
| scimark_sor                | 129 ms                                                 | 115 ms: 1.12x faster                                                            |
| sympy_str                  | 300 ms                                                 | 268 ms: 1.12x faster                                                            |
| chaos                      | 67.0 ms                                                | 60.2 ms: 1.11x faster                                                           |
| pathlib                    | 19.3 ms                                                | 17.4 ms: 1.11x faster                                                           |
| xml_etree_parse            | 159 ms                                                 | 144 ms: 1.11x faster                                                            |
| regex_effbot               | 3.61 ms                                                | 3.33 ms: 1.08x faster                                                           |
| crypto_pyaes               | 81.9 ms                                                | 75.7 ms: 1.08x faster                                                           |
| 2to3                       | 274 ms                                                 | 255 ms: 1.08x faster                                                            |
| deltablue                  | 3.72 ms                                                | 3.45 ms: 1.08x faster                                                           |
| xml_etree_iterparse        | 107 ms                                                 | 99.6 ms: 1.07x faster                                                           |
| docutils                   | 2.77 sec                                               | 2.59 sec: 1.07x faster                                                          |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                                            |
| django_template            | 34.6 ms                                                | 32.4 ms: 1.07x faster                                                           |
| richards                   | 45.8 ms                                                | 43.2 ms: 1.06x faster                                                           |
| scimark_fft                | 382 ms                                                 | 361 ms: 1.06x faster                                                            |
| sympy_expand               | 478 ms                                                 | 453 ms: 1.06x faster                                                            |
| richards_super             | 51.5 ms                                                | 48.8 ms: 1.06x faster                                                           |
| generators                 | 31.2 ms                                                | 29.7 ms: 1.05x faster                                                           |
| hexiom                     | 6.41 ms                                                | 6.11 ms: 1.05x faster                                                           |
| logging_format             | 7.23 us                                                | 6.90 us: 1.05x faster                                                           |
| logging_simple             | 6.46 us                                                | 6.19 us: 1.04x faster                                                           |
| xml_etree_generate         | 89.2 ms                                                | 85.6 ms: 1.04x faster                                                           |
| unpickle_pure_python       | 230 us                                                 | 222 us: 1.04x faster                                                            |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.04x faster                                                          |
| mako                       | 11.9 ms                                                | 11.5 ms: 1.03x faster                                                           |
| xml_etree_process          | 61.7 ms                                                | 60.0 ms: 1.03x faster                                                           |
| nqueens                    | 83.3 ms                                                | 81.2 ms: 1.03x faster                                                           |
| fannkuch                   | 417 ms                                                 | 408 ms: 1.02x faster                                                            |
| nbody                      | 97.0 ms                                                | 95.5 ms: 1.02x faster                                                           |
| regex_dna                  | 212 ms                                                 | 210 ms: 1.01x faster                                                            |
| pickle_pure_python         | 324 us                                                 | 321 us: 1.01x faster                                                            |
| json_loads                 | 28.5 us                                                | 28.3 us: 1.01x faster                                                           |
| python_startup_no_site     | 6.94 ms                                                | 6.95 ms: 1.00x slower                                                           |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                                            |
| regex_v8                   | 23.1 ms                                                | 23.5 ms: 1.01x slower                                                           |
| sqlite_synth               | 2.83 us                                                | 2.88 us: 1.02x slower                                                           |
| pidigits                   | 187 ms                                                 | 193 ms: 1.03x slower                                                            |
| pprint_safe_repr           | 776 ms                                                 | 807 ms: 1.04x slower                                                            |
| pprint_pformat             | 1.57 sec                                               | 1.65 sec: 1.05x slower                                                          |
| coroutines                 | 23.2 ms                                                | 24.4 ms: 1.05x slower                                                           |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                                            |
| json_dumps                 | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                           |
| telco                      | 7.10 ms                                                | 7.90 ms: 1.11x slower                                                           |
| coverage                   | 72.7 ms                                                | 87.3 ms: 1.20x slower                                                           |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.28x slower                                                           |
| gc_traversal               | 3.79 ms                                                | 5.02 ms: 1.32x slower                                                           |
| create_gc_cycles           | 1.48 ms                                                | 2.59 ms: 1.75x slower                                                           |
| logging_silent             | 104 ns                                                 | 471 ns: 4.51x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                                    |

Benchmark hidden because not significant (3): scimark_lu, scimark_sparse_mat_mult, json
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250623-3.15.0a0-c84beef/bm-20250623-linux-x86_64-faster%2dcpython-explicit_check_perio-3.15.0a0-c84beef.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.113x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.13x