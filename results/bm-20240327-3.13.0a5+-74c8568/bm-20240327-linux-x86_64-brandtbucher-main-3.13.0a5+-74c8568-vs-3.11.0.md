# Results vs. 3.11.0

- fork: brandtbucher
- ref: main
- machine: linux-x86_64
- commit hash: 74c8568
- commit date: 2024-03-27
- overall geometric mean: 1.07x faster
- HPT reliability: 99.91%
- HPT 99th percentile: 1.01x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5+-74c8568 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| 2to3           | 264 ms                                                 | 267 ms: 1.01x slower                                         |
| chameleon      | 6.70 ms                                                | 6.82 ms: 1.02x slower                                        |
| docutils       | 2.66 sec                                               | 2.77 sec: 1.04x slower                                       |
| html5lib       | 64.8 ms                                                | 67.9 ms: 1.05x slower                                        |
| tornado_http   | 98.1 ms                                                | 94.8 ms: 1.03x faster                                        |
| Geometric mean | (ref)                                                  | 1.02x slower                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5+-74c8568 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| async_tree_none_tg         | 491 ms                                                 | 338 ms: 1.45x faster                                         |
| async_tree_memoization     | 639 ms                                                 | 440 ms: 1.45x faster                                         |
| async_tree_io_tg           | 1.29 sec                                               | 914 ms: 1.42x faster                                         |
| async_tree_memoization_tg  | 626 ms                                                 | 445 ms: 1.41x faster                                         |
| async_tree_io              | 1.29 sec                                               | 915 ms: 1.41x faster                                         |
| async_tree_none            | 528 ms                                                 | 381 ms: 1.39x faster                                         |
| async_tree_cpu_io_mixed_tg | 761 ms                                                 | 577 ms: 1.32x faster                                         |
| async_tree_cpu_io_mixed    | 749 ms                                                 | 592 ms: 1.27x faster                                         |
| Geometric mean             | (ref)                                                  | 1.39x faster                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5+-74c8568 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 96.0 ms                                                | 88.3 ms: 1.09x faster                                        |
| float          | 78.9 ms                                                | 76.6 ms: 1.03x faster                                        |
| pidigits       | 194 ms                                                 | 189 ms: 1.03x faster                                         |
| Geometric mean | (ref)                                                  | 1.05x faster                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5+-74c8568 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| regex_compile  | 141 ms                                                 | 133 ms: 1.06x faster                                         |
| regex_effbot   | 3.51 ms                                                | 3.81 ms: 1.09x slower                                        |
| regex_dna      | 205 ms                                                 | 230 ms: 1.13x slower                                         |
| regex_v8       | 22.9 ms                                                | 26.0 ms: 1.14x slower                                        |
| Geometric mean | (ref)                                                  | 1.07x slower                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5+-74c8568 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| json_dumps           | 13.3 ms                                                | 10.4 ms: 1.28x faster                                        |
| unpickle_pure_python | 242 us                                                 | 215 us: 1.13x faster                                         |
| pickle_pure_python   | 320 us                                                 | 297 us: 1.08x faster                                         |
| tomli_loads          | 2.30 sec                                               | 2.20 sec: 1.05x faster                                       |
| json_loads           | 29.2 us                                                | 28.6 us: 1.02x faster                                        |
| xml_etree_parse      | 164 ms                                                 | 161 ms: 1.02x faster                                         |
| xml_etree_iterparse  | 108 ms                                                 | 106 ms: 1.02x faster                                         |
| unpickle_list        | 5.21 us                                                | 5.26 us: 1.01x slower                                        |
| pickle_dict          | 34.6 us                                                | 35.6 us: 1.03x slower                                        |
| xml_etree_process    | 56.9 ms                                                | 59.8 ms: 1.05x slower                                        |
| xml_etree_generate   | 81.1 ms                                                | 85.8 ms: 1.06x slower                                        |
| pickle               | 11.0 us                                                | 12.0 us: 1.09x slower                                        |
| pickle_list          | 4.59 us                                                | 5.40 us: 1.18x slower                                        |
| unpickle             | 13.8 us                                                | 16.7 us: 1.20x slower                                        |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5+-74c8568 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 8.56 ms                                                | 10.6 ms: 1.24x slower                                        |
| python_startup_no_site | 6.01 ms                                                | 9.00 ms: 1.50x slower                                        |
| Geometric mean         | (ref)                                                  | 1.36x slower                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5+-74c8568 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_xml      | 53.4 ms                                                | 50.8 ms: 1.05x faster                                        |
| mako            | 10.7 ms                                                | 10.7 ms: 1.01x slower                                        |
| django_template | 33.5 ms                                                | 34.8 ms: 1.04x slower                                        |
| genshi_text     | 22.5 ms                                                | 24.0 ms: 1.06x slower                                        |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240327-linux-x86_64-brandtbucher-main-3.13.0a5+-74c8568 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------:|
| typing_runtime_protocols   | 520 us                                                 | 111 us: 4.68x faster                                         |
| generators                 | 74.9 ms                                                | 29.5 ms: 2.54x faster                                        |
| asyncio_tcp                | 875 ms                                                 | 501 ms: 1.75x faster                                         |
| asyncio_tcp_ssl            | 3.11 sec                                               | 1.84 sec: 1.69x faster                                       |
| pylint                     | 476 ms                                                 | 318 ms: 1.50x faster                                         |
| async_tree_none_tg         | 491 ms                                                 | 338 ms: 1.45x faster                                         |
| async_tree_memoization     | 639 ms                                                 | 440 ms: 1.45x faster                                         |
| comprehensions             | 23.6 us                                                | 16.5 us: 1.43x faster                                        |
| async_tree_io_tg           | 1.29 sec                                               | 914 ms: 1.42x faster                                         |
| async_tree_memoization_tg  | 626 ms                                                 | 445 ms: 1.41x faster                                         |
| async_tree_io              | 1.29 sec                                               | 915 ms: 1.41x faster                                         |
| async_tree_none            | 528 ms                                                 | 381 ms: 1.39x faster                                         |
| async_tree_cpu_io_mixed_tg | 761 ms                                                 | 577 ms: 1.32x faster                                         |
| json_dumps                 | 13.3 ms                                                | 10.4 ms: 1.28x faster                                        |
| async_tree_cpu_io_mixed    | 749 ms                                                 | 592 ms: 1.27x faster                                         |
| richards_super             | 61.9 ms                                                | 51.2 ms: 1.21x faster                                        |
| deltablue                  | 3.92 ms                                                | 3.26 ms: 1.20x faster                                        |
| chaos                      | 71.9 ms                                                | 59.7 ms: 1.20x faster                                        |
| coroutines                 | 27.0 ms                                                | 23.0 ms: 1.18x faster                                        |
| raytrace                   | 309 ms                                                 | 263 ms: 1.17x faster                                         |
| unpickle_pure_python       | 242 us                                                 | 215 us: 1.13x faster                                         |
| logging_silent             | 111 ns                                                 | 98.9 ns: 1.12x faster                                        |
| sqlglot_parse              | 1.43 ms                                                | 1.28 ms: 1.12x faster                                        |
| hexiom                     | 6.89 ms                                                | 6.19 ms: 1.11x faster                                        |
| sqlglot_transpile          | 1.75 ms                                                | 1.58 ms: 1.11x faster                                        |
| sympy_sum                  | 169 ms                                                 | 153 ms: 1.10x faster                                         |
| richards                   | 49.8 ms                                                | 45.4 ms: 1.10x faster                                        |
| sympy_str                  | 297 ms                                                 | 272 ms: 1.09x faster                                         |
| nqueens                    | 87.9 ms                                                | 80.5 ms: 1.09x faster                                        |
| nbody                      | 96.0 ms                                                | 88.3 ms: 1.09x faster                                        |
| deepcopy_memo              | 40.2 us                                                | 37.0 us: 1.08x faster                                        |
| pickle_pure_python         | 320 us                                                 | 297 us: 1.08x faster                                         |
| sympy_integrate            | 21.5 ms                                                | 20.0 ms: 1.07x faster                                        |
| scimark_monte_carlo        | 70.7 ms                                                | 66.0 ms: 1.07x faster                                        |
| regex_compile              | 141 ms                                                 | 133 ms: 1.06x faster                                         |
| go                         | 149 ms                                                 | 140 ms: 1.06x faster                                         |
| logging_simple             | 6.22 us                                                | 5.87 us: 1.06x faster                                        |
| djangocms                  | 33.5 us                                                | 31.7 us: 1.06x faster                                        |
| deepcopy                   | 365 us                                                 | 347 us: 1.05x faster                                         |
| genshi_xml                 | 53.4 ms                                                | 50.8 ms: 1.05x faster                                        |
| sympy_expand               | 484 ms                                                 | 461 ms: 1.05x faster                                         |
| crypto_pyaes               | 76.7 ms                                                | 73.1 ms: 1.05x faster                                        |
| tomli_loads                | 2.30 sec                                               | 2.20 sec: 1.05x faster                                       |
| deepcopy_reduce            | 3.22 us                                                | 3.10 us: 1.04x faster                                        |
| sqlglot_normalize          | 113 ms                                                 | 109 ms: 1.04x faster                                         |
| fannkuch                   | 405 ms                                                 | 391 ms: 1.04x faster                                         |
| pprint_pformat             | 1.55 sec                                               | 1.50 sec: 1.03x faster                                       |
| logging_format             | 6.81 us                                                | 6.59 us: 1.03x faster                                        |
| tornado_http               | 98.1 ms                                                | 94.8 ms: 1.03x faster                                        |
| float                      | 78.9 ms                                                | 76.6 ms: 1.03x faster                                        |
| mdp                        | 2.77 sec                                               | 2.70 sec: 1.03x faster                                       |
| pidigits                   | 194 ms                                                 | 189 ms: 1.03x faster                                         |
| scimark_lu                 | 116 ms                                                 | 114 ms: 1.02x faster                                         |
| json_loads                 | 29.2 us                                                | 28.6 us: 1.02x faster                                        |
| xml_etree_parse            | 164 ms                                                 | 161 ms: 1.02x faster                                         |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.95 ms: 1.02x faster                                        |
| xml_etree_iterparse        | 108 ms                                                 | 106 ms: 1.02x faster                                         |
| bench_thread_pool          | 834 us                                                 | 825 us: 1.01x faster                                         |
| sqlglot_optimize           | 55.3 ms                                                | 54.7 ms: 1.01x faster                                        |
| pprint_safe_repr           | 747 ms                                                 | 740 ms: 1.01x faster                                         |
| bench_mp_pool              | 24.0 ms                                                | 23.8 ms: 1.01x faster                                        |
| scimark_sor                | 121 ms                                                 | 122 ms: 1.01x slower                                         |
| mako                       | 10.7 ms                                                | 10.7 ms: 1.01x slower                                        |
| unpickle_list              | 5.21 us                                                | 5.26 us: 1.01x slower                                        |
| 2to3                       | 264 ms                                                 | 267 ms: 1.01x slower                                         |
| spectral_norm              | 108 ms                                                 | 110 ms: 1.02x slower                                         |
| chameleon                  | 6.70 ms                                                | 6.82 ms: 1.02x slower                                        |
| unpack_sequence            | 43.5 ns                                                | 44.4 ns: 1.02x slower                                        |
| json                       | 5.24 ms                                                | 5.37 ms: 1.02x slower                                        |
| pickle_dict                | 34.6 us                                                | 35.6 us: 1.03x slower                                        |
| pycparser                  | 1.19 sec                                               | 1.22 sec: 1.03x slower                                       |
| asyncio_websockets         | 550 ms                                                 | 569 ms: 1.03x slower                                         |
| scimark_fft                | 345 ms                                                 | 358 ms: 1.04x slower                                         |
| django_template            | 33.5 ms                                                | 34.8 ms: 1.04x slower                                        |
| docutils                   | 2.66 sec                                               | 2.77 sec: 1.04x slower                                       |
| dulwich_log                | 64.6 ms                                                | 67.3 ms: 1.04x slower                                        |
| thrift                     | 784 us                                                 | 819 us: 1.04x slower                                         |
| html5lib                   | 64.8 ms                                                | 67.9 ms: 1.05x slower                                        |
| xml_etree_process          | 56.9 ms                                                | 59.8 ms: 1.05x slower                                        |
| aiohttp                    | 1.12 ms                                                | 1.18 ms: 1.06x slower                                        |
| xml_etree_generate         | 81.1 ms                                                | 85.8 ms: 1.06x slower                                        |
| genshi_text                | 22.5 ms                                                | 24.0 ms: 1.06x slower                                        |
| gunicorn                   | 1.20 ms                                                | 1.28 ms: 1.06x slower                                        |
| mypy2                      | 686 ms                                                 | 733 ms: 1.07x slower                                         |
| pyflate                    | 434 ms                                                 | 464 ms: 1.07x slower                                         |
| regex_effbot               | 3.51 ms                                                | 3.81 ms: 1.09x slower                                        |
| pickle                     | 11.0 us                                                | 12.0 us: 1.09x slower                                        |
| sqlite_synth               | 2.57 us                                                | 2.88 us: 1.12x slower                                        |
| regex_dna                  | 205 ms                                                 | 230 ms: 1.13x slower                                         |
| regex_v8                   | 22.9 ms                                                | 26.0 ms: 1.14x slower                                        |
| create_gc_cycles           | 1.43 ms                                                | 1.68 ms: 1.17x slower                                        |
| pickle_list                | 4.59 us                                                | 5.40 us: 1.18x slower                                        |
| async_generators           | 374 ms                                                 | 441 ms: 1.18x slower                                         |
| unpickle                   | 13.8 us                                                | 16.7 us: 1.20x slower                                        |
| coverage                   | 78.8 ms                                                | 97.2 ms: 1.23x slower                                        |
| python_startup             | 8.56 ms                                                | 10.6 ms: 1.24x slower                                        |
| telco                      | 6.86 ms                                                | 8.59 ms: 1.25x slower                                        |
| python_startup_no_site     | 6.01 ms                                                | 9.00 ms: 1.50x slower                                        |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                 |

Benchmark hidden because not significant (4): meteor_contest, gc_traversal, pathlib, dask
Ignored benchmarks (3) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 99.91% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x


# Memory

- memory change: 1.01x