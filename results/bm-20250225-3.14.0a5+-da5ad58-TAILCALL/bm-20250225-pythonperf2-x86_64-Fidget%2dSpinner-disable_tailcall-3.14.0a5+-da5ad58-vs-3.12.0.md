# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: disable_tailcall
- machine: linux-x86_64
- commit hash: da5ad58
- commit date: 2025-02-25
- overall geometric mean: 1.082x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-pythonperf2-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 307 ms: 1.08x slower                                                               |
| docutils       | 2.87 sec                                                     | 2.98 sec: 1.04x slower                                                             |
| Geometric mean | (ref)                                                        | 1.06x slower                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-pythonperf2-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 713 ms: 1.48x faster                                                               |
| async_tree_io              | 1.04 sec                                                     | 713 ms: 1.46x faster                                                               |
| async_tree_memoization_tg  | 540 ms                                                       | 372 ms: 1.45x faster                                                               |
| async_tree_none            | 452 ms                                                       | 319 ms: 1.41x faster                                                               |
| async_tree_none_tg         | 431 ms                                                       | 307 ms: 1.40x faster                                                               |
| async_tree_memoization     | 544 ms                                                       | 390 ms: 1.40x faster                                                               |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 568 ms: 1.23x faster                                                               |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 586 ms: 1.19x faster                                                               |
| Geometric mean             | (ref)                                                        | 1.37x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-pythonperf2-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| float          | 76.6 ms                                                      | 84.7 ms: 1.11x slower                                                              |
| pidigits       | 265 ms                                                       | 293 ms: 1.11x slower                                                               |
| nbody          | 88.0 ms                                                      | 123 ms: 1.40x slower                                                               |
| Geometric mean | (ref)                                                        | 1.20x slower                                                                       |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-pythonperf2-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.01 ms: 1.19x faster                                                              |
| regex_dna      | 239 ms                                                       | 226 ms: 1.06x faster                                                               |
| regex_v8       | 23.6 ms                                                      | 26.4 ms: 1.12x slower                                                              |
| regex_compile  | 144 ms                                                       | 165 ms: 1.14x slower                                                               |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-pythonperf2-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 92.0 ms: 1.07x slower                                                              |
| json_loads           | 24.4 us                                                      | 26.7 us: 1.10x slower                                                              |
| xml_etree_iterparse  | 103 ms                                                       | 114 ms: 1.11x slower                                                               |
| xml_etree_parse      | 144 ms                                                       | 163 ms: 1.13x slower                                                               |
| xml_etree_process    | 58.4 ms                                                      | 67.8 ms: 1.16x slower                                                              |
| json_dumps           | 10.2 ms                                                      | 12.3 ms: 1.20x slower                                                              |
| pickle_pure_python   | 318 us                                                       | 404 us: 1.27x slower                                                               |
| tomli_loads          | 2.16 sec                                                     | 2.75 sec: 1.28x slower                                                             |
| unpickle_pure_python | 210 us                                                       | 275 us: 1.31x slower                                                               |
| Geometric mean       | (ref)                                                        | 1.18x slower                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-pythonperf2-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.26 ms: 1.07x slower                                                              |
| python_startup         | 11.6 ms                                                      | 16.4 ms: 1.41x slower                                                              |
| Geometric mean         | (ref)                                                        | 1.23x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-pythonperf2-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|-----------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| django_template | 38.2 ms                                                      | 42.4 ms: 1.11x slower                                                              |
| mako            | 10.0 ms                                                      | 12.9 ms: 1.29x slower                                                              |
| Geometric mean  | (ref)                                                        | 1.20x slower                                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250225-pythonperf2-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------------|:------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.05 sec                                                     | 713 ms: 1.48x faster                                                               |
| async_tree_io              | 1.04 sec                                                     | 713 ms: 1.46x faster                                                               |
| async_tree_memoization_tg  | 540 ms                                                       | 372 ms: 1.45x faster                                                               |
| async_tree_none            | 452 ms                                                       | 319 ms: 1.41x faster                                                               |
| async_tree_none_tg         | 431 ms                                                       | 307 ms: 1.40x faster                                                               |
| async_tree_memoization     | 544 ms                                                       | 390 ms: 1.40x faster                                                               |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 568 ms: 1.23x faster                                                               |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 586 ms: 1.19x faster                                                               |
| regex_effbot               | 3.57 ms                                                      | 3.01 ms: 1.19x faster                                                              |
| deepcopy                   | 368 us                                                       | 320 us: 1.15x faster                                                               |
| pathlib                    | 18.9 ms                                                      | 17.4 ms: 1.09x faster                                                              |
| comprehensions             | 21.9 us                                                      | 20.3 us: 1.08x faster                                                              |
| regex_dna                  | 239 ms                                                       | 226 ms: 1.06x faster                                                               |
| sqlalchemy_declarative     | 159 ms                                                       | 154 ms: 1.04x faster                                                               |
| coroutines                 | 23.0 ms                                                      | 22.6 ms: 1.02x faster                                                              |
| generators                 | 37.4 ms                                                      | 37.0 ms: 1.01x faster                                                              |
| deepcopy_reduce            | 3.37 us                                                      | 3.33 us: 1.01x faster                                                              |
| sympy_sum                  | 162 ms                                                       | 164 ms: 1.01x slower                                                               |
| deepcopy_memo              | 36.8 us                                                      | 37.9 us: 1.03x slower                                                              |
| sympy_integrate            | 23.9 ms                                                      | 24.7 ms: 1.03x slower                                                              |
| sqlalchemy_imperative      | 18.7 ms                                                      | 19.3 ms: 1.03x slower                                                              |
| sqlite_synth               | 2.77 us                                                      | 2.88 us: 1.04x slower                                                              |
| docutils                   | 2.87 sec                                                     | 2.98 sec: 1.04x slower                                                             |
| sympy_str                  | 302 ms                                                       | 316 ms: 1.05x slower                                                               |
| json                       | 5.12 ms                                                      | 5.40 ms: 1.06x slower                                                              |
| xml_etree_generate         | 86.1 ms                                                      | 92.0 ms: 1.07x slower                                                              |
| python_startup_no_site     | 8.64 ms                                                      | 9.26 ms: 1.07x slower                                                              |
| crypto_pyaes               | 80.3 ms                                                      | 86.4 ms: 1.08x slower                                                              |
| 2to3                       | 285 ms                                                       | 307 ms: 1.08x slower                                                               |
| logging_format             | 7.48 us                                                      | 8.07 us: 1.08x slower                                                              |
| spectral_norm              | 91.6 ms                                                      | 99.0 ms: 1.08x slower                                                              |
| bench_thread_pool          | 950 us                                                       | 1.03 ms: 1.08x slower                                                              |
| logging_simple             | 6.71 us                                                      | 7.34 us: 1.09x slower                                                              |
| dulwich_log                | 65.4 ms                                                      | 71.5 ms: 1.09x slower                                                              |
| json_loads                 | 24.4 us                                                      | 26.7 us: 1.10x slower                                                              |
| sympy_expand               | 484 ms                                                       | 532 ms: 1.10x slower                                                               |
| mdp                        | 2.57 sec                                                     | 2.83 sec: 1.10x slower                                                             |
| float                      | 76.6 ms                                                      | 84.7 ms: 1.11x slower                                                              |
| pidigits                   | 265 ms                                                       | 293 ms: 1.11x slower                                                               |
| xml_etree_iterparse        | 103 ms                                                       | 114 ms: 1.11x slower                                                               |
| django_template            | 38.2 ms                                                      | 42.4 ms: 1.11x slower                                                              |
| sqlglot_optimize           | 57.5 ms                                                      | 63.9 ms: 1.11x slower                                                              |
| pycparser                  | 1.23 sec                                                     | 1.37 sec: 1.11x slower                                                             |
| meteor_contest             | 128 ms                                                       | 143 ms: 1.11x slower                                                               |
| raytrace                   | 298 ms                                                       | 333 ms: 1.12x slower                                                               |
| regex_v8                   | 23.6 ms                                                      | 26.4 ms: 1.12x slower                                                              |
| xml_etree_parse            | 144 ms                                                       | 163 ms: 1.13x slower                                                               |
| sqlglot_normalize          | 116 ms                                                       | 131 ms: 1.13x slower                                                               |
| chaos                      | 64.0 ms                                                      | 72.6 ms: 1.13x slower                                                              |
| async_generators           | 390 ms                                                       | 445 ms: 1.14x slower                                                               |
| regex_compile              | 144 ms                                                       | 165 ms: 1.14x slower                                                               |
| xml_etree_process          | 58.4 ms                                                      | 67.8 ms: 1.16x slower                                                              |
| scimark_fft                | 301 ms                                                       | 351 ms: 1.16x slower                                                               |
| sqlglot_transpile          | 1.78 ms                                                      | 2.07 ms: 1.17x slower                                                              |
| go                         | 150 ms                                                       | 175 ms: 1.17x slower                                                               |
| telco                      | 6.96 ms                                                      | 8.17 ms: 1.17x slower                                                              |
| pyflate                    | 439 ms                                                       | 517 ms: 1.18x slower                                                               |
| pprint_pformat             | 1.65 sec                                                     | 1.97 sec: 1.19x slower                                                             |
| scimark_monte_carlo        | 69.0 ms                                                      | 82.3 ms: 1.19x slower                                                              |
| scimark_lu                 | 98.8 ms                                                      | 118 ms: 1.19x slower                                                               |
| coverage                   | 66.7 ms                                                      | 79.8 ms: 1.20x slower                                                              |
| json_dumps                 | 10.2 ms                                                      | 12.3 ms: 1.20x slower                                                              |
| pprint_safe_repr           | 807 ms                                                       | 967 ms: 1.20x slower                                                               |
| typing_runtime_protocols   | 152 us                                                       | 182 us: 1.20x slower                                                               |
| logging_silent             | 94.4 ns                                                      | 114 ns: 1.21x slower                                                               |
| sqlglot_parse              | 1.38 ms                                                      | 1.68 ms: 1.22x slower                                                              |
| nqueens                    | 89.9 ms                                                      | 110 ms: 1.22x slower                                                               |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 5.21 ms: 1.24x slower                                                              |
| pickle_pure_python         | 318 us                                                       | 404 us: 1.27x slower                                                               |
| tomli_loads                | 2.16 sec                                                     | 2.75 sec: 1.28x slower                                                             |
| mako                       | 10.0 ms                                                      | 12.9 ms: 1.29x slower                                                              |
| richards_super             | 51.3 ms                                                      | 66.4 ms: 1.29x slower                                                              |
| richards                   | 45.7 ms                                                      | 59.9 ms: 1.31x slower                                                              |
| unpickle_pure_python       | 210 us                                                       | 275 us: 1.31x slower                                                               |
| deltablue                  | 3.24 ms                                                      | 4.36 ms: 1.35x slower                                                              |
| scimark_sor                | 109 ms                                                       | 147 ms: 1.35x slower                                                               |
| hexiom                     | 5.96 ms                                                      | 8.11 ms: 1.36x slower                                                              |
| nbody                      | 88.0 ms                                                      | 123 ms: 1.40x slower                                                               |
| python_startup             | 11.6 ms                                                      | 16.4 ms: 1.41x slower                                                              |
| fannkuch                   | 350 ms                                                       | 496 ms: 1.42x slower                                                               |
| gc_traversal               | 3.48 ms                                                      | 5.31 ms: 1.53x slower                                                              |
| create_gc_cycles           | 1.59 ms                                                      | 2.77 ms: 1.74x slower                                                              |
| bench_mp_pool              | 4.76 ms                                                      | 1.09 sec: 228.41x slower                                                           |
| Geometric mean             | (ref)                                                        | 1.16x slower                                                                       |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250225-3.14.0a5+-da5ad58-CLANG/bm-20250225-pythonperf2-x86_64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.082x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.09x
- 95% likely to have a slowdown of 1.08x
- 99% likely to have a slowdown of 1.06x

# Memory
- memory change: 1.10x