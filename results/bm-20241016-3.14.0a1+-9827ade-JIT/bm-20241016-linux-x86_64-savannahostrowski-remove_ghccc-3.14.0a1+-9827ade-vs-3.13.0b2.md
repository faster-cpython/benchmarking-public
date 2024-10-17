# Results vs. 3.13.0b2

- fork: savannahostrowski
- ref: remove_ghccc
- machine: linux-x86_64
- commit hash: 9827ade
- commit date: 2024-10-16
- overall geometric mean: 1.01x faster
- HPT reliability: 99.72%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.19x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 274 ms                                                     | 278 ms: 1.01x slower                                                      |
| docutils       | 2.83 sec                                                   | 2.91 sec: 1.03x slower                                                    |
| html5lib       | 67.2 ms                                                    | 65.5 ms: 1.03x faster                                                     |
| tornado_http   | 94.6 ms                                                    | 93.2 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                      | 1.00x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 444 ms                                                     | 375 ms: 1.18x faster                                                      |
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                                      |
| async_tree_memoization     | 463 ms                                                     | 414 ms: 1.12x faster                                                      |
| async_tree_io              | 939 ms                                                     | 848 ms: 1.11x faster                                                      |
| async_tree_none_tg         | 336 ms                                                     | 316 ms: 1.06x faster                                                      |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 577 ms: 1.06x faster                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 561 ms: 1.05x faster                                                      |
| async_tree_io_tg           | 936 ms                                                     | 976 ms: 1.04x slower                                                      |
| Geometric mean             | (ref)                                                      | 1.09x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                    | 82.1 ms: 1.08x faster                                                     |
| float          | 78.9 ms                                                    | 75.9 ms: 1.04x faster                                                     |
| pidigits       | 191 ms                                                     | 186 ms: 1.03x faster                                                      |
| Geometric mean | (ref)                                                      | 1.05x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                     | 208 ms: 1.06x faster                                                      |
| regex_v8       | 25.1 ms                                                    | 24.1 ms: 1.04x faster                                                     |
| regex_effbot   | 3.67 ms                                                    | 3.62 ms: 1.01x faster                                                     |
| regex_compile  | 137 ms                                                     | 141 ms: 1.03x slower                                                      |
| Geometric mean | (ref)                                                      | 1.02x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|---------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_generate  | 87.4 ms                                                    | 79.0 ms: 1.11x faster                                                     |
| xml_etree_process   | 61.2 ms                                                    | 55.5 ms: 1.10x faster                                                     |
| xml_etree_parse     | 162 ms                                                     | 149 ms: 1.09x faster                                                      |
| tomli_loads         | 2.12 sec                                                   | 1.95 sec: 1.09x faster                                                    |
| xml_etree_iterparse | 107 ms                                                     | 99.8 ms: 1.08x faster                                                     |
| json_loads          | 28.9 us                                                    | 27.0 us: 1.07x faster                                                     |
| unpickle            | 15.1 us                                                    | 14.7 us: 1.03x faster                                                     |
| pickle_pure_python  | 305 us                                                     | 309 us: 1.01x slower                                                      |
| unpickle_list       | 5.34 us                                                    | 5.47 us: 1.02x slower                                                     |
| pickle_dict         | 34.8 us                                                    | 35.9 us: 1.03x slower                                                     |
| pickle_list         | 5.11 us                                                    | 5.28 us: 1.03x slower                                                     |
| json_dumps          | 10.7 ms                                                    | 11.1 ms: 1.04x slower                                                     |
| pickle              | 11.5 us                                                    | 12.0 us: 1.05x slower                                                     |
| Geometric mean      | (ref)                                                      | 1.03x faster                                                              |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 7.11 ms                                                    | 7.06 ms: 1.01x faster                                                     |
| python_startup         | 10.8 ms                                                    | 11.9 ms: 1.10x slower                                                     |
| Geometric mean         | (ref)                                                      | 1.05x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|-----------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.2 ms                                                    | 10.3 ms: 1.09x faster                                                     |
| django_template | 34.8 ms                                                    | 36.3 ms: 1.04x slower                                                     |
| genshi_text     | 23.7 ms                                                    | 26.1 ms: 1.10x slower                                                     |
| genshi_xml      | 51.6 ms                                                    | 61.7 ms: 1.20x slower                                                     |
| Geometric mean  | (ref)                                                      | 1.06x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17 | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------------|:----------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy                   | 367 us                                                     | 274 us: 1.34x faster                                                      |
| deepcopy_memo              | 39.7 us                                                    | 29.8 us: 1.33x faster                                                     |
| scimark_fft                | 392 ms                                                     | 317 ms: 1.24x faster                                                      |
| richards                   | 50.9 ms                                                    | 41.2 ms: 1.24x faster                                                     |
| deepcopy_reduce            | 3.35 us                                                    | 2.74 us: 1.22x faster                                                     |
| richards_super             | 57.4 ms                                                    | 47.5 ms: 1.21x faster                                                     |
| async_tree_memoization_tg  | 444 ms                                                     | 375 ms: 1.18x faster                                                      |
| async_tree_none            | 378 ms                                                     | 326 ms: 1.16x faster                                                      |
| crypto_pyaes               | 77.5 ms                                                    | 67.1 ms: 1.15x faster                                                     |
| scimark_sparse_mat_mult    | 5.27 ms                                                    | 4.61 ms: 1.14x faster                                                     |
| bpe_tokeniser              | 5.02 sec                                                   | 4.46 sec: 1.13x faster                                                    |
| async_tree_memoization     | 463 ms                                                     | 414 ms: 1.12x faster                                                      |
| async_tree_io              | 939 ms                                                     | 848 ms: 1.11x faster                                                      |
| xml_etree_generate         | 87.4 ms                                                    | 79.0 ms: 1.11x faster                                                     |
| telco                      | 8.41 ms                                                    | 7.61 ms: 1.11x faster                                                     |
| coverage                   | 93.1 ms                                                    | 84.5 ms: 1.10x faster                                                     |
| xml_etree_process          | 61.2 ms                                                    | 55.5 ms: 1.10x faster                                                     |
| scimark_lu                 | 122 ms                                                     | 111 ms: 1.09x faster                                                      |
| mako                       | 11.2 ms                                                    | 10.3 ms: 1.09x faster                                                     |
| xml_etree_parse            | 162 ms                                                     | 149 ms: 1.09x faster                                                      |
| tomli_loads                | 2.12 sec                                                   | 1.95 sec: 1.09x faster                                                    |
| pathlib                    | 17.3 ms                                                    | 16.0 ms: 1.08x faster                                                     |
| go                         | 145 ms                                                     | 134 ms: 1.08x faster                                                      |
| pyflate                    | 484 ms                                                     | 449 ms: 1.08x faster                                                      |
| xml_etree_iterparse        | 107 ms                                                     | 99.8 ms: 1.08x faster                                                     |
| mdp                        | 2.79 sec                                                   | 2.59 sec: 1.08x faster                                                    |
| nbody                      | 88.3 ms                                                    | 82.1 ms: 1.08x faster                                                     |
| sqlite_synth               | 2.99 us                                                    | 2.78 us: 1.07x faster                                                     |
| logging_silent             | 105 ns                                                     | 97.7 ns: 1.07x faster                                                     |
| json_loads                 | 28.9 us                                                    | 27.0 us: 1.07x faster                                                     |
| scimark_sor                | 127 ms                                                     | 119 ms: 1.07x faster                                                      |
| json                       | 5.31 ms                                                    | 4.96 ms: 1.07x faster                                                     |
| async_tree_none_tg         | 336 ms                                                     | 316 ms: 1.06x faster                                                      |
| logging_format             | 6.47 us                                                    | 6.09 us: 1.06x faster                                                     |
| regex_dna                  | 221 ms                                                     | 208 ms: 1.06x faster                                                      |
| scimark_monte_carlo        | 69.2 ms                                                    | 65.1 ms: 1.06x faster                                                     |
| async_tree_cpu_io_mixed    | 611 ms                                                     | 577 ms: 1.06x faster                                                      |
| async_tree_cpu_io_mixed_tg | 587 ms                                                     | 561 ms: 1.05x faster                                                      |
| fannkuch                   | 402 ms                                                     | 385 ms: 1.04x faster                                                      |
| logging_simple             | 5.74 us                                                    | 5.51 us: 1.04x faster                                                     |
| chaos                      | 61.3 ms                                                    | 58.9 ms: 1.04x faster                                                     |
| regex_v8                   | 25.1 ms                                                    | 24.1 ms: 1.04x faster                                                     |
| pprint_pformat             | 1.56 sec                                                   | 1.50 sec: 1.04x faster                                                    |
| float                      | 78.9 ms                                                    | 75.9 ms: 1.04x faster                                                     |
| asyncio_tcp                | 508 ms                                                     | 493 ms: 1.03x faster                                                      |
| thrift                     | 823 us                                                     | 799 us: 1.03x faster                                                      |
| asyncio_tcp_ssl            | 1.84 sec                                                   | 1.79 sec: 1.03x faster                                                    |
| unpickle                   | 15.1 us                                                    | 14.7 us: 1.03x faster                                                     |
| pidigits                   | 191 ms                                                     | 186 ms: 1.03x faster                                                      |
| html5lib                   | 67.2 ms                                                    | 65.5 ms: 1.03x faster                                                     |
| pprint_safe_repr           | 758 ms                                                     | 739 ms: 1.03x faster                                                      |
| coroutines                 | 23.2 ms                                                    | 22.8 ms: 1.02x faster                                                     |
| asyncio_websockets         | 567 ms                                                     | 558 ms: 1.02x faster                                                      |
| tornado_http               | 94.6 ms                                                    | 93.2 ms: 1.02x faster                                                     |
| regex_effbot               | 3.67 ms                                                    | 3.62 ms: 1.01x faster                                                     |
| spectral_norm              | 116 ms                                                     | 115 ms: 1.01x faster                                                      |
| dulwich_log                | 67.2 ms                                                    | 66.6 ms: 1.01x faster                                                     |
| python_startup_no_site     | 7.11 ms                                                    | 7.06 ms: 1.01x faster                                                     |
| deltablue                  | 3.25 ms                                                    | 3.27 ms: 1.01x slower                                                     |
| pickle_pure_python         | 305 us                                                     | 309 us: 1.01x slower                                                      |
| typing_runtime_protocols   | 165 us                                                     | 167 us: 1.01x slower                                                      |
| 2to3                       | 274 ms                                                     | 278 ms: 1.01x slower                                                      |
| unpickle_list              | 5.34 us                                                    | 5.47 us: 1.02x slower                                                     |
| sqlglot_transpile          | 1.63 ms                                                    | 1.67 ms: 1.02x slower                                                     |
| regex_compile              | 137 ms                                                     | 141 ms: 1.03x slower                                                      |
| docutils                   | 2.83 sec                                                   | 2.91 sec: 1.03x slower                                                    |
| pickle_dict                | 34.8 us                                                    | 35.9 us: 1.03x slower                                                     |
| pickle_list                | 5.11 us                                                    | 5.28 us: 1.03x slower                                                     |
| async_generators           | 442 ms                                                     | 458 ms: 1.04x slower                                                      |
| sqlglot_normalize          | 110 ms                                                     | 114 ms: 1.04x slower                                                      |
| json_dumps                 | 10.7 ms                                                    | 11.1 ms: 1.04x slower                                                     |
| comprehensions             | 16.6 us                                                    | 17.3 us: 1.04x slower                                                     |
| django_template            | 34.8 ms                                                    | 36.3 ms: 1.04x slower                                                     |
| async_tree_io_tg           | 936 ms                                                     | 976 ms: 1.04x slower                                                      |
| pickle                     | 11.5 us                                                    | 12.0 us: 1.05x slower                                                     |
| bench_thread_pool          | 834 us                                                     | 877 us: 1.05x slower                                                      |
| sympy_expand               | 473 ms                                                     | 498 ms: 1.05x slower                                                      |
| raytrace                   | 267 ms                                                     | 283 ms: 1.06x slower                                                      |
| sympy_str                  | 282 ms                                                     | 302 ms: 1.07x slower                                                      |
| sqlglot_optimize           | 55.5 ms                                                    | 59.7 ms: 1.08x slower                                                     |
| genshi_text                | 23.7 ms                                                    | 26.1 ms: 1.10x slower                                                     |
| python_startup             | 10.8 ms                                                    | 11.9 ms: 1.10x slower                                                     |
| nqueens                    | 81.4 ms                                                    | 90.7 ms: 1.11x slower                                                     |
| sympy_sum                  | 156 ms                                                     | 175 ms: 1.12x slower                                                      |
| hexiom                     | 6.30 ms                                                    | 7.06 ms: 1.12x slower                                                     |
| sympy_integrate            | 20.5 ms                                                    | 23.5 ms: 1.15x slower                                                     |
| pylint                     | 317 ms                                                     | 376 ms: 1.19x slower                                                      |
| genshi_xml                 | 51.6 ms                                                    | 61.7 ms: 1.20x slower                                                     |
| generators                 | 29.6 ms                                                    | 35.7 ms: 1.20x slower                                                     |
| gc_traversal               | 3.98 ms                                                    | 4.80 ms: 1.21x slower                                                     |
| create_gc_cycles           | 1.82 ms                                                    | 2.68 ms: 1.48x slower                                                     |
| bench_mp_pool              | 23.9 ms                                                    | 83.8 ms: 3.51x slower                                                     |
| Geometric mean             | (ref)                                                      | 1.01x faster                                                              |

Benchmark hidden because not significant (4): unpickle_pure_python, sqlglot_parse, meteor_contest, pycparser
Ignored benchmarks (7) of results/bm-20240605-3.13.0b2-3a83b17/bm-20240605-linux-x86_64-python-v3.13.0b2-3.13.0b2-3a83b17.json: aiohttp, chameleon, dask, djangocms, flaskblogging, gunicorn, mypy2
Ignored benchmarks (2) of results/bm-20241016-3.14.0a1+-9827ade-JIT/bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade.json: sphinx, unpack_sequence

# HPT report

- Reliability score: 99.72% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.19x