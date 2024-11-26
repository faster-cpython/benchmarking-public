# Results vs. 3.13.0

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: linux-aarch64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.353x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.36x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 509 ms: 1.68x slower                                                    |
| docutils       | 2.89 sec                                                 | 3.97 sec: 1.37x slower                                                  |
| html5lib       | 66.4 ms                                                  | 118 ms: 1.78x slower                                                    |
| tornado_http   | 128 ms                                                   | 203 ms: 1.59x slower                                                    |
| Geometric mean | (ref)                                                    | 1.60x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| asyncio_websockets         | 659 ms                                                   | 672 ms: 1.02x slower                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 692 ms: 1.07x slower                                                    |
| async_tree_memoization     | 651 ms                                                   | 723 ms: 1.11x slower                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 866 ms: 1.13x slower                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 901 ms: 1.18x slower                                                    |
| async_tree_io_tg           | 1.13 sec                                                 | 1.34 sec: 1.18x slower                                                  |
| async_tree_none_tg         | 470 ms                                                   | 562 ms: 1.20x slower                                                    |
| async_tree_none            | 497 ms                                                   | 600 ms: 1.21x slower                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.37 sec: 1.24x slower                                                  |
| async_generators           | 489 ms                                                   | 656 ms: 1.34x slower                                                    |
| coroutines                 | 28.5 ms                                                  | 39.2 ms: 1.38x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.18x slower                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 93.3 ms                                                  | 205 ms: 2.19x slower                                                    |
| nbody          | 114 ms                                                   | 281 ms: 2.46x slower                                                    |
| Geometric mean | (ref)                                                    | 1.75x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.89 ms                                                  | 4.47 ms: 1.09x faster                                                   |
| regex_v8       | 31.8 ms                                                  | 32.2 ms: 1.01x slower                                                   |
| regex_dna      | 253 ms                                                   | 258 ms: 1.02x slower                                                    |
| regex_compile  | 127 ms                                                   | 246 ms: 1.93x slower                                                    |
| Geometric mean | (ref)                                                    | 1.16x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                   | 183 ms: 1.07x faster                                                    |
| xml_etree_iterparse  | 149 ms                                                   | 153 ms: 1.02x slower                                                    |
| json_loads           | 31.7 us                                                  | 38.1 us: 1.20x slower                                                   |
| json_dumps           | 13.6 ms                                                  | 17.4 ms: 1.28x slower                                                   |
| xml_etree_generate   | 113 ms                                                   | 155 ms: 1.37x slower                                                    |
| xml_etree_process    | 80.5 ms                                                  | 125 ms: 1.55x slower                                                    |
| tomli_loads          | 2.54 sec                                                 | 4.12 sec: 1.62x slower                                                  |
| unpickle_pure_python | 251 us                                                   | 525 us: 2.10x slower                                                    |
| pickle_pure_python   | 357 us                                                   | 749 us: 2.10x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.41x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 15.4 ms                                                  | 18.1 ms: 1.17x slower                                                   |
| python_startup_no_site | 8.73 ms                                                  | 12.0 ms: 1.37x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.27x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.3 ms                                                  | 100 ms: 1.66x slower                                                    |
| genshi_text     | 27.7 ms                                                  | 51.0 ms: 1.84x slower                                                   |
| django_template | 41.6 ms                                                  | 79.2 ms: 1.90x slower                                                   |
| mako            | 13.4 ms                                                  | 28.4 ms: 2.13x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.88x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 1.60 ms: 2.09x faster                                                   |
| gc_traversal               | 5.77 ms                                                  | 3.46 ms: 1.67x faster                                                   |
| bench_mp_pool              | 7.68 ms                                                  | 6.94 ms: 1.11x faster                                                   |
| regex_effbot               | 4.89 ms                                                  | 4.47 ms: 1.09x faster                                                   |
| xml_etree_parse            | 197 ms                                                   | 183 ms: 1.07x faster                                                    |
| regex_v8                   | 31.8 ms                                                  | 32.2 ms: 1.01x slower                                                   |
| regex_dna                  | 253 ms                                                   | 258 ms: 1.02x slower                                                    |
| asyncio_websockets         | 659 ms                                                   | 672 ms: 1.02x slower                                                    |
| xml_etree_iterparse        | 149 ms                                                   | 153 ms: 1.02x slower                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 692 ms: 1.07x slower                                                    |
| async_tree_memoization     | 651 ms                                                   | 723 ms: 1.11x slower                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 866 ms: 1.13x slower                                                    |
| pathlib                    | 22.7 ms                                                  | 26.1 ms: 1.15x slower                                                   |
| python_startup             | 15.4 ms                                                  | 18.1 ms: 1.17x slower                                                   |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 901 ms: 1.18x slower                                                    |
| json                       | 5.73 ms                                                  | 6.75 ms: 1.18x slower                                                   |
| async_tree_io_tg           | 1.13 sec                                                 | 1.34 sec: 1.18x slower                                                  |
| deepcopy                   | 447 us                                                   | 530 us: 1.19x slower                                                    |
| async_tree_none_tg         | 470 ms                                                   | 562 ms: 1.20x slower                                                    |
| json_loads                 | 31.7 us                                                  | 38.1 us: 1.20x slower                                                   |
| async_tree_none            | 497 ms                                                   | 600 ms: 1.21x slower                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.37 sec: 1.24x slower                                                  |
| json_dumps                 | 13.6 ms                                                  | 17.4 ms: 1.28x slower                                                   |
| mdp                        | 3.34 sec                                                 | 4.29 sec: 1.29x slower                                                  |
| scimark_fft                | 447 ms                                                   | 579 ms: 1.30x slower                                                    |
| telco                      | 9.74 ms                                                  | 12.7 ms: 1.30x slower                                                   |
| coverage                   | 99.1 ms                                                  | 130 ms: 1.31x slower                                                    |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 8.64 ms: 1.33x slower                                                   |
| async_generators           | 489 ms                                                   | 656 ms: 1.34x slower                                                    |
| deepcopy_memo              | 50.4 us                                                  | 67.7 us: 1.34x slower                                                   |
| xml_etree_generate         | 113 ms                                                   | 155 ms: 1.37x slower                                                    |
| python_startup_no_site     | 8.73 ms                                                  | 12.0 ms: 1.37x slower                                                   |
| docutils                   | 2.89 sec                                                 | 3.97 sec: 1.37x slower                                                  |
| coroutines                 | 28.5 ms                                                  | 39.2 ms: 1.38x slower                                                   |
| deepcopy_reduce            | 4.07 us                                                  | 5.71 us: 1.40x slower                                                   |
| meteor_contest             | 114 ms                                                   | 167 ms: 1.47x slower                                                    |
| pylint                     | 342 ms                                                   | 506 ms: 1.48x slower                                                    |
| nqueens                    | 100 ms                                                   | 149 ms: 1.49x slower                                                    |
| generators                 | 37.6 ms                                                  | 58.3 ms: 1.55x slower                                                   |
| xml_etree_process          | 80.5 ms                                                  | 125 ms: 1.55x slower                                                    |
| pycparser                  | 1.27 sec                                                 | 1.99 sec: 1.57x slower                                                  |
| bench_thread_pool          | 1.27 ms                                                  | 2.02 ms: 1.59x slower                                                   |
| bpe_tokeniser              | 5.87 sec                                                 | 9.33 sec: 1.59x slower                                                  |
| tornado_http               | 128 ms                                                   | 203 ms: 1.59x slower                                                    |
| fannkuch                   | 461 ms                                                   | 741 ms: 1.61x slower                                                    |
| spectral_norm              | 143 ms                                                   | 231 ms: 1.62x slower                                                    |
| tomli_loads                | 2.54 sec                                                 | 4.12 sec: 1.62x slower                                                  |
| crypto_pyaes               | 83.7 ms                                                  | 137 ms: 1.64x slower                                                    |
| sympy_integrate            | 20.8 ms                                                  | 34.4 ms: 1.65x slower                                                   |
| genshi_xml                 | 60.3 ms                                                  | 100 ms: 1.66x slower                                                    |
| typing_runtime_protocols   | 193 us                                                   | 324 us: 1.68x slower                                                    |
| 2to3                       | 304 ms                                                   | 509 ms: 1.68x slower                                                    |
| thrift                     | 968 us                                                   | 1.63 ms: 1.69x slower                                                   |
| sqlglot_normalize          | 127 ms                                                   | 219 ms: 1.72x slower                                                    |
| sqlglot_optimize           | 62.2 ms                                                  | 109 ms: 1.76x slower                                                    |
| html5lib                   | 66.4 ms                                                  | 118 ms: 1.78x slower                                                    |
| pprint_safe_repr           | 926 ms                                                   | 1.65 sec: 1.78x slower                                                  |
| pprint_pformat             | 1.90 sec                                                 | 3.40 sec: 1.79x slower                                                  |
| pyflate                    | 556 ms                                                   | 1.00 sec: 1.80x slower                                                  |
| genshi_text                | 27.7 ms                                                  | 51.0 ms: 1.84x slower                                                   |
| django_template            | 41.6 ms                                                  | 79.2 ms: 1.90x slower                                                   |
| sympy_str                  | 264 ms                                                   | 507 ms: 1.92x slower                                                    |
| regex_compile              | 127 ms                                                   | 246 ms: 1.93x slower                                                    |
| comprehensions             | 20.4 us                                                  | 40.1 us: 1.97x slower                                                   |
| logging_format             | 7.82 us                                                  | 15.5 us: 1.99x slower                                                   |
| logging_simple             | 7.07 us                                                  | 14.1 us: 1.99x slower                                                   |
| sympy_expand               | 457 ms                                                   | 936 ms: 2.05x slower                                                    |
| scimark_monte_carlo        | 83.6 ms                                                  | 172 ms: 2.05x slower                                                    |
| unpickle_pure_python       | 251 us                                                   | 525 us: 2.10x slower                                                    |
| pickle_pure_python         | 357 us                                                   | 749 us: 2.10x slower                                                    |
| mako                       | 13.4 ms                                                  | 28.4 ms: 2.13x slower                                                   |
| scimark_sor                | 160 ms                                                   | 341 ms: 2.14x slower                                                    |
| logging_silent             | 133 ns                                                   | 285 ns: 2.14x slower                                                    |
| hexiom                     | 7.11 ms                                                  | 15.3 ms: 2.15x slower                                                   |
| float                      | 93.3 ms                                                  | 205 ms: 2.19x slower                                                    |
| sympy_sum                  | 144 ms                                                   | 317 ms: 2.20x slower                                                    |
| richards                   | 53.6 ms                                                  | 119 ms: 2.22x slower                                                    |
| richards_super             | 60.1 ms                                                  | 140 ms: 2.33x slower                                                    |
| chaos                      | 68.0 ms                                                  | 160 ms: 2.35x slower                                                    |
| scimark_lu                 | 139 ms                                                   | 329 ms: 2.36x slower                                                    |
| go                         | 160 ms                                                   | 382 ms: 2.39x slower                                                    |
| sqlglot_transpile          | 1.73 ms                                                  | 4.22 ms: 2.44x slower                                                   |
| nbody                      | 114 ms                                                   | 281 ms: 2.46x slower                                                    |
| sqlglot_parse              | 1.38 ms                                                  | 3.71 ms: 2.69x slower                                                   |
| raytrace                   | 300 ms                                                   | 813 ms: 2.71x slower                                                    |
| deltablue                  | 3.82 ms                                                  | 12.5 ms: 3.26x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.54x slower                                                            |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20240914-3.14.0a0-401fff7-NOGIL/bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.353x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.46x
- 95% likely to have a slowdown of 1.41x
- 99% likely to have a slowdown of 1.36x

# Memory
- memory change: 1.06x