# Results vs. 3.12.0

- fork: faster-cpython
- ref: virtual_iterators
- machine: linux-x86_64
- commit hash: cad1946
- commit date: 2025-04-30
- overall geometric mean: 1.118x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 252 ms: 1.09x faster                                                          |
| docutils       | 2.77 sec                                               | 2.60 sec: 1.06x faster                                                        |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 598 ms: 1.93x faster                                                          |
| async_tree_io_tg           | 1.18 sec                                               | 614 ms: 1.93x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 311 ms: 1.85x faster                                                          |
| async_tree_memoization     | 578 ms                                                 | 316 ms: 1.83x faster                                                          |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                          |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.78x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 488 ms: 1.49x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 495 ms: 1.47x faster                                                          |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.4 ms: 1.20x faster                                                         |
| pidigits       | 187 ms                                                 | 190 ms: 1.02x slower                                                          |
| nbody          | 97.0 ms                                                | 98.8 ms: 1.02x slower                                                         |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                          |
| regex_effbot   | 3.61 ms                                                | 3.10 ms: 1.16x faster                                                         |
| regex_v8       | 23.1 ms                                                | 22.3 ms: 1.04x faster                                                         |
| regex_dna      | 212 ms                                                 | 205 ms: 1.03x faster                                                          |
| Geometric mean | (ref)                                                  | 1.10x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.01 sec: 1.16x faster                                                        |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                                          |
| xml_etree_iterparse  | 107 ms                                                 | 99.3 ms: 1.08x faster                                                         |
| unpickle_pure_python | 230 us                                                 | 219 us: 1.05x faster                                                          |
| xml_etree_generate   | 89.2 ms                                                | 85.5 ms: 1.04x faster                                                         |
| xml_etree_process    | 61.7 ms                                                | 59.7 ms: 1.03x faster                                                         |
| pickle_pure_python   | 324 us                                                 | 319 us: 1.02x faster                                                          |
| json_loads           | 28.5 us                                                | 30.4 us: 1.07x slower                                                         |
| json_dumps           | 10.4 ms                                                | 12.1 ms: 1.16x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.92 ms: 1.00x faster                                                         |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.38x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.0 ms: 1.08x faster                                                         |
| mako            | 11.9 ms                                                | 11.7 ms: 1.02x faster                                                         |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250430-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946 |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.22 sec: 2.16x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 598 ms: 1.93x faster                                                          |
| async_tree_io_tg           | 1.18 sec                                               | 614 ms: 1.93x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 311 ms: 1.85x faster                                                          |
| async_tree_memoization     | 578 ms                                                 | 316 ms: 1.83x faster                                                          |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                          |
| async_tree_none_tg         | 450 ms                                                 | 253 ms: 1.78x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 488 ms: 1.49x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 495 ms: 1.47x faster                                                          |
| deepcopy                   | 371 us                                                 | 256 us: 1.45x faster                                                          |
| deepcopy_memo              | 40.7 us                                                | 28.9 us: 1.41x faster                                                         |
| comprehensions             | 21.8 us                                                | 16.2 us: 1.34x faster                                                         |
| go                         | 139 ms                                                 | 110 ms: 1.27x faster                                                          |
| deepcopy_reduce            | 3.35 us                                                | 2.78 us: 1.20x faster                                                         |
| float                      | 84.7 ms                                                | 70.4 ms: 1.20x faster                                                         |
| logging_format             | 7.23 us                                                | 6.13 us: 1.18x faster                                                         |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                          |
| raytrace                   | 312 ms                                                 | 268 ms: 1.17x faster                                                          |
| regex_effbot               | 3.61 ms                                                | 3.10 ms: 1.16x faster                                                         |
| tomli_loads                | 2.33 sec                                               | 2.01 sec: 1.16x faster                                                        |
| logging_simple             | 6.46 us                                                | 5.57 us: 1.16x faster                                                         |
| dulwich_log                | 68.5 ms                                                | 59.7 ms: 1.15x faster                                                         |
| async_generators           | 463 ms                                                 | 410 ms: 1.13x faster                                                          |
| pathlib                    | 19.3 ms                                                | 17.1 ms: 1.13x faster                                                         |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                          |
| chaos                      | 67.0 ms                                                | 59.6 ms: 1.12x faster                                                         |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                                          |
| deltablue                  | 3.72 ms                                                | 3.36 ms: 1.11x faster                                                         |
| scimark_monte_carlo        | 75.1 ms                                                | 68.0 ms: 1.10x faster                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.1 ms: 1.09x faster                                                         |
| crypto_pyaes               | 81.9 ms                                                | 75.1 ms: 1.09x faster                                                         |
| 2to3                       | 274 ms                                                 | 252 ms: 1.09x faster                                                          |
| pprint_safe_repr           | 776 ms                                                 | 715 ms: 1.08x faster                                                          |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.08x faster                                                          |
| django_template            | 34.6 ms                                                | 32.0 ms: 1.08x faster                                                         |
| pprint_pformat             | 1.57 sec                                               | 1.46 sec: 1.08x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                 | 99.3 ms: 1.08x faster                                                         |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                                          |
| docutils                   | 2.77 sec                                               | 2.60 sec: 1.06x faster                                                        |
| richards                   | 45.8 ms                                                | 43.1 ms: 1.06x faster                                                         |
| logging_silent             | 104 ns                                                 | 98.3 ns: 1.06x faster                                                         |
| generators                 | 31.2 ms                                                | 29.4 ms: 1.06x faster                                                         |
| pyflate                    | 482 ms                                                 | 457 ms: 1.06x faster                                                          |
| spectral_norm              | 115 ms                                                 | 109 ms: 1.06x faster                                                          |
| unpickle_pure_python       | 230 us                                                 | 219 us: 1.05x faster                                                          |
| hexiom                     | 6.41 ms                                                | 6.14 ms: 1.04x faster                                                         |
| xml_etree_generate         | 89.2 ms                                                | 85.5 ms: 1.04x faster                                                         |
| regex_v8                   | 23.1 ms                                                | 22.3 ms: 1.04x faster                                                         |
| regex_dna                  | 212 ms                                                 | 205 ms: 1.03x faster                                                          |
| xml_etree_process          | 61.7 ms                                                | 59.7 ms: 1.03x faster                                                         |
| richards_super             | 51.5 ms                                                | 49.9 ms: 1.03x faster                                                         |
| scimark_fft                | 382 ms                                                 | 372 ms: 1.03x faster                                                          |
| nqueens                    | 83.3 ms                                                | 81.7 ms: 1.02x faster                                                         |
| mako                       | 11.9 ms                                                | 11.7 ms: 1.02x faster                                                         |
| pickle_pure_python         | 324 us                                                 | 319 us: 1.02x faster                                                          |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                          |
| python_startup_no_site     | 6.94 ms                                                | 6.92 ms: 1.00x faster                                                         |
| sqlite_synth               | 2.83 us                                                | 2.87 us: 1.01x slower                                                         |
| pidigits                   | 187 ms                                                 | 190 ms: 1.02x slower                                                          |
| nbody                      | 97.0 ms                                                | 98.8 ms: 1.02x slower                                                         |
| typing_runtime_protocols   | 158 us                                                 | 161 us: 1.02x slower                                                          |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.18 ms: 1.02x slower                                                         |
| json                       | 5.26 ms                                                | 5.49 ms: 1.04x slower                                                         |
| bench_thread_pool          | 842 us                                                 | 885 us: 1.05x slower                                                          |
| json_loads                 | 28.5 us                                                | 30.4 us: 1.07x slower                                                         |
| coroutines                 | 23.2 ms                                                | 24.8 ms: 1.07x slower                                                         |
| telco                      | 7.10 ms                                                | 7.93 ms: 1.12x slower                                                         |
| json_dumps                 | 10.4 ms                                                | 12.1 ms: 1.16x slower                                                         |
| gc_traversal               | 3.79 ms                                                | 4.82 ms: 1.27x slower                                                         |
| coverage                   | 72.7 ms                                                | 93.2 ms: 1.28x slower                                                         |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.38x slower                                                         |
| create_gc_cycles           | 1.48 ms                                                | 2.48 ms: 1.68x slower                                                         |
| bench_mp_pool              | 24.0 ms                                                | 82.5 ms: 3.43x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                                  |

Benchmark hidden because not significant (3): pycparser, asyncio_websockets, fannkuch
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, sympy_expand, sympy_integrate, sympy_str, sympy_sum, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (22) of results/bm-20250430-3.14.0a7+-cad1946/bm-20250430-linux-x86_64-faster%2dcpython-virtual_iterators-3.14.0a7+-cad1946.json: async_tree_eager, async_tree_eager_cpu_io_mixed, async_tree_eager_cpu_io_mixed_tg, async_tree_eager_io, async_tree_eager_io_tg, async_tree_eager_memoization, async_tree_eager_memoization_tg, async_tree_eager_tg, bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.118x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.11x