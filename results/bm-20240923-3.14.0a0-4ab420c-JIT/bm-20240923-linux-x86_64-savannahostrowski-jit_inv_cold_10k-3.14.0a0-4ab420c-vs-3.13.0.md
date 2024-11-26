# Results vs. 3.13.0

- fork: savannahostrowski
- ref: jit_inv_cold_10k
- machine: linux-x86_64
- commit hash: 4ab420c
- commit date: 2024-09-23
- overall geometric mean: 1.009x faster
- HPT reliability: 69.13%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.95x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 285 ms: 1.07x slower                                                         |
| docutils       | 2.59 sec                                               | 2.89 sec: 1.11x slower                                                       |
| html5lib       | 64.2 ms                                                | 66.2 ms: 1.03x slower                                                        |
| tornado_http   | 92.4 ms                                                | 96.0 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                  | 1.06x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 389 ms: 1.19x faster                                                         |
| async_tree_memoization     | 442 ms                                                 | 399 ms: 1.11x faster                                                         |
| async_tree_none            | 351 ms                                                 | 320 ms: 1.10x faster                                                         |
| async_tree_none_tg         | 321 ms                                                 | 301 ms: 1.07x faster                                                         |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 569 ms: 1.01x faster                                                         |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                                         |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 551 ms: 1.01x slower                                                         |
| async_tree_io_tg           | 857 ms                                                 | 878 ms: 1.03x slower                                                         |
| coroutines                 | 22.7 ms                                                | 23.5 ms: 1.04x slower                                                        |
| async_generators           | 436 ms                                                 | 456 ms: 1.05x slower                                                         |
| async_tree_io              | 842 ms                                                 | 886 ms: 1.05x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                                 |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 71.4 ms: 1.11x faster                                                        |
| nbody          | 87.0 ms                                                | 82.1 ms: 1.06x faster                                                        |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_effbot   | 3.73 ms                                                | 3.78 ms: 1.01x slower                                                        |
| regex_dna      | 218 ms                                                 | 224 ms: 1.03x slower                                                         |
| regex_compile  | 132 ms                                                 | 139 ms: 1.05x slower                                                         |
| Geometric mean | (ref)                                                  | 1.02x slower                                                                 |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.14 sec                                               | 1.93 sec: 1.11x faster                                                       |
| xml_etree_process    | 60.6 ms                                                | 56.2 ms: 1.08x faster                                                        |
| xml_etree_generate   | 86.7 ms                                                | 80.7 ms: 1.08x faster                                                        |
| xml_etree_parse      | 156 ms                                                 | 149 ms: 1.05x faster                                                         |
| json_dumps           | 10.6 ms                                                | 10.2 ms: 1.04x faster                                                        |
| pickle_pure_python   | 310 us                                                 | 303 us: 1.02x faster                                                         |
| xml_etree_iterparse  | 101 ms                                                 | 99.7 ms: 1.02x faster                                                        |
| json_loads           | 27.2 us                                                | 27.4 us: 1.00x slower                                                        |
| unpickle_pure_python | 216 us                                                 | 219 us: 1.01x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                 |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                        |
| python_startup_no_site | 6.96 ms                                                | 7.05 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.94 ms: 1.12x faster                                                        |
| django_template | 35.2 ms                                                | 36.9 ms: 1.05x slower                                                        |
| genshi_text     | 23.5 ms                                                | 25.7 ms: 1.09x slower                                                        |
| genshi_xml      | 50.9 ms                                                | 60.8 ms: 1.19x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.05x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 27.0 us: 1.45x faster                                                        |
| create_gc_cycles           | 2.41 ms                                                | 1.72 ms: 1.40x faster                                                        |
| deepcopy                   | 358 us                                                 | 269 us: 1.33x faster                                                         |
| deepcopy_reduce            | 3.20 us                                                | 2.67 us: 1.20x faster                                                        |
| async_tree_memoization_tg  | 464 ms                                                 | 389 ms: 1.19x faster                                                         |
| python_startup             | 12.5 ms                                                | 10.5 ms: 1.19x faster                                                        |
| richards_super             | 54.9 ms                                                | 47.0 ms: 1.17x faster                                                        |
| gc_traversal               | 4.37 ms                                                | 3.80 ms: 1.15x faster                                                        |
| scimark_fft                | 364 ms                                                 | 317 ms: 1.15x faster                                                         |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.40 ms: 1.15x faster                                                        |
| richards                   | 48.7 ms                                                | 42.7 ms: 1.14x faster                                                        |
| mako                       | 11.1 ms                                                | 9.94 ms: 1.12x faster                                                        |
| crypto_pyaes               | 75.3 ms                                                | 67.9 ms: 1.11x faster                                                        |
| float                      | 79.2 ms                                                | 71.4 ms: 1.11x faster                                                        |
| tomli_loads                | 2.14 sec                                               | 1.93 sec: 1.11x faster                                                       |
| async_tree_memoization     | 442 ms                                                 | 399 ms: 1.11x faster                                                         |
| async_tree_none            | 351 ms                                                 | 320 ms: 1.10x faster                                                         |
| pathlib                    | 17.5 ms                                                | 16.1 ms: 1.09x faster                                                        |
| xml_etree_process          | 60.6 ms                                                | 56.2 ms: 1.08x faster                                                        |
| fannkuch                   | 404 ms                                                 | 376 ms: 1.08x faster                                                         |
| xml_etree_generate         | 86.7 ms                                                | 80.7 ms: 1.08x faster                                                        |
| async_tree_none_tg         | 321 ms                                                 | 301 ms: 1.07x faster                                                         |
| mdp                        | 2.72 sec                                               | 2.55 sec: 1.06x faster                                                       |
| telco                      | 8.54 ms                                                | 8.03 ms: 1.06x faster                                                        |
| scimark_monte_carlo        | 67.4 ms                                                | 63.7 ms: 1.06x faster                                                        |
| nbody                      | 87.0 ms                                                | 82.1 ms: 1.06x faster                                                        |
| go                         | 144 ms                                                 | 136 ms: 1.06x faster                                                         |
| json                       | 5.36 ms                                                | 5.08 ms: 1.06x faster                                                        |
| scimark_sor                | 124 ms                                                 | 117 ms: 1.05x faster                                                         |
| xml_etree_parse            | 156 ms                                                 | 149 ms: 1.05x faster                                                         |
| json_dumps                 | 10.6 ms                                                | 10.2 ms: 1.04x faster                                                        |
| logging_format             | 6.40 us                                                | 6.18 us: 1.03x faster                                                        |
| pyflate                    | 471 ms                                                 | 456 ms: 1.03x faster                                                         |
| thrift                     | 809 us                                                 | 786 us: 1.03x faster                                                         |
| spectral_norm              | 115 ms                                                 | 112 ms: 1.03x faster                                                         |
| pickle_pure_python         | 310 us                                                 | 303 us: 1.02x faster                                                         |
| meteor_contest             | 109 ms                                                 | 106 ms: 1.02x faster                                                         |
| xml_etree_iterparse        | 101 ms                                                 | 99.7 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 569 ms: 1.01x faster                                                         |
| logging_simple             | 5.72 us                                                | 5.68 us: 1.01x faster                                                        |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| json_loads                 | 27.2 us                                                | 27.4 us: 1.00x slower                                                        |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                                         |
| logging_silent             | 102 ns                                                 | 102 ns: 1.01x slower                                                         |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 551 ms: 1.01x slower                                                         |
| regex_effbot               | 3.73 ms                                                | 3.78 ms: 1.01x slower                                                        |
| python_startup_no_site     | 6.96 ms                                                | 7.05 ms: 1.01x slower                                                        |
| unpickle_pure_python       | 216 us                                                 | 219 us: 1.01x slower                                                         |
| pycparser                  | 1.20 sec                                               | 1.23 sec: 1.02x slower                                                       |
| comprehensions             | 16.5 us                                                | 16.8 us: 1.02x slower                                                        |
| chaos                      | 58.1 ms                                                | 59.3 ms: 1.02x slower                                                        |
| bench_thread_pool          | 822 us                                                 | 841 us: 1.02x slower                                                         |
| scimark_lu                 | 113 ms                                                 | 115 ms: 1.02x slower                                                         |
| regex_dna                  | 218 ms                                                 | 224 ms: 1.03x slower                                                         |
| async_tree_io_tg           | 857 ms                                                 | 878 ms: 1.03x slower                                                         |
| html5lib                   | 64.2 ms                                                | 66.2 ms: 1.03x slower                                                        |
| bpe_tokeniser              | 4.75 sec                                               | 4.90 sec: 1.03x slower                                                       |
| coverage                   | 84.0 ms                                                | 86.9 ms: 1.04x slower                                                        |
| coroutines                 | 22.7 ms                                                | 23.5 ms: 1.04x slower                                                        |
| tornado_http               | 92.4 ms                                                | 96.0 ms: 1.04x slower                                                        |
| pprint_safe_repr           | 728 ms                                                 | 760 ms: 1.04x slower                                                         |
| async_generators           | 436 ms                                                 | 456 ms: 1.05x slower                                                         |
| pprint_pformat             | 1.49 sec                                               | 1.57 sec: 1.05x slower                                                       |
| django_template            | 35.2 ms                                                | 36.9 ms: 1.05x slower                                                        |
| async_tree_io              | 842 ms                                                 | 886 ms: 1.05x slower                                                         |
| regex_compile              | 132 ms                                                 | 139 ms: 1.05x slower                                                         |
| raytrace                   | 267 ms                                                 | 281 ms: 1.05x slower                                                         |
| dulwich_log                | 64.3 ms                                                | 68.1 ms: 1.06x slower                                                        |
| sqlglot_parse              | 1.27 ms                                                | 1.35 ms: 1.06x slower                                                        |
| sqlglot_transpile          | 1.58 ms                                                | 1.69 ms: 1.07x slower                                                        |
| 2to3                       | 267 ms                                                 | 285 ms: 1.07x slower                                                         |
| sympy_expand               | 463 ms                                                 | 503 ms: 1.09x slower                                                         |
| sqlglot_normalize          | 108 ms                                                 | 117 ms: 1.09x slower                                                         |
| genshi_text                | 23.5 ms                                                | 25.7 ms: 1.09x slower                                                        |
| docutils                   | 2.59 sec                                               | 2.89 sec: 1.11x slower                                                       |
| nqueens                    | 78.4 ms                                                | 87.7 ms: 1.12x slower                                                        |
| sympy_str                  | 275 ms                                                 | 308 ms: 1.12x slower                                                         |
| deltablue                  | 3.23 ms                                                | 3.65 ms: 1.13x slower                                                        |
| sympy_sum                  | 150 ms                                                 | 172 ms: 1.14x slower                                                         |
| genshi_xml                 | 50.9 ms                                                | 60.8 ms: 1.19x slower                                                        |
| sqlglot_optimize           | 53.7 ms                                                | 64.3 ms: 1.20x slower                                                        |
| pylint                     | 313 ms                                                 | 380 ms: 1.21x slower                                                         |
| generators                 | 29.0 ms                                                | 35.6 ms: 1.23x slower                                                        |
| hexiom                     | 6.16 ms                                                | 7.80 ms: 1.26x slower                                                        |
| sympy_integrate            | 19.9 ms                                                | 26.7 ms: 1.34x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (3): regex_v8, bench_mp_pool, typing_runtime_protocols
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240923-3.14.0a0-4ab420c-JIT/bm-20240923-linux-x86_64-savannahostrowski-jit_inv_cold_10k-3.14.0a0-4ab420c.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.009x faster
# HPT report

- Reliability score: 69.13% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.95x