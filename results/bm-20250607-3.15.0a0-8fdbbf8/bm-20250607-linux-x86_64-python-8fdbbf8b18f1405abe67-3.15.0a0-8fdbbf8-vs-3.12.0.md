# Results vs. 3.12.0

- fork: python
- ref: 8fdbbf8b18f1405abe67
- machine: linux-x86_64
- commit hash: 8fdbbf8
- commit date: 2025-06-07
- overall geometric mean: 1.116x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 254 ms: 1.08x faster                                                  |
| docutils       | 2.77 sec                                               | 2.57 sec: 1.08x faster                                                |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 595 ms: 1.94x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 617 ms: 1.92x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                  |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 494 ms: 1.47x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 505 ms: 1.44x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 71.1 ms: 1.19x faster                                                 |
| nbody          | 97.0 ms                                                | 98.2 ms: 1.01x slower                                                 |
| pidigits       | 187 ms                                                 | 192 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.06 ms: 1.18x faster                                                 |
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                  |
| regex_dna      | 212 ms                                                 | 188 ms: 1.13x faster                                                  |
| regex_v8       | 23.1 ms                                                | 22.4 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.02 sec: 1.15x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 144 ms: 1.11x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 99.3 ms: 1.08x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 85.9 ms: 1.04x faster                                                 |
| pickle_pure_python   | 324 us                                                 | 318 us: 1.02x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 60.7 ms: 1.02x faster                                                 |
| json_loads           | 28.5 us                                                | 28.4 us: 1.00x faster                                                 |
| json_dumps           | 10.4 ms                                                | 10.9 ms: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.90 ms: 1.01x faster                                                 |
| python_startup         | 9.55 ms                                                | 12.1 ms: 1.27x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.12x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.3 ms: 1.07x faster                                                 |
| mako            | 11.9 ms                                                | 11.7 ms: 1.02x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.22 sec: 2.15x faster                                                |
| async_tree_io              | 1.16 sec                                               | 595 ms: 1.94x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 617 ms: 1.92x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 314 ms: 1.83x faster                                                  |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 250 ms: 1.80x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 494 ms: 1.47x faster                                                  |
| deepcopy                   | 371 us                                                 | 255 us: 1.46x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 505 ms: 1.44x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 28.9 us: 1.41x faster                                                 |
| comprehensions             | 21.8 us                                                | 15.9 us: 1.37x faster                                                 |
| go                         | 139 ms                                                 | 111 ms: 1.26x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.70 us: 1.24x faster                                                 |
| float                      | 84.7 ms                                                | 71.1 ms: 1.19x faster                                                 |
| regex_effbot               | 3.61 ms                                                | 3.06 ms: 1.18x faster                                                 |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                  |
| raytrace                   | 312 ms                                                 | 269 ms: 1.16x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 59.2 ms: 1.16x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 2.02 sec: 1.15x faster                                                |
| pathlib                    | 19.3 ms                                                | 17.0 ms: 1.14x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.14x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 18.9 ms: 1.13x faster                                                 |
| regex_dna                  | 212 ms                                                 | 188 ms: 1.13x faster                                                  |
| sympy_str                  | 300 ms                                                 | 266 ms: 1.13x faster                                                  |
| async_generators           | 463 ms                                                 | 412 ms: 1.12x faster                                                  |
| pyflate                    | 482 ms                                                 | 430 ms: 1.12x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 144 ms: 1.11x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 67.9 ms: 1.11x faster                                                 |
| chaos                      | 67.0 ms                                                | 60.6 ms: 1.10x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 75.3 ms: 1.09x faster                                                 |
| 2to3                       | 274 ms                                                 | 254 ms: 1.08x faster                                                  |
| logging_format             | 7.23 us                                                | 6.72 us: 1.08x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 99.3 ms: 1.08x faster                                                 |
| docutils                   | 2.77 sec                                               | 2.57 sec: 1.08x faster                                                |
| django_template            | 34.6 ms                                                | 32.3 ms: 1.07x faster                                                 |
| richards                   | 45.8 ms                                                | 42.9 ms: 1.07x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.48 ms: 1.07x faster                                                 |
| scimark_sor                | 129 ms                                                 | 121 ms: 1.06x faster                                                  |
| logging_simple             | 6.46 us                                                | 6.08 us: 1.06x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                  |
| sympy_expand               | 478 ms                                                 | 451 ms: 1.06x faster                                                  |
| hexiom                     | 6.41 ms                                                | 6.08 ms: 1.05x faster                                                 |
| richards_super             | 51.5 ms                                                | 49.0 ms: 1.05x faster                                                 |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 85.9 ms: 1.04x faster                                                 |
| spectral_norm              | 115 ms                                                 | 111 ms: 1.04x faster                                                  |
| regex_v8                   | 23.1 ms                                                | 22.4 ms: 1.03x faster                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.91 ms: 1.03x faster                                                 |
| nqueens                    | 83.3 ms                                                | 81.4 ms: 1.02x faster                                                 |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.02x faster                                                |
| mako                       | 11.9 ms                                                | 11.7 ms: 1.02x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 318 us: 1.02x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 60.7 ms: 1.02x faster                                                 |
| generators                 | 31.2 ms                                                | 31.0 ms: 1.01x faster                                                 |
| scimark_fft                | 382 ms                                                 | 380 ms: 1.01x faster                                                  |
| python_startup_no_site     | 6.94 ms                                                | 6.90 ms: 1.01x faster                                                 |
| json_loads                 | 28.5 us                                                | 28.4 us: 1.00x faster                                                 |
| scimark_lu                 | 118 ms                                                 | 119 ms: 1.00x slower                                                  |
| sqlite_synth               | 2.83 us                                                | 2.85 us: 1.01x slower                                                 |
| nbody                      | 97.0 ms                                                | 98.2 ms: 1.01x slower                                                 |
| json                       | 5.26 ms                                                | 5.33 ms: 1.01x slower                                                 |
| fannkuch                   | 417 ms                                                 | 425 ms: 1.02x slower                                                  |
| pprint_safe_repr           | 776 ms                                                 | 794 ms: 1.02x slower                                                  |
| pidigits                   | 187 ms                                                 | 192 ms: 1.03x slower                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.61 sec: 1.03x slower                                                |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 10.9 ms: 1.05x slower                                                 |
| coroutines                 | 23.2 ms                                                | 25.1 ms: 1.08x slower                                                 |
| telco                      | 7.10 ms                                                | 8.12 ms: 1.14x slower                                                 |
| coverage                   | 72.7 ms                                                | 87.4 ms: 1.20x slower                                                 |
| python_startup             | 9.55 ms                                                | 12.1 ms: 1.27x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 4.84 ms: 1.28x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 2.57 ms: 1.74x slower                                                 |
| logging_silent             | 104 ns                                                 | 473 ns: 4.53x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                          |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (17) of results/bm-20250607-3.15.0a0-8fdbbf8/bm-20250607-linux-x86_64-python-8fdbbf8b18f1405abe67-3.15.0a0-8fdbbf8.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.116x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.13x