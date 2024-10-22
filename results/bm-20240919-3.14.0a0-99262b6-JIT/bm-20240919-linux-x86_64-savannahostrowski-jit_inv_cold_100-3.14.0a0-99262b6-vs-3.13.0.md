# Results vs. 3.13.0

- fork: savannahostrowski
- ref: jit_inv_cold_100
- machine: linux-x86_64
- commit hash: 99262b6
- commit date: 2024-09-19
- overall geometric mean: 1.02x slower
- HPT reliability: 82.67%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 318 ms: 1.20x slower                                                         |
| docutils       | 2.58 sec                                               | 2.70 sec: 1.05x slower                                                       |
| html5lib       | 64.5 ms                                                | 63.2 ms: 1.02x faster                                                        |
| tornado_http   | 91.5 ms                                                | 110 ms: 1.20x slower                                                         |
| Geometric mean | (ref)                                                  | 1.10x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 390 ms: 1.19x faster                                                         |
| async_tree_none            | 354 ms                                                 | 322 ms: 1.10x faster                                                         |
| async_tree_memoization     | 442 ms                                                 | 403 ms: 1.10x faster                                                         |
| async_tree_none_tg         | 320 ms                                                 | 306 ms: 1.05x faster                                                         |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.82 sec: 1.02x slower                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 554 ms: 1.02x slower                                                         |
| asyncio_tcp                | 488 ms                                                 | 504 ms: 1.03x slower                                                         |
| coroutines                 | 22.5 ms                                                | 23.3 ms: 1.03x slower                                                        |
| async_generators           | 433 ms                                                 | 454 ms: 1.05x slower                                                         |
| async_tree_io              | 843 ms                                                 | 892 ms: 1.06x slower                                                         |
| async_tree_io_tg           | 825 ms                                                 | 875 ms: 1.06x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 71.3 ms: 1.10x faster                                                        |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                 |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.62 ms: 1.07x faster                                                        |
| regex_dna      | 220 ms                                                 | 215 ms: 1.02x faster                                                         |
| regex_compile  | 131 ms                                                 | 130 ms: 1.01x faster                                                         |
| regex_v8       | 25.3 ms                                                | 26.4 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 156 ms                                                 | 146 ms: 1.07x faster                                                         |
| unpickle             | 14.9 us                                                | 14.5 us: 1.03x faster                                                        |
| xml_etree_iterparse  | 102 ms                                                 | 99.7 ms: 1.02x faster                                                        |
| xml_etree_process    | 60.4 ms                                                | 59.3 ms: 1.02x faster                                                        |
| json_dumps           | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                        |
| xml_etree_generate   | 87.0 ms                                                | 85.6 ms: 1.02x faster                                                        |
| json_loads           | 27.0 us                                                | 26.8 us: 1.01x faster                                                        |
| pickle               | 11.6 us                                                | 11.8 us: 1.02x slower                                                        |
| unpickle_pure_python | 213 us                                                 | 220 us: 1.03x slower                                                         |
| pickle_list          | 5.01 us                                                | 5.17 us: 1.03x slower                                                        |
| unpickle_list        | 4.96 us                                                | 5.26 us: 1.06x slower                                                        |
| pickle_dict          | 33.2 us                                                | 35.4 us: 1.07x slower                                                        |
| pickle_pure_python   | 300 us                                                 | 331 us: 1.10x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                        |
| python_startup_no_site | 6.99 ms                                                | 7.05 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.1 ms: 1.10x faster                                                        |
| genshi_text     | 22.9 ms                                                | 24.3 ms: 1.06x slower                                                        |
| django_template | 34.4 ms                                                | 38.4 ms: 1.12x slower                                                        |
| genshi_xml      | 50.3 ms                                                | 57.8 ms: 1.15x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.06x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240919-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-99262b6 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 27.5 us: 1.38x faster                                                        |
| deepcopy                   | 352 us                                                 | 270 us: 1.31x faster                                                         |
| deepcopy_reduce            | 3.17 us                                                | 2.64 us: 1.20x faster                                                        |
| async_tree_memoization_tg  | 465 ms                                                 | 390 ms: 1.19x faster                                                         |
| go                         | 142 ms                                                 | 122 ms: 1.16x faster                                                         |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.47 ms: 1.12x faster                                                        |
| async_tree_none            | 354 ms                                                 | 322 ms: 1.10x faster                                                         |
| float                      | 78.5 ms                                                | 71.3 ms: 1.10x faster                                                        |
| mako                       | 11.1 ms                                                | 10.1 ms: 1.10x faster                                                        |
| async_tree_memoization     | 442 ms                                                 | 403 ms: 1.10x faster                                                         |
| crypto_pyaes               | 73.0 ms                                                | 67.5 ms: 1.08x faster                                                        |
| regex_effbot               | 3.88 ms                                                | 3.62 ms: 1.07x faster                                                        |
| xml_etree_parse            | 156 ms                                                 | 146 ms: 1.07x faster                                                         |
| json                       | 5.20 ms                                                | 4.94 ms: 1.05x faster                                                        |
| spectral_norm              | 115 ms                                                 | 110 ms: 1.05x faster                                                         |
| telco                      | 8.45 ms                                                | 8.08 ms: 1.05x faster                                                        |
| pathlib                    | 17.1 ms                                                | 16.3 ms: 1.05x faster                                                        |
| async_tree_none_tg         | 320 ms                                                 | 306 ms: 1.05x faster                                                         |
| scimark_sor                | 122 ms                                                 | 118 ms: 1.04x faster                                                         |
| sqlite_synth               | 2.85 us                                                | 2.75 us: 1.03x faster                                                        |
| unpickle                   | 14.9 us                                                | 14.5 us: 1.03x faster                                                        |
| xml_etree_iterparse        | 102 ms                                                 | 99.7 ms: 1.02x faster                                                        |
| richards_super             | 54.4 ms                                                | 53.2 ms: 1.02x faster                                                        |
| regex_dna                  | 220 ms                                                 | 215 ms: 1.02x faster                                                         |
| html5lib                   | 64.5 ms                                                | 63.2 ms: 1.02x faster                                                        |
| scimark_lu                 | 115 ms                                                 | 113 ms: 1.02x faster                                                         |
| xml_etree_process          | 60.4 ms                                                | 59.3 ms: 1.02x faster                                                        |
| json_dumps                 | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                        |
| pprint_safe_repr           | 744 ms                                                 | 732 ms: 1.02x faster                                                         |
| mdp                        | 2.74 sec                                               | 2.70 sec: 1.02x faster                                                       |
| xml_etree_generate         | 87.0 ms                                                | 85.6 ms: 1.02x faster                                                        |
| pprint_pformat             | 1.51 sec                                               | 1.49 sec: 1.02x faster                                                       |
| pycparser                  | 1.19 sec                                               | 1.18 sec: 1.01x faster                                                       |
| thrift                     | 796 us                                                 | 788 us: 1.01x faster                                                         |
| regex_compile              | 131 ms                                                 | 130 ms: 1.01x faster                                                         |
| scimark_fft                | 369 ms                                                 | 366 ms: 1.01x faster                                                         |
| python_startup             | 10.6 ms                                                | 10.5 ms: 1.01x faster                                                        |
| json_loads                 | 27.0 us                                                | 26.8 us: 1.01x faster                                                        |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| comprehensions             | 16.4 us                                                | 16.5 us: 1.00x slower                                                        |
| python_startup_no_site     | 6.99 ms                                                | 7.05 ms: 1.01x slower                                                        |
| logging_simple             | 5.66 us                                                | 5.74 us: 1.01x slower                                                        |
| coverage                   | 83.7 ms                                                | 84.9 ms: 1.01x slower                                                        |
| pyflate                    | 460 ms                                                 | 466 ms: 1.01x slower                                                         |
| pickle                     | 11.6 us                                                | 11.8 us: 1.02x slower                                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.82 sec: 1.02x slower                                                       |
| sympy_expand               | 462 ms                                                 | 470 ms: 1.02x slower                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 554 ms: 1.02x slower                                                         |
| fannkuch                   | 381 ms                                                 | 389 ms: 1.02x slower                                                         |
| unpickle_pure_python       | 213 us                                                 | 220 us: 1.03x slower                                                         |
| asyncio_tcp                | 488 ms                                                 | 504 ms: 1.03x slower                                                         |
| pickle_list                | 5.01 us                                                | 5.17 us: 1.03x slower                                                        |
| coroutines                 | 22.5 ms                                                | 23.3 ms: 1.03x slower                                                        |
| bpe_tokeniser              | 4.69 sec                                               | 4.86 sec: 1.04x slower                                                       |
| sympy_str                  | 274 ms                                                 | 284 ms: 1.04x slower                                                         |
| gc_traversal               | 3.81 ms                                                | 3.96 ms: 1.04x slower                                                        |
| sqlglot_parse              | 1.27 ms                                                | 1.32 ms: 1.04x slower                                                        |
| regex_v8                   | 25.3 ms                                                | 26.4 ms: 1.04x slower                                                        |
| docutils                   | 2.58 sec                                               | 2.70 sec: 1.05x slower                                                       |
| typing_runtime_protocols   | 159 us                                                 | 167 us: 1.05x slower                                                         |
| meteor_contest             | 108 ms                                                 | 113 ms: 1.05x slower                                                         |
| async_generators           | 433 ms                                                 | 454 ms: 1.05x slower                                                         |
| sympy_sum                  | 150 ms                                                 | 157 ms: 1.05x slower                                                         |
| raytrace                   | 262 ms                                                 | 275 ms: 1.05x slower                                                         |
| async_tree_io              | 843 ms                                                 | 892 ms: 1.06x slower                                                         |
| unpickle_list              | 4.96 us                                                | 5.26 us: 1.06x slower                                                        |
| async_tree_io_tg           | 825 ms                                                 | 875 ms: 1.06x slower                                                         |
| genshi_text                | 22.9 ms                                                | 24.3 ms: 1.06x slower                                                        |
| pickle_dict                | 33.2 us                                                | 35.4 us: 1.07x slower                                                        |
| chaos                      | 58.4 ms                                                | 62.5 ms: 1.07x slower                                                        |
| create_gc_cycles           | 1.61 ms                                                | 1.74 ms: 1.08x slower                                                        |
| sqlglot_normalize          | 107 ms                                                 | 116 ms: 1.08x slower                                                         |
| nqueens                    | 80.6 ms                                                | 87.5 ms: 1.09x slower                                                        |
| dulwich_log                | 63.0 ms                                                | 69.2 ms: 1.10x slower                                                        |
| pickle_pure_python         | 300 us                                                 | 331 us: 1.10x slower                                                         |
| hexiom                     | 6.13 ms                                                | 6.81 ms: 1.11x slower                                                        |
| django_template            | 34.4 ms                                                | 38.4 ms: 1.12x slower                                                        |
| sqlglot_optimize           | 53.9 ms                                                | 60.1 ms: 1.12x slower                                                        |
| deltablue                  | 3.15 ms                                                | 3.58 ms: 1.14x slower                                                        |
| bench_thread_pool          | 815 us                                                 | 928 us: 1.14x slower                                                         |
| genshi_xml                 | 50.3 ms                                                | 57.8 ms: 1.15x slower                                                        |
| sqlglot_transpile          | 1.57 ms                                                | 1.83 ms: 1.17x slower                                                        |
| tornado_http               | 91.5 ms                                                | 110 ms: 1.20x slower                                                         |
| pylint                     | 313 ms                                                 | 376 ms: 1.20x slower                                                         |
| 2to3                       | 265 ms                                                 | 318 ms: 1.20x slower                                                         |
| generators                 | 28.8 ms                                                | 36.8 ms: 1.28x slower                                                        |
| sympy_integrate            | 19.9 ms                                                | 28.0 ms: 1.41x slower                                                        |
| unpack_sequence            | 42.4 ns                                                | 110 ns: 2.59x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.02x slower                                                                 |

Benchmark hidden because not significant (9): async_tree_cpu_io_mixed, scimark_monte_carlo, nbody, asyncio_websockets, logging_format, tomli_loads, bench_mp_pool, logging_silent, richards
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 82.67% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.04x