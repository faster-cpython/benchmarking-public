# Results vs. 3.12.0

- fork: python
- ref: afc5ab6cce9d7095b99c
- machine: linux-x86_64
- commit hash: afc5ab6
- commit date: 2025-06-13
- overall geometric mean: 1.087x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-linux-x86_64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 255 ms: 1.08x faster                                                  |
| docutils       | 2.77 sec                                               | 2.58 sec: 1.07x faster                                                |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-linux-x86_64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 600 ms: 1.93x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 634 ms: 1.87x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 309 ms: 1.86x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 247 ms: 1.82x faster                                                  |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 492 ms: 1.47x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 502 ms: 1.45x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.75x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-linux-x86_64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 73.6 ms: 1.15x faster                                                 |
| pidigits       | 187 ms                                                 | 192 ms: 1.03x slower                                                  |
| nbody          | 97.0 ms                                                | 102 ms: 1.05x slower                                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-linux-x86_64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.22 ms: 1.12x faster                                                 |
| regex_dna      | 212 ms                                                 | 194 ms: 1.09x faster                                                  |
| regex_v8       | 23.1 ms                                                | 23.3 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.09x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-linux-x86_64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.03 sec: 1.15x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 143 ms: 1.11x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 99.1 ms: 1.08x faster                                                 |
| xml_etree_generate   | 89.2 ms                                                | 85.4 ms: 1.04x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 222 us: 1.04x faster                                                  |
| xml_etree_process    | 61.7 ms                                                | 60.2 ms: 1.03x faster                                                 |
| json_loads           | 28.5 us                                                | 27.8 us: 1.02x faster                                                 |
| json_dumps           | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-linux-x86_64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.92 ms: 1.00x faster                                                 |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.27x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-linux-x86_64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.3 ms: 1.07x faster                                                 |
| mako            | 11.9 ms                                                | 11.4 ms: 1.04x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-linux-x86_64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.22 sec: 2.15x faster                                                |
| async_tree_io              | 1.16 sec                                               | 600 ms: 1.93x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 634 ms: 1.87x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 309 ms: 1.86x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 312 ms: 1.85x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 247 ms: 1.82x faster                                                  |
| async_tree_none            | 472 ms                                                 | 261 ms: 1.81x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 492 ms: 1.47x faster                                                  |
| deepcopy                   | 371 us                                                 | 256 us: 1.45x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 502 ms: 1.45x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 29.4 us: 1.38x faster                                                 |
| comprehensions             | 21.8 us                                                | 16.1 us: 1.36x faster                                                 |
| go                         | 139 ms                                                 | 112 ms: 1.25x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.76 us: 1.21x faster                                                 |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 59.5 ms: 1.15x faster                                                 |
| float                      | 84.7 ms                                                | 73.6 ms: 1.15x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 2.03 sec: 1.15x faster                                                |
| sympy_sum                  | 169 ms                                                 | 147 ms: 1.15x faster                                                  |
| raytrace                   | 312 ms                                                 | 273 ms: 1.14x faster                                                  |
| pathlib                    | 19.3 ms                                                | 17.0 ms: 1.14x faster                                                 |
| sympy_integrate            | 21.4 ms                                                | 18.9 ms: 1.13x faster                                                 |
| async_generators           | 463 ms                                                 | 410 ms: 1.13x faster                                                  |
| sympy_str                  | 300 ms                                                 | 265 ms: 1.13x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.22 ms: 1.12x faster                                                 |
| pyflate                    | 482 ms                                                 | 432 ms: 1.12x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 143 ms: 1.11x faster                                                  |
| regex_dna                  | 212 ms                                                 | 194 ms: 1.09x faster                                                  |
| chaos                      | 67.0 ms                                                | 61.5 ms: 1.09x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 69.6 ms: 1.08x faster                                                 |
| 2to3                       | 274 ms                                                 | 255 ms: 1.08x faster                                                  |
| xml_etree_iterparse        | 107 ms                                                 | 99.1 ms: 1.08x faster                                                 |
| logging_format             | 7.23 us                                                | 6.72 us: 1.08x faster                                                 |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.07x faster                                                  |
| crypto_pyaes               | 81.9 ms                                                | 76.3 ms: 1.07x faster                                                 |
| docutils                   | 2.77 sec                                               | 2.58 sec: 1.07x faster                                                |
| django_template            | 34.6 ms                                                | 32.3 ms: 1.07x faster                                                 |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                                  |
| logging_simple             | 6.46 us                                                | 6.07 us: 1.06x faster                                                 |
| sympy_expand               | 478 ms                                                 | 450 ms: 1.06x faster                                                  |
| generators                 | 31.2 ms                                                | 29.5 ms: 1.06x faster                                                 |
| richards                   | 45.8 ms                                                | 43.4 ms: 1.06x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.54 ms: 1.05x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 85.4 ms: 1.04x faster                                                 |
| mako                       | 11.9 ms                                                | 11.4 ms: 1.04x faster                                                 |
| hexiom                     | 6.41 ms                                                | 6.15 ms: 1.04x faster                                                 |
| spectral_norm              | 115 ms                                                 | 110 ms: 1.04x faster                                                  |
| pycparser                  | 1.18 sec                                               | 1.14 sec: 1.04x faster                                                |
| unpickle_pure_python       | 230 us                                                 | 222 us: 1.04x faster                                                  |
| richards_super             | 51.5 ms                                                | 49.8 ms: 1.03x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 60.2 ms: 1.03x faster                                                 |
| json_loads                 | 28.5 us                                                | 27.8 us: 1.02x faster                                                 |
| json                       | 5.26 ms                                                | 5.13 ms: 1.02x faster                                                 |
| nqueens                    | 83.3 ms                                                | 81.5 ms: 1.02x faster                                                 |
| python_startup_no_site     | 6.94 ms                                                | 6.92 ms: 1.00x faster                                                 |
| asyncio_websockets         | 551 ms                                                 | 554 ms: 1.00x slower                                                  |
| regex_v8                   | 23.1 ms                                                | 23.3 ms: 1.01x slower                                                 |
| scimark_fft                | 382 ms                                                 | 386 ms: 1.01x slower                                                  |
| scimark_lu                 | 118 ms                                                 | 120 ms: 1.01x slower                                                  |
| sqlite_synth               | 2.83 us                                                | 2.88 us: 1.02x slower                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.18 ms: 1.02x slower                                                 |
| pidigits                   | 187 ms                                                 | 192 ms: 1.03x slower                                                  |
| pprint_safe_repr           | 776 ms                                                 | 805 ms: 1.04x slower                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.65 sec: 1.05x slower                                                |
| nbody                      | 97.0 ms                                                | 102 ms: 1.05x slower                                                  |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                                  |
| json_dumps                 | 10.4 ms                                                | 11.2 ms: 1.08x slower                                                 |
| coroutines                 | 23.2 ms                                                | 26.1 ms: 1.13x slower                                                 |
| telco                      | 7.10 ms                                                | 8.08 ms: 1.14x slower                                                 |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.27x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 4.95 ms: 1.30x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 2.60 ms: 1.76x slower                                                 |
| logging_silent             | 104 ns                                                 | 476 ns: 4.56x slower                                                  |
| coverage                   | 72.7 ms                                                | 423 ms: 5.82x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (2): pickle_pure_python, fannkuch
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250613-3.15.0a0-afc5ab6/bm-20250613-linux-x86_64-python-afc5ab6cce9d7095b99c-3.15.0a0-afc5ab6.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.087x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x

# Memory
- memory change: 1.13x