# Results vs. 3.13.0

- fork: nick-arm
- ref: codecache
- machine: linux-aarch64
- commit hash: aa18ec3
- commit date: 2024-10-07
- overall geometric mean: 1.074x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 374 ms: 1.23x slower                                             |
| docutils       | 2.89 sec                                                 | 3.63 sec: 1.26x slower                                           |
| html5lib       | 66.4 ms                                                  | 71.3 ms: 1.07x slower                                            |
| tornado_http   | 128 ms                                                   | 142 ms: 1.11x slower                                             |
| Geometric mean | (ref)                                                    | 1.17x slower                                                     |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 561 ms: 1.16x faster                                             |
| async_tree_none            | 497 ms                                                   | 448 ms: 1.11x faster                                             |
| async_tree_none_tg         | 470 ms                                                   | 426 ms: 1.10x faster                                             |
| async_tree_memoization     | 651 ms                                                   | 591 ms: 1.10x faster                                             |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 744 ms: 1.03x faster                                             |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 752 ms: 1.02x faster                                             |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                           |
| async_generators           | 489 ms                                                   | 507 ms: 1.04x slower                                             |
| async_tree_io_tg           | 1.13 sec                                                 | 1.18 sec: 1.04x slower                                           |
| Geometric mean             | (ref)                                                    | 1.03x faster                                                     |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| float          | 93.3 ms                                                  | 90.0 ms: 1.04x faster                                            |
| Geometric mean | (ref)                                                    | 1.02x faster                                                     |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| regex_dna      | 253 ms                                                   | 247 ms: 1.03x faster                                             |
| regex_v8       | 31.8 ms                                                  | 31.4 ms: 1.01x faster                                            |
| regex_compile  | 127 ms                                                   | 181 ms: 1.42x slower                                             |
| Geometric mean | (ref)                                                    | 1.08x slower                                                     |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| xml_etree_generate   | 113 ms                                                   | 110 ms: 1.03x faster                                             |
| json_loads           | 31.7 us                                                  | 31.0 us: 1.02x faster                                            |
| xml_etree_iterparse  | 149 ms                                                   | 152 ms: 1.02x slower                                             |
| tomli_loads          | 2.54 sec                                                 | 2.61 sec: 1.03x slower                                           |
| unpickle_pure_python | 251 us                                                   | 267 us: 1.07x slower                                             |
| pickle_pure_python   | 357 us                                                   | 384 us: 1.08x slower                                             |
| Geometric mean       | (ref)                                                    | 1.01x slower                                                     |

Benchmark hidden because not significant (3): json_dumps, xml_etree_parse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 13.1 ms: 1.18x faster                                            |
| Geometric mean | (ref)                                                    | 1.08x faster                                                     |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|-----------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| mako            | 13.4 ms                                                  | 13.2 ms: 1.02x faster                                            |
| django_template | 41.6 ms                                                  | 51.9 ms: 1.25x slower                                            |
| genshi_text     | 27.7 ms                                                  | 34.8 ms: 1.26x slower                                            |
| genshi_xml      | 60.3 ms                                                  | 83.0 ms: 1.38x slower                                            |
| Geometric mean  | (ref)                                                    | 1.21x slower                                                     |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3 |
|----------------------------|:--------------------------------------------------------:|:----------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 2.31 ms: 1.45x faster                                            |
| deepcopy_memo              | 50.4 us                                                  | 37.4 us: 1.35x faster                                            |
| python_startup             | 15.4 ms                                                  | 13.1 ms: 1.18x faster                                            |
| async_tree_memoization_tg  | 649 ms                                                   | 561 ms: 1.16x faster                                             |
| async_tree_none            | 497 ms                                                   | 448 ms: 1.11x faster                                             |
| gc_traversal               | 5.77 ms                                                  | 5.21 ms: 1.11x faster                                            |
| deepcopy                   | 447 us                                                   | 405 us: 1.10x faster                                             |
| async_tree_none_tg         | 470 ms                                                   | 426 ms: 1.10x faster                                             |
| async_tree_memoization     | 651 ms                                                   | 591 ms: 1.10x faster                                             |
| deepcopy_reduce            | 4.07 us                                                  | 3.85 us: 1.06x faster                                            |
| pathlib                    | 22.7 ms                                                  | 21.5 ms: 1.05x faster                                            |
| float                      | 93.3 ms                                                  | 90.0 ms: 1.04x faster                                            |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 744 ms: 1.03x faster                                             |
| json                       | 5.73 ms                                                  | 5.57 ms: 1.03x faster                                            |
| xml_etree_generate         | 113 ms                                                   | 110 ms: 1.03x faster                                             |
| regex_dna                  | 253 ms                                                   | 247 ms: 1.03x faster                                             |
| json_loads                 | 31.7 us                                                  | 31.0 us: 1.02x faster                                            |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 752 ms: 1.02x faster                                             |
| mako                       | 13.4 ms                                                  | 13.2 ms: 1.02x faster                                            |
| regex_v8                   | 31.8 ms                                                  | 31.4 ms: 1.01x faster                                            |
| thrift                     | 968 us                                                   | 960 us: 1.01x faster                                             |
| scimark_fft                | 447 ms                                                   | 444 ms: 1.01x faster                                             |
| telco                      | 9.74 ms                                                  | 9.86 ms: 1.01x slower                                            |
| xml_etree_iterparse        | 149 ms                                                   | 152 ms: 1.02x slower                                             |
| bpe_tokeniser              | 5.87 sec                                                 | 5.99 sec: 1.02x slower                                           |
| spectral_norm              | 143 ms                                                   | 145 ms: 1.02x slower                                             |
| logging_format             | 7.82 us                                                  | 8.02 us: 1.03x slower                                            |
| tomli_loads                | 2.54 sec                                                 | 2.61 sec: 1.03x slower                                           |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                           |
| async_generators           | 489 ms                                                   | 507 ms: 1.04x slower                                             |
| async_tree_io_tg           | 1.13 sec                                                 | 1.18 sec: 1.04x slower                                           |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 6.79 ms: 1.04x slower                                            |
| logging_simple             | 7.07 us                                                  | 7.40 us: 1.05x slower                                            |
| scimark_sor                | 160 ms                                                   | 167 ms: 1.05x slower                                             |
| mdp                        | 3.34 sec                                                 | 3.50 sec: 1.05x slower                                           |
| scimark_monte_carlo        | 83.6 ms                                                  | 87.5 ms: 1.05x slower                                            |
| crypto_pyaes               | 83.7 ms                                                  | 88.1 ms: 1.05x slower                                            |
| unpickle_pure_python       | 251 us                                                   | 267 us: 1.07x slower                                             |
| bench_thread_pool          | 1.27 ms                                                  | 1.37 ms: 1.07x slower                                            |
| html5lib                   | 66.4 ms                                                  | 71.3 ms: 1.07x slower                                            |
| pickle_pure_python         | 357 us                                                   | 384 us: 1.08x slower                                             |
| scimark_lu                 | 139 ms                                                   | 150 ms: 1.08x slower                                             |
| typing_runtime_protocols   | 193 us                                                   | 211 us: 1.09x slower                                             |
| fannkuch                   | 461 ms                                                   | 503 ms: 1.09x slower                                             |
| meteor_contest             | 114 ms                                                   | 125 ms: 1.10x slower                                             |
| tornado_http               | 128 ms                                                   | 142 ms: 1.11x slower                                             |
| pyflate                    | 556 ms                                                   | 617 ms: 1.11x slower                                             |
| richards                   | 53.6 ms                                                  | 60.3 ms: 1.13x slower                                            |
| deltablue                  | 3.82 ms                                                  | 4.38 ms: 1.15x slower                                            |
| pycparser                  | 1.27 sec                                                 | 1.47 sec: 1.15x slower                                           |
| raytrace                   | 300 ms                                                   | 347 ms: 1.16x slower                                             |
| richards_super             | 60.1 ms                                                  | 70.7 ms: 1.18x slower                                            |
| go                         | 160 ms                                                   | 189 ms: 1.18x slower                                             |
| comprehensions             | 20.4 us                                                  | 24.5 us: 1.20x slower                                            |
| nqueens                    | 100 ms                                                   | 122 ms: 1.22x slower                                             |
| sqlglot_normalize          | 127 ms                                                   | 155 ms: 1.22x slower                                             |
| sqlglot_parse              | 1.38 ms                                                  | 1.68 ms: 1.22x slower                                            |
| 2to3                       | 304 ms                                                   | 374 ms: 1.23x slower                                             |
| django_template            | 41.6 ms                                                  | 51.9 ms: 1.25x slower                                            |
| docutils                   | 2.89 sec                                                 | 3.63 sec: 1.26x slower                                           |
| genshi_text                | 27.7 ms                                                  | 34.8 ms: 1.26x slower                                            |
| sqlglot_transpile          | 1.73 ms                                                  | 2.22 ms: 1.28x slower                                            |
| sqlglot_optimize           | 62.2 ms                                                  | 80.2 ms: 1.29x slower                                            |
| sympy_expand               | 457 ms                                                   | 591 ms: 1.29x slower                                             |
| pprint_safe_repr           | 926 ms                                                   | 1.20 sec: 1.30x slower                                           |
| chaos                      | 68.0 ms                                                  | 88.3 ms: 1.30x slower                                            |
| pprint_pformat             | 1.90 sec                                                 | 2.50 sec: 1.32x slower                                           |
| sympy_str                  | 264 ms                                                   | 358 ms: 1.36x slower                                             |
| genshi_xml                 | 60.3 ms                                                  | 83.0 ms: 1.38x slower                                            |
| pylint                     | 342 ms                                                   | 472 ms: 1.38x slower                                             |
| sympy_integrate            | 20.8 ms                                                  | 28.8 ms: 1.38x slower                                            |
| regex_compile              | 127 ms                                                   | 181 ms: 1.42x slower                                             |
| hexiom                     | 7.11 ms                                                  | 10.1 ms: 1.42x slower                                            |
| sympy_sum                  | 144 ms                                                   | 214 ms: 1.49x slower                                             |
| generators                 | 37.6 ms                                                  | 59.3 ms: 1.58x slower                                            |
| bench_mp_pool              | 7.68 ms                                                  | 1.89 sec: 246.48x slower                                         |
| Geometric mean             | (ref)                                                    | 1.15x slower                                                     |

Benchmark hidden because not significant (11): json_dumps, xml_etree_parse, nbody, xml_etree_process, logging_silent, coverage, regex_effbot, pidigits, asyncio_websockets, coroutines, python_startup_no_site
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20241007-3.14.0a0-aa18ec3-JIT/bm-20241007-arminc-aarch64-nick%2darm-codecache-3.14.0a0-aa18ec3.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.074x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 0.98x