# Results vs. 3.12.0

- fork: brandtbucher
- ref: justin_cold_14
- machine: linux-x86_64
- commit hash: b9d0b2b
- commit date: 2024-12-10
- overall geometric mean: 1.098x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_14-3.14.0a2+-b9d0b2b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 259 ms: 1.06x faster                                                   |
| docutils       | 2.77 sec                                               | 2.65 sec: 1.04x faster                                                 |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_14-3.14.0a2+-b9d0b2b |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 629 ms: 1.88x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 625 ms: 1.85x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 254 ms: 1.77x faster                                                   |
| async_tree_none            | 472 ms                                                 | 271 ms: 1.74x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 342 ms: 1.69x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 483 ms: 1.50x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 497 ms: 1.46x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.71x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_14-3.14.0a2+-b9d0b2b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 81.0 ms: 1.20x faster                                                  |
| float          | 84.7 ms                                                | 76.1 ms: 1.11x faster                                                  |
| pidigits       | 187 ms                                                 | 187 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_14-3.14.0a2+-b9d0b2b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 130 ms: 1.14x faster                                                   |
| regex_effbot   | 3.61 ms                                                | 3.26 ms: 1.11x faster                                                  |
| regex_dna      | 212 ms                                                 | 215 ms: 1.01x slower                                                   |
| regex_v8       | 23.1 ms                                                | 25.1 ms: 1.08x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_14-3.14.0a2+-b9d0b2b |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 1.93 sec: 1.20x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 196 us: 1.17x faster                                                   |
| xml_etree_parse      | 159 ms                                                 | 137 ms: 1.16x faster                                                   |
| xml_etree_iterparse  | 107 ms                                                 | 95.4 ms: 1.12x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 80.2 ms: 1.11x faster                                                  |
| json_loads           | 28.5 us                                                | 26.1 us: 1.09x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 57.1 ms: 1.08x faster                                                  |
| pickle_pure_python   | 324 us                                                 | 322 us: 1.01x faster                                                   |
| json_dumps           | 10.4 ms                                                | 11.0 ms: 1.06x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.10x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_14-3.14.0a2+-b9d0b2b |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                  |
| python_startup         | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.17x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_14-3.14.0a2+-b9d0b2b |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako           | 11.9 ms                                                | 10.2 ms: 1.17x faster                                                  |
| Geometric mean | (ref)                                                  | 1.08x faster                                                           |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20241210-linux-x86_64-brandtbucher-justin_cold_14-3.14.0a2+-b9d0b2b |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 629 ms: 1.88x faster                                                   |
| async_tree_io              | 1.16 sec                                               | 625 ms: 1.85x faster                                                   |
| async_tree_memoization_tg  | 575 ms                                                 | 317 ms: 1.81x faster                                                   |
| async_tree_none_tg         | 450 ms                                                 | 254 ms: 1.77x faster                                                   |
| async_tree_none            | 472 ms                                                 | 271 ms: 1.74x faster                                                   |
| async_tree_memoization     | 578 ms                                                 | 342 ms: 1.69x faster                                                   |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 483 ms: 1.50x faster                                                   |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 497 ms: 1.46x faster                                                   |
| deepcopy_memo              | 40.7 us                                                | 29.3 us: 1.39x faster                                                  |
| deepcopy                   | 371 us                                                 | 274 us: 1.35x faster                                                   |
| comprehensions             | 21.8 us                                                | 17.4 us: 1.25x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.74 us: 1.22x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 1.93 sec: 1.20x faster                                                 |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                                  |
| richards                   | 45.8 ms                                                | 38.2 ms: 1.20x faster                                                  |
| nbody                      | 97.0 ms                                                | 81.0 ms: 1.20x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 69.0 ms: 1.19x faster                                                  |
| scimark_fft                | 382 ms                                                 | 322 ms: 1.19x faster                                                   |
| unpickle_pure_python       | 230 us                                                 | 196 us: 1.17x faster                                                   |
| scimark_monte_carlo        | 75.1 ms                                                | 64.1 ms: 1.17x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.18 ms: 1.17x faster                                                  |
| mako                       | 11.9 ms                                                | 10.2 ms: 1.17x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 137 ms: 1.16x faster                                                   |
| richards_super             | 51.5 ms                                                | 45.0 ms: 1.15x faster                                                  |
| logging_format             | 7.23 us                                                | 6.33 us: 1.14x faster                                                  |
| regex_compile              | 148 ms                                                 | 130 ms: 1.14x faster                                                   |
| sqlalchemy_declarative     | 147 ms                                                 | 130 ms: 1.13x faster                                                   |
| chaos                      | 67.0 ms                                                | 59.4 ms: 1.13x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 95.4 ms: 1.12x faster                                                  |
| float                      | 84.7 ms                                                | 76.1 ms: 1.11x faster                                                  |
| sqlalchemy_imperative      | 18.7 ms                                                | 16.8 ms: 1.11x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 80.2 ms: 1.11x faster                                                  |
| json                       | 5.26 ms                                                | 4.74 ms: 1.11x faster                                                  |
| logging_simple             | 6.46 us                                                | 5.83 us: 1.11x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.26 ms: 1.11x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 154 ms: 1.10x faster                                                   |
| json_loads                 | 28.5 us                                                | 26.1 us: 1.09x faster                                                  |
| raytrace                   | 312 ms                                                 | 287 ms: 1.09x faster                                                   |
| sympy_str                  | 300 ms                                                 | 277 ms: 1.08x faster                                                   |
| scimark_sor                | 129 ms                                                 | 119 ms: 1.08x faster                                                   |
| xml_etree_process          | 61.7 ms                                                | 57.1 ms: 1.08x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 721 ms: 1.08x faster                                                   |
| pyflate                    | 482 ms                                                 | 453 ms: 1.06x faster                                                   |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.76 ms: 1.06x faster                                                  |
| 2to3                       | 274 ms                                                 | 259 ms: 1.06x faster                                                   |
| scimark_lu                 | 118 ms                                                 | 112 ms: 1.06x faster                                                   |
| pprint_pformat             | 1.57 sec                                               | 1.49 sec: 1.06x faster                                                 |
| sympy_integrate            | 21.4 ms                                                | 20.5 ms: 1.05x faster                                                  |
| docutils                   | 2.77 sec                                               | 2.65 sec: 1.04x faster                                                 |
| go                         | 139 ms                                                 | 134 ms: 1.04x faster                                                   |
| meteor_contest             | 112 ms                                                 | 108 ms: 1.04x faster                                                   |
| fannkuch                   | 417 ms                                                 | 402 ms: 1.04x faster                                                   |
| logging_silent             | 104 ns                                                 | 101 ns: 1.03x faster                                                   |
| sqlglot_transpile          | 1.68 ms                                                | 1.64 ms: 1.03x faster                                                  |
| sympy_expand               | 478 ms                                                 | 465 ms: 1.03x faster                                                   |
| sqlglot_parse              | 1.36 ms                                                | 1.33 ms: 1.03x faster                                                  |
| async_generators           | 463 ms                                                 | 454 ms: 1.02x faster                                                   |
| sqlite_synth               | 2.83 us                                                | 2.80 us: 1.01x faster                                                  |
| pickle_pure_python         | 324 us                                                 | 322 us: 1.01x faster                                                   |
| dulwich_log                | 68.5 ms                                                | 68.3 ms: 1.00x faster                                                  |
| pidigits                   | 187 ms                                                 | 187 ms: 1.00x faster                                                   |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                   |
| sqlglot_optimize           | 54.8 ms                                                | 55.2 ms: 1.01x slower                                                  |
| regex_dna                  | 212 ms                                                 | 215 ms: 1.01x slower                                                   |
| python_startup_no_site     | 6.94 ms                                                | 7.06 ms: 1.02x slower                                                  |
| bench_thread_pool          | 842 us                                                 | 880 us: 1.05x slower                                                   |
| mdp                        | 2.63 sec                                               | 2.78 sec: 1.06x slower                                                 |
| json_dumps                 | 10.4 ms                                                | 11.0 ms: 1.06x slower                                                  |
| telco                      | 7.10 ms                                                | 7.56 ms: 1.06x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 25.1 ms: 1.08x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 172 us: 1.09x slower                                                   |
| nqueens                    | 83.3 ms                                                | 91.5 ms: 1.10x slower                                                  |
| hexiom                     | 6.41 ms                                                | 7.10 ms: 1.11x slower                                                  |
| coverage                   | 72.7 ms                                                | 83.8 ms: 1.15x slower                                                  |
| mypy2                      | 830 ms                                                 | 959 ms: 1.16x slower                                                   |
| generators                 | 31.2 ms                                                | 36.5 ms: 1.17x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 4.87 ms: 1.28x slower                                                  |
| python_startup             | 9.55 ms                                                | 12.8 ms: 1.34x slower                                                  |
| create_gc_cycles           | 1.48 ms                                                | 2.45 ms: 1.66x slower                                                  |
| bench_mp_pool              | 24.0 ms                                                | 82.0 ms: 3.42x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                           |

Benchmark hidden because not significant (5): django_template, sqlglot_normalize, coroutines, spectral_norm, pycparser
Ignored benchmarks (13) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, chameleon, dask, gunicorn, pickle, pickle_dict, pickle_list, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (13) of results/bm-20241210-3.14.0a2+-b9d0b2b-JIT/bm-20241210-linux-x86_64-brandtbucher-justin_cold_14-3.14.0a2+-b9d0b2b.json: bpe_tokeniser, connected_components, djangocms, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, subparsers, thrift

- Geometric mean (including insignificant results): 1.098x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.11x