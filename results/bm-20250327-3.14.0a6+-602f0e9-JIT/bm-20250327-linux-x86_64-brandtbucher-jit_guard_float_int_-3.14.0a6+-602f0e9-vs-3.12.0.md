# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_guard_float_int_
- machine: linux-x86_64
- commit hash: 602f0e9
- commit date: 2025-03-27
- overall geometric mean: 1.132x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250327-linux-x86_64-brandtbucher-jit_guard_float_int_-3.14.0a6+-602f0e9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 261 ms: 1.05x faster                                                         |
| docutils       | 2.77 sec                                               | 2.66 sec: 1.04x faster                                                       |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250327-linux-x86_64-brandtbucher-jit_guard_float_int_-3.14.0a6+-602f0e9 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 613 ms: 1.93x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 612 ms: 1.89x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.84x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.83x faster                                                         |
| async_tree_none            | 472 ms                                                 | 260 ms: 1.81x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 473 ms: 1.53x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 487 ms: 1.49x faster                                                         |
| Geometric mean             | (ref)                                                  | 1.76x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250327-linux-x86_64-brandtbucher-jit_guard_float_int_-3.14.0a6+-602f0e9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 63.4 ms: 1.34x faster                                                        |
| nbody          | 97.0 ms                                                | 86.3 ms: 1.12x faster                                                        |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.15x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250327-linux-x86_64-brandtbucher-jit_guard_float_int_-3.14.0a6+-602f0e9 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 126 ms: 1.17x faster                                                         |
| regex_effbot   | 3.61 ms                                                | 3.23 ms: 1.12x faster                                                        |
| regex_v8       | 23.1 ms                                                | 23.0 ms: 1.00x faster                                                        |
| regex_dna      | 212 ms                                                 | 219 ms: 1.03x slower                                                         |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250327-linux-x86_64-brandtbucher-jit_guard_float_int_-3.14.0a6+-602f0e9 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.87 sec: 1.25x faster                                                       |
| xml_etree_parse      | 159 ms                                                 | 139 ms: 1.14x faster                                                         |
| xml_etree_generate   | 89.2 ms                                                | 79.0 ms: 1.13x faster                                                        |
| xml_etree_process    | 61.7 ms                                                | 56.0 ms: 1.10x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                 | 98.5 ms: 1.08x faster                                                        |
| unpickle_pure_python | 230 us                                                 | 218 us: 1.05x faster                                                         |
| json_loads           | 28.5 us                                                | 29.7 us: 1.04x slower                                                        |
| json_dumps           | 10.4 ms                                                | 11.6 ms: 1.11x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                                 |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250327-linux-x86_64-brandtbucher-jit_guard_float_int_-3.14.0a6+-602f0e9 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.19 ms: 1.18x slower                                                        |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250327-linux-x86_64-brandtbucher-jit_guard_float_int_-3.14.0a6+-602f0e9 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.0 ms: 1.09x faster                                                        |
| django_template | 34.6 ms                                                | 32.1 ms: 1.08x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250327-linux-x86_64-brandtbucher-jit_guard_float_int_-3.14.0a6+-602f0e9 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.23 sec: 2.14x faster                                                       |
| async_tree_io_tg           | 1.18 sec                                               | 613 ms: 1.93x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 612 ms: 1.89x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 313 ms: 1.84x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.83x faster                                                         |
| async_tree_none            | 472 ms                                                 | 260 ms: 1.81x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 473 ms: 1.53x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 487 ms: 1.49x faster                                                         |
| deepcopy                   | 371 us                                                 | 260 us: 1.42x faster                                                         |
| deepcopy_memo              | 40.7 us                                                | 29.2 us: 1.40x faster                                                        |
| float                      | 84.7 ms                                                | 63.4 ms: 1.34x faster                                                        |
| richards                   | 45.8 ms                                                | 35.5 ms: 1.29x faster                                                        |
| richards_super             | 51.5 ms                                                | 40.8 ms: 1.26x faster                                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.66 us: 1.26x faster                                                        |
| tomli_loads                | 2.33 sec                                               | 1.87 sec: 1.25x faster                                                       |
| scimark_fft                | 382 ms                                                 | 310 ms: 1.23x faster                                                         |
| spectral_norm              | 115 ms                                                 | 94.6 ms: 1.21x faster                                                        |
| deltablue                  | 3.72 ms                                                | 3.07 ms: 1.21x faster                                                        |
| logging_format             | 7.23 us                                                | 6.11 us: 1.18x faster                                                        |
| regex_compile              | 148 ms                                                 | 126 ms: 1.17x faster                                                         |
| raytrace                   | 312 ms                                                 | 266 ms: 1.17x faster                                                         |
| pathlib                    | 19.3 ms                                                | 16.5 ms: 1.17x faster                                                        |
| comprehensions             | 21.8 us                                                | 18.7 us: 1.17x faster                                                        |
| logging_simple             | 6.46 us                                                | 5.55 us: 1.16x faster                                                        |
| chaos                      | 67.0 ms                                                | 58.4 ms: 1.15x faster                                                        |
| xml_etree_parse            | 159 ms                                                 | 139 ms: 1.14x faster                                                         |
| dulwich_log                | 68.5 ms                                                | 60.2 ms: 1.14x faster                                                        |
| xml_etree_generate         | 89.2 ms                                                | 79.0 ms: 1.13x faster                                                        |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.48 ms: 1.13x faster                                                        |
| nbody                      | 97.0 ms                                                | 86.3 ms: 1.12x faster                                                        |
| async_generators           | 463 ms                                                 | 414 ms: 1.12x faster                                                         |
| sqlalchemy_declarative     | 147 ms                                                 | 131 ms: 1.12x faster                                                         |
| regex_effbot               | 3.61 ms                                                | 3.23 ms: 1.12x faster                                                        |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                                         |
| scimark_monte_carlo        | 75.1 ms                                                | 67.5 ms: 1.11x faster                                                        |
| generators                 | 31.2 ms                                                | 28.1 ms: 1.11x faster                                                        |
| go                         | 139 ms                                                 | 126 ms: 1.10x faster                                                         |
| xml_etree_process          | 61.7 ms                                                | 56.0 ms: 1.10x faster                                                        |
| sympy_str                  | 300 ms                                                 | 273 ms: 1.10x faster                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.1 ms: 1.10x faster                                                        |
| pyflate                    | 482 ms                                                 | 441 ms: 1.09x faster                                                         |
| logging_silent             | 104 ns                                                 | 96.2 ns: 1.09x faster                                                        |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.09x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                 | 98.5 ms: 1.08x faster                                                        |
| sympy_integrate            | 21.4 ms                                                | 19.8 ms: 1.08x faster                                                        |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.08x faster                                                         |
| crypto_pyaes               | 81.9 ms                                                | 75.9 ms: 1.08x faster                                                        |
| django_template            | 34.6 ms                                                | 32.1 ms: 1.08x faster                                                        |
| unpickle_pure_python       | 230 us                                                 | 218 us: 1.05x faster                                                         |
| 2to3                       | 274 ms                                                 | 261 ms: 1.05x faster                                                         |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                         |
| pycparser                  | 1.18 sec                                               | 1.13 sec: 1.04x faster                                                       |
| docutils                   | 2.77 sec                                               | 2.66 sec: 1.04x faster                                                       |
| sqlite_synth               | 2.83 us                                                | 2.73 us: 1.04x faster                                                        |
| sympy_expand               | 478 ms                                                 | 472 ms: 1.01x faster                                                         |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                         |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                         |
| regex_v8                   | 23.1 ms                                                | 23.0 ms: 1.00x faster                                                        |
| nqueens                    | 83.3 ms                                                | 83.7 ms: 1.01x slower                                                        |
| json                       | 5.26 ms                                                | 5.34 ms: 1.02x slower                                                        |
| pprint_pformat             | 1.57 sec                                               | 1.60 sec: 1.02x slower                                                       |
| regex_dna                  | 212 ms                                                 | 219 ms: 1.03x slower                                                         |
| hexiom                     | 6.41 ms                                                | 6.69 ms: 1.04x slower                                                        |
| json_loads                 | 28.5 us                                                | 29.7 us: 1.04x slower                                                        |
| bench_thread_pool          | 842 us                                                 | 880 us: 1.05x slower                                                         |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                                         |
| json_dumps                 | 10.4 ms                                                | 11.6 ms: 1.11x slower                                                        |
| telco                      | 7.10 ms                                                | 8.02 ms: 1.13x slower                                                        |
| coverage                   | 72.7 ms                                                | 83.7 ms: 1.15x slower                                                        |
| python_startup_no_site     | 6.94 ms                                                | 8.19 ms: 1.18x slower                                                        |
| gc_traversal               | 3.79 ms                                                | 4.76 ms: 1.25x slower                                                        |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.37x slower                                                        |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.67x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 83.0 ms: 3.46x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.11x faster                                                                 |

Benchmark hidden because not significant (5): asyncio_websockets, pickle_pure_python, fannkuch, coroutines, pprint_safe_repr
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250327-3.14.0a6+-602f0e9-JIT/bm-20250327-linux-x86_64-brandtbucher-jit_guard_float_int_-3.14.0a6+-602f0e9.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.132x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.12x