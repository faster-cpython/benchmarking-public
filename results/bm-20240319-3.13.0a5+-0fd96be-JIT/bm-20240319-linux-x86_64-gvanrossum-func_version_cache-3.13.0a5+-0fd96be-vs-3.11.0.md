# Results vs. 3.11.0

- fork: gvanrossum
- ref: func_version_cache
- machine: linux-x86_64
- commit hash: 0fd96be
- commit date: 2024-03-19
- overall geometric mean: 1.02x faster
- HPT reliability: 54.72%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5+-0fd96be |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 264 ms                                                 | 281 ms: 1.06x slower                                                     |
| chameleon      | 6.70 ms                                                | 6.93 ms: 1.03x slower                                                    |
| docutils       | 2.66 sec                                               | 2.75 sec: 1.03x slower                                                   |
| html5lib       | 64.8 ms                                                | 67.0 ms: 1.03x slower                                                    |
| tornado_http   | 98.1 ms                                                | 99.1 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                  | 1.04x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5+-0fd96be |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_none            | 528 ms                                                 | 450 ms: 1.17x faster                                                     |
| async_tree_memoization     | 639 ms                                                 | 575 ms: 1.11x faster                                                     |
| async_tree_none_tg         | 491 ms                                                 | 460 ms: 1.07x faster                                                     |
| async_tree_memoization_tg  | 626 ms                                                 | 592 ms: 1.06x faster                                                     |
| async_tree_io_tg           | 1.29 sec                                               | 1.23 sec: 1.05x faster                                                   |
| async_tree_io              | 1.29 sec                                               | 1.22 sec: 1.05x faster                                                   |
| async_tree_cpu_io_mixed    | 749 ms                                                 | 730 ms: 1.03x faster                                                     |
| async_tree_cpu_io_mixed_tg | 761 ms                                                 | 743 ms: 1.02x faster                                                     |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5+-0fd96be |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| nbody          | 96.0 ms                                                | 92.6 ms: 1.04x faster                                                    |
| pidigits       | 194 ms                                                 | 190 ms: 1.02x faster                                                     |
| float          | 78.9 ms                                                | 81.4 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                  | 1.01x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5+-0fd96be |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 141 ms                                                 | 143 ms: 1.01x slower                                                     |
| regex_effbot   | 3.51 ms                                                | 3.58 ms: 1.02x slower                                                    |
| regex_v8       | 22.9 ms                                                | 24.3 ms: 1.06x slower                                                    |
| regex_dna      | 205 ms                                                 | 219 ms: 1.07x slower                                                     |
| Geometric mean | (ref)                                                  | 1.04x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5+-0fd96be |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 13.3 ms                                                | 10.5 ms: 1.27x faster                                                    |
| tomli_loads          | 2.30 sec                                               | 2.06 sec: 1.12x faster                                                   |
| pickle_pure_python   | 320 us                                                 | 304 us: 1.05x faster                                                     |
| pickle_dict          | 34.6 us                                                | 33.5 us: 1.03x faster                                                    |
| unpickle_list        | 5.21 us                                                | 5.05 us: 1.03x faster                                                    |
| json_loads           | 29.2 us                                                | 28.7 us: 1.02x faster                                                    |
| unpickle_pure_python | 242 us                                                 | 237 us: 1.02x faster                                                     |
| xml_etree_parse      | 164 ms                                                 | 161 ms: 1.02x faster                                                     |
| xml_etree_iterparse  | 108 ms                                                 | 109 ms: 1.01x slower                                                     |
| pickle               | 11.0 us                                                | 11.6 us: 1.05x slower                                                    |
| xml_etree_process    | 56.9 ms                                                | 60.1 ms: 1.06x slower                                                    |
| pickle_list          | 4.59 us                                                | 4.93 us: 1.07x slower                                                    |
| xml_etree_generate   | 81.1 ms                                                | 88.0 ms: 1.09x slower                                                    |
| unpickle             | 13.8 us                                                | 15.1 us: 1.09x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.01x faster                                                             |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5+-0fd96be |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 8.56 ms                                                | 11.5 ms: 1.35x slower                                                    |
| python_startup_no_site | 6.01 ms                                                | 10.1 ms: 1.68x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.51x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5+-0fd96be |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| django_template | 33.5 ms                                                | 34.5 ms: 1.03x slower                                                    |
| mako            | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                    |
| genshi_xml      | 53.4 ms                                                | 55.0 ms: 1.03x slower                                                    |
| genshi_text     | 22.5 ms                                                | 24.2 ms: 1.08x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240319-linux-x86_64-gvanrossum-func_version_cache-3.13.0a5+-0fd96be |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| typing_runtime_protocols   | 520 us                                                 | 111 us: 4.66x faster                                                     |
| generators                 | 74.9 ms                                                | 29.6 ms: 2.53x faster                                                    |
| asyncio_tcp                | 875 ms                                                 | 504 ms: 1.74x faster                                                     |
| asyncio_tcp_ssl            | 3.11 sec                                               | 1.85 sec: 1.68x faster                                                   |
| pylint                     | 476 ms                                                 | 324 ms: 1.47x faster                                                     |
| comprehensions             | 23.6 us                                                | 17.9 us: 1.32x faster                                                    |
| json_dumps                 | 13.3 ms                                                | 10.5 ms: 1.27x faster                                                    |
| coroutines                 | 27.0 ms                                                | 22.7 ms: 1.19x faster                                                    |
| richards_super             | 61.9 ms                                                | 52.5 ms: 1.18x faster                                                    |
| async_tree_none            | 528 ms                                                 | 450 ms: 1.17x faster                                                     |
| deltablue                  | 3.92 ms                                                | 3.46 ms: 1.13x faster                                                    |
| chaos                      | 71.9 ms                                                | 64.3 ms: 1.12x faster                                                    |
| tomli_loads                | 2.30 sec                                               | 2.06 sec: 1.12x faster                                                   |
| async_tree_memoization     | 639 ms                                                 | 575 ms: 1.11x faster                                                     |
| logging_silent             | 111 ns                                                 | 101 ns: 1.10x faster                                                     |
| sqlglot_parse              | 1.43 ms                                                | 1.32 ms: 1.08x faster                                                    |
| richards                   | 49.8 ms                                                | 46.2 ms: 1.08x faster                                                    |
| async_tree_none_tg         | 491 ms                                                 | 460 ms: 1.07x faster                                                     |
| logging_simple             | 6.22 us                                                | 5.84 us: 1.07x faster                                                    |
| async_tree_memoization_tg  | 626 ms                                                 | 592 ms: 1.06x faster                                                     |
| mdp                        | 2.77 sec                                               | 2.63 sec: 1.06x faster                                                   |
| async_tree_io_tg           | 1.29 sec                                               | 1.23 sec: 1.05x faster                                                   |
| pickle_pure_python         | 320 us                                                 | 304 us: 1.05x faster                                                     |
| async_tree_io              | 1.29 sec                                               | 1.22 sec: 1.05x faster                                                   |
| sqlglot_transpile          | 1.75 ms                                                | 1.66 ms: 1.05x faster                                                    |
| logging_format             | 6.81 us                                                | 6.48 us: 1.05x faster                                                    |
| djangocms                  | 33.5 us                                                | 31.9 us: 1.05x faster                                                    |
| raytrace                   | 309 ms                                                 | 294 ms: 1.05x faster                                                     |
| deepcopy_memo              | 40.2 us                                                | 38.5 us: 1.04x faster                                                    |
| gc_traversal               | 4.01 ms                                                | 3.85 ms: 1.04x faster                                                    |
| deepcopy                   | 365 us                                                 | 351 us: 1.04x faster                                                     |
| nbody                      | 96.0 ms                                                | 92.6 ms: 1.04x faster                                                    |
| sqlglot_normalize          | 113 ms                                                 | 109 ms: 1.03x faster                                                     |
| pickle_dict                | 34.6 us                                                | 33.5 us: 1.03x faster                                                    |
| unpickle_list              | 5.21 us                                                | 5.05 us: 1.03x faster                                                    |
| sympy_sum                  | 169 ms                                                 | 164 ms: 1.03x faster                                                     |
| deepcopy_reduce            | 3.22 us                                                | 3.13 us: 1.03x faster                                                    |
| sympy_str                  | 297 ms                                                 | 289 ms: 1.03x faster                                                     |
| async_tree_cpu_io_mixed    | 749 ms                                                 | 730 ms: 1.03x faster                                                     |
| pidigits                   | 194 ms                                                 | 190 ms: 1.02x faster                                                     |
| async_tree_cpu_io_mixed_tg | 761 ms                                                 | 743 ms: 1.02x faster                                                     |
| json_loads                 | 29.2 us                                                | 28.7 us: 1.02x faster                                                    |
| unpickle_pure_python       | 242 us                                                 | 237 us: 1.02x faster                                                     |
| xml_etree_parse            | 164 ms                                                 | 161 ms: 1.02x faster                                                     |
| crypto_pyaes               | 76.7 ms                                                | 75.6 ms: 1.01x faster                                                    |
| fannkuch                   | 405 ms                                                 | 400 ms: 1.01x faster                                                     |
| sympy_integrate            | 21.5 ms                                                | 21.3 ms: 1.01x faster                                                    |
| scimark_fft                | 345 ms                                                 | 348 ms: 1.01x slower                                                     |
| sympy_expand               | 484 ms                                                 | 490 ms: 1.01x slower                                                     |
| regex_compile              | 141 ms                                                 | 143 ms: 1.01x slower                                                     |
| tornado_http               | 98.1 ms                                                | 99.1 ms: 1.01x slower                                                    |
| pathlib                    | 18.5 ms                                                | 18.7 ms: 1.01x slower                                                    |
| pycparser                  | 1.19 sec                                               | 1.20 sec: 1.01x slower                                                   |
| xml_etree_iterparse        | 108 ms                                                 | 109 ms: 1.01x slower                                                     |
| meteor_contest             | 109 ms                                                 | 110 ms: 1.01x slower                                                     |
| bench_thread_pool          | 834 us                                                 | 848 us: 1.02x slower                                                     |
| dask                       | 365 ms                                                 | 371 ms: 1.02x slower                                                     |
| pprint_safe_repr           | 747 ms                                                 | 760 ms: 1.02x slower                                                     |
| hexiom                     | 6.89 ms                                                | 7.03 ms: 1.02x slower                                                    |
| regex_effbot               | 3.51 ms                                                | 3.58 ms: 1.02x slower                                                    |
| asyncio_websockets         | 550 ms                                                 | 564 ms: 1.02x slower                                                     |
| nqueens                    | 87.9 ms                                                | 90.2 ms: 1.03x slower                                                    |
| thrift                     | 784 us                                                 | 805 us: 1.03x slower                                                     |
| django_template            | 33.5 ms                                                | 34.5 ms: 1.03x slower                                                    |
| mako                       | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                    |
| genshi_xml                 | 53.4 ms                                                | 55.0 ms: 1.03x slower                                                    |
| float                      | 78.9 ms                                                | 81.4 ms: 1.03x slower                                                    |
| sqlglot_optimize           | 55.3 ms                                                | 57.2 ms: 1.03x slower                                                    |
| html5lib                   | 64.8 ms                                                | 67.0 ms: 1.03x slower                                                    |
| docutils                   | 2.66 sec                                               | 2.75 sec: 1.03x slower                                                   |
| chameleon                  | 6.70 ms                                                | 6.93 ms: 1.03x slower                                                    |
| pickle                     | 11.0 us                                                | 11.6 us: 1.05x slower                                                    |
| xml_etree_process          | 56.9 ms                                                | 60.1 ms: 1.06x slower                                                    |
| spectral_norm              | 108 ms                                                 | 115 ms: 1.06x slower                                                     |
| scimark_sor                | 121 ms                                                 | 129 ms: 1.06x slower                                                     |
| regex_v8                   | 22.9 ms                                                | 24.3 ms: 1.06x slower                                                    |
| go                         | 149 ms                                                 | 158 ms: 1.06x slower                                                     |
| 2to3                       | 264 ms                                                 | 281 ms: 1.06x slower                                                     |
| create_gc_cycles           | 1.43 ms                                                | 1.53 ms: 1.07x slower                                                    |
| aiohttp                    | 1.12 ms                                                | 1.19 ms: 1.07x slower                                                    |
| regex_dna                  | 205 ms                                                 | 219 ms: 1.07x slower                                                     |
| pickle_list                | 4.59 us                                                | 4.93 us: 1.07x slower                                                    |
| genshi_text                | 22.5 ms                                                | 24.2 ms: 1.08x slower                                                    |
| gunicorn                   | 1.20 ms                                                | 1.29 ms: 1.08x slower                                                    |
| xml_etree_generate         | 81.1 ms                                                | 88.0 ms: 1.09x slower                                                    |
| dulwich_log                | 64.6 ms                                                | 70.2 ms: 1.09x slower                                                    |
| unpickle                   | 13.8 us                                                | 15.1 us: 1.09x slower                                                    |
| sqlite_synth               | 2.57 us                                                | 2.85 us: 1.11x slower                                                    |
| scimark_lu                 | 116 ms                                                 | 131 ms: 1.12x slower                                                     |
| pyflate                    | 434 ms                                                 | 495 ms: 1.14x slower                                                     |
| telco                      | 6.86 ms                                                | 8.42 ms: 1.23x slower                                                    |
| coverage                   | 78.8 ms                                                | 98.6 ms: 1.25x slower                                                    |
| async_generators           | 374 ms                                                 | 478 ms: 1.28x slower                                                     |
| mypy2                      | 686 ms                                                 | 903 ms: 1.32x slower                                                     |
| python_startup             | 8.56 ms                                                | 11.5 ms: 1.35x slower                                                    |
| python_startup_no_site     | 6.01 ms                                                | 10.1 ms: 1.68x slower                                                    |
| unpack_sequence            | 43.5 ns                                                | 87.7 ns: 2.02x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                             |

Benchmark hidden because not significant (5): pprint_pformat, bench_mp_pool, scimark_monte_carlo, json, scimark_sparse_mat_mult
Ignored benchmarks (3) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 54.72% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: 1.13x