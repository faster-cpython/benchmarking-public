# Results vs. 3.12.0

- fork: python
- ref: cebae977a63f32c3c03d
- machine: linux-x86_64
- commit hash: cebae97
- commit date: 2025-06-01
- overall geometric mean: 1.058x slower
- HPT reliability: 95.02%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 289 ms: 1.06x slower                                                  |
| docutils       | 2.77 sec                                               | 2.84 sec: 1.03x slower                                                |
| Geometric mean | (ref)                                                  | 1.04x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 662 ms: 1.75x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 696 ms: 1.70x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 350 ms: 1.65x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 352 ms: 1.63x faster                                                  |
| async_tree_none            | 472 ms                                                 | 291 ms: 1.62x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 279 ms: 1.61x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 598 ms: 1.21x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 607 ms: 1.20x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.53x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 75.1 ms: 1.13x faster                                                 |
| pidigits       | 187 ms                                                 | 202 ms: 1.08x slower                                                  |
| nbody          | 97.0 ms                                                | 109 ms: 1.12x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.00 ms: 1.20x faster                                                 |
| regex_dna      | 212 ms                                                 | 204 ms: 1.04x faster                                                  |
| regex_compile  | 148 ms                                                 | 143 ms: 1.03x faster                                                  |
| regex_v8       | 23.1 ms                                                | 24.0 ms: 1.04x slower                                                 |
| Geometric mean | (ref)                                                  | 1.06x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.25 sec: 1.03x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 161 ms: 1.01x slower                                                  |
| pickle_dict          | 35.5 us                                                | 36.2 us: 1.02x slower                                                 |
| xml_etree_iterparse  | 107 ms                                                 | 111 ms: 1.04x slower                                                  |
| unpickle_list        | 5.29 us                                                | 5.59 us: 1.06x slower                                                 |
| unpickle_pure_python | 230 us                                                 | 255 us: 1.11x slower                                                  |
| pickle_list          | 5.08 us                                                | 5.85 us: 1.15x slower                                                 |
| pickle_pure_python   | 324 us                                                 | 380 us: 1.17x slower                                                  |
| unpickle             | 15.9 us                                                | 18.9 us: 1.19x slower                                                 |
| json_loads           | 28.5 us                                                | 33.9 us: 1.19x slower                                                 |
| xml_etree_process    | 61.7 ms                                                | 73.6 ms: 1.19x slower                                                 |
| xml_etree_generate   | 89.2 ms                                                | 107 ms: 1.20x slower                                                  |
| json_dumps           | 10.4 ms                                                | 13.3 ms: 1.28x slower                                                 |
| pickle               | 11.6 us                                                | 15.0 us: 1.30x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.13x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.42 ms: 1.07x slower                                                 |
| python_startup         | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.21x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 13.7 ms: 1.15x slower                                                 |
| django_template | 34.6 ms                                                | 40.3 ms: 1.17x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.16x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.47 sec: 1.79x faster                                                |
| async_tree_io              | 1.16 sec                                               | 662 ms: 1.75x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 696 ms: 1.70x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 350 ms: 1.65x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 352 ms: 1.63x faster                                                  |
| async_tree_none            | 472 ms                                                 | 291 ms: 1.62x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 279 ms: 1.61x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 598 ms: 1.21x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.00 ms: 1.20x faster                                                 |
| deepcopy_memo              | 40.7 us                                                | 34.0 us: 1.20x faster                                                 |
| deepcopy                   | 371 us                                                 | 310 us: 1.20x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 607 ms: 1.20x faster                                                  |
| go                         | 139 ms                                                 | 119 ms: 1.17x faster                                                  |
| comprehensions             | 21.8 us                                                | 19.1 us: 1.14x faster                                                 |
| float                      | 84.7 ms                                                | 75.1 ms: 1.13x faster                                                 |
| async_generators           | 463 ms                                                 | 416 ms: 1.11x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 64.0 ms: 1.07x faster                                                 |
| unpack_sequence            | 54.0 ns                                                | 50.5 ns: 1.07x faster                                                 |
| pathlib                    | 19.3 ms                                                | 18.2 ms: 1.06x faster                                                 |
| regex_dna                  | 212 ms                                                 | 204 ms: 1.04x faster                                                  |
| regex_compile              | 148 ms                                                 | 143 ms: 1.03x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 2.25 sec: 1.03x faster                                                |
| sympy_integrate            | 21.4 ms                                                | 20.9 ms: 1.02x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 166 ms: 1.02x faster                                                  |
| pyflate                    | 482 ms                                                 | 476 ms: 1.01x faster                                                  |
| asyncio_tcp                | 491 ms                                                 | 484 ms: 1.01x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 3.30 us: 1.01x faster                                                 |
| spectral_norm              | 115 ms                                                 | 113 ms: 1.01x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 161 ms: 1.01x slower                                                  |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.82 sec: 1.02x slower                                                |
| pickle_dict                | 35.5 us                                                | 36.2 us: 1.02x slower                                                 |
| raytrace                   | 312 ms                                                 | 319 ms: 1.02x slower                                                  |
| sympy_str                  | 300 ms                                                 | 307 ms: 1.03x slower                                                  |
| docutils                   | 2.77 sec                                               | 2.84 sec: 1.03x slower                                                |
| meteor_contest             | 112 ms                                                 | 116 ms: 1.03x slower                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 111 ms: 1.04x slower                                                  |
| deltablue                  | 3.72 ms                                                | 3.86 ms: 1.04x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 24.0 ms: 1.04x slower                                                 |
| generators                 | 31.2 ms                                                | 32.4 ms: 1.04x slower                                                 |
| hexiom                     | 6.41 ms                                                | 6.66 ms: 1.04x slower                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 78.2 ms: 1.04x slower                                                 |
| chaos                      | 67.0 ms                                                | 69.9 ms: 1.04x slower                                                 |
| scimark_sor                | 129 ms                                                 | 136 ms: 1.05x slower                                                  |
| 2to3                       | 274 ms                                                 | 289 ms: 1.06x slower                                                  |
| unpickle_list              | 5.29 us                                                | 5.59 us: 1.06x slower                                                 |
| pycparser                  | 1.18 sec                                               | 1.25 sec: 1.06x slower                                                |
| crypto_pyaes               | 81.9 ms                                                | 87.1 ms: 1.06x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 7.42 ms: 1.07x slower                                                 |
| pidigits                   | 187 ms                                                 | 202 ms: 1.08x slower                                                  |
| scimark_fft                | 382 ms                                                 | 420 ms: 1.10x slower                                                  |
| unpickle_pure_python       | 230 us                                                 | 255 us: 1.11x slower                                                  |
| sympy_expand               | 478 ms                                                 | 534 ms: 1.12x slower                                                  |
| sqlite_synth               | 2.83 us                                                | 3.17 us: 1.12x slower                                                 |
| nbody                      | 97.0 ms                                                | 109 ms: 1.12x slower                                                  |
| scimark_lu                 | 118 ms                                                 | 134 ms: 1.14x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 957 us: 1.14x slower                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.78 ms: 1.14x slower                                                 |
| pickle_list                | 5.08 us                                                | 5.85 us: 1.15x slower                                                 |
| mako                       | 11.9 ms                                                | 13.7 ms: 1.15x slower                                                 |
| json                       | 5.26 ms                                                | 6.11 ms: 1.16x slower                                                 |
| logging_simple             | 6.46 us                                                | 7.52 us: 1.17x slower                                                 |
| django_template            | 34.6 ms                                                | 40.3 ms: 1.17x slower                                                 |
| pickle_pure_python         | 324 us                                                 | 380 us: 1.17x slower                                                  |
| fannkuch                   | 417 ms                                                 | 491 ms: 1.18x slower                                                  |
| richards                   | 45.8 ms                                                | 54.3 ms: 1.18x slower                                                 |
| logging_format             | 7.23 us                                                | 8.58 us: 1.19x slower                                                 |
| unpickle                   | 15.9 us                                                | 18.9 us: 1.19x slower                                                 |
| json_loads                 | 28.5 us                                                | 33.9 us: 1.19x slower                                                 |
| nqueens                    | 83.3 ms                                                | 99.3 ms: 1.19x slower                                                 |
| xml_etree_process          | 61.7 ms                                                | 73.6 ms: 1.19x slower                                                 |
| richards_super             | 51.5 ms                                                | 61.5 ms: 1.19x slower                                                 |
| xml_etree_generate         | 89.2 ms                                                | 107 ms: 1.20x slower                                                  |
| coroutines                 | 23.2 ms                                                | 28.1 ms: 1.21x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 195 us: 1.23x slower                                                  |
| pprint_safe_repr           | 776 ms                                                 | 988 ms: 1.27x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 13.3 ms: 1.28x slower                                                 |
| pprint_pformat             | 1.57 sec                                               | 2.01 sec: 1.28x slower                                                |
| pickle                     | 11.6 us                                                | 15.0 us: 1.30x slower                                                 |
| telco                      | 7.10 ms                                                | 9.39 ms: 1.32x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 5.16 ms: 1.36x slower                                                 |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.38x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 2.63 ms: 1.78x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 104 ms: 4.33x slower                                                  |
| logging_silent             | 104 ns                                                 | 651 ns: 6.23x slower                                                  |
| coverage                   | 72.7 ms                                                | 514 ms: 7.08x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.08x slower                                                          |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250601-3.15.0a0-cebae97/bm-20250601-linux-x86_64-python-cebae977a63f32c3c03d-3.15.0a0-cebae97.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.058x slower

# HPT report

- Reliability score: 95.02% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.13x