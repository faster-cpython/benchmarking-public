# Results vs. 3.13.0

- fork: python
- ref: 16cd6cc86b3ba20074ae
- machine: linux-aarch64
- commit hash: 16cd6cc
- commit date: 2024-10-05
- overall geometric mean: 1.351x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.36x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 509 ms: 1.68x slower                                                    |
| docutils       | 2.89 sec                                                 | 3.93 sec: 1.36x slower                                                  |
| html5lib       | 66.4 ms                                                  | 119 ms: 1.80x slower                                                    |
| tornado_http   | 128 ms                                                   | 202 ms: 1.58x slower                                                    |
| Geometric mean | (ref)                                                    | 1.60x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| asyncio_websockets         | 659 ms                                                   | 672 ms: 1.02x slower                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 692 ms: 1.07x slower                                                    |
| async_tree_memoization     | 651 ms                                                   | 730 ms: 1.12x slower                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 865 ms: 1.12x slower                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 895 ms: 1.17x slower                                                    |
| async_tree_io_tg           | 1.13 sec                                                 | 1.33 sec: 1.18x slower                                                  |
| async_tree_none_tg         | 470 ms                                                   | 568 ms: 1.21x slower                                                    |
| async_tree_none            | 497 ms                                                   | 623 ms: 1.25x slower                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.40 sec: 1.27x slower                                                  |
| async_generators           | 489 ms                                                   | 658 ms: 1.34x slower                                                    |
| coroutines                 | 28.5 ms                                                  | 39.2 ms: 1.38x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.19x slower                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 93.3 ms                                                  | 204 ms: 2.18x slower                                                    |
| nbody          | 114 ms                                                   | 279 ms: 2.44x slower                                                    |
| Geometric mean | (ref)                                                    | 1.75x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.89 ms                                                  | 4.44 ms: 1.10x faster                                                   |
| regex_dna      | 253 ms                                                   | 257 ms: 1.02x slower                                                    |
| regex_v8       | 31.8 ms                                                  | 33.2 ms: 1.04x slower                                                   |
| regex_compile  | 127 ms                                                   | 244 ms: 1.92x slower                                                    |
| Geometric mean | (ref)                                                    | 1.17x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                   | 184 ms: 1.07x faster                                                    |
| xml_etree_iterparse  | 149 ms                                                   | 156 ms: 1.05x slower                                                    |
| json_loads           | 31.7 us                                                  | 37.3 us: 1.18x slower                                                   |
| json_dumps           | 13.6 ms                                                  | 17.4 ms: 1.28x slower                                                   |
| xml_etree_generate   | 113 ms                                                   | 157 ms: 1.38x slower                                                    |
| xml_etree_process    | 80.5 ms                                                  | 130 ms: 1.61x slower                                                    |
| tomli_loads          | 2.54 sec                                                 | 4.12 sec: 1.62x slower                                                  |
| unpickle_pure_python | 251 us                                                   | 522 us: 2.08x slower                                                    |
| pickle_pure_python   | 357 us                                                   | 751 us: 2.10x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.42x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 15.4 ms                                                  | 18.0 ms: 1.17x slower                                                   |
| python_startup_no_site | 8.73 ms                                                  | 11.9 ms: 1.37x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.27x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.3 ms                                                  | 100 ms: 1.66x slower                                                    |
| genshi_text     | 27.7 ms                                                  | 50.4 ms: 1.82x slower                                                   |
| django_template | 41.6 ms                                                  | 80.7 ms: 1.94x slower                                                   |
| mako            | 13.4 ms                                                  | 28.4 ms: 2.13x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.88x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 1.62 ms: 2.06x faster                                                   |
| gc_traversal               | 5.77 ms                                                  | 3.47 ms: 1.66x faster                                                   |
| regex_effbot               | 4.89 ms                                                  | 4.44 ms: 1.10x faster                                                   |
| xml_etree_parse            | 197 ms                                                   | 184 ms: 1.07x faster                                                    |
| regex_dna                  | 253 ms                                                   | 257 ms: 1.02x slower                                                    |
| asyncio_websockets         | 659 ms                                                   | 672 ms: 1.02x slower                                                    |
| regex_v8                   | 31.8 ms                                                  | 33.2 ms: 1.04x slower                                                   |
| xml_etree_iterparse        | 149 ms                                                   | 156 ms: 1.05x slower                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 692 ms: 1.07x slower                                                    |
| async_tree_memoization     | 651 ms                                                   | 730 ms: 1.12x slower                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 865 ms: 1.12x slower                                                    |
| json                       | 5.73 ms                                                  | 6.65 ms: 1.16x slower                                                   |
| pathlib                    | 22.7 ms                                                  | 26.4 ms: 1.16x slower                                                   |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 895 ms: 1.17x slower                                                    |
| python_startup             | 15.4 ms                                                  | 18.0 ms: 1.17x slower                                                   |
| async_tree_io_tg           | 1.13 sec                                                 | 1.33 sec: 1.18x slower                                                  |
| json_loads                 | 31.7 us                                                  | 37.3 us: 1.18x slower                                                   |
| deepcopy                   | 447 us                                                   | 528 us: 1.18x slower                                                    |
| async_tree_none_tg         | 470 ms                                                   | 568 ms: 1.21x slower                                                    |
| scimark_fft                | 447 ms                                                   | 560 ms: 1.25x slower                                                    |
| async_tree_none            | 497 ms                                                   | 623 ms: 1.25x slower                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.40 sec: 1.27x slower                                                  |
| mdp                        | 3.34 sec                                                 | 4.26 sec: 1.28x slower                                                  |
| telco                      | 9.74 ms                                                  | 12.4 ms: 1.28x slower                                                   |
| json_dumps                 | 13.6 ms                                                  | 17.4 ms: 1.28x slower                                                   |
| coverage                   | 99.1 ms                                                  | 129 ms: 1.30x slower                                                    |
| deepcopy_memo              | 50.4 us                                                  | 67.1 us: 1.33x slower                                                   |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 8.70 ms: 1.34x slower                                                   |
| async_generators           | 489 ms                                                   | 658 ms: 1.34x slower                                                    |
| docutils                   | 2.89 sec                                                 | 3.93 sec: 1.36x slower                                                  |
| python_startup_no_site     | 8.73 ms                                                  | 11.9 ms: 1.37x slower                                                   |
| coroutines                 | 28.5 ms                                                  | 39.2 ms: 1.38x slower                                                   |
| xml_etree_generate         | 113 ms                                                   | 157 ms: 1.38x slower                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 5.71 us: 1.40x slower                                                   |
| pylint                     | 342 ms                                                   | 498 ms: 1.46x slower                                                    |
| meteor_contest             | 114 ms                                                   | 167 ms: 1.47x slower                                                    |
| nqueens                    | 100 ms                                                   | 149 ms: 1.49x slower                                                    |
| generators                 | 37.6 ms                                                  | 57.3 ms: 1.52x slower                                                   |
| spectral_norm              | 143 ms                                                   | 220 ms: 1.55x slower                                                    |
| bench_thread_pool          | 1.27 ms                                                  | 1.98 ms: 1.55x slower                                                   |
| bpe_tokeniser              | 5.87 sec                                                 | 9.20 sec: 1.57x slower                                                  |
| pycparser                  | 1.27 sec                                                 | 2.01 sec: 1.58x slower                                                  |
| tornado_http               | 128 ms                                                   | 202 ms: 1.58x slower                                                    |
| xml_etree_process          | 80.5 ms                                                  | 130 ms: 1.61x slower                                                    |
| fannkuch                   | 461 ms                                                   | 743 ms: 1.61x slower                                                    |
| tomli_loads                | 2.54 sec                                                 | 4.12 sec: 1.62x slower                                                  |
| crypto_pyaes               | 83.7 ms                                                  | 137 ms: 1.64x slower                                                    |
| genshi_xml                 | 60.3 ms                                                  | 100 ms: 1.66x slower                                                    |
| typing_runtime_protocols   | 193 us                                                   | 322 us: 1.66x slower                                                    |
| sympy_integrate            | 20.8 ms                                                  | 34.8 ms: 1.67x slower                                                   |
| thrift                     | 968 us                                                   | 1.62 ms: 1.67x slower                                                   |
| 2to3                       | 304 ms                                                   | 509 ms: 1.68x slower                                                    |
| sqlglot_normalize          | 127 ms                                                   | 218 ms: 1.72x slower                                                    |
| sqlglot_optimize           | 62.2 ms                                                  | 111 ms: 1.79x slower                                                    |
| pprint_safe_repr           | 926 ms                                                   | 1.66 sec: 1.79x slower                                                  |
| pprint_pformat             | 1.90 sec                                                 | 3.40 sec: 1.79x slower                                                  |
| html5lib                   | 66.4 ms                                                  | 119 ms: 1.80x slower                                                    |
| pyflate                    | 556 ms                                                   | 1.00 sec: 1.80x slower                                                  |
| genshi_text                | 27.7 ms                                                  | 50.4 ms: 1.82x slower                                                   |
| sympy_str                  | 264 ms                                                   | 503 ms: 1.90x slower                                                    |
| logging_format             | 7.82 us                                                  | 15.0 us: 1.91x slower                                                   |
| regex_compile              | 127 ms                                                   | 244 ms: 1.92x slower                                                    |
| django_template            | 41.6 ms                                                  | 80.7 ms: 1.94x slower                                                   |
| logging_simple             | 7.07 us                                                  | 13.8 us: 1.95x slower                                                   |
| comprehensions             | 20.4 us                                                  | 40.3 us: 1.98x slower                                                   |
| sympy_expand               | 457 ms                                                   | 926 ms: 2.03x slower                                                    |
| scimark_monte_carlo        | 83.6 ms                                                  | 173 ms: 2.07x slower                                                    |
| unpickle_pure_python       | 251 us                                                   | 522 us: 2.08x slower                                                    |
| pickle_pure_python         | 357 us                                                   | 751 us: 2.10x slower                                                    |
| scimark_sor                | 160 ms                                                   | 336 ms: 2.10x slower                                                    |
| logging_silent             | 133 ns                                                   | 281 ns: 2.11x slower                                                    |
| mako                       | 13.4 ms                                                  | 28.4 ms: 2.13x slower                                                   |
| hexiom                     | 7.11 ms                                                  | 15.3 ms: 2.15x slower                                                   |
| sympy_sum                  | 144 ms                                                   | 309 ms: 2.15x slower                                                    |
| float                      | 93.3 ms                                                  | 204 ms: 2.18x slower                                                    |
| richards                   | 53.6 ms                                                  | 118 ms: 2.21x slower                                                    |
| richards_super             | 60.1 ms                                                  | 136 ms: 2.26x slower                                                    |
| chaos                      | 68.0 ms                                                  | 157 ms: 2.31x slower                                                    |
| scimark_lu                 | 139 ms                                                   | 326 ms: 2.34x slower                                                    |
| go                         | 160 ms                                                   | 387 ms: 2.42x slower                                                    |
| nbody                      | 114 ms                                                   | 279 ms: 2.44x slower                                                    |
| sqlglot_transpile          | 1.73 ms                                                  | 4.26 ms: 2.46x slower                                                   |
| sqlglot_parse              | 1.38 ms                                                  | 3.68 ms: 2.67x slower                                                   |
| raytrace                   | 300 ms                                                   | 803 ms: 2.68x slower                                                    |
| deltablue                  | 3.82 ms                                                  | 12.4 ms: 3.25x slower                                                   |
| bench_mp_pool              | 7.68 ms                                                  | 40.1 ms: 5.22x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.57x slower                                                            |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20241005-3.14.0a0-16cd6cc-NOGIL/bm-20241005-arminc-aarch64-python-16cd6cc86b3ba20074ae-3.14.0a0-16cd6cc.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.351x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.45x
- 95% likely to have a slowdown of 1.41x
- 99% likely to have a slowdown of 1.36x

# Memory
- memory change: 1.06x