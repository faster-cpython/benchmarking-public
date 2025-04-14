# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: trace_function_entry
- machine: linux-aarch64
- commit hash: 553888a
- commit date: 2025-03-07
- overall geometric mean: 1.040x faster
- HPT reliability: 99.96%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250307-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 305 ms: 1.01x faster                                                               |
| html5lib       | 65.1 ms                                                               | 62.2 ms: 1.05x faster                                                              |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                                       |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250307-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 379 ms: 1.65x faster                                                               |
| async_tree_memoization     | 777 ms                                                                | 478 ms: 1.63x faster                                                               |
| async_tree_io              | 1.41 sec                                                              | 887 ms: 1.59x faster                                                               |
| async_tree_memoization_tg  | 740 ms                                                                | 470 ms: 1.57x faster                                                               |
| async_tree_io_tg           | 1.40 sec                                                              | 896 ms: 1.57x faster                                                               |
| async_tree_none_tg         | 577 ms                                                                | 373 ms: 1.55x faster                                                               |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 662 ms: 1.38x faster                                                               |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 651 ms: 1.36x faster                                                               |
| Geometric mean             | (ref)                                                                 | 1.53x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250307-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 82.8 ms: 1.11x faster                                                              |
| nbody          | 105 ms                                                                | 122 ms: 1.16x slower                                                               |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                                       |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250307-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 3.93 ms: 1.18x faster                                                              |
| regex_compile  | 137 ms                                                                | 128 ms: 1.07x faster                                                               |
| regex_dna      | 254 ms                                                                | 242 ms: 1.05x faster                                                               |
| regex_v8       | 28.3 ms                                                               | 29.8 ms: 1.05x slower                                                              |
| Geometric mean | (ref)                                                                 | 1.06x faster                                                                       |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250307-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| xml_etree_parse      | 195 ms                                                                | 176 ms: 1.11x faster                                                               |
| xml_etree_generate   | 112 ms                                                                | 106 ms: 1.06x faster                                                               |
| xml_etree_iterparse  | 150 ms                                                                | 144 ms: 1.04x faster                                                               |
| xml_etree_process    | 79.0 ms                                                               | 75.7 ms: 1.04x faster                                                              |
| tomli_loads          | 2.59 sec                                                              | 2.49 sec: 1.04x faster                                                             |
| unpickle_pure_python | 260 us                                                                | 276 us: 1.06x slower                                                               |
| json_dumps           | 12.3 ms                                                               | 13.6 ms: 1.11x slower                                                              |
| pickle_pure_python   | 365 us                                                                | 407 us: 1.11x slower                                                               |
| json_loads           | 30.7 us                                                               | 34.3 us: 1.12x slower                                                              |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                                       |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250307-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 10.1 ms: 1.21x slower                                                              |
| python_startup         | 11.4 ms                                                               | 16.0 ms: 1.41x slower                                                              |
| Geometric mean         | (ref)                                                                 | 1.30x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250307-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 39.0 ms: 1.04x faster                                                              |
| genshi_text     | 27.4 ms                                                               | 26.6 ms: 1.03x faster                                                              |
| mako            | 12.9 ms                                                               | 13.2 ms: 1.03x slower                                                              |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                                       |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250307-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_none            | 624 ms                                                                | 379 ms: 1.65x faster                                                               |
| async_tree_memoization     | 777 ms                                                                | 478 ms: 1.63x faster                                                               |
| async_tree_io              | 1.41 sec                                                              | 887 ms: 1.59x faster                                                               |
| async_tree_memoization_tg  | 740 ms                                                                | 470 ms: 1.57x faster                                                               |
| async_tree_io_tg           | 1.40 sec                                                              | 896 ms: 1.57x faster                                                               |
| async_tree_none_tg         | 577 ms                                                                | 373 ms: 1.55x faster                                                               |
| deepcopy                   | 446 us                                                                | 320 us: 1.39x faster                                                               |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 662 ms: 1.38x faster                                                               |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 651 ms: 1.36x faster                                                               |
| deepcopy_memo              | 49.6 us                                                               | 37.4 us: 1.33x faster                                                              |
| deepcopy_reduce            | 4.10 us                                                               | 3.38 us: 1.21x faster                                                              |
| generators                 | 43.5 ms                                                               | 36.2 ms: 1.20x faster                                                              |
| regex_effbot               | 4.64 ms                                                               | 3.93 ms: 1.18x faster                                                              |
| spectral_norm              | 131 ms                                                                | 113 ms: 1.15x faster                                                               |
| async_generators           | 491 ms                                                                | 427 ms: 1.15x faster                                                               |
| go                         | 157 ms                                                                | 138 ms: 1.14x faster                                                               |
| raytrace                   | 353 ms                                                                | 310 ms: 1.14x faster                                                               |
| pylint                     | 355 ms                                                                | 313 ms: 1.13x faster                                                               |
| float                      | 92.1 ms                                                               | 82.8 ms: 1.11x faster                                                              |
| logging_simple             | 7.63 us                                                               | 6.88 us: 1.11x faster                                                              |
| logging_format             | 8.34 us                                                               | 7.53 us: 1.11x faster                                                              |
| xml_etree_parse            | 195 ms                                                                | 176 ms: 1.11x faster                                                               |
| pathlib                    | 24.5 ms                                                               | 22.5 ms: 1.09x faster                                                              |
| comprehensions             | 25.4 us                                                               | 23.6 us: 1.07x faster                                                              |
| regex_compile              | 137 ms                                                                | 128 ms: 1.07x faster                                                               |
| sqlalchemy_declarative     | 157 ms                                                                | 147 ms: 1.07x faster                                                               |
| chaos                      | 71.4 ms                                                               | 67.0 ms: 1.06x faster                                                              |
| xml_etree_generate         | 112 ms                                                                | 106 ms: 1.06x faster                                                               |
| sympy_sum                  | 154 ms                                                                | 147 ms: 1.05x faster                                                               |
| regex_dna                  | 254 ms                                                                | 242 ms: 1.05x faster                                                               |
| html5lib                   | 65.1 ms                                                               | 62.2 ms: 1.05x faster                                                              |
| xml_etree_iterparse        | 150 ms                                                                | 144 ms: 1.04x faster                                                               |
| xml_etree_process          | 79.0 ms                                                               | 75.7 ms: 1.04x faster                                                              |
| tomli_loads                | 2.59 sec                                                              | 2.49 sec: 1.04x faster                                                             |
| django_template            | 40.7 ms                                                               | 39.0 ms: 1.04x faster                                                              |
| sympy_str                  | 280 ms                                                                | 269 ms: 1.04x faster                                                               |
| genshi_text                | 27.4 ms                                                               | 26.6 ms: 1.03x faster                                                              |
| sympy_integrate            | 21.6 ms                                                               | 21.1 ms: 1.03x faster                                                              |
| mdp                        | 3.41 sec                                                              | 3.33 sec: 1.03x faster                                                             |
| deltablue                  | 4.12 ms                                                               | 4.03 ms: 1.02x faster                                                              |
| pyflate                    | 559 ms                                                                | 553 ms: 1.01x faster                                                               |
| 2to3                       | 308 ms                                                                | 305 ms: 1.01x faster                                                               |
| bench_thread_pool          | 1.31 ms                                                               | 1.33 ms: 1.02x slower                                                              |
| sqlglot_transpile          | 1.83 ms                                                               | 1.88 ms: 1.03x slower                                                              |
| mako                       | 12.9 ms                                                               | 13.2 ms: 1.03x slower                                                              |
| logging_silent             | 127 ns                                                                | 131 ns: 1.03x slower                                                               |
| sympy_expand               | 454 ms                                                                | 470 ms: 1.04x slower                                                               |
| hexiom                     | 6.98 ms                                                               | 7.24 ms: 1.04x slower                                                              |
| json                       | 5.54 ms                                                               | 5.76 ms: 1.04x slower                                                              |
| regex_v8                   | 28.3 ms                                                               | 29.8 ms: 1.05x slower                                                              |
| sqlglot_parse              | 1.46 ms                                                               | 1.54 ms: 1.05x slower                                                              |
| unpickle_pure_python       | 260 us                                                                | 276 us: 1.06x slower                                                               |
| nqueens                    | 99.2 ms                                                               | 106 ms: 1.07x slower                                                               |
| meteor_contest             | 112 ms                                                                | 121 ms: 1.08x slower                                                               |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.69 ms: 1.08x slower                                                              |
| pycparser                  | 1.26 sec                                                              | 1.37 sec: 1.09x slower                                                             |
| dulwich_log                | 62.0 ms                                                               | 67.6 ms: 1.09x slower                                                              |
| json_dumps                 | 12.3 ms                                                               | 13.6 ms: 1.11x slower                                                              |
| pickle_pure_python         | 365 us                                                                | 407 us: 1.11x slower                                                               |
| telco                      | 8.51 ms                                                               | 9.52 ms: 1.12x slower                                                              |
| json_loads                 | 30.7 us                                                               | 34.3 us: 1.12x slower                                                              |
| coverage                   | 87.3 ms                                                               | 99.6 ms: 1.14x slower                                                              |
| nbody                      | 105 ms                                                                | 122 ms: 1.16x slower                                                               |
| typing_runtime_protocols   | 181 us                                                                | 211 us: 1.17x slower                                                               |
| crypto_pyaes               | 86.6 ms                                                               | 102 ms: 1.17x slower                                                               |
| fannkuch                   | 443 ms                                                                | 529 ms: 1.19x slower                                                               |
| python_startup_no_site     | 8.37 ms                                                               | 10.1 ms: 1.21x slower                                                              |
| python_startup             | 11.4 ms                                                               | 16.0 ms: 1.41x slower                                                              |
| gc_traversal               | 4.40 ms                                                               | 6.67 ms: 1.52x slower                                                              |
| create_gc_cycles           | 1.92 ms                                                               | 3.51 ms: 1.83x slower                                                              |
| bench_mp_pool              | 7.05 ms                                                               | 548 ms: 77.73x slower                                                              |
| Geometric mean             | (ref)                                                                 | 1.02x slower                                                                       |

Benchmark hidden because not significant (13): coroutines, scimark_lu, scimark_monte_carlo, scimark_fft, genshi_xml, richards_super, sqlite_synth, thrift, scimark_sor, asyncio_websockets, sqlalchemy_imperative, richards, pidigits
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, docutils, gunicorn, mypy2, pickle, pickle_dict, pickle_list, pprint_pformat, pprint_safe_repr, sqlglot_normalize, sqlglot_optimize, tornado_http, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20250307-3.14.0a5+-553888a-JIT/bm-20250307-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a5+-553888a.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.040x faster

# HPT report

- Reliability score: 99.96% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 1.05x