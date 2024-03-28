# Results vs. 3.11.0

- fork: faster-cpython
- ref: no_thresholds
- machine: linux-x86_64
- commit hash: 174fc24
- commit date: 2024-03-28
- overall geometric mean: 1.01x faster
- HPT reliability: 92.79%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.11x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-174fc24 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 264 ms                                                 | 280 ms: 1.06x slower                                                      |
| chameleon      | 6.70 ms                                                | 7.16 ms: 1.07x slower                                                     |
| docutils       | 2.66 sec                                               | 2.93 sec: 1.10x slower                                                    |
| html5lib       | 64.8 ms                                                | 66.4 ms: 1.02x slower                                                     |
| tornado_http   | 98.1 ms                                                | 96.9 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.05x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-174fc24 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_none            | 528 ms                                                 | 360 ms: 1.47x faster                                                      |
| async_tree_io_tg           | 1.29 sec                                               | 909 ms: 1.42x faster                                                      |
| async_tree_none_tg         | 491 ms                                                 | 348 ms: 1.41x faster                                                      |
| async_tree_memoization_tg  | 626 ms                                                 | 448 ms: 1.40x faster                                                      |
| async_tree_memoization     | 639 ms                                                 | 458 ms: 1.39x faster                                                      |
| async_tree_io              | 1.29 sec                                               | 932 ms: 1.38x faster                                                      |
| async_tree_cpu_io_mixed_tg | 761 ms                                                 | 593 ms: 1.28x faster                                                      |
| async_tree_cpu_io_mixed    | 749 ms                                                 | 613 ms: 1.22x faster                                                      |
| Geometric mean             | (ref)                                                  | 1.37x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-174fc24 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 96.0 ms                                                | 92.7 ms: 1.04x faster                                                     |
| pidigits       | 194 ms                                                 | 189 ms: 1.03x faster                                                      |
| float          | 78.9 ms                                                | 79.6 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-174fc24 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 141 ms                                                 | 151 ms: 1.07x slower                                                      |
| regex_effbot   | 3.51 ms                                                | 3.78 ms: 1.08x slower                                                     |
| regex_v8       | 22.9 ms                                                | 25.7 ms: 1.12x slower                                                     |
| regex_dna      | 205 ms                                                 | 234 ms: 1.14x slower                                                      |
| Geometric mean | (ref)                                                  | 1.10x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-174fc24 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_dumps           | 13.3 ms                                                | 10.7 ms: 1.25x faster                                                     |
| tomli_loads          | 2.30 sec                                               | 2.13 sec: 1.08x faster                                                    |
| pickle_pure_python   | 320 us                                                 | 309 us: 1.03x faster                                                      |
| xml_etree_parse      | 164 ms                                                 | 160 ms: 1.03x faster                                                      |
| json_loads           | 29.2 us                                                | 28.6 us: 1.02x faster                                                     |
| unpickle_list        | 5.21 us                                                | 5.19 us: 1.01x faster                                                     |
| xml_etree_iterparse  | 108 ms                                                 | 112 ms: 1.04x slower                                                      |
| pickle_dict          | 34.6 us                                                | 36.5 us: 1.06x slower                                                     |
| xml_etree_process    | 56.9 ms                                                | 62.6 ms: 1.10x slower                                                     |
| pickle               | 11.0 us                                                | 12.1 us: 1.10x slower                                                     |
| unpickle_pure_python | 242 us                                                 | 268 us: 1.11x slower                                                      |
| pickle_list          | 4.59 us                                                | 5.12 us: 1.12x slower                                                     |
| xml_etree_generate   | 81.1 ms                                                | 92.9 ms: 1.15x slower                                                     |
| unpickle             | 13.8 us                                                | 17.1 us: 1.24x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.03x slower                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-174fc24 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 8.56 ms                                                | 11.1 ms: 1.29x slower                                                     |
| python_startup_no_site | 6.01 ms                                                | 9.54 ms: 1.59x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.43x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-174fc24 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 10.8 ms: 1.01x slower                                                     |
| genshi_xml      | 53.4 ms                                                | 57.3 ms: 1.07x slower                                                     |
| django_template | 33.5 ms                                                | 37.1 ms: 1.11x slower                                                     |
| genshi_text     | 22.5 ms                                                | 25.8 ms: 1.14x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.08x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240328-linux-x86_64-faster%2dcpython-no_thresholds-3.13.0a5+-174fc24 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| typing_runtime_protocols   | 520 us                                                 | 116 us: 4.47x faster                                                      |
| generators                 | 74.9 ms                                                | 29.9 ms: 2.50x faster                                                     |
| asyncio_tcp                | 875 ms                                                 | 511 ms: 1.71x faster                                                      |
| asyncio_tcp_ssl            | 3.11 sec                                               | 1.86 sec: 1.67x faster                                                    |
| async_tree_none            | 528 ms                                                 | 360 ms: 1.47x faster                                                      |
| async_tree_io_tg           | 1.29 sec                                               | 909 ms: 1.42x faster                                                      |
| async_tree_none_tg         | 491 ms                                                 | 348 ms: 1.41x faster                                                      |
| pylint                     | 476 ms                                                 | 340 ms: 1.40x faster                                                      |
| async_tree_memoization_tg  | 626 ms                                                 | 448 ms: 1.40x faster                                                      |
| async_tree_memoization     | 639 ms                                                 | 458 ms: 1.39x faster                                                      |
| async_tree_io              | 1.29 sec                                               | 932 ms: 1.38x faster                                                      |
| async_tree_cpu_io_mixed_tg | 761 ms                                                 | 593 ms: 1.28x faster                                                      |
| json_dumps                 | 13.3 ms                                                | 10.7 ms: 1.25x faster                                                     |
| async_tree_cpu_io_mixed    | 749 ms                                                 | 613 ms: 1.22x faster                                                      |
| comprehensions             | 23.6 us                                                | 19.4 us: 1.22x faster                                                     |
| coroutines                 | 27.0 ms                                                | 22.6 ms: 1.19x faster                                                     |
| chaos                      | 71.9 ms                                                | 65.4 ms: 1.10x faster                                                     |
| tomli_loads                | 2.30 sec                                               | 2.13 sec: 1.08x faster                                                    |
| gc_traversal               | 4.01 ms                                                | 3.78 ms: 1.06x faster                                                     |
| logging_silent             | 111 ns                                                 | 106 ns: 1.05x faster                                                      |
| sqlglot_parse              | 1.43 ms                                                | 1.37 ms: 1.04x faster                                                     |
| djangocms                  | 33.5 us                                                | 32.2 us: 1.04x faster                                                     |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.84 ms: 1.04x faster                                                     |
| richards_super             | 61.9 ms                                                | 59.7 ms: 1.04x faster                                                     |
| nbody                      | 96.0 ms                                                | 92.7 ms: 1.04x faster                                                     |
| pickle_pure_python         | 320 us                                                 | 309 us: 1.03x faster                                                      |
| pidigits                   | 194 ms                                                 | 189 ms: 1.03x faster                                                      |
| logging_simple             | 6.22 us                                                | 6.07 us: 1.03x faster                                                     |
| xml_etree_parse            | 164 ms                                                 | 160 ms: 1.03x faster                                                      |
| sqlglot_transpile          | 1.75 ms                                                | 1.71 ms: 1.02x faster                                                     |
| json_loads                 | 29.2 us                                                | 28.6 us: 1.02x faster                                                     |
| raytrace                   | 309 ms                                                 | 303 ms: 1.02x faster                                                      |
| logging_format             | 6.81 us                                                | 6.71 us: 1.01x faster                                                     |
| crypto_pyaes               | 76.7 ms                                                | 75.6 ms: 1.01x faster                                                     |
| tornado_http               | 98.1 ms                                                | 96.9 ms: 1.01x faster                                                     |
| scimark_fft                | 345 ms                                                 | 342 ms: 1.01x faster                                                      |
| mdp                        | 2.77 sec                                               | 2.75 sec: 1.01x faster                                                    |
| sympy_sum                  | 169 ms                                                 | 167 ms: 1.01x faster                                                      |
| unpickle_list              | 5.21 us                                                | 5.19 us: 1.01x faster                                                     |
| float                      | 78.9 ms                                                | 79.6 ms: 1.01x slower                                                     |
| deepcopy                   | 365 us                                                 | 370 us: 1.01x slower                                                      |
| mako                       | 10.7 ms                                                | 10.8 ms: 1.01x slower                                                     |
| fannkuch                   | 405 ms                                                 | 410 ms: 1.01x slower                                                      |
| sqlglot_normalize          | 113 ms                                                 | 114 ms: 1.02x slower                                                      |
| deepcopy_reduce            | 3.22 us                                                | 3.27 us: 1.02x slower                                                     |
| meteor_contest             | 109 ms                                                 | 111 ms: 1.02x slower                                                      |
| html5lib                   | 64.8 ms                                                | 66.4 ms: 1.02x slower                                                     |
| pprint_pformat             | 1.55 sec                                               | 1.60 sec: 1.03x slower                                                    |
| pprint_safe_repr           | 747 ms                                                 | 767 ms: 1.03x slower                                                      |
| sympy_expand               | 484 ms                                                 | 500 ms: 1.03x slower                                                      |
| asyncio_websockets         | 550 ms                                                 | 570 ms: 1.04x slower                                                      |
| dask                       | 365 ms                                                 | 378 ms: 1.04x slower                                                      |
| xml_etree_iterparse        | 108 ms                                                 | 112 ms: 1.04x slower                                                      |
| sympy_integrate            | 21.5 ms                                                | 22.4 ms: 1.04x slower                                                     |
| json                       | 5.24 ms                                                | 5.47 ms: 1.04x slower                                                     |
| pathlib                    | 18.5 ms                                                | 19.4 ms: 1.05x slower                                                     |
| thrift                     | 784 us                                                 | 822 us: 1.05x slower                                                      |
| spectral_norm              | 108 ms                                                 | 114 ms: 1.05x slower                                                      |
| pickle_dict                | 34.6 us                                                | 36.5 us: 1.06x slower                                                     |
| pycparser                  | 1.19 sec                                               | 1.25 sec: 1.06x slower                                                    |
| deltablue                  | 3.92 ms                                                | 4.15 ms: 1.06x slower                                                     |
| 2to3                       | 264 ms                                                 | 280 ms: 1.06x slower                                                      |
| scimark_monte_carlo        | 70.7 ms                                                | 75.3 ms: 1.07x slower                                                     |
| bench_thread_pool          | 834 us                                                 | 890 us: 1.07x slower                                                      |
| chameleon                  | 6.70 ms                                                | 7.16 ms: 1.07x slower                                                     |
| regex_compile              | 141 ms                                                 | 151 ms: 1.07x slower                                                      |
| genshi_xml                 | 53.4 ms                                                | 57.3 ms: 1.07x slower                                                     |
| sqlglot_optimize           | 55.3 ms                                                | 59.5 ms: 1.08x slower                                                     |
| regex_effbot               | 3.51 ms                                                | 3.78 ms: 1.08x slower                                                     |
| richards                   | 49.8 ms                                                | 54.0 ms: 1.08x slower                                                     |
| aiohttp                    | 1.12 ms                                                | 1.21 ms: 1.09x slower                                                     |
| scimark_sor                | 121 ms                                                 | 132 ms: 1.09x slower                                                      |
| gunicorn                   | 1.20 ms                                                | 1.31 ms: 1.09x slower                                                     |
| docutils                   | 2.66 sec                                               | 2.93 sec: 1.10x slower                                                    |
| xml_etree_process          | 56.9 ms                                                | 62.6 ms: 1.10x slower                                                     |
| pickle                     | 11.0 us                                                | 12.1 us: 1.10x slower                                                     |
| django_template            | 33.5 ms                                                | 37.1 ms: 1.11x slower                                                     |
| unpickle_pure_python       | 242 us                                                 | 268 us: 1.11x slower                                                      |
| dulwich_log                | 64.6 ms                                                | 71.8 ms: 1.11x slower                                                     |
| deepcopy_memo              | 40.2 us                                                | 44.8 us: 1.12x slower                                                     |
| pickle_list                | 4.59 us                                                | 5.12 us: 1.12x slower                                                     |
| sqlite_synth               | 2.57 us                                                | 2.88 us: 1.12x slower                                                     |
| regex_v8                   | 22.9 ms                                                | 25.7 ms: 1.12x slower                                                     |
| pyflate                    | 434 ms                                                 | 488 ms: 1.12x slower                                                      |
| scimark_lu                 | 116 ms                                                 | 132 ms: 1.13x slower                                                      |
| regex_dna                  | 205 ms                                                 | 234 ms: 1.14x slower                                                      |
| genshi_text                | 22.5 ms                                                | 25.8 ms: 1.14x slower                                                     |
| xml_etree_generate         | 81.1 ms                                                | 92.9 ms: 1.15x slower                                                     |
| mypy2                      | 686 ms                                                 | 801 ms: 1.17x slower                                                      |
| go                         | 149 ms                                                 | 175 ms: 1.18x slower                                                      |
| hexiom                     | 6.89 ms                                                | 8.12 ms: 1.18x slower                                                     |
| create_gc_cycles           | 1.43 ms                                                | 1.69 ms: 1.18x slower                                                     |
| unpickle                   | 13.8 us                                                | 17.1 us: 1.24x slower                                                     |
| coverage                   | 78.8 ms                                                | 97.8 ms: 1.24x slower                                                     |
| nqueens                    | 87.9 ms                                                | 109 ms: 1.24x slower                                                      |
| telco                      | 6.86 ms                                                | 8.85 ms: 1.29x slower                                                     |
| python_startup             | 8.56 ms                                                | 11.1 ms: 1.29x slower                                                     |
| async_generators           | 374 ms                                                 | 502 ms: 1.34x slower                                                      |
| python_startup_no_site     | 6.01 ms                                                | 9.54 ms: 1.59x slower                                                     |
| unpack_sequence            | 43.5 ns                                                | 88.0 ns: 2.02x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (2): sympy_str, bench_mp_pool
Ignored benchmarks (3) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 92.79% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 1.11x