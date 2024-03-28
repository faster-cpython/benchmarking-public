# Results vs. 3.11.0

- fork: faster-cpython
- ref: no_thresholds
- machine: linux-x86_64
- commit hash: a4985b2
- commit date: 2024-03-28
- overall geometric mean: 1.01x faster
- HPT reliability: 87.83%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-a4985b2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 264 ms                                                 | 281 ms: 1.06x slower                                                      |
| chameleon      | 6.70 ms                                                | 7.06 ms: 1.05x slower                                                     |
| docutils       | 2.66 sec                                               | 2.94 sec: 1.10x slower                                                    |
| html5lib       | 64.8 ms                                                | 66.2 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                  | 1.05x slower                                                              |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-a4985b2 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none            | 528 ms                                                 | 355 ms: 1.49x faster                                                      |
| async_tree_none_tg         | 491 ms                                                 | 347 ms: 1.42x faster                                                      |
| async_tree_memoization     | 639 ms                                                 | 455 ms: 1.41x faster                                                      |
| async_tree_io_tg           | 1.29 sec                                               | 922 ms: 1.40x faster                                                      |
| async_tree_memoization_tg  | 626 ms                                                 | 448 ms: 1.40x faster                                                      |
| async_tree_io              | 1.29 sec                                               | 938 ms: 1.37x faster                                                      |
| async_tree_cpu_io_mixed_tg | 761 ms                                                 | 596 ms: 1.28x faster                                                      |
| async_tree_cpu_io_mixed    | 749 ms                                                 | 612 ms: 1.22x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.37x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-a4985b2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 96.0 ms                                                | 90.6 ms: 1.06x faster                                                     |
| pidigits       | 194 ms                                                 | 190 ms: 1.02x faster                                                      |
| float          | 78.9 ms                                                | 79.5 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-a4985b2 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 141 ms                                                 | 151 ms: 1.07x slower                                                      |
| regex_effbot   | 3.51 ms                                                | 3.81 ms: 1.09x slower                                                     |
| regex_dna      | 205 ms                                                 | 231 ms: 1.13x slower                                                      |
| regex_v8       | 22.9 ms                                                | 26.2 ms: 1.15x slower                                                     |
| Geometric mean | (ref)                                                  | 1.11x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-a4985b2 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 13.3 ms                                                | 10.6 ms: 1.26x faster                                                     |
| tomli_loads          | 2.30 sec                                               | 2.15 sec: 1.07x faster                                                    |
| pickle_pure_python   | 320 us                                                 | 306 us: 1.04x faster                                                      |
| unpickle_list        | 5.21 us                                                | 5.04 us: 1.04x faster                                                     |
| json_loads           | 29.2 us                                                | 28.3 us: 1.03x faster                                                     |
| pickle_dict          | 34.6 us                                                | 34.0 us: 1.02x faster                                                     |
| xml_etree_parse      | 164 ms                                                 | 162 ms: 1.01x faster                                                      |
| xml_etree_iterparse  | 108 ms                                                 | 113 ms: 1.05x slower                                                      |
| pickle_list          | 4.59 us                                                | 4.94 us: 1.08x slower                                                     |
| pickle               | 11.0 us                                                | 11.9 us: 1.08x slower                                                     |
| xml_etree_process    | 56.9 ms                                                | 62.8 ms: 1.10x slower                                                     |
| unpickle_pure_python | 242 us                                                 | 267 us: 1.11x slower                                                      |
| xml_etree_generate   | 81.1 ms                                                | 91.9 ms: 1.13x slower                                                     |
| unpickle             | 13.8 us                                                | 16.7 us: 1.21x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-a4985b2 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 8.56 ms                                                | 11.2 ms: 1.31x slower                                                     |
| python_startup_no_site | 6.01 ms                                                | 9.62 ms: 1.60x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.44x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-a4985b2 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_xml      | 53.4 ms                                                | 57.0 ms: 1.07x slower                                                     |
| django_template | 33.5 ms                                                | 37.0 ms: 1.10x slower                                                     |
| genshi_text     | 22.5 ms                                                | 25.9 ms: 1.15x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.08x slower                                                              |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                  | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-a4985b2 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols   | 520 us                                                 | 116 us: 4.50x faster                                                      |
| generators                 | 74.9 ms                                                | 29.8 ms: 2.51x faster                                                     |
| asyncio_tcp                | 875 ms                                                 | 512 ms: 1.71x faster                                                      |
| asyncio_tcp_ssl            | 3.11 sec                                               | 1.85 sec: 1.68x faster                                                    |
| async_tree_none            | 528 ms                                                 | 355 ms: 1.49x faster                                                      |
| async_tree_none_tg         | 491 ms                                                 | 347 ms: 1.42x faster                                                      |
| async_tree_memoization     | 639 ms                                                 | 455 ms: 1.41x faster                                                      |
| async_tree_io_tg           | 1.29 sec                                               | 922 ms: 1.40x faster                                                      |
| async_tree_memoization_tg  | 626 ms                                                 | 448 ms: 1.40x faster                                                      |
| pylint                     | 476 ms                                                 | 341 ms: 1.40x faster                                                      |
| async_tree_io              | 1.29 sec                                               | 938 ms: 1.37x faster                                                      |
| async_tree_cpu_io_mixed_tg | 761 ms                                                 | 596 ms: 1.28x faster                                                      |
| json_dumps                 | 13.3 ms                                                | 10.6 ms: 1.26x faster                                                     |
| async_tree_cpu_io_mixed    | 749 ms                                                 | 612 ms: 1.22x faster                                                      |
| comprehensions             | 23.6 us                                                | 19.5 us: 1.21x faster                                                     |
| coroutines                 | 27.0 ms                                                | 23.1 ms: 1.17x faster                                                     |
| chaos                      | 71.9 ms                                                | 65.3 ms: 1.10x faster                                                     |
| tomli_loads                | 2.30 sec                                               | 2.15 sec: 1.07x faster                                                    |
| logging_silent             | 111 ns                                                 | 104 ns: 1.07x faster                                                      |
| gc_traversal               | 4.01 ms                                                | 3.77 ms: 1.06x faster                                                     |
| nbody                      | 96.0 ms                                                | 90.6 ms: 1.06x faster                                                     |
| richards_super             | 61.9 ms                                                | 58.6 ms: 1.06x faster                                                     |
| sqlglot_parse              | 1.43 ms                                                | 1.36 ms: 1.05x faster                                                     |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.79 ms: 1.05x faster                                                     |
| pickle_pure_python         | 320 us                                                 | 306 us: 1.04x faster                                                      |
| sqlglot_transpile          | 1.75 ms                                                | 1.69 ms: 1.04x faster                                                     |
| unpickle_list              | 5.21 us                                                | 5.04 us: 1.04x faster                                                     |
| djangocms                  | 33.5 us                                                | 32.4 us: 1.03x faster                                                     |
| logging_simple             | 6.22 us                                                | 6.01 us: 1.03x faster                                                     |
| json_loads                 | 29.2 us                                                | 28.3 us: 1.03x faster                                                     |
| crypto_pyaes               | 76.7 ms                                                | 74.9 ms: 1.02x faster                                                     |
| pidigits                   | 194 ms                                                 | 190 ms: 1.02x faster                                                      |
| raytrace                   | 309 ms                                                 | 302 ms: 1.02x faster                                                      |
| pickle_dict                | 34.6 us                                                | 34.0 us: 1.02x faster                                                     |
| xml_etree_parse            | 164 ms                                                 | 162 ms: 1.01x faster                                                      |
| fannkuch                   | 405 ms                                                 | 400 ms: 1.01x faster                                                      |
| logging_format             | 6.81 us                                                | 6.73 us: 1.01x faster                                                     |
| sympy_str                  | 297 ms                                                 | 295 ms: 1.01x faster                                                      |
| scimark_fft                | 345 ms                                                 | 343 ms: 1.01x faster                                                      |
| sympy_sum                  | 169 ms                                                 | 168 ms: 1.01x faster                                                      |
| float                      | 78.9 ms                                                | 79.5 ms: 1.01x slower                                                     |
| sqlglot_normalize          | 113 ms                                                 | 115 ms: 1.02x slower                                                      |
| pprint_pformat             | 1.55 sec                                               | 1.58 sec: 1.02x slower                                                    |
| deepcopy_reduce            | 3.22 us                                                | 3.28 us: 1.02x slower                                                     |
| html5lib                   | 64.8 ms                                                | 66.2 ms: 1.02x slower                                                     |
| deepcopy                   | 365 us                                                 | 375 us: 1.03x slower                                                      |
| sympy_expand               | 484 ms                                                 | 498 ms: 1.03x slower                                                      |
| meteor_contest             | 109 ms                                                 | 112 ms: 1.03x slower                                                      |
| dask                       | 365 ms                                                 | 376 ms: 1.03x slower                                                      |
| pprint_safe_repr           | 747 ms                                                 | 772 ms: 1.03x slower                                                      |
| asyncio_websockets         | 550 ms                                                 | 570 ms: 1.04x slower                                                      |
| json                       | 5.24 ms                                                | 5.43 ms: 1.04x slower                                                     |
| pathlib                    | 18.5 ms                                                | 19.2 ms: 1.04x slower                                                     |
| sympy_integrate            | 21.5 ms                                                | 22.4 ms: 1.04x slower                                                     |
| thrift                     | 784 us                                                 | 819 us: 1.04x slower                                                      |
| xml_etree_iterparse        | 108 ms                                                 | 113 ms: 1.05x slower                                                      |
| chameleon                  | 6.70 ms                                                | 7.06 ms: 1.05x slower                                                     |
| spectral_norm              | 108 ms                                                 | 114 ms: 1.05x slower                                                      |
| deltablue                  | 3.92 ms                                                | 4.14 ms: 1.06x slower                                                     |
| scimark_monte_carlo        | 70.7 ms                                                | 74.8 ms: 1.06x slower                                                     |
| 2to3                       | 264 ms                                                 | 281 ms: 1.06x slower                                                      |
| richards                   | 49.8 ms                                                | 52.9 ms: 1.06x slower                                                     |
| pycparser                  | 1.19 sec                                               | 1.26 sec: 1.06x slower                                                    |
| bench_thread_pool          | 834 us                                                 | 890 us: 1.07x slower                                                      |
| genshi_xml                 | 53.4 ms                                                | 57.0 ms: 1.07x slower                                                     |
| regex_compile              | 141 ms                                                 | 151 ms: 1.07x slower                                                      |
| sqlglot_optimize           | 55.3 ms                                                | 59.4 ms: 1.07x slower                                                     |
| pickle_list                | 4.59 us                                                | 4.94 us: 1.08x slower                                                     |
| pickle                     | 11.0 us                                                | 11.9 us: 1.08x slower                                                     |
| regex_effbot               | 3.51 ms                                                | 3.81 ms: 1.09x slower                                                     |
| aiohttp                    | 1.12 ms                                                | 1.21 ms: 1.09x slower                                                     |
| gunicorn                   | 1.20 ms                                                | 1.30 ms: 1.09x slower                                                     |
| scimark_sor                | 121 ms                                                 | 132 ms: 1.09x slower                                                      |
| docutils                   | 2.66 sec                                               | 2.94 sec: 1.10x slower                                                    |
| django_template            | 33.5 ms                                                | 37.0 ms: 1.10x slower                                                     |
| xml_etree_process          | 56.9 ms                                                | 62.8 ms: 1.10x slower                                                     |
| unpickle_pure_python       | 242 us                                                 | 267 us: 1.11x slower                                                      |
| dulwich_log                | 64.6 ms                                                | 71.5 ms: 1.11x slower                                                     |
| sqlite_synth               | 2.57 us                                                | 2.87 us: 1.11x slower                                                     |
| deepcopy_memo              | 40.2 us                                                | 44.9 us: 1.12x slower                                                     |
| pyflate                    | 434 ms                                                 | 488 ms: 1.12x slower                                                      |
| regex_dna                  | 205 ms                                                 | 231 ms: 1.13x slower                                                      |
| xml_etree_generate         | 81.1 ms                                                | 91.9 ms: 1.13x slower                                                     |
| scimark_lu                 | 116 ms                                                 | 132 ms: 1.14x slower                                                      |
| regex_v8                   | 22.9 ms                                                | 26.2 ms: 1.15x slower                                                     |
| genshi_text                | 22.5 ms                                                | 25.9 ms: 1.15x slower                                                     |
| mypy2                      | 686 ms                                                 | 798 ms: 1.16x slower                                                      |
| go                         | 149 ms                                                 | 173 ms: 1.17x slower                                                      |
| hexiom                     | 6.89 ms                                                | 8.09 ms: 1.17x slower                                                     |
| create_gc_cycles           | 1.43 ms                                                | 1.70 ms: 1.19x slower                                                     |
| nqueens                    | 87.9 ms                                                | 104 ms: 1.19x slower                                                      |
| unpickle                   | 13.8 us                                                | 16.7 us: 1.21x slower                                                     |
| coverage                   | 78.8 ms                                                | 97.5 ms: 1.24x slower                                                     |
| telco                      | 6.86 ms                                                | 8.68 ms: 1.27x slower                                                     |
| python_startup             | 8.56 ms                                                | 11.2 ms: 1.31x slower                                                     |
| async_generators           | 374 ms                                                 | 493 ms: 1.32x slower                                                      |
| python_startup_no_site     | 6.01 ms                                                | 9.62 ms: 1.60x slower                                                     |
| unpack_sequence            | 43.5 ns                                                | 86.9 ns: 2.00x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (4): tornado_http, mdp, bench_mp_pool, mako
Ignored benchmarks (3) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 87.83% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 1.11x