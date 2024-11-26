# Results vs. 3.13.0

- fork: savannahostrowski
- ref: jit_inv_cold_100
- machine: linux-x86_64
- commit hash: 0ee16f5
- commit date: 2024-09-23
- overall geometric mean: 1.001x faster
- HPT reliability: 92.88%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.94x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 318 ms: 1.19x slower                                                         |
| docutils       | 2.59 sec                                               | 2.72 sec: 1.05x slower                                                       |
| html5lib       | 64.2 ms                                                | 65.4 ms: 1.02x slower                                                        |
| tornado_http   | 92.4 ms                                                | 110 ms: 1.19x slower                                                         |
| Geometric mean | (ref)                                                  | 1.11x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 390 ms: 1.19x faster                                                         |
| async_tree_none            | 351 ms                                                 | 319 ms: 1.10x faster                                                         |
| async_tree_memoization     | 442 ms                                                 | 407 ms: 1.09x faster                                                         |
| async_tree_none_tg         | 321 ms                                                 | 307 ms: 1.04x faster                                                         |
| asyncio_websockets         | 552 ms                                                 | 560 ms: 1.01x slower                                                         |
| async_tree_io_tg           | 857 ms                                                 | 874 ms: 1.02x slower                                                         |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 557 ms: 1.02x slower                                                         |
| coroutines                 | 22.7 ms                                                | 23.2 ms: 1.02x slower                                                        |
| async_generators           | 436 ms                                                 | 460 ms: 1.06x slower                                                         |
| async_tree_io              | 842 ms                                                 | 892 ms: 1.06x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                 |

Benchmark hidden because not significant (1): async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 70.9 ms: 1.12x faster                                                        |
| nbody          | 87.0 ms                                                | 80.6 ms: 1.08x faster                                                        |
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                | 3.65 ms: 1.02x faster                                                        |
| regex_compile  | 132 ms                                                 | 132 ms: 1.01x faster                                                         |
| regex_dna      | 218 ms                                                 | 221 ms: 1.01x slower                                                         |
| regex_v8       | 26.2 ms                                                | 27.3 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_parse      | 156 ms                                                 | 149 ms: 1.04x faster                                                         |
| json_dumps           | 10.6 ms                                                | 10.2 ms: 1.03x faster                                                        |
| xml_etree_iterparse  | 101 ms                                                 | 100.0 ms: 1.01x faster                                                       |
| xml_etree_process    | 60.6 ms                                                | 61.2 ms: 1.01x slower                                                        |
| unpickle_pure_python | 216 us                                                 | 220 us: 1.02x slower                                                         |
| xml_etree_generate   | 86.7 ms                                                | 88.8 ms: 1.02x slower                                                        |
| pickle_pure_python   | 310 us                                                 | 332 us: 1.07x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (2): tomli_loads, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.6 ms: 1.18x faster                                                        |
| python_startup_no_site | 6.96 ms                                                | 7.10 ms: 1.02x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 10.5 ms: 1.06x faster                                                        |
| genshi_text     | 23.5 ms                                                | 24.5 ms: 1.04x slower                                                        |
| django_template | 35.2 ms                                                | 37.1 ms: 1.05x slower                                                        |
| genshi_xml      | 50.9 ms                                                | 58.3 ms: 1.15x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.04x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 27.8 us: 1.41x faster                                                        |
| create_gc_cycles           | 2.41 ms                                                | 1.73 ms: 1.39x faster                                                        |
| deepcopy                   | 358 us                                                 | 272 us: 1.32x faster                                                         |
| deepcopy_reduce            | 3.20 us                                                | 2.64 us: 1.21x faster                                                        |
| async_tree_memoization_tg  | 464 ms                                                 | 390 ms: 1.19x faster                                                         |
| python_startup             | 12.5 ms                                                | 10.6 ms: 1.18x faster                                                        |
| go                         | 144 ms                                                 | 122 ms: 1.18x faster                                                         |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.45 ms: 1.13x faster                                                        |
| float                      | 79.2 ms                                                | 70.9 ms: 1.12x faster                                                        |
| crypto_pyaes               | 75.3 ms                                                | 67.7 ms: 1.11x faster                                                        |
| gc_traversal               | 4.37 ms                                                | 3.93 ms: 1.11x faster                                                        |
| async_tree_none            | 351 ms                                                 | 319 ms: 1.10x faster                                                         |
| async_tree_memoization     | 442 ms                                                 | 407 ms: 1.09x faster                                                         |
| nbody                      | 87.0 ms                                                | 80.6 ms: 1.08x faster                                                        |
| pathlib                    | 17.5 ms                                                | 16.3 ms: 1.07x faster                                                        |
| mdp                        | 2.72 sec                                               | 2.57 sec: 1.06x faster                                                       |
| mako                       | 11.1 ms                                                | 10.5 ms: 1.06x faster                                                        |
| telco                      | 8.54 ms                                                | 8.09 ms: 1.06x faster                                                        |
| scimark_sor                | 124 ms                                                 | 117 ms: 1.05x faster                                                         |
| json                       | 5.36 ms                                                | 5.09 ms: 1.05x faster                                                        |
| spectral_norm              | 115 ms                                                 | 110 ms: 1.05x faster                                                         |
| xml_etree_parse            | 156 ms                                                 | 149 ms: 1.04x faster                                                         |
| async_tree_none_tg         | 321 ms                                                 | 307 ms: 1.04x faster                                                         |
| richards_super             | 54.9 ms                                                | 52.9 ms: 1.04x faster                                                        |
| fannkuch                   | 404 ms                                                 | 390 ms: 1.04x faster                                                         |
| json_dumps                 | 10.6 ms                                                | 10.2 ms: 1.03x faster                                                        |
| scimark_monte_carlo        | 67.4 ms                                                | 65.5 ms: 1.03x faster                                                        |
| regex_effbot               | 3.73 ms                                                | 3.65 ms: 1.02x faster                                                        |
| logging_format             | 6.40 us                                                | 6.27 us: 1.02x faster                                                        |
| richards                   | 48.7 ms                                                | 47.9 ms: 1.02x faster                                                        |
| thrift                     | 809 us                                                 | 798 us: 1.01x faster                                                         |
| xml_etree_iterparse        | 101 ms                                                 | 100.0 ms: 1.01x faster                                                       |
| regex_compile              | 132 ms                                                 | 132 ms: 1.01x faster                                                         |
| scimark_lu                 | 113 ms                                                 | 113 ms: 1.00x slower                                                         |
| pprint_safe_repr           | 728 ms                                                 | 732 ms: 1.01x slower                                                         |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                                         |
| coverage                   | 84.0 ms                                                | 84.6 ms: 1.01x slower                                                        |
| pycparser                  | 1.20 sec                                               | 1.21 sec: 1.01x slower                                                       |
| xml_etree_process          | 60.6 ms                                                | 61.2 ms: 1.01x slower                                                        |
| logging_simple             | 5.72 us                                                | 5.79 us: 1.01x slower                                                        |
| regex_dna                  | 218 ms                                                 | 221 ms: 1.01x slower                                                         |
| asyncio_websockets         | 552 ms                                                 | 560 ms: 1.01x slower                                                         |
| comprehensions             | 16.5 us                                                | 16.8 us: 1.02x slower                                                        |
| html5lib                   | 64.2 ms                                                | 65.4 ms: 1.02x slower                                                        |
| unpickle_pure_python       | 216 us                                                 | 220 us: 1.02x slower                                                         |
| async_tree_io_tg           | 857 ms                                                 | 874 ms: 1.02x slower                                                         |
| python_startup_no_site     | 6.96 ms                                                | 7.10 ms: 1.02x slower                                                        |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 557 ms: 1.02x slower                                                         |
| coroutines                 | 22.7 ms                                                | 23.2 ms: 1.02x slower                                                        |
| sympy_expand               | 463 ms                                                 | 474 ms: 1.02x slower                                                         |
| xml_etree_generate         | 86.7 ms                                                | 88.8 ms: 1.02x slower                                                        |
| raytrace                   | 267 ms                                                 | 274 ms: 1.03x slower                                                         |
| bpe_tokeniser              | 4.75 sec                                               | 4.88 sec: 1.03x slower                                                       |
| pyflate                    | 471 ms                                                 | 486 ms: 1.03x slower                                                         |
| regex_v8                   | 26.2 ms                                                | 27.3 ms: 1.04x slower                                                        |
| meteor_contest             | 109 ms                                                 | 113 ms: 1.04x slower                                                         |
| genshi_text                | 23.5 ms                                                | 24.5 ms: 1.04x slower                                                        |
| sympy_str                  | 275 ms                                                 | 287 ms: 1.04x slower                                                         |
| docutils                   | 2.59 sec                                               | 2.72 sec: 1.05x slower                                                       |
| sqlglot_parse              | 1.27 ms                                                | 1.34 ms: 1.05x slower                                                        |
| django_template            | 35.2 ms                                                | 37.1 ms: 1.05x slower                                                        |
| sympy_sum                  | 150 ms                                                 | 159 ms: 1.05x slower                                                         |
| async_generators           | 436 ms                                                 | 460 ms: 1.06x slower                                                         |
| async_tree_io              | 842 ms                                                 | 892 ms: 1.06x slower                                                         |
| chaos                      | 58.1 ms                                                | 61.6 ms: 1.06x slower                                                        |
| pickle_pure_python         | 310 us                                                 | 332 us: 1.07x slower                                                         |
| dulwich_log                | 64.3 ms                                                | 69.1 ms: 1.07x slower                                                        |
| sqlglot_normalize          | 108 ms                                                 | 116 ms: 1.08x slower                                                         |
| deltablue                  | 3.23 ms                                                | 3.58 ms: 1.11x slower                                                        |
| hexiom                     | 6.16 ms                                                | 6.84 ms: 1.11x slower                                                        |
| nqueens                    | 78.4 ms                                                | 87.1 ms: 1.11x slower                                                        |
| sqlglot_optimize           | 53.7 ms                                                | 60.3 ms: 1.12x slower                                                        |
| bench_thread_pool          | 822 us                                                 | 932 us: 1.13x slower                                                         |
| genshi_xml                 | 50.9 ms                                                | 58.3 ms: 1.15x slower                                                        |
| sqlglot_transpile          | 1.58 ms                                                | 1.85 ms: 1.17x slower                                                        |
| tornado_http               | 92.4 ms                                                | 110 ms: 1.19x slower                                                         |
| 2to3                       | 267 ms                                                 | 318 ms: 1.19x slower                                                         |
| pylint                     | 313 ms                                                 | 377 ms: 1.21x slower                                                         |
| generators                 | 29.0 ms                                                | 35.5 ms: 1.23x slower                                                        |
| sympy_integrate            | 19.9 ms                                                | 28.1 ms: 1.41x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, logging_silent, bench_mp_pool, tomli_loads, scimark_fft, pprint_pformat, json_loads, typing_runtime_protocols
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240923-3.14.0a0-0ee16f5-JIT/bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_100-3.14.0a0-0ee16f5.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.001x faster
# HPT report

- Reliability score: 92.88% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.94x