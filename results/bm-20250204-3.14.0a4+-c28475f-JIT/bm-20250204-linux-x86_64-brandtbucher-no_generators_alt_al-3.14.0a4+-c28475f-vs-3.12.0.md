# Results vs. 3.12.0

- fork: brandtbucher
- ref: no_generators_alt_al
- machine: linux-x86_64
- commit hash: c28475f
- commit date: 2025-02-04
- overall geometric mean: 1.108x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-c28475f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 258 ms: 1.06x faster                                                         |
| docutils       | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-c28475f |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 619 ms: 1.91x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 627 ms: 1.84x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.82x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 255 ms: 1.76x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 328 ms: 1.76x faster                                                         |
| async_tree_none            | 472 ms                                                 | 269 ms: 1.75x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 478 ms: 1.52x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 494 ms: 1.47x faster                                                         |
| Geometric mean             | (ref)                                                  | 1.72x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-c28475f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 67.2 ms: 1.26x faster                                                        |
| nbody          | 97.0 ms                                                | 90.6 ms: 1.07x faster                                                        |
| pidigits       | 187 ms                                                 | 186 ms: 1.01x faster                                                         |
| Geometric mean | (ref)                                                  | 1.11x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-c28475f |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                         |
| regex_effbot   | 3.61 ms                                                | 3.31 ms: 1.09x faster                                                        |
| regex_dna      | 212 ms                                                 | 212 ms: 1.00x faster                                                         |
| regex_v8       | 23.1 ms                                                | 23.9 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-c28475f |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.84 sec: 1.26x faster                                                       |
| unpickle_pure_python | 230 us                                                 | 201 us: 1.14x faster                                                         |
| xml_etree_parse      | 159 ms                                                 | 139 ms: 1.14x faster                                                         |
| xml_etree_generate   | 89.2 ms                                                | 78.6 ms: 1.13x faster                                                        |
| xml_etree_iterparse  | 107 ms                                                 | 94.6 ms: 1.13x faster                                                        |
| xml_etree_process    | 61.7 ms                                                | 55.3 ms: 1.12x faster                                                        |
| pickle_pure_python   | 324 us                                                 | 315 us: 1.03x faster                                                         |
| json_loads           | 28.5 us                                                | 29.4 us: 1.03x slower                                                        |
| json_dumps           | 10.4 ms                                                | 11.3 ms: 1.09x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.09x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-c28475f |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                        |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-c28475f |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.1 ms: 1.18x faster                                                        |
| django_template | 34.6 ms                                                | 33.2 ms: 1.04x faster                                                        |
| Geometric mean  | (ref)                                                  | 1.11x faster                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-c28475f |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 619 ms: 1.91x faster                                                         |
| async_tree_io              | 1.16 sec                                               | 627 ms: 1.84x faster                                                         |
| async_tree_memoization_tg  | 575 ms                                                 | 315 ms: 1.82x faster                                                         |
| async_tree_none_tg         | 450 ms                                                 | 255 ms: 1.76x faster                                                         |
| async_tree_memoization     | 578 ms                                                 | 328 ms: 1.76x faster                                                         |
| async_tree_none            | 472 ms                                                 | 269 ms: 1.75x faster                                                         |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 478 ms: 1.52x faster                                                         |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 494 ms: 1.47x faster                                                         |
| deepcopy                   | 371 us                                                 | 270 us: 1.37x faster                                                         |
| deepcopy_memo              | 40.7 us                                                | 30.6 us: 1.33x faster                                                        |
| comprehensions             | 21.8 us                                                | 17.1 us: 1.28x faster                                                        |
| tomli_loads                | 2.33 sec                                               | 1.84 sec: 1.26x faster                                                       |
| float                      | 84.7 ms                                                | 67.2 ms: 1.26x faster                                                        |
| scimark_fft                | 382 ms                                                 | 309 ms: 1.24x faster                                                         |
| deepcopy_reduce            | 3.35 us                                                | 2.78 us: 1.20x faster                                                        |
| scimark_monte_carlo        | 75.1 ms                                                | 62.6 ms: 1.20x faster                                                        |
| pathlib                    | 19.3 ms                                                | 16.2 ms: 1.19x faster                                                        |
| spectral_norm              | 115 ms                                                 | 96.5 ms: 1.19x faster                                                        |
| mako                       | 11.9 ms                                                | 10.1 ms: 1.18x faster                                                        |
| crypto_pyaes               | 81.9 ms                                                | 70.0 ms: 1.17x faster                                                        |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                         |
| unpickle_pure_python       | 230 us                                                 | 201 us: 1.14x faster                                                         |
| xml_etree_parse            | 159 ms                                                 | 139 ms: 1.14x faster                                                         |
| chaos                      | 67.0 ms                                                | 58.6 ms: 1.14x faster                                                        |
| async_generators           | 463 ms                                                 | 405 ms: 1.14x faster                                                         |
| scimark_sor                | 129 ms                                                 | 113 ms: 1.14x faster                                                         |
| logging_format             | 7.23 us                                                | 6.35 us: 1.14x faster                                                        |
| xml_etree_generate         | 89.2 ms                                                | 78.6 ms: 1.13x faster                                                        |
| xml_etree_iterparse        | 107 ms                                                 | 94.6 ms: 1.13x faster                                                        |
| sqlalchemy_declarative     | 147 ms                                                 | 130 ms: 1.13x faster                                                         |
| xml_etree_process          | 61.7 ms                                                | 55.3 ms: 1.12x faster                                                        |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.8 ms: 1.11x faster                                                        |
| logging_simple             | 6.46 us                                                | 5.85 us: 1.10x faster                                                        |
| go                         | 139 ms                                                 | 126 ms: 1.10x faster                                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.59 ms: 1.10x faster                                                        |
| sympy_sum                  | 169 ms                                                 | 154 ms: 1.09x faster                                                         |
| regex_effbot               | 3.61 ms                                                | 3.31 ms: 1.09x faster                                                        |
| raytrace                   | 312 ms                                                 | 287 ms: 1.09x faster                                                         |
| generators                 | 31.2 ms                                                | 28.9 ms: 1.08x faster                                                        |
| pyflate                    | 482 ms                                                 | 448 ms: 1.08x faster                                                         |
| fannkuch                   | 417 ms                                                 | 388 ms: 1.08x faster                                                         |
| sympy_str                  | 300 ms                                                 | 279 ms: 1.07x faster                                                         |
| nbody                      | 97.0 ms                                                | 90.6 ms: 1.07x faster                                                        |
| 2to3                       | 274 ms                                                 | 258 ms: 1.06x faster                                                         |
| sqlglot_parse              | 1.36 ms                                                | 1.28 ms: 1.06x faster                                                        |
| deltablue                  | 3.72 ms                                                | 3.52 ms: 1.06x faster                                                        |
| sqlglot_transpile          | 1.68 ms                                                | 1.60 ms: 1.05x faster                                                        |
| pprint_safe_repr           | 776 ms                                                 | 738 ms: 1.05x faster                                                         |
| richards                   | 45.8 ms                                                | 43.6 ms: 1.05x faster                                                        |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.05x faster                                                       |
| dulwich_log                | 68.5 ms                                                | 65.6 ms: 1.04x faster                                                        |
| django_template            | 34.6 ms                                                | 33.2 ms: 1.04x faster                                                        |
| sympy_integrate            | 21.4 ms                                                | 20.6 ms: 1.04x faster                                                        |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                         |
| sqlglot_normalize          | 110 ms                                                 | 106 ms: 1.04x faster                                                         |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.03x faster                                                         |
| sqlite_synth               | 2.83 us                                                | 2.74 us: 1.03x faster                                                        |
| richards_super             | 51.5 ms                                                | 50.0 ms: 1.03x faster                                                        |
| docutils                   | 2.77 sec                                               | 2.69 sec: 1.03x faster                                                       |
| mdp                        | 2.63 sec                                               | 2.56 sec: 1.03x faster                                                       |
| pycparser                  | 1.18 sec                                               | 1.15 sec: 1.03x faster                                                       |
| pickle_pure_python         | 324 us                                                 | 315 us: 1.03x faster                                                         |
| sqlglot_optimize           | 54.8 ms                                                | 53.6 ms: 1.02x faster                                                        |
| sympy_expand               | 478 ms                                                 | 472 ms: 1.01x faster                                                         |
| json                       | 5.26 ms                                                | 5.21 ms: 1.01x faster                                                        |
| pidigits                   | 187 ms                                                 | 186 ms: 1.01x faster                                                         |
| regex_dna                  | 212 ms                                                 | 212 ms: 1.00x faster                                                         |
| python_startup_no_site     | 6.94 ms                                                | 7.07 ms: 1.02x slower                                                        |
| coroutines                 | 23.2 ms                                                | 23.9 ms: 1.03x slower                                                        |
| json_loads                 | 28.5 us                                                | 29.4 us: 1.03x slower                                                        |
| regex_v8                   | 23.1 ms                                                | 23.9 ms: 1.03x slower                                                        |
| typing_runtime_protocols   | 158 us                                                 | 164 us: 1.04x slower                                                         |
| bench_thread_pool          | 842 us                                                 | 887 us: 1.05x slower                                                         |
| logging_silent             | 104 ns                                                 | 111 ns: 1.07x slower                                                         |
| nqueens                    | 83.3 ms                                                | 89.6 ms: 1.08x slower                                                        |
| json_dumps                 | 10.4 ms                                                | 11.3 ms: 1.09x slower                                                        |
| telco                      | 7.10 ms                                                | 7.74 ms: 1.09x slower                                                        |
| hexiom                     | 6.41 ms                                                | 7.39 ms: 1.15x slower                                                        |
| coverage                   | 72.7 ms                                                | 90.6 ms: 1.25x slower                                                        |
| gc_traversal               | 3.79 ms                                                | 5.04 ms: 1.33x slower                                                        |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                        |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.67x slower                                                        |
| bench_mp_pool              | 24.0 ms                                                | 80.6 ms: 3.36x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.09x faster                                                                 |

Benchmark hidden because not significant (1): asyncio_websockets
Ignored benchmarks (14) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250204-3.14.0a4+-c28475f-JIT/bm-20250204-linux-x86_64-brandtbucher-no_generators_alt_al-3.14.0a4+-c28475f.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.108x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.10x