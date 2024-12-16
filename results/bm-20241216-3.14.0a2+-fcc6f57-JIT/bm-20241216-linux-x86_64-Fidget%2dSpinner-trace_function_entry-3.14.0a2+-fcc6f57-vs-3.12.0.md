# Results vs. 3.12.0

- fork: Fidget-Spinner
- ref: trace_function_entry
- machine: linux-x86_64
- commit hash: fcc6f57
- commit date: 2024-12-16
- overall geometric mean: 1.114x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241216-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 257 ms: 1.07x faster                                                             |
| docutils       | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                           |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241216-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 611 ms: 1.93x faster                                                             |
| async_tree_io              | 1.16 sec                                               | 616 ms: 1.88x faster                                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 308 ms: 1.87x faster                                                             |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.81x faster                                                             |
| async_tree_none            | 472 ms                                                 | 267 ms: 1.77x faster                                                             |
| async_tree_memoization     | 578 ms                                                 | 333 ms: 1.73x faster                                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 482 ms: 1.51x faster                                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 497 ms: 1.46x faster                                                             |
| Geometric mean             | (ref)                                                  | 1.74x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241216-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 82.8 ms: 1.17x faster                                                            |
| float          | 84.7 ms                                                | 73.5 ms: 1.15x faster                                                            |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                             |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241216-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.18x faster                                                             |
| regex_effbot   | 3.61 ms                                                | 3.21 ms: 1.12x faster                                                            |
| regex_dna      | 212 ms                                                 | 209 ms: 1.02x faster                                                             |
| regex_v8       | 23.1 ms                                                | 25.0 ms: 1.08x slower                                                            |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241216-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.82 sec: 1.28x faster                                                           |
| unpickle_pure_python | 230 us                                                 | 193 us: 1.19x faster                                                             |
| xml_etree_parse      | 159 ms                                                 | 136 ms: 1.17x faster                                                             |
| xml_etree_generate   | 89.2 ms                                                | 76.9 ms: 1.16x faster                                                            |
| xml_etree_process    | 61.7 ms                                                | 54.3 ms: 1.14x faster                                                            |
| xml_etree_iterparse  | 107 ms                                                 | 96.0 ms: 1.11x faster                                                            |
| json_loads           | 28.5 us                                                | 25.9 us: 1.10x faster                                                            |
| pickle_pure_python   | 324 us                                                 | 314 us: 1.03x faster                                                             |
| json_dumps           | 10.4 ms                                                | 11.1 ms: 1.07x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.12x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241216-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                            |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241216-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.1 ms: 1.17x faster                                                            |
| django_template | 34.6 ms                                                | 31.9 ms: 1.08x faster                                                            |
| Geometric mean  | (ref)                                                  | 1.13x faster                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241216-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 611 ms: 1.93x faster                                                             |
| async_tree_io              | 1.16 sec                                               | 616 ms: 1.88x faster                                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 308 ms: 1.87x faster                                                             |
| async_tree_none_tg         | 450 ms                                                 | 248 ms: 1.81x faster                                                             |
| async_tree_none            | 472 ms                                                 | 267 ms: 1.77x faster                                                             |
| async_tree_memoization     | 578 ms                                                 | 333 ms: 1.73x faster                                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 482 ms: 1.51x faster                                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 497 ms: 1.46x faster                                                             |
| deepcopy                   | 371 us                                                 | 263 us: 1.41x faster                                                             |
| deepcopy_memo              | 40.7 us                                                | 31.5 us: 1.29x faster                                                            |
| comprehensions             | 21.8 us                                                | 16.9 us: 1.28x faster                                                            |
| tomli_loads                | 2.33 sec                                               | 1.82 sec: 1.28x faster                                                           |
| crypto_pyaes               | 81.9 ms                                                | 66.6 ms: 1.23x faster                                                            |
| scimark_fft                | 382 ms                                                 | 312 ms: 1.23x faster                                                             |
| deepcopy_reduce            | 3.35 us                                                | 2.74 us: 1.22x faster                                                            |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.20x faster                                                            |
| unpickle_pure_python       | 230 us                                                 | 193 us: 1.19x faster                                                             |
| scimark_monte_carlo        | 75.1 ms                                                | 63.1 ms: 1.19x faster                                                            |
| regex_compile              | 148 ms                                                 | 126 ms: 1.18x faster                                                             |
| mako                       | 11.9 ms                                                | 10.1 ms: 1.17x faster                                                            |
| nbody                      | 97.0 ms                                                | 82.8 ms: 1.17x faster                                                            |
| xml_etree_parse            | 159 ms                                                 | 136 ms: 1.17x faster                                                             |
| xml_etree_generate         | 89.2 ms                                                | 76.9 ms: 1.16x faster                                                            |
| float                      | 84.7 ms                                                | 73.5 ms: 1.15x faster                                                            |
| sqlalchemy_declarative     | 147 ms                                                 | 128 ms: 1.14x faster                                                             |
| raytrace                   | 312 ms                                                 | 273 ms: 1.14x faster                                                             |
| logging_format             | 7.23 us                                                | 6.35 us: 1.14x faster                                                            |
| go                         | 139 ms                                                 | 123 ms: 1.14x faster                                                             |
| logging_simple             | 6.46 us                                                | 5.68 us: 1.14x faster                                                            |
| xml_etree_process          | 61.7 ms                                                | 54.3 ms: 1.14x faster                                                            |
| regex_effbot               | 3.61 ms                                                | 3.21 ms: 1.12x faster                                                            |
| spectral_norm              | 115 ms                                                 | 103 ms: 1.12x faster                                                             |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                                             |
| generators                 | 31.2 ms                                                | 28.0 ms: 1.11x faster                                                            |
| xml_etree_iterparse        | 107 ms                                                 | 96.0 ms: 1.11x faster                                                            |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.55 ms: 1.11x faster                                                            |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.8 ms: 1.11x faster                                                            |
| json_loads                 | 28.5 us                                                | 25.9 us: 1.10x faster                                                            |
| async_generators           | 463 ms                                                 | 422 ms: 1.10x faster                                                             |
| fannkuch                   | 417 ms                                                 | 381 ms: 1.09x faster                                                             |
| json                       | 5.26 ms                                                | 4.83 ms: 1.09x faster                                                            |
| chaos                      | 67.0 ms                                                | 61.7 ms: 1.09x faster                                                            |
| pyflate                    | 482 ms                                                 | 445 ms: 1.08x faster                                                             |
| django_template            | 34.6 ms                                                | 31.9 ms: 1.08x faster                                                            |
| sympy_str                  | 300 ms                                                 | 277 ms: 1.08x faster                                                             |
| 2to3                       | 274 ms                                                 | 257 ms: 1.07x faster                                                             |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.07x faster                                                            |
| mdp                        | 2.63 sec                                               | 2.48 sec: 1.06x faster                                                           |
| deltablue                  | 3.72 ms                                                | 3.51 ms: 1.06x faster                                                            |
| sqlglot_transpile          | 1.68 ms                                                | 1.60 ms: 1.06x faster                                                            |
| sympy_integrate            | 21.4 ms                                                | 20.4 ms: 1.05x faster                                                            |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                             |
| sqlite_synth               | 2.83 us                                                | 2.71 us: 1.04x faster                                                            |
| sqlglot_normalize          | 110 ms                                                 | 106 ms: 1.04x faster                                                             |
| scimark_sor                | 129 ms                                                 | 125 ms: 1.04x faster                                                             |
| pickle_pure_python         | 324 us                                                 | 314 us: 1.03x faster                                                             |
| pprint_safe_repr           | 776 ms                                                 | 752 ms: 1.03x faster                                                             |
| docutils                   | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                           |
| dulwich_log                | 68.5 ms                                                | 66.9 ms: 1.02x faster                                                            |
| sqlglot_optimize           | 54.8 ms                                                | 53.6 ms: 1.02x faster                                                            |
| nqueens                    | 83.3 ms                                                | 81.6 ms: 1.02x faster                                                            |
| regex_dna                  | 212 ms                                                 | 209 ms: 1.02x faster                                                             |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.01x faster                                                             |
| sympy_expand               | 478 ms                                                 | 472 ms: 1.01x faster                                                             |
| richards                   | 45.8 ms                                                | 45.5 ms: 1.01x faster                                                            |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                             |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                                             |
| richards_super             | 51.5 ms                                                | 52.2 ms: 1.01x slower                                                            |
| coroutines                 | 23.2 ms                                                | 23.5 ms: 1.01x slower                                                            |
| python_startup_no_site     | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                            |
| bench_thread_pool          | 842 us                                                 | 872 us: 1.04x slower                                                             |
| logging_silent             | 104 ns                                                 | 109 ns: 1.04x slower                                                             |
| typing_runtime_protocols   | 158 us                                                 | 165 us: 1.04x slower                                                             |
| hexiom                     | 6.41 ms                                                | 6.71 ms: 1.05x slower                                                            |
| telco                      | 7.10 ms                                                | 7.51 ms: 1.06x slower                                                            |
| json_dumps                 | 10.4 ms                                                | 11.1 ms: 1.07x slower                                                            |
| regex_v8                   | 23.1 ms                                                | 25.0 ms: 1.08x slower                                                            |
| coverage                   | 72.7 ms                                                | 82.8 ms: 1.14x slower                                                            |
| mypy2                      | 830 ms                                                 | 953 ms: 1.15x slower                                                             |
| gc_traversal               | 3.79 ms                                                | 4.76 ms: 1.25x slower                                                            |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                            |
| create_gc_cycles           | 1.48 ms                                                | 2.45 ms: 1.66x slower                                                            |
| bench_mp_pool              | 24.0 ms                                                | 81.5 ms: 3.39x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                                     |

Benchmark hidden because not significant (2): pprint_pformat, pycparser
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241216-3.14.0a2+-fcc6f57-JIT/bm-20241216-linux-x86_64-Fidget%2dSpinner-trace_function_entry-3.14.0a2+-fcc6f57.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.114x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.12x