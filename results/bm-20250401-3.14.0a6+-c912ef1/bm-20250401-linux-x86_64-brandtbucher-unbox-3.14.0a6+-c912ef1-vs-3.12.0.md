# Results vs. 3.12.0

- fork: brandtbucher
- ref: unbox
- machine: linux-x86_64
- commit hash: c912ef1
- commit date: 2025-04-01
- overall geometric mean: 1.098x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 261 ms: 1.05x faster                                          |
| docutils       | 2.77 sec                                               | 2.65 sec: 1.04x faster                                        |
| Geometric mean | (ref)                                                  | 1.05x faster                                                  |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 640 ms: 1.85x faster                                          |
| async_tree_io              | 1.16 sec                                               | 634 ms: 1.82x faster                                          |
| async_tree_memoization     | 578 ms                                                 | 324 ms: 1.78x faster                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 326 ms: 1.76x faster                                          |
| async_tree_none            | 472 ms                                                 | 268 ms: 1.76x faster                                          |
| async_tree_none_tg         | 450 ms                                                 | 257 ms: 1.75x faster                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 482 ms: 1.50x faster                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 495 ms: 1.47x faster                                          |
| Geometric mean             | (ref)                                                  | 1.71x faster                                                  |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| float          | 84.7 ms                                                | 75.4 ms: 1.12x faster                                         |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                          |
| nbody          | 97.0 ms                                                | 102 ms: 1.05x slower                                          |
| Geometric mean | (ref)                                                  | 1.02x faster                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 131 ms: 1.13x faster                                          |
| regex_effbot   | 3.61 ms                                                | 3.44 ms: 1.05x faster                                         |
| regex_dna      | 212 ms                                                 | 217 ms: 1.02x slower                                          |
| regex_v8       | 23.1 ms                                                | 24.6 ms: 1.06x slower                                         |
| Geometric mean | (ref)                                                  | 1.02x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.88 sec: 1.24x faster                                        |
| xml_etree_parse      | 159 ms                                                 | 141 ms: 1.13x faster                                          |
| xml_etree_iterparse  | 107 ms                                                 | 99.6 ms: 1.07x faster                                         |
| xml_etree_generate   | 89.2 ms                                                | 85.1 ms: 1.05x faster                                         |
| xml_etree_process    | 61.7 ms                                                | 59.8 ms: 1.03x faster                                         |
| unpickle_pure_python | 230 us                                                 | 226 us: 1.02x faster                                          |
| pickle_pure_python   | 324 us                                                 | 326 us: 1.01x slower                                          |
| json_dumps           | 10.4 ms                                                | 11.6 ms: 1.12x slower                                         |
| json_loads           | 28.5 us                                                | 32.0 us: 1.12x slower                                         |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                  |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 8.22 ms: 1.18x slower                                         |
| python_startup         | 9.55 ms                                                | 13.2 ms: 1.38x slower                                         |
| Geometric mean         | (ref)                                                  | 1.28x slower                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.5 ms: 1.07x faster                                         |
| mako            | 11.9 ms                                                | 12.0 ms: 1.01x slower                                         |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                  |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.24 sec: 2.12x faster                                        |
| async_tree_io_tg           | 1.18 sec                                               | 640 ms: 1.85x faster                                          |
| async_tree_io              | 1.16 sec                                               | 634 ms: 1.82x faster                                          |
| async_tree_memoization     | 578 ms                                                 | 324 ms: 1.78x faster                                          |
| async_tree_memoization_tg  | 575 ms                                                 | 326 ms: 1.76x faster                                          |
| async_tree_none            | 472 ms                                                 | 268 ms: 1.76x faster                                          |
| async_tree_none_tg         | 450 ms                                                 | 257 ms: 1.75x faster                                          |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 482 ms: 1.50x faster                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 495 ms: 1.47x faster                                          |
| deepcopy                   | 371 us                                                 | 263 us: 1.41x faster                                          |
| deepcopy_memo              | 40.7 us                                                | 30.8 us: 1.32x faster                                         |
| spectral_norm              | 115 ms                                                 | 91.1 ms: 1.26x faster                                         |
| comprehensions             | 21.8 us                                                | 17.3 us: 1.26x faster                                         |
| tomli_loads                | 2.33 sec                                               | 1.88 sec: 1.24x faster                                        |
| deepcopy_reduce            | 3.35 us                                                | 2.72 us: 1.23x faster                                         |
| chaos                      | 67.0 ms                                                | 57.2 ms: 1.17x faster                                         |
| go                         | 139 ms                                                 | 120 ms: 1.17x faster                                          |
| async_generators           | 463 ms                                                 | 399 ms: 1.16x faster                                          |
| pathlib                    | 19.3 ms                                                | 16.7 ms: 1.16x faster                                         |
| logging_format             | 7.23 us                                                | 6.26 us: 1.16x faster                                         |
| raytrace                   | 312 ms                                                 | 270 ms: 1.15x faster                                          |
| dulwich_log                | 68.5 ms                                                | 59.4 ms: 1.15x faster                                         |
| xml_etree_parse            | 159 ms                                                 | 141 ms: 1.13x faster                                          |
| regex_compile              | 148 ms                                                 | 131 ms: 1.13x faster                                          |
| logging_simple             | 6.46 us                                                | 5.71 us: 1.13x faster                                         |
| float                      | 84.7 ms                                                | 75.4 ms: 1.12x faster                                         |
| deltablue                  | 3.72 ms                                                | 3.33 ms: 1.12x faster                                         |
| sympy_sum                  | 169 ms                                                 | 152 ms: 1.11x faster                                          |
| sqlalchemy_declarative     | 147 ms                                                 | 132 ms: 1.11x faster                                          |
| scimark_monte_carlo        | 75.1 ms                                                | 67.9 ms: 1.11x faster                                         |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.0 ms: 1.10x faster                                         |
| sympy_str                  | 300 ms                                                 | 273 ms: 1.10x faster                                          |
| scimark_sor                | 129 ms                                                 | 118 ms: 1.09x faster                                          |
| sympy_integrate            | 21.4 ms                                                | 19.7 ms: 1.09x faster                                         |
| generators                 | 31.2 ms                                                | 29.0 ms: 1.08x faster                                         |
| xml_etree_iterparse        | 107 ms                                                 | 99.6 ms: 1.07x faster                                         |
| logging_silent             | 104 ns                                                 | 97.7 ns: 1.07x faster                                         |
| django_template            | 34.6 ms                                                | 32.5 ms: 1.07x faster                                         |
| coroutines                 | 23.2 ms                                                | 21.8 ms: 1.06x faster                                         |
| hexiom                     | 6.41 ms                                                | 6.08 ms: 1.06x faster                                         |
| 2to3                       | 274 ms                                                 | 261 ms: 1.05x faster                                          |
| regex_effbot               | 3.61 ms                                                | 3.44 ms: 1.05x faster                                         |
| xml_etree_generate         | 89.2 ms                                                | 85.1 ms: 1.05x faster                                         |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                          |
| docutils                   | 2.77 sec                                               | 2.65 sec: 1.04x faster                                        |
| xml_etree_process          | 61.7 ms                                                | 59.8 ms: 1.03x faster                                         |
| sympy_expand               | 478 ms                                                 | 466 ms: 1.03x faster                                          |
| pprint_safe_repr           | 776 ms                                                 | 762 ms: 1.02x faster                                          |
| unpickle_pure_python       | 230 us                                                 | 226 us: 1.02x faster                                          |
| pyflate                    | 482 ms                                                 | 476 ms: 1.01x faster                                          |
| sqlite_synth               | 2.83 us                                                | 2.82 us: 1.01x faster                                         |
| nqueens                    | 83.3 ms                                                | 83.5 ms: 1.00x slower                                         |
| scimark_fft                | 382 ms                                                 | 384 ms: 1.01x slower                                          |
| pickle_pure_python         | 324 us                                                 | 326 us: 1.01x slower                                          |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                          |
| crypto_pyaes               | 81.9 ms                                                | 82.8 ms: 1.01x slower                                         |
| mako                       | 11.9 ms                                                | 12.0 ms: 1.01x slower                                         |
| richards_super             | 51.5 ms                                                | 52.5 ms: 1.02x slower                                         |
| fannkuch                   | 417 ms                                                 | 426 ms: 1.02x slower                                          |
| regex_dna                  | 212 ms                                                 | 217 ms: 1.02x slower                                          |
| json                       | 5.26 ms                                                | 5.47 ms: 1.04x slower                                         |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.29 ms: 1.05x slower                                         |
| typing_runtime_protocols   | 158 us                                                 | 166 us: 1.05x slower                                          |
| nbody                      | 97.0 ms                                                | 102 ms: 1.05x slower                                          |
| bench_thread_pool          | 842 us                                                 | 884 us: 1.05x slower                                          |
| regex_v8                   | 23.1 ms                                                | 24.6 ms: 1.06x slower                                         |
| scimark_lu                 | 118 ms                                                 | 126 ms: 1.07x slower                                          |
| json_dumps                 | 10.4 ms                                                | 11.6 ms: 1.12x slower                                         |
| json_loads                 | 28.5 us                                                | 32.0 us: 1.12x slower                                         |
| telco                      | 7.10 ms                                                | 8.07 ms: 1.14x slower                                         |
| coverage                   | 72.7 ms                                                | 84.6 ms: 1.16x slower                                         |
| python_startup_no_site     | 6.94 ms                                                | 8.22 ms: 1.18x slower                                         |
| gc_traversal               | 3.79 ms                                                | 4.99 ms: 1.32x slower                                         |
| python_startup             | 9.55 ms                                                | 13.2 ms: 1.38x slower                                         |
| create_gc_cycles           | 1.48 ms                                                | 2.47 ms: 1.68x slower                                         |
| bench_mp_pool              | 24.0 ms                                                | 83.7 ms: 3.48x slower                                         |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                  |

Benchmark hidden because not significant (4): pprint_pformat, asyncio_websockets, pycparser, richards
Ignored benchmarks (18) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (15) of results/bm-20250401-3.14.0a6+-c912ef1/bm-20250401-linux-x86_64-brandtbucher-unbox-3.14.0a6+-c912ef1.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers

- Geometric mean (including insignificant results): 1.098x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 1.11x