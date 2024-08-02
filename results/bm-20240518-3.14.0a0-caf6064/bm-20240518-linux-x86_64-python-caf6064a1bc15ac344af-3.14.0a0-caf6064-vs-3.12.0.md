# Results vs. 3.12.0

- fork: python
- ref: caf6064a1bc15ac344af
- machine: linux-x86_64
- commit hash: caf6064
- commit date: 2024-05-18
- overall geometric mean: 1.00x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 268 ms: 1.02x faster                                                  |
| chameleon      | 7.41 ms                                                | 6.97 ms: 1.06x faster                                                 |
| docutils       | 2.77 sec                                               | 2.78 sec: 1.00x slower                                                |
| tornado_http   | 103 ms                                                 | 94.1 ms: 1.09x faster                                                 |
| Geometric mean | (ref)                                                  | 1.04x faster                                                          |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 342 ms: 1.32x faster                                                  |
| async_tree_none            | 472 ms                                                 | 362 ms: 1.30x faster                                                  |
| async_tree_memoization_tg  | 575 ms                                                 | 447 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 585 ms: 1.24x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 471 ms: 1.23x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 969 ms: 1.22x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 947 ms: 1.22x faster                                                  |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 617 ms: 1.18x faster                                                  |
| Geometric mean             | (ref)                                                  | 1.25x faster                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 87.2 ms: 1.11x faster                                                 |
| float          | 84.7 ms                                                | 77.2 ms: 1.10x faster                                                 |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                  | 1.07x faster                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 134 ms: 1.10x faster                                                  |
| regex_effbot   | 3.61 ms                                                | 3.55 ms: 1.02x faster                                                 |
| regex_dna      | 212 ms                                                 | 219 ms: 1.03x slower                                                  |
| regex_v8       | 23.1 ms                                                | 25.5 ms: 1.10x slower                                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.11 sec: 1.10x faster                                                |
| pickle_pure_python   | 324 us                                                 | 305 us: 1.06x faster                                                  |
| unpickle_pure_python | 230 us                                                 | 220 us: 1.04x faster                                                  |
| pickle_dict          | 35.5 us                                                | 34.2 us: 1.04x faster                                                 |
| xml_etree_generate   | 89.2 ms                                                | 86.4 ms: 1.03x faster                                                 |
| xml_etree_process    | 61.7 ms                                                | 60.1 ms: 1.03x faster                                                 |
| pickle               | 11.6 us                                                | 11.7 us: 1.01x slower                                                 |
| json_loads           | 28.5 us                                                | 28.9 us: 1.01x slower                                                 |
| json_dumps           | 10.4 ms                                                | 10.7 ms: 1.03x slower                                                 |
| unpickle_list        | 5.29 us                                                | 5.47 us: 1.03x slower                                                 |
| unpickle             | 15.9 us                                                | 16.9 us: 1.07x slower                                                 |
| pickle_list          | 5.08 us                                                | 5.61 us: 1.10x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.10 ms: 1.02x slower                                                 |
| python_startup         | 9.55 ms                                                | 10.4 ms: 1.09x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.05x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.2 ms: 1.07x faster                                                 |
| django_template | 34.6 ms                                                | 34.3 ms: 1.01x faster                                                 |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064 |
|----------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_none_tg         | 450 ms                                                 | 342 ms: 1.32x faster                                                  |
| async_tree_none            | 472 ms                                                 | 362 ms: 1.30x faster                                                  |
| comprehensions             | 21.8 us                                                | 16.8 us: 1.30x faster                                                 |
| async_tree_memoization_tg  | 575 ms                                                 | 447 ms: 1.28x faster                                                  |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 585 ms: 1.24x faster                                                  |
| async_tree_memoization     | 578 ms                                                 | 471 ms: 1.23x faster                                                  |
| async_tree_io_tg           | 1.18 sec                                               | 969 ms: 1.22x faster                                                  |
| async_tree_io              | 1.16 sec                                               | 947 ms: 1.22x faster                                                  |
| pathlib                    | 19.3 ms                                                | 16.3 ms: 1.18x faster                                                 |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 617 ms: 1.18x faster                                                  |
| raytrace                   | 312 ms                                                 | 266 ms: 1.17x faster                                                  |
| logging_format             | 7.23 us                                                | 6.29 us: 1.15x faster                                                 |
| deltablue                  | 3.72 ms                                                | 3.29 ms: 1.13x faster                                                 |
| logging_simple             | 6.46 us                                                | 5.72 us: 1.13x faster                                                 |
| chaos                      | 67.0 ms                                                | 59.8 ms: 1.12x faster                                                 |
| crypto_pyaes               | 81.9 ms                                                | 73.4 ms: 1.11x faster                                                 |
| nbody                      | 97.0 ms                                                | 87.2 ms: 1.11x faster                                                 |
| tomli_loads                | 2.33 sec                                               | 2.11 sec: 1.10x faster                                                |
| regex_compile              | 148 ms                                                 | 134 ms: 1.10x faster                                                  |
| scimark_monte_carlo        | 75.1 ms                                                | 68.4 ms: 1.10x faster                                                 |
| float                      | 84.7 ms                                                | 77.2 ms: 1.10x faster                                                 |
| tornado_http               | 103 ms                                                 | 94.1 ms: 1.09x faster                                                 |
| sympy_sum                  | 169 ms                                                 | 155 ms: 1.09x faster                                                  |
| sympy_str                  | 300 ms                                                 | 278 ms: 1.08x faster                                                  |
| mako                       | 11.9 ms                                                | 11.2 ms: 1.07x faster                                                 |
| chameleon                  | 7.41 ms                                                | 6.97 ms: 1.06x faster                                                 |
| pickle_pure_python         | 324 us                                                 | 305 us: 1.06x faster                                                  |
| sympy_integrate            | 21.4 ms                                                | 20.3 ms: 1.06x faster                                                 |
| generators                 | 31.2 ms                                                | 29.7 ms: 1.05x faster                                                 |
| nqueens                    | 83.3 ms                                                | 79.6 ms: 1.05x faster                                                 |
| sqlglot_transpile          | 1.68 ms                                                | 1.61 ms: 1.04x faster                                                 |
| unpickle_pure_python       | 230 us                                                 | 220 us: 1.04x faster                                                  |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                                 |
| deepcopy_memo              | 40.7 us                                                | 39.1 us: 1.04x faster                                                 |
| fannkuch                   | 417 ms                                                 | 402 ms: 1.04x faster                                                  |
| pickle_dict                | 35.5 us                                                | 34.2 us: 1.04x faster                                                 |
| async_generators           | 463 ms                                                 | 447 ms: 1.04x faster                                                  |
| pprint_safe_repr           | 776 ms                                                 | 751 ms: 1.03x faster                                                  |
| dulwich_log                | 68.5 ms                                                | 66.4 ms: 1.03x faster                                                 |
| xml_etree_generate         | 89.2 ms                                                | 86.4 ms: 1.03x faster                                                 |
| spectral_norm              | 115 ms                                                 | 111 ms: 1.03x faster                                                  |
| deepcopy                   | 371 us                                                 | 361 us: 1.03x faster                                                  |
| xml_etree_process          | 61.7 ms                                                | 60.1 ms: 1.03x faster                                                 |
| deepcopy_reduce            | 3.35 us                                                | 3.26 us: 1.03x faster                                                 |
| logging_silent             | 104 ns                                                 | 102 ns: 1.03x faster                                                  |
| sympy_expand               | 478 ms                                                 | 467 ms: 1.02x faster                                                  |
| 2to3                       | 274 ms                                                 | 268 ms: 1.02x faster                                                  |
| pprint_pformat             | 1.57 sec                                               | 1.54 sec: 1.02x faster                                                |
| hexiom                     | 6.41 ms                                                | 6.30 ms: 1.02x faster                                                 |
| scimark_sor                | 129 ms                                                 | 127 ms: 1.02x faster                                                  |
| regex_effbot               | 3.61 ms                                                | 3.55 ms: 1.02x faster                                                 |
| meteor_contest             | 112 ms                                                 | 111 ms: 1.02x faster                                                  |
| sqlglot_normalize          | 110 ms                                                 | 109 ms: 1.02x faster                                                  |
| mdp                        | 2.63 sec                                               | 2.59 sec: 1.02x faster                                                |
| scimark_fft                | 382 ms                                                 | 377 ms: 1.01x faster                                                  |
| bench_thread_pool          | 842 us                                                 | 832 us: 1.01x faster                                                  |
| scimark_lu                 | 118 ms                                                 | 117 ms: 1.01x faster                                                  |
| django_template            | 34.6 ms                                                | 34.3 ms: 1.01x faster                                                 |
| bench_mp_pool              | 24.0 ms                                                | 23.8 ms: 1.01x faster                                                 |
| pyflate                    | 482 ms                                                 | 480 ms: 1.00x faster                                                  |
| sqlglot_optimize           | 54.8 ms                                                | 54.7 ms: 1.00x faster                                                 |
| docutils                   | 2.77 sec                                               | 2.78 sec: 1.00x slower                                                |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                                  |
| pickle                     | 11.6 us                                                | 11.7 us: 1.01x slower                                                 |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 5.11 ms: 1.01x slower                                                 |
| pycparser                  | 1.18 sec                                               | 1.19 sec: 1.01x slower                                                |
| json_loads                 | 28.5 us                                                | 28.9 us: 1.01x slower                                                 |
| python_startup_no_site     | 6.94 ms                                                | 7.10 ms: 1.02x slower                                                 |
| json                       | 5.26 ms                                                | 5.39 ms: 1.03x slower                                                 |
| asyncio_websockets         | 551 ms                                                 | 567 ms: 1.03x slower                                                  |
| gc_traversal               | 3.79 ms                                                | 3.90 ms: 1.03x slower                                                 |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.84 sec: 1.03x slower                                                |
| json_dumps                 | 10.4 ms                                                | 10.7 ms: 1.03x slower                                                 |
| asyncio_tcp                | 491 ms                                                 | 506 ms: 1.03x slower                                                  |
| regex_dna                  | 212 ms                                                 | 219 ms: 1.03x slower                                                  |
| unpickle_list              | 5.29 us                                                | 5.47 us: 1.03x slower                                                 |
| sqlite_synth               | 2.83 us                                                | 2.95 us: 1.04x slower                                                 |
| go                         | 139 ms                                                 | 145 ms: 1.04x slower                                                  |
| richards                   | 45.8 ms                                                | 48.0 ms: 1.05x slower                                                 |
| typing_runtime_protocols   | 158 us                                                 | 167 us: 1.06x slower                                                  |
| richards_super             | 51.5 ms                                                | 54.5 ms: 1.06x slower                                                 |
| unpickle                   | 15.9 us                                                | 16.9 us: 1.07x slower                                                 |
| python_startup             | 9.55 ms                                                | 10.4 ms: 1.09x slower                                                 |
| pickle_list                | 5.08 us                                                | 5.61 us: 1.10x slower                                                 |
| regex_v8                   | 23.1 ms                                                | 25.5 ms: 1.10x slower                                                 |
| create_gc_cycles           | 1.48 ms                                                | 1.82 ms: 1.23x slower                                                 |
| coverage                   | 72.7 ms                                                | 92.8 ms: 1.28x slower                                                 |
| telco                      | 7.10 ms                                                | 173 ms: 24.44x slower                                                 |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                          |

Benchmark hidden because not significant (4): dask, xml_etree_parse, coroutines, xml_etree_iterparse
Ignored benchmarks (6) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative, unpack_sequence
Ignored benchmarks (6) of results/bm-20240518-3.14.0a0-caf6064/bm-20240518-linux-x86_64-python-caf6064a1bc15ac344af-3.14.0a0-caf6064.json: flaskblogging, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x

# Memory
- memory change: 0.97x