# Results vs. 3.12.0

- fork: faster-cpython
- ref: no_thresholds
- machine: linux-x86_64
- commit hash: a4985b2
- commit date: 2024-03-28
- overall geometric mean: 1.01x slower
- HPT reliability: 90.08%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-a4985b2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 281 ms: 1.02x slower                                                      |
| chameleon      | 7.41 ms                                                | 7.06 ms: 1.05x faster                                                     |
| docutils       | 2.77 sec                                               | 2.94 sec: 1.06x slower                                                    |
| tornado_http   | 103 ms                                                 | 97.6 ms: 1.05x faster                                                     |
| Geometric mean | (ref)                                                  | 1.00x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-a4985b2 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 355 ms: 1.33x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 347 ms: 1.30x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 448 ms: 1.28x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 922 ms: 1.28x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 455 ms: 1.27x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 938 ms: 1.23x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 596 ms: 1.22x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 612 ms: 1.19x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.26x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-a4985b2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 97.0 ms                                                | 90.6 ms: 1.07x faster                                                     |
| float          | 84.7 ms                                                | 79.5 ms: 1.07x faster                                                     |
| pidigits       | 187 ms                                                 | 190 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                  | 1.04x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-a4985b2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 151 ms: 1.02x slower                                                      |
| regex_effbot   | 3.61 ms                                                | 3.81 ms: 1.05x slower                                                     |
| regex_dna      | 212 ms                                                 | 231 ms: 1.09x slower                                                      |
| regex_v8       | 23.1 ms                                                | 26.2 ms: 1.13x slower                                                     |
| Geometric mean | (ref)                                                  | 1.07x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-a4985b2 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.15 sec: 1.08x faster                                                    |
| pickle_pure_python   | 324 us                                                 | 306 us: 1.06x faster                                                      |
| unpickle_list        | 5.29 us                                                | 5.04 us: 1.05x faster                                                     |
| pickle_dict          | 35.5 us                                                | 34.0 us: 1.04x faster                                                     |
| pickle_list          | 5.08 us                                                | 4.94 us: 1.03x faster                                                     |
| json_loads           | 28.5 us                                                | 28.3 us: 1.01x faster                                                     |
| xml_etree_parse      | 159 ms                                                 | 162 ms: 1.01x slower                                                      |
| xml_etree_process    | 61.7 ms                                                | 62.8 ms: 1.02x slower                                                     |
| json_dumps           | 10.4 ms                                                | 10.6 ms: 1.02x slower                                                     |
| pickle               | 11.6 us                                                | 11.9 us: 1.03x slower                                                     |
| xml_etree_generate   | 89.2 ms                                                | 91.9 ms: 1.03x slower                                                     |
| unpickle             | 15.9 us                                                | 16.7 us: 1.05x slower                                                     |
| xml_etree_iterparse  | 107 ms                                                 | 113 ms: 1.06x slower                                                      |
| unpickle_pure_python | 230 us                                                 | 267 us: 1.16x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-a4985b2 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 9.55 ms                                                | 11.2 ms: 1.17x slower                                                     |
| python_startup_no_site | 6.94 ms                                                | 9.62 ms: 1.39x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.27x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-a4985b2 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.7 ms: 1.11x faster                                                     |
| django_template | 34.6 ms                                                | 37.0 ms: 1.07x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-a4985b2 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols   | 158 us                                                 | 116 us: 1.37x faster                                                      |
| async_tree_none            | 472 ms                                                 | 355 ms: 1.33x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 347 ms: 1.30x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 448 ms: 1.28x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 922 ms: 1.28x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 455 ms: 1.27x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 938 ms: 1.23x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 596 ms: 1.22x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 612 ms: 1.19x faster                                                      |
| comprehensions             | 21.8 us                                                | 19.5 us: 1.12x faster                                                     |
| scimark_fft                | 382 ms                                                 | 343 ms: 1.11x faster                                                      |
| mako                       | 11.9 ms                                                | 10.7 ms: 1.11x faster                                                     |
| crypto_pyaes               | 81.9 ms                                                | 74.9 ms: 1.09x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 2.15 sec: 1.08x faster                                                    |
| logging_format             | 7.23 us                                                | 6.73 us: 1.07x faster                                                     |
| logging_simple             | 6.46 us                                                | 6.01 us: 1.07x faster                                                     |
| nbody                      | 97.0 ms                                                | 90.6 ms: 1.07x faster                                                     |
| float                      | 84.7 ms                                                | 79.5 ms: 1.07x faster                                                     |
| pickle_pure_python         | 324 us                                                 | 306 us: 1.06x faster                                                      |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.79 ms: 1.05x faster                                                     |
| tornado_http               | 103 ms                                                 | 97.6 ms: 1.05x faster                                                     |
| unpickle_list              | 5.29 us                                                | 5.04 us: 1.05x faster                                                     |
| chameleon                  | 7.41 ms                                                | 7.06 ms: 1.05x faster                                                     |
| generators                 | 31.2 ms                                                | 29.8 ms: 1.05x faster                                                     |
| pickle_dict                | 35.5 us                                                | 34.0 us: 1.04x faster                                                     |
| fannkuch                   | 417 ms                                                 | 400 ms: 1.04x faster                                                      |
| raytrace                   | 312 ms                                                 | 302 ms: 1.03x faster                                                      |
| pickle_list                | 5.08 us                                                | 4.94 us: 1.03x faster                                                     |
| chaos                      | 67.0 ms                                                | 65.3 ms: 1.03x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                | 3.28 us: 1.02x faster                                                     |
| sympy_str                  | 300 ms                                                 | 295 ms: 1.02x faster                                                      |
| json_loads                 | 28.5 us                                                | 28.3 us: 1.01x faster                                                     |
| logging_silent             | 104 ns                                                 | 104 ns: 1.01x faster                                                      |
| gc_traversal               | 3.79 ms                                                | 3.77 ms: 1.01x faster                                                     |
| sympy_sum                  | 169 ms                                                 | 168 ms: 1.01x faster                                                      |
| spectral_norm              | 115 ms                                                 | 114 ms: 1.01x faster                                                      |
| scimark_monte_carlo        | 75.1 ms                                                | 74.8 ms: 1.00x faster                                                     |
| deepcopy                   | 371 us                                                 | 375 us: 1.01x slower                                                      |
| pprint_pformat             | 1.57 sec                                               | 1.58 sec: 1.01x slower                                                    |
| pyflate                    | 482 ms                                                 | 488 ms: 1.01x slower                                                      |
| sqlite_synth               | 2.83 us                                                | 2.87 us: 1.01x slower                                                     |
| dask                       | 372 ms                                                 | 376 ms: 1.01x slower                                                      |
| pidigits                   | 187 ms                                                 | 190 ms: 1.01x slower                                                      |
| xml_etree_parse            | 159 ms                                                 | 162 ms: 1.01x slower                                                      |
| regex_compile              | 148 ms                                                 | 151 ms: 1.02x slower                                                      |
| xml_etree_process          | 61.7 ms                                                | 62.8 ms: 1.02x slower                                                     |
| json_dumps                 | 10.4 ms                                                | 10.6 ms: 1.02x slower                                                     |
| 2to3                       | 274 ms                                                 | 281 ms: 1.02x slower                                                      |
| scimark_sor                | 129 ms                                                 | 132 ms: 1.02x slower                                                      |
| pickle                     | 11.6 us                                                | 11.9 us: 1.03x slower                                                     |
| xml_etree_generate         | 89.2 ms                                                | 91.9 ms: 1.03x slower                                                     |
| json                       | 5.26 ms                                                | 5.43 ms: 1.03x slower                                                     |
| asyncio_websockets         | 551 ms                                                 | 570 ms: 1.03x slower                                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.85 sec: 1.04x slower                                                    |
| sqlglot_normalize          | 110 ms                                                 | 115 ms: 1.04x slower                                                      |
| sympy_expand               | 478 ms                                                 | 498 ms: 1.04x slower                                                      |
| asyncio_tcp                | 491 ms                                                 | 512 ms: 1.04x slower                                                      |
| dulwich_log                | 68.5 ms                                                | 71.5 ms: 1.04x slower                                                     |
| sympy_integrate            | 21.4 ms                                                | 22.4 ms: 1.04x slower                                                     |
| gunicorn                   | 1.24 ms                                                | 1.30 ms: 1.05x slower                                                     |
| mdp                        | 2.63 sec                                               | 2.77 sec: 1.05x slower                                                    |
| aiohttp                    | 1.15 ms                                                | 1.21 ms: 1.05x slower                                                     |
| unpickle                   | 15.9 us                                                | 16.7 us: 1.05x slower                                                     |
| regex_effbot               | 3.61 ms                                                | 3.81 ms: 1.05x slower                                                     |
| bench_thread_pool          | 842 us                                                 | 890 us: 1.06x slower                                                      |
| xml_etree_iterparse        | 107 ms                                                 | 113 ms: 1.06x slower                                                      |
| docutils                   | 2.77 sec                                               | 2.94 sec: 1.06x slower                                                    |
| async_generators           | 463 ms                                                 | 493 ms: 1.07x slower                                                      |
| pycparser                  | 1.18 sec                                               | 1.26 sec: 1.07x slower                                                    |
| django_template            | 34.6 ms                                                | 37.0 ms: 1.07x slower                                                     |
| sqlglot_optimize           | 54.8 ms                                                | 59.4 ms: 1.08x slower                                                     |
| regex_dna                  | 212 ms                                                 | 231 ms: 1.09x slower                                                      |
| deepcopy_memo              | 40.7 us                                                | 44.9 us: 1.10x slower                                                     |
| deltablue                  | 3.72 ms                                                | 4.14 ms: 1.11x slower                                                     |
| scimark_lu                 | 118 ms                                                 | 132 ms: 1.12x slower                                                      |
| regex_v8                   | 23.1 ms                                                | 26.2 ms: 1.13x slower                                                     |
| richards_super             | 51.5 ms                                                | 58.6 ms: 1.14x slower                                                     |
| create_gc_cycles           | 1.48 ms                                                | 1.70 ms: 1.15x slower                                                     |
| richards                   | 45.8 ms                                                | 52.9 ms: 1.15x slower                                                     |
| unpickle_pure_python       | 230 us                                                 | 267 us: 1.16x slower                                                      |
| python_startup             | 9.55 ms                                                | 11.2 ms: 1.17x slower                                                     |
| telco                      | 7.10 ms                                                | 8.68 ms: 1.22x slower                                                     |
| go                         | 139 ms                                                 | 173 ms: 1.24x slower                                                      |
| nqueens                    | 83.3 ms                                                | 104 ms: 1.25x slower                                                      |
| hexiom                     | 6.41 ms                                                | 8.09 ms: 1.26x slower                                                     |
| coverage                   | 72.7 ms                                                | 97.5 ms: 1.34x slower                                                     |
| python_startup_no_site     | 6.94 ms                                                | 9.62 ms: 1.39x slower                                                     |
| unpack_sequence            | 54.0 ns                                                | 86.9 ns: 1.61x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (8): mypy2, pathlib, pprint_safe_repr, coroutines, meteor_contest, bench_mp_pool, sqlglot_transpile, sqlglot_parse
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240328-3.13.0a5+-a4985b2-JIT/bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-a4985b2.json: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 90.08% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 1.05x