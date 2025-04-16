# Results vs. 3.12.0

- fork: mdboom
- ref: fast_tuple_dealloc
- machine: linux-x86_64
- commit hash: 661a2b8
- commit date: 2025-04-15
- overall geometric mean: 1.114x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.18x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7+-661a2b8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 262 ms: 1.05x faster                                                 |
| docutils       | 2.77 sec                                               | 3.21 sec: 1.16x slower                                               |
| Geometric mean | (ref)                                                  | 1.05x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7+-661a2b8 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 616 ms: 1.92x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 611 ms: 1.89x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 310 ms: 1.86x faster                                                 |
| async_tree_none            | 472 ms                                                 | 258 ms: 1.83x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.81x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 490 ms: 1.48x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 493 ms: 1.47x faster                                                 |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7+-661a2b8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.1 ms: 1.23x faster                                                |
| nbody          | 97.0 ms                                                | 94.6 ms: 1.02x faster                                                |
| pidigits       | 187 ms                                                 | 198 ms: 1.06x slower                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7+-661a2b8 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                 |
| regex_effbot   | 3.61 ms                                                | 3.15 ms: 1.14x faster                                                |
| regex_dna      | 212 ms                                                 | 203 ms: 1.05x faster                                                 |
| regex_v8       | 23.1 ms                                                | 22.7 ms: 1.02x faster                                                |
| Geometric mean | (ref)                                                  | 1.09x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7+-661a2b8 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.98 sec: 1.18x faster                                               |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 98.7 ms: 1.08x faster                                                |
| xml_etree_generate   | 89.2 ms                                                | 84.4 ms: 1.06x faster                                                |
| unpickle_pure_python | 230 us                                                 | 218 us: 1.06x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 58.6 ms: 1.05x faster                                                |
| pickle_pure_python   | 324 us                                                 | 319 us: 1.02x faster                                                 |
| json_loads           | 28.5 us                                                | 29.5 us: 1.04x slower                                                |
| json_dumps           | 10.4 ms                                                | 12.1 ms: 1.17x slower                                                |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7+-661a2b8 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.24 ms: 1.19x slower                                                |
| python_startup         | 9.55 ms                                                | 13.3 ms: 1.39x slower                                                |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7+-661a2b8 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 31.3 ms: 1.10x faster                                                |
| mako            | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7+-661a2b8 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.25 sec: 2.10x faster                                               |
| async_tree_io_tg           | 1.18 sec                                               | 616 ms: 1.92x faster                                                 |
| async_tree_io              | 1.16 sec                                               | 611 ms: 1.89x faster                                                 |
| async_tree_memoization     | 578 ms                                                 | 310 ms: 1.86x faster                                                 |
| async_tree_none            | 472 ms                                                 | 258 ms: 1.83x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                 |
| async_tree_none_tg         | 450 ms                                                 | 249 ms: 1.81x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 490 ms: 1.48x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 493 ms: 1.47x faster                                                 |
| deepcopy                   | 371 us                                                 | 254 us: 1.46x faster                                                 |
| deepcopy_memo              | 40.7 us                                                | 29.7 us: 1.37x faster                                                |
| comprehensions             | 21.8 us                                                | 16.7 us: 1.30x faster                                                |
| deepcopy_reduce            | 3.35 us                                                | 2.69 us: 1.24x faster                                                |
| float                      | 84.7 ms                                                | 69.1 ms: 1.23x faster                                                |
| go                         | 139 ms                                                 | 114 ms: 1.23x faster                                                 |
| raytrace                   | 312 ms                                                 | 264 ms: 1.18x faster                                                 |
| chaos                      | 67.0 ms                                                | 56.6 ms: 1.18x faster                                                |
| tomli_loads                | 2.33 sec                                               | 1.98 sec: 1.18x faster                                               |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                 |
| logging_format             | 7.23 us                                                | 6.25 us: 1.16x faster                                                |
| async_generators           | 463 ms                                                 | 401 ms: 1.16x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.60 us: 1.15x faster                                                |
| pathlib                    | 19.3 ms                                                | 16.8 ms: 1.15x faster                                                |
| dulwich_log                | 68.5 ms                                                | 59.7 ms: 1.15x faster                                                |
| regex_effbot               | 3.61 ms                                                | 3.15 ms: 1.14x faster                                                |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 151 ms: 1.12x faster                                                 |
| sympy_integrate            | 21.4 ms                                                | 19.3 ms: 1.11x faster                                                |
| crypto_pyaes               | 81.9 ms                                                | 73.9 ms: 1.11x faster                                                |
| sympy_str                  | 300 ms                                                 | 271 ms: 1.10x faster                                                 |
| django_template            | 34.6 ms                                                | 31.3 ms: 1.10x faster                                                |
| deltablue                  | 3.72 ms                                                | 3.37 ms: 1.10x faster                                                |
| scimark_monte_carlo        | 75.1 ms                                                | 68.2 ms: 1.10x faster                                                |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.1 ms: 1.09x faster                                                |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.09x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 98.7 ms: 1.08x faster                                                |
| pyflate                    | 482 ms                                                 | 447 ms: 1.08x faster                                                 |
| spectral_norm              | 115 ms                                                 | 106 ms: 1.08x faster                                                 |
| pprint_safe_repr           | 776 ms                                                 | 719 ms: 1.08x faster                                                 |
| sqlalchemy_declarative     | 147 ms                                                 | 137 ms: 1.07x faster                                                 |
| pprint_pformat             | 1.57 sec                                               | 1.46 sec: 1.07x faster                                               |
| scimark_fft                | 382 ms                                                 | 358 ms: 1.07x faster                                                 |
| logging_silent             | 104 ns                                                 | 98.2 ns: 1.06x faster                                                |
| generators                 | 31.2 ms                                                | 29.5 ms: 1.06x faster                                                |
| xml_etree_generate         | 89.2 ms                                                | 84.4 ms: 1.06x faster                                                |
| unpickle_pure_python       | 230 us                                                 | 218 us: 1.06x faster                                                 |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 58.6 ms: 1.05x faster                                                |
| richards                   | 45.8 ms                                                | 43.6 ms: 1.05x faster                                                |
| mako                       | 11.9 ms                                                | 11.3 ms: 1.05x faster                                                |
| 2to3                       | 274 ms                                                 | 262 ms: 1.05x faster                                                 |
| regex_dna                  | 212 ms                                                 | 203 ms: 1.05x faster                                                 |
| richards_super             | 51.5 ms                                                | 49.4 ms: 1.04x faster                                                |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.86 ms: 1.04x faster                                                |
| sympy_expand               | 478 ms                                                 | 463 ms: 1.03x faster                                                 |
| nqueens                    | 83.3 ms                                                | 81.1 ms: 1.03x faster                                                |
| nbody                      | 97.0 ms                                                | 94.6 ms: 1.02x faster                                                |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.02x faster                                               |
| regex_v8                   | 23.1 ms                                                | 22.7 ms: 1.02x faster                                                |
| pickle_pure_python         | 324 us                                                 | 319 us: 1.02x faster                                                 |
| hexiom                     | 6.41 ms                                                | 6.32 ms: 1.01x faster                                                |
| fannkuch                   | 417 ms                                                 | 425 ms: 1.02x slower                                                 |
| json                       | 5.26 ms                                                | 5.36 ms: 1.02x slower                                                |
| json_loads                 | 28.5 us                                                | 29.5 us: 1.04x slower                                                |
| coroutines                 | 23.2 ms                                                | 24.2 ms: 1.05x slower                                                |
| bench_thread_pool          | 842 us                                                 | 892 us: 1.06x slower                                                 |
| pidigits                   | 187 ms                                                 | 198 ms: 1.06x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 169 us: 1.07x slower                                                 |
| telco                      | 7.10 ms                                                | 7.86 ms: 1.11x slower                                                |
| docutils                   | 2.77 sec                                               | 3.21 sec: 1.16x slower                                               |
| json_dumps                 | 10.4 ms                                                | 12.1 ms: 1.17x slower                                                |
| python_startup_no_site     | 6.94 ms                                                | 8.24 ms: 1.19x slower                                                |
| coverage                   | 72.7 ms                                                | 88.4 ms: 1.22x slower                                                |
| gc_traversal               | 3.79 ms                                                | 5.11 ms: 1.35x slower                                                |
| python_startup             | 9.55 ms                                                | 13.3 ms: 1.39x slower                                                |
| create_gc_cycles           | 1.48 ms                                                | 2.48 ms: 1.68x slower                                                |
| bench_mp_pool              | 24.0 ms                                                | 82.1 ms: 3.42x slower                                                |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                         |

Benchmark hidden because not significant (3): asyncio_websockets, sqlite_synth, scimark_lu
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250415-3.14.0a7+-661a2b8/bm-20250415-linux-x86_64-mdboom-fast_tuple_dealloc-3.14.0a7+-661a2b8.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.114x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.18x