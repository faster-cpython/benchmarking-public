# Results vs. 3.13.0

- fork: nick-arm
- ref: codecache_rwx
- machine: linux-aarch64
- commit hash: 0442576
- commit date: 2024-10-07
- overall geometric mean: 1.067x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 0.97x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 365 ms: 1.20x slower                                                 |
| docutils       | 2.89 sec                                                 | 3.56 sec: 1.23x slower                                               |
| html5lib       | 66.4 ms                                                  | 70.6 ms: 1.06x slower                                                |
| tornado_http   | 128 ms                                                   | 149 ms: 1.16x slower                                                 |
| Geometric mean | (ref)                                                    | 1.16x slower                                                         |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 561 ms: 1.16x faster                                                 |
| async_tree_none            | 497 ms                                                   | 442 ms: 1.12x faster                                                 |
| async_tree_memoization     | 651 ms                                                   | 585 ms: 1.11x faster                                                 |
| async_tree_none_tg         | 470 ms                                                   | 427 ms: 1.10x faster                                                 |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 732 ms: 1.05x faster                                                 |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 754 ms: 1.02x faster                                                 |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.03x slower                                               |
| async_tree_io_tg           | 1.13 sec                                                 | 1.17 sec: 1.04x slower                                               |
| async_generators           | 489 ms                                                   | 517 ms: 1.06x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.04x faster                                                         |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| float          | 93.3 ms                                                  | 90.2 ms: 1.04x faster                                                |
| nbody          | 114 ms                                                   | 111 ms: 1.03x faster                                                 |
| Geometric mean | (ref)                                                    | 1.02x faster                                                         |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 4.89 ms                                                  | 5.00 ms: 1.02x slower                                                |
| regex_dna      | 253 ms                                                   | 263 ms: 1.04x slower                                                 |
| regex_compile  | 127 ms                                                   | 174 ms: 1.37x slower                                                 |
| Geometric mean | (ref)                                                    | 1.09x slower                                                         |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| xml_etree_generate   | 113 ms                                                   | 109 ms: 1.04x faster                                                 |
| json_loads           | 31.7 us                                                  | 31.1 us: 1.02x faster                                                |
| xml_etree_iterparse  | 149 ms                                                   | 151 ms: 1.01x slower                                                 |
| tomli_loads          | 2.54 sec                                                 | 2.64 sec: 1.04x slower                                               |
| unpickle_pure_python | 251 us                                                   | 265 us: 1.06x slower                                                 |
| pickle_pure_python   | 357 us                                                   | 395 us: 1.11x slower                                                 |
| Geometric mean       | (ref)                                                    | 1.01x slower                                                         |

Benchmark hidden because not significant (3): xml_etree_parse, json_dumps, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 13.1 ms: 1.17x faster                                                |
| Geometric mean | (ref)                                                    | 1.08x faster                                                         |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|-----------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako            | 13.4 ms                                                  | 13.2 ms: 1.02x faster                                                |
| genshi_text     | 27.7 ms                                                  | 33.1 ms: 1.19x slower                                                |
| django_template | 41.6 ms                                                  | 51.2 ms: 1.23x slower                                                |
| genshi_xml      | 60.3 ms                                                  | 78.1 ms: 1.29x slower                                                |
| Geometric mean  | (ref)                                                    | 1.17x slower                                                         |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576 |
|----------------------------|:--------------------------------------------------------:|:--------------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 2.28 ms: 1.47x faster                                                |
| deepcopy_memo              | 50.4 us                                                  | 37.4 us: 1.35x faster                                                |
| python_startup             | 15.4 ms                                                  | 13.1 ms: 1.17x faster                                                |
| async_tree_memoization_tg  | 649 ms                                                   | 561 ms: 1.16x faster                                                 |
| async_tree_none            | 497 ms                                                   | 442 ms: 1.12x faster                                                 |
| deepcopy                   | 447 us                                                   | 402 us: 1.11x faster                                                 |
| async_tree_memoization     | 651 ms                                                   | 585 ms: 1.11x faster                                                 |
| gc_traversal               | 5.77 ms                                                  | 5.21 ms: 1.11x faster                                                |
| async_tree_none_tg         | 470 ms                                                   | 427 ms: 1.10x faster                                                 |
| scimark_sor                | 160 ms                                                   | 151 ms: 1.06x faster                                                 |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 732 ms: 1.05x faster                                                 |
| telco                      | 9.74 ms                                                  | 9.37 ms: 1.04x faster                                                |
| xml_etree_generate         | 113 ms                                                   | 109 ms: 1.04x faster                                                 |
| pathlib                    | 22.7 ms                                                  | 21.9 ms: 1.04x faster                                                |
| float                      | 93.3 ms                                                  | 90.2 ms: 1.04x faster                                                |
| nbody                      | 114 ms                                                   | 111 ms: 1.03x faster                                                 |
| json                       | 5.73 ms                                                  | 5.54 ms: 1.03x faster                                                |
| deepcopy_reduce            | 4.07 us                                                  | 3.94 us: 1.03x faster                                                |
| json_loads                 | 31.7 us                                                  | 31.1 us: 1.02x faster                                                |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 754 ms: 1.02x faster                                                 |
| mako                       | 13.4 ms                                                  | 13.2 ms: 1.02x faster                                                |
| thrift                     | 968 us                                                   | 959 us: 1.01x faster                                                 |
| xml_etree_iterparse        | 149 ms                                                   | 151 ms: 1.01x slower                                                 |
| bpe_tokeniser              | 5.87 sec                                                 | 5.96 sec: 1.02x slower                                               |
| regex_effbot               | 4.89 ms                                                  | 5.00 ms: 1.02x slower                                                |
| mdp                        | 3.34 sec                                                 | 3.45 sec: 1.03x slower                                               |
| spectral_norm              | 143 ms                                                   | 147 ms: 1.03x slower                                                 |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.03x slower                                               |
| logging_format             | 7.82 us                                                  | 8.10 us: 1.04x slower                                                |
| async_tree_io_tg           | 1.13 sec                                                 | 1.17 sec: 1.04x slower                                               |
| regex_dna                  | 253 ms                                                   | 263 ms: 1.04x slower                                                 |
| tomli_loads                | 2.54 sec                                                 | 2.64 sec: 1.04x slower                                               |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 6.83 ms: 1.05x slower                                                |
| scimark_monte_carlo        | 83.6 ms                                                  | 88.2 ms: 1.06x slower                                                |
| async_generators           | 489 ms                                                   | 517 ms: 1.06x slower                                                 |
| unpickle_pure_python       | 251 us                                                   | 265 us: 1.06x slower                                                 |
| crypto_pyaes               | 83.7 ms                                                  | 88.6 ms: 1.06x slower                                                |
| logging_simple             | 7.07 us                                                  | 7.49 us: 1.06x slower                                                |
| richards                   | 53.6 ms                                                  | 56.9 ms: 1.06x slower                                                |
| typing_runtime_protocols   | 193 us                                                   | 205 us: 1.06x slower                                                 |
| html5lib                   | 66.4 ms                                                  | 70.6 ms: 1.06x slower                                                |
| bench_thread_pool          | 1.27 ms                                                  | 1.37 ms: 1.07x slower                                                |
| meteor_contest             | 114 ms                                                   | 123 ms: 1.08x slower                                                 |
| scimark_lu                 | 139 ms                                                   | 151 ms: 1.09x slower                                                 |
| fannkuch                   | 461 ms                                                   | 504 ms: 1.09x slower                                                 |
| pickle_pure_python         | 357 us                                                   | 395 us: 1.11x slower                                                 |
| pyflate                    | 556 ms                                                   | 620 ms: 1.11x slower                                                 |
| richards_super             | 60.1 ms                                                  | 67.3 ms: 1.12x slower                                                |
| deltablue                  | 3.82 ms                                                  | 4.34 ms: 1.14x slower                                                |
| go                         | 160 ms                                                   | 182 ms: 1.14x slower                                                 |
| raytrace                   | 300 ms                                                   | 345 ms: 1.15x slower                                                 |
| pycparser                  | 1.27 sec                                                 | 1.47 sec: 1.16x slower                                               |
| tornado_http               | 128 ms                                                   | 149 ms: 1.16x slower                                                 |
| sqlglot_normalize          | 127 ms                                                   | 149 ms: 1.18x slower                                                 |
| genshi_text                | 27.7 ms                                                  | 33.1 ms: 1.19x slower                                                |
| 2to3                       | 304 ms                                                   | 365 ms: 1.20x slower                                                 |
| comprehensions             | 20.4 us                                                  | 24.6 us: 1.21x slower                                                |
| sqlglot_parse              | 1.38 ms                                                  | 1.68 ms: 1.22x slower                                                |
| sqlglot_optimize           | 62.2 ms                                                  | 76.1 ms: 1.22x slower                                                |
| nqueens                    | 100 ms                                                   | 123 ms: 1.23x slower                                                 |
| django_template            | 41.6 ms                                                  | 51.2 ms: 1.23x slower                                                |
| docutils                   | 2.89 sec                                                 | 3.56 sec: 1.23x slower                                               |
| sympy_expand               | 457 ms                                                   | 573 ms: 1.26x slower                                                 |
| chaos                      | 68.0 ms                                                  | 86.4 ms: 1.27x slower                                                |
| sqlglot_transpile          | 1.73 ms                                                  | 2.21 ms: 1.27x slower                                                |
| genshi_xml                 | 60.3 ms                                                  | 78.1 ms: 1.29x slower                                                |
| sympy_str                  | 264 ms                                                   | 346 ms: 1.31x slower                                                 |
| pprint_safe_repr           | 926 ms                                                   | 1.22 sec: 1.32x slower                                               |
| pprint_pformat             | 1.90 sec                                                 | 2.54 sec: 1.34x slower                                               |
| pylint                     | 342 ms                                                   | 459 ms: 1.34x slower                                                 |
| regex_compile              | 127 ms                                                   | 174 ms: 1.37x slower                                                 |
| sympy_integrate            | 20.8 ms                                                  | 28.5 ms: 1.37x slower                                                |
| hexiom                     | 7.11 ms                                                  | 9.90 ms: 1.39x slower                                                |
| sympy_sum                  | 144 ms                                                   | 210 ms: 1.46x slower                                                 |
| generators                 | 37.6 ms                                                  | 58.8 ms: 1.56x slower                                                |
| bench_mp_pool              | 7.68 ms                                                  | 2.94 sec: 383.07x slower                                             |
| Geometric mean             | (ref)                                                    | 1.14x slower                                                         |

Benchmark hidden because not significant (11): xml_etree_parse, json_dumps, regex_v8, xml_etree_process, coverage, logging_silent, scimark_fft, coroutines, python_startup_no_site, pidigits, asyncio_websockets
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20241007-3.14.0a0-0442576-JIT/bm-20241007-arminc-aarch64-nick%2darm-codecache_rwx-3.14.0a0-0442576.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.067x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 0.97x