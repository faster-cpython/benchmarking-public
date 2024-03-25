# Results vs. 3.11.0

- fork: faster-cpython
- ref: tier2_hot_cold_split
- machine: linux-x86_64
- commit hash: 37627d3
- commit date: 2024-03-25
- overall geometric mean: 1.04x faster
- HPT reliability: 67.57%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.10x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240325-linux-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-37627d3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 264 ms                                                 | 278 ms: 1.05x slower                                                             |
| chameleon      | 6.70 ms                                                | 7.14 ms: 1.07x slower                                                            |
| docutils       | 2.66 sec                                               | 2.88 sec: 1.08x slower                                                           |
| html5lib       | 64.8 ms                                                | 67.7 ms: 1.05x slower                                                            |
| tornado_http   | 98.1 ms                                                | 96.8 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                  | 1.05x slower                                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240325-linux-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-37627d3 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| async_tree_none            | 528 ms                                                 | 375 ms: 1.41x faster                                                             |
| async_tree_memoization_tg  | 626 ms                                                 | 447 ms: 1.40x faster                                                             |
| async_tree_io_tg           | 1.29 sec                                               | 929 ms: 1.39x faster                                                             |
| async_tree_io              | 1.29 sec                                               | 924 ms: 1.39x faster                                                             |
| async_tree_none_tg         | 491 ms                                                 | 354 ms: 1.39x faster                                                             |
| async_tree_memoization     | 639 ms                                                 | 462 ms: 1.38x faster                                                             |
| async_tree_cpu_io_mixed    | 749 ms                                                 | 595 ms: 1.26x faster                                                             |
| async_tree_cpu_io_mixed_tg | 761 ms                                                 | 611 ms: 1.25x faster                                                             |
| Geometric mean             | (ref)                                                  | 1.36x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240325-linux-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-37627d3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 96.0 ms                                                | 91.1 ms: 1.05x faster                                                            |
| float          | 78.9 ms                                                | 77.1 ms: 1.02x faster                                                            |
| pidigits       | 194 ms                                                 | 190 ms: 1.02x faster                                                             |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240325-linux-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-37627d3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.51 ms                                                | 3.53 ms: 1.01x slower                                                            |
| regex_compile  | 141 ms                                                 | 146 ms: 1.03x slower                                                             |
| regex_v8       | 22.9 ms                                                | 24.2 ms: 1.06x slower                                                            |
| regex_dna      | 205 ms                                                 | 218 ms: 1.07x slower                                                             |
| Geometric mean | (ref)                                                  | 1.04x slower                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240325-linux-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-37627d3 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 13.3 ms                                                | 10.5 ms: 1.27x faster                                                            |
| tomli_loads          | 2.30 sec                                               | 2.07 sec: 1.11x faster                                                           |
| pickle_pure_python   | 320 us                                                 | 310 us: 1.03x faster                                                             |
| unpickle_list        | 5.21 us                                                | 5.08 us: 1.03x faster                                                            |
| xml_etree_parse      | 164 ms                                                 | 160 ms: 1.03x faster                                                             |
| json_loads           | 29.2 us                                                | 28.6 us: 1.02x faster                                                            |
| unpickle_pure_python | 242 us                                                 | 240 us: 1.01x faster                                                             |
| xml_etree_iterparse  | 108 ms                                                 | 108 ms: 1.00x faster                                                             |
| pickle_dict          | 34.6 us                                                | 34.8 us: 1.01x slower                                                            |
| xml_etree_process    | 56.9 ms                                                | 60.4 ms: 1.06x slower                                                            |
| pickle               | 11.0 us                                                | 11.8 us: 1.07x slower                                                            |
| xml_etree_generate   | 81.1 ms                                                | 87.8 ms: 1.08x slower                                                            |
| unpickle             | 13.8 us                                                | 15.1 us: 1.09x slower                                                            |
| pickle_list          | 4.59 us                                                | 5.13 us: 1.12x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                                     |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240325-linux-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-37627d3 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 8.56 ms                                                | 11.0 ms: 1.29x slower                                                            |
| python_startup_no_site | 6.01 ms                                                | 9.44 ms: 1.57x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.42x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240325-linux-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-37627d3 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 53.4 ms                                                | 54.0 ms: 1.01x slower                                                            |
| mako            | 10.7 ms                                                | 10.8 ms: 1.01x slower                                                            |
| django_template | 33.5 ms                                                | 36.2 ms: 1.08x slower                                                            |
| genshi_text     | 22.5 ms                                                | 24.4 ms: 1.08x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240325-linux-x86_64-faster%2dcpython-tier2_hot_cold_split-3.13.0a5+-37627d3 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| typing_runtime_protocols   | 520 us                                                 | 112 us: 4.65x faster                                                             |
| generators                 | 74.9 ms                                                | 30.4 ms: 2.46x faster                                                            |
| asyncio_tcp                | 875 ms                                                 | 511 ms: 1.71x faster                                                             |
| asyncio_tcp_ssl            | 3.11 sec                                               | 1.86 sec: 1.67x faster                                                           |
| pylint                     | 476 ms                                                 | 336 ms: 1.42x faster                                                             |
| async_tree_none            | 528 ms                                                 | 375 ms: 1.41x faster                                                             |
| async_tree_memoization_tg  | 626 ms                                                 | 447 ms: 1.40x faster                                                             |
| async_tree_io_tg           | 1.29 sec                                               | 929 ms: 1.39x faster                                                             |
| async_tree_io              | 1.29 sec                                               | 924 ms: 1.39x faster                                                             |
| async_tree_none_tg         | 491 ms                                                 | 354 ms: 1.39x faster                                                             |
| async_tree_memoization     | 639 ms                                                 | 462 ms: 1.38x faster                                                             |
| comprehensions             | 23.6 us                                                | 18.2 us: 1.30x faster                                                            |
| json_dumps                 | 13.3 ms                                                | 10.5 ms: 1.27x faster                                                            |
| async_tree_cpu_io_mixed    | 749 ms                                                 | 595 ms: 1.26x faster                                                             |
| async_tree_cpu_io_mixed_tg | 761 ms                                                 | 611 ms: 1.25x faster                                                             |
| richards_super             | 61.9 ms                                                | 52.0 ms: 1.19x faster                                                            |
| coroutines                 | 27.0 ms                                                | 22.8 ms: 1.18x faster                                                            |
| chaos                      | 71.9 ms                                                | 63.1 ms: 1.14x faster                                                            |
| deltablue                  | 3.92 ms                                                | 3.46 ms: 1.13x faster                                                            |
| logging_silent             | 111 ns                                                 | 99.3 ns: 1.12x faster                                                            |
| tomli_loads                | 2.30 sec                                               | 2.07 sec: 1.11x faster                                                           |
| richards                   | 49.8 ms                                                | 45.7 ms: 1.09x faster                                                            |
| sqlglot_parse              | 1.43 ms                                                | 1.33 ms: 1.07x faster                                                            |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.69 ms: 1.07x faster                                                            |
| djangocms                  | 33.5 us                                                | 31.3 us: 1.07x faster                                                            |
| raytrace                   | 309 ms                                                 | 292 ms: 1.06x faster                                                             |
| nbody                      | 96.0 ms                                                | 91.1 ms: 1.05x faster                                                            |
| logging_simple             | 6.22 us                                                | 5.90 us: 1.05x faster                                                            |
| sqlglot_transpile          | 1.75 ms                                                | 1.66 ms: 1.05x faster                                                            |
| gc_traversal               | 4.01 ms                                                | 3.82 ms: 1.05x faster                                                            |
| logging_format             | 6.81 us                                                | 6.55 us: 1.04x faster                                                            |
| fannkuch                   | 405 ms                                                 | 391 ms: 1.04x faster                                                             |
| crypto_pyaes               | 76.7 ms                                                | 74.1 ms: 1.03x faster                                                            |
| pickle_pure_python         | 320 us                                                 | 310 us: 1.03x faster                                                             |
| unpickle_list              | 5.21 us                                                | 5.08 us: 1.03x faster                                                            |
| xml_etree_parse            | 164 ms                                                 | 160 ms: 1.03x faster                                                             |
| float                      | 78.9 ms                                                | 77.1 ms: 1.02x faster                                                            |
| deepcopy_memo              | 40.2 us                                                | 39.3 us: 1.02x faster                                                            |
| pidigits                   | 194 ms                                                 | 190 ms: 1.02x faster                                                             |
| json_loads                 | 29.2 us                                                | 28.6 us: 1.02x faster                                                            |
| sympy_str                  | 297 ms                                                 | 291 ms: 1.02x faster                                                             |
| sympy_sum                  | 169 ms                                                 | 165 ms: 1.02x faster                                                             |
| scimark_fft                | 345 ms                                                 | 339 ms: 1.02x faster                                                             |
| pprint_pformat             | 1.55 sec                                               | 1.53 sec: 1.01x faster                                                           |
| tornado_http               | 98.1 ms                                                | 96.8 ms: 1.01x faster                                                            |
| scimark_monte_carlo        | 70.7 ms                                                | 70.0 ms: 1.01x faster                                                            |
| deepcopy_reduce            | 3.22 us                                                | 3.18 us: 1.01x faster                                                            |
| unpickle_pure_python       | 242 us                                                 | 240 us: 1.01x faster                                                             |
| deepcopy                   | 365 us                                                 | 363 us: 1.01x faster                                                             |
| xml_etree_iterparse        | 108 ms                                                 | 108 ms: 1.00x faster                                                             |
| pickle_dict                | 34.6 us                                                | 34.8 us: 1.01x slower                                                            |
| sqlglot_normalize          | 113 ms                                                 | 113 ms: 1.01x slower                                                             |
| regex_effbot               | 3.51 ms                                                | 3.53 ms: 1.01x slower                                                            |
| mdp                        | 2.77 sec                                               | 2.80 sec: 1.01x slower                                                           |
| genshi_xml                 | 53.4 ms                                                | 54.0 ms: 1.01x slower                                                            |
| mako                       | 10.7 ms                                                | 10.8 ms: 1.01x slower                                                            |
| sympy_expand               | 484 ms                                                 | 491 ms: 1.01x slower                                                             |
| sympy_integrate            | 21.5 ms                                                | 21.8 ms: 1.02x slower                                                            |
| json                       | 5.24 ms                                                | 5.35 ms: 1.02x slower                                                            |
| meteor_contest             | 109 ms                                                 | 112 ms: 1.02x slower                                                             |
| create_gc_cycles           | 1.43 ms                                                | 1.47 ms: 1.03x slower                                                            |
| bench_thread_pool          | 834 us                                                 | 859 us: 1.03x slower                                                             |
| regex_compile              | 141 ms                                                 | 146 ms: 1.03x slower                                                             |
| pathlib                    | 18.5 ms                                                | 19.1 ms: 1.03x slower                                                            |
| nqueens                    | 87.9 ms                                                | 90.8 ms: 1.03x slower                                                            |
| dask                       | 365 ms                                                 | 378 ms: 1.03x slower                                                             |
| asyncio_websockets         | 550 ms                                                 | 570 ms: 1.04x slower                                                             |
| thrift                     | 784 us                                                 | 816 us: 1.04x slower                                                             |
| go                         | 149 ms                                                 | 155 ms: 1.04x slower                                                             |
| html5lib                   | 64.8 ms                                                | 67.7 ms: 1.05x slower                                                            |
| hexiom                     | 6.89 ms                                                | 7.22 ms: 1.05x slower                                                            |
| 2to3                       | 264 ms                                                 | 278 ms: 1.05x slower                                                             |
| sqlglot_optimize           | 55.3 ms                                                | 58.1 ms: 1.05x slower                                                            |
| regex_v8                   | 22.9 ms                                                | 24.2 ms: 1.06x slower                                                            |
| xml_etree_process          | 56.9 ms                                                | 60.4 ms: 1.06x slower                                                            |
| chameleon                  | 6.70 ms                                                | 7.14 ms: 1.07x slower                                                            |
| regex_dna                  | 205 ms                                                 | 218 ms: 1.07x slower                                                             |
| pickle                     | 11.0 us                                                | 11.8 us: 1.07x slower                                                            |
| spectral_norm              | 108 ms                                                 | 116 ms: 1.07x slower                                                             |
| django_template            | 33.5 ms                                                | 36.2 ms: 1.08x slower                                                            |
| docutils                   | 2.66 sec                                               | 2.88 sec: 1.08x slower                                                           |
| xml_etree_generate         | 81.1 ms                                                | 87.8 ms: 1.08x slower                                                            |
| genshi_text                | 22.5 ms                                                | 24.4 ms: 1.08x slower                                                            |
| unpickle                   | 13.8 us                                                | 15.1 us: 1.09x slower                                                            |
| gunicorn                   | 1.20 ms                                                | 1.31 ms: 1.10x slower                                                            |
| dulwich_log                | 64.6 ms                                                | 70.9 ms: 1.10x slower                                                            |
| aiohttp                    | 1.12 ms                                                | 1.22 ms: 1.10x slower                                                            |
| pyflate                    | 434 ms                                                 | 481 ms: 1.11x slower                                                             |
| sqlite_synth               | 2.57 us                                                | 2.87 us: 1.11x slower                                                            |
| pickle_list                | 4.59 us                                                | 5.13 us: 1.12x slower                                                            |
| scimark_sor                | 121 ms                                                 | 136 ms: 1.12x slower                                                             |
| scimark_lu                 | 116 ms                                                 | 132 ms: 1.13x slower                                                             |
| mypy2                      | 686 ms                                                 | 795 ms: 1.16x slower                                                             |
| coverage                   | 78.8 ms                                                | 96.7 ms: 1.23x slower                                                            |
| async_generators           | 374 ms                                                 | 460 ms: 1.23x slower                                                             |
| telco                      | 6.86 ms                                                | 8.51 ms: 1.24x slower                                                            |
| python_startup             | 8.56 ms                                                | 11.0 ms: 1.29x slower                                                            |
| python_startup_no_site     | 6.01 ms                                                | 9.44 ms: 1.57x slower                                                            |
| unpack_sequence            | 43.5 ns                                                | 92.1 ns: 2.12x slower                                                            |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                                     |

Benchmark hidden because not significant (3): pycparser, bench_mp_pool, pprint_safe_repr
Ignored benchmarks (3) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 67.57% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: 1.10x