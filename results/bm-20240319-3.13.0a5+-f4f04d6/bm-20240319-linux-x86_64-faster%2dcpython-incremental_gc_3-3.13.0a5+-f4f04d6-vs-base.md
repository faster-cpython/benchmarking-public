# Results vs. base

- fork: faster-cpython
- ref: incremental_gc_3
- machine: linux-x86_64
- commit hash: f4f04d6
- commit date: 2024-03-19
- overall geometric mean: 1.24x slower
- HPT reliability: 99.79%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240319-linux-x86_64-python-039d20ae5428dfe3d704-3.13.0a5+-039d20a | bm-20240319-linux-x86_64-faster%2dcpython-incremental_gc_3-3.13.0a5+-f4f04d6 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 272 ms                                                                 | 294 ms: 1.08x slower                                                         |
| chameleon      | 7.01 ms                                                                | 6.94 ms: 1.01x faster                                                        |
| docutils       | 2.65 sec                                                               | 4.66 sec: 1.76x slower                                                       |
| html5lib       | 67.6 ms                                                                | 75.0 ms: 1.11x slower                                                        |
| tornado_http   | 97.4 ms                                                                | 99.0 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.16x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240319-linux-x86_64-python-039d20ae5428dfe3d704-3.13.0a5+-039d20a | bm-20240319-linux-x86_64-faster%2dcpython-incremental_gc_3-3.13.0a5+-f4f04d6 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 727 ms                                                                 | 4.17 sec: 5.73x slower                                                       |
| async_tree_cpu_io_mixed_tg | 744 ms                                                                 | 4.58 sec: 6.15x slower                                                       |
| async_tree_none            | 451 ms                                                                 | 3.42 sec: 7.59x slower                                                       |
| async_tree_memoization     | 578 ms                                                                 | 4.43 sec: 7.66x slower                                                       |
| async_tree_memoization_tg  | 593 ms                                                                 | 4.73 sec: 7.98x slower                                                       |
| async_tree_none_tg         | 459 ms                                                                 | 3.78 sec: 8.23x slower                                                       |
| async_tree_io              | 1.21 sec                                                               | 13.3 sec: 10.98x slower                                                      |
| async_tree_io_tg           | 1.22 sec                                                               | 14.3 sec: 11.69x slower                                                      |
| Geometric mean             | (ref)                                                                  | 8.03x slower                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240319-linux-x86_64-python-039d20ae5428dfe3d704-3.13.0a5+-039d20a | bm-20240319-linux-x86_64-faster%2dcpython-incremental_gc_3-3.13.0a5+-f4f04d6 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 98.6 ms                                                                | 91.7 ms: 1.08x faster                                                        |
| pidigits       | 190 ms                                                                 | 190 ms: 1.00x faster                                                         |
| float          | 81.8 ms                                                                | 144 ms: 1.76x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.18x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240319-linux-x86_64-python-039d20ae5428dfe3d704-3.13.0a5+-039d20a | bm-20240319-linux-x86_64-faster%2dcpython-incremental_gc_3-3.13.0a5+-f4f04d6 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 135 ms                                                                 | 134 ms: 1.01x faster                                                         |
| regex_effbot   | 3.61 ms                                                                | 3.69 ms: 1.02x slower                                                        |
| regex_v8       | 25.5 ms                                                                | 26.6 ms: 1.04x slower                                                        |
| regex_dna      | 212 ms                                                                 | 228 ms: 1.08x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240319-linux-x86_64-python-039d20ae5428dfe3d704-3.13.0a5+-039d20a | bm-20240319-linux-x86_64-faster%2dcpython-incremental_gc_3-3.13.0a5+-f4f04d6 |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| unpickle_pure_python | 224 us                                                                 | 216 us: 1.04x faster                                                         |
| pickle_pure_python   | 302 us                                                                 | 297 us: 1.02x faster                                                         |
| pickle               | 11.9 us                                                                | 11.9 us: 1.00x slower                                                        |
| json_dumps           | 10.5 ms                                                                | 10.6 ms: 1.01x slower                                                        |
| pickle_dict          | 33.5 us                                                                | 35.0 us: 1.05x slower                                                        |
| pickle_list          | 4.94 us                                                                | 5.33 us: 1.08x slower                                                        |
| xml_etree_generate   | 87.3 ms                                                                | 98.4 ms: 1.13x slower                                                        |
| xml_etree_process    | 60.1 ms                                                                | 67.9 ms: 1.13x slower                                                        |
| xml_etree_parse      | 161 ms                                                                 | 217 ms: 1.35x slower                                                         |
| xml_etree_iterparse  | 107 ms                                                                 | 165 ms: 1.54x slower                                                         |
| Geometric mean       | (ref)                                                                  | 1.08x slower                                                                 |

Benchmark hidden because not significant (4): unpickle, json_loads, tomli_loads, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240319-linux-x86_64-python-039d20ae5428dfe3d704-3.13.0a5+-039d20a | bm-20240319-linux-x86_64-faster%2dcpython-incremental_gc_3-3.13.0a5+-f4f04d6 |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup_no_site | 8.92 ms                                                                | 8.85 ms: 1.01x faster                                                        |
| python_startup         | 10.3 ms                                                                | 10.5 ms: 1.02x slower                                                        |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240319-linux-x86_64-python-039d20ae5428dfe3d704-3.13.0a5+-039d20a | bm-20240319-linux-x86_64-faster%2dcpython-incremental_gc_3-3.13.0a5+-f4f04d6 |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako           | 11.2 ms                                                                | 11.1 ms: 1.01x faster                                                        |
| genshi_xml     | 52.1 ms                                                                | 59.8 ms: 1.15x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                                 |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark                  | bm-20240319-linux-x86_64-python-039d20ae5428dfe3d704-3.13.0a5+-039d20a | bm-20240319-linux-x86_64-faster%2dcpython-incremental_gc_3-3.13.0a5+-f4f04d6 |
|----------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| gc_traversal               | 3.83 ms                                                                | 3.56 ms: 1.08x faster                                                        |
| scimark_sor                | 129 ms                                                                 | 120 ms: 1.08x faster                                                         |
| nbody                      | 98.6 ms                                                                | 91.7 ms: 1.08x faster                                                        |
| pyflate                    | 487 ms                                                                 | 461 ms: 1.06x faster                                                         |
| hexiom                     | 6.34 ms                                                                | 6.10 ms: 1.04x faster                                                        |
| unpickle_pure_python       | 224 us                                                                 | 216 us: 1.04x faster                                                         |
| spectral_norm              | 113 ms                                                                 | 109 ms: 1.04x faster                                                         |
| deepcopy_memo              | 38.0 us                                                                | 36.8 us: 1.03x faster                                                        |
| scimark_monte_carlo        | 69.1 ms                                                                | 66.9 ms: 1.03x faster                                                        |
| comprehensions             | 16.5 us                                                                | 16.1 us: 1.03x faster                                                        |
| generators                 | 29.9 ms                                                                | 29.2 ms: 1.02x faster                                                        |
| scimark_lu                 | 116 ms                                                                 | 113 ms: 1.02x faster                                                         |
| create_gc_cycles           | 1.52 ms                                                                | 1.49 ms: 1.02x faster                                                        |
| raytrace                   | 269 ms                                                                 | 263 ms: 1.02x faster                                                         |
| coroutines                 | 23.2 ms                                                                | 22.8 ms: 1.02x faster                                                        |
| deepcopy_reduce            | 3.17 us                                                                | 3.11 us: 1.02x faster                                                        |
| pickle_pure_python         | 302 us                                                                 | 297 us: 1.02x faster                                                         |
| crypto_pyaes               | 73.1 ms                                                                | 71.9 ms: 1.02x faster                                                        |
| chaos                      | 61.7 ms                                                                | 60.8 ms: 1.01x faster                                                        |
| deepcopy                   | 350 us                                                                 | 345 us: 1.01x faster                                                         |
| thrift                     | 811 us                                                                 | 800 us: 1.01x faster                                                         |
| mako                       | 11.2 ms                                                                | 11.1 ms: 1.01x faster                                                        |
| coverage                   | 97.1 ms                                                                | 96.1 ms: 1.01x faster                                                        |
| richards                   | 45.6 ms                                                                | 45.1 ms: 1.01x faster                                                        |
| chameleon                  | 7.01 ms                                                                | 6.94 ms: 1.01x faster                                                        |
| logging_simple             | 5.90 us                                                                | 5.85 us: 1.01x faster                                                        |
| bench_mp_pool              | 23.9 ms                                                                | 23.7 ms: 1.01x faster                                                        |
| regex_compile              | 135 ms                                                                 | 134 ms: 1.01x faster                                                         |
| python_startup_no_site     | 8.92 ms                                                                | 8.85 ms: 1.01x faster                                                        |
| pprint_pformat             | 1.51 sec                                                               | 1.50 sec: 1.01x faster                                                       |
| meteor_contest             | 110 ms                                                                 | 110 ms: 1.01x faster                                                         |
| logging_silent             | 98.1 ns                                                                | 97.5 ns: 1.01x faster                                                        |
| logging_format             | 6.55 us                                                                | 6.51 us: 1.01x faster                                                        |
| sympy_integrate            | 20.0 ms                                                                | 19.9 ms: 1.01x faster                                                        |
| pprint_safe_repr           | 736 ms                                                                 | 734 ms: 1.00x faster                                                         |
| bench_thread_pool          | 826 us                                                                 | 824 us: 1.00x faster                                                         |
| pidigits                   | 190 ms                                                                 | 190 ms: 1.00x faster                                                         |
| asyncio_tcp_ssl            | 1.84 sec                                                               | 1.84 sec: 1.00x slower                                                       |
| pickle                     | 11.9 us                                                                | 11.9 us: 1.00x slower                                                        |
| scimark_fft                | 364 ms                                                                 | 366 ms: 1.00x slower                                                         |
| asyncio_tcp                | 500 ms                                                                 | 502 ms: 1.01x slower                                                         |
| json_dumps                 | 10.5 ms                                                                | 10.6 ms: 1.01x slower                                                        |
| asyncio_websockets         | 564 ms                                                                 | 568 ms: 1.01x slower                                                         |
| sqlite_synth               | 2.90 us                                                                | 2.93 us: 1.01x slower                                                        |
| richards_super             | 51.5 ms                                                                | 52.3 ms: 1.02x slower                                                        |
| tornado_http               | 97.4 ms                                                                | 99.0 ms: 1.02x slower                                                        |
| pathlib                    | 18.3 ms                                                                | 18.6 ms: 1.02x slower                                                        |
| fannkuch                   | 399 ms                                                                 | 406 ms: 1.02x slower                                                         |
| dulwich_log                | 66.8 ms                                                                | 68.1 ms: 1.02x slower                                                        |
| python_startup             | 10.3 ms                                                                | 10.5 ms: 1.02x slower                                                        |
| regex_effbot               | 3.61 ms                                                                | 3.69 ms: 1.02x slower                                                        |
| mdp                        | 2.56 sec                                                               | 2.62 sec: 1.02x slower                                                       |
| typing_runtime_protocols   | 111 us                                                                 | 114 us: 1.02x slower                                                         |
| sqlglot_optimize           | 54.1 ms                                                                | 56.1 ms: 1.04x slower                                                        |
| regex_v8                   | 25.5 ms                                                                | 26.6 ms: 1.04x slower                                                        |
| pickle_dict                | 33.5 us                                                                | 35.0 us: 1.05x slower                                                        |
| gunicorn                   | 1.26 ms                                                                | 1.33 ms: 1.05x slower                                                        |
| djangocms                  | 31.7 us                                                                | 33.3 us: 1.05x slower                                                        |
| aiohttp                    | 1.16 ms                                                                | 1.23 ms: 1.06x slower                                                        |
| regex_dna                  | 212 ms                                                                 | 228 ms: 1.08x slower                                                         |
| pickle_list                | 4.94 us                                                                | 5.33 us: 1.08x slower                                                        |
| 2to3                       | 272 ms                                                                 | 294 ms: 1.08x slower                                                         |
| deltablue                  | 3.27 ms                                                                | 3.57 ms: 1.09x slower                                                        |
| html5lib                   | 67.6 ms                                                                | 75.0 ms: 1.11x slower                                                        |
| xml_etree_generate         | 87.3 ms                                                                | 98.4 ms: 1.13x slower                                                        |
| xml_etree_process          | 60.1 ms                                                                | 67.9 ms: 1.13x slower                                                        |
| genshi_xml                 | 52.1 ms                                                                | 59.8 ms: 1.15x slower                                                        |
| sqlglot_transpile          | 1.61 ms                                                                | 1.86 ms: 1.16x slower                                                        |
| sqlglot_parse              | 1.28 ms                                                                | 1.49 ms: 1.17x slower                                                        |
| async_generators           | 454 ms                                                                 | 536 ms: 1.18x slower                                                         |
| unpack_sequence            | 47.0 ns                                                                | 56.9 ns: 1.21x slower                                                        |
| pycparser                  | 1.20 sec                                                               | 1.52 sec: 1.27x slower                                                       |
| xml_etree_parse            | 161 ms                                                                 | 217 ms: 1.35x slower                                                         |
| xml_etree_iterparse        | 107 ms                                                                 | 165 ms: 1.54x slower                                                         |
| docutils                   | 2.65 sec                                                               | 4.66 sec: 1.76x slower                                                       |
| float                      | 81.8 ms                                                                | 144 ms: 1.76x slower                                                         |
| dask                       | 369 ms                                                                 | 756 ms: 2.05x slower                                                         |
| pylint                     | 311 ms                                                                 | 1.00 sec: 3.22x slower                                                       |
| async_tree_cpu_io_mixed    | 727 ms                                                                 | 4.17 sec: 5.73x slower                                                       |
| async_tree_cpu_io_mixed_tg | 744 ms                                                                 | 4.58 sec: 6.15x slower                                                       |
| async_tree_none            | 451 ms                                                                 | 3.42 sec: 7.59x slower                                                       |
| async_tree_memoization     | 578 ms                                                                 | 4.43 sec: 7.66x slower                                                       |
| async_tree_memoization_tg  | 593 ms                                                                 | 4.73 sec: 7.98x slower                                                       |
| async_tree_none_tg         | 459 ms                                                                 | 3.78 sec: 8.23x slower                                                       |
| async_tree_io              | 1.21 sec                                                               | 13.3 sec: 10.98x slower                                                      |
| async_tree_io_tg           | 1.22 sec                                                               | 14.3 sec: 11.69x slower                                                      |
| Geometric mean             | (ref)                                                                  | 1.24x slower                                                                 |

Benchmark hidden because not significant (16): mypy2, unpickle, json_loads, go, telco, tomli_loads, django_template, scimark_sparse_mat_mult, unpickle_list, sympy_str, nqueens, sympy_sum, genshi_text, sqlglot_normalize, sympy_expand, json


# HPT report

- Reliability score: 99.79% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 0.99x