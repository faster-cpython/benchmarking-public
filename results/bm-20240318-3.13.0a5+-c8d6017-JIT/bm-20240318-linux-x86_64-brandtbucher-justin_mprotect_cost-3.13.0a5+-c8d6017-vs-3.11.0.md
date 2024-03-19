# Results vs. 3.11.0

- fork: brandtbucher
- ref: justin_mprotect_cost
- machine: linux-x86_64
- commit hash: c8d6017
- commit date: 2024-03-18
- overall geometric mean: 1.02x faster
- HPT reliability: 52.20%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.24x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240318-linux-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 264 ms                                                 | 282 ms: 1.07x slower                                                         |
| chameleon      | 6.70 ms                                                | 6.84 ms: 1.02x slower                                                        |
| docutils       | 2.66 sec                                               | 2.78 sec: 1.05x slower                                                       |
| html5lib       | 64.8 ms                                                | 66.4 ms: 1.02x slower                                                        |
| tornado_http   | 98.1 ms                                                | 99.0 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                  | 1.03x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240318-linux-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_none            | 528 ms                                                 | 447 ms: 1.18x faster                                                         |
| async_tree_memoization     | 639 ms                                                 | 577 ms: 1.11x faster                                                         |
| async_tree_none_tg         | 491 ms                                                 | 458 ms: 1.07x faster                                                         |
| async_tree_memoization_tg  | 626 ms                                                 | 589 ms: 1.06x faster                                                         |
| async_tree_io              | 1.29 sec                                               | 1.22 sec: 1.06x faster                                                       |
| async_tree_io_tg           | 1.29 sec                                               | 1.23 sec: 1.05x faster                                                       |
| async_tree_cpu_io_mixed    | 749 ms                                                 | 723 ms: 1.04x faster                                                         |
| async_tree_cpu_io_mixed_tg | 761 ms                                                 | 740 ms: 1.03x faster                                                         |
| Geometric mean             | (ref)                                                  | 1.07x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240318-linux-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| pidigits       | 194 ms                                                 | 189 ms: 1.03x faster                                                         |
| nbody          | 96.0 ms                                                | 94.2 ms: 1.02x faster                                                        |
| float          | 78.9 ms                                                | 80.5 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240318-linux-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 141 ms                                                 | 143 ms: 1.01x slower                                                         |
| regex_effbot   | 3.51 ms                                                | 3.85 ms: 1.10x slower                                                        |
| regex_v8       | 22.9 ms                                                | 25.8 ms: 1.13x slower                                                        |
| regex_dna      | 205 ms                                                 | 231 ms: 1.13x slower                                                         |
| Geometric mean | (ref)                                                  | 1.09x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240318-linux-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 13.3 ms                                                | 10.4 ms: 1.28x faster                                                        |
| tomli_loads          | 2.30 sec                                               | 2.08 sec: 1.11x faster                                                       |
| pickle_pure_python   | 320 us                                                 | 302 us: 1.06x faster                                                         |
| json_loads           | 29.2 us                                                | 27.9 us: 1.05x faster                                                        |
| unpickle_list        | 5.21 us                                                | 5.02 us: 1.04x faster                                                        |
| xml_etree_parse      | 164 ms                                                 | 161 ms: 1.02x faster                                                         |
| pickle_dict          | 34.6 us                                                | 34.1 us: 1.01x faster                                                        |
| unpickle_pure_python | 242 us                                                 | 239 us: 1.01x faster                                                         |
| xml_etree_process    | 56.9 ms                                                | 59.9 ms: 1.05x slower                                                        |
| pickle               | 11.0 us                                                | 11.6 us: 1.05x slower                                                        |
| unpickle             | 13.8 us                                                | 14.6 us: 1.06x slower                                                        |
| pickle_list          | 4.59 us                                                | 4.92 us: 1.07x slower                                                        |
| xml_etree_generate   | 81.1 ms                                                | 87.6 ms: 1.08x slower                                                        |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                                 |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240318-linux-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.56 ms                                                | 11.8 ms: 1.37x slower                                                        |
| python_startup_no_site | 6.01 ms                                                | 10.3 ms: 1.72x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.54x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240318-linux-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                        |
| genshi_xml      | 53.4 ms                                                | 55.3 ms: 1.03x slower                                                        |
| django_template | 33.5 ms                                                | 34.9 ms: 1.04x slower                                                        |
| genshi_text     | 22.5 ms                                                | 24.3 ms: 1.08x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240318-linux-x86_64-brandtbucher-justin_mprotect_cost-3.13.0a5+-c8d6017 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| typing_runtime_protocols   | 520 us                                                 | 111 us: 4.69x faster                                                         |
| generators                 | 74.9 ms                                                | 29.8 ms: 2.52x faster                                                        |
| asyncio_tcp                | 875 ms                                                 | 504 ms: 1.74x faster                                                         |
| asyncio_tcp_ssl            | 3.11 sec                                               | 1.85 sec: 1.68x faster                                                       |
| pylint                     | 476 ms                                                 | 325 ms: 1.47x faster                                                         |
| comprehensions             | 23.6 us                                                | 17.3 us: 1.36x faster                                                        |
| json_dumps                 | 13.3 ms                                                | 10.4 ms: 1.28x faster                                                        |
| async_tree_none            | 528 ms                                                 | 447 ms: 1.18x faster                                                         |
| coroutines                 | 27.0 ms                                                | 22.9 ms: 1.18x faster                                                        |
| richards_super             | 61.9 ms                                                | 53.0 ms: 1.17x faster                                                        |
| deltablue                  | 3.92 ms                                                | 3.43 ms: 1.14x faster                                                        |
| chaos                      | 71.9 ms                                                | 64.4 ms: 1.12x faster                                                        |
| tomli_loads                | 2.30 sec                                               | 2.08 sec: 1.11x faster                                                       |
| async_tree_memoization     | 639 ms                                                 | 577 ms: 1.11x faster                                                         |
| logging_silent             | 111 ns                                                 | 101 ns: 1.10x faster                                                         |
| sqlglot_parse              | 1.43 ms                                                | 1.32 ms: 1.09x faster                                                        |
| async_tree_none_tg         | 491 ms                                                 | 458 ms: 1.07x faster                                                         |
| richards                   | 49.8 ms                                                | 46.7 ms: 1.07x faster                                                        |
| async_tree_memoization_tg  | 626 ms                                                 | 589 ms: 1.06x faster                                                         |
| pickle_pure_python         | 320 us                                                 | 302 us: 1.06x faster                                                         |
| async_tree_io              | 1.29 sec                                               | 1.22 sec: 1.06x faster                                                       |
| logging_simple             | 6.22 us                                                | 5.88 us: 1.06x faster                                                        |
| sqlglot_transpile          | 1.75 ms                                                | 1.66 ms: 1.06x faster                                                        |
| deepcopy_reduce            | 3.22 us                                                | 3.05 us: 1.05x faster                                                        |
| logging_format             | 6.81 us                                                | 6.48 us: 1.05x faster                                                        |
| async_tree_io_tg           | 1.29 sec                                               | 1.23 sec: 1.05x faster                                                       |
| sympy_sum                  | 169 ms                                                 | 161 ms: 1.05x faster                                                         |
| raytrace                   | 309 ms                                                 | 295 ms: 1.05x faster                                                         |
| json_loads                 | 29.2 us                                                | 27.9 us: 1.05x faster                                                        |
| deepcopy                   | 365 us                                                 | 349 us: 1.05x faster                                                         |
| sqlglot_normalize          | 113 ms                                                 | 108 ms: 1.04x faster                                                         |
| sympy_str                  | 297 ms                                                 | 285 ms: 1.04x faster                                                         |
| djangocms                  | 33.5 us                                                | 32.2 us: 1.04x faster                                                        |
| unpickle_list              | 5.21 us                                                | 5.02 us: 1.04x faster                                                        |
| async_tree_cpu_io_mixed    | 749 ms                                                 | 723 ms: 1.04x faster                                                         |
| deepcopy_memo              | 40.2 us                                                | 38.9 us: 1.03x faster                                                        |
| async_tree_cpu_io_mixed_tg | 761 ms                                                 | 740 ms: 1.03x faster                                                         |
| pidigits                   | 194 ms                                                 | 189 ms: 1.03x faster                                                         |
| gc_traversal               | 4.01 ms                                                | 3.92 ms: 1.02x faster                                                        |
| fannkuch                   | 405 ms                                                 | 397 ms: 1.02x faster                                                         |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.92 ms: 1.02x faster                                                        |
| xml_etree_parse            | 164 ms                                                 | 161 ms: 1.02x faster                                                         |
| json                       | 5.24 ms                                                | 5.15 ms: 1.02x faster                                                        |
| nbody                      | 96.0 ms                                                | 94.2 ms: 1.02x faster                                                        |
| scimark_fft                | 345 ms                                                 | 340 ms: 1.02x faster                                                         |
| crypto_pyaes               | 76.7 ms                                                | 75.4 ms: 1.02x faster                                                        |
| pickle_dict                | 34.6 us                                                | 34.1 us: 1.01x faster                                                        |
| sympy_integrate            | 21.5 ms                                                | 21.2 ms: 1.01x faster                                                        |
| unpickle_pure_python       | 242 us                                                 | 239 us: 1.01x faster                                                         |
| sympy_expand               | 484 ms                                                 | 486 ms: 1.00x slower                                                         |
| pathlib                    | 18.5 ms                                                | 18.7 ms: 1.01x slower                                                        |
| tornado_http               | 98.1 ms                                                | 99.0 ms: 1.01x slower                                                        |
| meteor_contest             | 109 ms                                                 | 110 ms: 1.01x slower                                                         |
| regex_compile              | 141 ms                                                 | 143 ms: 1.01x slower                                                         |
| pprint_pformat             | 1.55 sec                                               | 1.58 sec: 1.02x slower                                                       |
| nqueens                    | 87.9 ms                                                | 89.3 ms: 1.02x slower                                                        |
| sqlglot_optimize           | 55.3 ms                                                | 56.3 ms: 1.02x slower                                                        |
| chameleon                  | 6.70 ms                                                | 6.84 ms: 1.02x slower                                                        |
| float                      | 78.9 ms                                                | 80.5 ms: 1.02x slower                                                        |
| dask                       | 365 ms                                                 | 373 ms: 1.02x slower                                                         |
| mdp                        | 2.77 sec                                               | 2.84 sec: 1.02x slower                                                       |
| thrift                     | 784 us                                                 | 802 us: 1.02x slower                                                         |
| asyncio_websockets         | 550 ms                                                 | 563 ms: 1.02x slower                                                         |
| hexiom                     | 6.89 ms                                                | 7.05 ms: 1.02x slower                                                        |
| html5lib                   | 64.8 ms                                                | 66.4 ms: 1.02x slower                                                        |
| bench_thread_pool          | 834 us                                                 | 859 us: 1.03x slower                                                         |
| mako                       | 10.7 ms                                                | 11.0 ms: 1.03x slower                                                        |
| pprint_safe_repr           | 747 ms                                                 | 772 ms: 1.03x slower                                                         |
| genshi_xml                 | 53.4 ms                                                | 55.3 ms: 1.03x slower                                                        |
| django_template            | 33.5 ms                                                | 34.9 ms: 1.04x slower                                                        |
| docutils                   | 2.66 sec                                               | 2.78 sec: 1.05x slower                                                       |
| spectral_norm              | 108 ms                                                 | 113 ms: 1.05x slower                                                         |
| xml_etree_process          | 56.9 ms                                                | 59.9 ms: 1.05x slower                                                        |
| scimark_sor                | 121 ms                                                 | 128 ms: 1.05x slower                                                         |
| pickle                     | 11.0 us                                                | 11.6 us: 1.05x slower                                                        |
| unpickle                   | 13.8 us                                                | 14.6 us: 1.06x slower                                                        |
| pycparser                  | 1.19 sec                                               | 1.26 sec: 1.06x slower                                                       |
| go                         | 149 ms                                                 | 158 ms: 1.06x slower                                                         |
| 2to3                       | 264 ms                                                 | 282 ms: 1.07x slower                                                         |
| pickle_list                | 4.59 us                                                | 4.92 us: 1.07x slower                                                        |
| genshi_text                | 22.5 ms                                                | 24.3 ms: 1.08x slower                                                        |
| create_gc_cycles           | 1.43 ms                                                | 1.55 ms: 1.08x slower                                                        |
| xml_etree_generate         | 81.1 ms                                                | 87.6 ms: 1.08x slower                                                        |
| gunicorn                   | 1.20 ms                                                | 1.30 ms: 1.08x slower                                                        |
| aiohttp                    | 1.12 ms                                                | 1.21 ms: 1.08x slower                                                        |
| dulwich_log                | 64.6 ms                                                | 70.5 ms: 1.09x slower                                                        |
| regex_effbot               | 3.51 ms                                                | 3.85 ms: 1.10x slower                                                        |
| sqlite_synth               | 2.57 us                                                | 2.85 us: 1.11x slower                                                        |
| scimark_lu                 | 116 ms                                                 | 129 ms: 1.11x slower                                                         |
| regex_v8                   | 22.9 ms                                                | 25.8 ms: 1.13x slower                                                        |
| regex_dna                  | 205 ms                                                 | 231 ms: 1.13x slower                                                         |
| pyflate                    | 434 ms                                                 | 495 ms: 1.14x slower                                                         |
| telco                      | 6.86 ms                                                | 8.33 ms: 1.21x slower                                                        |
| coverage                   | 78.8 ms                                                | 96.9 ms: 1.23x slower                                                        |
| async_generators           | 374 ms                                                 | 464 ms: 1.24x slower                                                         |
| mypy2                      | 686 ms                                                 | 900 ms: 1.31x slower                                                         |
| python_startup             | 8.56 ms                                                | 11.8 ms: 1.37x slower                                                        |
| python_startup_no_site     | 6.01 ms                                                | 10.3 ms: 1.72x slower                                                        |
| unpack_sequence            | 43.5 ns                                                | 89.2 ns: 2.05x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                 |

Benchmark hidden because not significant (3): bench_mp_pool, xml_etree_iterparse, scimark_monte_carlo
Ignored benchmarks (3) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 52.20% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 1.24x