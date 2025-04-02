# Results vs. 3.12.0

- fork: brandtbucher
- ref: jit_guard_dict_tuple
- machine: linux-x86_64
- commit hash: 99d6288
- commit date: 2025-04-01
- overall geometric mean: 1.136x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.06x faster
- Memory change: 1.12x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6+-99d6288 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 258 ms: 1.06x faster                                                         |
| docutils       | 2.77 sec                                               | 2.68 sec: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6+-99d6288 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 611 ms: 1.93x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 613 ms: 1.89x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 311 ms: 1.86x faster                                                         |
| async_tree_none            | 472 ms                                                 | 259 ms: 1.82x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 477 ms: 1.52x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 490 ms: 1.48x faster                                                         |
| Geometric mean             | (ref)                                                  | 1.76x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6+-99d6288 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 61.6 ms: 1.38x faster                                                        |
| nbody          | 97.0 ms                                                | 84.0 ms: 1.15x faster                                                        |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.17x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6+-99d6288 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                         |
| regex_effbot   | 3.61 ms                                                | 3.15 ms: 1.15x faster                                                        |
| regex_dna      | 212 ms                                                 | 205 ms: 1.04x faster                                                         |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                 |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6+-99d6288 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.83 sec: 1.27x faster                                                       |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                                         |
| xml_etree_generate   | 89.2 ms                                                | 79.6 ms: 1.12x faster                                                        |
| unpickle_pure_python | 230 us                                                 | 209 us: 1.10x faster                                                         |
| xml_etree_process    | 61.7 ms                                                | 56.5 ms: 1.09x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                 | 98.2 ms: 1.09x faster                                                        |
| pickle_pure_python   | 324 us                                                 | 320 us: 1.01x faster                                                         |
| json_loads           | 28.5 us                                                | 29.7 us: 1.04x slower                                                        |
| json_dumps           | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.07x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6+-99d6288 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.21 ms: 1.18x slower                                                        |
| python_startup         | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6+-99d6288 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.8 ms: 1.09x faster                                                        |
| mako            | 11.9 ms                                                | 10.9 ms: 1.09x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.09x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6+-99d6288 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.22 sec: 2.15x faster                                                       |
| async_tree_io_tg           | 1.18 sec                                               | 611 ms: 1.93x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 613 ms: 1.89x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 311 ms: 1.86x faster                                                         |
| async_tree_none            | 472 ms                                                 | 259 ms: 1.82x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 316 ms: 1.82x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 251 ms: 1.79x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 477 ms: 1.52x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 490 ms: 1.48x faster                                                         |
| deepcopy                   | 371 us                                                 | 254 us: 1.46x faster                                                         |
| deepcopy_memo              | 40.7 us                                                | 29.2 us: 1.39x faster                                                        |
| float                      | 84.7 ms                                                | 61.6 ms: 1.38x faster                                                        |
| richards                   | 45.8 ms                                                | 34.9 ms: 1.31x faster                                                        |
| richards_super             | 51.5 ms                                                | 39.6 ms: 1.30x faster                                                        |
| tomli_loads                | 2.33 sec                                               | 1.83 sec: 1.27x faster                                                       |
| deepcopy_reduce            | 3.35 us                                                | 2.68 us: 1.25x faster                                                        |
| scimark_fft                | 382 ms                                                 | 307 ms: 1.24x faster                                                         |
| raytrace                   | 312 ms                                                 | 260 ms: 1.20x faster                                                         |
| deltablue                  | 3.72 ms                                                | 3.11 ms: 1.20x faster                                                        |
| comprehensions             | 21.8 us                                                | 18.3 us: 1.19x faster                                                        |
| chaos                      | 67.0 ms                                                | 57.0 ms: 1.18x faster                                                        |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                         |
| pathlib                    | 19.3 ms                                                | 16.6 ms: 1.16x faster                                                        |
| spectral_norm              | 115 ms                                                 | 99.1 ms: 1.16x faster                                                        |
| nbody                      | 97.0 ms                                                | 84.0 ms: 1.15x faster                                                        |
| logging_format             | 7.23 us                                                | 6.30 us: 1.15x faster                                                        |
| regex_effbot               | 3.61 ms                                                | 3.15 ms: 1.15x faster                                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 65.6 ms: 1.15x faster                                                        |
| logging_simple             | 6.46 us                                                | 5.65 us: 1.14x faster                                                        |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                         |
| dulwich_log                | 68.5 ms                                                | 60.6 ms: 1.13x faster                                                        |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                                         |
| xml_etree_generate         | 89.2 ms                                                | 79.6 ms: 1.12x faster                                                        |
| async_generators           | 463 ms                                                 | 413 ms: 1.12x faster                                                         |
| go                         | 139 ms                                                 | 125 ms: 1.12x faster                                                         |
| sqlalchemy_declarative     | 147 ms                                                 | 133 ms: 1.11x faster                                                         |
| crypto_pyaes               | 81.9 ms                                                | 74.0 ms: 1.11x faster                                                        |
| sympy_str                  | 300 ms                                                 | 271 ms: 1.10x faster                                                         |
| unpickle_pure_python       | 230 us                                                 | 209 us: 1.10x faster                                                         |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.0 ms: 1.10x faster                                                        |
| xml_etree_process          | 61.7 ms                                                | 56.5 ms: 1.09x faster                                                        |
| pyflate                    | 482 ms                                                 | 442 ms: 1.09x faster                                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.63 ms: 1.09x faster                                                        |
| django_template            | 34.6 ms                                                | 31.8 ms: 1.09x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                 | 98.2 ms: 1.09x faster                                                        |
| sympy_integrate            | 21.4 ms                                                | 19.7 ms: 1.09x faster                                                        |
| mako                       | 11.9 ms                                                | 10.9 ms: 1.09x faster                                                        |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.08x faster                                                         |
| 2to3                       | 274 ms                                                 | 258 ms: 1.06x faster                                                         |
| pycparser                  | 1.18 sec                                               | 1.12 sec: 1.06x faster                                                       |
| generators                 | 31.2 ms                                                | 29.7 ms: 1.05x faster                                                        |
| logging_silent             | 104 ns                                                 | 100 ns: 1.04x faster                                                         |
| sqlite_synth               | 2.83 us                                                | 2.72 us: 1.04x faster                                                        |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                         |
| regex_dna                  | 212 ms                                                 | 205 ms: 1.04x faster                                                         |
| docutils                   | 2.77 sec                                               | 2.68 sec: 1.03x faster                                                       |
| pprint_safe_repr           | 776 ms                                                 | 751 ms: 1.03x faster                                                         |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                                         |
| pprint_pformat             | 1.57 sec                                               | 1.54 sec: 1.02x faster                                                       |
| sympy_expand               | 478 ms                                                 | 471 ms: 1.02x faster                                                         |
| pickle_pure_python         | 324 us                                                 | 320 us: 1.01x faster                                                         |
| fannkuch                   | 417 ms                                                 | 414 ms: 1.01x faster                                                         |
| nqueens                    | 83.3 ms                                                | 82.8 ms: 1.01x faster                                                        |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                         |
| coroutines                 | 23.2 ms                                                | 23.6 ms: 1.02x slower                                                        |
| json_loads                 | 28.5 us                                                | 29.7 us: 1.04x slower                                                        |
| hexiom                     | 6.41 ms                                                | 6.72 ms: 1.05x slower                                                        |
| bench_thread_pool          | 842 us                                                 | 887 us: 1.05x slower                                                         |
| typing_runtime_protocols   | 158 us                                                 | 169 us: 1.07x slower                                                         |
| telco                      | 7.10 ms                                                | 7.86 ms: 1.11x slower                                                        |
| json_dumps                 | 10.4 ms                                                | 11.5 ms: 1.11x slower                                                        |
| python_startup_no_site     | 6.94 ms                                                | 8.21 ms: 1.18x slower                                                        |
| coverage                   | 72.7 ms                                                | 86.0 ms: 1.18x slower                                                        |
| gc_traversal               | 3.79 ms                                                | 4.99 ms: 1.31x slower                                                        |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                        |
| create_gc_cycles           | 1.48 ms                                                | 2.49 ms: 1.69x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 83.4 ms: 3.47x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.11x faster                                                                 |

Benchmark hidden because not significant (3): asyncio_websockets, regex_v8, json
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250401-3.14.0a6+-99d6288-JIT/bm-20250401-linux-x86_64-brandtbucher-jit_guard_dict_tuple-3.14.0a6+-99d6288.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.136x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.08x
- 95% likely to have a speedup of 1.08x
- 99% likely to have a speedup of 1.06x

# Memory
- memory change: 1.12x