# Results vs. 3.13.0

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: linux-aarch64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.079x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 0.96x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 383 ms: 1.26x slower                                                    |
| docutils       | 2.89 sec                                                 | 3.71 sec: 1.28x slower                                                  |
| html5lib       | 66.4 ms                                                  | 71.0 ms: 1.07x slower                                                   |
| tornado_http   | 128 ms                                                   | 147 ms: 1.15x slower                                                    |
| Geometric mean | (ref)                                                    | 1.19x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 561 ms: 1.16x faster                                                    |
| async_tree_none_tg         | 470 ms                                                   | 420 ms: 1.12x faster                                                    |
| async_tree_none            | 497 ms                                                   | 445 ms: 1.12x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 591 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 739 ms: 1.04x faster                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 753 ms: 1.02x faster                                                    |
| coroutines                 | 28.5 ms                                                  | 29.0 ms: 1.02x slower                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                  |
| async_generators           | 489 ms                                                   | 508 ms: 1.04x slower                                                    |
| async_tree_io_tg           | 1.13 sec                                                 | 1.18 sec: 1.04x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 93.3 ms                                                  | 90.0 ms: 1.04x faster                                                   |
| nbody          | 114 ms                                                   | 112 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 31.0 ms: 1.03x faster                                                   |
| regex_effbot   | 4.89 ms                                                  | 5.02 ms: 1.03x slower                                                   |
| regex_dna      | 253 ms                                                   | 262 ms: 1.03x slower                                                    |
| regex_compile  | 127 ms                                                   | 184 ms: 1.45x slower                                                    |
| Geometric mean | (ref)                                                    | 1.11x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                   | 188 ms: 1.05x faster                                                    |
| json_loads           | 31.7 us                                                  | 31.1 us: 1.02x faster                                                   |
| tomli_loads          | 2.54 sec                                                 | 2.64 sec: 1.04x slower                                                  |
| unpickle_pure_python | 251 us                                                   | 268 us: 1.07x slower                                                    |
| pickle_pure_python   | 357 us                                                   | 386 us: 1.08x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (4): json_dumps, xml_etree_generate, xml_etree_iterparse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 12.9 ms: 1.19x faster                                                   |
| Geometric mean | (ref)                                                    | 1.09x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.4 ms                                                  | 13.0 ms: 1.03x faster                                                   |
| genshi_text     | 27.7 ms                                                  | 34.4 ms: 1.24x slower                                                   |
| django_template | 41.6 ms                                                  | 51.8 ms: 1.24x slower                                                   |
| genshi_xml      | 60.3 ms                                                  | 83.1 ms: 1.38x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.20x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 2.29 ms: 1.46x faster                                                   |
| deepcopy_memo              | 50.4 us                                                  | 37.9 us: 1.33x faster                                                   |
| python_startup             | 15.4 ms                                                  | 12.9 ms: 1.19x faster                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 561 ms: 1.16x faster                                                    |
| gc_traversal               | 5.77 ms                                                  | 5.05 ms: 1.14x faster                                                   |
| async_tree_none_tg         | 470 ms                                                   | 420 ms: 1.12x faster                                                    |
| deepcopy                   | 447 us                                                   | 400 us: 1.12x faster                                                    |
| async_tree_none            | 497 ms                                                   | 445 ms: 1.12x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 591 ms: 1.10x faster                                                    |
| scimark_sor                | 160 ms                                                   | 152 ms: 1.05x faster                                                    |
| xml_etree_parse            | 197 ms                                                   | 188 ms: 1.05x faster                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 739 ms: 1.04x faster                                                    |
| pathlib                    | 22.7 ms                                                  | 21.8 ms: 1.04x faster                                                   |
| float                      | 93.3 ms                                                  | 90.0 ms: 1.04x faster                                                   |
| deepcopy_reduce            | 4.07 us                                                  | 3.93 us: 1.04x faster                                                   |
| json                       | 5.73 ms                                                  | 5.57 ms: 1.03x faster                                                   |
| regex_v8                   | 31.8 ms                                                  | 31.0 ms: 1.03x faster                                                   |
| nbody                      | 114 ms                                                   | 112 ms: 1.03x faster                                                    |
| mako                       | 13.4 ms                                                  | 13.0 ms: 1.03x faster                                                   |
| json_loads                 | 31.7 us                                                  | 31.1 us: 1.02x faster                                                   |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 753 ms: 1.02x faster                                                    |
| logging_silent             | 133 ns                                                   | 131 ns: 1.02x faster                                                    |
| bpe_tokeniser              | 5.87 sec                                                 | 5.97 sec: 1.02x slower                                                  |
| coroutines                 | 28.5 ms                                                  | 29.0 ms: 1.02x slower                                                   |
| regex_effbot               | 4.89 ms                                                  | 5.02 ms: 1.03x slower                                                   |
| regex_dna                  | 253 ms                                                   | 262 ms: 1.03x slower                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                  |
| logging_format             | 7.82 us                                                  | 8.11 us: 1.04x slower                                                   |
| async_generators           | 489 ms                                                   | 508 ms: 1.04x slower                                                    |
| async_tree_io_tg           | 1.13 sec                                                 | 1.18 sec: 1.04x slower                                                  |
| tomli_loads                | 2.54 sec                                                 | 2.64 sec: 1.04x slower                                                  |
| mdp                        | 3.34 sec                                                 | 3.48 sec: 1.04x slower                                                  |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 6.87 ms: 1.06x slower                                                   |
| logging_simple             | 7.07 us                                                  | 7.54 us: 1.07x slower                                                   |
| scimark_monte_carlo        | 83.6 ms                                                  | 89.1 ms: 1.07x slower                                                   |
| unpickle_pure_python       | 251 us                                                   | 268 us: 1.07x slower                                                    |
| html5lib                   | 66.4 ms                                                  | 71.0 ms: 1.07x slower                                                   |
| crypto_pyaes               | 83.7 ms                                                  | 89.9 ms: 1.07x slower                                                   |
| scimark_lu                 | 139 ms                                                   | 150 ms: 1.08x slower                                                    |
| bench_thread_pool          | 1.27 ms                                                  | 1.37 ms: 1.08x slower                                                   |
| pickle_pure_python         | 357 us                                                   | 386 us: 1.08x slower                                                    |
| meteor_contest             | 114 ms                                                   | 124 ms: 1.09x slower                                                    |
| fannkuch                   | 461 ms                                                   | 503 ms: 1.09x slower                                                    |
| typing_runtime_protocols   | 193 us                                                   | 213 us: 1.10x slower                                                    |
| deltablue                  | 3.82 ms                                                  | 4.35 ms: 1.14x slower                                                   |
| pyflate                    | 556 ms                                                   | 640 ms: 1.15x slower                                                    |
| tornado_http               | 128 ms                                                   | 147 ms: 1.15x slower                                                    |
| go                         | 160 ms                                                   | 185 ms: 1.16x slower                                                    |
| pycparser                  | 1.27 sec                                                 | 1.48 sec: 1.16x slower                                                  |
| raytrace                   | 300 ms                                                   | 350 ms: 1.17x slower                                                    |
| richards                   | 53.6 ms                                                  | 63.8 ms: 1.19x slower                                                   |
| richards_super             | 60.1 ms                                                  | 72.0 ms: 1.20x slower                                                   |
| comprehensions             | 20.4 us                                                  | 24.9 us: 1.22x slower                                                   |
| sqlglot_normalize          | 127 ms                                                   | 156 ms: 1.23x slower                                                    |
| nqueens                    | 100 ms                                                   | 124 ms: 1.24x slower                                                    |
| genshi_text                | 27.7 ms                                                  | 34.4 ms: 1.24x slower                                                   |
| django_template            | 41.6 ms                                                  | 51.8 ms: 1.24x slower                                                   |
| sqlglot_parse              | 1.38 ms                                                  | 1.74 ms: 1.26x slower                                                   |
| 2to3                       | 304 ms                                                   | 383 ms: 1.26x slower                                                    |
| sqlglot_transpile          | 1.73 ms                                                  | 2.21 ms: 1.28x slower                                                   |
| docutils                   | 2.89 sec                                                 | 3.71 sec: 1.28x slower                                                  |
| sympy_expand               | 457 ms                                                   | 598 ms: 1.31x slower                                                    |
| sqlglot_optimize           | 62.2 ms                                                  | 82.2 ms: 1.32x slower                                                   |
| pprint_safe_repr           | 926 ms                                                   | 1.23 sec: 1.33x slower                                                  |
| chaos                      | 68.0 ms                                                  | 90.5 ms: 1.33x slower                                                   |
| pprint_pformat             | 1.90 sec                                                 | 2.61 sec: 1.37x slower                                                  |
| genshi_xml                 | 60.3 ms                                                  | 83.1 ms: 1.38x slower                                                   |
| sympy_str                  | 264 ms                                                   | 366 ms: 1.39x slower                                                    |
| sympy_integrate            | 20.8 ms                                                  | 29.6 ms: 1.42x slower                                                   |
| hexiom                     | 7.11 ms                                                  | 10.1 ms: 1.42x slower                                                   |
| pylint                     | 342 ms                                                   | 486 ms: 1.42x slower                                                    |
| regex_compile              | 127 ms                                                   | 184 ms: 1.45x slower                                                    |
| sympy_sum                  | 144 ms                                                   | 218 ms: 1.52x slower                                                    |
| generators                 | 37.6 ms                                                  | 59.2 ms: 1.57x slower                                                   |
| bench_mp_pool              | 7.68 ms                                                  | 2.07 sec: 269.01x slower                                                |
| Geometric mean             | (ref)                                                    | 1.15x slower                                                            |

Benchmark hidden because not significant (12): json_dumps, xml_etree_generate, thrift, scimark_fft, python_startup_no_site, telco, pidigits, xml_etree_iterparse, asyncio_websockets, xml_etree_process, spectral_norm, coverage
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20241005-3.14.0a0-16cd6cc-JIT/bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.079x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 0.96x