# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: trace_function_entry
- machine: linux-x86_64
- commit hash: fcc6f57
- commit date: 2024-12-16
- overall geometric mean: 1.016x faster
- HPT reliability: 78.62%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241216-pythonperf2-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                       | 289 ms: 1.01x slower                                                                   |
| docutils       | 2.87 sec                                                     | 3.01 sec: 1.05x slower                                                                 |
| Geometric mean | (ref)                                                        | 1.03x slower                                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241216-pythonperf2-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 335 ms: 1.61x faster                                                                   |
| async_tree_io_tg           | 1.05 sec                                                     | 654 ms: 1.61x faster                                                                   |
| async_tree_io              | 1.04 sec                                                     | 662 ms: 1.57x faster                                                                   |
| async_tree_none_tg         | 431 ms                                                       | 274 ms: 1.57x faster                                                                   |
| async_tree_none            | 452 ms                                                       | 296 ms: 1.52x faster                                                                   |
| async_tree_memoization     | 544 ms                                                       | 362 ms: 1.50x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 510 ms: 1.37x faster                                                                   |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 527 ms: 1.32x faster                                                                   |
| Geometric mean             | (ref)                                                        | 1.51x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241216-pythonperf2-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| pidigits       | 265 ms                                                       | 251 ms: 1.05x faster                                                                   |
| float          | 76.6 ms                                                      | 79.3 ms: 1.03x slower                                                                  |
| nbody          | 88.0 ms                                                      | 91.2 ms: 1.04x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.01x slower                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241216-pythonperf2-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_effbot   | 3.57 ms                                                      | 3.26 ms: 1.10x faster                                                                  |
| regex_compile  | 144 ms                                                       | 139 ms: 1.03x faster                                                                   |
| regex_dna      | 239 ms                                                       | 247 ms: 1.03x slower                                                                   |
| regex_v8       | 23.6 ms                                                      | 25.4 ms: 1.08x slower                                                                  |
| Geometric mean | (ref)                                                        | 1.00x faster                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241216-pythonperf2-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| xml_etree_generate   | 86.1 ms                                                      | 79.3 ms: 1.09x faster                                                                  |
| xml_etree_parse      | 144 ms                                                       | 135 ms: 1.07x faster                                                                   |
| xml_etree_iterparse  | 103 ms                                                       | 96.3 ms: 1.07x faster                                                                  |
| unpickle_pure_python | 210 us                                                       | 198 us: 1.06x faster                                                                   |
| xml_etree_process    | 58.4 ms                                                      | 56.4 ms: 1.04x faster                                                                  |
| tomli_loads          | 2.16 sec                                                     | 2.10 sec: 1.03x faster                                                                 |
| json_loads           | 24.4 us                                                      | 25.4 us: 1.04x slower                                                                  |
| pickle_pure_python   | 318 us                                                       | 339 us: 1.07x slower                                                                   |
| json_dumps           | 10.2 ms                                                      | 11.2 ms: 1.10x slower                                                                  |
| Geometric mean       | (ref)                                                        | 1.02x faster                                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241216-pythonperf2-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup_no_site | 8.64 ms                                                      | 9.08 ms: 1.05x slower                                                                  |
| python_startup         | 11.6 ms                                                      | 16.1 ms: 1.39x slower                                                                  |
| Geometric mean         | (ref)                                                        | 1.21x slower                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241216-pythonperf2-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|-----------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| mako            | 10.0 ms                                                      | 9.47 ms: 1.06x faster                                                                  |
| django_template | 38.2 ms                                                      | 38.5 ms: 1.01x slower                                                                  |
| Geometric mean  | (ref)                                                        | 1.02x faster                                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241216-pythonperf2-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------------|:------------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 540 ms                                                       | 335 ms: 1.61x faster                                                                   |
| async_tree_io_tg           | 1.05 sec                                                     | 654 ms: 1.61x faster                                                                   |
| async_tree_io              | 1.04 sec                                                     | 662 ms: 1.57x faster                                                                   |
| async_tree_none_tg         | 431 ms                                                       | 274 ms: 1.57x faster                                                                   |
| async_tree_none            | 452 ms                                                       | 296 ms: 1.52x faster                                                                   |
| async_tree_memoization     | 544 ms                                                       | 362 ms: 1.50x faster                                                                   |
| async_tree_cpu_io_mixed_tg | 697 ms                                                       | 510 ms: 1.37x faster                                                                   |
| async_tree_cpu_io_mixed    | 696 ms                                                       | 527 ms: 1.32x faster                                                                   |
| deepcopy                   | 368 us                                                       | 291 us: 1.27x faster                                                                   |
| generators                 | 37.4 ms                                                      | 30.4 ms: 1.23x faster                                                                  |
| deepcopy_memo              | 36.8 us                                                      | 29.9 us: 1.23x faster                                                                  |
| deepcopy_reduce            | 3.37 us                                                      | 2.95 us: 1.14x faster                                                                  |
| comprehensions             | 21.9 us                                                      | 19.3 us: 1.14x faster                                                                  |
| pathlib                    | 18.9 ms                                                      | 16.6 ms: 1.14x faster                                                                  |
| sqlalchemy_declarative     | 159 ms                                                       | 144 ms: 1.11x faster                                                                   |
| regex_effbot               | 3.57 ms                                                      | 3.26 ms: 1.10x faster                                                                  |
| scimark_monte_carlo        | 69.0 ms                                                      | 63.3 ms: 1.09x faster                                                                  |
| xml_etree_generate         | 86.1 ms                                                      | 79.3 ms: 1.09x faster                                                                  |
| coroutines                 | 23.0 ms                                                      | 21.3 ms: 1.08x faster                                                                  |
| logging_format             | 7.48 us                                                      | 6.96 us: 1.08x faster                                                                  |
| crypto_pyaes               | 80.3 ms                                                      | 75.2 ms: 1.07x faster                                                                  |
| xml_etree_parse            | 144 ms                                                       | 135 ms: 1.07x faster                                                                   |
| xml_etree_iterparse        | 103 ms                                                       | 96.3 ms: 1.07x faster                                                                  |
| go                         | 150 ms                                                       | 141 ms: 1.06x faster                                                                   |
| mako                       | 10.0 ms                                                      | 9.47 ms: 1.06x faster                                                                  |
| unpickle_pure_python       | 210 us                                                       | 198 us: 1.06x faster                                                                   |
| pidigits                   | 265 ms                                                       | 251 ms: 1.05x faster                                                                   |
| logging_simple             | 6.71 us                                                      | 6.39 us: 1.05x faster                                                                  |
| dulwich_log                | 65.4 ms                                                      | 62.9 ms: 1.04x faster                                                                  |
| sympy_sum                  | 162 ms                                                       | 156 ms: 1.04x faster                                                                   |
| xml_etree_process          | 58.4 ms                                                      | 56.4 ms: 1.04x faster                                                                  |
| regex_compile              | 144 ms                                                       | 139 ms: 1.03x faster                                                                   |
| sqlalchemy_imperative      | 18.7 ms                                                      | 18.2 ms: 1.03x faster                                                                  |
| spectral_norm              | 91.6 ms                                                      | 88.9 ms: 1.03x faster                                                                  |
| tomli_loads                | 2.16 sec                                                     | 2.10 sec: 1.03x faster                                                                 |
| mdp                        | 2.57 sec                                                     | 2.51 sec: 1.02x faster                                                                 |
| scimark_lu                 | 98.8 ms                                                      | 97.9 ms: 1.01x faster                                                                  |
| scimark_fft                | 301 ms                                                       | 300 ms: 1.00x faster                                                                   |
| sympy_integrate            | 23.9 ms                                                      | 23.8 ms: 1.00x faster                                                                  |
| pyflate                    | 439 ms                                                       | 437 ms: 1.00x faster                                                                   |
| pprint_pformat             | 1.65 sec                                                     | 1.65 sec: 1.00x faster                                                                 |
| django_template            | 38.2 ms                                                      | 38.5 ms: 1.01x slower                                                                  |
| sqlite_synth               | 2.77 us                                                      | 2.81 us: 1.01x slower                                                                  |
| 2to3                       | 285 ms                                                       | 289 ms: 1.01x slower                                                                   |
| meteor_contest             | 128 ms                                                       | 132 ms: 1.03x slower                                                                   |
| json                       | 5.12 ms                                                      | 5.27 ms: 1.03x slower                                                                  |
| regex_dna                  | 239 ms                                                       | 247 ms: 1.03x slower                                                                   |
| float                      | 76.6 ms                                                      | 79.3 ms: 1.03x slower                                                                  |
| nbody                      | 88.0 ms                                                      | 91.2 ms: 1.04x slower                                                                  |
| json_loads                 | 24.4 us                                                      | 25.4 us: 1.04x slower                                                                  |
| docutils                   | 2.87 sec                                                     | 3.01 sec: 1.05x slower                                                                 |
| python_startup_no_site     | 8.64 ms                                                      | 9.08 ms: 1.05x slower                                                                  |
| scimark_sor                | 109 ms                                                       | 115 ms: 1.05x slower                                                                   |
| pycparser                  | 1.23 sec                                                     | 1.30 sec: 1.05x slower                                                                 |
| raytrace                   | 298 ms                                                       | 315 ms: 1.06x slower                                                                   |
| chaos                      | 64.0 ms                                                      | 67.8 ms: 1.06x slower                                                                  |
| pickle_pure_python         | 318 us                                                       | 339 us: 1.07x slower                                                                   |
| fannkuch                   | 350 ms                                                       | 373 ms: 1.07x slower                                                                   |
| sqlglot_transpile          | 1.78 ms                                                      | 1.90 ms: 1.07x slower                                                                  |
| logging_silent             | 94.4 ns                                                      | 101 ns: 1.07x slower                                                                   |
| sympy_expand               | 484 ms                                                       | 520 ms: 1.07x slower                                                                   |
| regex_v8                   | 23.6 ms                                                      | 25.4 ms: 1.08x slower                                                                  |
| sqlglot_normalize          | 116 ms                                                       | 125 ms: 1.08x slower                                                                   |
| sqlglot_parse              | 1.38 ms                                                      | 1.49 ms: 1.09x slower                                                                  |
| sqlglot_optimize           | 57.5 ms                                                      | 62.5 ms: 1.09x slower                                                                  |
| telco                      | 6.96 ms                                                      | 7.63 ms: 1.10x slower                                                                  |
| json_dumps                 | 10.2 ms                                                      | 11.2 ms: 1.10x slower                                                                  |
| async_generators           | 390 ms                                                       | 429 ms: 1.10x slower                                                                   |
| hexiom                     | 5.96 ms                                                      | 6.77 ms: 1.14x slower                                                                  |
| deltablue                  | 3.24 ms                                                      | 3.70 ms: 1.14x slower                                                                  |
| richards                   | 45.7 ms                                                      | 52.6 ms: 1.15x slower                                                                  |
| richards_super             | 51.3 ms                                                      | 59.4 ms: 1.16x slower                                                                  |
| scimark_sparse_mat_mult    | 4.21 ms                                                      | 4.89 ms: 1.16x slower                                                                  |
| coverage                   | 66.7 ms                                                      | 81.1 ms: 1.22x slower                                                                  |
| typing_runtime_protocols   | 152 us                                                       | 186 us: 1.23x slower                                                                   |
| mypy2                      | 830 ms                                                       | 1.05 sec: 1.26x slower                                                                 |
| python_startup             | 11.6 ms                                                      | 16.1 ms: 1.39x slower                                                                  |
| create_gc_cycles           | 1.59 ms                                                      | 2.72 ms: 1.71x slower                                                                  |
| gc_traversal               | 3.48 ms                                                      | 6.53 ms: 1.88x slower                                                                  |
| bench_mp_pool              | 4.76 ms                                                      | 938 ms: 197.02x slower                                                                 |
| Geometric mean             | (ref)                                                        | 1.05x slower                                                                           |

Benchmark hidden because not significant (5): nqueens, sympy_str, pprint_safe_repr, asyncio_websockets, bench_thread_pool
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-pythonperf2-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241216-3.14.0a2+-fcc6f57-JIT/bm-20241216-pythonperf2-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.016x faster

# HPT report

- Reliability score: 78.62% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x