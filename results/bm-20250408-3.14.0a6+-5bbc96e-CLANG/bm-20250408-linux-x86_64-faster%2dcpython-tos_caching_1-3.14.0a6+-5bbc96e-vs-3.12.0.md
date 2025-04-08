# Results vs. 3.12.0

- fork: faster-cpython
- ref: tos_caching_1
- machine: linux-x86_64
- commit hash: 5bbc96e
- commit date: 2025-04-08
- overall geometric mean: 1.156x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.07x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 245 ms: 1.12x faster                                                      |
| docutils       | 2.77 sec                                               | 2.58 sec: 1.07x faster                                                    |
| Geometric mean | (ref)                                                  | 1.10x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 618 ms: 1.91x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 605 ms: 1.91x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 309 ms: 1.87x faster                                                      |
| async_tree_none            | 472 ms                                                 | 257 ms: 1.84x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 313 ms: 1.83x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 247 ms: 1.82x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 484 ms: 1.50x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 488 ms: 1.49x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.76x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 66.9 ms: 1.27x faster                                                     |
| nbody          | 97.0 ms                                                | 82.1 ms: 1.18x faster                                                     |
| pidigits       | 187 ms                                                 | 202 ms: 1.08x slower                                                      |
| Geometric mean | (ref)                                                  | 1.12x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.06 ms: 1.18x faster                                                     |
| regex_compile  | 148 ms                                                 | 126 ms: 1.18x faster                                                      |
| regex_dna      | 212 ms                                                 | 191 ms: 1.11x faster                                                      |
| regex_v8       | 23.1 ms                                                | 22.3 ms: 1.04x faster                                                     |
| Geometric mean | (ref)                                                  | 1.12x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.84 sec: 1.27x faster                                                    |
| pickle_pure_python   | 324 us                                                 | 309 us: 1.05x faster                                                      |
| unpickle_pure_python | 230 us                                                 | 220 us: 1.05x faster                                                      |
| xml_etree_iterparse  | 107 ms                                                 | 103 ms: 1.04x faster                                                      |
| xml_etree_process    | 61.7 ms                                                | 60.7 ms: 1.02x faster                                                     |
| xml_etree_generate   | 89.2 ms                                                | 87.9 ms: 1.01x faster                                                     |
| json_loads           | 28.5 us                                                | 28.3 us: 1.01x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 162 ms: 1.02x slower                                                      |
| json_dumps           | 10.4 ms                                                | 12.3 ms: 1.18x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.12 ms: 1.17x slower                                                     |
| python_startup         | 9.55 ms                                                | 13.0 ms: 1.36x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.26x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.9 ms: 1.08x faster                                                     |
| mako            | 11.9 ms                                                | 11.6 ms: 1.02x faster                                                     |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250408-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.21 sec: 2.17x faster                                                    |
| async_tree_io_tg           | 1.18 sec                                               | 618 ms: 1.91x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 605 ms: 1.91x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 309 ms: 1.87x faster                                                      |
| async_tree_none            | 472 ms                                                 | 257 ms: 1.84x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 313 ms: 1.83x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 247 ms: 1.82x faster                                                      |
| deepcopy                   | 371 us                                                 | 247 us: 1.51x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 484 ms: 1.50x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 488 ms: 1.49x faster                                                      |
| deepcopy_memo              | 40.7 us                                                | 29.1 us: 1.40x faster                                                     |
| comprehensions             | 21.8 us                                                | 15.6 us: 1.40x faster                                                     |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 3.81 ms: 1.33x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                | 2.57 us: 1.30x faster                                                     |
| go                         | 139 ms                                                 | 108 ms: 1.29x faster                                                      |
| pathlib                    | 19.3 ms                                                | 15.1 ms: 1.28x faster                                                     |
| scimark_monte_carlo        | 75.1 ms                                                | 58.6 ms: 1.28x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 1.84 sec: 1.27x faster                                                    |
| float                      | 84.7 ms                                                | 66.9 ms: 1.27x faster                                                     |
| scimark_fft                | 382 ms                                                 | 303 ms: 1.26x faster                                                      |
| raytrace                   | 312 ms                                                 | 252 ms: 1.24x faster                                                      |
| deltablue                  | 3.72 ms                                                | 3.01 ms: 1.24x faster                                                     |
| spectral_norm              | 115 ms                                                 | 93.5 ms: 1.23x faster                                                     |
| chaos                      | 67.0 ms                                                | 54.6 ms: 1.23x faster                                                     |
| async_generators           | 463 ms                                                 | 386 ms: 1.20x faster                                                      |
| pyflate                    | 482 ms                                                 | 407 ms: 1.19x faster                                                      |
| scimark_sor                | 129 ms                                                 | 109 ms: 1.18x faster                                                      |
| logging_format             | 7.23 us                                                | 6.11 us: 1.18x faster                                                     |
| nbody                      | 97.0 ms                                                | 82.1 ms: 1.18x faster                                                     |
| regex_effbot               | 3.61 ms                                                | 3.06 ms: 1.18x faster                                                     |
| logging_silent             | 104 ns                                                 | 88.7 ns: 1.18x faster                                                     |
| dulwich_log                | 68.5 ms                                                | 58.2 ms: 1.18x faster                                                     |
| regex_compile              | 148 ms                                                 | 126 ms: 1.18x faster                                                      |
| logging_simple             | 6.46 us                                                | 5.53 us: 1.17x faster                                                     |
| sympy_sum                  | 169 ms                                                 | 146 ms: 1.16x faster                                                      |
| sympy_integrate            | 21.4 ms                                                | 18.6 ms: 1.15x faster                                                     |
| sqlalchemy_declarative     | 147 ms                                                 | 128 ms: 1.15x faster                                                      |
| crypto_pyaes               | 81.9 ms                                                | 71.7 ms: 1.14x faster                                                     |
| sympy_str                  | 300 ms                                                 | 265 ms: 1.13x faster                                                      |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.5 ms: 1.13x faster                                                     |
| 2to3                       | 274 ms                                                 | 245 ms: 1.12x faster                                                      |
| richards                   | 45.8 ms                                                | 41.1 ms: 1.11x faster                                                     |
| generators                 | 31.2 ms                                                | 28.0 ms: 1.11x faster                                                     |
| regex_dna                  | 212 ms                                                 | 191 ms: 1.11x faster                                                      |
| richards_super             | 51.5 ms                                                | 47.0 ms: 1.10x faster                                                     |
| hexiom                     | 6.41 ms                                                | 5.86 ms: 1.09x faster                                                     |
| django_template            | 34.6 ms                                                | 31.9 ms: 1.08x faster                                                     |
| pycparser                  | 1.18 sec                                               | 1.09 sec: 1.08x faster                                                    |
| docutils                   | 2.77 sec                                               | 2.58 sec: 1.07x faster                                                    |
| sqlite_synth               | 2.83 us                                                | 2.66 us: 1.07x faster                                                     |
| nqueens                    | 83.3 ms                                                | 78.8 ms: 1.06x faster                                                     |
| fannkuch                   | 417 ms                                                 | 396 ms: 1.05x faster                                                      |
| sympy_expand               | 478 ms                                                 | 455 ms: 1.05x faster                                                      |
| pickle_pure_python         | 324 us                                                 | 309 us: 1.05x faster                                                      |
| unpickle_pure_python       | 230 us                                                 | 220 us: 1.05x faster                                                      |
| scimark_lu                 | 118 ms                                                 | 113 ms: 1.04x faster                                                      |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                      |
| regex_v8                   | 23.1 ms                                                | 22.3 ms: 1.04x faster                                                     |
| xml_etree_iterparse        | 107 ms                                                 | 103 ms: 1.04x faster                                                      |
| pprint_safe_repr           | 776 ms                                                 | 758 ms: 1.02x faster                                                      |
| mako                       | 11.9 ms                                                | 11.6 ms: 1.02x faster                                                     |
| xml_etree_process          | 61.7 ms                                                | 60.7 ms: 1.02x faster                                                     |
| xml_etree_generate         | 89.2 ms                                                | 87.9 ms: 1.01x faster                                                     |
| pprint_pformat             | 1.57 sec                                               | 1.56 sec: 1.01x faster                                                    |
| json_loads                 | 28.5 us                                                | 28.3 us: 1.01x faster                                                     |
| typing_runtime_protocols   | 158 us                                                 | 157 us: 1.01x faster                                                      |
| bench_thread_pool          | 842 us                                                 | 848 us: 1.01x slower                                                      |
| xml_etree_parse            | 159 ms                                                 | 162 ms: 1.02x slower                                                      |
| telco                      | 7.10 ms                                                | 7.38 ms: 1.04x slower                                                     |
| pidigits                   | 187 ms                                                 | 202 ms: 1.08x slower                                                      |
| coverage                   | 72.7 ms                                                | 82.1 ms: 1.13x slower                                                     |
| python_startup_no_site     | 6.94 ms                                                | 8.12 ms: 1.17x slower                                                     |
| json_dumps                 | 10.4 ms                                                | 12.3 ms: 1.18x slower                                                     |
| gc_traversal               | 3.79 ms                                                | 4.94 ms: 1.30x slower                                                     |
| python_startup             | 9.55 ms                                                | 13.0 ms: 1.36x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 2.51 ms: 1.70x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 80.9 ms: 3.37x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.14x faster                                                              |

Benchmark hidden because not significant (3): json, asyncio_websockets, coroutines
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250408-3.14.0a6+-5bbc96e-CLANG/bm-20250408-linux-x86_64-faster%2dcpython-tos_caching_1-3.14.0a6+-5bbc96e.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.156x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.10x
- 95% likely to have a speedup of 1.09x
- 99% likely to have a speedup of 1.07x

# Memory
- memory change: 1.11x