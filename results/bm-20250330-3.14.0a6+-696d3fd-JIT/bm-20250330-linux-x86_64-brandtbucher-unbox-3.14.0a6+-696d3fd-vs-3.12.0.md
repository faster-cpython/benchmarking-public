# Results vs. 3.12.0

- fork: brandtbucher
- ref: unbox
- machine: linux-x86_64
- commit hash: 696d3fd
- commit date: 2025-03-30
- overall geometric mean: 1.067x faster
- HPT reliability: 96.73%
- HPT 99th percentile: 1.00x faster
- Memory change: 2.23x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 272 ms: 1.01x faster                                          |
| Geometric mean | (ref)                                                  | 1.00x faster                                                  |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 613 ms: 1.93x faster                                          |
| async_tree_io              | 1.16 sec                                               | 625 ms: 1.85x faster                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 322 ms: 1.78x faster                                          |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.78x faster                                          |
| async_tree_none            | 472 ms                                                 | 267 ms: 1.77x faster                                          |
| async_tree_memoization     | 578 ms                                                 | 328 ms: 1.76x faster                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 474 ms: 1.53x faster                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 494 ms: 1.47x faster                                          |
| Geometric mean             | (ref)                                                  | 1.73x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 84.7 ms                                                | 81.0 ms: 1.05x faster                                         |
| pidigits       | 187 ms                                                 | 188 ms: 1.00x slower                                          |
| nbody          | 97.0 ms                                                | 107 ms: 1.11x slower                                          |
| Geometric mean | (ref)                                                  | 1.02x slower                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 3.26 ms: 1.11x faster                                         |
| regex_compile  | 148 ms                                                 | 137 ms: 1.08x faster                                          |
| regex_dna      | 212 ms                                                 | 209 ms: 1.01x faster                                          |
| regex_v8       | 23.1 ms                                                | 23.2 ms: 1.00x slower                                         |
| Geometric mean | (ref)                                                  | 1.05x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.85 sec: 1.26x faster                                        |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                          |
| xml_etree_iterparse  | 107 ms                                                 | 99.1 ms: 1.08x faster                                         |
| xml_etree_generate   | 89.2 ms                                                | 84.5 ms: 1.06x faster                                         |
| xml_etree_process    | 61.7 ms                                                | 59.1 ms: 1.04x faster                                         |
| unpickle_pure_python | 230 us                                                 | 236 us: 1.02x slower                                          |
| json_loads           | 28.5 us                                                | 29.8 us: 1.05x slower                                         |
| pickle_pure_python   | 324 us                                                 | 342 us: 1.06x slower                                          |
| json_dumps           | 10.4 ms                                                | 11.5 ms: 1.11x slower                                         |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.22 ms: 1.18x slower                                         |
| python_startup         | 9.55 ms                                                | 13.2 ms: 1.38x slower                                         |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 33.5 ms: 1.03x faster                                         |
| mako            | 11.9 ms                                                | 11.6 ms: 1.02x faster                                         |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.33 sec: 1.98x faster                                        |
| async_tree_io_tg           | 1.18 sec                                               | 613 ms: 1.93x faster                                          |
| async_tree_io              | 1.16 sec                                               | 625 ms: 1.85x faster                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 322 ms: 1.78x faster                                          |
| async_tree_none_tg         | 450 ms                                                 | 252 ms: 1.78x faster                                          |
| async_tree_none            | 472 ms                                                 | 267 ms: 1.77x faster                                          |
| async_tree_memoization     | 578 ms                                                 | 328 ms: 1.76x faster                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 474 ms: 1.53x faster                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 494 ms: 1.47x faster                                          |
| deepcopy                   | 371 us                                                 | 274 us: 1.35x faster                                          |
| deepcopy_memo              | 40.7 us                                                | 30.8 us: 1.32x faster                                         |
| tomli_loads                | 2.33 sec                                               | 1.85 sec: 1.26x faster                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.89 us: 1.16x faster                                         |
| pathlib                    | 19.3 ms                                                | 16.8 ms: 1.15x faster                                         |
| richards                   | 45.8 ms                                                | 40.4 ms: 1.14x faster                                         |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                          |
| logging_format             | 7.23 us                                                | 6.40 us: 1.13x faster                                         |
| richards_super             | 51.5 ms                                                | 45.8 ms: 1.13x faster                                         |
| async_generators           | 463 ms                                                 | 418 ms: 1.11x faster                                          |
| regex_effbot               | 3.61 ms                                                | 3.26 ms: 1.11x faster                                         |
| logging_simple             | 6.46 us                                                | 5.85 us: 1.10x faster                                         |
| dulwich_log                | 68.5 ms                                                | 62.2 ms: 1.10x faster                                         |
| chaos                      | 67.0 ms                                                | 61.3 ms: 1.09x faster                                         |
| sympy_sum                  | 169 ms                                                 | 156 ms: 1.08x faster                                          |
| regex_compile              | 148 ms                                                 | 137 ms: 1.08x faster                                          |
| sqlalchemy_declarative     | 147 ms                                                 | 136 ms: 1.08x faster                                          |
| xml_etree_iterparse        | 107 ms                                                 | 99.1 ms: 1.08x faster                                         |
| raytrace                   | 312 ms                                                 | 291 ms: 1.07x faster                                          |
| comprehensions             | 21.8 us                                                | 20.5 us: 1.06x faster                                         |
| coroutines                 | 23.2 ms                                                | 21.9 ms: 1.06x faster                                         |
| xml_etree_generate         | 89.2 ms                                                | 84.5 ms: 1.06x faster                                         |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.7 ms: 1.06x faster                                         |
| generators                 | 31.2 ms                                                | 29.7 ms: 1.05x faster                                         |
| sympy_str                  | 300 ms                                                 | 286 ms: 1.05x faster                                          |
| float                      | 84.7 ms                                                | 81.0 ms: 1.05x faster                                         |
| xml_etree_process          | 61.7 ms                                                | 59.1 ms: 1.04x faster                                         |
| deltablue                  | 3.72 ms                                                | 3.58 ms: 1.04x faster                                         |
| scimark_monte_carlo        | 75.1 ms                                                | 72.6 ms: 1.03x faster                                         |
| logging_silent             | 104 ns                                                 | 101 ns: 1.03x faster                                          |
| sympy_integrate            | 21.4 ms                                                | 20.7 ms: 1.03x faster                                         |
| django_template            | 34.6 ms                                                | 33.5 ms: 1.03x faster                                         |
| mako                       | 11.9 ms                                                | 11.6 ms: 1.02x faster                                         |
| regex_dna                  | 212 ms                                                 | 209 ms: 1.01x faster                                          |
| pyflate                    | 482 ms                                                 | 478 ms: 1.01x faster                                          |
| 2to3                       | 274 ms                                                 | 272 ms: 1.01x faster                                          |
| pidigits                   | 187 ms                                                 | 188 ms: 1.00x slower                                          |
| regex_v8                   | 23.1 ms                                                | 23.2 ms: 1.00x slower                                         |
| meteor_contest             | 112 ms                                                 | 114 ms: 1.01x slower                                          |
| scimark_fft                | 382 ms                                                 | 390 ms: 1.02x slower                                          |
| unpickle_pure_python       | 230 us                                                 | 236 us: 1.02x slower                                          |
| scimark_sor                | 129 ms                                                 | 134 ms: 1.04x slower                                          |
| sympy_expand               | 478 ms                                                 | 498 ms: 1.04x slower                                          |
| json_loads                 | 28.5 us                                                | 29.8 us: 1.05x slower                                         |
| pprint_safe_repr           | 776 ms                                                 | 817 ms: 1.05x slower                                          |
| pickle_pure_python         | 324 us                                                 | 342 us: 1.06x slower                                          |
| pycparser                  | 1.18 sec                                               | 1.25 sec: 1.06x slower                                        |
| bench_thread_pool          | 842 us                                                 | 899 us: 1.07x slower                                          |
| scimark_lu                 | 118 ms                                                 | 126 ms: 1.07x slower                                          |
| go                         | 139 ms                                                 | 150 ms: 1.07x slower                                          |
| fannkuch                   | 417 ms                                                 | 448 ms: 1.08x slower                                          |
| nqueens                    | 83.3 ms                                                | 89.7 ms: 1.08x slower                                         |
| crypto_pyaes               | 81.9 ms                                                | 88.5 ms: 1.08x slower                                         |
| pprint_pformat             | 1.57 sec                                               | 1.71 sec: 1.09x slower                                        |
| spectral_norm              | 115 ms                                                 | 127 ms: 1.10x slower                                          |
| nbody                      | 97.0 ms                                                | 107 ms: 1.11x slower                                          |
| json_dumps                 | 10.4 ms                                                | 11.5 ms: 1.11x slower                                         |
| typing_runtime_protocols   | 158 us                                                 | 181 us: 1.15x slower                                          |
| telco                      | 7.10 ms                                                | 8.19 ms: 1.15x slower                                         |
| hexiom                     | 6.41 ms                                                | 7.41 ms: 1.16x slower                                         |
| coverage                   | 72.7 ms                                                | 86.1 ms: 1.18x slower                                         |
| python_startup_no_site     | 6.94 ms                                                | 8.22 ms: 1.18x slower                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 6.18 ms: 1.22x slower                                         |
| gc_traversal               | 3.79 ms                                                | 4.82 ms: 1.27x slower                                         |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.38x slower                                         |
| create_gc_cycles           | 1.48 ms                                                | 2.49 ms: 1.68x slower                                         |
| bench_mp_pool              | 24.0 ms                                                | 84.3 ms: 3.51x slower                                         |
| Geometric mean             | (ref)                                                  | 1.05x faster                                                  |

Benchmark hidden because not significant (4): sqlite_synth, docutils, asyncio_websockets, json
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250330-3.14.0a6+-696d3fd-JIT/bm-20250330-linux-x86_64-brandtbucher-unbox-3.14.0a6+-696d3fd.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.067x faster

# HPT report

- Reliability score: 96.73% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 2.23x