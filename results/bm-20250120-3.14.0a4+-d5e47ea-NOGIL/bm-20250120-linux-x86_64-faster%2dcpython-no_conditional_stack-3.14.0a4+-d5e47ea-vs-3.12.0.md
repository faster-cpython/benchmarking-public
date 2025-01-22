# Results vs. 3.12.0

- fork: faster-cpython
- ref: no_conditional_stack
- machine: linux-x86_64
- commit hash: d5e47ea
- commit date: 2025-01-20
- overall geometric mean: 1.044x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.30x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250120-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d5e47ea |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 313 ms: 1.14x slower                                                             |
| docutils       | 2.77 sec                                               | 2.87 sec: 1.04x slower                                                           |
| Geometric mean | (ref)                                                  | 1.09x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250120-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d5e47ea |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 551 ms: 2.15x faster                                                             |
| async_tree_io              | 1.16 sec                                               | 606 ms: 1.91x faster                                                             |
| async_tree_none_tg         | 450 ms                                                 | 241 ms: 1.87x faster                                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 321 ms: 1.79x faster                                                             |
| async_tree_none            | 472 ms                                                 | 292 ms: 1.61x faster                                                             |
| async_tree_memoization     | 578 ms                                                 | 372 ms: 1.55x faster                                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 469 ms: 1.55x faster                                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 523 ms: 1.39x faster                                                             |
| Geometric mean             | (ref)                                                  | 1.71x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250120-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d5e47ea |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 78.9 ms: 1.07x faster                                                            |
| pidigits       | 187 ms                                                 | 190 ms: 1.01x slower                                                             |
| nbody          | 97.0 ms                                                | 139 ms: 1.43x slower                                                             |
| Geometric mean | (ref)                                                  | 1.11x slower                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250120-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d5e47ea |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.36 ms: 1.07x faster                                                            |
| regex_compile  | 148 ms                                                 | 153 ms: 1.03x slower                                                             |
| regex_dna      | 212 ms                                                 | 223 ms: 1.05x slower                                                             |
| regex_v8       | 23.1 ms                                                | 25.0 ms: 1.08x slower                                                            |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250120-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d5e47ea |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 107 ms                                                 | 96.4 ms: 1.11x faster                                                            |
| xml_etree_parse      | 159 ms                                                 | 150 ms: 1.06x faster                                                             |
| tomli_loads          | 2.33 sec                                               | 2.45 sec: 1.05x slower                                                           |
| xml_etree_generate   | 89.2 ms                                                | 96.8 ms: 1.09x slower                                                            |
| json_loads           | 28.5 us                                                | 31.7 us: 1.11x slower                                                            |
| xml_etree_process    | 61.7 ms                                                | 72.1 ms: 1.17x slower                                                            |
| pickle_pure_python   | 324 us                                                 | 382 us: 1.18x slower                                                             |
| unpickle_pure_python | 230 us                                                 | 273 us: 1.18x slower                                                             |
| json_dumps           | 10.4 ms                                                | 12.8 ms: 1.23x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.09x slower                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250120-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d5e47ea |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 9.37 ms: 1.35x slower                                                            |
| python_startup         | 9.55 ms                                                | 15.1 ms: 1.58x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.46x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250120-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d5e47ea |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 41.7 ms: 1.20x slower                                                            |
| mako            | 11.9 ms                                                | 16.5 ms: 1.39x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.29x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250120-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d5e47ea |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 551 ms: 2.15x faster                                                             |
| async_tree_io              | 1.16 sec                                               | 606 ms: 1.91x faster                                                             |
| async_tree_none_tg         | 450 ms                                                 | 241 ms: 1.87x faster                                                             |
| async_tree_memoization_tg  | 575 ms                                                 | 321 ms: 1.79x faster                                                             |
| async_tree_none            | 472 ms                                                 | 292 ms: 1.61x faster                                                             |
| async_tree_memoization     | 578 ms                                                 | 372 ms: 1.55x faster                                                             |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 469 ms: 1.55x faster                                                             |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 523 ms: 1.39x faster                                                             |
| pathlib                    | 19.3 ms                                                | 16.4 ms: 1.18x faster                                                            |
| deepcopy                   | 371 us                                                 | 319 us: 1.16x faster                                                             |
| xml_etree_iterparse        | 107 ms                                                 | 96.4 ms: 1.11x faster                                                            |
| regex_effbot               | 3.61 ms                                                | 3.36 ms: 1.07x faster                                                            |
| float                      | 84.7 ms                                                | 78.9 ms: 1.07x faster                                                            |
| xml_etree_parse            | 159 ms                                                 | 150 ms: 1.06x faster                                                             |
| async_generators           | 463 ms                                                 | 437 ms: 1.06x faster                                                             |
| sqlite_synth               | 2.83 us                                                | 2.75 us: 1.03x faster                                                            |
| deepcopy_memo              | 40.7 us                                                | 39.7 us: 1.03x faster                                                            |
| comprehensions             | 21.8 us                                                | 21.2 us: 1.03x faster                                                            |
| deepcopy_reduce            | 3.35 us                                                | 3.26 us: 1.02x faster                                                            |
| generators                 | 31.2 ms                                                | 31.6 ms: 1.01x slower                                                            |
| pidigits                   | 187 ms                                                 | 190 ms: 1.01x slower                                                             |
| pycparser                  | 1.18 sec                                               | 1.21 sec: 1.03x slower                                                           |
| regex_compile              | 148 ms                                                 | 153 ms: 1.03x slower                                                             |
| docutils                   | 2.77 sec                                               | 2.87 sec: 1.04x slower                                                           |
| go                         | 139 ms                                                 | 145 ms: 1.04x slower                                                             |
| mdp                        | 2.63 sec                                               | 2.73 sec: 1.04x slower                                                           |
| spectral_norm              | 115 ms                                                 | 119 ms: 1.04x slower                                                             |
| dulwich_log                | 68.5 ms                                                | 71.3 ms: 1.04x slower                                                            |
| tomli_loads                | 2.33 sec                                               | 2.45 sec: 1.05x slower                                                           |
| regex_dna                  | 212 ms                                                 | 223 ms: 1.05x slower                                                             |
| json                       | 5.26 ms                                                | 5.58 ms: 1.06x slower                                                            |
| sympy_sum                  | 169 ms                                                 | 180 ms: 1.06x slower                                                             |
| sympy_str                  | 300 ms                                                 | 323 ms: 1.08x slower                                                             |
| regex_v8                   | 23.1 ms                                                | 25.0 ms: 1.08x slower                                                            |
| pyflate                    | 482 ms                                                 | 521 ms: 1.08x slower                                                             |
| logging_simple             | 6.46 us                                                | 7.01 us: 1.09x slower                                                            |
| xml_etree_generate         | 89.2 ms                                                | 96.8 ms: 1.09x slower                                                            |
| scimark_sor                | 129 ms                                                 | 141 ms: 1.10x slower                                                             |
| coroutines                 | 23.2 ms                                                | 25.5 ms: 1.10x slower                                                            |
| sqlglot_normalize          | 110 ms                                                 | 122 ms: 1.11x slower                                                             |
| crypto_pyaes               | 81.9 ms                                                | 90.7 ms: 1.11x slower                                                            |
| logging_format             | 7.23 us                                                | 8.02 us: 1.11x slower                                                            |
| chaos                      | 67.0 ms                                                | 74.3 ms: 1.11x slower                                                            |
| scimark_fft                | 382 ms                                                 | 425 ms: 1.11x slower                                                             |
| json_loads                 | 28.5 us                                                | 31.7 us: 1.11x slower                                                            |
| sqlalchemy_declarative     | 147 ms                                                 | 164 ms: 1.11x slower                                                             |
| pprint_safe_repr           | 776 ms                                                 | 866 ms: 1.12x slower                                                             |
| sympy_integrate            | 21.4 ms                                                | 24.1 ms: 1.13x slower                                                            |
| sqlglot_optimize           | 54.8 ms                                                | 62.0 ms: 1.13x slower                                                            |
| sympy_expand               | 478 ms                                                 | 541 ms: 1.13x slower                                                             |
| 2to3                       | 274 ms                                                 | 313 ms: 1.14x slower                                                             |
| pprint_pformat             | 1.57 sec                                               | 1.79 sec: 1.14x slower                                                           |
| logging_silent             | 104 ns                                                 | 120 ns: 1.15x slower                                                             |
| sqlalchemy_imperative      | 18.7 ms                                                | 21.5 ms: 1.15x slower                                                            |
| raytrace                   | 312 ms                                                 | 360 ms: 1.15x slower                                                             |
| sqlglot_transpile          | 1.68 ms                                                | 1.94 ms: 1.15x slower                                                            |
| create_gc_cycles           | 1.48 ms                                                | 1.71 ms: 1.16x slower                                                            |
| xml_etree_process          | 61.7 ms                                                | 72.1 ms: 1.17x slower                                                            |
| gc_traversal               | 3.79 ms                                                | 4.44 ms: 1.17x slower                                                            |
| meteor_contest             | 112 ms                                                 | 132 ms: 1.17x slower                                                             |
| scimark_monte_carlo        | 75.1 ms                                                | 88.1 ms: 1.17x slower                                                            |
| sqlglot_parse              | 1.36 ms                                                | 1.60 ms: 1.18x slower                                                            |
| pickle_pure_python         | 324 us                                                 | 382 us: 1.18x slower                                                             |
| unpickle_pure_python       | 230 us                                                 | 273 us: 1.18x slower                                                             |
| nqueens                    | 83.3 ms                                                | 99.1 ms: 1.19x slower                                                            |
| scimark_lu                 | 118 ms                                                 | 141 ms: 1.19x slower                                                             |
| richards                   | 45.8 ms                                                | 54.9 ms: 1.20x slower                                                            |
| django_template            | 34.6 ms                                                | 41.7 ms: 1.20x slower                                                            |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 6.13 ms: 1.21x slower                                                            |
| hexiom                     | 6.41 ms                                                | 7.83 ms: 1.22x slower                                                            |
| json_dumps                 | 10.4 ms                                                | 12.8 ms: 1.23x slower                                                            |
| richards_super             | 51.5 ms                                                | 64.0 ms: 1.24x slower                                                            |
| fannkuch                   | 417 ms                                                 | 521 ms: 1.25x slower                                                             |
| deltablue                  | 3.72 ms                                                | 4.77 ms: 1.28x slower                                                            |
| telco                      | 7.10 ms                                                | 9.21 ms: 1.30x slower                                                            |
| python_startup_no_site     | 6.94 ms                                                | 9.37 ms: 1.35x slower                                                            |
| typing_runtime_protocols   | 158 us                                                 | 216 us: 1.37x slower                                                             |
| mako                       | 11.9 ms                                                | 16.5 ms: 1.39x slower                                                            |
| nbody                      | 97.0 ms                                                | 139 ms: 1.43x slower                                                             |
| coverage                   | 72.7 ms                                                | 107 ms: 1.47x slower                                                             |
| python_startup             | 9.55 ms                                                | 15.1 ms: 1.58x slower                                                            |
| bench_mp_pool              | 24.0 ms                                                | 89.8 ms: 3.74x slower                                                            |
| bench_thread_pool          | 842 us                                                 | 3.49 ms: 4.15x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.08x slower                                                                     |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250120-3.14.0a4+-d5e47ea-NOGIL/bm-20250120-linux-x86_64-faster%2dcpython-no_conditional_stack-3.14.0a4+-d5e47ea.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.044x slower

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.30x