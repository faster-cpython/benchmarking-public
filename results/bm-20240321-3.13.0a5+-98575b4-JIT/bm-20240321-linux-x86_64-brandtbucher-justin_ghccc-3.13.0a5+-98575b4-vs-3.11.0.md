# Results vs. 3.11.0

- fork: brandtbucher
- ref: justin_ghccc
- machine: linux-x86_64
- commit hash: 98575b4
- commit date: 2024-03-21
- overall geometric mean: 1.20x slower
- HPT reliability: 98.86%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.13x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 264 ms                                                 | 303 ms: 1.15x slower                                                 |
| chameleon      | 6.70 ms                                                | 7.04 ms: 1.05x slower                                                |
| docutils       | 2.66 sec                                               | 4.82 sec: 1.81x slower                                               |
| html5lib       | 64.8 ms                                                | 75.2 ms: 1.16x slower                                                |
| tornado_http   | 98.1 ms                                                | 101 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.21x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_cpu_io_mixed    | 749 ms                                                 | 4.17 sec: 5.57x slower                                               |
| async_tree_cpu_io_mixed_tg | 761 ms                                                 | 4.57 sec: 6.00x slower                                               |
| async_tree_none            | 528 ms                                                 | 3.43 sec: 6.50x slower                                               |
| async_tree_memoization     | 639 ms                                                 | 4.43 sec: 6.93x slower                                               |
| async_tree_memoization_tg  | 626 ms                                                 | 4.71 sec: 7.52x slower                                               |
| async_tree_none_tg         | 491 ms                                                 | 3.75 sec: 7.63x slower                                               |
| async_tree_io              | 1.29 sec                                               | 13.3 sec: 10.31x slower                                              |
| async_tree_io_tg           | 1.29 sec                                               | 14.1 sec: 10.91x slower                                              |
| Geometric mean             | (ref)                                                  | 7.47x slower                                                         |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 96.0 ms                                                | 81.4 ms: 1.18x faster                                                |
| pidigits       | 194 ms                                                 | 189 ms: 1.03x faster                                                 |
| float          | 78.9 ms                                                | 139 ms: 1.76x slower                                                 |
| Geometric mean | (ref)                                                  | 1.13x slower                                                         |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.51 ms                                                | 3.70 ms: 1.05x slower                                                |
| regex_dna      | 205 ms                                                 | 227 ms: 1.11x slower                                                 |
| regex_v8       | 22.9 ms                                                | 26.1 ms: 1.14x slower                                                |
| Geometric mean | (ref)                                                  | 1.07x slower                                                         |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| json_dumps           | 13.3 ms                                                | 10.6 ms: 1.26x faster                                                |
| tomli_loads          | 2.30 sec                                               | 2.00 sec: 1.15x faster                                               |
| unpickle_pure_python | 242 us                                                 | 227 us: 1.07x faster                                                 |
| pickle_pure_python   | 320 us                                                 | 307 us: 1.04x faster                                                 |
| json_loads           | 29.2 us                                                | 28.4 us: 1.03x faster                                                |
| unpickle_list        | 5.21 us                                                | 5.17 us: 1.01x faster                                                |
| pickle_dict          | 34.6 us                                                | 36.3 us: 1.05x slower                                                |
| unpickle             | 13.8 us                                                | 15.1 us: 1.09x slower                                                |
| pickle               | 11.0 us                                                | 12.0 us: 1.09x slower                                                |
| pickle_list          | 4.59 us                                                | 5.20 us: 1.13x slower                                                |
| xml_etree_process    | 56.9 ms                                                | 68.3 ms: 1.20x slower                                                |
| xml_etree_generate   | 81.1 ms                                                | 99.2 ms: 1.22x slower                                                |
| xml_etree_parse      | 164 ms                                                 | 219 ms: 1.33x slower                                                 |
| xml_etree_iterparse  | 108 ms                                                 | 162 ms: 1.50x slower                                                 |
| Geometric mean       | (ref)                                                  | 1.07x slower                                                         |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 8.56 ms                                                | 11.8 ms: 1.37x slower                                                |
| python_startup_no_site | 6.01 ms                                                | 10.1 ms: 1.68x slower                                                |
| Geometric mean         | (ref)                                                  | 1.52x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 10.7 ms                                                | 10.4 ms: 1.03x faster                                                |
| django_template | 33.5 ms                                                | 35.5 ms: 1.06x slower                                                |
| genshi_text     | 22.5 ms                                                | 25.1 ms: 1.11x slower                                                |
| genshi_xml      | 53.4 ms                                                | 60.5 ms: 1.13x slower                                                |
| Geometric mean  | (ref)                                                  | 1.07x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240321-linux-x86_64-brandtbucher-justin_ghccc-3.13.0a5+-98575b4 |
|----------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| typing_runtime_protocols   | 520 us                                                 | 113 us: 4.61x faster                                                 |
| generators                 | 74.9 ms                                                | 29.7 ms: 2.52x faster                                                |
| asyncio_tcp                | 875 ms                                                 | 510 ms: 1.72x faster                                                 |
| asyncio_tcp_ssl            | 3.11 sec                                               | 1.86 sec: 1.68x faster                                               |
| comprehensions             | 23.6 us                                                | 16.9 us: 1.40x faster                                                |
| json_dumps                 | 13.3 ms                                                | 10.6 ms: 1.26x faster                                                |
| richards_super             | 61.9 ms                                                | 51.7 ms: 1.20x faster                                                |
| nbody                      | 96.0 ms                                                | 81.4 ms: 1.18x faster                                                |
| chaos                      | 71.9 ms                                                | 61.6 ms: 1.17x faster                                                |
| coroutines                 | 27.0 ms                                                | 23.3 ms: 1.16x faster                                                |
| tomli_loads                | 2.30 sec                                               | 2.00 sec: 1.15x faster                                               |
| crypto_pyaes               | 76.7 ms                                                | 69.0 ms: 1.11x faster                                                |
| richards                   | 49.8 ms                                                | 45.0 ms: 1.11x faster                                                |
| logging_silent             | 111 ns                                                 | 101 ns: 1.10x faster                                                 |
| scimark_fft                | 345 ms                                                 | 316 ms: 1.09x faster                                                 |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.61 ms: 1.09x faster                                                |
| raytrace                   | 309 ms                                                 | 283 ms: 1.09x faster                                                 |
| fannkuch                   | 405 ms                                                 | 373 ms: 1.09x faster                                                 |
| scimark_monte_carlo        | 70.7 ms                                                | 65.2 ms: 1.08x faster                                                |
| spectral_norm              | 108 ms                                                 | 100 ms: 1.08x faster                                                 |
| deltablue                  | 3.92 ms                                                | 3.64 ms: 1.08x faster                                                |
| gc_traversal               | 4.01 ms                                                | 3.75 ms: 1.07x faster                                                |
| unpickle_pure_python       | 242 us                                                 | 227 us: 1.07x faster                                                 |
| logging_simple             | 6.22 us                                                | 5.84 us: 1.06x faster                                                |
| logging_format             | 6.81 us                                                | 6.49 us: 1.05x faster                                                |
| sympy_sum                  | 169 ms                                                 | 162 ms: 1.05x faster                                                 |
| pickle_pure_python         | 320 us                                                 | 307 us: 1.04x faster                                                 |
| deepcopy_memo              | 40.2 us                                                | 38.6 us: 1.04x faster                                                |
| sympy_str                  | 297 ms                                                 | 286 ms: 1.04x faster                                                 |
| pprint_pformat             | 1.55 sec                                               | 1.50 sec: 1.03x faster                                               |
| deepcopy                   | 365 us                                                 | 354 us: 1.03x faster                                                 |
| deepcopy_reduce            | 3.22 us                                                | 3.12 us: 1.03x faster                                                |
| pprint_safe_repr           | 747 ms                                                 | 726 ms: 1.03x faster                                                 |
| pidigits                   | 194 ms                                                 | 189 ms: 1.03x faster                                                 |
| mdp                        | 2.77 sec                                               | 2.70 sec: 1.03x faster                                               |
| json_loads                 | 29.2 us                                                | 28.4 us: 1.03x faster                                                |
| mako                       | 10.7 ms                                                | 10.4 ms: 1.03x faster                                                |
| hexiom                     | 6.89 ms                                                | 6.79 ms: 1.01x faster                                                |
| sympy_integrate            | 21.5 ms                                                | 21.3 ms: 1.01x faster                                                |
| unpickle_list              | 5.21 us                                                | 5.17 us: 1.01x faster                                                |
| meteor_contest             | 109 ms                                                 | 109 ms: 1.00x slower                                                 |
| sympy_expand               | 484 ms                                                 | 487 ms: 1.01x slower                                                 |
| sqlglot_parse              | 1.43 ms                                                | 1.45 ms: 1.01x slower                                                |
| pathlib                    | 18.5 ms                                                | 18.8 ms: 1.02x slower                                                |
| nqueens                    | 87.9 ms                                                | 89.4 ms: 1.02x slower                                                |
| bench_thread_pool          | 834 us                                                 | 856 us: 1.03x slower                                                 |
| tornado_http               | 98.1 ms                                                | 101 ms: 1.03x slower                                                 |
| asyncio_websockets         | 550 ms                                                 | 567 ms: 1.03x slower                                                 |
| create_gc_cycles           | 1.43 ms                                                | 1.49 ms: 1.04x slower                                                |
| thrift                     | 784 us                                                 | 816 us: 1.04x slower                                                 |
| pickle_dict                | 34.6 us                                                | 36.3 us: 1.05x slower                                                |
| chameleon                  | 6.70 ms                                                | 7.04 ms: 1.05x slower                                                |
| pyflate                    | 434 ms                                                 | 456 ms: 1.05x slower                                                 |
| sqlglot_transpile          | 1.75 ms                                                | 1.84 ms: 1.05x slower                                                |
| regex_effbot               | 3.51 ms                                                | 3.70 ms: 1.05x slower                                                |
| django_template            | 33.5 ms                                                | 35.5 ms: 1.06x slower                                                |
| sqlglot_optimize           | 55.3 ms                                                | 59.1 ms: 1.07x slower                                                |
| go                         | 149 ms                                                 | 159 ms: 1.07x slower                                                 |
| scimark_sor                | 121 ms                                                 | 132 ms: 1.09x slower                                                 |
| unpickle                   | 13.8 us                                                | 15.1 us: 1.09x slower                                                |
| pickle                     | 11.0 us                                                | 12.0 us: 1.09x slower                                                |
| scimark_lu                 | 116 ms                                                 | 127 ms: 1.09x slower                                                 |
| dulwich_log                | 64.6 ms                                                | 71.0 ms: 1.10x slower                                                |
| sqlite_synth               | 2.57 us                                                | 2.83 us: 1.10x slower                                                |
| regex_dna                  | 205 ms                                                 | 227 ms: 1.11x slower                                                 |
| genshi_text                | 22.5 ms                                                | 25.1 ms: 1.11x slower                                                |
| gunicorn                   | 1.20 ms                                                | 1.35 ms: 1.13x slower                                                |
| aiohttp                    | 1.12 ms                                                | 1.26 ms: 1.13x slower                                                |
| genshi_xml                 | 53.4 ms                                                | 60.5 ms: 1.13x slower                                                |
| pickle_list                | 4.59 us                                                | 5.20 us: 1.13x slower                                                |
| regex_v8                   | 22.9 ms                                                | 26.1 ms: 1.14x slower                                                |
| 2to3                       | 264 ms                                                 | 303 ms: 1.15x slower                                                 |
| html5lib                   | 64.8 ms                                                | 75.2 ms: 1.16x slower                                                |
| xml_etree_process          | 56.9 ms                                                | 68.3 ms: 1.20x slower                                                |
| xml_etree_generate         | 81.1 ms                                                | 99.2 ms: 1.22x slower                                                |
| telco                      | 6.86 ms                                                | 8.50 ms: 1.24x slower                                                |
| mypy2                      | 686 ms                                                 | 852 ms: 1.24x slower                                                 |
| coverage                   | 78.8 ms                                                | 99.1 ms: 1.26x slower                                                |
| pycparser                  | 1.19 sec                                               | 1.51 sec: 1.27x slower                                               |
| xml_etree_parse            | 164 ms                                                 | 219 ms: 1.33x slower                                                 |
| python_startup             | 8.56 ms                                                | 11.8 ms: 1.37x slower                                                |
| async_generators           | 374 ms                                                 | 557 ms: 1.49x slower                                                 |
| xml_etree_iterparse        | 108 ms                                                 | 162 ms: 1.50x slower                                                 |
| python_startup_no_site     | 6.01 ms                                                | 10.1 ms: 1.68x slower                                                |
| float                      | 78.9 ms                                                | 139 ms: 1.76x slower                                                 |
| docutils                   | 2.66 sec                                               | 4.82 sec: 1.81x slower                                               |
| dask                       | 365 ms                                                 | 766 ms: 2.10x slower                                                 |
| pylint                     | 476 ms                                                 | 1.01 sec: 2.13x slower                                               |
| unpack_sequence            | 43.5 ns                                                | 113 ns: 2.60x slower                                                 |
| async_tree_cpu_io_mixed    | 749 ms                                                 | 4.17 sec: 5.57x slower                                               |
| async_tree_cpu_io_mixed_tg | 761 ms                                                 | 4.57 sec: 6.00x slower                                               |
| async_tree_none            | 528 ms                                                 | 3.43 sec: 6.50x slower                                               |
| async_tree_memoization     | 639 ms                                                 | 4.43 sec: 6.93x slower                                               |
| async_tree_memoization_tg  | 626 ms                                                 | 4.71 sec: 7.52x slower                                               |
| async_tree_none_tg         | 491 ms                                                 | 3.75 sec: 7.63x slower                                               |
| async_tree_io              | 1.29 sec                                               | 13.3 sec: 10.31x slower                                              |
| async_tree_io_tg           | 1.29 sec                                               | 14.1 sec: 10.91x slower                                              |
| Geometric mean             | (ref)                                                  | 1.20x slower                                                         |

Benchmark hidden because not significant (5): json, sqlglot_normalize, regex_compile, djangocms, bench_mp_pool
Ignored benchmarks (3) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 98.86% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.00x


# Memory

- memory change: 1.13x