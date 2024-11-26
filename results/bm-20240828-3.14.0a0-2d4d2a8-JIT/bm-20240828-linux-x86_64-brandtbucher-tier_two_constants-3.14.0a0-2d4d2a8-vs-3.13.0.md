# Results vs. 3.13.0

- fork: brandtbucher
- ref: tier_two_constants
- machine: linux-x86_64
- commit hash: 2d4d2a8
- commit date: 2024-08-28
- overall geometric mean: 1.028x faster
- HPT reliability: 78.12%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 277 ms: 1.04x slower                                                      |
| docutils       | 2.59 sec                                               | 3.04 sec: 1.17x slower                                                    |
| tornado_http   | 92.4 ms                                                | 94.4 ms: 1.02x slower                                                     |
| Geometric mean | (ref)                                                  | 1.06x slower                                                              |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 404 ms: 1.15x faster                                                      |
| async_tree_none            | 351 ms                                                 | 328 ms: 1.07x faster                                                      |
| async_tree_memoization     | 442 ms                                                 | 417 ms: 1.06x faster                                                      |
| async_tree_none_tg         | 321 ms                                                 | 310 ms: 1.03x faster                                                      |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 560 ms: 1.03x faster                                                      |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 537 ms: 1.02x faster                                                      |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                                      |
| coroutines                 | 22.7 ms                                                | 23.6 ms: 1.04x slower                                                     |
| async_generators           | 436 ms                                                 | 459 ms: 1.05x slower                                                      |
| async_tree_io_tg           | 857 ms                                                 | 902 ms: 1.05x slower                                                      |
| async_tree_io              | 842 ms                                                 | 938 ms: 1.11x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.01x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 70.8 ms: 1.12x faster                                                     |
| nbody          | 87.0 ms                                                | 79.6 ms: 1.09x faster                                                     |
| pidigits       | 186 ms                                                 | 186 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                  | 1.07x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.3 ms: 1.08x faster                                                     |
| regex_effbot   | 3.73 ms                                                | 3.56 ms: 1.05x faster                                                     |
| regex_dna      | 218 ms                                                 | 213 ms: 1.03x faster                                                      |
| regex_compile  | 132 ms                                                 | 141 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|---------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_generate  | 86.7 ms                                                | 77.6 ms: 1.12x faster                                                     |
| xml_etree_process   | 60.6 ms                                                | 54.5 ms: 1.11x faster                                                     |
| tomli_loads         | 2.14 sec                                               | 1.93 sec: 1.11x faster                                                    |
| json_dumps          | 10.6 ms                                                | 9.96 ms: 1.06x faster                                                     |
| xml_etree_parse     | 156 ms                                                 | 148 ms: 1.05x faster                                                      |
| pickle_pure_python  | 310 us                                                 | 302 us: 1.03x faster                                                      |
| xml_etree_iterparse | 101 ms                                                 | 98.6 ms: 1.03x faster                                                     |
| json_loads          | 27.2 us                                                | 28.8 us: 1.06x slower                                                     |
| Geometric mean      | (ref)                                                  | 1.05x faster                                                              |

Benchmark hidden because not significant (1): unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.6 ms: 1.18x faster                                                     |
| python_startup_no_site | 6.96 ms                                                | 7.17 ms: 1.03x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.07x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| mako            | 11.1 ms                                                | 9.67 ms: 1.15x faster                                                     |
| genshi_text     | 23.5 ms                                                | 24.1 ms: 1.03x slower                                                     |
| django_template | 35.2 ms                                                | 36.7 ms: 1.04x slower                                                     |
| genshi_xml      | 50.9 ms                                                | 56.7 ms: 1.11x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.01x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy_memo              | 39.1 us                                                | 26.9 us: 1.45x faster                                                     |
| deepcopy                   | 358 us                                                 | 261 us: 1.37x faster                                                      |
| create_gc_cycles           | 2.41 ms                                                | 1.79 ms: 1.34x faster                                                     |
| richards                   | 48.7 ms                                                | 39.3 ms: 1.24x faster                                                     |
| richards_super             | 54.9 ms                                                | 45.0 ms: 1.22x faster                                                     |
| deepcopy_reduce            | 3.20 us                                                | 2.63 us: 1.22x faster                                                     |
| gc_traversal               | 4.37 ms                                                | 3.67 ms: 1.19x faster                                                     |
| scimark_fft                | 364 ms                                                 | 307 ms: 1.19x faster                                                      |
| python_startup             | 12.5 ms                                                | 10.6 ms: 1.18x faster                                                     |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.30 ms: 1.17x faster                                                     |
| spectral_norm              | 115 ms                                                 | 98.5 ms: 1.17x faster                                                     |
| crypto_pyaes               | 75.3 ms                                                | 65.6 ms: 1.15x faster                                                     |
| async_tree_memoization_tg  | 464 ms                                                 | 404 ms: 1.15x faster                                                      |
| mako                       | 11.1 ms                                                | 9.67 ms: 1.15x faster                                                     |
| telco                      | 8.54 ms                                                | 7.62 ms: 1.12x faster                                                     |
| float                      | 79.2 ms                                                | 70.8 ms: 1.12x faster                                                     |
| xml_etree_generate         | 86.7 ms                                                | 77.6 ms: 1.12x faster                                                     |
| xml_etree_process          | 60.6 ms                                                | 54.5 ms: 1.11x faster                                                     |
| tomli_loads                | 2.14 sec                                               | 1.93 sec: 1.11x faster                                                    |
| pathlib                    | 17.5 ms                                                | 15.8 ms: 1.11x faster                                                     |
| nbody                      | 87.0 ms                                                | 79.6 ms: 1.09x faster                                                     |
| fannkuch                   | 404 ms                                                 | 370 ms: 1.09x faster                                                      |
| pyflate                    | 471 ms                                                 | 435 ms: 1.08x faster                                                      |
| regex_v8                   | 26.2 ms                                                | 24.3 ms: 1.08x faster                                                     |
| bpe_tokeniser              | 4.75 sec                                               | 4.40 sec: 1.08x faster                                                    |
| async_tree_none            | 351 ms                                                 | 328 ms: 1.07x faster                                                      |
| scimark_monte_carlo        | 67.4 ms                                                | 63.2 ms: 1.07x faster                                                     |
| mdp                        | 2.72 sec                                               | 2.56 sec: 1.06x faster                                                    |
| async_tree_memoization     | 442 ms                                                 | 417 ms: 1.06x faster                                                      |
| json_dumps                 | 10.6 ms                                                | 9.96 ms: 1.06x faster                                                     |
| xml_etree_parse            | 156 ms                                                 | 148 ms: 1.05x faster                                                      |
| regex_effbot               | 3.73 ms                                                | 3.56 ms: 1.05x faster                                                     |
| scimark_sor                | 124 ms                                                 | 118 ms: 1.05x faster                                                      |
| async_tree_none_tg         | 321 ms                                                 | 310 ms: 1.03x faster                                                      |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 560 ms: 1.03x faster                                                      |
| logging_format             | 6.40 us                                                | 6.21 us: 1.03x faster                                                     |
| pickle_pure_python         | 310 us                                                 | 302 us: 1.03x faster                                                      |
| xml_etree_iterparse        | 101 ms                                                 | 98.6 ms: 1.03x faster                                                     |
| regex_dna                  | 218 ms                                                 | 213 ms: 1.03x faster                                                      |
| scimark_lu                 | 113 ms                                                 | 110 ms: 1.02x faster                                                      |
| meteor_contest             | 109 ms                                                 | 107 ms: 1.02x faster                                                      |
| logging_simple             | 5.72 us                                                | 5.61 us: 1.02x faster                                                     |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 537 ms: 1.02x faster                                                      |
| bench_thread_pool          | 822 us                                                 | 816 us: 1.01x faster                                                      |
| pidigits                   | 186 ms                                                 | 186 ms: 1.00x faster                                                      |
| comprehensions             | 16.5 us                                                | 16.6 us: 1.01x slower                                                     |
| asyncio_websockets         | 552 ms                                                 | 555 ms: 1.01x slower                                                      |
| chaos                      | 58.1 ms                                                | 58.5 ms: 1.01x slower                                                     |
| pprint_pformat             | 1.49 sec                                               | 1.51 sec: 1.01x slower                                                    |
| tornado_http               | 92.4 ms                                                | 94.4 ms: 1.02x slower                                                     |
| logging_silent             | 102 ns                                                 | 104 ns: 1.02x slower                                                      |
| genshi_text                | 23.5 ms                                                | 24.1 ms: 1.03x slower                                                     |
| python_startup_no_site     | 6.96 ms                                                | 7.17 ms: 1.03x slower                                                     |
| coverage                   | 84.0 ms                                                | 87.1 ms: 1.04x slower                                                     |
| 2to3                       | 267 ms                                                 | 277 ms: 1.04x slower                                                      |
| raytrace                   | 267 ms                                                 | 277 ms: 1.04x slower                                                      |
| coroutines                 | 22.7 ms                                                | 23.6 ms: 1.04x slower                                                     |
| sqlglot_normalize          | 108 ms                                                 | 112 ms: 1.04x slower                                                      |
| django_template            | 35.2 ms                                                | 36.7 ms: 1.04x slower                                                     |
| async_generators           | 436 ms                                                 | 459 ms: 1.05x slower                                                      |
| async_tree_io_tg           | 857 ms                                                 | 902 ms: 1.05x slower                                                      |
| json_loads                 | 27.2 us                                                | 28.8 us: 1.06x slower                                                     |
| sqlglot_parse              | 1.27 ms                                                | 1.35 ms: 1.06x slower                                                     |
| regex_compile              | 132 ms                                                 | 141 ms: 1.07x slower                                                      |
| sqlglot_transpile          | 1.58 ms                                                | 1.69 ms: 1.07x slower                                                     |
| nqueens                    | 78.4 ms                                                | 84.3 ms: 1.08x slower                                                     |
| sqlglot_optimize           | 53.7 ms                                                | 58.1 ms: 1.08x slower                                                     |
| sympy_str                  | 275 ms                                                 | 299 ms: 1.09x slower                                                      |
| sympy_expand               | 463 ms                                                 | 504 ms: 1.09x slower                                                      |
| hexiom                     | 6.16 ms                                                | 6.86 ms: 1.11x slower                                                     |
| genshi_xml                 | 50.9 ms                                                | 56.7 ms: 1.11x slower                                                     |
| async_tree_io              | 842 ms                                                 | 938 ms: 1.11x slower                                                      |
| generators                 | 29.0 ms                                                | 32.6 ms: 1.13x slower                                                     |
| sympy_sum                  | 150 ms                                                 | 171 ms: 1.14x slower                                                      |
| sympy_integrate            | 19.9 ms                                                | 22.8 ms: 1.15x slower                                                     |
| docutils                   | 2.59 sec                                               | 3.04 sec: 1.17x slower                                                    |
| go                         | 144 ms                                                 | 170 ms: 1.19x slower                                                      |
| pylint                     | 313 ms                                                 | 372 ms: 1.19x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.03x faster                                                              |

Benchmark hidden because not significant (9): thrift, typing_runtime_protocols, deltablue, unpickle_pure_python, html5lib, bench_mp_pool, pycparser, pprint_safe_repr, json
Ignored benchmarks (10) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, dulwich_log, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (2) of results/bm-20240828-3.14.0a0-2d4d2a8-JIT/bm-20240828-linux-x86_64-brandtbucher-tier_two_constants-3.14.0a0-2d4d2a8.json: asyncio_tcp, asyncio_tcp_ssl

- Geometric mean (including insignificant results): 1.028x faster
# HPT report

- Reliability score: 78.12% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.99x