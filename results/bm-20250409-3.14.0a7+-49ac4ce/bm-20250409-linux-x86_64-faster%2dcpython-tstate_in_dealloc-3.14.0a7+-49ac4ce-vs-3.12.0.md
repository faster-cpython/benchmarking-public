# Results vs. 3.12.0

- fork: faster-cpython
- ref: tstate_in_dealloc
- machine: linux-x86_64
- commit hash: 49ac4ce
- commit date: 2025-04-09
- overall geometric mean: 1.124x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-linux-x86_64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 252 ms: 1.09x faster                                                          |
| docutils       | 2.77 sec                                               | 2.61 sec: 1.06x faster                                                        |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-linux-x86_64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 614 ms: 1.93x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 616 ms: 1.88x faster                                                          |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.85x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.82x faster                                                          |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.81x faster                                                          |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 483 ms: 1.50x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 489 ms: 1.49x faster                                                          |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-linux-x86_64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.3 ms: 1.21x faster                                                         |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                  |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-linux-x86_64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 125 ms: 1.19x faster                                                          |
| regex_effbot   | 3.61 ms                                                | 3.10 ms: 1.16x faster                                                         |
| regex_dna      | 212 ms                                                 | 209 ms: 1.02x faster                                                          |
| regex_v8       | 23.1 ms                                                | 23.9 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-linux-x86_64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.00 sec: 1.17x faster                                                        |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                                          |
| xml_etree_iterparse  | 107 ms                                                 | 97.7 ms: 1.09x faster                                                         |
| unpickle_pure_python | 230 us                                                 | 214 us: 1.08x faster                                                          |
| xml_etree_generate   | 89.2 ms                                                | 83.5 ms: 1.07x faster                                                         |
| xml_etree_process    | 61.7 ms                                                | 58.1 ms: 1.06x faster                                                         |
| pickle_pure_python   | 324 us                                                 | 313 us: 1.04x faster                                                          |
| json_loads           | 28.5 us                                                | 30.5 us: 1.07x slower                                                         |
| json_dumps           | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-linux-x86_64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.24 ms: 1.19x slower                                                         |
| python_startup         | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-linux-x86_64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.4 ms: 1.10x faster                                                         |
| mako            | 11.9 ms                                                | 11.3 ms: 1.06x faster                                                         |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250409-linux-x86_64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.23 sec: 2.14x faster                                                        |
| async_tree_io_tg           | 1.18 sec                                               | 614 ms: 1.93x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 616 ms: 1.88x faster                                                          |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.85x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.82x faster                                                          |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.81x faster                                                          |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 483 ms: 1.50x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 489 ms: 1.49x faster                                                          |
| deepcopy                   | 371 us                                                 | 251 us: 1.48x faster                                                          |
| deepcopy_memo              | 40.7 us                                                | 28.9 us: 1.41x faster                                                         |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.30x faster                                                         |
| go                         | 139 ms                                                 | 110 ms: 1.27x faster                                                          |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.25x faster                                                         |
| float                      | 84.7 ms                                                | 70.3 ms: 1.21x faster                                                         |
| regex_compile              | 148 ms                                                 | 125 ms: 1.19x faster                                                          |
| raytrace                   | 312 ms                                                 | 265 ms: 1.18x faster                                                          |
| tomli_loads                | 2.33 sec                                               | 2.00 sec: 1.17x faster                                                        |
| regex_effbot               | 3.61 ms                                                | 3.10 ms: 1.16x faster                                                         |
| logging_format             | 7.23 us                                                | 6.22 us: 1.16x faster                                                         |
| chaos                      | 67.0 ms                                                | 57.7 ms: 1.16x faster                                                         |
| pathlib                    | 19.3 ms                                                | 16.9 ms: 1.15x faster                                                         |
| logging_simple             | 6.46 us                                                | 5.63 us: 1.15x faster                                                         |
| dulwich_log                | 68.5 ms                                                | 60.1 ms: 1.14x faster                                                         |
| async_generators           | 463 ms                                                 | 407 ms: 1.14x faster                                                          |
| pyflate                    | 482 ms                                                 | 425 ms: 1.14x faster                                                          |
| deltablue                  | 3.72 ms                                                | 3.28 ms: 1.13x faster                                                         |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.13x faster                                                          |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                          |
| sympy_integrate            | 21.4 ms                                                | 19.1 ms: 1.12x faster                                                         |
| sympy_str                  | 300 ms                                                 | 269 ms: 1.11x faster                                                          |
| scimark_monte_carlo        | 75.1 ms                                                | 67.5 ms: 1.11x faster                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.8 ms: 1.11x faster                                                         |
| sqlalchemy_declarative     | 147 ms                                                 | 133 ms: 1.11x faster                                                          |
| django_template            | 34.6 ms                                                | 31.4 ms: 1.10x faster                                                         |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.10x faster                                                          |
| logging_silent             | 104 ns                                                 | 95.5 ns: 1.09x faster                                                         |
| xml_etree_iterparse        | 107 ms                                                 | 97.7 ms: 1.09x faster                                                         |
| 2to3                       | 274 ms                                                 | 252 ms: 1.09x faster                                                          |
| crypto_pyaes               | 81.9 ms                                                | 75.4 ms: 1.09x faster                                                         |
| pprint_safe_repr           | 776 ms                                                 | 717 ms: 1.08x faster                                                          |
| richards                   | 45.8 ms                                                | 42.4 ms: 1.08x faster                                                         |
| unpickle_pure_python       | 230 us                                                 | 214 us: 1.08x faster                                                          |
| pprint_pformat             | 1.57 sec                                               | 1.46 sec: 1.07x faster                                                        |
| spectral_norm              | 115 ms                                                 | 107 ms: 1.07x faster                                                          |
| xml_etree_generate         | 89.2 ms                                                | 83.5 ms: 1.07x faster                                                         |
| xml_etree_process          | 61.7 ms                                                | 58.1 ms: 1.06x faster                                                         |
| docutils                   | 2.77 sec                                               | 2.61 sec: 1.06x faster                                                        |
| hexiom                     | 6.41 ms                                                | 6.05 ms: 1.06x faster                                                         |
| richards_super             | 51.5 ms                                                | 48.7 ms: 1.06x faster                                                         |
| pycparser                  | 1.18 sec                                               | 1.12 sec: 1.06x faster                                                        |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.06x faster                                                         |
| meteor_contest             | 112 ms                                                 | 106 ms: 1.06x faster                                                          |
| generators                 | 31.2 ms                                                | 29.9 ms: 1.04x faster                                                         |
| scimark_fft                | 382 ms                                                 | 366 ms: 1.04x faster                                                          |
| sympy_expand               | 478 ms                                                 | 459 ms: 1.04x faster                                                          |
| pickle_pure_python         | 324 us                                                 | 313 us: 1.04x faster                                                          |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.03x faster                                                          |
| fannkuch                   | 417 ms                                                 | 408 ms: 1.02x faster                                                          |
| nqueens                    | 83.3 ms                                                | 81.6 ms: 1.02x faster                                                         |
| regex_dna                  | 212 ms                                                 | 209 ms: 1.02x faster                                                          |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                          |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.10 ms: 1.01x slower                                                         |
| typing_runtime_protocols   | 158 us                                                 | 162 us: 1.03x slower                                                          |
| coroutines                 | 23.2 ms                                                | 23.9 ms: 1.03x slower                                                         |
| regex_v8                   | 23.1 ms                                                | 23.9 ms: 1.03x slower                                                         |
| bench_thread_pool          | 842 us                                                 | 882 us: 1.05x slower                                                          |
| json                       | 5.26 ms                                                | 5.54 ms: 1.05x slower                                                         |
| json_loads                 | 28.5 us                                                | 30.5 us: 1.07x slower                                                         |
| json_dumps                 | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                         |
| telco                      | 7.10 ms                                                | 7.98 ms: 1.12x slower                                                         |
| coverage                   | 72.7 ms                                                | 85.6 ms: 1.18x slower                                                         |
| python_startup_no_site     | 6.94 ms                                                | 8.24 ms: 1.19x slower                                                         |
| gc_traversal               | 3.79 ms                                                | 4.79 ms: 1.26x slower                                                         |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                         |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.67x slower                                                         |
| bench_mp_pool              | 24.0 ms                                                | 82.3 ms: 3.43x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                                  |

Benchmark hidden because not significant (3): asyncio_websockets, nbody, sqlite_synth
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250409-3.14.0a7+-49ac4ce/bm-20250409-linux-x86_64-faster%2dcpython-tstate_in_dealloc-3.14.0a7+-49ac4ce.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.124x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.07x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.10x