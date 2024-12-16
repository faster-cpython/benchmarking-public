# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: trace_function_entry
- machine: linux-aarch64
- commit hash: fcc6f57
- commit date: 2024-12-16
- overall geometric mean: 1.010x slower
- HPT reliability: 51.12%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241216-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| docutils       | 2.98 sec                                                              | 3.22 sec: 1.08x slower                                                             |
| html5lib       | 65.1 ms                                                               | 72.0 ms: 1.11x slower                                                              |
| Geometric mean | (ref)                                                                 | 1.07x slower                                                                       |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241216-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 912 ms: 1.54x faster                                                               |
| async_tree_none            | 624 ms                                                                | 406 ms: 1.54x faster                                                               |
| async_tree_memoization_tg  | 740 ms                                                                | 482 ms: 1.53x faster                                                               |
| async_tree_io              | 1.41 sec                                                              | 920 ms: 1.53x faster                                                               |
| async_tree_memoization     | 777 ms                                                                | 516 ms: 1.50x faster                                                               |
| async_tree_none_tg         | 577 ms                                                                | 390 ms: 1.48x faster                                                               |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 698 ms: 1.31x faster                                                               |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 687 ms: 1.29x faster                                                               |
| Geometric mean             | (ref)                                                                 | 1.46x faster                                                                       |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241216-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| pidigits       | 233 ms                                                                | 240 ms: 1.03x slower                                                               |
| nbody          | 105 ms                                                                | 114 ms: 1.09x slower                                                               |
| Geometric mean | (ref)                                                                 | 1.04x slower                                                                       |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241216-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| regex_effbot   | 4.64 ms                                                               | 4.02 ms: 1.15x faster                                                              |
| regex_dna      | 254 ms                                                                | 266 ms: 1.05x slower                                                               |
| regex_v8       | 28.3 ms                                                               | 32.4 ms: 1.14x slower                                                              |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                                       |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241216-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|---------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| xml_etree_parse     | 195 ms                                                                | 179 ms: 1.09x faster                                                               |
| xml_etree_iterparse | 150 ms                                                                | 144 ms: 1.04x faster                                                               |
| xml_etree_process   | 79.0 ms                                                               | 78.0 ms: 1.01x faster                                                              |
| json_loads          | 30.7 us                                                               | 32.6 us: 1.06x slower                                                              |
| pickle_pure_python  | 365 us                                                                | 431 us: 1.18x slower                                                               |
| json_dumps          | 12.3 ms                                                               | 14.7 ms: 1.20x slower                                                              |
| Geometric mean      | (ref)                                                                 | 1.03x slower                                                                       |

Benchmark hidden because not significant (3): xml_etree_generate, tomli_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241216-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| python_startup_no_site | 8.37 ms                                                               | 9.01 ms: 1.08x slower                                                              |
| python_startup         | 11.4 ms                                                               | 16.1 ms: 1.42x slower                                                              |
| Geometric mean         | (ref)                                                                 | 1.24x slower                                                                       |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241216-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| genshi_text     | 27.4 ms                                                               | 28.8 ms: 1.05x slower                                                              |
| django_template | 40.7 ms                                                               | 43.2 ms: 1.06x slower                                                              |
| mako            | 12.9 ms                                                               | 13.9 ms: 1.08x slower                                                              |
| genshi_xml      | 60.6 ms                                                               | 70.1 ms: 1.16x slower                                                              |
| Geometric mean  | (ref)                                                                 | 1.09x slower                                                                       |

All benchmarks:
===============

| Benchmark                  | bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0 | bm-20241216-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.40 sec                                                              | 912 ms: 1.54x faster                                                               |
| async_tree_none            | 624 ms                                                                | 406 ms: 1.54x faster                                                               |
| async_tree_memoization_tg  | 740 ms                                                                | 482 ms: 1.53x faster                                                               |
| async_tree_io              | 1.41 sec                                                              | 920 ms: 1.53x faster                                                               |
| async_tree_memoization     | 777 ms                                                                | 516 ms: 1.50x faster                                                               |
| async_tree_none_tg         | 577 ms                                                                | 390 ms: 1.48x faster                                                               |
| async_tree_cpu_io_mixed    | 912 ms                                                                | 698 ms: 1.31x faster                                                               |
| async_tree_cpu_io_mixed_tg | 884 ms                                                                | 687 ms: 1.29x faster                                                               |
| deepcopy                   | 446 us                                                                | 350 us: 1.27x faster                                                               |
| deepcopy_memo              | 49.6 us                                                               | 41.4 us: 1.20x faster                                                              |
| generators                 | 43.5 ms                                                               | 37.2 ms: 1.17x faster                                                              |
| regex_effbot               | 4.64 ms                                                               | 4.02 ms: 1.15x faster                                                              |
| deepcopy_reduce            | 4.10 us                                                               | 3.64 us: 1.13x faster                                                              |
| pylint                     | 355 ms                                                                | 319 ms: 1.11x faster                                                               |
| xml_etree_parse            | 195 ms                                                                | 179 ms: 1.09x faster                                                               |
| pathlib                    | 24.5 ms                                                               | 22.8 ms: 1.07x faster                                                              |
| scimark_monte_carlo        | 85.1 ms                                                               | 80.4 ms: 1.06x faster                                                              |
| sqlalchemy_declarative     | 157 ms                                                                | 150 ms: 1.05x faster                                                               |
| go                         | 157 ms                                                                | 150 ms: 1.05x faster                                                               |
| raytrace                   | 353 ms                                                                | 338 ms: 1.05x faster                                                               |
| xml_etree_iterparse        | 150 ms                                                                | 144 ms: 1.04x faster                                                               |
| xml_etree_process          | 79.0 ms                                                               | 78.0 ms: 1.01x faster                                                              |
| bench_thread_pool          | 1.31 ms                                                               | 1.33 ms: 1.01x slower                                                              |
| asyncio_websockets         | 658 ms                                                                | 675 ms: 1.03x slower                                                               |
| pidigits                   | 233 ms                                                                | 240 ms: 1.03x slower                                                               |
| sympy_str                  | 280 ms                                                                | 289 ms: 1.03x slower                                                               |
| sympy_integrate            | 21.6 ms                                                               | 22.4 ms: 1.04x slower                                                              |
| regex_dna                  | 254 ms                                                                | 266 ms: 1.05x slower                                                               |
| genshi_text                | 27.4 ms                                                               | 28.8 ms: 1.05x slower                                                              |
| json_loads                 | 30.7 us                                                               | 32.6 us: 1.06x slower                                                              |
| django_template            | 40.7 ms                                                               | 43.2 ms: 1.06x slower                                                              |
| pyflate                    | 559 ms                                                                | 597 ms: 1.07x slower                                                               |
| sympy_sum                  | 154 ms                                                                | 165 ms: 1.07x slower                                                               |
| richards_super             | 58.5 ms                                                               | 62.6 ms: 1.07x slower                                                              |
| sqlite_synth               | 3.77 us                                                               | 4.05 us: 1.07x slower                                                              |
| python_startup_no_site     | 8.37 ms                                                               | 9.01 ms: 1.08x slower                                                              |
| mako                       | 12.9 ms                                                               | 13.9 ms: 1.08x slower                                                              |
| docutils                   | 2.98 sec                                                              | 3.22 sec: 1.08x slower                                                             |
| scimark_sparse_mat_mult    | 6.19 ms                                                               | 6.69 ms: 1.08x slower                                                              |
| sqlglot_transpile          | 1.83 ms                                                               | 1.98 ms: 1.08x slower                                                              |
| crypto_pyaes               | 86.6 ms                                                               | 94.0 ms: 1.09x slower                                                              |
| richards                   | 50.9 ms                                                               | 55.4 ms: 1.09x slower                                                              |
| nbody                      | 105 ms                                                                | 114 ms: 1.09x slower                                                               |
| scimark_sor                | 150 ms                                                                | 163 ms: 1.09x slower                                                               |
| thrift                     | 937 us                                                                | 1.03 ms: 1.09x slower                                                              |
| sqlalchemy_imperative      | 16.7 ms                                                               | 18.3 ms: 1.10x slower                                                              |
| meteor_contest             | 112 ms                                                                | 123 ms: 1.10x slower                                                               |
| sqlglot_normalize          | 126 ms                                                                | 139 ms: 1.10x slower                                                               |
| logging_silent             | 127 ns                                                                | 140 ns: 1.10x slower                                                               |
| sqlglot_parse              | 1.46 ms                                                               | 1.62 ms: 1.10x slower                                                              |
| html5lib                   | 65.1 ms                                                               | 72.0 ms: 1.11x slower                                                              |
| deltablue                  | 4.12 ms                                                               | 4.56 ms: 1.11x slower                                                              |
| nqueens                    | 99.2 ms                                                               | 111 ms: 1.12x slower                                                               |
| sqlglot_optimize           | 61.3 ms                                                               | 70.2 ms: 1.14x slower                                                              |
| regex_v8                   | 28.3 ms                                                               | 32.4 ms: 1.14x slower                                                              |
| telco                      | 8.51 ms                                                               | 9.78 ms: 1.15x slower                                                              |
| sympy_expand               | 454 ms                                                                | 522 ms: 1.15x slower                                                               |
| coverage                   | 87.3 ms                                                               | 101 ms: 1.16x slower                                                               |
| genshi_xml                 | 60.6 ms                                                               | 70.1 ms: 1.16x slower                                                              |
| fannkuch                   | 443 ms                                                                | 517 ms: 1.17x slower                                                               |
| pickle_pure_python         | 365 us                                                                | 431 us: 1.18x slower                                                               |
| pycparser                  | 1.26 sec                                                              | 1.49 sec: 1.19x slower                                                             |
| json_dumps                 | 12.3 ms                                                               | 14.7 ms: 1.20x slower                                                              |
| hexiom                     | 6.98 ms                                                               | 8.46 ms: 1.21x slower                                                              |
| typing_runtime_protocols   | 181 us                                                                | 220 us: 1.22x slower                                                               |
| mypy2                      | 873 ms                                                                | 1.07 sec: 1.23x slower                                                             |
| chaos                      | 71.4 ms                                                               | 87.9 ms: 1.23x slower                                                              |
| pprint_safe_repr           | 916 ms                                                                | 1.23 sec: 1.35x slower                                                             |
| dulwich_log                | 62.0 ms                                                               | 86.4 ms: 1.39x slower                                                              |
| pprint_pformat             | 1.88 sec                                                              | 2.62 sec: 1.39x slower                                                             |
| python_startup             | 11.4 ms                                                               | 16.1 ms: 1.42x slower                                                              |
| gc_traversal               | 4.40 ms                                                               | 6.90 ms: 1.57x slower                                                              |
| create_gc_cycles           | 1.92 ms                                                               | 3.71 ms: 1.93x slower                                                              |
| bench_mp_pool              | 7.05 ms                                                               | 984 ms: 139.45x slower                                                             |
| Geometric mean             | (ref)                                                                 | 1.09x slower                                                                       |

Benchmark hidden because not significant (16): scimark_lu, comprehensions, xml_etree_generate, regex_compile, logging_simple, tomli_loads, mdp, async_generators, float, spectral_norm, coroutines, scimark_fft, json, 2to3, logging_format, unpickle_pure_python
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-arminc-aarch64-python-0fb18b02c8ad56299d6a-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpickle, unpickle_list
Ignored benchmarks (8) of results/bm-20241216-3.14.0a2+-fcc6f57-JIT/bm-20241216-arminc-aarch64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57.json: bpe_tokeniser, connected_components, djangocms, k_core, many_optionals, shortest_path, sphinx, subparsers

- Geometric mean (including insignificant results): 1.010x slower

# HPT report

- Reliability score: 51.12% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.07x