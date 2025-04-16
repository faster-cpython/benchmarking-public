# Results vs. 3.12.0

- fork: faster-cpython
- ref: virtual_iterators
- machine: linux-x86_64
- commit hash: a4b740d
- commit date: 2025-04-16
- overall geometric mean: 1.136x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250416-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 250 ms: 1.10x faster                                                          |
| docutils       | 2.77 sec                                               | 2.56 sec: 1.08x faster                                                        |
| Geometric mean | (ref)                                                  | 1.09x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250416-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 621 ms: 1.90x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 610 ms: 1.89x faster                                                          |
| async_tree_memoization     | 578 ms                                                 | 309 ms: 1.87x faster                                                          |
| async_tree_none            | 472 ms                                                 | 256 ms: 1.84x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                          |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 474 ms: 1.53x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 480 ms: 1.51x faster                                                          |
| Geometric mean             | (ref)                                                  | 1.76x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250416-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.0 ms: 1.23x faster                                                         |
| nbody          | 97.0 ms                                                | 93.9 ms: 1.03x faster                                                         |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                          |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250416-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.02 ms: 1.20x faster                                                         |
| regex_compile  | 148 ms                                                 | 125 ms: 1.19x faster                                                          |
| regex_dna      | 212 ms                                                 | 203 ms: 1.04x faster                                                          |
| regex_v8       | 23.1 ms                                                | 22.3 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250416-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                        |
| xml_etree_parse      | 159 ms                                                 | 142 ms: 1.12x faster                                                          |
| xml_etree_iterparse  | 107 ms                                                 | 98.7 ms: 1.08x faster                                                         |
| xml_etree_generate   | 89.2 ms                                                | 83.2 ms: 1.07x faster                                                         |
| xml_etree_process    | 61.7 ms                                                | 57.8 ms: 1.07x faster                                                         |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                          |
| pickle_pure_python   | 324 us                                                 | 317 us: 1.02x faster                                                          |
| json_loads           | 28.5 us                                                | 30.1 us: 1.06x slower                                                         |
| json_dumps           | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250416-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.23 ms: 1.19x slower                                                         |
| python_startup         | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250416-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.0 ms: 1.12x faster                                                         |
| mako            | 11.9 ms                                                | 11.3 ms: 1.06x faster                                                         |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250416-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.20 sec: 2.19x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 621 ms: 1.90x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 610 ms: 1.89x faster                                                          |
| async_tree_memoization     | 578 ms                                                 | 309 ms: 1.87x faster                                                          |
| async_tree_none            | 472 ms                                                 | 256 ms: 1.84x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                          |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 474 ms: 1.53x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 480 ms: 1.51x faster                                                          |
| deepcopy                   | 371 us                                                 | 250 us: 1.48x faster                                                          |
| deepcopy_memo              | 40.7 us                                                | 28.7 us: 1.42x faster                                                         |
| comprehensions             | 21.8 us                                                | 15.9 us: 1.37x faster                                                         |
| go                         | 139 ms                                                 | 108 ms: 1.29x faster                                                          |
| deepcopy_reduce            | 3.35 us                                                | 2.65 us: 1.26x faster                                                         |
| float                      | 84.7 ms                                                | 69.0 ms: 1.23x faster                                                         |
| raytrace                   | 312 ms                                                 | 260 ms: 1.20x faster                                                          |
| logging_format             | 7.23 us                                                | 6.02 us: 1.20x faster                                                         |
| tomli_loads                | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                        |
| regex_effbot               | 3.61 ms                                                | 3.02 ms: 1.20x faster                                                         |
| regex_compile              | 148 ms                                                 | 125 ms: 1.19x faster                                                          |
| chaos                      | 67.0 ms                                                | 56.5 ms: 1.19x faster                                                         |
| logging_simple             | 6.46 us                                                | 5.46 us: 1.18x faster                                                         |
| async_generators           | 463 ms                                                 | 394 ms: 1.17x faster                                                          |
| dulwich_log                | 68.5 ms                                                | 59.5 ms: 1.15x faster                                                         |
| pathlib                    | 19.3 ms                                                | 16.8 ms: 1.15x faster                                                         |
| scimark_monte_carlo        | 75.1 ms                                                | 66.2 ms: 1.13x faster                                                         |
| sqlalchemy_declarative     | 147 ms                                                 | 130 ms: 1.13x faster                                                          |
| xml_etree_parse            | 159 ms                                                 | 142 ms: 1.12x faster                                                          |
| pyflate                    | 482 ms                                                 | 431 ms: 1.12x faster                                                          |
| django_template            | 34.6 ms                                                | 31.0 ms: 1.12x faster                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.8 ms: 1.11x faster                                                         |
| crypto_pyaes               | 81.9 ms                                                | 73.8 ms: 1.11x faster                                                         |
| spectral_norm              | 115 ms                                                 | 104 ms: 1.11x faster                                                          |
| pprint_safe_repr           | 776 ms                                                 | 702 ms: 1.10x faster                                                          |
| 2to3                       | 274 ms                                                 | 250 ms: 1.10x faster                                                          |
| deltablue                  | 3.72 ms                                                | 3.39 ms: 1.10x faster                                                         |
| logging_silent             | 104 ns                                                 | 95.3 ns: 1.10x faster                                                         |
| pprint_pformat             | 1.57 sec                                               | 1.44 sec: 1.09x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                 | 98.7 ms: 1.08x faster                                                         |
| docutils                   | 2.77 sec                                               | 2.56 sec: 1.08x faster                                                        |
| generators                 | 31.2 ms                                                | 28.9 ms: 1.08x faster                                                         |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.08x faster                                                          |
| meteor_contest             | 112 ms                                                 | 104 ms: 1.08x faster                                                          |
| pycparser                  | 1.18 sec                                               | 1.10 sec: 1.07x faster                                                        |
| xml_etree_generate         | 89.2 ms                                                | 83.2 ms: 1.07x faster                                                         |
| richards                   | 45.8 ms                                                | 42.9 ms: 1.07x faster                                                         |
| xml_etree_process          | 61.7 ms                                                | 57.8 ms: 1.07x faster                                                         |
| scimark_fft                | 382 ms                                                 | 358 ms: 1.07x faster                                                          |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                          |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.06x faster                                                         |
| hexiom                     | 6.41 ms                                                | 6.11 ms: 1.05x faster                                                         |
| richards_super             | 51.5 ms                                                | 49.1 ms: 1.05x faster                                                         |
| regex_dna                  | 212 ms                                                 | 203 ms: 1.04x faster                                                          |
| nqueens                    | 83.3 ms                                                | 80.1 ms: 1.04x faster                                                         |
| regex_v8                   | 23.1 ms                                                | 22.3 ms: 1.04x faster                                                         |
| nbody                      | 97.0 ms                                                | 93.9 ms: 1.03x faster                                                         |
| pickle_pure_python         | 324 us                                                 | 317 us: 1.02x faster                                                          |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.96 ms: 1.02x faster                                                         |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                                         |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                          |
| typing_runtime_protocols   | 158 us                                                 | 159 us: 1.01x slower                                                          |
| json                       | 5.26 ms                                                | 5.34 ms: 1.01x slower                                                         |
| bench_thread_pool          | 842 us                                                 | 880 us: 1.04x slower                                                          |
| coroutines                 | 23.2 ms                                                | 24.4 ms: 1.05x slower                                                         |
| json_loads                 | 28.5 us                                                | 30.1 us: 1.06x slower                                                         |
| telco                      | 7.10 ms                                                | 7.64 ms: 1.08x slower                                                         |
| json_dumps                 | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                         |
| python_startup_no_site     | 6.94 ms                                                | 8.23 ms: 1.19x slower                                                         |
| coverage                   | 72.7 ms                                                | 86.8 ms: 1.19x slower                                                         |
| gc_traversal               | 3.79 ms                                                | 5.05 ms: 1.33x slower                                                         |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                         |
| create_gc_cycles           | 1.48 ms                                                | 2.49 ms: 1.68x slower                                                         |
| bench_mp_pool              | 24.0 ms                                                | 81.8 ms: 3.41x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.11x faster                                                                  |

Benchmark hidden because not significant (3): scimark_lu, fannkuch, asyncio_websockets
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (14) of results/bm-20250416-3.14.0a7+-a4b740d/bm-20250416-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-a4b740d.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.136x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.10x