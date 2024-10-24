# Results vs. 3.13.0

- fork: savannahostrowski
- ref: remove_ghccc
- machine: linux-x86_64
- commit hash: 9827ade
- commit date: 2024-10-16
- overall geometric mean: 1.03x slower
- HPT reliability: 70.53%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 265 ms                                                 | 278 ms: 1.05x slower                                                      |
| docutils       | 2.58 sec                                               | 2.91 sec: 1.12x slower                                                    |
| html5lib       | 64.5 ms                                                | 65.5 ms: 1.01x slower                                                     |
| tornado_http   | 91.5 ms                                                | 93.2 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                  | 1.05x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 465 ms                                                 | 375 ms: 1.24x faster                                                      |
| async_tree_none            | 354 ms                                                 | 326 ms: 1.09x faster                                                      |
| async_tree_memoization     | 442 ms                                                 | 414 ms: 1.07x faster                                                      |
| asyncio_tcp                | 488 ms                                                 | 493 ms: 1.01x slower                                                      |
| coroutines                 | 22.5 ms                                                | 22.8 ms: 1.01x slower                                                     |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 561 ms: 1.03x slower                                                      |
| async_generators           | 433 ms                                                 | 458 ms: 1.06x slower                                                      |
| async_tree_io_tg           | 825 ms                                                 | 976 ms: 1.18x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (5): async_tree_none_tg, asyncio_tcp_ssl, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 85.7 ms                                                | 82.1 ms: 1.04x faster                                                     |
| float          | 78.5 ms                                                | 75.9 ms: 1.03x faster                                                     |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x slower                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_effbot   | 3.88 ms                                                | 3.62 ms: 1.07x faster                                                     |
| regex_dna      | 220 ms                                                 | 208 ms: 1.06x faster                                                      |
| regex_v8       | 25.3 ms                                                | 24.1 ms: 1.05x faster                                                     |
| regex_compile  | 131 ms                                                 | 141 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_generate   | 87.0 ms                                                | 79.0 ms: 1.10x faster                                                     |
| xml_etree_process    | 60.4 ms                                                | 55.5 ms: 1.09x faster                                                     |
| tomli_loads          | 2.11 sec                                               | 1.95 sec: 1.08x faster                                                    |
| xml_etree_parse      | 156 ms                                                 | 149 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 102 ms                                                 | 99.8 ms: 1.02x faster                                                     |
| unpickle_pure_python | 213 us                                                 | 217 us: 1.02x slower                                                      |
| pickle_pure_python   | 300 us                                                 | 309 us: 1.03x slower                                                      |
| pickle               | 11.6 us                                                | 12.0 us: 1.04x slower                                                     |
| pickle_list          | 5.01 us                                                | 5.28 us: 1.05x slower                                                     |
| json_dumps           | 10.4 ms                                                | 11.1 ms: 1.07x slower                                                     |
| pickle_dict          | 33.2 us                                                | 35.9 us: 1.08x slower                                                     |
| unpickle_list        | 4.96 us                                                | 5.47 us: 1.10x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (2): unpickle, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.99 ms                                                | 7.06 ms: 1.01x slower                                                     |
| python_startup         | 10.6 ms                                                | 11.9 ms: 1.12x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.3 ms: 1.08x faster                                                     |
| django_template | 34.4 ms                                                | 36.3 ms: 1.05x slower                                                     |
| genshi_text     | 22.9 ms                                                | 26.1 ms: 1.14x slower                                                     |
| genshi_xml      | 50.3 ms                                                | 61.7 ms: 1.23x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.08x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy                   | 352 us                                                 | 274 us: 1.29x faster                                                      |
| deepcopy_memo              | 38.0 us                                                | 29.8 us: 1.27x faster                                                     |
| async_tree_memoization_tg  | 465 ms                                                 | 375 ms: 1.24x faster                                                      |
| richards                   | 48.1 ms                                                | 41.2 ms: 1.17x faster                                                     |
| scimark_fft                | 369 ms                                                 | 317 ms: 1.16x faster                                                      |
| deepcopy_reduce            | 3.17 us                                                | 2.74 us: 1.16x faster                                                     |
| richards_super             | 54.4 ms                                                | 47.5 ms: 1.15x faster                                                     |
| telco                      | 8.45 ms                                                | 7.61 ms: 1.11x faster                                                     |
| xml_etree_generate         | 87.0 ms                                                | 79.0 ms: 1.10x faster                                                     |
| scimark_sparse_mat_mult    | 5.03 ms                                                | 4.61 ms: 1.09x faster                                                     |
| async_tree_none            | 354 ms                                                 | 326 ms: 1.09x faster                                                      |
| crypto_pyaes               | 73.0 ms                                                | 67.1 ms: 1.09x faster                                                     |
| xml_etree_process          | 60.4 ms                                                | 55.5 ms: 1.09x faster                                                     |
| tomli_loads                | 2.11 sec                                               | 1.95 sec: 1.08x faster                                                    |
| mako                       | 11.1 ms                                                | 10.3 ms: 1.08x faster                                                     |
| regex_effbot               | 3.88 ms                                                | 3.62 ms: 1.07x faster                                                     |
| async_tree_memoization     | 442 ms                                                 | 414 ms: 1.07x faster                                                      |
| pathlib                    | 17.1 ms                                                | 16.0 ms: 1.06x faster                                                     |
| mdp                        | 2.74 sec                                               | 2.59 sec: 1.06x faster                                                    |
| go                         | 142 ms                                                 | 134 ms: 1.06x faster                                                      |
| regex_dna                  | 220 ms                                                 | 208 ms: 1.06x faster                                                      |
| bpe_tokeniser              | 4.69 sec                                               | 4.46 sec: 1.05x faster                                                    |
| xml_etree_parse            | 156 ms                                                 | 149 ms: 1.05x faster                                                      |
| regex_v8                   | 25.3 ms                                                | 24.1 ms: 1.05x faster                                                     |
| json                       | 5.20 ms                                                | 4.96 ms: 1.05x faster                                                     |
| logging_silent             | 102 ns                                                 | 97.7 ns: 1.04x faster                                                     |
| nbody                      | 85.7 ms                                                | 82.1 ms: 1.04x faster                                                     |
| float                      | 78.5 ms                                                | 75.9 ms: 1.03x faster                                                     |
| scimark_lu                 | 115 ms                                                 | 111 ms: 1.03x faster                                                      |
| pycparser                  | 1.19 sec                                               | 1.16 sec: 1.03x faster                                                    |
| logging_simple             | 5.66 us                                                | 5.51 us: 1.03x faster                                                     |
| scimark_sor                | 122 ms                                                 | 119 ms: 1.03x faster                                                      |
| logging_format             | 6.25 us                                                | 6.09 us: 1.03x faster                                                     |
| sqlite_synth               | 2.85 us                                                | 2.78 us: 1.02x faster                                                     |
| pyflate                    | 460 ms                                                 | 449 ms: 1.02x faster                                                      |
| xml_etree_iterparse        | 102 ms                                                 | 99.8 ms: 1.02x faster                                                     |
| scimark_monte_carlo        | 66.3 ms                                                | 65.1 ms: 1.02x faster                                                     |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x slower                                                      |
| chaos                      | 58.4 ms                                                | 58.9 ms: 1.01x slower                                                     |
| asyncio_tcp                | 488 ms                                                 | 493 ms: 1.01x slower                                                      |
| coverage                   | 83.7 ms                                                | 84.5 ms: 1.01x slower                                                     |
| fannkuch                   | 381 ms                                                 | 385 ms: 1.01x slower                                                      |
| python_startup_no_site     | 6.99 ms                                                | 7.06 ms: 1.01x slower                                                     |
| coroutines                 | 22.5 ms                                                | 22.8 ms: 1.01x slower                                                     |
| html5lib                   | 64.5 ms                                                | 65.5 ms: 1.01x slower                                                     |
| unpickle_pure_python       | 213 us                                                 | 217 us: 1.02x slower                                                      |
| meteor_contest             | 108 ms                                                 | 110 ms: 1.02x slower                                                      |
| tornado_http               | 91.5 ms                                                | 93.2 ms: 1.02x slower                                                     |
| pickle_pure_python         | 300 us                                                 | 309 us: 1.03x slower                                                      |
| async_tree_cpu_io_mixed_tg | 543 ms                                                 | 561 ms: 1.03x slower                                                      |
| deltablue                  | 3.15 ms                                                | 3.27 ms: 1.04x slower                                                     |
| sqlglot_parse              | 1.27 ms                                                | 1.32 ms: 1.04x slower                                                     |
| pickle                     | 11.6 us                                                | 12.0 us: 1.04x slower                                                     |
| 2to3                       | 265 ms                                                 | 278 ms: 1.05x slower                                                      |
| typing_runtime_protocols   | 159 us                                                 | 167 us: 1.05x slower                                                      |
| comprehensions             | 16.4 us                                                | 17.3 us: 1.05x slower                                                     |
| django_template            | 34.4 ms                                                | 36.3 ms: 1.05x slower                                                     |
| pickle_list                | 5.01 us                                                | 5.28 us: 1.05x slower                                                     |
| dulwich_log                | 63.0 ms                                                | 66.6 ms: 1.06x slower                                                     |
| async_generators           | 433 ms                                                 | 458 ms: 1.06x slower                                                      |
| sqlglot_transpile          | 1.57 ms                                                | 1.67 ms: 1.06x slower                                                     |
| sqlglot_normalize          | 107 ms                                                 | 114 ms: 1.07x slower                                                      |
| json_dumps                 | 10.4 ms                                                | 11.1 ms: 1.07x slower                                                     |
| regex_compile              | 131 ms                                                 | 141 ms: 1.07x slower                                                      |
| bench_thread_pool          | 815 us                                                 | 877 us: 1.08x slower                                                      |
| sympy_expand               | 462 ms                                                 | 498 ms: 1.08x slower                                                      |
| raytrace                   | 262 ms                                                 | 283 ms: 1.08x slower                                                      |
| pickle_dict                | 33.2 us                                                | 35.9 us: 1.08x slower                                                     |
| unpickle_list              | 4.96 us                                                | 5.47 us: 1.10x slower                                                     |
| sympy_str                  | 274 ms                                                 | 302 ms: 1.11x slower                                                      |
| sqlglot_optimize           | 53.9 ms                                                | 59.7 ms: 1.11x slower                                                     |
| python_startup             | 10.6 ms                                                | 11.9 ms: 1.12x slower                                                     |
| docutils                   | 2.58 sec                                               | 2.91 sec: 1.12x slower                                                    |
| nqueens                    | 80.6 ms                                                | 90.7 ms: 1.12x slower                                                     |
| genshi_text                | 22.9 ms                                                | 26.1 ms: 1.14x slower                                                     |
| hexiom                     | 6.13 ms                                                | 7.06 ms: 1.15x slower                                                     |
| sympy_sum                  | 150 ms                                                 | 175 ms: 1.17x slower                                                      |
| sympy_integrate            | 19.9 ms                                                | 23.5 ms: 1.18x slower                                                     |
| async_tree_io_tg           | 825 ms                                                 | 976 ms: 1.18x slower                                                      |
| pylint                     | 313 ms                                                 | 376 ms: 1.20x slower                                                      |
| genshi_xml                 | 50.3 ms                                                | 61.7 ms: 1.23x slower                                                     |
| generators                 | 28.8 ms                                                | 35.7 ms: 1.24x slower                                                     |
| gc_traversal               | 3.81 ms                                                | 4.80 ms: 1.26x slower                                                     |
| create_gc_cycles           | 1.61 ms                                                | 2.68 ms: 1.67x slower                                                     |
| unpack_sequence            | 42.4 ns                                                | 110 ns: 2.59x slower                                                      |
| bench_mp_pool              | 24.0 ms                                                | 83.8 ms: 3.49x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.03x slower                                                              |

Benchmark hidden because not significant (11): async_tree_none_tg, unpickle, pprint_pformat, pprint_safe_repr, spectral_norm, asyncio_tcp_ssl, json_loads, thrift, asyncio_websockets, async_tree_cpu_io_mixed, async_tree_io
Ignored benchmarks (7) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (1) of results/bm-20241016-3.14.0a1+-9827ade-JIT/bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade.json: sphinx

# HPT report

- Reliability score: 70.53% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.19x