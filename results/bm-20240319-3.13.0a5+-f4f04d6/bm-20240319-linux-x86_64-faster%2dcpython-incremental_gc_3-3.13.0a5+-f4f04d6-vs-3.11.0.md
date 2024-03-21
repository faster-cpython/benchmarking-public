# Results vs. 3.11.0

- fork: faster-cpython
- ref: incremental_gc_3
- machine: linux-x86_64
- commit hash: f4f04d6
- commit date: 2024-03-19
- overall geometric mean: 1.18x slower
- HPT reliability: 95.06%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240319-linux-x86_64-faster%2dcpython-incremental_gc_3-3.13.0a5+-f4f04d6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 264 ms                                                 | 294 ms: 1.11x slower                                                         |
| chameleon      | 6.70 ms                                                | 6.94 ms: 1.04x slower                                                        |
| docutils       | 2.66 sec                                               | 4.66 sec: 1.75x slower                                                       |
| html5lib       | 64.8 ms                                                | 75.0 ms: 1.16x slower                                                        |
| tornado_http   | 98.1 ms                                                | 99.0 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                  | 1.19x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240319-linux-x86_64-faster%2dcpython-incremental_gc_3-3.13.0a5+-f4f04d6 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 749 ms                                                 | 4.17 sec: 5.57x slower                                                       |
| async_tree_cpu_io_mixed_tg | 761 ms                                                 | 4.58 sec: 6.01x slower                                                       |
| async_tree_none            | 528 ms                                                 | 3.42 sec: 6.48x slower                                                       |
| async_tree_memoization     | 639 ms                                                 | 4.43 sec: 6.93x slower                                                       |
| async_tree_memoization_tg  | 626 ms                                                 | 4.73 sec: 7.55x slower                                                       |
| async_tree_none_tg         | 491 ms                                                 | 3.78 sec: 7.70x slower                                                       |
| async_tree_io              | 1.29 sec                                               | 13.3 sec: 10.32x slower                                                      |
| async_tree_io_tg           | 1.29 sec                                               | 14.3 sec: 11.03x slower                                                      |
| Geometric mean             | (ref)                                                  | 7.49x slower                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240319-linux-x86_64-faster%2dcpython-incremental_gc_3-3.13.0a5+-f4f04d6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| nbody          | 96.0 ms                                                | 91.7 ms: 1.05x faster                                                        |
| pidigits       | 194 ms                                                 | 190 ms: 1.02x faster                                                         |
| float          | 78.9 ms                                                | 144 ms: 1.82x slower                                                         |
| Geometric mean | (ref)                                                  | 1.19x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240319-linux-x86_64-faster%2dcpython-incremental_gc_3-3.13.0a5+-f4f04d6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 141 ms                                                 | 134 ms: 1.05x faster                                                         |
| regex_effbot   | 3.51 ms                                                | 3.69 ms: 1.05x slower                                                        |
| regex_dna      | 205 ms                                                 | 228 ms: 1.12x slower                                                         |
| regex_v8       | 22.9 ms                                                | 26.6 ms: 1.16x slower                                                        |
| Geometric mean | (ref)                                                  | 1.07x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240319-linux-x86_64-faster%2dcpython-incremental_gc_3-3.13.0a5+-f4f04d6 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 13.3 ms                                                | 10.6 ms: 1.26x faster                                                        |
| unpickle_pure_python | 242 us                                                 | 216 us: 1.12x faster                                                         |
| pickle_pure_python   | 320 us                                                 | 297 us: 1.08x faster                                                         |
| tomli_loads          | 2.30 sec                                               | 2.20 sec: 1.04x faster                                                       |
| json_loads           | 29.2 us                                                | 28.1 us: 1.04x faster                                                        |
| unpickle_list        | 5.21 us                                                | 5.11 us: 1.02x faster                                                        |
| pickle_dict          | 34.6 us                                                | 35.0 us: 1.01x slower                                                        |
| pickle               | 11.0 us                                                | 11.9 us: 1.08x slower                                                        |
| unpickle             | 13.8 us                                                | 15.4 us: 1.11x slower                                                        |
| pickle_list          | 4.59 us                                                | 5.33 us: 1.16x slower                                                        |
| xml_etree_process    | 56.9 ms                                                | 67.9 ms: 1.19x slower                                                        |
| xml_etree_generate   | 81.1 ms                                                | 98.4 ms: 1.21x slower                                                        |
| xml_etree_parse      | 164 ms                                                 | 217 ms: 1.32x slower                                                         |
| xml_etree_iterparse  | 108 ms                                                 | 165 ms: 1.53x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.07x slower                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240319-linux-x86_64-faster%2dcpython-incremental_gc_3-3.13.0a5+-f4f04d6 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.56 ms                                                | 10.5 ms: 1.23x slower                                                        |
| python_startup_no_site | 6.01 ms                                                | 8.85 ms: 1.47x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.35x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240319-linux-x86_64-faster%2dcpython-incremental_gc_3-3.13.0a5+-f4f04d6 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 33.5 ms                                                | 34.5 ms: 1.03x slower                                                        |
| genshi_text     | 22.5 ms                                                | 23.2 ms: 1.03x slower                                                        |
| mako            | 10.7 ms                                                | 11.1 ms: 1.04x slower                                                        |
| genshi_xml      | 53.4 ms                                                | 59.8 ms: 1.12x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240319-linux-x86_64-faster%2dcpython-incremental_gc_3-3.13.0a5+-f4f04d6 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols   | 520 us                                                 | 114 us: 4.56x faster                                                         |
| generators                 | 74.9 ms                                                | 29.2 ms: 2.57x faster                                                        |
| asyncio_tcp                | 875 ms                                                 | 502 ms: 1.74x faster                                                         |
| asyncio_tcp_ssl            | 3.11 sec                                               | 1.84 sec: 1.69x faster                                                       |
| comprehensions             | 23.6 us                                                | 16.1 us: 1.46x faster                                                        |
| json_dumps                 | 13.3 ms                                                | 10.6 ms: 1.26x faster                                                        |
| coroutines                 | 27.0 ms                                                | 22.8 ms: 1.19x faster                                                        |
| chaos                      | 71.9 ms                                                | 60.8 ms: 1.18x faster                                                        |
| richards_super             | 61.9 ms                                                | 52.3 ms: 1.18x faster                                                        |
| raytrace                   | 309 ms                                                 | 263 ms: 1.17x faster                                                         |
| logging_silent             | 111 ns                                                 | 97.5 ns: 1.14x faster                                                        |
| hexiom                     | 6.89 ms                                                | 6.10 ms: 1.13x faster                                                        |
| gc_traversal               | 4.01 ms                                                | 3.56 ms: 1.13x faster                                                        |
| unpickle_pure_python       | 242 us                                                 | 216 us: 1.12x faster                                                         |
| sympy_sum                  | 169 ms                                                 | 153 ms: 1.10x faster                                                         |
| richards                   | 49.8 ms                                                | 45.1 ms: 1.10x faster                                                        |
| deltablue                  | 3.92 ms                                                | 3.57 ms: 1.10x faster                                                        |
| deepcopy_memo              | 40.2 us                                                | 36.8 us: 1.09x faster                                                        |
| nqueens                    | 87.9 ms                                                | 80.8 ms: 1.09x faster                                                        |
| sympy_str                  | 297 ms                                                 | 274 ms: 1.08x faster                                                         |
| sympy_integrate            | 21.5 ms                                                | 19.9 ms: 1.08x faster                                                        |
| pickle_pure_python         | 320 us                                                 | 297 us: 1.08x faster                                                         |
| crypto_pyaes               | 76.7 ms                                                | 71.9 ms: 1.07x faster                                                        |
| logging_simple             | 6.22 us                                                | 5.85 us: 1.06x faster                                                        |
| deepcopy                   | 365 us                                                 | 345 us: 1.06x faster                                                         |
| go                         | 149 ms                                                 | 140 ms: 1.06x faster                                                         |
| mdp                        | 2.77 sec                                               | 2.62 sec: 1.06x faster                                                       |
| scimark_monte_carlo        | 70.7 ms                                                | 66.9 ms: 1.06x faster                                                        |
| regex_compile              | 141 ms                                                 | 134 ms: 1.05x faster                                                         |
| sympy_expand               | 484 ms                                                 | 463 ms: 1.05x faster                                                         |
| nbody                      | 96.0 ms                                                | 91.7 ms: 1.05x faster                                                        |
| logging_format             | 6.81 us                                                | 6.51 us: 1.05x faster                                                        |
| sqlglot_normalize          | 113 ms                                                 | 108 ms: 1.04x faster                                                         |
| tomli_loads                | 2.30 sec                                               | 2.20 sec: 1.04x faster                                                       |
| json_loads                 | 29.2 us                                                | 28.1 us: 1.04x faster                                                        |
| pprint_pformat             | 1.55 sec                                               | 1.50 sec: 1.04x faster                                                       |
| deepcopy_reduce            | 3.22 us                                                | 3.11 us: 1.03x faster                                                        |
| scimark_lu                 | 116 ms                                                 | 113 ms: 1.03x faster                                                         |
| pidigits                   | 194 ms                                                 | 190 ms: 1.02x faster                                                         |
| unpickle_list              | 5.21 us                                                | 5.11 us: 1.02x faster                                                        |
| pprint_safe_repr           | 747 ms                                                 | 734 ms: 1.02x faster                                                         |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.95 ms: 1.02x faster                                                        |
| scimark_sor                | 121 ms                                                 | 120 ms: 1.01x faster                                                         |
| bench_thread_pool          | 834 us                                                 | 824 us: 1.01x faster                                                         |
| bench_mp_pool              | 24.0 ms                                                | 23.7 ms: 1.01x faster                                                        |
| meteor_contest             | 109 ms                                                 | 110 ms: 1.01x slower                                                         |
| tornado_http               | 98.1 ms                                                | 99.0 ms: 1.01x slower                                                        |
| pickle_dict                | 34.6 us                                                | 35.0 us: 1.01x slower                                                        |
| sqlglot_optimize           | 55.3 ms                                                | 56.1 ms: 1.01x slower                                                        |
| thrift                     | 784 us                                                 | 800 us: 1.02x slower                                                         |
| django_template            | 33.5 ms                                                | 34.5 ms: 1.03x slower                                                        |
| genshi_text                | 22.5 ms                                                | 23.2 ms: 1.03x slower                                                        |
| asyncio_websockets         | 550 ms                                                 | 568 ms: 1.03x slower                                                         |
| chameleon                  | 6.70 ms                                                | 6.94 ms: 1.04x slower                                                        |
| create_gc_cycles           | 1.43 ms                                                | 1.49 ms: 1.04x slower                                                        |
| sqlglot_parse              | 1.43 ms                                                | 1.49 ms: 1.04x slower                                                        |
| mako                       | 10.7 ms                                                | 11.1 ms: 1.04x slower                                                        |
| regex_effbot               | 3.51 ms                                                | 3.69 ms: 1.05x slower                                                        |
| dulwich_log                | 64.6 ms                                                | 68.1 ms: 1.05x slower                                                        |
| scimark_fft                | 345 ms                                                 | 366 ms: 1.06x slower                                                         |
| pyflate                    | 434 ms                                                 | 461 ms: 1.06x slower                                                         |
| sqlglot_transpile          | 1.75 ms                                                | 1.86 ms: 1.06x slower                                                        |
| pickle                     | 11.0 us                                                | 11.9 us: 1.08x slower                                                        |
| aiohttp                    | 1.12 ms                                                | 1.23 ms: 1.11x slower                                                        |
| gunicorn                   | 1.20 ms                                                | 1.33 ms: 1.11x slower                                                        |
| unpickle                   | 13.8 us                                                | 15.4 us: 1.11x slower                                                        |
| 2to3                       | 264 ms                                                 | 294 ms: 1.11x slower                                                         |
| regex_dna                  | 205 ms                                                 | 228 ms: 1.12x slower                                                         |
| genshi_xml                 | 53.4 ms                                                | 59.8 ms: 1.12x slower                                                        |
| sqlite_synth               | 2.57 us                                                | 2.93 us: 1.14x slower                                                        |
| html5lib                   | 64.8 ms                                                | 75.0 ms: 1.16x slower                                                        |
| pickle_list                | 4.59 us                                                | 5.33 us: 1.16x slower                                                        |
| regex_v8                   | 22.9 ms                                                | 26.6 ms: 1.16x slower                                                        |
| mypy2                      | 686 ms                                                 | 806 ms: 1.18x slower                                                         |
| xml_etree_process          | 56.9 ms                                                | 67.9 ms: 1.19x slower                                                        |
| xml_etree_generate         | 81.1 ms                                                | 98.4 ms: 1.21x slower                                                        |
| coverage                   | 78.8 ms                                                | 96.1 ms: 1.22x slower                                                        |
| python_startup             | 8.56 ms                                                | 10.5 ms: 1.23x slower                                                        |
| telco                      | 6.86 ms                                                | 8.63 ms: 1.26x slower                                                        |
| pycparser                  | 1.19 sec                                               | 1.52 sec: 1.28x slower                                                       |
| unpack_sequence            | 43.5 ns                                                | 56.9 ns: 1.31x slower                                                        |
| xml_etree_parse            | 164 ms                                                 | 217 ms: 1.32x slower                                                         |
| async_generators           | 374 ms                                                 | 536 ms: 1.44x slower                                                         |
| python_startup_no_site     | 6.01 ms                                                | 8.85 ms: 1.47x slower                                                        |
| xml_etree_iterparse        | 108 ms                                                 | 165 ms: 1.53x slower                                                         |
| docutils                   | 2.66 sec                                               | 4.66 sec: 1.75x slower                                                       |
| float                      | 78.9 ms                                                | 144 ms: 1.82x slower                                                         |
| dask                       | 365 ms                                                 | 756 ms: 2.07x slower                                                         |
| pylint                     | 476 ms                                                 | 1.00 sec: 2.10x slower                                                       |
| async_tree_cpu_io_mixed    | 749 ms                                                 | 4.17 sec: 5.57x slower                                                       |
| async_tree_cpu_io_mixed_tg | 761 ms                                                 | 4.58 sec: 6.01x slower                                                       |
| async_tree_none            | 528 ms                                                 | 3.42 sec: 6.48x slower                                                       |
| async_tree_memoization     | 639 ms                                                 | 4.43 sec: 6.93x slower                                                       |
| async_tree_memoization_tg  | 626 ms                                                 | 4.73 sec: 7.55x slower                                                       |
| async_tree_none_tg         | 491 ms                                                 | 3.78 sec: 7.70x slower                                                       |
| async_tree_io              | 1.29 sec                                               | 13.3 sec: 10.32x slower                                                      |
| async_tree_io_tg           | 1.29 sec                                               | 14.3 sec: 11.03x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.18x slower                                                                 |

Benchmark hidden because not significant (5): djangocms, json, fannkuch, pathlib, spectral_norm
Ignored benchmarks (3) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 95.06% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 0.99x