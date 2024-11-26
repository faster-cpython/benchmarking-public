# Results vs. 3.13.0

- fork: python
- ref: 11fa11987990eb7ed75b
- machine: linux-aarch64
- commit hash: 11fa119
- commit date: 2024-09-07
- overall geometric mean: 1.079x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 0.99x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 380 ms: 1.25x slower                                                    |
| docutils       | 2.89 sec                                                 | 3.94 sec: 1.36x slower                                                  |
| html5lib       | 66.4 ms                                                  | 70.2 ms: 1.06x slower                                                   |
| tornado_http   | 128 ms                                                   | 147 ms: 1.15x slower                                                    |
| Geometric mean | (ref)                                                    | 1.20x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 555 ms: 1.17x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 570 ms: 1.14x faster                                                    |
| async_tree_none_tg         | 470 ms                                                   | 429 ms: 1.09x faster                                                    |
| async_tree_none            | 497 ms                                                   | 457 ms: 1.09x faster                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 720 ms: 1.07x faster                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 748 ms: 1.02x faster                                                    |
| async_tree_io_tg           | 1.13 sec                                                 | 1.15 sec: 1.02x slower                                                  |
| async_generators           | 489 ms                                                   | 504 ms: 1.03x slower                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.18 sec: 1.07x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 93.3 ms                                                  | 89.1 ms: 1.05x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 31.1 ms: 1.02x faster                                                   |
| regex_compile  | 127 ms                                                   | 188 ms: 1.48x slower                                                    |
| Geometric mean | (ref)                                                    | 1.10x slower                                                            |

Benchmark hidden because not significant (2): regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                   | 187 ms: 1.05x faster                                                    |
| xml_etree_generate   | 113 ms                                                   | 111 ms: 1.02x faster                                                    |
| json_loads           | 31.7 us                                                  | 32.5 us: 1.03x slower                                                   |
| tomli_loads          | 2.54 sec                                                 | 2.61 sec: 1.03x slower                                                  |
| unpickle_pure_python | 251 us                                                   | 265 us: 1.06x slower                                                    |
| pickle_pure_python   | 357 us                                                   | 393 us: 1.10x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (3): xml_etree_process, xml_etree_iterparse, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 15.4 ms                                                  | 13.2 ms: 1.17x faster                                                   |
| python_startup_no_site | 8.73 ms                                                  | 8.90 ms: 1.02x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.07x faster                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.4 ms                                                  | 13.2 ms: 1.01x faster                                                   |
| genshi_text     | 27.7 ms                                                  | 34.1 ms: 1.23x slower                                                   |
| django_template | 41.6 ms                                                  | 51.4 ms: 1.23x slower                                                   |
| genshi_xml      | 60.3 ms                                                  | 80.1 ms: 1.33x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.19x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 2.33 ms: 1.44x faster                                                   |
| deepcopy_memo              | 50.4 us                                                  | 37.3 us: 1.35x faster                                                   |
| gc_traversal               | 5.77 ms                                                  | 4.93 ms: 1.17x faster                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 555 ms: 1.17x faster                                                    |
| python_startup             | 15.4 ms                                                  | 13.2 ms: 1.17x faster                                                   |
| deepcopy                   | 447 us                                                   | 388 us: 1.15x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 570 ms: 1.14x faster                                                    |
| async_tree_none_tg         | 470 ms                                                   | 429 ms: 1.09x faster                                                    |
| async_tree_none            | 497 ms                                                   | 457 ms: 1.09x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 3.80 us: 1.07x faster                                                   |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 720 ms: 1.07x faster                                                    |
| scimark_sor                | 160 ms                                                   | 150 ms: 1.06x faster                                                    |
| xml_etree_parse            | 197 ms                                                   | 187 ms: 1.05x faster                                                    |
| float                      | 93.3 ms                                                  | 89.1 ms: 1.05x faster                                                   |
| pathlib                    | 22.7 ms                                                  | 22.0 ms: 1.03x faster                                                   |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 748 ms: 1.02x faster                                                    |
| xml_etree_generate         | 113 ms                                                   | 111 ms: 1.02x faster                                                    |
| regex_v8                   | 31.8 ms                                                  | 31.1 ms: 1.02x faster                                                   |
| mako                       | 13.4 ms                                                  | 13.2 ms: 1.01x faster                                                   |
| bpe_tokeniser              | 5.87 sec                                                 | 5.96 sec: 1.02x slower                                                  |
| bench_mp_pool              | 7.68 ms                                                  | 7.82 ms: 1.02x slower                                                   |
| python_startup_no_site     | 8.73 ms                                                  | 8.90 ms: 1.02x slower                                                   |
| async_tree_io_tg           | 1.13 sec                                                 | 1.15 sec: 1.02x slower                                                  |
| spectral_norm              | 143 ms                                                   | 146 ms: 1.02x slower                                                    |
| json_loads                 | 31.7 us                                                  | 32.5 us: 1.03x slower                                                   |
| logging_silent             | 133 ns                                                   | 137 ns: 1.03x slower                                                    |
| scimark_fft                | 447 ms                                                   | 460 ms: 1.03x slower                                                    |
| tomli_loads                | 2.54 sec                                                 | 2.61 sec: 1.03x slower                                                  |
| async_generators           | 489 ms                                                   | 504 ms: 1.03x slower                                                    |
| logging_format             | 7.82 us                                                  | 8.09 us: 1.03x slower                                                   |
| bench_thread_pool          | 1.27 ms                                                  | 1.32 ms: 1.03x slower                                                   |
| mdp                        | 3.34 sec                                                 | 3.47 sec: 1.04x slower                                                  |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 6.82 ms: 1.05x slower                                                   |
| logging_simple             | 7.07 us                                                  | 7.42 us: 1.05x slower                                                   |
| unpickle_pure_python       | 251 us                                                   | 265 us: 1.06x slower                                                    |
| html5lib                   | 66.4 ms                                                  | 70.2 ms: 1.06x slower                                                   |
| telco                      | 9.74 ms                                                  | 10.4 ms: 1.07x slower                                                   |
| crypto_pyaes               | 83.7 ms                                                  | 89.3 ms: 1.07x slower                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.18 sec: 1.07x slower                                                  |
| scimark_lu                 | 139 ms                                                   | 151 ms: 1.08x slower                                                    |
| meteor_contest             | 114 ms                                                   | 124 ms: 1.09x slower                                                    |
| fannkuch                   | 461 ms                                                   | 504 ms: 1.09x slower                                                    |
| pickle_pure_python         | 357 us                                                   | 393 us: 1.10x slower                                                    |
| typing_runtime_protocols   | 193 us                                                   | 214 us: 1.11x slower                                                    |
| scimark_monte_carlo        | 83.6 ms                                                  | 93.7 ms: 1.12x slower                                                   |
| pyflate                    | 556 ms                                                   | 627 ms: 1.13x slower                                                    |
| deltablue                  | 3.82 ms                                                  | 4.34 ms: 1.14x slower                                                   |
| tornado_http               | 128 ms                                                   | 147 ms: 1.15x slower                                                    |
| pycparser                  | 1.27 sec                                                 | 1.49 sec: 1.17x slower                                                  |
| raytrace                   | 300 ms                                                   | 352 ms: 1.17x slower                                                    |
| go                         | 160 ms                                                   | 188 ms: 1.18x slower                                                    |
| sqlglot_normalize          | 127 ms                                                   | 149 ms: 1.18x slower                                                    |
| comprehensions             | 20.4 us                                                  | 24.6 us: 1.21x slower                                                   |
| genshi_text                | 27.7 ms                                                  | 34.1 ms: 1.23x slower                                                   |
| django_template            | 41.6 ms                                                  | 51.4 ms: 1.23x slower                                                   |
| nqueens                    | 100 ms                                                   | 124 ms: 1.24x slower                                                    |
| sqlglot_optimize           | 62.2 ms                                                  | 77.4 ms: 1.24x slower                                                   |
| richards                   | 53.6 ms                                                  | 66.8 ms: 1.25x slower                                                   |
| richards_super             | 60.1 ms                                                  | 75.0 ms: 1.25x slower                                                   |
| 2to3                       | 304 ms                                                   | 380 ms: 1.25x slower                                                    |
| sqlglot_parse              | 1.38 ms                                                  | 1.73 ms: 1.26x slower                                                   |
| sqlglot_transpile          | 1.73 ms                                                  | 2.19 ms: 1.26x slower                                                   |
| sympy_expand               | 457 ms                                                   | 606 ms: 1.33x slower                                                    |
| genshi_xml                 | 60.3 ms                                                  | 80.1 ms: 1.33x slower                                                   |
| chaos                      | 68.0 ms                                                  | 91.4 ms: 1.34x slower                                                   |
| pprint_safe_repr           | 926 ms                                                   | 1.25 sec: 1.35x slower                                                  |
| docutils                   | 2.89 sec                                                 | 3.94 sec: 1.36x slower                                                  |
| pylint                     | 342 ms                                                   | 466 ms: 1.36x slower                                                    |
| pprint_pformat             | 1.90 sec                                                 | 2.59 sec: 1.37x slower                                                  |
| sympy_integrate            | 20.8 ms                                                  | 28.5 ms: 1.37x slower                                                   |
| sympy_str                  | 264 ms                                                   | 366 ms: 1.38x slower                                                    |
| hexiom                     | 7.11 ms                                                  | 10.2 ms: 1.43x slower                                                   |
| regex_compile              | 127 ms                                                   | 188 ms: 1.48x slower                                                    |
| sympy_sum                  | 144 ms                                                   | 214 ms: 1.49x slower                                                    |
| generators                 | 37.6 ms                                                  | 57.3 ms: 1.52x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.08x slower                                                            |

Benchmark hidden because not significant (12): xml_etree_process, xml_etree_iterparse, json_dumps, nbody, thrift, coroutines, pidigits, asyncio_websockets, regex_dna, coverage, regex_effbot, json
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20240907-3.14.0a0-11fa119-JIT/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.079x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 0.99x