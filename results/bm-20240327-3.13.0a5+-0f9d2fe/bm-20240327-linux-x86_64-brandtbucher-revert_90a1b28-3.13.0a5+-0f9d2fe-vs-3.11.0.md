# Results vs. 3.11.0

- fork: brandtbucher
- ref: revert_90a1b28
- machine: linux-x86_64
- commit hash: 0f9d2fe
- commit date: 2024-03-27
- overall geometric mean: 1.08x faster
- HPT reliability: 99.91%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5+-0f9d2fe |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 264 ms                                                 | 267 ms: 1.01x slower                                                   |
| chameleon      | 6.70 ms                                                | 6.95 ms: 1.04x slower                                                  |
| docutils       | 2.66 sec                                               | 2.76 sec: 1.04x slower                                                 |
| html5lib       | 64.8 ms                                                | 65.7 ms: 1.01x slower                                                  |
| tornado_http   | 98.1 ms                                                | 95.0 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.01x slower                                                           |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5+-0f9d2fe |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization     | 639 ms                                                 | 442 ms: 1.45x faster                                                   |
| async_tree_memoization_tg  | 626 ms                                                 | 435 ms: 1.44x faster                                                   |
| async_tree_io_tg           | 1.29 sec                                               | 898 ms: 1.44x faster                                                   |
| async_tree_none            | 528 ms                                                 | 368 ms: 1.43x faster                                                   |
| async_tree_none_tg         | 491 ms                                                 | 343 ms: 1.43x faster                                                   |
| async_tree_io              | 1.29 sec                                               | 918 ms: 1.40x faster                                                   |
| async_tree_cpu_io_mixed_tg | 761 ms                                                 | 587 ms: 1.30x faster                                                   |
| async_tree_cpu_io_mixed    | 749 ms                                                 | 609 ms: 1.23x faster                                                   |
| Geometric mean             | (ref)                                                  | 1.39x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5+-0f9d2fe |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 96.0 ms                                                | 90.2 ms: 1.06x faster                                                  |
| float          | 78.9 ms                                                | 76.7 ms: 1.03x faster                                                  |
| pidigits       | 194 ms                                                 | 190 ms: 1.02x faster                                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5+-0f9d2fe |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 141 ms                                                 | 134 ms: 1.05x faster                                                   |
| regex_effbot   | 3.51 ms                                                | 3.71 ms: 1.06x slower                                                  |
| regex_dna      | 205 ms                                                 | 225 ms: 1.10x slower                                                   |
| regex_v8       | 22.9 ms                                                | 25.6 ms: 1.12x slower                                                  |
| Geometric mean | (ref)                                                  | 1.06x slower                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5+-0f9d2fe |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 13.3 ms                                                | 10.5 ms: 1.27x faster                                                  |
| unpickle_pure_python | 242 us                                                 | 222 us: 1.09x faster                                                   |
| pickle_pure_python   | 320 us                                                 | 299 us: 1.07x faster                                                   |
| tomli_loads          | 2.30 sec                                               | 2.17 sec: 1.06x faster                                                 |
| xml_etree_parse      | 164 ms                                                 | 160 ms: 1.02x faster                                                   |
| xml_etree_iterparse  | 108 ms                                                 | 106 ms: 1.02x faster                                                   |
| json_loads           | 29.2 us                                                | 28.8 us: 1.01x faster                                                  |
| unpickle_list        | 5.21 us                                                | 5.16 us: 1.01x faster                                                  |
| pickle_dict          | 34.6 us                                                | 34.3 us: 1.01x faster                                                  |
| xml_etree_process    | 56.9 ms                                                | 59.2 ms: 1.04x slower                                                  |
| xml_etree_generate   | 81.1 ms                                                | 85.8 ms: 1.06x slower                                                  |
| pickle               | 11.0 us                                                | 11.7 us: 1.06x slower                                                  |
| unpickle             | 13.8 us                                                | 14.9 us: 1.08x slower                                                  |
| pickle_list          | 4.59 us                                                | 4.97 us: 1.08x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5+-0f9d2fe |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 6.01 ms                                                | 6.89 ms: 1.15x slower                                                  |
| python_startup         | 8.56 ms                                                | 10.4 ms: 1.21x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.18x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5+-0f9d2fe |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 53.4 ms                                                | 51.7 ms: 1.03x faster                                                  |
| django_template | 33.5 ms                                                | 34.2 ms: 1.02x slower                                                  |
| mako            | 10.7 ms                                                | 10.9 ms: 1.02x slower                                                  |
| genshi_text     | 22.5 ms                                                | 24.5 ms: 1.09x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.02x slower                                                           |

All benchmarks:
===============

| Benchmark                  | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20240327-linux-x86_64-brandtbucher-revert_90a1b28-3.13.0a5+-0f9d2fe |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| typing_runtime_protocols   | 520 us                                                 | 112 us: 4.64x faster                                                   |
| generators                 | 74.9 ms                                                | 29.7 ms: 2.52x faster                                                  |
| asyncio_tcp                | 875 ms                                                 | 498 ms: 1.76x faster                                                   |
| asyncio_tcp_ssl            | 3.11 sec                                               | 1.84 sec: 1.69x faster                                                 |
| pylint                     | 476 ms                                                 | 318 ms: 1.50x faster                                                   |
| async_tree_memoization     | 639 ms                                                 | 442 ms: 1.45x faster                                                   |
| async_tree_memoization_tg  | 626 ms                                                 | 435 ms: 1.44x faster                                                   |
| async_tree_io_tg           | 1.29 sec                                               | 898 ms: 1.44x faster                                                   |
| comprehensions             | 23.6 us                                                | 16.5 us: 1.43x faster                                                  |
| async_tree_none            | 528 ms                                                 | 368 ms: 1.43x faster                                                   |
| async_tree_none_tg         | 491 ms                                                 | 343 ms: 1.43x faster                                                   |
| async_tree_io              | 1.29 sec                                               | 918 ms: 1.40x faster                                                   |
| async_tree_cpu_io_mixed_tg | 761 ms                                                 | 587 ms: 1.30x faster                                                   |
| json_dumps                 | 13.3 ms                                                | 10.5 ms: 1.27x faster                                                  |
| async_tree_cpu_io_mixed    | 749 ms                                                 | 609 ms: 1.23x faster                                                   |
| deltablue                  | 3.92 ms                                                | 3.24 ms: 1.21x faster                                                  |
| chaos                      | 71.9 ms                                                | 60.2 ms: 1.19x faster                                                  |
| coroutines                 | 27.0 ms                                                | 22.7 ms: 1.19x faster                                                  |
| richards_super             | 61.9 ms                                                | 52.2 ms: 1.19x faster                                                  |
| raytrace                   | 309 ms                                                 | 266 ms: 1.16x faster                                                   |
| sqlglot_parse              | 1.43 ms                                                | 1.27 ms: 1.13x faster                                                  |
| sqlglot_transpile          | 1.75 ms                                                | 1.57 ms: 1.11x faster                                                  |
| sympy_sum                  | 169 ms                                                 | 152 ms: 1.11x faster                                                   |
| logging_silent             | 111 ns                                                 | 101 ns: 1.10x faster                                                   |
| hexiom                     | 6.89 ms                                                | 6.29 ms: 1.10x faster                                                  |
| nqueens                    | 87.9 ms                                                | 80.3 ms: 1.09x faster                                                  |
| unpickle_pure_python       | 242 us                                                 | 222 us: 1.09x faster                                                   |
| sympy_str                  | 297 ms                                                 | 273 ms: 1.09x faster                                                   |
| mdp                        | 2.77 sec                                               | 2.57 sec: 1.08x faster                                                 |
| richards                   | 49.8 ms                                                | 46.3 ms: 1.07x faster                                                  |
| pickle_pure_python         | 320 us                                                 | 299 us: 1.07x faster                                                   |
| sympy_integrate            | 21.5 ms                                                | 20.1 ms: 1.07x faster                                                  |
| nbody                      | 96.0 ms                                                | 90.2 ms: 1.06x faster                                                  |
| tomli_loads                | 2.30 sec                                               | 2.17 sec: 1.06x faster                                                 |
| djangocms                  | 33.5 us                                                | 31.7 us: 1.06x faster                                                  |
| regex_compile              | 141 ms                                                 | 134 ms: 1.05x faster                                                   |
| go                         | 149 ms                                                 | 141 ms: 1.05x faster                                                   |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.80 ms: 1.05x faster                                                  |
| sympy_expand               | 484 ms                                                 | 462 ms: 1.05x faster                                                   |
| logging_simple             | 6.22 us                                                | 5.95 us: 1.05x faster                                                  |
| crypto_pyaes               | 76.7 ms                                                | 73.4 ms: 1.05x faster                                                  |
| scimark_monte_carlo        | 70.7 ms                                                | 67.7 ms: 1.04x faster                                                  |
| deepcopy_memo              | 40.2 us                                                | 38.5 us: 1.04x faster                                                  |
| logging_format             | 6.81 us                                                | 6.54 us: 1.04x faster                                                  |
| deepcopy                   | 365 us                                                 | 352 us: 1.04x faster                                                   |
| sqlglot_normalize          | 113 ms                                                 | 109 ms: 1.03x faster                                                   |
| genshi_xml                 | 53.4 ms                                                | 51.7 ms: 1.03x faster                                                  |
| pprint_pformat             | 1.55 sec                                               | 1.51 sec: 1.03x faster                                                 |
| tornado_http               | 98.1 ms                                                | 95.0 ms: 1.03x faster                                                  |
| float                      | 78.9 ms                                                | 76.7 ms: 1.03x faster                                                  |
| fannkuch                   | 405 ms                                                 | 394 ms: 1.03x faster                                                   |
| xml_etree_parse            | 164 ms                                                 | 160 ms: 1.02x faster                                                   |
| pidigits                   | 194 ms                                                 | 190 ms: 1.02x faster                                                   |
| xml_etree_iterparse        | 108 ms                                                 | 106 ms: 1.02x faster                                                   |
| pprint_safe_repr           | 747 ms                                                 | 735 ms: 1.02x faster                                                   |
| deepcopy_reduce            | 3.22 us                                                | 3.17 us: 1.02x faster                                                  |
| json_loads                 | 29.2 us                                                | 28.8 us: 1.01x faster                                                  |
| scimark_lu                 | 116 ms                                                 | 115 ms: 1.01x faster                                                   |
| sqlglot_optimize           | 55.3 ms                                                | 54.7 ms: 1.01x faster                                                  |
| unpickle_list              | 5.21 us                                                | 5.16 us: 1.01x faster                                                  |
| pickle_dict                | 34.6 us                                                | 34.3 us: 1.01x faster                                                  |
| bench_mp_pool              | 24.0 ms                                                | 23.8 ms: 1.01x faster                                                  |
| bench_thread_pool          | 834 us                                                 | 831 us: 1.00x faster                                                   |
| meteor_contest             | 109 ms                                                 | 109 ms: 1.00x faster                                                   |
| 2to3                       | 264 ms                                                 | 267 ms: 1.01x slower                                                   |
| scimark_sor                | 121 ms                                                 | 123 ms: 1.01x slower                                                   |
| html5lib                   | 64.8 ms                                                | 65.7 ms: 1.01x slower                                                  |
| json                       | 5.24 ms                                                | 5.33 ms: 1.02x slower                                                  |
| django_template            | 33.5 ms                                                | 34.2 ms: 1.02x slower                                                  |
| mako                       | 10.7 ms                                                | 10.9 ms: 1.02x slower                                                  |
| thrift                     | 784 us                                                 | 806 us: 1.03x slower                                                   |
| asyncio_websockets         | 550 ms                                                 | 569 ms: 1.03x slower                                                   |
| docutils                   | 2.66 sec                                               | 2.76 sec: 1.04x slower                                                 |
| chameleon                  | 6.70 ms                                                | 6.95 ms: 1.04x slower                                                  |
| xml_etree_process          | 56.9 ms                                                | 59.2 ms: 1.04x slower                                                  |
| dulwich_log                | 64.6 ms                                                | 67.5 ms: 1.04x slower                                                  |
| aiohttp                    | 1.12 ms                                                | 1.17 ms: 1.05x slower                                                  |
| xml_etree_generate         | 81.1 ms                                                | 85.8 ms: 1.06x slower                                                  |
| regex_effbot               | 3.51 ms                                                | 3.71 ms: 1.06x slower                                                  |
| scimark_fft                | 345 ms                                                 | 366 ms: 1.06x slower                                                   |
| pickle                     | 11.0 us                                                | 11.7 us: 1.06x slower                                                  |
| gunicorn                   | 1.20 ms                                                | 1.28 ms: 1.07x slower                                                  |
| pyflate                    | 434 ms                                                 | 463 ms: 1.07x slower                                                   |
| mypy2                      | 686 ms                                                 | 735 ms: 1.07x slower                                                   |
| unpickle                   | 13.8 us                                                | 14.9 us: 1.08x slower                                                  |
| pickle_list                | 4.59 us                                                | 4.97 us: 1.08x slower                                                  |
| genshi_text                | 22.5 ms                                                | 24.5 ms: 1.09x slower                                                  |
| regex_dna                  | 205 ms                                                 | 225 ms: 1.10x slower                                                   |
| regex_v8                   | 22.9 ms                                                | 25.6 ms: 1.12x slower                                                  |
| sqlite_synth               | 2.57 us                                                | 2.93 us: 1.14x slower                                                  |
| python_startup_no_site     | 6.01 ms                                                | 6.89 ms: 1.15x slower                                                  |
| create_gc_cycles           | 1.43 ms                                                | 1.67 ms: 1.16x slower                                                  |
| async_generators           | 374 ms                                                 | 445 ms: 1.19x slower                                                   |
| coverage                   | 78.8 ms                                                | 95.5 ms: 1.21x slower                                                  |
| python_startup             | 8.56 ms                                                | 10.4 ms: 1.21x slower                                                  |
| telco                      | 6.86 ms                                                | 8.45 ms: 1.23x slower                                                  |
| unpack_sequence            | 43.5 ns                                                | 54.5 ns: 1.25x slower                                                  |
| Geometric mean             | (ref)                                                  | 1.08x faster                                                           |

Benchmark hidden because not significant (5): pathlib, pycparser, gc_traversal, spectral_norm, dask
Ignored benchmarks (3) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: flaskblogging, sqlalchemy_declarative, sqlalchemy_imperative


# HPT report

- Reliability score: 99.91% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x


# Memory

- memory change: 1.01x