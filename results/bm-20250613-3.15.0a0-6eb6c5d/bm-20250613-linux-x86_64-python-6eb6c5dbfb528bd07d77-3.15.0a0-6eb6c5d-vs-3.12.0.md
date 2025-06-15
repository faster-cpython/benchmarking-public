# Results vs. 3.12.0

- fork: python
- ref: 6eb6c5dbfb528bd07d77
- machine: linux-x86_64
- commit hash: 6eb6c5d
- commit date: 2025-06-13
- overall geometric mean: 1.096x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 255 ms: 1.08x faster                                                  |
| docutils       | 2.77 sec                                               | 2.58 sec: 1.07x faster                                                |
| Geometric mean | (ref)                                                  | 1.08x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_io              | 1.16 sec                                               | 597 ms: 1.93x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 631 ms: 1.87x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 307 ms: 1.87x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 310 ms: 1.86x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 245 ms: 1.83x faster                                                  |
| async_tree_none            | 472 ms                                                 | 260 ms: 1.81x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 490 ms: 1.48x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 502 ms: 1.45x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.76x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 72.4 ms: 1.17x faster                                                 |
| pidigits       | 187 ms                                                 | 192 ms: 1.03x slower                                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 127 ms: 1.17x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.10 ms: 1.16x faster                                                 |
| regex_dna      | 212 ms                                                 | 184 ms: 1.16x faster                                                  |
| regex_v8       | 23.1 ms                                                | 22.1 ms: 1.05x faster                                                 |
| Geometric mean | (ref)                                                  | 1.13x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.04 sec: 1.14x faster                                                |
| xml_etree_parse      | 159 ms                                                 | 142 ms: 1.12x faster                                                  |
| xml_etree_iterparse  | 107 ms                                                 | 98.7 ms: 1.08x faster                                                 |
| unpickle_pure_python | 230 us                                                 | 217 us: 1.06x faster                                                  |
| xml_etree_generate   | 89.2 ms                                                | 85.3 ms: 1.05x faster                                                 |
| json_loads           | 28.5 us                                                | 27.4 us: 1.04x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 59.6 ms: 1.04x faster                                                 |
| json_dumps           | 10.4 ms                                                | 10.9 ms: 1.05x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                          |

Benchmark hidden because not significant (1): pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 6.91 ms: 1.00x faster                                                 |
| python_startup         | 9.55 ms                                                | 12.2 ms: 1.27x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.13x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 34.6 ms                                                | 32.2 ms: 1.07x faster                                                 |
| mako            | 11.9 ms                                                | 11.4 ms: 1.04x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.06x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                        | 2.63 sec                                               | 1.23 sec: 2.15x faster                                                |
| async_tree_io              | 1.16 sec                                               | 597 ms: 1.93x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 631 ms: 1.87x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 307 ms: 1.87x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 310 ms: 1.86x faster                                                  |
| async_tree_none_tg         | 450 ms                                                 | 245 ms: 1.83x faster                                                  |
| async_tree_none            | 472 ms                                                 | 260 ms: 1.81x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 490 ms: 1.48x faster                                                  |
| deepcopy                   | 371 us                                                 | 254 us: 1.46x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 502 ms: 1.45x faster                                                  |
| deepcopy_memo              | 40.7 us                                                | 28.8 us: 1.41x faster                                                 |
| comprehensions             | 21.8 us                                                | 16.0 us: 1.36x faster                                                 |
| go                         | 139 ms                                                 | 110 ms: 1.27x faster                                                  |
| deepcopy_reduce            | 3.35 us                                                | 2.71 us: 1.23x faster                                                 |
| float                      | 84.7 ms                                                | 72.4 ms: 1.17x faster                                                 |
| regex_compile              | 148 ms                                                 | 127 ms: 1.17x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.10 ms: 1.16x faster                                                 |
| regex_dna                  | 212 ms                                                 | 184 ms: 1.16x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 59.7 ms: 1.15x faster                                                 |
| raytrace                   | 312 ms                                                 | 272 ms: 1.15x faster                                                  |
| tomli_loads                | 2.33 sec                                               | 2.04 sec: 1.14x faster                                                |
| sympy_sum                  | 169 ms                                                 | 149 ms: 1.13x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 18.9 ms: 1.13x faster                                                 |
| pyflate                    | 482 ms                                                 | 427 ms: 1.13x faster                                                  |
| async_generators           | 463 ms                                                 | 411 ms: 1.12x faster                                                  |
| sympy_str                  | 300 ms                                                 | 266 ms: 1.12x faster                                                  |
| xml_etree_parse            | 159 ms                                                 | 142 ms: 1.12x faster                                                  |
| pathlib                    | 19.3 ms                                                | 17.4 ms: 1.11x faster                                                 |
| scimark_monte_carlo        | 75.1 ms                                                | 67.6 ms: 1.11x faster                                                 |
| chaos                      | 67.0 ms                                                | 60.3 ms: 1.11x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 74.5 ms: 1.10x faster                                                 |
| xml_etree_iterparse        | 107 ms                                                 | 98.7 ms: 1.08x faster                                                 |
| richards                   | 45.8 ms                                                | 42.4 ms: 1.08x faster                                                 |
| 2to3                       | 274 ms                                                 | 255 ms: 1.08x faster                                                  |
| django_template            | 34.6 ms                                                | 32.2 ms: 1.07x faster                                                 |
| docutils                   | 2.77 sec                                               | 2.58 sec: 1.07x faster                                                |
| hexiom                     | 6.41 ms                                                | 5.97 ms: 1.07x faster                                                 |
| scimark_sor                | 129 ms                                                 | 120 ms: 1.07x faster                                                  |
| deltablue                  | 3.72 ms                                                | 3.47 ms: 1.07x faster                                                 |
| meteor_contest             | 112 ms                                                 | 105 ms: 1.07x faster                                                  |
| richards_super             | 51.5 ms                                                | 48.6 ms: 1.06x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 217 us: 1.06x faster                                                  |
| sympy_expand               | 478 ms                                                 | 451 ms: 1.06x faster                                                  |
| pycparser                  | 1.18 sec                                               | 1.12 sec: 1.06x faster                                                |
| spectral_norm              | 115 ms                                                 | 109 ms: 1.06x faster                                                  |
| xml_etree_generate         | 89.2 ms                                                | 85.3 ms: 1.05x faster                                                 |
| regex_v8                   | 23.1 ms                                                | 22.1 ms: 1.05x faster                                                 |
| mako                       | 11.9 ms                                                | 11.4 ms: 1.04x faster                                                 |
| generators                 | 31.2 ms                                                | 30.0 ms: 1.04x faster                                                 |
| json_loads                 | 28.5 us                                                | 27.4 us: 1.04x faster                                                 |
| xml_etree_process          | 61.7 ms                                                | 59.6 ms: 1.04x faster                                                 |
| nqueens                    | 83.3 ms                                                | 80.6 ms: 1.03x faster                                                 |
| logging_format             | 7.23 us                                                | 7.00 us: 1.03x faster                                                 |
| scimark_fft                | 382 ms                                                 | 372 ms: 1.03x faster                                                  |
| logging_simple             | 6.46 us                                                | 6.32 us: 1.02x faster                                                 |
| fannkuch                   | 417 ms                                                 | 408 ms: 1.02x faster                                                  |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.98 ms: 1.01x faster                                                 |
| python_startup_no_site     | 6.94 ms                                                | 6.91 ms: 1.00x faster                                                 |
| asyncio_websockets         | 551 ms                                                 | 553 ms: 1.00x slower                                                  |
| scimark_lu                 | 118 ms                                                 | 119 ms: 1.01x slower                                                  |
| sqlite_synth               | 2.83 us                                                | 2.87 us: 1.01x slower                                                 |
| pidigits                   | 187 ms                                                 | 192 ms: 1.03x slower                                                  |
| pprint_safe_repr           | 776 ms                                                 | 799 ms: 1.03x slower                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.63 sec: 1.04x slower                                                |
| json_dumps                 | 10.4 ms                                                | 10.9 ms: 1.05x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 168 us: 1.07x slower                                                  |
| coroutines                 | 23.2 ms                                                | 25.0 ms: 1.08x slower                                                 |
| telco                      | 7.10 ms                                                | 8.06 ms: 1.14x slower                                                 |
| gc_traversal               | 3.79 ms                                                | 4.78 ms: 1.26x slower                                                 |
| python_startup             | 9.55 ms                                                | 12.2 ms: 1.27x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 2.59 ms: 1.76x slower                                                 |
| logging_silent             | 104 ns                                                 | 468 ns: 4.48x slower                                                  |
| coverage                   | 72.7 ms                                                | 433 ms: 5.95x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                          |

Benchmark hidden because not significant (3): json, pickle_pure_python, nbody
Ignored benchmarks (22) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, chameleon, dask, gunicorn, mypy2, pickle, pickle_dict, pickle_list, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tornado_http, unpack_sequence, unpickle, unpickle_list
Ignored benchmarks (16) of results/bm-20250613-3.15.0a0-6eb6c5d/bm-20250613-linux-x86_64-python-6eb6c5dbfb528bd07d77-3.15.0a0-6eb6c5d.json: bpe_tokeniser, connected_components, genshi_text, genshi_xml, html5lib, k_core, many_optionals, pylint, shortest_path, sphinx, sqlglot_v2_normalize, sqlglot_v2_optimize, sqlglot_v2_parse, sqlglot_v2_transpile, subparsers, thrift

- Geometric mean (including insignificant results): 1.096x faster

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.07x
- 95% likely to have a speedup of 1.06x
- 99% likely to have a speedup of 1.05x

# Memory
- memory change: 1.13x