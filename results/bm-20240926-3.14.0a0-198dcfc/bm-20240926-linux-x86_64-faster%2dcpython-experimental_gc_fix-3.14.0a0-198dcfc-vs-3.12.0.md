# Results vs. 3.12.0

- fork: faster-cpython
- ref: experimental_gc_fix
- machine: linux-x86_64
- commit hash: 198dcfc
- commit date: 2024-09-26
- overall geometric mean: 1.06x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster
- Memory change: 0.96x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 271 ms: 1.01x faster                                                           |
| docutils       | 2.77 sec                                               | 2.70 sec: 1.03x faster                                                         |
| tornado_http   | 103 ms                                                 | 91.8 ms: 1.12x faster                                                          |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                   |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| async_tree_io_tg           | 1.18 sec                                               | 959 ms: 1.23x faster                                                           |
| async_tree_memoization     | 578 ms                                                 | 481 ms: 1.20x faster                                                           |
| async_tree_io              | 1.16 sec                                               | 987 ms: 1.17x faster                                                           |
| async_tree_none_tg         | 450 ms                                                 | 386 ms: 1.16x faster                                                           |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 627 ms: 1.16x faster                                                           |
| async_tree_memoization_tg  | 575 ms                                                 | 498 ms: 1.15x faster                                                           |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 644 ms: 1.13x faster                                                           |
| async_tree_none            | 472 ms                                                 | 424 ms: 1.11x faster                                                           |
| Geometric mean             | (ref)                                                  | 1.16x faster                                                                   |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 86.4 ms: 1.12x faster                                                          |
| float          | 84.7 ms                                                | 95.9 ms: 1.13x slower                                                          |
| Geometric mean | (ref)                                                  | 1.00x slower                                                                   |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 128 ms: 1.16x faster                                                           |
| regex_effbot   | 3.61 ms                                                | 3.64 ms: 1.01x slower                                                          |
| regex_dna      | 212 ms                                                 | 222 ms: 1.05x slower                                                           |
| regex_v8       | 23.1 ms                                                | 25.1 ms: 1.08x slower                                                          |
| Geometric mean | (ref)                                                  | 1.00x faster                                                                   |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.07 sec: 1.13x faster                                                         |
| unpickle_pure_python | 230 us                                                 | 211 us: 1.09x faster                                                           |
| unpickle             | 15.9 us                                                | 14.6 us: 1.08x faster                                                          |
| pickle_pure_python   | 324 us                                                 | 303 us: 1.07x faster                                                           |
| json_loads           | 28.5 us                                                | 27.2 us: 1.05x faster                                                          |
| pickle_dict          | 35.5 us                                                | 34.4 us: 1.03x faster                                                          |
| unpickle_list        | 5.29 us                                                | 5.25 us: 1.01x faster                                                          |
| pickle               | 11.6 us                                                | 11.6 us: 1.00x faster                                                          |
| pickle_list          | 5.08 us                                                | 5.13 us: 1.01x slower                                                          |
| xml_etree_generate   | 89.2 ms                                                | 91.0 ms: 1.02x slower                                                          |
| xml_etree_process    | 61.7 ms                                                | 65.2 ms: 1.06x slower                                                          |
| xml_etree_parse      | 159 ms                                                 | 171 ms: 1.07x slower                                                           |
| xml_etree_iterparse  | 107 ms                                                 | 157 ms: 1.47x slower                                                           |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                                   |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| python_startup_no_site | 6.94 ms                                                | 7.01 ms: 1.01x slower                                                          |
| python_startup         | 9.55 ms                                                | 10.7 ms: 1.12x slower                                                          |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                   |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 11.2 ms: 1.06x faster                                                          |
| django_template | 34.6 ms                                                | 34.2 ms: 1.01x faster                                                          |
| Geometric mean  | (ref)                                                  | 1.04x faster                                                                   |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------------:|
| deepcopy                   | 371 us                                                 | 256 us: 1.45x faster                                                           |
| deepcopy_memo              | 40.7 us                                                | 29.6 us: 1.38x faster                                                          |
| comprehensions             | 21.8 us                                                | 16.5 us: 1.32x faster                                                          |
| deepcopy_reduce            | 3.35 us                                                | 2.65 us: 1.26x faster                                                          |
| async_tree_io_tg           | 1.18 sec                                               | 959 ms: 1.23x faster                                                           |
| async_tree_memoization     | 578 ms                                                 | 481 ms: 1.20x faster                                                           |
| pathlib                    | 19.3 ms                                                | 16.1 ms: 1.20x faster                                                          |
| raytrace                   | 312 ms                                                 | 261 ms: 1.20x faster                                                           |
| go                         | 139 ms                                                 | 117 ms: 1.19x faster                                                           |
| unpack_sequence            | 54.0 ns                                                | 45.5 ns: 1.19x faster                                                          |
| async_tree_io              | 1.16 sec                                               | 987 ms: 1.17x faster                                                           |
| logging_format             | 7.23 us                                                | 6.20 us: 1.17x faster                                                          |
| async_tree_none_tg         | 450 ms                                                 | 386 ms: 1.16x faster                                                           |
| regex_compile              | 148 ms                                                 | 128 ms: 1.16x faster                                                           |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 627 ms: 1.16x faster                                                           |
| async_tree_memoization_tg  | 575 ms                                                 | 498 ms: 1.15x faster                                                           |
| logging_simple             | 6.46 us                                                | 5.61 us: 1.15x faster                                                          |
| chaos                      | 67.0 ms                                                | 58.5 ms: 1.14x faster                                                          |
| sympy_sum                  | 169 ms                                                 | 148 ms: 1.14x faster                                                           |
| crypto_pyaes               | 81.9 ms                                                | 71.9 ms: 1.14x faster                                                          |
| deltablue                  | 3.72 ms                                                | 3.29 ms: 1.13x faster                                                          |
| generators                 | 31.2 ms                                                | 27.6 ms: 1.13x faster                                                          |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 644 ms: 1.13x faster                                                           |
| tomli_loads                | 2.33 sec                                               | 2.07 sec: 1.13x faster                                                         |
| scimark_monte_carlo        | 75.1 ms                                                | 66.8 ms: 1.12x faster                                                          |
| nbody                      | 97.0 ms                                                | 86.4 ms: 1.12x faster                                                          |
| sympy_str                  | 300 ms                                                 | 268 ms: 1.12x faster                                                           |
| tornado_http               | 103 ms                                                 | 91.8 ms: 1.12x faster                                                          |
| async_tree_none            | 472 ms                                                 | 424 ms: 1.11x faster                                                           |
| sympy_integrate            | 21.4 ms                                                | 19.5 ms: 1.10x faster                                                          |
| pprint_safe_repr           | 776 ms                                                 | 708 ms: 1.10x faster                                                           |
| unpickle_pure_python       | 230 us                                                 | 211 us: 1.09x faster                                                           |
| unpickle                   | 15.9 us                                                | 14.6 us: 1.08x faster                                                          |
| pprint_pformat             | 1.57 sec                                               | 1.45 sec: 1.08x faster                                                         |
| gc_traversal               | 3.79 ms                                                | 3.53 ms: 1.07x faster                                                          |
| pickle_pure_python         | 324 us                                                 | 303 us: 1.07x faster                                                           |
| scimark_fft                | 382 ms                                                 | 358 ms: 1.07x faster                                                           |
| bench_thread_pool          | 842 us                                                 | 790 us: 1.07x faster                                                           |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.74 ms: 1.07x faster                                                          |
| dulwich_log                | 68.5 ms                                                | 64.5 ms: 1.06x faster                                                          |
| mako                       | 11.9 ms                                                | 11.2 ms: 1.06x faster                                                          |
| sympy_expand               | 478 ms                                                 | 453 ms: 1.06x faster                                                           |
| meteor_contest             | 112 ms                                                 | 107 ms: 1.05x faster                                                           |
| scimark_sor                | 129 ms                                                 | 123 ms: 1.05x faster                                                           |
| nqueens                    | 83.3 ms                                                | 79.5 ms: 1.05x faster                                                          |
| json_loads                 | 28.5 us                                                | 27.2 us: 1.05x faster                                                          |
| sqlglot_normalize          | 110 ms                                                 | 106 ms: 1.04x faster                                                           |
| sqlglot_transpile          | 1.68 ms                                                | 1.62 ms: 1.04x faster                                                          |
| mdp                        | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                         |
| sqlglot_parse              | 1.36 ms                                                | 1.31 ms: 1.04x faster                                                          |
| hexiom                     | 6.41 ms                                                | 6.18 ms: 1.04x faster                                                          |
| scimark_lu                 | 118 ms                                                 | 114 ms: 1.04x faster                                                           |
| logging_silent             | 104 ns                                                 | 101 ns: 1.04x faster                                                           |
| pickle_dict                | 35.5 us                                                | 34.4 us: 1.03x faster                                                          |
| fannkuch                   | 417 ms                                                 | 404 ms: 1.03x faster                                                           |
| spectral_norm              | 115 ms                                                 | 112 ms: 1.03x faster                                                           |
| docutils                   | 2.77 sec                                               | 2.70 sec: 1.03x faster                                                         |
| pyflate                    | 482 ms                                                 | 472 ms: 1.02x faster                                                           |
| asyncio_tcp                | 491 ms                                                 | 480 ms: 1.02x faster                                                           |
| json                       | 5.26 ms                                                | 5.17 ms: 1.02x faster                                                          |
| async_generators           | 463 ms                                                 | 455 ms: 1.02x faster                                                           |
| sqlglot_optimize           | 54.8 ms                                                | 54.1 ms: 1.01x faster                                                          |
| 2to3                       | 274 ms                                                 | 271 ms: 1.01x faster                                                           |
| django_template            | 34.6 ms                                                | 34.2 ms: 1.01x faster                                                          |
| unpickle_list              | 5.29 us                                                | 5.25 us: 1.01x faster                                                          |
| coroutines                 | 23.2 ms                                                | 23.0 ms: 1.01x faster                                                          |
| pickle                     | 11.6 us                                                | 11.6 us: 1.00x faster                                                          |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.78 sec: 1.00x faster                                                         |
| richards_super             | 51.5 ms                                                | 51.9 ms: 1.01x slower                                                          |
| asyncio_websockets         | 551 ms                                                 | 555 ms: 1.01x slower                                                           |
| regex_effbot               | 3.61 ms                                                | 3.64 ms: 1.01x slower                                                          |
| pickle_list                | 5.08 us                                                | 5.13 us: 1.01x slower                                                          |
| python_startup_no_site     | 6.94 ms                                                | 7.01 ms: 1.01x slower                                                          |
| typing_runtime_protocols   | 158 us                                                 | 160 us: 1.01x slower                                                           |
| xml_etree_generate         | 89.2 ms                                                | 91.0 ms: 1.02x slower                                                          |
| pycparser                  | 1.18 sec                                               | 1.22 sec: 1.03x slower                                                         |
| regex_dna                  | 212 ms                                                 | 222 ms: 1.05x slower                                                           |
| xml_etree_process          | 61.7 ms                                                | 65.2 ms: 1.06x slower                                                          |
| xml_etree_parse            | 159 ms                                                 | 171 ms: 1.07x slower                                                           |
| regex_v8                   | 23.1 ms                                                | 25.1 ms: 1.08x slower                                                          |
| python_startup             | 9.55 ms                                                | 10.7 ms: 1.12x slower                                                          |
| float                      | 84.7 ms                                                | 95.9 ms: 1.13x slower                                                          |
| create_gc_cycles           | 1.48 ms                                                | 1.71 ms: 1.16x slower                                                          |
| telco                      | 7.10 ms                                                | 8.30 ms: 1.17x slower                                                          |
| coverage                   | 72.7 ms                                                | 85.3 ms: 1.17x slower                                                          |
| xml_etree_iterparse        | 107 ms                                                 | 157 ms: 1.47x slower                                                           |
| Geometric mean             | (ref)                                                  | 1.06x faster                                                                   |

Benchmark hidden because not significant (5): sqlite_synth, json_dumps, bench_mp_pool, pidigits, richards
Ignored benchmarks (7) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: aiohttp, chameleon, dask, gunicorn, mypy2, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240926-3.14.0a0-198dcfc/bm-20240926-linux-x86_64-faster%2dcpython-experimental_gc_fix-3.14.0a0-198dcfc.json: bpe_tokeniser, genshi_text, genshi_xml, html5lib, pylint, thrift

# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x

# Memory
- memory change: 0.96x