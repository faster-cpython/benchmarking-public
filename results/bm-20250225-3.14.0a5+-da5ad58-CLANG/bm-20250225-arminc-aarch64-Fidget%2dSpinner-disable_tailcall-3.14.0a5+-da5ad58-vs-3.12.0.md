# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: disable_tailcall
- machine: linux-aarch64
- commit hash: da5ad58
- commit date: 2025-02-25
- overall geometric mean: 1.067x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250225-arminc-aarch64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 308 ms                                                                | 337 ms: 1.09x slower                                                           |
| docutils       | 2.98 sec                                                              | 3.16 sec: 1.06x slower                                                         |
| html5lib       | 65.1 ms                                                               | 70.3 ms: 1.08x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.08x slower                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250225-arminc-aarch64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 534 ms: 1.45x faster                                                           |
| async_tree_none            | 624 ms                                                                | 434 ms: 1.44x faster                                                           |
| async_tree_io_tg           | 1.40 sec                                                              | 993 ms: 1.41x faster                                                           |
| async_tree_io              | 1.41 sec                                                              | 999 ms: 1.41x faster                                                           |
| async_tree_memoization_tg  | 740 ms                                                                | 529 ms: 1.40x faster                                                           |
| async_tree_none_tg         | 577 ms                                                                | 422 ms: 1.37x faster                                                           |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 761 ms: 1.16x faster                                                           |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 789 ms: 1.16x faster                                                           |
| Geometric mean             | (ref)                                                                 | 1.35x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250225-arminc-aarch64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| float          | 92.1 ms                                                               | 100 ms: 1.09x slower                                                           |
| pidigits       | 233 ms                                                                | 310 ms: 1.33x slower                                                           |
| nbody          | 105 ms                                                                | 145 ms: 1.39x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.26x slower                                                                   |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250225-arminc-aarch64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.20 ms: 1.10x faster                                                          |
| regex_dna      | 254 ms                                                                | 244 ms: 1.04x faster                                                           |
| regex_compile  | 137 ms                                                                | 156 ms: 1.14x slower                                                           |
| regex_v8       | 28.3 ms                                                               | 35.4 ms: 1.25x slower                                                          |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250225-arminc-aarch64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 150 ms                                                                | 164 ms: 1.09x slower                                                           |
| xml_etree_parse      | 195 ms                                                                | 216 ms: 1.11x slower                                                           |
| xml_etree_generate   | 112 ms                                                                | 125 ms: 1.11x slower                                                           |
| xml_etree_process    | 79.0 ms                                                               | 92.9 ms: 1.18x slower                                                          |
| json_loads           | 30.7 us                                                               | 36.6 us: 1.19x slower                                                          |
| tomli_loads          | 2.59 sec                                                              | 3.26 sec: 1.26x slower                                                         |
| pickle_pure_python   | 365 us                                                                | 465 us: 1.27x slower                                                           |
| unpickle_pure_python | 260 us                                                                | 333 us: 1.28x slower                                                           |
| json_dumps           | 12.3 ms                                                               | 15.9 ms: 1.29x slower                                                          |
| Geometric mean       | (ref)                                                                 | 1.20x slower                                                                   |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250225-arminc-aarch64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.39 ms: 1.12x slower                                                          |
| python_startup         | 11.4 ms                                                               | 16.9 ms: 1.49x slower                                                          |
| Geometric mean         | (ref)                                                                 | 1.29x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250225-arminc-aarch64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| django_template | 40.7 ms                                                               | 45.5 ms: 1.12x slower                                                          |
| genshi_xml      | 60.6 ms                                                               | 73.1 ms: 1.21x slower                                                          |
| genshi_text     | 27.4 ms                                                               | 33.7 ms: 1.23x slower                                                          |
| mako            | 12.9 ms                                                               | 16.0 ms: 1.24x slower                                                          |
| Geometric mean  | (ref)                                                                 | 1.20x slower                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20250225-arminc-aarch64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58 |
|----------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_memoization     | 777 ms                                                                | 534 ms: 1.45x faster                                                           |
| async_tree_none            | 624 ms                                                                | 434 ms: 1.44x faster                                                           |
| async_tree_io_tg           | 1.40 sec                                                              | 993 ms: 1.41x faster                                                           |
| async_tree_io              | 1.41 sec                                                              | 999 ms: 1.41x faster                                                           |
| async_tree_memoization_tg  | 740 ms                                                                | 529 ms: 1.40x faster                                                           |
| async_tree_none_tg         | 577 ms                                                                | 422 ms: 1.37x faster                                                           |
| deepcopy                   | 446 us                                                                | 379 us: 1.17x faster                                                           |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 761 ms: 1.16x faster                                                           |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 789 ms: 1.16x faster                                                           |
| comprehensions             | 25.4 us                                                               | 22.4 us: 1.13x faster                                                          |
| regex_effbot               | 4.64 ms                                                               | 4.20 ms: 1.10x faster                                                          |
| pylint                     | 355 ms                                                                | 324 ms: 1.09x faster                                                           |
| pathlib                    | 24.5 ms                                                               | 23.3 ms: 1.05x faster                                                          |
| spectral_norm              | 131 ms                                                                | 125 ms: 1.05x faster                                                           |
| regex_dna                  | 254 ms                                                                | 244 ms: 1.04x faster                                                           |
| sqlalchemy_declarative     | 157 ms                                                                | 154 ms: 1.02x faster                                                           |
| deepcopy_reduce            | 4.10 us                                                               | 4.03 us: 1.02x faster                                                          |
| mdp                        | 3.41 sec                                                              | 3.46 sec: 1.01x slower                                                         |
| sqlalchemy_imperative      | 16.7 ms                                                               | 17.4 ms: 1.04x slower                                                          |
| raytrace                   | 353 ms                                                                | 368 ms: 1.04x slower                                                           |
| asyncio_websockets         | 658 ms                                                                | 686 ms: 1.04x slower                                                           |
| sympy_sum                  | 154 ms                                                                | 161 ms: 1.04x slower                                                           |
| docutils                   | 2.98 sec                                                              | 3.16 sec: 1.06x slower                                                         |
| bench_thread_pool          | 1.31 ms                                                               | 1.40 ms: 1.07x slower                                                          |
| scimark_fft                | 418 ms                                                                | 448 ms: 1.07x slower                                                           |
| html5lib                   | 65.1 ms                                                               | 70.3 ms: 1.08x slower                                                          |
| logging_format             | 8.34 us                                                               | 9.02 us: 1.08x slower                                                          |
| sympy_str                  | 280 ms                                                                | 303 ms: 1.08x slower                                                           |
| float                      | 92.1 ms                                                               | 100 ms: 1.09x slower                                                           |
| xml_etree_iterparse        | 150 ms                                                                | 164 ms: 1.09x slower                                                           |
| sympy_integrate            | 21.6 ms                                                               | 23.5 ms: 1.09x slower                                                          |
| logging_simple             | 7.63 us                                                               | 8.33 us: 1.09x slower                                                          |
| 2to3                       | 308 ms                                                                | 337 ms: 1.09x slower                                                           |
| xml_etree_parse            | 195 ms                                                                | 216 ms: 1.11x slower                                                           |
| xml_etree_generate         | 112 ms                                                                | 125 ms: 1.11x slower                                                           |
| go                         | 157 ms                                                                | 175 ms: 1.12x slower                                                           |
| generators                 | 43.5 ms                                                               | 48.5 ms: 1.12x slower                                                          |
| coroutines                 | 29.0 ms                                                               | 32.4 ms: 1.12x slower                                                          |
| django_template            | 40.7 ms                                                               | 45.5 ms: 1.12x slower                                                          |
| python_startup_no_site     | 8.37 ms                                                               | 9.39 ms: 1.12x slower                                                          |
| dulwich_log                | 62.0 ms                                                               | 69.5 ms: 1.12x slower                                                          |
| sqlite_synth               | 3.77 us                                                               | 4.26 us: 1.13x slower                                                          |
| pyflate                    | 559 ms                                                                | 633 ms: 1.13x slower                                                           |
| regex_compile              | 137 ms                                                                | 156 ms: 1.14x slower                                                           |
| json                       | 5.54 ms                                                               | 6.34 ms: 1.15x slower                                                          |
| sqlglot_transpile          | 1.83 ms                                                               | 2.09 ms: 1.15x slower                                                          |
| sqlglot_optimize           | 61.3 ms                                                               | 70.4 ms: 1.15x slower                                                          |
| pycparser                  | 1.26 sec                                                              | 1.44 sec: 1.15x slower                                                         |
| chaos                      | 71.4 ms                                                               | 82.2 ms: 1.15x slower                                                          |
| logging_silent             | 127 ns                                                                | 147 ns: 1.16x slower                                                           |
| thrift                     | 937 us                                                                | 1.09 ms: 1.17x slower                                                          |
| crypto_pyaes               | 86.6 ms                                                               | 101 ms: 1.17x slower                                                           |
| meteor_contest             | 112 ms                                                                | 131 ms: 1.17x slower                                                           |
| deltablue                  | 4.12 ms                                                               | 4.82 ms: 1.17x slower                                                          |
| sympy_expand               | 454 ms                                                                | 532 ms: 1.17x slower                                                           |
| xml_etree_process          | 79.0 ms                                                               | 92.9 ms: 1.18x slower                                                          |
| scimark_lu                 | 146 ms                                                                | 172 ms: 1.18x slower                                                           |
| coverage                   | 87.3 ms                                                               | 104 ms: 1.19x slower                                                           |
| telco                      | 8.51 ms                                                               | 10.1 ms: 1.19x slower                                                          |
| scimark_monte_carlo        | 85.1 ms                                                               | 101 ms: 1.19x slower                                                           |
| json_loads                 | 30.7 us                                                               | 36.6 us: 1.19x slower                                                          |
| sqlglot_normalize          | 126 ms                                                                | 151 ms: 1.20x slower                                                           |
| sqlglot_parse              | 1.46 ms                                                               | 1.76 ms: 1.20x slower                                                          |
| typing_runtime_protocols   | 181 us                                                                | 217 us: 1.20x slower                                                           |
| nqueens                    | 99.2 ms                                                               | 120 ms: 1.20x slower                                                           |
| genshi_xml                 | 60.6 ms                                                               | 73.1 ms: 1.21x slower                                                          |
| richards                   | 50.9 ms                                                               | 61.6 ms: 1.21x slower                                                          |
| genshi_text                | 27.4 ms                                                               | 33.7 ms: 1.23x slower                                                          |
| pprint_pformat             | 1.88 sec                                                              | 2.32 sec: 1.23x slower                                                         |
| scimark_sor                | 150 ms                                                                | 185 ms: 1.24x slower                                                           |
| pprint_safe_repr           | 916 ms                                                                | 1.14 sec: 1.24x slower                                                         |
| mako                       | 12.9 ms                                                               | 16.0 ms: 1.24x slower                                                          |
| regex_v8                   | 28.3 ms                                                               | 35.4 ms: 1.25x slower                                                          |
| richards_super             | 58.5 ms                                                               | 73.0 ms: 1.25x slower                                                          |
| tomli_loads                | 2.59 sec                                                              | 3.26 sec: 1.26x slower                                                         |
| pickle_pure_python         | 365 us                                                                | 465 us: 1.27x slower                                                           |
| unpickle_pure_python       | 260 us                                                                | 333 us: 1.28x slower                                                           |
| json_dumps                 | 12.3 ms                                                               | 15.9 ms: 1.29x slower                                                          |
| hexiom                     | 6.98 ms                                                               | 9.10 ms: 1.30x slower                                                          |
| pidigits                   | 233 ms                                                                | 310 ms: 1.33x slower                                                           |
| nbody                      | 105 ms                                                                | 145 ms: 1.39x slower                                                           |
| fannkuch                   | 443 ms                                                                | 624 ms: 1.41x slower                                                           |
| python_startup             | 11.4 ms                                                               | 16.9 ms: 1.49x slower                                                          |
| gc_traversal               | 4.40 ms                                                               | 6.79 ms: 1.54x slower                                                          |
| create_gc_cycles           | 1.92 ms                                                               | 3.79 ms: 1.97x slower                                                          |
| bench_mp_pool              | 7.05 ms                                                               | 8.30 sec: 1176.56x slower                                                      |
| Geometric mean             | (ref)                                                                 | 1.19x slower                                                                   |

Benchmark hidden because not significant (3): deepcopy_memo, async_generators, scimark_sparse_mat_mult
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (7) of results/bm-20250225-3.14.0a5+-da5ad58-CLANG/bm-20250225-arminc-aarch64-Fidget%2dSpinner-disable_tailcall-3.14.0a5+-da5ad58.json: bpe_tokeniser, connected_components, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.067x slower

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.10x