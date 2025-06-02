# Results vs. 3.12.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-x86_64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.383x faster
- HPT reliability: 51.26%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.14x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 297 ms: 1.08x slower                                                  |
| docutils       | 2.77 sec                                               | 2.91 sec: 1.05x slower                                                |
| Geometric mean | (ref)                                                  | 1.07x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 678 ms: 1.74x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 665 ms: 1.74x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 345 ms: 1.67x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 345 ms: 1.67x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 274 ms: 1.64x faster                                                  |
| async_tree_none            | 472 ms                                                 | 289 ms: 1.63x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 579 ms: 1.25x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 592 ms: 1.23x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.56x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 69.2 ms: 1.22x faster                                                 |
| nbody          | 97.0 ms                                                | 98.5 ms: 1.02x slower                                                 |
| pidigits       | 187 ms                                                 | 206 ms: 1.10x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.20 ms: 1.13x faster                                                 |
| regex_dna      | 212 ms                                                 | 201 ms: 1.05x faster                                                  |
| regex_v8       | 23.1 ms                                                | 24.9 ms: 1.07x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.09 sec: 1.11x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 162 ms: 1.01x slower                                                  |
| unpickle_pure_python | 230 us                                                 | 234 us: 1.02x slower                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 110 ms: 1.03x slower                                                  |
| pickle_dict          | 35.5 us                                                | 37.8 us: 1.06x slower                                                 |
| unpickle_list        | 5.29 us                                                | 5.86 us: 1.11x slower                                                 |
| xml_etree_process    | 61.7 ms                                                | 69.2 ms: 1.12x slower                                                 |
| xml_etree_generate   | 89.2 ms                                                | 102 ms: 1.14x slower                                                  |
| pickle_pure_python   | 324 us                                                 | 372 us: 1.15x slower                                                  |
| json_loads           | 28.5 us                                                | 33.6 us: 1.18x slower                                                 |
| pickle_list          | 5.08 us                                                | 6.01 us: 1.18x slower                                                 |
| unpickle             | 15.9 us                                                | 19.1 us: 1.20x slower                                                 |
| pickle               | 11.6 us                                                | 14.9 us: 1.28x slower                                                 |
| json_dumps           | 10.4 ms                                                | 13.4 ms: 1.29x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.12x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.40 ms: 1.07x slower                                                 |
| python_startup         | 9.55 ms                                                | 13.1 ms: 1.38x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.21x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 13.3 ms: 1.12x slower                                                 |
| django_template | 34.6 ms                                                | 39.9 ms: 1.15x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.14x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pprint_pformat             | 1.57 sec                                               | 1.86 us: 843814.72x faster                                            |
| pprint_safe_repr           | 776 ms                                                 | 1.12 us: 690214.75x faster                                            |
| mdp                        | 2.63 sec                                               | 1.48 sec: 1.78x faster                                                |
| async_tree_io_tg           | 1.18 sec                                               | 678 ms: 1.74x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 665 ms: 1.74x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 345 ms: 1.67x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 345 ms: 1.67x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 274 ms: 1.64x faster                                                  |
| async_tree_none            | 472 ms                                                 | 289 ms: 1.63x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 579 ms: 1.25x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 592 ms: 1.23x faster                                                  |
| float                      | 84.7 ms                                                | 69.2 ms: 1.22x faster                                                 |
| deepcopy                   | 371 us                                                 | 315 us: 1.18x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 34.8 us: 1.17x faster                                                 |
| richards                   | 45.8 ms                                                | 39.6 ms: 1.16x faster                                                 |
| regex_effbot               | 3.61 ms                                                | 3.20 ms: 1.13x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 2.09 sec: 1.11x faster                                                |
| richards_super             | 51.5 ms                                                | 46.3 ms: 1.11x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.37 ms: 1.10x faster                                                 |
| comprehensions             | 21.8 us                                                | 20.1 us: 1.08x faster                                                 |
| scimark_fft                | 382 ms                                                 | 353 ms: 1.08x faster                                                  |
| pyflate                    | 482 ms                                                 | 450 ms: 1.07x faster                                                  |
| go                         | 139 ms                                                 | 130 ms: 1.07x faster                                                  |
| regex_dna                  | 212 ms                                                 | 201 ms: 1.05x faster                                                  |
| async_generators           | 463 ms                                                 | 439 ms: 1.05x faster                                                  |
| pathlib                    | 19.3 ms                                                | 18.4 ms: 1.05x faster                                                 |
| spectral_norm              | 115 ms                                                 | 110 ms: 1.05x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 66.1 ms: 1.04x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 73.1 ms: 1.03x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 167 ms: 1.01x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 3.38 us: 1.01x slower                                                 |
| xml_etree_parse            | 159 ms                                                 | 162 ms: 1.01x slower                                                  |
| unpickle_pure_python       | 230 us                                                 | 234 us: 1.02x slower                                                  |
| nbody                      | 97.0 ms                                                | 98.5 ms: 1.02x slower                                                 |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.82 sec: 1.02x slower                                                |
| meteor_contest             | 112 ms                                                 | 115 ms: 1.03x slower                                                  |
| raytrace                   | 312 ms                                                 | 322 ms: 1.03x slower                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 110 ms: 1.03x slower                                                  |
| chaos                      | 67.0 ms                                                | 70.1 ms: 1.05x slower                                                 |
| sympy_str                  | 300 ms                                                 | 314 ms: 1.05x slower                                                  |
| crypto_pyaes               | 81.9 ms                                                | 85.8 ms: 1.05x slower                                                 |
| docutils                   | 2.77 sec                                               | 2.91 sec: 1.05x slower                                                |
| scimark_sor                | 129 ms                                                 | 137 ms: 1.06x slower                                                  |
| generators                 | 31.2 ms                                                | 33.1 ms: 1.06x slower                                                 |
| pickle_dict                | 35.5 us                                                | 37.8 us: 1.06x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 7.40 ms: 1.07x slower                                                 |
| pycparser                  | 1.18 sec                                               | 1.26 sec: 1.07x slower                                                |
| regex_v8                   | 23.1 ms                                                | 24.9 ms: 1.07x slower                                                 |
| hexiom                     | 6.41 ms                                                | 6.94 ms: 1.08x slower                                                 |
| 2to3                       | 274 ms                                                 | 297 ms: 1.08x slower                                                  |
| sqlite_synth               | 2.83 us                                                | 3.08 us: 1.09x slower                                                 |
| pidigits                   | 187 ms                                                 | 206 ms: 1.10x slower                                                  |
| unpickle_list              | 5.29 us                                                | 5.86 us: 1.11x slower                                                 |
| mako                       | 11.9 ms                                                | 13.3 ms: 1.12x slower                                                 |
| xml_etree_process          | 61.7 ms                                                | 69.2 ms: 1.12x slower                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.74 ms: 1.14x slower                                                 |
| xml_etree_generate         | 89.2 ms                                                | 102 ms: 1.14x slower                                                  |
| json                       | 5.26 ms                                                | 6.01 ms: 1.14x slower                                                 |
| scimark_lu                 | 118 ms                                                 | 135 ms: 1.14x slower                                                  |
| sympy_expand               | 478 ms                                                 | 548 ms: 1.15x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 965 us: 1.15x slower                                                  |
| logging_simple             | 6.46 us                                                | 7.41 us: 1.15x slower                                                 |
| fannkuch                   | 417 ms                                                 | 479 ms: 1.15x slower                                                  |
| pickle_pure_python         | 324 us                                                 | 372 us: 1.15x slower                                                  |
| django_template            | 34.6 ms                                                | 39.9 ms: 1.15x slower                                                 |
| logging_format             | 7.23 us                                                | 8.43 us: 1.17x slower                                                 |
| json_loads                 | 28.5 us                                                | 33.6 us: 1.18x slower                                                 |
| pickle_list                | 5.08 us                                                | 6.01 us: 1.18x slower                                                 |
| coroutines                 | 23.2 ms                                                | 27.4 ms: 1.18x slower                                                 |
| unpickle                   | 15.9 us                                                | 19.1 us: 1.20x slower                                                 |
| nqueens                    | 83.3 ms                                                | 103 ms: 1.23x slower                                                  |
| telco                      | 7.10 ms                                                | 9.04 ms: 1.27x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 201 us: 1.27x slower                                                  |
| pickle                     | 11.6 us                                                | 14.9 us: 1.28x slower                                                 |
| json_dumps                 | 10.4 ms                                                | 13.4 ms: 1.29x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 5.11 ms: 1.35x slower                                                 |
| python_startup             | 9.55 ms                                                | 13.1 ms: 1.38x slower                                                 |
| unpack_sequence            | 54.0 ns                                                | 75.6 ns: 1.40x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 2.61 ms: 1.77x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 105 ms: 4.35x slower                                                  |
| logging_silent             | 104 ns                                                 | 623 ns: 5.96x slower                                                  |
| coverage                   | 72.7 ms                                                | 529 ms: 7.28x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.29x faster                                                          |

Benchmark hidden because not significant (3): sympy_integrate, asyncio_tcp, asyncio_websockets
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, regex_compile, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250601-3.15.0a0-cebae97-JIT/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.383x faster

# HPT report

- Reliability score: 51.26% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.14x