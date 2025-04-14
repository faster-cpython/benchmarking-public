# Results vs. 3.12.0

- fork: faster-cpython
- ref: single_point_of_allo
- machine: linux-x86_64
- commit hash: af468a2
- commit date: 2025-03-13
- overall geometric mean: 1.054x faster
- HPT reliability: 99.58%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250313-linux-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-af468a2 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 271 ms: 1.01x faster                                                             |
| docutils       | 2.77 sec                                               | 2.71 sec: 1.02x faster                                                           |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250313-linux-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-af468a2 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 617 ms: 1.87x faster                                                             |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                             |
| async_tree_io_tg           | 1.18 sec                                               | 657 ms: 1.80x faster                                                             |
| async_tree_none_tg         | 450 ms                                                 | 254 ms: 1.77x faster                                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 330 ms: 1.74x faster                                                             |
| async_tree_memoization     | 578 ms                                                 | 336 ms: 1.72x faster                                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 488 ms: 1.49x faster                                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 499 ms: 1.46x faster                                                             |
| Geometric mean             | (ref)                                                  | 1.70x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250313-linux-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-af468a2 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 75.7 ms: 1.12x faster                                                            |
| pidigits       | 187 ms                                                 | 191 ms: 1.02x slower                                                             |
| nbody          | 97.0 ms                                                | 124 ms: 1.28x slower                                                             |
| Geometric mean | (ref)                                                  | 1.05x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250313-linux-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-af468a2 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 134 ms: 1.11x faster                                                             |
| regex_effbot   | 3.61 ms                                                | 3.53 ms: 1.02x faster                                                            |
| regex_v8       | 23.1 ms                                                | 24.3 ms: 1.05x slower                                                            |
| regex_dna      | 212 ms                                                 | 227 ms: 1.07x slower                                                             |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250313-linux-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-af468a2 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_parse      | 159 ms                                                 | 142 ms: 1.12x faster                                                             |
| tomli_loads          | 2.33 sec                                               | 2.13 sec: 1.09x faster                                                           |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                             |
| xml_etree_iterparse  | 107 ms                                                 | 103 ms: 1.04x faster                                                             |
| xml_etree_process    | 61.7 ms                                                | 60.5 ms: 1.02x faster                                                            |
| xml_etree_generate   | 89.2 ms                                                | 87.5 ms: 1.02x faster                                                            |
| json_dumps           | 10.4 ms                                                | 11.7 ms: 1.13x slower                                                            |
| json_loads           | 28.5 us                                                | 32.6 us: 1.14x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                                     |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250313-linux-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-af468a2 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.30 ms: 1.20x slower                                                            |
| python_startup         | 9.55 ms                                                | 13.3 ms: 1.39x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.29x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250313-linux-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-af468a2 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.1 ms: 1.08x faster                                                            |
| django_template | 34.6 ms                                                | 33.6 ms: 1.03x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250313-linux-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-af468a2 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 617 ms: 1.87x faster                                                             |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                             |
| async_tree_io_tg           | 1.18 sec                                               | 657 ms: 1.80x faster                                                             |
| async_tree_none_tg         | 450 ms                                                 | 254 ms: 1.77x faster                                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 330 ms: 1.74x faster                                                             |
| async_tree_memoization     | 578 ms                                                 | 336 ms: 1.72x faster                                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 488 ms: 1.49x faster                                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 499 ms: 1.46x faster                                                             |
| deepcopy_memo              | 40.7 us                                                | 29.5 us: 1.38x faster                                                            |
| deepcopy                   | 371 us                                                 | 272 us: 1.36x faster                                                             |
| comprehensions             | 21.8 us                                                | 17.5 us: 1.24x faster                                                            |
| go                         | 139 ms                                                 | 117 ms: 1.20x faster                                                             |
| deltablue                  | 3.72 ms                                                | 3.21 ms: 1.16x faster                                                            |
| deepcopy_reduce            | 3.35 us                                                | 2.91 us: 1.15x faster                                                            |
| logging_simple             | 6.46 us                                                | 5.76 us: 1.12x faster                                                            |
| generators                 | 31.2 ms                                                | 27.9 ms: 1.12x faster                                                            |
| xml_etree_parse            | 159 ms                                                 | 142 ms: 1.12x faster                                                             |
| float                      | 84.7 ms                                                | 75.7 ms: 1.12x faster                                                            |
| dulwich_log                | 68.5 ms                                                | 61.4 ms: 1.12x faster                                                            |
| logging_format             | 7.23 us                                                | 6.51 us: 1.11x faster                                                            |
| regex_compile              | 148 ms                                                 | 134 ms: 1.11x faster                                                             |
| pathlib                    | 19.3 ms                                                | 17.6 ms: 1.10x faster                                                            |
| tomli_loads                | 2.33 sec                                               | 2.13 sec: 1.09x faster                                                           |
| crypto_pyaes               | 81.9 ms                                                | 75.3 ms: 1.09x faster                                                            |
| sqlalchemy_declarative     | 147 ms                                                 | 136 ms: 1.08x faster                                                             |
| sympy_sum                  | 169 ms                                                 | 157 ms: 1.08x faster                                                             |
| mako                       | 11.9 ms                                                | 11.1 ms: 1.08x faster                                                            |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                             |
| raytrace                   | 312 ms                                                 | 298 ms: 1.05x faster                                                             |
| richards                   | 45.8 ms                                                | 43.8 ms: 1.05x faster                                                            |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.9 ms: 1.05x faster                                                            |
| sympy_integrate            | 21.4 ms                                                | 20.6 ms: 1.04x faster                                                            |
| xml_etree_iterparse        | 107 ms                                                 | 103 ms: 1.04x faster                                                             |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                             |
| hexiom                     | 6.41 ms                                                | 6.19 ms: 1.04x faster                                                            |
| django_template            | 34.6 ms                                                | 33.6 ms: 1.03x faster                                                            |
| chaos                      | 67.0 ms                                                | 65.3 ms: 1.03x faster                                                            |
| pprint_safe_repr           | 776 ms                                                 | 757 ms: 1.02x faster                                                             |
| sympy_str                  | 300 ms                                                 | 293 ms: 1.02x faster                                                             |
| richards_super             | 51.5 ms                                                | 50.3 ms: 1.02x faster                                                            |
| mdp                        | 2.63 sec                                               | 2.57 sec: 1.02x faster                                                           |
| regex_effbot               | 3.61 ms                                                | 3.53 ms: 1.02x faster                                                            |
| xml_etree_process          | 61.7 ms                                                | 60.5 ms: 1.02x faster                                                            |
| docutils                   | 2.77 sec                                               | 2.71 sec: 1.02x faster                                                           |
| async_generators           | 463 ms                                                 | 454 ms: 1.02x faster                                                             |
| xml_etree_generate         | 89.2 ms                                                | 87.5 ms: 1.02x faster                                                            |
| 2to3                       | 274 ms                                                 | 271 ms: 1.01x faster                                                             |
| pyflate                    | 482 ms                                                 | 479 ms: 1.01x faster                                                             |
| coroutines                 | 23.2 ms                                                | 23.3 ms: 1.00x slower                                                            |
| scimark_monte_carlo        | 75.1 ms                                                | 76.0 ms: 1.01x slower                                                            |
| pidigits                   | 187 ms                                                 | 191 ms: 1.02x slower                                                             |
| logging_silent             | 104 ns                                                 | 108 ns: 1.03x slower                                                             |
| sqlite_synth               | 2.83 us                                                | 2.93 us: 1.03x slower                                                            |
| pycparser                  | 1.18 sec                                               | 1.22 sec: 1.03x slower                                                           |
| sympy_expand               | 478 ms                                                 | 501 ms: 1.05x slower                                                             |
| regex_v8                   | 23.1 ms                                                | 24.3 ms: 1.05x slower                                                            |
| scimark_sor                | 129 ms                                                 | 136 ms: 1.05x slower                                                             |
| regex_dna                  | 212 ms                                                 | 227 ms: 1.07x slower                                                             |
| bench_thread_pool          | 842 us                                                 | 906 us: 1.08x slower                                                             |
| nqueens                    | 83.3 ms                                                | 89.7 ms: 1.08x slower                                                            |
| scimark_lu                 | 118 ms                                                 | 128 ms: 1.08x slower                                                             |
| json                       | 5.26 ms                                                | 5.77 ms: 1.10x slower                                                            |
| spectral_norm              | 115 ms                                                 | 127 ms: 1.10x slower                                                             |
| scimark_fft                | 382 ms                                                 | 423 ms: 1.11x slower                                                             |
| fannkuch                   | 417 ms                                                 | 467 ms: 1.12x slower                                                             |
| json_dumps                 | 10.4 ms                                                | 11.7 ms: 1.13x slower                                                            |
| json_loads                 | 28.5 us                                                | 32.6 us: 1.14x slower                                                            |
| telco                      | 7.10 ms                                                | 8.13 ms: 1.15x slower                                                            |
| typing_runtime_protocols   | 158 us                                                 | 183 us: 1.16x slower                                                             |
| coverage                   | 72.7 ms                                                | 85.4 ms: 1.17x slower                                                            |
| python_startup_no_site     | 6.94 ms                                                | 8.30 ms: 1.20x slower                                                            |
| gc_traversal               | 3.79 ms                                                | 4.75 ms: 1.25x slower                                                            |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 6.40 ms: 1.26x slower                                                            |
| nbody                      | 97.0 ms                                                | 124 ms: 1.28x slower                                                             |
| python_startup             | 9.55 ms                                                | 13.3 ms: 1.39x slower                                                            |
| create_gc_cycles           | 1.48 ms                                                | 2.48 ms: 1.68x slower                                                            |
| bench_mp_pool              | 24.0 ms                                                | 84.9 ms: 3.53x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                     |

Benchmark hidden because not significant (3): pprint_pformat, asyncio_websockets, pickle_pure_python
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250313-3.14.0a5+-af468a2/bm-20250313-linux-x86_64-faster%2dcpython-single_point_of_allo-3.14.0a5+-af468a2.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.054x faster

# HPT report

- Reliability score: 99.58% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.10x