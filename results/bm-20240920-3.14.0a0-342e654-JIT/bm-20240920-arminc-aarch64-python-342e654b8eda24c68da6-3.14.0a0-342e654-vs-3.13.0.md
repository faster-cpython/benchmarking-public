# Results vs. 3.13.0

- fork: python
- ref: 342e654b8eda24c68da6
- machine: linux-aarch64
- commit hash: 342e654
- commit date: 2024-09-20
- overall geometric mean: 1.082x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 382 ms: 1.26x slower                                                    |
| docutils       | 2.89 sec                                                 | 3.94 sec: 1.36x slower                                                  |
| html5lib       | 66.4 ms                                                  | 71.9 ms: 1.08x slower                                                   |
| tornado_http   | 128 ms                                                   | 150 ms: 1.17x slower                                                    |
| Geometric mean | (ref)                                                    | 1.21x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 556 ms: 1.17x faster                                                    |
| async_tree_none            | 497 ms                                                   | 442 ms: 1.12x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 589 ms: 1.11x faster                                                    |
| async_tree_none_tg         | 470 ms                                                   | 426 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 735 ms: 1.05x faster                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 748 ms: 1.02x faster                                                    |
| async_tree_io_tg           | 1.13 sec                                                 | 1.17 sec: 1.03x slower                                                  |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                  |
| async_generators           | 489 ms                                                   | 512 ms: 1.05x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (2): coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 93.3 ms                                                  | 87.5 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 31.1 ms: 1.02x faster                                                   |
| regex_compile  | 127 ms                                                   | 196 ms: 1.54x slower                                                    |
| Geometric mean | (ref)                                                    | 1.11x slower                                                            |

Benchmark hidden because not significant (2): regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                   | 187 ms: 1.05x faster                                                    |
| xml_etree_generate   | 113 ms                                                   | 111 ms: 1.02x faster                                                    |
| xml_etree_iterparse  | 149 ms                                                   | 148 ms: 1.01x faster                                                    |
| json_loads           | 31.7 us                                                  | 31.4 us: 1.01x faster                                                   |
| tomli_loads          | 2.54 sec                                                 | 2.64 sec: 1.04x slower                                                  |
| unpickle_pure_python | 251 us                                                   | 267 us: 1.06x slower                                                    |
| pickle_pure_python   | 357 us                                                   | 392 us: 1.10x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (2): json_dumps, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 13.1 ms: 1.17x faster                                                   |
| Geometric mean | (ref)                                                    | 1.08x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.4 ms                                                  | 12.9 ms: 1.03x faster                                                   |
| django_template | 41.6 ms                                                  | 51.4 ms: 1.23x slower                                                   |
| genshi_text     | 27.7 ms                                                  | 35.0 ms: 1.26x slower                                                   |
| genshi_xml      | 60.3 ms                                                  | 80.8 ms: 1.34x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.19x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 2.31 ms: 1.45x faster                                                   |
| deepcopy_memo              | 50.4 us                                                  | 37.6 us: 1.34x faster                                                   |
| python_startup             | 15.4 ms                                                  | 13.1 ms: 1.17x faster                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 556 ms: 1.17x faster                                                    |
| gc_traversal               | 5.77 ms                                                  | 5.10 ms: 1.13x faster                                                   |
| async_tree_none            | 497 ms                                                   | 442 ms: 1.12x faster                                                    |
| deepcopy                   | 447 us                                                   | 401 us: 1.11x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 589 ms: 1.11x faster                                                    |
| async_tree_none_tg         | 470 ms                                                   | 426 ms: 1.10x faster                                                    |
| float                      | 93.3 ms                                                  | 87.5 ms: 1.07x faster                                                   |
| deepcopy_reduce            | 4.07 us                                                  | 3.83 us: 1.06x faster                                                   |
| xml_etree_parse            | 197 ms                                                   | 187 ms: 1.05x faster                                                    |
| pathlib                    | 22.7 ms                                                  | 21.7 ms: 1.05x faster                                                   |
| scimark_sor                | 160 ms                                                   | 152 ms: 1.05x faster                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 735 ms: 1.05x faster                                                    |
| mako                       | 13.4 ms                                                  | 12.9 ms: 1.03x faster                                                   |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 748 ms: 1.02x faster                                                    |
| xml_etree_generate         | 113 ms                                                   | 111 ms: 1.02x faster                                                    |
| regex_v8                   | 31.8 ms                                                  | 31.1 ms: 1.02x faster                                                   |
| xml_etree_iterparse        | 149 ms                                                   | 148 ms: 1.01x faster                                                    |
| json_loads                 | 31.7 us                                                  | 31.4 us: 1.01x faster                                                   |
| bpe_tokeniser              | 5.87 sec                                                 | 5.98 sec: 1.02x slower                                                  |
| spectral_norm              | 143 ms                                                   | 146 ms: 1.02x slower                                                    |
| scimark_fft                | 447 ms                                                   | 459 ms: 1.03x slower                                                    |
| coverage                   | 99.1 ms                                                  | 102 ms: 1.03x slower                                                    |
| logging_silent             | 133 ns                                                   | 137 ns: 1.03x slower                                                    |
| async_tree_io_tg           | 1.13 sec                                                 | 1.17 sec: 1.03x slower                                                  |
| async_tree_io              | 1.11 sec                                                 | 1.15 sec: 1.04x slower                                                  |
| tomli_loads                | 2.54 sec                                                 | 2.64 sec: 1.04x slower                                                  |
| async_generators           | 489 ms                                                   | 512 ms: 1.05x slower                                                    |
| logging_format             | 7.82 us                                                  | 8.20 us: 1.05x slower                                                   |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 6.85 ms: 1.05x slower                                                   |
| logging_simple             | 7.07 us                                                  | 7.46 us: 1.06x slower                                                   |
| mdp                        | 3.34 sec                                                 | 3.52 sec: 1.06x slower                                                  |
| bench_thread_pool          | 1.27 ms                                                  | 1.35 ms: 1.06x slower                                                   |
| unpickle_pure_python       | 251 us                                                   | 267 us: 1.06x slower                                                    |
| scimark_lu                 | 139 ms                                                   | 148 ms: 1.07x slower                                                    |
| crypto_pyaes               | 83.7 ms                                                  | 89.7 ms: 1.07x slower                                                   |
| html5lib                   | 66.4 ms                                                  | 71.9 ms: 1.08x slower                                                   |
| telco                      | 9.74 ms                                                  | 10.6 ms: 1.09x slower                                                   |
| meteor_contest             | 114 ms                                                   | 124 ms: 1.10x slower                                                    |
| pickle_pure_python         | 357 us                                                   | 392 us: 1.10x slower                                                    |
| typing_runtime_protocols   | 193 us                                                   | 213 us: 1.10x slower                                                    |
| fannkuch                   | 461 ms                                                   | 508 ms: 1.10x slower                                                    |
| scimark_monte_carlo        | 83.6 ms                                                  | 92.6 ms: 1.11x slower                                                   |
| deltablue                  | 3.82 ms                                                  | 4.39 ms: 1.15x slower                                                   |
| raytrace                   | 300 ms                                                   | 348 ms: 1.16x slower                                                    |
| tornado_http               | 128 ms                                                   | 150 ms: 1.17x slower                                                    |
| pyflate                    | 556 ms                                                   | 657 ms: 1.18x slower                                                    |
| sqlglot_normalize          | 127 ms                                                   | 150 ms: 1.18x slower                                                    |
| go                         | 160 ms                                                   | 190 ms: 1.19x slower                                                    |
| pycparser                  | 1.27 sec                                                 | 1.53 sec: 1.20x slower                                                  |
| comprehensions             | 20.4 us                                                  | 24.5 us: 1.20x slower                                                   |
| django_template            | 41.6 ms                                                  | 51.4 ms: 1.23x slower                                                   |
| richards                   | 53.6 ms                                                  | 66.3 ms: 1.24x slower                                                   |
| nqueens                    | 100 ms                                                   | 126 ms: 1.26x slower                                                    |
| 2to3                       | 304 ms                                                   | 382 ms: 1.26x slower                                                    |
| sqlglot_optimize           | 62.2 ms                                                  | 78.5 ms: 1.26x slower                                                   |
| genshi_text                | 27.7 ms                                                  | 35.0 ms: 1.26x slower                                                   |
| richards_super             | 60.1 ms                                                  | 75.9 ms: 1.26x slower                                                   |
| sqlglot_parse              | 1.38 ms                                                  | 1.76 ms: 1.28x slower                                                   |
| sqlglot_transpile          | 1.73 ms                                                  | 2.23 ms: 1.29x slower                                                   |
| genshi_xml                 | 60.3 ms                                                  | 80.8 ms: 1.34x slower                                                   |
| sympy_expand               | 457 ms                                                   | 613 ms: 1.34x slower                                                    |
| pprint_safe_repr           | 926 ms                                                   | 1.25 sec: 1.34x slower                                                  |
| chaos                      | 68.0 ms                                                  | 92.2 ms: 1.36x slower                                                   |
| docutils                   | 2.89 sec                                                 | 3.94 sec: 1.36x slower                                                  |
| sympy_integrate            | 20.8 ms                                                  | 28.5 ms: 1.37x slower                                                   |
| pprint_pformat             | 1.90 sec                                                 | 2.61 sec: 1.38x slower                                                  |
| sympy_str                  | 264 ms                                                   | 369 ms: 1.40x slower                                                    |
| pylint                     | 342 ms                                                   | 479 ms: 1.40x slower                                                    |
| hexiom                     | 7.11 ms                                                  | 10.3 ms: 1.46x slower                                                   |
| sympy_sum                  | 144 ms                                                   | 211 ms: 1.47x slower                                                    |
| generators                 | 37.6 ms                                                  | 57.6 ms: 1.53x slower                                                   |
| regex_compile              | 127 ms                                                   | 196 ms: 1.54x slower                                                    |
| Geometric mean             | (ref)                                                    | 1.09x slower                                                            |

Benchmark hidden because not significant (12): bench_mp_pool, json, json_dumps, regex_dna, nbody, coroutines, xml_etree_process, thrift, pidigits, asyncio_websockets, python_startup_no_site, regex_effbot
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20240920-3.14.0a0-342e654-JIT/bm-20240920-arminc-aarch64-python-342e654b8eda24c68da6-3.14.0a0-342e654.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.082x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 0.98x