# Results vs. 3.13.0

- fork: savannahostrowski
- ref: jit_inv_mem_100k
- machine: linux-x86_64
- commit hash: 17ece50
- commit date: 2024-09-23
- overall geometric mean: 1.020x faster
- HPT reliability: 59.69%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.96x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 280 ms: 1.05x slower                                                         |
| docutils       | 2.59 sec                                               | 2.93 sec: 1.13x slower                                                       |
| html5lib       | 64.2 ms                                                | 65.8 ms: 1.02x slower                                                        |
| tornado_http   | 92.4 ms                                                | 94.9 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                  | 1.06x slower                                                                 |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 391 ms: 1.19x faster                                                         |
| async_tree_none            | 351 ms                                                 | 318 ms: 1.10x faster                                                         |
| async_tree_memoization     | 442 ms                                                 | 409 ms: 1.08x faster                                                         |
| asyncio_websockets         | 552 ms                                                 | 556 ms: 1.01x slower                                                         |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 552 ms: 1.01x slower                                                         |
| coroutines                 | 22.7 ms                                                | 23.1 ms: 1.02x slower                                                        |
| async_tree_io_tg           | 857 ms                                                 | 880 ms: 1.03x slower                                                         |
| async_generators           | 436 ms                                                 | 457 ms: 1.05x slower                                                         |
| async_tree_io              | 842 ms                                                 | 886 ms: 1.05x slower                                                         |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                 |

Benchmark hidden because not significant (2): async_tree_none_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 71.1 ms: 1.11x faster                                                        |
| nbody          | 87.0 ms                                                | 80.6 ms: 1.08x faster                                                        |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 25.4 ms: 1.03x faster                                                        |
| regex_effbot   | 3.73 ms                                                | 3.65 ms: 1.02x faster                                                        |
| regex_dna      | 218 ms                                                 | 221 ms: 1.01x slower                                                         |
| regex_compile  | 132 ms                                                 | 144 ms: 1.09x slower                                                         |
| Geometric mean | (ref)                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| tomli_loads          | 2.14 sec                                               | 1.92 sec: 1.11x faster                                                       |
| xml_etree_generate   | 86.7 ms                                                | 78.2 ms: 1.11x faster                                                        |
| xml_etree_process    | 60.6 ms                                                | 55.6 ms: 1.09x faster                                                        |
| json_dumps           | 10.6 ms                                                | 10.0 ms: 1.06x faster                                                        |
| xml_etree_parse      | 156 ms                                                 | 148 ms: 1.05x faster                                                         |
| xml_etree_iterparse  | 101 ms                                                 | 98.8 ms: 1.02x faster                                                        |
| pickle_pure_python   | 310 us                                                 | 308 us: 1.01x faster                                                         |
| unpickle_pure_python | 216 us                                                 | 221 us: 1.02x slower                                                         |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                 |

Benchmark hidden because not significant (1): json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.5 ms: 1.18x faster                                                        |
| python_startup_no_site | 6.96 ms                                                | 7.07 ms: 1.02x slower                                                        |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.75 ms: 1.14x faster                                                        |
| django_template | 35.2 ms                                                | 36.3 ms: 1.03x slower                                                        |
| genshi_text     | 23.5 ms                                                | 25.4 ms: 1.08x slower                                                        |
| genshi_xml      | 50.9 ms                                                | 59.2 ms: 1.16x slower                                                        |
| Geometric mean  | (ref)                                                  | 1.03x slower                                                                 |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50 |
|----------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 27.1 us: 1.44x faster                                                        |
| create_gc_cycles           | 2.41 ms                                                | 1.72 ms: 1.40x faster                                                        |
| deepcopy                   | 358 us                                                 | 265 us: 1.35x faster                                                         |
| deepcopy_reduce            | 3.20 us                                                | 2.64 us: 1.21x faster                                                        |
| richards_super             | 54.9 ms                                                | 46.0 ms: 1.19x faster                                                        |
| richards                   | 48.7 ms                                                | 40.9 ms: 1.19x faster                                                        |
| async_tree_memoization_tg  | 464 ms                                                 | 391 ms: 1.19x faster                                                         |
| gc_traversal               | 4.37 ms                                                | 3.68 ms: 1.19x faster                                                        |
| python_startup             | 12.5 ms                                                | 10.5 ms: 1.18x faster                                                        |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.38 ms: 1.15x faster                                                        |
| scimark_fft                | 364 ms                                                 | 317 ms: 1.15x faster                                                         |
| mako                       | 11.1 ms                                                | 9.75 ms: 1.14x faster                                                        |
| crypto_pyaes               | 75.3 ms                                                | 66.7 ms: 1.13x faster                                                        |
| tomli_loads                | 2.14 sec                                               | 1.92 sec: 1.11x faster                                                       |
| float                      | 79.2 ms                                                | 71.1 ms: 1.11x faster                                                        |
| spectral_norm              | 115 ms                                                 | 104 ms: 1.11x faster                                                         |
| xml_etree_generate         | 86.7 ms                                                | 78.2 ms: 1.11x faster                                                        |
| pathlib                    | 17.5 ms                                                | 15.9 ms: 1.10x faster                                                        |
| async_tree_none            | 351 ms                                                 | 318 ms: 1.10x faster                                                         |
| xml_etree_process          | 60.6 ms                                                | 55.6 ms: 1.09x faster                                                        |
| go                         | 144 ms                                                 | 132 ms: 1.09x faster                                                         |
| async_tree_memoization     | 442 ms                                                 | 409 ms: 1.08x faster                                                         |
| nbody                      | 87.0 ms                                                | 80.6 ms: 1.08x faster                                                        |
| scimark_monte_carlo        | 67.4 ms                                                | 63.0 ms: 1.07x faster                                                        |
| mdp                        | 2.72 sec                                               | 2.54 sec: 1.07x faster                                                       |
| telco                      | 8.54 ms                                                | 7.98 ms: 1.07x faster                                                        |
| fannkuch                   | 404 ms                                                 | 378 ms: 1.07x faster                                                         |
| scimark_sor                | 124 ms                                                 | 117 ms: 1.06x faster                                                         |
| json_dumps                 | 10.6 ms                                                | 10.0 ms: 1.06x faster                                                        |
| bpe_tokeniser              | 4.75 sec                                               | 4.50 sec: 1.05x faster                                                       |
| xml_etree_parse            | 156 ms                                                 | 148 ms: 1.05x faster                                                         |
| json                       | 5.36 ms                                                | 5.10 ms: 1.05x faster                                                        |
| regex_v8                   | 26.2 ms                                                | 25.4 ms: 1.03x faster                                                        |
| thrift                     | 809 us                                                 | 786 us: 1.03x faster                                                         |
| logging_format             | 6.40 us                                                | 6.22 us: 1.03x faster                                                        |
| pyflate                    | 471 ms                                                 | 459 ms: 1.03x faster                                                         |
| xml_etree_iterparse        | 101 ms                                                 | 98.8 ms: 1.02x faster                                                        |
| regex_effbot               | 3.73 ms                                                | 3.65 ms: 1.02x faster                                                        |
| scimark_lu                 | 113 ms                                                 | 111 ms: 1.01x faster                                                         |
| pickle_pure_python         | 310 us                                                 | 308 us: 1.01x faster                                                         |
| meteor_contest             | 109 ms                                                 | 108 ms: 1.01x faster                                                         |
| logging_simple             | 5.72 us                                                | 5.69 us: 1.01x faster                                                        |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                         |
| asyncio_websockets         | 552 ms                                                 | 556 ms: 1.01x slower                                                         |
| regex_dna                  | 218 ms                                                 | 221 ms: 1.01x slower                                                         |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 552 ms: 1.01x slower                                                         |
| pycparser                  | 1.20 sec                                               | 1.22 sec: 1.01x slower                                                       |
| python_startup_no_site     | 6.96 ms                                                | 7.07 ms: 1.02x slower                                                        |
| coroutines                 | 22.7 ms                                                | 23.1 ms: 1.02x slower                                                        |
| bench_thread_pool          | 822 us                                                 | 839 us: 1.02x slower                                                         |
| unpickle_pure_python       | 216 us                                                 | 221 us: 1.02x slower                                                         |
| logging_silent             | 102 ns                                                 | 104 ns: 1.02x slower                                                         |
| html5lib                   | 64.2 ms                                                | 65.8 ms: 1.02x slower                                                        |
| tornado_http               | 92.4 ms                                                | 94.9 ms: 1.03x slower                                                        |
| comprehensions             | 16.5 us                                                | 16.9 us: 1.03x slower                                                        |
| async_tree_io_tg           | 857 ms                                                 | 880 ms: 1.03x slower                                                         |
| chaos                      | 58.1 ms                                                | 59.6 ms: 1.03x slower                                                        |
| pprint_safe_repr           | 728 ms                                                 | 751 ms: 1.03x slower                                                         |
| django_template            | 35.2 ms                                                | 36.3 ms: 1.03x slower                                                        |
| pprint_pformat             | 1.49 sec                                               | 1.56 sec: 1.05x slower                                                       |
| async_generators           | 436 ms                                                 | 457 ms: 1.05x slower                                                         |
| 2to3                       | 267 ms                                                 | 280 ms: 1.05x slower                                                         |
| async_tree_io              | 842 ms                                                 | 886 ms: 1.05x slower                                                         |
| raytrace                   | 267 ms                                                 | 281 ms: 1.05x slower                                                         |
| sqlglot_parse              | 1.27 ms                                                | 1.35 ms: 1.06x slower                                                        |
| sqlglot_normalize          | 108 ms                                                 | 114 ms: 1.06x slower                                                         |
| coverage                   | 84.0 ms                                                | 89.3 ms: 1.06x slower                                                        |
| dulwich_log                | 64.3 ms                                                | 68.5 ms: 1.06x slower                                                        |
| sqlglot_transpile          | 1.58 ms                                                | 1.69 ms: 1.07x slower                                                        |
| genshi_text                | 23.5 ms                                                | 25.4 ms: 1.08x slower                                                        |
| regex_compile              | 132 ms                                                 | 144 ms: 1.09x slower                                                         |
| sympy_expand               | 463 ms                                                 | 507 ms: 1.09x slower                                                         |
| sympy_str                  | 275 ms                                                 | 305 ms: 1.11x slower                                                         |
| nqueens                    | 78.4 ms                                                | 87.1 ms: 1.11x slower                                                        |
| sqlglot_optimize           | 53.7 ms                                                | 60.7 ms: 1.13x slower                                                        |
| docutils                   | 2.59 sec                                               | 2.93 sec: 1.13x slower                                                       |
| hexiom                     | 6.16 ms                                                | 7.02 ms: 1.14x slower                                                        |
| genshi_xml                 | 50.9 ms                                                | 59.2 ms: 1.16x slower                                                        |
| sympy_integrate            | 19.9 ms                                                | 23.1 ms: 1.16x slower                                                        |
| sympy_sum                  | 150 ms                                                 | 176 ms: 1.17x slower                                                         |
| pylint                     | 313 ms                                                 | 378 ms: 1.21x slower                                                         |
| generators                 | 29.0 ms                                                | 35.2 ms: 1.22x slower                                                        |
| Geometric mean             | (ref)                                                  | 1.02x faster                                                                 |

Benchmark hidden because not significant (6): async_tree_none_tg, async_tree_cpu_io_mixed, typing_runtime_protocols, deltablue, json_loads, bench_mp_pool
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20240923-3.14.0a0-17ece50-JIT/bm-20240923-linux-x86_64-savannahostrowski-jit_inv_mem_100k-3.14.0a0-17ece50.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.020x faster
# HPT report

- Reliability score: 59.69% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.96x