# Results vs. 3.13.0

- fork: savannahostrowski
- ref: remove_ghccc
- machine: linux-x86_64
- commit hash: 9827ade
- commit date: 2024-10-16
- overall geometric mean: 1.004x faster
- HPT reliability: 57.39%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 278 ms: 1.04x slower                                                      |
| docutils       | 2.59 sec                                               | 2.91 sec: 1.12x slower                                                    |
| html5lib       | 64.2 ms                                                | 65.5 ms: 1.02x slower                                                     |
| sphinx         | 1.03 sec                                               | 1.16 sec: 1.12x slower                                                    |
| tornado_http   | 92.4 ms                                                | 93.2 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                  | 1.06x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 375 ms: 1.24x faster                                                      |
| async_tree_none            | 351 ms                                                 | 326 ms: 1.08x faster                                                      |
| async_tree_memoization     | 442 ms                                                 | 414 ms: 1.07x faster                                                      |
| asyncio_websockets         | 552 ms                                                 | 558 ms: 1.01x slower                                                      |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 561 ms: 1.03x slower                                                      |
| async_generators           | 436 ms                                                 | 458 ms: 1.05x slower                                                      |
| async_tree_io_tg           | 857 ms                                                 | 976 ms: 1.14x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (4): async_tree_none_tg, async_tree_cpu_io_mixed, coroutines, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 87.0 ms                                                | 82.1 ms: 1.06x faster                                                     |
| float          | 79.2 ms                                                | 75.9 ms: 1.04x faster                                                     |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.1 ms: 1.09x faster                                                     |
| regex_dna      | 218 ms                                                 | 208 ms: 1.05x faster                                                      |
| regex_effbot   | 3.73 ms                                                | 3.62 ms: 1.03x faster                                                     |
| regex_compile  | 132 ms                                                 | 141 ms: 1.06x slower                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_generate   | 86.7 ms                                                | 79.0 ms: 1.10x faster                                                     |
| tomli_loads          | 2.14 sec                                               | 1.95 sec: 1.10x faster                                                    |
| xml_etree_process    | 60.6 ms                                                | 55.5 ms: 1.09x faster                                                     |
| xml_etree_parse      | 156 ms                                                 | 149 ms: 1.05x faster                                                      |
| xml_etree_iterparse  | 101 ms                                                 | 99.8 ms: 1.01x faster                                                     |
| json_loads           | 27.2 us                                                | 27.0 us: 1.01x faster                                                     |
| pickle_pure_python   | 310 us                                                 | 309 us: 1.01x faster                                                      |
| unpickle_pure_python | 216 us                                                 | 217 us: 1.01x slower                                                      |
| json_dumps           | 10.6 ms                                                | 11.1 ms: 1.05x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                              |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 11.9 ms: 1.05x faster                                                     |
| python_startup_no_site | 6.96 ms                                                | 7.06 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.3 ms: 1.08x faster                                                     |
| django_template | 35.2 ms                                                | 36.3 ms: 1.03x slower                                                     |
| genshi_text     | 23.5 ms                                                | 26.1 ms: 1.11x slower                                                     |
| genshi_xml      | 50.9 ms                                                | 61.7 ms: 1.21x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.07x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 29.8 us: 1.31x faster                                                     |
| deepcopy                   | 358 us                                                 | 274 us: 1.31x faster                                                      |
| async_tree_memoization_tg  | 464 ms                                                 | 375 ms: 1.24x faster                                                      |
| richards                   | 48.7 ms                                                | 41.2 ms: 1.18x faster                                                     |
| deepcopy_reduce            | 3.20 us                                                | 2.74 us: 1.17x faster                                                     |
| richards_super             | 54.9 ms                                                | 47.5 ms: 1.15x faster                                                     |
| scimark_fft                | 364 ms                                                 | 317 ms: 1.15x faster                                                      |
| crypto_pyaes               | 75.3 ms                                                | 67.1 ms: 1.12x faster                                                     |
| telco                      | 8.54 ms                                                | 7.61 ms: 1.12x faster                                                     |
| xml_etree_generate         | 86.7 ms                                                | 79.0 ms: 1.10x faster                                                     |
| tomli_loads                | 2.14 sec                                               | 1.95 sec: 1.10x faster                                                    |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.61 ms: 1.09x faster                                                     |
| pathlib                    | 17.5 ms                                                | 16.0 ms: 1.09x faster                                                     |
| xml_etree_process          | 60.6 ms                                                | 55.5 ms: 1.09x faster                                                     |
| regex_v8                   | 26.2 ms                                                | 24.1 ms: 1.09x faster                                                     |
| json                       | 5.36 ms                                                | 4.96 ms: 1.08x faster                                                     |
| async_tree_none            | 351 ms                                                 | 326 ms: 1.08x faster                                                      |
| mako                       | 11.1 ms                                                | 10.3 ms: 1.08x faster                                                     |
| go                         | 144 ms                                                 | 134 ms: 1.07x faster                                                      |
| async_tree_memoization     | 442 ms                                                 | 414 ms: 1.07x faster                                                      |
| bpe_tokeniser              | 4.75 sec                                               | 4.46 sec: 1.06x faster                                                    |
| nbody                      | 87.0 ms                                                | 82.1 ms: 1.06x faster                                                     |
| python_startup             | 12.5 ms                                                | 11.9 ms: 1.05x faster                                                     |
| fannkuch                   | 404 ms                                                 | 385 ms: 1.05x faster                                                      |
| logging_format             | 6.40 us                                                | 6.09 us: 1.05x faster                                                     |
| mdp                        | 2.72 sec                                               | 2.59 sec: 1.05x faster                                                    |
| regex_dna                  | 218 ms                                                 | 208 ms: 1.05x faster                                                      |
| pyflate                    | 471 ms                                                 | 449 ms: 1.05x faster                                                      |
| xml_etree_parse            | 156 ms                                                 | 149 ms: 1.05x faster                                                      |
| float                      | 79.2 ms                                                | 75.9 ms: 1.04x faster                                                     |
| logging_silent             | 102 ns                                                 | 97.7 ns: 1.04x faster                                                     |
| logging_simple             | 5.72 us                                                | 5.51 us: 1.04x faster                                                     |
| scimark_sor                | 124 ms                                                 | 119 ms: 1.04x faster                                                      |
| pycparser                  | 1.20 sec                                               | 1.16 sec: 1.04x faster                                                    |
| scimark_monte_carlo        | 67.4 ms                                                | 65.1 ms: 1.04x faster                                                     |
| regex_effbot               | 3.73 ms                                                | 3.62 ms: 1.03x faster                                                     |
| xml_etree_iterparse        | 101 ms                                                 | 99.8 ms: 1.01x faster                                                     |
| thrift                     | 809 us                                                 | 799 us: 1.01x faster                                                      |
| scimark_lu                 | 113 ms                                                 | 111 ms: 1.01x faster                                                      |
| json_loads                 | 27.2 us                                                | 27.0 us: 1.01x faster                                                     |
| pickle_pure_python         | 310 us                                                 | 309 us: 1.01x faster                                                      |
| spectral_norm              | 115 ms                                                 | 115 ms: 1.00x faster                                                      |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                      |
| coverage                   | 84.0 ms                                                | 84.5 ms: 1.01x slower                                                     |
| meteor_contest             | 109 ms                                                 | 110 ms: 1.01x slower                                                      |
| unpickle_pure_python       | 216 us                                                 | 217 us: 1.01x slower                                                      |
| tornado_http               | 92.4 ms                                                | 93.2 ms: 1.01x slower                                                     |
| asyncio_websockets         | 552 ms                                                 | 558 ms: 1.01x slower                                                      |
| typing_runtime_protocols   | 165 us                                                 | 167 us: 1.01x slower                                                      |
| chaos                      | 58.1 ms                                                | 58.9 ms: 1.01x slower                                                     |
| python_startup_no_site     | 6.96 ms                                                | 7.06 ms: 1.01x slower                                                     |
| deltablue                  | 3.23 ms                                                | 3.27 ms: 1.01x slower                                                     |
| pprint_safe_repr           | 728 ms                                                 | 739 ms: 1.02x slower                                                      |
| html5lib                   | 64.2 ms                                                | 65.5 ms: 1.02x slower                                                     |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 561 ms: 1.03x slower                                                      |
| django_template            | 35.2 ms                                                | 36.3 ms: 1.03x slower                                                     |
| sqlglot_parse              | 1.27 ms                                                | 1.32 ms: 1.03x slower                                                     |
| dulwich_log                | 64.3 ms                                                | 66.6 ms: 1.03x slower                                                     |
| 2to3                       | 267 ms                                                 | 278 ms: 1.04x slower                                                      |
| comprehensions             | 16.5 us                                                | 17.3 us: 1.05x slower                                                     |
| async_generators           | 436 ms                                                 | 458 ms: 1.05x slower                                                      |
| json_dumps                 | 10.6 ms                                                | 11.1 ms: 1.05x slower                                                     |
| sqlglot_transpile          | 1.58 ms                                                | 1.67 ms: 1.06x slower                                                     |
| raytrace                   | 267 ms                                                 | 283 ms: 1.06x slower                                                      |
| regex_compile              | 132 ms                                                 | 141 ms: 1.06x slower                                                      |
| sqlglot_normalize          | 108 ms                                                 | 114 ms: 1.06x slower                                                      |
| bench_thread_pool          | 822 us                                                 | 877 us: 1.07x slower                                                      |
| sympy_expand               | 463 ms                                                 | 498 ms: 1.07x slower                                                      |
| gc_traversal               | 4.37 ms                                                | 4.80 ms: 1.10x slower                                                     |
| sympy_str                  | 275 ms                                                 | 302 ms: 1.10x slower                                                      |
| genshi_text                | 23.5 ms                                                | 26.1 ms: 1.11x slower                                                     |
| sqlglot_optimize           | 53.7 ms                                                | 59.7 ms: 1.11x slower                                                     |
| create_gc_cycles           | 2.41 ms                                                | 2.68 ms: 1.11x slower                                                     |
| docutils                   | 2.59 sec                                               | 2.91 sec: 1.12x slower                                                    |
| sphinx                     | 1.03 sec                                               | 1.16 sec: 1.12x slower                                                    |
| async_tree_io_tg           | 857 ms                                                 | 976 ms: 1.14x slower                                                      |
| hexiom                     | 6.16 ms                                                | 7.06 ms: 1.15x slower                                                     |
| nqueens                    | 78.4 ms                                                | 90.7 ms: 1.16x slower                                                     |
| sympy_sum                  | 150 ms                                                 | 175 ms: 1.16x slower                                                      |
| sympy_integrate            | 19.9 ms                                                | 23.5 ms: 1.18x slower                                                     |
| pylint                     | 313 ms                                                 | 376 ms: 1.20x slower                                                      |
| genshi_xml                 | 50.9 ms                                                | 61.7 ms: 1.21x slower                                                     |
| generators                 | 29.0 ms                                                | 35.7 ms: 1.23x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 83.8 ms: 3.49x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (5): async_tree_none_tg, async_tree_cpu_io_mixed, pprint_pformat, coroutines, async_tree_io
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241016-3.14.0a1+-9827ade-JIT/bm-20241016-linux-x86_64-savannahostrowski-remove_ghccc-3.14.0a1+-9827ade.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.004x faster
# HPT report

- Reliability score: 57.39% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.07x