# Results vs. 3.12.0

- fork: faster-cpython
- ref: close_escapes_2
- machine: linux-x86_64
- commit hash: fa5c6fd
- commit date: 2025-01-28
- overall geometric mean: 1.116x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.09x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250128-linux-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 254 ms: 1.08x faster                                                        |
| docutils       | 2.77 sec                                               | 2.59 sec: 1.07x faster                                                      |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250128-linux-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 623 ms: 1.90x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 615 ms: 1.88x faster                                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 318 ms: 1.81x faster                                                        |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 321 ms: 1.80x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.78x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 484 ms: 1.50x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 495 ms: 1.47x faster                                                        |
| Geometric mean             | (ref)                                                  | 1.73x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250128-linux-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.4 ms: 1.20x faster                                                       |
| nbody          | 97.0 ms                                                | 92.8 ms: 1.04x faster                                                       |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250128-linux-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.18x faster                                                        |
| regex_effbot   | 3.61 ms                                                | 3.34 ms: 1.08x faster                                                       |
| regex_dna      | 212 ms                                                 | 211 ms: 1.01x faster                                                        |
| regex_v8       | 23.1 ms                                                | 25.5 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250128-linux-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                      |
| xml_etree_parse      | 159 ms                                                 | 138 ms: 1.15x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                 | 97.9 ms: 1.09x faster                                                       |
| unpickle_pure_python | 230 us                                                 | 218 us: 1.06x faster                                                        |
| xml_etree_generate   | 89.2 ms                                                | 85.3 ms: 1.04x faster                                                       |
| xml_etree_process    | 61.7 ms                                                | 60.1 ms: 1.03x faster                                                       |
| pickle_pure_python   | 324 us                                                 | 321 us: 1.01x faster                                                        |
| json_loads           | 28.5 us                                                | 29.0 us: 1.02x slower                                                       |
| json_dumps           | 10.4 ms                                                | 11.7 ms: 1.13x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250128-linux-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.04 ms: 1.01x slower                                                       |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250128-linux-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.7 ms: 1.09x faster                                                       |
| mako            | 11.9 ms                                                | 11.3 ms: 1.06x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.07x faster                                                                |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250128-linux-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 623 ms: 1.90x faster                                                        |
| async_tree_io              | 1.16 sec                                               | 615 ms: 1.88x faster                                                        |
| async_tree_memoization_tg  | 575 ms                                                 | 318 ms: 1.81x faster                                                        |
| async_tree_none            | 472 ms                                                 | 262 ms: 1.80x faster                                                        |
| async_tree_memoization     | 578 ms                                                 | 321 ms: 1.80x faster                                                        |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.78x faster                                                        |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 484 ms: 1.50x faster                                                        |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 495 ms: 1.47x faster                                                        |
| deepcopy                   | 371 us                                                 | 254 us: 1.46x faster                                                        |
| deepcopy_memo              | 40.7 us                                                | 30.4 us: 1.34x faster                                                       |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                       |
| pathlib                    | 19.3 ms                                                | 15.7 ms: 1.23x faster                                                       |
| deepcopy_reduce            | 3.35 us                                                | 2.71 us: 1.23x faster                                                       |
| async_generators           | 463 ms                                                 | 381 ms: 1.21x faster                                                        |
| go                         | 139 ms                                                 | 116 ms: 1.20x faster                                                        |
| float                      | 84.7 ms                                                | 70.4 ms: 1.20x faster                                                       |
| tomli_loads                | 2.33 sec                                               | 1.94 sec: 1.20x faster                                                      |
| logging_format             | 7.23 us                                                | 6.04 us: 1.20x faster                                                       |
| spectral_norm              | 115 ms                                                 | 96.5 ms: 1.19x faster                                                       |
| regex_compile              | 148 ms                                                 | 126 ms: 1.18x faster                                                        |
| logging_simple             | 6.46 us                                                | 5.50 us: 1.17x faster                                                       |
| deltablue                  | 3.72 ms                                                | 3.21 ms: 1.16x faster                                                       |
| xml_etree_parse            | 159 ms                                                 | 138 ms: 1.15x faster                                                        |
| chaos                      | 67.0 ms                                                | 58.1 ms: 1.15x faster                                                       |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                                        |
| raytrace                   | 312 ms                                                 | 271 ms: 1.15x faster                                                        |
| crypto_pyaes               | 81.9 ms                                                | 71.7 ms: 1.14x faster                                                       |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.4 ms: 1.14x faster                                                       |
| sqlalchemy_declarative     | 147 ms                                                 | 129 ms: 1.14x faster                                                        |
| generators                 | 31.2 ms                                                | 27.6 ms: 1.13x faster                                                       |
| scimark_monte_carlo        | 75.1 ms                                                | 66.6 ms: 1.13x faster                                                       |
| scimark_fft                | 382 ms                                                 | 340 ms: 1.12x faster                                                        |
| sympy_str                  | 300 ms                                                 | 267 ms: 1.12x faster                                                        |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.62 ms: 1.09x faster                                                       |
| xml_etree_iterparse        | 107 ms                                                 | 97.9 ms: 1.09x faster                                                       |
| django_template            | 34.6 ms                                                | 31.7 ms: 1.09x faster                                                       |
| sympy_integrate            | 21.4 ms                                                | 19.7 ms: 1.09x faster                                                       |
| sqlglot_parse              | 1.36 ms                                                | 1.26 ms: 1.08x faster                                                       |
| regex_effbot               | 3.61 ms                                                | 3.34 ms: 1.08x faster                                                       |
| 2to3                       | 274 ms                                                 | 254 ms: 1.08x faster                                                        |
| sqlglot_transpile          | 1.68 ms                                                | 1.56 ms: 1.08x faster                                                       |
| dulwich_log                | 68.5 ms                                                | 63.7 ms: 1.08x faster                                                       |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.07x faster                                                        |
| docutils                   | 2.77 sec                                               | 2.59 sec: 1.07x faster                                                      |
| pprint_safe_repr           | 776 ms                                                 | 726 ms: 1.07x faster                                                        |
| pprint_pformat             | 1.57 sec                                               | 1.48 sec: 1.06x faster                                                      |
| mdp                        | 2.63 sec                                               | 2.49 sec: 1.06x faster                                                      |
| unpickle_pure_python       | 230 us                                                 | 218 us: 1.06x faster                                                        |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.06x faster                                                       |
| sqlglot_normalize          | 110 ms                                                 | 104 ms: 1.06x faster                                                        |
| richards                   | 45.8 ms                                                | 43.5 ms: 1.05x faster                                                       |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                        |
| fannkuch                   | 417 ms                                                 | 398 ms: 1.05x faster                                                        |
| hexiom                     | 6.41 ms                                                | 6.12 ms: 1.05x faster                                                       |
| sympy_expand               | 478 ms                                                 | 456 ms: 1.05x faster                                                        |
| xml_etree_generate         | 89.2 ms                                                | 85.3 ms: 1.04x faster                                                       |
| nbody                      | 97.0 ms                                                | 92.8 ms: 1.04x faster                                                       |
| sqlglot_optimize           | 54.8 ms                                                | 52.6 ms: 1.04x faster                                                       |
| richards_super             | 51.5 ms                                                | 49.6 ms: 1.04x faster                                                       |
| nqueens                    | 83.3 ms                                                | 80.3 ms: 1.04x faster                                                       |
| pyflate                    | 482 ms                                                 | 466 ms: 1.03x faster                                                        |
| scimark_lu                 | 118 ms                                                 | 115 ms: 1.03x faster                                                        |
| xml_etree_process          | 61.7 ms                                                | 60.1 ms: 1.03x faster                                                       |
| json                       | 5.26 ms                                                | 5.12 ms: 1.03x faster                                                       |
| sqlite_synth               | 2.83 us                                                | 2.77 us: 1.02x faster                                                       |
| logging_silent             | 104 ns                                                 | 103 ns: 1.01x faster                                                        |
| pickle_pure_python         | 324 us                                                 | 321 us: 1.01x faster                                                        |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                        |
| regex_dna                  | 212 ms                                                 | 211 ms: 1.01x faster                                                        |
| python_startup_no_site     | 6.94 ms                                                | 7.04 ms: 1.01x slower                                                       |
| typing_runtime_protocols   | 158 us                                                 | 160 us: 1.02x slower                                                        |
| json_loads                 | 28.5 us                                                | 29.0 us: 1.02x slower                                                       |
| bench_thread_pool          | 842 us                                                 | 861 us: 1.02x slower                                                        |
| regex_v8                   | 23.1 ms                                                | 25.5 ms: 1.10x slower                                                       |
| telco                      | 7.10 ms                                                | 7.86 ms: 1.11x slower                                                       |
| json_dumps                 | 10.4 ms                                                | 11.7 ms: 1.13x slower                                                       |
| coverage                   | 72.7 ms                                                | 91.5 ms: 1.26x slower                                                       |
| gc_traversal               | 3.79 ms                                                | 4.88 ms: 1.29x slower                                                       |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                       |
| create_gc_cycles           | 1.48 ms                                                | 2.46 ms: 1.67x slower                                                       |
| bench_mp_pool              | 24.0 ms                                                | 81.2 ms: 3.38x slower                                                       |
| Geometric mean             | (ref)                                                  | 1.10x faster                                                                |

Benchmark hidden because not significant (3): pycparser, coroutines, asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250128-3.14.0a4+-fa5c6fd/bm-20250128-linux-x86_64-faster%2dcpython-close_escapes_2-3.14.0a4+-fa5c6fd.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.116x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.09x