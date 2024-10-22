# Results vs. 3.13.0

- fork: savannahostrowski
- ref: jit_inv_cold_100
- machine: linux-x86_64
- commit hash: 0ee16f5
- commit date: 2024-09-23
- overall geometric mean: 1.03x slower
- HPT reliability: 99.04%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.04x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 318 ms: 1.20x slower                                                         |
| docutils       | 2.58 sec                                               | 2.72 sec: 1.05x slower                                                       |
| html5lib       | 64.5 ms                                                | 65.4 ms: 1.01x slower                                                        |
| tornado_http   | 91.5 ms                                                | 110 ms: 1.20x slower                                                         |
| Geometric mean | (ref)                                                  | 1.11x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 390 ms: 1.19x faster                                                         |
| async_tree_none            | 354 ms                                                 | 319 ms: 1.11x faster                                                         |
| async_tree_memoization     | 442 ms                                                 | 407 ms: 1.09x faster                                                         |
| async_tree_none_tg         | 320 ms                                                 | 307 ms: 1.04x faster                                                         |
| asyncio_websockets         | 555 ms                                                 | 560 ms: 1.01x slower                                                         |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.82 sec: 1.01x slower                                                       |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 557 ms: 1.03x slower                                                         |
| coroutines                 | 22.5 ms                                                | 23.2 ms: 1.03x slower                                                        |
| asyncio_tcp                | 488 ms                                                 | 505 ms: 1.03x slower                                                         |
| async_tree_io              | 843 ms                                                 | 892 ms: 1.06x slower                                                         |
| async_tree_io_tg           | 825 ms                                                 | 874 ms: 1.06x slower                                                         |
| async_generators           | 433 ms                                                 | 460 ms: 1.06x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 78.5 ms                                                | 70.9 ms: 1.11x faster                                                        |
| nbody          | 85.7 ms                                                | 80.6 ms: 1.06x faster                                                        |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.65 ms: 1.06x faster                                                        |
| regex_dna      | 220 ms                                                 | 221 ms: 1.01x slower                                                         |
| regex_v8       | 25.3 ms                                                | 27.3 ms: 1.08x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                 |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 156 ms                                                 | 149 ms: 1.05x faster                                                         |
| xml_etree_iterparse  | 102 ms                                                 | 100.0 ms: 1.02x faster                                                       |
| json_dumps           | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                        |
| pickle               | 11.6 us                                                | 11.5 us: 1.01x faster                                                        |
| xml_etree_process    | 60.4 ms                                                | 61.2 ms: 1.01x slower                                                        |
| json_loads           | 27.0 us                                                | 27.3 us: 1.01x slower                                                        |
| tomli_loads          | 2.11 sec                                               | 2.14 sec: 1.02x slower                                                       |
| pickle_list          | 5.01 us                                                | 5.11 us: 1.02x slower                                                        |
| xml_etree_generate   | 87.0 ms                                                | 88.8 ms: 1.02x slower                                                        |
| unpickle_pure_python | 213 us                                                 | 220 us: 1.03x slower                                                         |
| unpickle_list        | 4.96 us                                                | 5.25 us: 1.06x slower                                                        |
| pickle_dict          | 33.2 us                                                | 35.2 us: 1.06x slower                                                        |
| pickle_pure_python   | 300 us                                                 | 332 us: 1.11x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                                 |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                        |
| python_startup_no_site | 6.99 ms                                                | 7.10 ms: 1.02x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.5 ms: 1.06x faster                                                        |
| genshi_text     | 22.9 ms                                                | 24.5 ms: 1.07x slower                                                        |
| django_template | 34.4 ms                                                | 37.1 ms: 1.08x slower                                                        |
| genshi_xml      | 50.3 ms                                                | 58.3 ms: 1.16x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.06x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy_memo              | 38.0 us                                                | 27.8 us: 1.37x faster                                                        |
| deepcopy                   | 352 us                                                 | 272 us: 1.29x faster                                                         |
| deepcopy_reduce            | 3.17 us                                                | 2.64 us: 1.20x faster                                                        |
| async_tree_memoization_tg  | 465 ms                                                 | 390 ms: 1.19x faster                                                         |
| go                         | 142 ms                                                 | 122 ms: 1.16x faster                                                         |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.45 ms: 1.13x faster                                                        |
| async_tree_none            | 354 ms                                                 | 319 ms: 1.11x faster                                                         |
| float                      | 78.5 ms                                                | 70.9 ms: 1.11x faster                                                        |
| async_tree_memoization     | 442 ms                                                 | 407 ms: 1.09x faster                                                         |
| crypto_pyaes               | 73.0 ms                                                | 67.7 ms: 1.08x faster                                                        |
| mdp                        | 2.74 sec                                               | 2.57 sec: 1.07x faster                                                       |
| regex_effbot               | 3.88 ms                                                | 3.65 ms: 1.06x faster                                                        |
| nbody                      | 85.7 ms                                                | 80.6 ms: 1.06x faster                                                        |
| mako                       | 11.1 ms                                                | 10.5 ms: 1.06x faster                                                        |
| spectral_norm              | 115 ms                                                 | 110 ms: 1.05x faster                                                         |
| xml_etree_parse            | 156 ms                                                 | 149 ms: 1.05x faster                                                         |
| scimark_sor                | 122 ms                                                 | 117 ms: 1.05x faster                                                         |
| telco                      | 8.45 ms                                                | 8.09 ms: 1.04x faster                                                        |
| pathlib                    | 17.1 ms                                                | 16.3 ms: 1.04x faster                                                        |
| async_tree_none_tg         | 320 ms                                                 | 307 ms: 1.04x faster                                                         |
| sqlite_synth               | 2.85 us                                                | 2.74 us: 1.04x faster                                                        |
| richards_super             | 54.4 ms                                                | 52.9 ms: 1.03x faster                                                        |
| xml_etree_iterparse        | 102 ms                                                 | 100.0 ms: 1.02x faster                                                       |
| json                       | 5.20 ms                                                | 5.09 ms: 1.02x faster                                                        |
| json_dumps                 | 10.4 ms                                                | 10.2 ms: 1.02x faster                                                        |
| pprint_safe_repr           | 744 ms                                                 | 732 ms: 1.02x faster                                                         |
| scimark_lu                 | 115 ms                                                 | 113 ms: 1.02x faster                                                         |
| scimark_monte_carlo        | 66.3 ms                                                | 65.5 ms: 1.01x faster                                                        |
| scimark_fft                | 369 ms                                                 | 365 ms: 1.01x faster                                                         |
| pprint_pformat             | 1.51 sec                                               | 1.50 sec: 1.01x faster                                                       |
| pickle                     | 11.6 us                                                | 11.5 us: 1.01x faster                                                        |
| python_startup             | 10.6 ms                                                | 10.6 ms: 1.00x slower                                                        |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                                         |
| regex_dna                  | 220 ms                                                 | 221 ms: 1.01x slower                                                         |
| asyncio_websockets         | 555 ms                                                 | 560 ms: 1.01x slower                                                         |
| coverage                   | 83.7 ms                                                | 84.6 ms: 1.01x slower                                                        |
| xml_etree_process          | 60.4 ms                                                | 61.2 ms: 1.01x slower                                                        |
| json_loads                 | 27.0 us                                                | 27.3 us: 1.01x slower                                                        |
| html5lib                   | 64.5 ms                                                | 65.4 ms: 1.01x slower                                                        |
| asyncio_tcp_ssl            | 1.79 sec                                               | 1.82 sec: 1.01x slower                                                       |
| pycparser                  | 1.19 sec                                               | 1.21 sec: 1.01x slower                                                       |
| tomli_loads                | 2.11 sec                                               | 2.14 sec: 1.02x slower                                                       |
| python_startup_no_site     | 6.99 ms                                                | 7.10 ms: 1.02x slower                                                        |
| pickle_list                | 5.01 us                                                | 5.11 us: 1.02x slower                                                        |
| xml_etree_generate         | 87.0 ms                                                | 88.8 ms: 1.02x slower                                                        |
| logging_simple             | 5.66 us                                                | 5.79 us: 1.02x slower                                                        |
| comprehensions             | 16.4 us                                                | 16.8 us: 1.02x slower                                                        |
| fannkuch                   | 381 ms                                                 | 390 ms: 1.02x slower                                                         |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 557 ms: 1.03x slower                                                         |
| sympy_expand               | 462 ms                                                 | 474 ms: 1.03x slower                                                         |
| coroutines                 | 22.5 ms                                                | 23.2 ms: 1.03x slower                                                        |
| unpickle_pure_python       | 213 us                                                 | 220 us: 1.03x slower                                                         |
| gc_traversal               | 3.81 ms                                                | 3.93 ms: 1.03x slower                                                        |
| asyncio_tcp                | 488 ms                                                 | 505 ms: 1.03x slower                                                         |
| bpe_tokeniser              | 4.69 sec                                               | 4.88 sec: 1.04x slower                                                       |
| typing_runtime_protocols   | 159 us                                                 | 166 us: 1.04x slower                                                         |
| sympy_str                  | 274 ms                                                 | 287 ms: 1.05x slower                                                         |
| raytrace                   | 262 ms                                                 | 274 ms: 1.05x slower                                                         |
| docutils                   | 2.58 sec                                               | 2.72 sec: 1.05x slower                                                       |
| meteor_contest             | 108 ms                                                 | 113 ms: 1.05x slower                                                         |
| chaos                      | 58.4 ms                                                | 61.6 ms: 1.05x slower                                                        |
| pyflate                    | 460 ms                                                 | 486 ms: 1.06x slower                                                         |
| async_tree_io              | 843 ms                                                 | 892 ms: 1.06x slower                                                         |
| unpickle_list              | 4.96 us                                                | 5.25 us: 1.06x slower                                                        |
| async_tree_io_tg           | 825 ms                                                 | 874 ms: 1.06x slower                                                         |
| sqlglot_parse              | 1.27 ms                                                | 1.34 ms: 1.06x slower                                                        |
| sympy_sum                  | 150 ms                                                 | 159 ms: 1.06x slower                                                         |
| pickle_dict                | 33.2 us                                                | 35.2 us: 1.06x slower                                                        |
| async_generators           | 433 ms                                                 | 460 ms: 1.06x slower                                                         |
| genshi_text                | 22.9 ms                                                | 24.5 ms: 1.07x slower                                                        |
| django_template            | 34.4 ms                                                | 37.1 ms: 1.08x slower                                                        |
| create_gc_cycles           | 1.61 ms                                                | 1.73 ms: 1.08x slower                                                        |
| regex_v8                   | 25.3 ms                                                | 27.3 ms: 1.08x slower                                                        |
| nqueens                    | 80.6 ms                                                | 87.1 ms: 1.08x slower                                                        |
| sqlglot_normalize          | 107 ms                                                 | 116 ms: 1.08x slower                                                         |
| dulwich_log                | 63.0 ms                                                | 69.1 ms: 1.10x slower                                                        |
| pickle_pure_python         | 300 us                                                 | 332 us: 1.11x slower                                                         |
| hexiom                     | 6.13 ms                                                | 6.84 ms: 1.12x slower                                                        |
| sqlglot_optimize           | 53.9 ms                                                | 60.3 ms: 1.12x slower                                                        |
| deltablue                  | 3.15 ms                                                | 3.58 ms: 1.14x slower                                                        |
| bench_thread_pool          | 815 us                                                 | 932 us: 1.14x slower                                                         |
| genshi_xml                 | 50.3 ms                                                | 58.3 ms: 1.16x slower                                                        |
| sqlglot_transpile          | 1.57 ms                                                | 1.85 ms: 1.18x slower                                                        |
| tornado_http               | 91.5 ms                                                | 110 ms: 1.20x slower                                                         |
| 2to3                       | 265 ms                                                 | 318 ms: 1.20x slower                                                         |
| pylint                     | 313 ms                                                 | 377 ms: 1.20x slower                                                         |
| generators                 | 28.8 ms                                                | 35.5 ms: 1.23x slower                                                        |
| sympy_integrate            | 19.9 ms                                                | 28.1 ms: 1.41x slower                                                        |
| unpack_sequence            | 42.4 ns                                                | 109 ns: 2.56x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.03x slower                                                                 |

Benchmark hidden because not significant (8): richards, logging_silent, async_tree_cpu_io_mixed, bench_mp_pool, thrift, regex_compile, logging_format, unpickle
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2

# HPT report

- Reliability score: 99.04% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.04x