# Results vs. 3.12.0

- fork: python
- ref: fba5dded6df3c2b19435
- machine: linux-x86_64
- commit hash: fba5dde
- commit date: 2025-06-17
- overall geometric mean: 1.152x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.07x slower
- Memory change: 1.39x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 339 ms: 1.23x slower                                                  |
| docutils       | 2.77 sec                                               | 3.16 sec: 1.14x slower                                                |
| Geometric mean | (ref)                                                  | 1.19x slower                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 594 ms: 1.99x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 633 ms: 1.83x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 260 ms: 1.73x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 336 ms: 1.71x faster                                                  |
| async_tree_none            | 472 ms                                                 | 299 ms: 1.58x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 375 ms: 1.54x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 567 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 610 ms: 1.19x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.58x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 81.1 ms: 1.04x faster                                                 |
| pidigits       | 187 ms                                                 | 203 ms: 1.08x slower                                                  |
| nbody          | 97.0 ms                                                | 151 ms: 1.56x slower                                                  |
| Geometric mean | (ref)                                                  | 1.17x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                | 2.99 ms: 1.21x faster                                                 |
| regex_dna      | 212 ms                                                 | 192 ms: 1.11x faster                                                  |
| regex_v8       | 23.1 ms                                                | 23.6 ms: 1.02x slower                                                 |
| regex_compile  | 148 ms                                                 | 172 ms: 1.16x slower                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| xml_etree_iterparse  | 107 ms                                                 | 108 ms: 1.01x slower                                                  |
| xml_etree_parse      | 159 ms                                                 | 165 ms: 1.03x slower                                                  |
| pickle_dict          | 35.5 us                                                | 37.4 us: 1.05x slower                                                 |
| tomli_loads          | 2.33 sec                                               | 2.63 sec: 1.13x slower                                                |
| pickle_list          | 5.08 us                                                | 5.91 us: 1.16x slower                                                 |
| unpickle_list        | 5.29 us                                                | 6.40 us: 1.21x slower                                                 |
| unpickle_pure_python | 230 us                                                 | 296 us: 1.29x slower                                                  |
| json_loads           | 28.5 us                                                | 37.2 us: 1.31x slower                                                 |
| pickle_pure_python   | 324 us                                                 | 424 us: 1.31x slower                                                  |
| pickle               | 11.6 us                                                | 15.4 us: 1.33x slower                                                 |
| xml_etree_generate   | 89.2 ms                                                | 125 ms: 1.40x slower                                                  |
| unpickle             | 15.9 us                                                | 22.2 us: 1.40x slower                                                 |
| xml_etree_process    | 61.7 ms                                                | 87.5 ms: 1.42x slower                                                 |
| json_dumps           | 10.4 ms                                                | 14.8 ms: 1.42x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.24x slower                                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 10.0 ms: 1.45x slower                                                 |
| python_startup         | 9.55 ms                                                | 17.2 ms: 1.80x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.62x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 53.5 ms: 1.55x slower                                                 |
| mako            | 11.9 ms                                                | 18.9 ms: 1.59x slower                                                 |
| Geometric mean  | (ref)                                                  | 1.57x slower                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 594 ms: 1.99x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 633 ms: 1.83x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 260 ms: 1.73x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 336 ms: 1.71x faster                                                  |
| async_tree_none            | 472 ms                                                 | 299 ms: 1.58x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 375 ms: 1.54x faster                                                  |
| mdp                        | 2.63 sec                                               | 1.74 sec: 1.51x faster                                                |
| gc_traversal               | 3.79 ms                                                | 2.89 ms: 1.31x faster                                                 |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 567 ms: 1.28x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 2.99 ms: 1.21x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 610 ms: 1.19x faster                                                  |
| regex_dna                  | 212 ms                                                 | 192 ms: 1.11x faster                                                  |
| float                      | 84.7 ms                                                | 81.1 ms: 1.04x faster                                                 |
| async_generators           | 463 ms                                                 | 452 ms: 1.02x faster                                                  |
| go                         | 139 ms                                                 | 139 ms: 1.00x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 108 ms: 1.01x slower                                                  |
| deepcopy                   | 371 us                                                 | 378 us: 1.02x slower                                                  |
| pathlib                    | 19.3 ms                                                | 19.7 ms: 1.02x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 23.6 ms: 1.02x slower                                                 |
| xml_etree_parse            | 159 ms                                                 | 165 ms: 1.03x slower                                                  |
| comprehensions             | 21.8 us                                                | 22.9 us: 1.05x slower                                                 |
| pickle_dict                | 35.5 us                                                | 37.4 us: 1.05x slower                                                 |
| unpack_sequence            | 54.0 ns                                                | 56.9 ns: 1.06x slower                                                 |
| dulwich_log                | 68.5 ms                                                | 73.0 ms: 1.07x slower                                                 |
| pidigits                   | 187 ms                                                 | 203 ms: 1.08x slower                                                  |
| pycparser                  | 1.18 sec                                               | 1.29 sec: 1.09x slower                                                |
| asyncio_tcp                | 491 ms                                                 | 549 ms: 1.12x slower                                                  |
| generators                 | 31.2 ms                                                | 35.1 ms: 1.13x slower                                                 |
| tomli_loads                | 2.33 sec                                               | 2.63 sec: 1.13x slower                                                |
| sqlite_synth               | 2.83 us                                                | 3.21 us: 1.13x slower                                                 |
| asyncio_tcp_ssl            | 1.79 sec                                               | 2.03 sec: 1.14x slower                                                |
| docutils                   | 2.77 sec                                               | 3.16 sec: 1.14x slower                                                |
| pyflate                    | 482 ms                                                 | 550 ms: 1.14x slower                                                  |
| regex_compile              | 148 ms                                                 | 172 ms: 1.16x slower                                                  |
| pickle_list                | 5.08 us                                                | 5.91 us: 1.16x slower                                                 |
| sympy_sum                  | 169 ms                                                 | 199 ms: 1.18x slower                                                  |
| sympy_integrate            | 21.4 ms                                                | 25.2 ms: 1.18x slower                                                 |
| spectral_norm              | 115 ms                                                 | 137 ms: 1.20x slower                                                  |
| scimark_sor                | 129 ms                                                 | 156 ms: 1.21x slower                                                  |
| unpickle_list              | 5.29 us                                                | 6.40 us: 1.21x slower                                                 |
| chaos                      | 67.0 ms                                                | 81.4 ms: 1.22x slower                                                 |
| meteor_contest             | 112 ms                                                 | 137 ms: 1.22x slower                                                  |
| deltablue                  | 3.72 ms                                                | 4.56 ms: 1.23x slower                                                 |
| hexiom                     | 6.41 ms                                                | 7.90 ms: 1.23x slower                                                 |
| sympy_str                  | 300 ms                                                 | 369 ms: 1.23x slower                                                  |
| 2to3                       | 274 ms                                                 | 339 ms: 1.23x slower                                                  |
| raytrace                   | 312 ms                                                 | 387 ms: 1.24x slower                                                  |
| coroutines                 | 23.2 ms                                                | 28.8 ms: 1.24x slower                                                 |
| deepcopy_reduce            | 3.35 us                                                | 4.18 us: 1.25x slower                                                 |
| scimark_fft                | 382 ms                                                 | 479 ms: 1.25x slower                                                  |
| json                       | 5.26 ms                                                | 6.62 ms: 1.26x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.88 ms: 1.27x slower                                                 |
| unpickle_pure_python       | 230 us                                                 | 296 us: 1.29x slower                                                  |
| json_loads                 | 28.5 us                                                | 37.2 us: 1.31x slower                                                 |
| pickle_pure_python         | 324 us                                                 | 424 us: 1.31x slower                                                  |
| sympy_expand               | 478 ms                                                 | 630 ms: 1.32x slower                                                  |
| pickle                     | 11.6 us                                                | 15.4 us: 1.33x slower                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 99.8 ms: 1.33x slower                                                 |
| scimark_lu                 | 118 ms                                                 | 161 ms: 1.37x slower                                                  |
| crypto_pyaes               | 81.9 ms                                                | 112 ms: 1.37x slower                                                  |
| fannkuch                   | 417 ms                                                 | 573 ms: 1.37x slower                                                  |
| nqueens                    | 83.3 ms                                                | 116 ms: 1.40x slower                                                  |
| xml_etree_generate         | 89.2 ms                                                | 125 ms: 1.40x slower                                                  |
| unpickle                   | 15.9 us                                                | 22.2 us: 1.40x slower                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 7.11 ms: 1.41x slower                                                 |
| logging_simple             | 6.46 us                                                | 9.09 us: 1.41x slower                                                 |
| logging_format             | 7.23 us                                                | 10.2 us: 1.41x slower                                                 |
| xml_etree_process          | 61.7 ms                                                | 87.5 ms: 1.42x slower                                                 |
| json_dumps                 | 10.4 ms                                                | 14.8 ms: 1.42x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 10.0 ms: 1.45x slower                                                 |
| richards                   | 45.8 ms                                                | 66.9 ms: 1.46x slower                                                 |
| pprint_safe_repr           | 776 ms                                                 | 1.15 sec: 1.49x slower                                                |
| richards_super             | 51.5 ms                                                | 77.4 ms: 1.50x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 238 us: 1.51x slower                                                  |
| pprint_pformat             | 1.57 sec                                               | 2.38 sec: 1.52x slower                                                |
| django_template            | 34.6 ms                                                | 53.5 ms: 1.55x slower                                                 |
| nbody                      | 97.0 ms                                                | 151 ms: 1.56x slower                                                  |
| mako                       | 11.9 ms                                                | 18.9 ms: 1.59x slower                                                 |
| telco                      | 7.10 ms                                                | 12.1 ms: 1.70x slower                                                 |
| coverage                   | 72.7 ms                                                | 128 ms: 1.76x slower                                                  |
| python_startup             | 9.55 ms                                                | 17.2 ms: 1.80x slower                                                 |
| bench_thread_pool          | 842 us                                                 | 3.51 ms: 4.17x slower                                                 |
| bench_mp_pool              | 24.0 ms                                                | 112 ms: 4.67x slower                                                  |
| logging_silent             | 104 ns                                                 | 755 ns: 7.23x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.21x slower                                                          |

Benchmark hidden because not significant (2): asyncio_websockets, deepcopy_memo
Ignored benchmarks (12) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http
Ignored benchmarks (16) of results/bm-20250617-3.15.0a0-fba5dde-NOGIL/bm-20250617-linux-x86_64-python-fba5dded6df3c2b19435-3.15.0a0-fba5dde.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.152x slower

# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.13x
- 95% likely to have a slowdown of 1.10x
- 99% likely to have a slowdown of 1.07x

# Memory
- memory change: 1.39x