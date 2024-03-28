# Results vs. 3.12.0

- fork: faster-cpython
- ref: no_thresholds
- machine: linux-x86_64
- commit hash: 174fc24
- commit date: 2024-03-28
- overall geometric mean: 1.01x slower
- HPT reliability: 93.53%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.05x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-174fc24 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                 | 280 ms: 1.02x slower                                                      |
| chameleon      | 7.41 ms                                                | 7.16 ms: 1.04x faster                                                     |
| docutils       | 2.77 sec                                               | 2.93 sec: 1.06x slower                                                    |
| tornado_http   | 103 ms                                                 | 96.9 ms: 1.06x faster                                                     |
| Geometric mean | (ref)                                                  | 1.00x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-174fc24 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none            | 472 ms                                                 | 360 ms: 1.31x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 909 ms: 1.30x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 348 ms: 1.29x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 448 ms: 1.28x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 458 ms: 1.26x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 932 ms: 1.24x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 593 ms: 1.22x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 613 ms: 1.18x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.26x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-174fc24 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 84.7 ms                                                | 79.6 ms: 1.06x faster                                                     |
| nbody          | 97.0 ms                                                | 92.7 ms: 1.05x faster                                                     |
| pidigits       | 187 ms                                                 | 189 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-174fc24 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 148 ms                                                 | 151 ms: 1.02x slower                                                      |
| regex_effbot   | 3.61 ms                                                | 3.78 ms: 1.05x slower                                                     |
| regex_dna      | 212 ms                                                 | 234 ms: 1.10x slower                                                      |
| regex_v8       | 23.1 ms                                                | 25.7 ms: 1.11x slower                                                     |
| Geometric mean | (ref)                                                  | 1.07x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-174fc24 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| tomli_loads          | 2.33 sec                                               | 2.13 sec: 1.09x faster                                                    |
| pickle_pure_python   | 324 us                                                 | 309 us: 1.05x faster                                                      |
| unpickle_list        | 5.29 us                                                | 5.19 us: 1.02x faster                                                     |
| pickle_list          | 5.08 us                                                | 5.12 us: 1.01x slower                                                     |
| xml_etree_process    | 61.7 ms                                                | 62.6 ms: 1.01x slower                                                     |
| pickle_dict          | 35.5 us                                                | 36.5 us: 1.03x slower                                                     |
| json_dumps           | 10.4 ms                                                | 10.7 ms: 1.03x slower                                                     |
| xml_etree_generate   | 89.2 ms                                                | 92.9 ms: 1.04x slower                                                     |
| pickle               | 11.6 us                                                | 12.1 us: 1.05x slower                                                     |
| xml_etree_iterparse  | 107 ms                                                 | 112 ms: 1.05x slower                                                      |
| unpickle             | 15.9 us                                                | 17.1 us: 1.08x slower                                                     |
| unpickle_pure_python | 230 us                                                 | 268 us: 1.17x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                              |

Benchmark hidden because not significant (2): json_loads, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-174fc24 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 9.55 ms                                                | 11.1 ms: 1.16x slower                                                     |
| python_startup_no_site | 6.94 ms                                                | 9.54 ms: 1.38x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.26x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-174fc24 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.9 ms                                                | 10.8 ms: 1.10x faster                                                     |
| django_template | 34.6 ms                                                | 37.1 ms: 1.07x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-174fc24 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols   | 158 us                                                 | 116 us: 1.36x faster                                                      |
| async_tree_none            | 472 ms                                                 | 360 ms: 1.31x faster                                                      |
| async_tree_io_tg           | 1.18 sec                                               | 909 ms: 1.30x faster                                                      |
| async_tree_none_tg         | 450 ms                                                 | 348 ms: 1.29x faster                                                      |
| async_tree_memoization_tg  | 575 ms                                                 | 448 ms: 1.28x faster                                                      |
| async_tree_memoization     | 578 ms                                                 | 458 ms: 1.26x faster                                                      |
| async_tree_io              | 1.16 sec                                               | 932 ms: 1.24x faster                                                      |
| async_tree_cpu_io_mixed_tg | 726 ms                                                 | 593 ms: 1.22x faster                                                      |
| async_tree_cpu_io_mixed    | 726 ms                                                 | 613 ms: 1.18x faster                                                      |
| comprehensions             | 21.8 us                                                | 19.4 us: 1.12x faster                                                     |
| scimark_fft                | 382 ms                                                 | 342 ms: 1.12x faster                                                      |
| mako                       | 11.9 ms                                                | 10.8 ms: 1.10x faster                                                     |
| tomli_loads                | 2.33 sec                                               | 2.13 sec: 1.09x faster                                                    |
| crypto_pyaes               | 81.9 ms                                                | 75.6 ms: 1.08x faster                                                     |
| logging_format             | 7.23 us                                                | 6.71 us: 1.08x faster                                                     |
| logging_simple             | 6.46 us                                                | 6.07 us: 1.06x faster                                                     |
| float                      | 84.7 ms                                                | 79.6 ms: 1.06x faster                                                     |
| tornado_http               | 103 ms                                                 | 96.9 ms: 1.06x faster                                                     |
| pickle_pure_python         | 324 us                                                 | 309 us: 1.05x faster                                                      |
| nbody                      | 97.0 ms                                                | 92.7 ms: 1.05x faster                                                     |
| scimark_sparse_mat_mult    | 5.06 ms                                                | 4.84 ms: 1.05x faster                                                     |
| generators                 | 31.2 ms                                                | 29.9 ms: 1.04x faster                                                     |
| chameleon                  | 7.41 ms                                                | 7.16 ms: 1.04x faster                                                     |
| raytrace                   | 312 ms                                                 | 303 ms: 1.03x faster                                                      |
| chaos                      | 67.0 ms                                                | 65.4 ms: 1.02x faster                                                     |
| coroutines                 | 23.2 ms                                                | 22.6 ms: 1.02x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                | 3.27 us: 1.02x faster                                                     |
| unpickle_list              | 5.29 us                                                | 5.19 us: 1.02x faster                                                     |
| fannkuch                   | 417 ms                                                 | 410 ms: 1.02x faster                                                      |
| sympy_str                  | 300 ms                                                 | 296 ms: 1.01x faster                                                      |
| pprint_safe_repr           | 776 ms                                                 | 767 ms: 1.01x faster                                                      |
| sympy_sum                  | 169 ms                                                 | 167 ms: 1.01x faster                                                      |
| meteor_contest             | 112 ms                                                 | 111 ms: 1.01x faster                                                      |
| spectral_norm              | 115 ms                                                 | 114 ms: 1.01x faster                                                      |
| gc_traversal               | 3.79 ms                                                | 3.78 ms: 1.00x faster                                                     |
| sqlglot_parse              | 1.36 ms                                                | 1.37 ms: 1.01x slower                                                     |
| pickle_list                | 5.08 us                                                | 5.12 us: 1.01x slower                                                     |
| pyflate                    | 482 ms                                                 | 488 ms: 1.01x slower                                                      |
| pidigits                   | 187 ms                                                 | 189 ms: 1.01x slower                                                      |
| xml_etree_process          | 61.7 ms                                                | 62.6 ms: 1.01x slower                                                     |
| sqlglot_transpile          | 1.68 ms                                                | 1.71 ms: 1.01x slower                                                     |
| logging_silent             | 104 ns                                                 | 106 ns: 1.02x slower                                                      |
| dask                       | 372 ms                                                 | 378 ms: 1.02x slower                                                      |
| pprint_pformat             | 1.57 sec                                               | 1.60 sec: 1.02x slower                                                    |
| sqlite_synth               | 2.83 us                                                | 2.88 us: 1.02x slower                                                     |
| regex_compile              | 148 ms                                                 | 151 ms: 1.02x slower                                                      |
| 2to3                       | 274 ms                                                 | 280 ms: 1.02x slower                                                      |
| scimark_sor                | 129 ms                                                 | 132 ms: 1.02x slower                                                      |
| pickle_dict                | 35.5 us                                                | 36.5 us: 1.03x slower                                                     |
| json_dumps                 | 10.4 ms                                                | 10.7 ms: 1.03x slower                                                     |
| asyncio_websockets         | 551 ms                                                 | 570 ms: 1.03x slower                                                      |
| sqlglot_normalize          | 110 ms                                                 | 114 ms: 1.04x slower                                                      |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.86 sec: 1.04x slower                                                    |
| json                       | 5.26 ms                                                | 5.47 ms: 1.04x slower                                                     |
| asyncio_tcp                | 491 ms                                                 | 511 ms: 1.04x slower                                                      |
| xml_etree_generate         | 89.2 ms                                                | 92.9 ms: 1.04x slower                                                     |
| sympy_integrate            | 21.4 ms                                                | 22.4 ms: 1.04x slower                                                     |
| mdp                        | 2.63 sec                                               | 2.75 sec: 1.04x slower                                                    |
| sympy_expand               | 478 ms                                                 | 500 ms: 1.05x slower                                                      |
| pickle                     | 11.6 us                                                | 12.1 us: 1.05x slower                                                     |
| regex_effbot               | 3.61 ms                                                | 3.78 ms: 1.05x slower                                                     |
| dulwich_log                | 68.5 ms                                                | 71.8 ms: 1.05x slower                                                     |
| aiohttp                    | 1.15 ms                                                | 1.21 ms: 1.05x slower                                                     |
| xml_etree_iterparse        | 107 ms                                                 | 112 ms: 1.05x slower                                                      |
| gunicorn                   | 1.24 ms                                                | 1.31 ms: 1.06x slower                                                     |
| bench_thread_pool          | 842 us                                                 | 890 us: 1.06x slower                                                      |
| docutils                   | 2.77 sec                                               | 2.93 sec: 1.06x slower                                                    |
| pycparser                  | 1.18 sec                                               | 1.25 sec: 1.06x slower                                                    |
| django_template            | 34.6 ms                                                | 37.1 ms: 1.07x slower                                                     |
| unpickle                   | 15.9 us                                                | 17.1 us: 1.08x slower                                                     |
| async_generators           | 463 ms                                                 | 502 ms: 1.08x slower                                                      |
| sqlglot_optimize           | 54.8 ms                                                | 59.5 ms: 1.09x slower                                                     |
| deepcopy_memo              | 40.7 us                                                | 44.8 us: 1.10x slower                                                     |
| regex_dna                  | 212 ms                                                 | 234 ms: 1.10x slower                                                      |
| regex_v8                   | 23.1 ms                                                | 25.7 ms: 1.11x slower                                                     |
| deltablue                  | 3.72 ms                                                | 4.15 ms: 1.12x slower                                                     |
| scimark_lu                 | 118 ms                                                 | 132 ms: 1.12x slower                                                      |
| create_gc_cycles           | 1.48 ms                                                | 1.69 ms: 1.15x slower                                                     |
| richards_super             | 51.5 ms                                                | 59.7 ms: 1.16x slower                                                     |
| python_startup             | 9.55 ms                                                | 11.1 ms: 1.16x slower                                                     |
| unpickle_pure_python       | 230 us                                                 | 268 us: 1.17x slower                                                      |
| richards                   | 45.8 ms                                                | 54.0 ms: 1.18x slower                                                     |
| telco                      | 7.10 ms                                                | 8.85 ms: 1.25x slower                                                     |
| go                         | 139 ms                                                 | 175 ms: 1.25x slower                                                      |
| hexiom                     | 6.41 ms                                                | 8.12 ms: 1.27x slower                                                     |
| nqueens                    | 83.3 ms                                                | 109 ms: 1.31x slower                                                      |
| coverage                   | 72.7 ms                                                | 97.8 ms: 1.35x slower                                                     |
| python_startup_no_site     | 6.94 ms                                                | 9.54 ms: 1.38x slower                                                     |
| unpack_sequence            | 54.0 ns                                                | 88.0 ns: 1.63x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (7): mypy2, deepcopy, bench_mp_pool, json_loads, scimark_monte_carlo, xml_etree_parse, pathlib
Ignored benchmarks (2) of results/bm-20231002-3.12.0-0fb18b0/bm-20231002-linux-x86_64-python-v3.12.0-3.12.0-0fb18b0.json: sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (6) of results/bm-20240328-3.13.0a5+-174fc24-JIT/bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-174fc24.json: djangocms, genshi_text, genshi_xml, html5lib, pylint, thrift


# HPT report

- Reliability score: 93.53% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 1.05x