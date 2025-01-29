# Results vs. 3.12.0

- fork: mdboom
- ref: specialize_compact_i
- machine: linux-x86_64
- commit hash: fd72580
- commit date: 2025-01-28
- overall geometric mean: 1.015x faster
- HPT reliability: 99.58%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2+-fd72580 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 265 ms: 1.03x faster                                                   |
| chameleon      | 7.41 ms                                                | 7.02 ms: 1.06x faster                                                  |
| docutils       | 2.77 sec                                               | 2.61 sec: 1.06x faster                                                 |
| tornado_http   | 103 ms                                                 | 96.0 ms: 1.07x faster                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2+-fd72580 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization     | 578 ms                                                 | 565 ms: 1.02x faster                                                   |
| async_tree_none            | 472 ms                                                 | 463 ms: 1.02x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 455 ms: 1.01x slower                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 741 ms: 1.02x slower                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 747 ms: 1.03x slower                                                   |
| async_tree_io              | 1.16 sec                                               | 1.20 sec: 1.03x slower                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 1.24 sec: 1.05x slower                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 632 ms: 1.10x slower                                                   |
| Geometric mean             | (ref)                                                  | 1.03x slower                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2+-fd72580 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 93.3 ms: 1.04x faster                                                  |
| float          | 84.7 ms                                                | 83.0 ms: 1.02x faster                                                  |
| pidigits       | 187 ms                                                 | 222 ms: 1.19x slower                                                   |
| Geometric mean | (ref)                                                  | 1.04x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2+-fd72580 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 134 ms: 1.11x faster                                                   |
| regex_dna      | 212 ms                                                 | 216 ms: 1.02x slower                                                   |
| regex_effbot   | 3.61 ms                                                | 3.70 ms: 1.02x slower                                                  |
| regex_v8       | 23.1 ms                                                | 26.1 ms: 1.13x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2+-fd72580 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.12 sec: 1.10x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 58.9 ms: 1.05x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 309 us: 1.05x faster                                                   |
| xml_etree_generate   | 89.2 ms                                                | 86.0 ms: 1.04x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 222 us: 1.04x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 158 ms: 1.01x faster                                                   |
| json_loads           | 28.5 us                                                | 28.4 us: 1.00x faster                                                  |
| json_dumps           | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                           |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2+-fd72580 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 9.00 ms: 1.30x slower                                                  |
| python_startup         | 9.55 ms                                                | 12.6 ms: 1.32x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.31x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2+-fd72580 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.0 ms: 1.09x faster                                                  |
| django_template | 34.6 ms                                                | 32.2 ms: 1.07x faster                                                  |
| Geometric mean  | (ref)                                                  | 1.08x faster                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2+-fd72580 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols   | 158 us                                                 | 115 us: 1.37x faster                                                   |
| comprehensions             | 21.8 us                                                | 16.6 us: 1.31x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.15x faster                                                   |
| raytrace                   | 312 ms                                                 | 276 ms: 1.13x faster                                                   |
| chaos                      | 67.0 ms                                                | 59.5 ms: 1.12x faster                                                  |
| logging_format             | 7.23 us                                                | 6.43 us: 1.12x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.33 ms: 1.12x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 67.5 ms: 1.11x faster                                                  |
| regex_compile              | 148 ms                                                 | 134 ms: 1.11x faster                                                   |
| sympy_str                  | 300 ms                                                 | 271 ms: 1.11x faster                                                   |
| crypto_pyaes               | 81.9 ms                                                | 74.3 ms: 1.10x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 19.5 ms: 1.10x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 2.12 sec: 1.10x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.91 us: 1.09x faster                                                  |
| mako                       | 11.9 ms                                                | 11.0 ms: 1.09x faster                                                  |
| sqlalchemy_imperative      | 18.7 ms                                                | 17.2 ms: 1.09x faster                                                  |
| django_template            | 34.6 ms                                                | 32.2 ms: 1.07x faster                                                  |
| sqlalchemy_declarative     | 147 ms                                                 | 137 ms: 1.07x faster                                                   |
| tornado_http               | 103 ms                                                 | 96.0 ms: 1.07x faster                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.27 ms: 1.07x faster                                                  |
| generators                 | 31.2 ms                                                | 29.3 ms: 1.07x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.61 sec: 1.06x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 3.16 us: 1.06x faster                                                  |
| deepcopy                   | 371 us                                                 | 351 us: 1.06x faster                                                   |
| fannkuch                   | 417 ms                                                 | 395 ms: 1.06x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 38.6 us: 1.06x faster                                                  |
| chameleon                  | 7.41 ms                                                | 7.02 ms: 1.06x faster                                                  |
| nqueens                    | 83.3 ms                                                | 79.0 ms: 1.05x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 735 ms: 1.05x faster                                                   |
| pyflate                    | 482 ms                                                 | 458 ms: 1.05x faster                                                   |
| sqlglot_transpile          | 1.68 ms                                                | 1.60 ms: 1.05x faster                                                  |
| pathlib                    | 19.3 ms                                                | 18.4 ms: 1.05x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 58.9 ms: 1.05x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 309 us: 1.05x faster                                                   |
| sympy_expand               | 478 ms                                                 | 457 ms: 1.05x faster                                                   |
| scimark_sor                | 129 ms                                                 | 124 ms: 1.04x faster                                                   |
| spectral_norm              | 115 ms                                                 | 110 ms: 1.04x faster                                                   |
| hexiom                     | 6.41 ms                                                | 6.15 ms: 1.04x faster                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.50 sec: 1.04x faster                                                 |
| nbody                      | 97.0 ms                                                | 93.3 ms: 1.04x faster                                                  |
| coroutines                 | 23.2 ms                                                | 22.3 ms: 1.04x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 86.0 ms: 1.04x faster                                                  |
| unpickle_pure_python       | 230 us                                                 | 222 us: 1.04x faster                                                   |
| sqlglot_normalize          | 110 ms                                                 | 106 ms: 1.04x faster                                                   |
| 2to3                       | 274 ms                                                 | 265 ms: 1.03x faster                                                   |
| sqlglot_optimize           | 54.8 ms                                                | 53.4 ms: 1.03x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 66.8 ms: 1.03x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 565 ms: 1.02x faster                                                   |
| scimark_fft                | 382 ms                                                 | 374 ms: 1.02x faster                                                   |
| float                      | 84.7 ms                                                | 83.0 ms: 1.02x faster                                                  |
| meteor_contest             | 112 ms                                                 | 110 ms: 1.02x faster                                                   |
| scimark_lu                 | 118 ms                                                 | 116 ms: 1.02x faster                                                   |
| async_tree_none            | 472 ms                                                 | 463 ms: 1.02x faster                                                   |
| async_generators           | 463 ms                                                 | 456 ms: 1.01x faster                                                   |
| json                       | 5.26 ms                                                | 5.20 ms: 1.01x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 158 ms: 1.01x faster                                                   |
| json_loads                 | 28.5 us                                                | 28.4 us: 1.00x faster                                                  |
| go                         | 139 ms                                                 | 139 ms: 1.00x faster                                                   |
| bench_thread_pool          | 842 us                                                 | 840 us: 1.00x faster                                                   |
| json_dumps                 | 10.4 ms                                                | 10.5 ms: 1.01x slower                                                  |
| asyncio_websockets         | 551 ms                                                 | 556 ms: 1.01x slower                                                   |
| logging_silent             | 104 ns                                                 | 105 ns: 1.01x slower                                                   |
| async_tree_none_tg         | 450 ms                                                 | 455 ms: 1.01x slower                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.13 ms: 1.01x slower                                                  |
| regex_dna                  | 212 ms                                                 | 216 ms: 1.02x slower                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 741 ms: 1.02x slower                                                   |
| mdp                        | 2.63 sec                                               | 2.69 sec: 1.02x slower                                                 |
| regex_effbot               | 3.61 ms                                                | 3.70 ms: 1.02x slower                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 747 ms: 1.03x slower                                                   |
| async_tree_io              | 1.16 sec                                               | 1.20 sec: 1.03x slower                                                 |
| pycparser                  | 1.18 sec                                               | 1.22 sec: 1.04x slower                                                 |
| async_tree_io_tg           | 1.18 sec                                               | 1.24 sec: 1.05x slower                                                 |
| richards                   | 45.8 ms                                                | 49.1 ms: 1.07x slower                                                  |
| richards_super             | 51.5 ms                                                | 55.3 ms: 1.07x slower                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 632 ms: 1.10x slower                                                   |
| regex_v8                   | 23.1 ms                                                | 26.1 ms: 1.13x slower                                                  |
| pidigits                   | 187 ms                                                 | 222 ms: 1.19x slower                                                   |
| telco                      | 7.10 ms                                                | 8.46 ms: 1.19x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 4.72 ms: 1.24x slower                                                  |
| coverage                   | 72.7 ms                                                | 94.2 ms: 1.30x slower                                                  |
| python_startup_no_site     | 6.94 ms                                                | 9.00 ms: 1.30x slower                                                  |
| python_startup             | 9.55 ms                                                | 12.6 ms: 1.32x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.42 ms: 1.64x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (4): bench_mp_pool, gunicorn, sqlite_synth, xml_etree_iterparse
Ignored benchmarks (11) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, dask, mypy2, pickle, pickle_dict, pickle_list, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (12) of results/bm-20250128-3.13.0a2+-fd72580/bm-20250128-linux-x86_64-mdboom-specialize_compact_i-3.13.0a2+-fd72580.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.015x faster

# HPT report

- Reliability score: 99.58% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.07x