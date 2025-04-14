# Results vs. 3.12.0

- fork: faster-cpython
- ref: c_recursion_limit
- machine: linux-x86_64
- commit hash: 21366c3
- commit date: 2025-02-17
- overall geometric mean: 1.115x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-linux-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 254 ms: 1.08x faster                                                          |
| docutils       | 2.77 sec                                               | 2.60 sec: 1.07x faster                                                        |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-linux-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 620 ms: 1.91x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 621 ms: 1.86x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                          |
| async_tree_memoization     | 578 ms                                                 | 323 ms: 1.79x faster                                                          |
| async_tree_none            | 472 ms                                                 | 265 ms: 1.78x faster                                                          |
| async_tree_none_tg         | 450 ms                                                 | 256 ms: 1.75x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 481 ms: 1.51x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 488 ms: 1.49x faster                                                          |
| Geometric mean             | (ref)                                                  | 1.73x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-linux-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.9 ms: 1.19x faster                                                         |
| nbody          | 97.0 ms                                                | 93.6 ms: 1.04x faster                                                         |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-linux-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 125 ms: 1.19x faster                                                          |
| regex_effbot   | 3.61 ms                                                | 3.15 ms: 1.15x faster                                                         |
| regex_dna      | 212 ms                                                 | 220 ms: 1.04x slower                                                          |
| regex_v8       | 23.1 ms                                                | 24.9 ms: 1.08x slower                                                         |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-linux-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                        |
| xml_etree_parse      | 159 ms                                                 | 140 ms: 1.14x faster                                                          |
| xml_etree_iterparse  | 107 ms                                                 | 97.4 ms: 1.10x faster                                                         |
| unpickle_pure_python | 230 us                                                 | 216 us: 1.07x faster                                                          |
| xml_etree_generate   | 89.2 ms                                                | 84.5 ms: 1.06x faster                                                         |
| xml_etree_process    | 61.7 ms                                                | 58.8 ms: 1.05x faster                                                         |
| pickle_pure_python   | 324 us                                                 | 313 us: 1.03x faster                                                          |
| json_loads           | 28.5 us                                                | 30.4 us: 1.07x slower                                                         |
| json_dumps           | 10.4 ms                                                | 11.4 ms: 1.10x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-linux-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                         |
| python_startup         | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-linux-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.0 ms: 1.09x faster                                                         |
| django_template | 34.6 ms                                                | 32.0 ms: 1.08x faster                                                         |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250217-linux-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 620 ms: 1.91x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 621 ms: 1.86x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                          |
| async_tree_memoization     | 578 ms                                                 | 323 ms: 1.79x faster                                                          |
| async_tree_none            | 472 ms                                                 | 265 ms: 1.78x faster                                                          |
| async_tree_none_tg         | 450 ms                                                 | 256 ms: 1.75x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 481 ms: 1.51x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 488 ms: 1.49x faster                                                          |
| deepcopy                   | 371 us                                                 | 261 us: 1.42x faster                                                          |
| deepcopy_memo              | 40.7 us                                                | 29.9 us: 1.36x faster                                                         |
| comprehensions             | 21.8 us                                                | 16.4 us: 1.33x faster                                                         |
| deepcopy_reduce            | 3.35 us                                                | 2.73 us: 1.23x faster                                                         |
| go                         | 139 ms                                                 | 115 ms: 1.21x faster                                                          |
| tomli_loads                | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                        |
| float                      | 84.7 ms                                                | 70.9 ms: 1.19x faster                                                         |
| logging_format             | 7.23 us                                                | 6.07 us: 1.19x faster                                                         |
| regex_compile              | 148 ms                                                 | 125 ms: 1.19x faster                                                          |
| async_generators           | 463 ms                                                 | 389 ms: 1.19x faster                                                          |
| spectral_norm              | 115 ms                                                 | 96.9 ms: 1.19x faster                                                         |
| deltablue                  | 3.72 ms                                                | 3.15 ms: 1.18x faster                                                         |
| logging_simple             | 6.46 us                                                | 5.49 us: 1.18x faster                                                         |
| pathlib                    | 19.3 ms                                                | 16.5 ms: 1.17x faster                                                         |
| chaos                      | 67.0 ms                                                | 57.7 ms: 1.16x faster                                                         |
| raytrace                   | 312 ms                                                 | 269 ms: 1.16x faster                                                          |
| regex_effbot               | 3.61 ms                                                | 3.15 ms: 1.15x faster                                                         |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                                          |
| sqlalchemy_declarative     | 147 ms                                                 | 128 ms: 1.15x faster                                                          |
| xml_etree_parse            | 159 ms                                                 | 140 ms: 1.14x faster                                                          |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.4 ms: 1.14x faster                                                         |
| scimark_monte_carlo        | 75.1 ms                                                | 66.5 ms: 1.13x faster                                                         |
| crypto_pyaes               | 81.9 ms                                                | 72.6 ms: 1.13x faster                                                         |
| sympy_str                  | 300 ms                                                 | 267 ms: 1.12x faster                                                          |
| scimark_fft                | 382 ms                                                 | 342 ms: 1.12x faster                                                          |
| generators                 | 31.2 ms                                                | 28.4 ms: 1.10x faster                                                         |
| xml_etree_iterparse        | 107 ms                                                 | 97.4 ms: 1.10x faster                                                         |
| sympy_integrate            | 21.4 ms                                                | 19.7 ms: 1.09x faster                                                         |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.09x faster                                                          |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.09x faster                                                         |
| sqlglot_parse              | 1.36 ms                                                | 1.26 ms: 1.08x faster                                                         |
| django_template            | 34.6 ms                                                | 32.0 ms: 1.08x faster                                                         |
| 2to3                       | 274 ms                                                 | 254 ms: 1.08x faster                                                          |
| pprint_safe_repr           | 776 ms                                                 | 719 ms: 1.08x faster                                                          |
| sqlglot_transpile          | 1.68 ms                                                | 1.56 ms: 1.08x faster                                                         |
| pprint_pformat             | 1.57 sec                                               | 1.46 sec: 1.07x faster                                                        |
| docutils                   | 2.77 sec                                               | 2.60 sec: 1.07x faster                                                        |
| dulwich_log                | 68.5 ms                                                | 64.3 ms: 1.07x faster                                                         |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                                          |
| unpickle_pure_python       | 230 us                                                 | 216 us: 1.07x faster                                                          |
| mdp                        | 2.63 sec                                               | 2.48 sec: 1.06x faster                                                        |
| pyflate                    | 482 ms                                                 | 455 ms: 1.06x faster                                                          |
| sqlglot_normalize          | 110 ms                                                 | 104 ms: 1.06x faster                                                          |
| xml_etree_generate         | 89.2 ms                                                | 84.5 ms: 1.06x faster                                                         |
| sympy_expand               | 478 ms                                                 | 453 ms: 1.06x faster                                                          |
| richards                   | 45.8 ms                                                | 43.6 ms: 1.05x faster                                                         |
| xml_etree_process          | 61.7 ms                                                | 58.8 ms: 1.05x faster                                                         |
| sqlglot_optimize           | 54.8 ms                                                | 52.3 ms: 1.05x faster                                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.83 ms: 1.05x faster                                                         |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.04x faster                                                        |
| hexiom                     | 6.41 ms                                                | 6.15 ms: 1.04x faster                                                         |
| nbody                      | 97.0 ms                                                | 93.6 ms: 1.04x faster                                                         |
| richards_super             | 51.5 ms                                                | 49.8 ms: 1.04x faster                                                         |
| pickle_pure_python         | 324 us                                                 | 313 us: 1.03x faster                                                          |
| fannkuch                   | 417 ms                                                 | 403 ms: 1.03x faster                                                          |
| nqueens                    | 83.3 ms                                                | 81.7 ms: 1.02x faster                                                         |
| sqlite_synth               | 2.83 us                                                | 2.78 us: 1.02x faster                                                         |
| logging_silent             | 104 ns                                                 | 103 ns: 1.02x faster                                                          |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.01x faster                                                          |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                          |
| coroutines                 | 23.2 ms                                                | 23.4 ms: 1.01x slower                                                         |
| python_startup_no_site     | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                         |
| json                       | 5.26 ms                                                | 5.38 ms: 1.02x slower                                                         |
| bench_thread_pool          | 842 us                                                 | 866 us: 1.03x slower                                                          |
| regex_dna                  | 212 ms                                                 | 220 ms: 1.04x slower                                                          |
| json_loads                 | 28.5 us                                                | 30.4 us: 1.07x slower                                                         |
| regex_v8                   | 23.1 ms                                                | 24.9 ms: 1.08x slower                                                         |
| telco                      | 7.10 ms                                                | 7.75 ms: 1.09x slower                                                         |
| json_dumps                 | 10.4 ms                                                | 11.4 ms: 1.10x slower                                                         |
| coverage                   | 72.7 ms                                                | 90.8 ms: 1.25x slower                                                         |
| gc_traversal               | 3.79 ms                                                | 4.93 ms: 1.30x slower                                                         |
| python_startup             | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                         |
| create_gc_cycles           | 1.48 ms                                                | 2.48 ms: 1.68x slower                                                         |
| bench_mp_pool              | 24.0 ms                                                | 81.6 ms: 3.40x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                                  |

Benchmark hidden because not significant (2): typing_runtime_protocols, asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250217-3.14.0a5+-21366c3/bm-20250217-linux-x86_64-faster%2dcpython-c_recursion_limit-3.14.0a5+-21366c3.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.115x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.09x