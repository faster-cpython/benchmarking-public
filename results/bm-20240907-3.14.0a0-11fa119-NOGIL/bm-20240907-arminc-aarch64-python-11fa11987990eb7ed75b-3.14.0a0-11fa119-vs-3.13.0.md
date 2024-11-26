# Results vs. 3.13.0

- fork: python
- ref: 11fa11987990eb7ed75b
- machine: linux-aarch64
- commit hash: 11fa119
- commit date: 2024-09-07
- overall geometric mean: 1.367x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.40x slower
- Memory change: 1.06x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 518 ms: 1.71x slower                                                    |
| docutils       | 2.89 sec                                                 | 4.10 sec: 1.42x slower                                                  |
| html5lib       | 66.4 ms                                                  | 121 ms: 1.82x slower                                                    |
| tornado_http   | 128 ms                                                   | 207 ms: 1.62x slower                                                    |
| Geometric mean | (ref)                                                    | 1.63x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| asyncio_websockets         | 659 ms                                                   | 672 ms: 1.02x slower                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 699 ms: 1.08x slower                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 871 ms: 1.13x slower                                                    |
| async_tree_memoization     | 651 ms                                                   | 739 ms: 1.14x slower                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 914 ms: 1.19x slower                                                    |
| async_tree_io_tg           | 1.13 sec                                                 | 1.36 sec: 1.20x slower                                                  |
| async_tree_none_tg         | 470 ms                                                   | 572 ms: 1.22x slower                                                    |
| async_tree_none            | 497 ms                                                   | 625 ms: 1.26x slower                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.41 sec: 1.27x slower                                                  |
| async_generators           | 489 ms                                                   | 653 ms: 1.33x slower                                                    |
| coroutines                 | 28.5 ms                                                  | 40.9 ms: 1.44x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.20x slower                                                            |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 93.3 ms                                                  | 207 ms: 2.22x slower                                                    |
| nbody          | 114 ms                                                   | 281 ms: 2.45x slower                                                    |
| Geometric mean | (ref)                                                    | 1.76x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.89 ms                                                  | 4.48 ms: 1.09x faster                                                   |
| regex_dna      | 253 ms                                                   | 261 ms: 1.03x slower                                                    |
| regex_v8       | 31.8 ms                                                  | 33.0 ms: 1.04x slower                                                   |
| regex_compile  | 127 ms                                                   | 259 ms: 2.04x slower                                                    |
| Geometric mean | (ref)                                                    | 1.19x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                   | 184 ms: 1.07x faster                                                    |
| xml_etree_iterparse  | 149 ms                                                   | 157 ms: 1.05x slower                                                    |
| json_loads           | 31.7 us                                                  | 39.3 us: 1.24x slower                                                   |
| json_dumps           | 13.6 ms                                                  | 17.9 ms: 1.32x slower                                                   |
| xml_etree_generate   | 113 ms                                                   | 163 ms: 1.44x slower                                                    |
| xml_etree_process    | 80.5 ms                                                  | 130 ms: 1.62x slower                                                    |
| tomli_loads          | 2.54 sec                                                 | 4.19 sec: 1.65x slower                                                  |
| unpickle_pure_python | 251 us                                                   | 542 us: 2.16x slower                                                    |
| pickle_pure_python   | 357 us                                                   | 777 us: 2.18x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.45x slower                                                            |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 15.4 ms                                                  | 18.2 ms: 1.18x slower                                                   |
| python_startup_no_site | 8.73 ms                                                  | 12.2 ms: 1.40x slower                                                   |
| Geometric mean         | (ref)                                                    | 1.29x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml      | 60.3 ms                                                  | 104 ms: 1.72x slower                                                    |
| genshi_text     | 27.7 ms                                                  | 53.3 ms: 1.92x slower                                                   |
| django_template | 41.6 ms                                                  | 83.4 ms: 2.00x slower                                                   |
| mako            | 13.4 ms                                                  | 28.9 ms: 2.16x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.95x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 1.62 ms: 2.07x faster                                                   |
| gc_traversal               | 5.77 ms                                                  | 3.45 ms: 1.67x faster                                                   |
| regex_effbot               | 4.89 ms                                                  | 4.48 ms: 1.09x faster                                                   |
| bench_mp_pool              | 7.68 ms                                                  | 7.20 ms: 1.07x faster                                                   |
| xml_etree_parse            | 197 ms                                                   | 184 ms: 1.07x faster                                                    |
| asyncio_websockets         | 659 ms                                                   | 672 ms: 1.02x slower                                                    |
| regex_dna                  | 253 ms                                                   | 261 ms: 1.03x slower                                                    |
| regex_v8                   | 31.8 ms                                                  | 33.0 ms: 1.04x slower                                                   |
| xml_etree_iterparse        | 149 ms                                                   | 157 ms: 1.05x slower                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 699 ms: 1.08x slower                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 871 ms: 1.13x slower                                                    |
| async_tree_memoization     | 651 ms                                                   | 739 ms: 1.14x slower                                                    |
| pathlib                    | 22.7 ms                                                  | 26.8 ms: 1.18x slower                                                   |
| python_startup             | 15.4 ms                                                  | 18.2 ms: 1.18x slower                                                   |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 914 ms: 1.19x slower                                                    |
| async_tree_io_tg           | 1.13 sec                                                 | 1.36 sec: 1.20x slower                                                  |
| async_tree_none_tg         | 470 ms                                                   | 572 ms: 1.22x slower                                                    |
| json                       | 5.73 ms                                                  | 7.03 ms: 1.23x slower                                                   |
| json_loads                 | 31.7 us                                                  | 39.3 us: 1.24x slower                                                   |
| async_tree_none            | 497 ms                                                   | 625 ms: 1.26x slower                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.41 sec: 1.27x slower                                                  |
| deepcopy                   | 447 us                                                   | 571 us: 1.28x slower                                                    |
| scimark_fft                | 447 ms                                                   | 573 ms: 1.28x slower                                                    |
| mdp                        | 3.34 sec                                                 | 4.32 sec: 1.30x slower                                                  |
| telco                      | 9.74 ms                                                  | 12.8 ms: 1.31x slower                                                   |
| json_dumps                 | 13.6 ms                                                  | 17.9 ms: 1.32x slower                                                   |
| async_generators           | 489 ms                                                   | 653 ms: 1.33x slower                                                    |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 8.82 ms: 1.35x slower                                                   |
| coverage                   | 99.1 ms                                                  | 136 ms: 1.37x slower                                                    |
| python_startup_no_site     | 8.73 ms                                                  | 12.2 ms: 1.40x slower                                                   |
| docutils                   | 2.89 sec                                                 | 4.10 sec: 1.42x slower                                                  |
| deepcopy_memo              | 50.4 us                                                  | 72.1 us: 1.43x slower                                                   |
| xml_etree_generate         | 113 ms                                                   | 163 ms: 1.44x slower                                                    |
| coroutines                 | 28.5 ms                                                  | 40.9 ms: 1.44x slower                                                   |
| meteor_contest             | 114 ms                                                   | 167 ms: 1.47x slower                                                    |
| pylint                     | 342 ms                                                   | 511 ms: 1.49x slower                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 6.14 us: 1.51x slower                                                   |
| nqueens                    | 100 ms                                                   | 152 ms: 1.52x slower                                                    |
| generators                 | 37.6 ms                                                  | 57.7 ms: 1.53x slower                                                   |
| pycparser                  | 1.27 sec                                                 | 2.02 sec: 1.59x slower                                                  |
| spectral_norm              | 143 ms                                                   | 226 ms: 1.59x slower                                                    |
| fannkuch                   | 461 ms                                                   | 738 ms: 1.60x slower                                                    |
| bpe_tokeniser              | 5.87 sec                                                 | 9.48 sec: 1.61x slower                                                  |
| tornado_http               | 128 ms                                                   | 207 ms: 1.62x slower                                                    |
| xml_etree_process          | 80.5 ms                                                  | 130 ms: 1.62x slower                                                    |
| crypto_pyaes               | 83.7 ms                                                  | 137 ms: 1.63x slower                                                    |
| tomli_loads                | 2.54 sec                                                 | 4.19 sec: 1.65x slower                                                  |
| sympy_integrate            | 20.8 ms                                                  | 34.7 ms: 1.67x slower                                                   |
| bench_thread_pool          | 1.27 ms                                                  | 2.13 ms: 1.67x slower                                                   |
| 2to3                       | 304 ms                                                   | 518 ms: 1.71x slower                                                    |
| genshi_xml                 | 60.3 ms                                                  | 104 ms: 1.72x slower                                                    |
| typing_runtime_protocols   | 193 us                                                   | 336 us: 1.74x slower                                                    |
| thrift                     | 968 us                                                   | 1.69 ms: 1.74x slower                                                   |
| html5lib                   | 66.4 ms                                                  | 121 ms: 1.82x slower                                                    |
| pyflate                    | 556 ms                                                   | 1.02 sec: 1.83x slower                                                  |
| sqlglot_normalize          | 127 ms                                                   | 237 ms: 1.87x slower                                                    |
| pprint_safe_repr           | 926 ms                                                   | 1.76 sec: 1.90x slower                                                  |
| sqlglot_optimize           | 62.2 ms                                                  | 119 ms: 1.91x slower                                                    |
| pprint_pformat             | 1.90 sec                                                 | 3.64 sec: 1.92x slower                                                  |
| genshi_text                | 27.7 ms                                                  | 53.3 ms: 1.92x slower                                                   |
| sympy_str                  | 264 ms                                                   | 514 ms: 1.95x slower                                                    |
| django_template            | 41.6 ms                                                  | 83.4 ms: 2.00x slower                                                   |
| comprehensions             | 20.4 us                                                  | 40.9 us: 2.01x slower                                                   |
| logging_format             | 7.82 us                                                  | 15.9 us: 2.04x slower                                                   |
| regex_compile              | 127 ms                                                   | 259 ms: 2.04x slower                                                    |
| logging_simple             | 7.07 us                                                  | 14.6 us: 2.07x slower                                                   |
| sympy_expand               | 457 ms                                                   | 961 ms: 2.10x slower                                                    |
| scimark_monte_carlo        | 83.6 ms                                                  | 176 ms: 2.10x slower                                                    |
| scimark_sor                | 160 ms                                                   | 341 ms: 2.13x slower                                                    |
| logging_silent             | 133 ns                                                   | 284 ns: 2.14x slower                                                    |
| mako                       | 13.4 ms                                                  | 28.9 ms: 2.16x slower                                                   |
| unpickle_pure_python       | 251 us                                                   | 542 us: 2.16x slower                                                    |
| pickle_pure_python         | 357 us                                                   | 777 us: 2.18x slower                                                    |
| richards                   | 53.6 ms                                                  | 117 ms: 2.18x slower                                                    |
| sympy_sum                  | 144 ms                                                   | 318 ms: 2.21x slower                                                    |
| float                      | 93.3 ms                                                  | 207 ms: 2.22x slower                                                    |
| hexiom                     | 7.11 ms                                                  | 15.9 ms: 2.24x slower                                                   |
| chaos                      | 68.0 ms                                                  | 160 ms: 2.35x slower                                                    |
| richards_super             | 60.1 ms                                                  | 143 ms: 2.37x slower                                                    |
| nbody                      | 114 ms                                                   | 281 ms: 2.45x slower                                                    |
| scimark_lu                 | 139 ms                                                   | 350 ms: 2.51x slower                                                    |
| go                         | 160 ms                                                   | 404 ms: 2.53x slower                                                    |
| sqlglot_transpile          | 1.73 ms                                                  | 4.45 ms: 2.57x slower                                                   |
| sqlglot_parse              | 1.38 ms                                                  | 3.67 ms: 2.66x slower                                                   |
| raytrace                   | 300 ms                                                   | 815 ms: 2.72x slower                                                    |
| deltablue                  | 3.82 ms                                                  | 12.7 ms: 3.33x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.58x slower                                                            |

Benchmark hidden because not significant (1): pidigits
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20240907-3.14.0a0-11fa119-NOGIL/bm-20240907-arminc-aarch64-python-11fa11987990eb7ed75b-3.14.0a0-11fa119.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.367x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.48x
- 95% likely to have a slowdown of 1.44x
- 99% likely to have a slowdown of 1.40x

# Memory
- memory change: 1.06x