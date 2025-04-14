# Results vs. 3.12.0

- fork: kumaraditya303
- ref: per_thread_cur_task
- machine: linux-x86_64
- commit hash: ba92dfb
- commit date: 2025-02-10
- overall geometric mean: 1.113x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 257 ms: 1.07x faster                                                          |
| docutils       | 2.77 sec                                               | 2.66 sec: 1.04x faster                                                        |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 616 ms: 1.92x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 617 ms: 1.87x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 321 ms: 1.79x faster                                                          |
| async_tree_none            | 472 ms                                                 | 264 ms: 1.79x faster                                                          |
| async_tree_memoization     | 578 ms                                                 | 324 ms: 1.78x faster                                                          |
| async_tree_none_tg         | 450 ms                                                 | 256 ms: 1.76x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 486 ms: 1.49x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 497 ms: 1.46x faster                                                          |
| Geometric mean             | (ref)                                                  | 1.72x faster                                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 70.8 ms: 1.20x faster                                                         |
| nbody          | 97.0 ms                                                | 94.5 ms: 1.03x faster                                                         |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 125 ms: 1.19x faster                                                          |
| regex_effbot   | 3.61 ms                                                | 3.23 ms: 1.12x faster                                                         |
| regex_v8       | 23.1 ms                                                | 24.1 ms: 1.04x slower                                                         |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                  |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.84 sec: 1.26x faster                                                        |
| unpickle_pure_python | 230 us                                                 | 198 us: 1.16x faster                                                          |
| xml_etree_parse      | 159 ms                                                 | 138 ms: 1.16x faster                                                          |
| xml_etree_generate   | 89.2 ms                                                | 78.5 ms: 1.13x faster                                                         |
| xml_etree_process    | 61.7 ms                                                | 55.1 ms: 1.12x faster                                                         |
| xml_etree_iterparse  | 107 ms                                                 | 96.0 ms: 1.11x faster                                                         |
| pickle_pure_python   | 324 us                                                 | 315 us: 1.03x faster                                                          |
| json_loads           | 28.5 us                                                | 29.0 us: 1.02x slower                                                         |
| json_dumps           | 10.4 ms                                                | 12.0 ms: 1.16x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                         |
| python_startup         | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                         |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.2 ms: 1.17x faster                                                         |
| django_template | 34.6 ms                                                | 32.2 ms: 1.07x faster                                                         |
| Geometric mean  | (ref)                                                  | 1.12x faster                                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb |
|----------------------------|:------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 616 ms: 1.92x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 617 ms: 1.87x faster                                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 321 ms: 1.79x faster                                                          |
| async_tree_none            | 472 ms                                                 | 264 ms: 1.79x faster                                                          |
| async_tree_memoization     | 578 ms                                                 | 324 ms: 1.78x faster                                                          |
| async_tree_none_tg         | 450 ms                                                 | 256 ms: 1.76x faster                                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 486 ms: 1.49x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 497 ms: 1.46x faster                                                          |
| deepcopy                   | 371 us                                                 | 257 us: 1.44x faster                                                          |
| deepcopy_memo              | 40.7 us                                                | 30.7 us: 1.33x faster                                                         |
| comprehensions             | 21.8 us                                                | 17.2 us: 1.27x faster                                                         |
| tomli_loads                | 2.33 sec                                               | 1.84 sec: 1.26x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.66 us: 1.26x faster                                                         |
| scimark_fft                | 382 ms                                                 | 313 ms: 1.22x faster                                                          |
| spectral_norm              | 115 ms                                                 | 95.7 ms: 1.20x faster                                                         |
| float                      | 84.7 ms                                                | 70.8 ms: 1.20x faster                                                         |
| regex_compile              | 148 ms                                                 | 125 ms: 1.19x faster                                                          |
| logging_format             | 7.23 us                                                | 6.10 us: 1.19x faster                                                         |
| pathlib                    | 19.3 ms                                                | 16.5 ms: 1.17x faster                                                         |
| logging_simple             | 6.46 us                                                | 5.51 us: 1.17x faster                                                         |
| crypto_pyaes               | 81.9 ms                                                | 70.0 ms: 1.17x faster                                                         |
| mako                       | 11.9 ms                                                | 10.2 ms: 1.17x faster                                                         |
| unpickle_pure_python       | 230 us                                                 | 198 us: 1.16x faster                                                          |
| xml_etree_parse            | 159 ms                                                 | 138 ms: 1.16x faster                                                          |
| chaos                      | 67.0 ms                                                | 58.4 ms: 1.15x faster                                                         |
| xml_etree_generate         | 89.2 ms                                                | 78.5 ms: 1.13x faster                                                         |
| scimark_monte_carlo        | 75.1 ms                                                | 66.3 ms: 1.13x faster                                                         |
| raytrace                   | 312 ms                                                 | 276 ms: 1.13x faster                                                          |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.48 ms: 1.13x faster                                                         |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                                          |
| xml_etree_process          | 61.7 ms                                                | 55.1 ms: 1.12x faster                                                         |
| regex_effbot               | 3.61 ms                                                | 3.23 ms: 1.12x faster                                                         |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                                          |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.7 ms: 1.12x faster                                                         |
| async_generators           | 463 ms                                                 | 416 ms: 1.11x faster                                                          |
| xml_etree_iterparse        | 107 ms                                                 | 96.0 ms: 1.11x faster                                                         |
| generators                 | 31.2 ms                                                | 28.4 ms: 1.10x faster                                                         |
| deltablue                  | 3.72 ms                                                | 3.38 ms: 1.10x faster                                                         |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.09x faster                                                          |
| sympy_str                  | 300 ms                                                 | 275 ms: 1.09x faster                                                          |
| pyflate                    | 482 ms                                                 | 446 ms: 1.08x faster                                                          |
| go                         | 139 ms                                                 | 129 ms: 1.08x faster                                                          |
| django_template            | 34.6 ms                                                | 32.2 ms: 1.07x faster                                                         |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.07x faster                                                         |
| 2to3                       | 274 ms                                                 | 257 ms: 1.07x faster                                                          |
| sympy_integrate            | 21.4 ms                                                | 20.1 ms: 1.07x faster                                                         |
| sqlglot_transpile          | 1.68 ms                                                | 1.59 ms: 1.06x faster                                                         |
| pycparser                  | 1.18 sec                                               | 1.11 sec: 1.06x faster                                                        |
| fannkuch                   | 417 ms                                                 | 397 ms: 1.05x faster                                                          |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                          |
| sqlglot_normalize          | 110 ms                                                 | 106 ms: 1.04x faster                                                          |
| richards                   | 45.8 ms                                                | 44.1 ms: 1.04x faster                                                         |
| docutils                   | 2.77 sec                                               | 2.66 sec: 1.04x faster                                                        |
| dulwich_log                | 68.5 ms                                                | 66.0 ms: 1.04x faster                                                         |
| pprint_safe_repr           | 776 ms                                                 | 749 ms: 1.04x faster                                                          |
| sqlite_synth               | 2.83 us                                                | 2.74 us: 1.03x faster                                                         |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.03x faster                                                          |
| mdp                        | 2.63 sec                                               | 2.55 sec: 1.03x faster                                                        |
| pickle_pure_python         | 324 us                                                 | 315 us: 1.03x faster                                                          |
| nbody                      | 97.0 ms                                                | 94.5 ms: 1.03x faster                                                         |
| coroutines                 | 23.2 ms                                                | 22.6 ms: 1.02x faster                                                         |
| sqlglot_optimize           | 54.8 ms                                                | 53.5 ms: 1.02x faster                                                         |
| richards_super             | 51.5 ms                                                | 50.3 ms: 1.02x faster                                                         |
| sympy_expand               | 478 ms                                                 | 468 ms: 1.02x faster                                                          |
| pprint_pformat             | 1.57 sec                                               | 1.54 sec: 1.02x faster                                                        |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                          |
| logging_silent             | 104 ns                                                 | 106 ns: 1.01x slower                                                          |
| json_loads                 | 28.5 us                                                | 29.0 us: 1.02x slower                                                         |
| python_startup_no_site     | 6.94 ms                                                | 7.08 ms: 1.02x slower                                                         |
| typing_runtime_protocols   | 158 us                                                 | 162 us: 1.03x slower                                                          |
| regex_v8                   | 23.1 ms                                                | 24.1 ms: 1.04x slower                                                         |
| bench_thread_pool          | 842 us                                                 | 885 us: 1.05x slower                                                          |
| nqueens                    | 83.3 ms                                                | 88.2 ms: 1.06x slower                                                         |
| hexiom                     | 6.41 ms                                                | 6.86 ms: 1.07x slower                                                         |
| telco                      | 7.10 ms                                                | 7.59 ms: 1.07x slower                                                         |
| json_dumps                 | 10.4 ms                                                | 12.0 ms: 1.16x slower                                                         |
| coverage                   | 72.7 ms                                                | 89.5 ms: 1.23x slower                                                         |
| gc_traversal               | 3.79 ms                                                | 4.72 ms: 1.24x slower                                                         |
| python_startup             | 9.55 ms                                                | 12.9 ms: 1.35x slower                                                         |
| create_gc_cycles           | 1.48 ms                                                | 2.48 ms: 1.68x slower                                                         |
| bench_mp_pool              | 24.0 ms                                                | 81.6 ms: 3.40x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                                  |

Benchmark hidden because not significant (3): json, regex_dna, asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250210-3.14.0a4+-ba92dfb-JIT/bm-20250210-linux-x86_64-kumaraditya303-per_thread_cur_task-3.14.0a4+-ba92dfb.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.113x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.11x