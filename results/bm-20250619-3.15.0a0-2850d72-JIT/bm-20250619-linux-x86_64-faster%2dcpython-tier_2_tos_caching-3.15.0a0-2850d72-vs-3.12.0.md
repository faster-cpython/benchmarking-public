# Results vs. 3.12.0

- fork: faster-cpython
- ref: tier_2_tos_caching
- machine: linux-x86_64
- commit hash: 2850d72
- commit date: 2025-06-19
- overall geometric mean: 1.131x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.15x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 260 ms: 1.06x faster                                                          |
| docutils       | 2.77 sec                                               | 2.64 sec: 1.05x faster                                                        |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 616 ms: 1.92x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 607 ms: 1.90x faster                                                          |
| async_tree_memoization     | 578 ms                                                 | 317 ms: 1.82x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                          |
| async_tree_none            | 472 ms                                                 | 265 ms: 1.78x faster                                                          |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.78x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 498 ms: 1.46x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 506 ms: 1.43x faster                                                          |
| Geometric mean             | (ref)                                                  | 1.73x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 65.0 ms: 1.30x faster                                                         |
| nbody          | 97.0 ms                                                | 82.8 ms: 1.17x faster                                                         |
| pidigits       | 187 ms                                                 | 193 ms: 1.03x slower                                                          |
| Geometric mean | (ref)                                                  | 1.14x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                          |
| regex_effbot   | 3.61 ms                                                | 3.10 ms: 1.16x faster                                                         |
| regex_dna      | 212 ms                                                 | 186 ms: 1.14x faster                                                          |
| regex_v8       | 23.1 ms                                                | 22.3 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                  | 1.13x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.86 sec: 1.25x faster                                                        |
| xml_etree_parse      | 159 ms                                                 | 139 ms: 1.15x faster                                                          |
| unpickle_pure_python | 230 us                                                 | 205 us: 1.12x faster                                                          |
| xml_etree_process    | 61.7 ms                                                | 56.0 ms: 1.10x faster                                                         |
| xml_etree_generate   | 89.2 ms                                                | 81.1 ms: 1.10x faster                                                         |
| xml_etree_iterparse  | 107 ms                                                 | 98.5 ms: 1.08x faster                                                         |
| json_loads           | 28.5 us                                                | 27.9 us: 1.02x faster                                                         |
| json_dumps           | 10.4 ms                                                | 11.0 ms: 1.06x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.08x faster                                                                  |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.98 ms: 1.01x slower                                                         |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.28x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.14x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.8 ms: 1.10x faster                                                         |
| django_template | 34.6 ms                                                | 32.3 ms: 1.07x faster                                                         |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250619-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.24 sec: 2.13x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 616 ms: 1.92x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 607 ms: 1.90x faster                                                          |
| async_tree_memoization     | 578 ms                                                 | 317 ms: 1.82x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                          |
| async_tree_none            | 472 ms                                                 | 265 ms: 1.78x faster                                                          |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.78x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 498 ms: 1.46x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 506 ms: 1.43x faster                                                          |
| deepcopy                   | 371 us                                                 | 262 us: 1.42x faster                                                          |
| deepcopy_memo              | 40.7 us                                                | 29.5 us: 1.38x faster                                                         |
| richards                   | 45.8 ms                                                | 33.8 ms: 1.35x faster                                                         |
| richards_super             | 51.5 ms                                                | 38.9 ms: 1.32x faster                                                         |
| float                      | 84.7 ms                                                | 65.0 ms: 1.30x faster                                                         |
| comprehensions             | 21.8 us                                                | 17.2 us: 1.27x faster                                                         |
| tomli_loads                | 2.33 sec                                               | 1.86 sec: 1.25x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                                         |
| spectral_norm              | 115 ms                                                 | 94.7 ms: 1.21x faster                                                         |
| scimark_fft                | 382 ms                                                 | 318 ms: 1.20x faster                                                          |
| deltablue                  | 3.72 ms                                                | 3.14 ms: 1.18x faster                                                         |
| nbody                      | 97.0 ms                                                | 82.8 ms: 1.17x faster                                                         |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                          |
| regex_effbot               | 3.61 ms                                                | 3.10 ms: 1.16x faster                                                         |
| dulwich_log                | 68.5 ms                                                | 59.5 ms: 1.15x faster                                                         |
| go                         | 139 ms                                                 | 121 ms: 1.15x faster                                                          |
| pyflate                    | 482 ms                                                 | 420 ms: 1.15x faster                                                          |
| xml_etree_parse            | 159 ms                                                 | 139 ms: 1.15x faster                                                          |
| regex_dna                  | 212 ms                                                 | 186 ms: 1.14x faster                                                          |
| raytrace                   | 312 ms                                                 | 274 ms: 1.14x faster                                                          |
| scimark_monte_carlo        | 75.1 ms                                                | 66.0 ms: 1.14x faster                                                         |
| pathlib                    | 19.3 ms                                                | 17.0 ms: 1.14x faster                                                         |
| sympy_sum                  | 169 ms                                                 | 150 ms: 1.13x faster                                                          |
| unpickle_pure_python       | 230 us                                                 | 205 us: 1.12x faster                                                          |
| sympy_integrate            | 21.4 ms                                                | 19.3 ms: 1.11x faster                                                         |
| sympy_str                  | 300 ms                                                 | 271 ms: 1.10x faster                                                          |
| xml_etree_process          | 61.7 ms                                                | 56.0 ms: 1.10x faster                                                         |
| mako                       | 11.9 ms                                                | 10.8 ms: 1.10x faster                                                         |
| xml_etree_generate         | 89.2 ms                                                | 81.1 ms: 1.10x faster                                                         |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.10x faster                                                          |
| chaos                      | 67.0 ms                                                | 61.5 ms: 1.09x faster                                                         |
| xml_etree_iterparse        | 107 ms                                                 | 98.5 ms: 1.08x faster                                                         |
| async_generators           | 463 ms                                                 | 428 ms: 1.08x faster                                                          |
| django_template            | 34.6 ms                                                | 32.3 ms: 1.07x faster                                                         |
| pycparser                  | 1.18 sec                                               | 1.11 sec: 1.07x faster                                                        |
| crypto_pyaes               | 81.9 ms                                                | 76.8 ms: 1.07x faster                                                         |
| 2to3                       | 274 ms                                                 | 260 ms: 1.06x faster                                                          |
| logging_format             | 7.23 us                                                | 6.85 us: 1.06x faster                                                         |
| docutils                   | 2.77 sec                                               | 2.64 sec: 1.05x faster                                                        |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                          |
| logging_simple             | 6.46 us                                                | 6.19 us: 1.04x faster                                                         |
| regex_v8                   | 23.1 ms                                                | 22.3 ms: 1.04x faster                                                         |
| fannkuch                   | 417 ms                                                 | 401 ms: 1.04x faster                                                          |
| generators                 | 31.2 ms                                                | 30.3 ms: 1.03x faster                                                         |
| sympy_expand               | 478 ms                                                 | 468 ms: 1.02x faster                                                          |
| json                       | 5.26 ms                                                | 5.15 ms: 1.02x faster                                                         |
| json_loads                 | 28.5 us                                                | 27.9 us: 1.02x faster                                                         |
| nqueens                    | 83.3 ms                                                | 82.0 ms: 1.02x faster                                                         |
| sqlite_synth               | 2.83 us                                                | 2.81 us: 1.01x faster                                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.04 ms: 1.00x faster                                                         |
| python_startup_no_site     | 6.94 ms                                                | 6.98 ms: 1.01x slower                                                         |
| pidigits                   | 187 ms                                                 | 193 ms: 1.03x slower                                                          |
| json_dumps                 | 10.4 ms                                                | 11.0 ms: 1.06x slower                                                         |
| typing_runtime_protocols   | 158 us                                                 | 171 us: 1.08x slower                                                          |
| coroutines                 | 23.2 ms                                                | 25.1 ms: 1.08x slower                                                         |
| pprint_safe_repr           | 776 ms                                                 | 855 ms: 1.10x slower                                                          |
| telco                      | 7.10 ms                                                | 7.91 ms: 1.11x slower                                                         |
| pprint_pformat             | 1.57 sec                                               | 1.75 sec: 1.12x slower                                                        |
| coverage                   | 72.7 ms                                                | 87.4 ms: 1.20x slower                                                         |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.28x slower                                                         |
| gc_traversal               | 3.79 ms                                                | 5.07 ms: 1.34x slower                                                         |
| create_gc_cycles           | 1.48 ms                                                | 2.59 ms: 1.75x slower                                                         |
| logging_silent             | 104 ns                                                 | 477 ns: 4.57x slower                                                          |
| Geometric mean             | (ref)                                                  | 1.11x faster                                                                  |

Benchmark hidden because not significant (4): scimark_lu, pickle_pure_python, hexiom, asyncio_websockets
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250619-3.15.0a0-2850d72-JIT/bm-20250619-linux-x86_64-faster%2dcpython-tier_2_tos_caching-3.15.0a0-2850d72.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.131x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.15x