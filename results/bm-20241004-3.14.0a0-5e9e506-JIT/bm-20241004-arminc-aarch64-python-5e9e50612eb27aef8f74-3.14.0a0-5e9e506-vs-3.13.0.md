# Results vs. 3.13.0

- fork: python
- ref: 5e9e50612eb27aef8f74
- machine: linux-aarch64
- commit hash: 5e9e506
- commit date: 2024-10-04
- overall geometric mean: 1.092x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x slower
- Memory change: 1.07x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 386 ms: 1.27x slower                                                    |
| docutils       | 2.89 sec                                                 | 3.71 sec: 1.28x slower                                                  |
| html5lib       | 66.4 ms                                                  | 71.9 ms: 1.08x slower                                                   |
| sphinx         | 1.17 sec                                                 | 1.46 sec: 1.25x slower                                                  |
| tornado_http   | 128 ms                                                   | 148 ms: 1.16x slower                                                    |
| Geometric mean | (ref)                                                    | 1.21x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 543 ms: 1.20x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 582 ms: 1.12x faster                                                    |
| async_tree_none_tg         | 470 ms                                                   | 423 ms: 1.11x faster                                                    |
| async_tree_none            | 497 ms                                                   | 459 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 728 ms: 1.06x faster                                                    |
| async_generators           | 489 ms                                                   | 508 ms: 1.04x slower                                                    |
| async_tree_io_tg           | 1.13 sec                                                 | 1.20 sec: 1.06x slower                                                  |
| async_tree_io              | 1.11 sec                                                 | 1.20 sec: 1.08x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| nbody          | 114 ms                                                   | 111 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                    | 1.01x faster                                                            |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 31.8 ms                                                  | 30.9 ms: 1.03x faster                                                   |
| regex_dna      | 253 ms                                                   | 255 ms: 1.01x slower                                                    |
| regex_effbot   | 4.89 ms                                                  | 5.00 ms: 1.02x slower                                                   |
| regex_compile  | 127 ms                                                   | 180 ms: 1.42x slower                                                    |
| Geometric mean | (ref)                                                    | 1.09x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                   | 188 ms: 1.04x faster                                                    |
| xml_etree_iterparse  | 149 ms                                                   | 152 ms: 1.02x slower                                                    |
| tomli_loads          | 2.54 sec                                                 | 2.65 sec: 1.04x slower                                                  |
| unpickle_pure_python | 251 us                                                   | 267 us: 1.06x slower                                                    |
| pickle_pure_python   | 357 us                                                   | 393 us: 1.10x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.02x slower                                                            |

Benchmark hidden because not significant (4): xml_etree_generate, json_loads, json_dumps, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 14.6 ms: 1.06x faster                                                   |
| Geometric mean | (ref)                                                    | 1.03x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.4 ms                                                  | 13.0 ms: 1.03x faster                                                   |
| genshi_text     | 27.7 ms                                                  | 34.4 ms: 1.24x slower                                                   |
| django_template | 41.6 ms                                                  | 52.2 ms: 1.25x slower                                                   |
| genshi_xml      | 60.3 ms                                                  | 84.4 ms: 1.40x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.21x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| deepcopy_memo              | 50.4 us                                                  | 37.6 us: 1.34x faster                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 543 ms: 1.20x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 582 ms: 1.12x faster                                                    |
| async_tree_none_tg         | 470 ms                                                   | 423 ms: 1.11x faster                                                    |
| deepcopy                   | 447 us                                                   | 407 us: 1.10x faster                                                    |
| async_tree_none            | 497 ms                                                   | 459 ms: 1.08x faster                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 728 ms: 1.06x faster                                                    |
| python_startup             | 15.4 ms                                                  | 14.6 ms: 1.06x faster                                                   |
| xml_etree_parse            | 197 ms                                                   | 188 ms: 1.04x faster                                                    |
| scimark_sor                | 160 ms                                                   | 153 ms: 1.04x faster                                                    |
| pathlib                    | 22.7 ms                                                  | 21.9 ms: 1.04x faster                                                   |
| nbody                      | 114 ms                                                   | 111 ms: 1.03x faster                                                    |
| deepcopy_reduce            | 4.07 us                                                  | 3.94 us: 1.03x faster                                                   |
| regex_v8                   | 31.8 ms                                                  | 30.9 ms: 1.03x faster                                                   |
| mako                       | 13.4 ms                                                  | 13.0 ms: 1.03x faster                                                   |
| thrift                     | 968 us                                                   | 955 us: 1.01x faster                                                    |
| regex_dna                  | 253 ms                                                   | 255 ms: 1.01x slower                                                    |
| logging_silent             | 133 ns                                                   | 134 ns: 1.01x slower                                                    |
| xml_etree_iterparse        | 149 ms                                                   | 152 ms: 1.02x slower                                                    |
| regex_effbot               | 4.89 ms                                                  | 5.00 ms: 1.02x slower                                                   |
| bpe_tokeniser              | 5.87 sec                                                 | 6.07 sec: 1.03x slower                                                  |
| async_generators           | 489 ms                                                   | 508 ms: 1.04x slower                                                    |
| tomli_loads                | 2.54 sec                                                 | 2.65 sec: 1.04x slower                                                  |
| mdp                        | 3.34 sec                                                 | 3.51 sec: 1.05x slower                                                  |
| async_tree_io_tg           | 1.13 sec                                                 | 1.20 sec: 1.06x slower                                                  |
| gc_traversal               | 5.77 ms                                                  | 6.11 ms: 1.06x slower                                                   |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 6.91 ms: 1.06x slower                                                   |
| unpickle_pure_python       | 251 us                                                   | 267 us: 1.06x slower                                                    |
| logging_format             | 7.82 us                                                  | 8.34 us: 1.07x slower                                                   |
| create_gc_cycles           | 3.35 ms                                                  | 3.57 ms: 1.07x slower                                                   |
| spectral_norm              | 143 ms                                                   | 152 ms: 1.07x slower                                                    |
| scimark_monte_carlo        | 83.6 ms                                                  | 89.5 ms: 1.07x slower                                                   |
| crypto_pyaes               | 83.7 ms                                                  | 89.8 ms: 1.07x slower                                                   |
| async_tree_io              | 1.11 sec                                                 | 1.20 sec: 1.08x slower                                                  |
| html5lib                   | 66.4 ms                                                  | 71.9 ms: 1.08x slower                                                   |
| scimark_lu                 | 139 ms                                                   | 151 ms: 1.09x slower                                                    |
| logging_simple             | 7.07 us                                                  | 7.70 us: 1.09x slower                                                   |
| typing_runtime_protocols   | 193 us                                                   | 211 us: 1.09x slower                                                    |
| fannkuch                   | 461 ms                                                   | 503 ms: 1.09x slower                                                    |
| bench_thread_pool          | 1.27 ms                                                  | 1.39 ms: 1.09x slower                                                   |
| pickle_pure_python         | 357 us                                                   | 393 us: 1.10x slower                                                    |
| meteor_contest             | 114 ms                                                   | 125 ms: 1.10x slower                                                    |
| pyflate                    | 556 ms                                                   | 616 ms: 1.11x slower                                                    |
| go                         | 160 ms                                                   | 184 ms: 1.15x slower                                                    |
| deltablue                  | 3.82 ms                                                  | 4.40 ms: 1.15x slower                                                   |
| tornado_http               | 128 ms                                                   | 148 ms: 1.16x slower                                                    |
| raytrace                   | 300 ms                                                   | 351 ms: 1.17x slower                                                    |
| pycparser                  | 1.27 sec                                                 | 1.51 sec: 1.18x slower                                                  |
| comprehensions             | 20.4 us                                                  | 25.0 us: 1.23x slower                                                   |
| sqlglot_parse              | 1.38 ms                                                  | 1.69 ms: 1.23x slower                                                   |
| richards                   | 53.6 ms                                                  | 66.2 ms: 1.23x slower                                                   |
| sqlglot_normalize          | 127 ms                                                   | 157 ms: 1.24x slower                                                    |
| genshi_text                | 27.7 ms                                                  | 34.4 ms: 1.24x slower                                                   |
| richards_super             | 60.1 ms                                                  | 74.9 ms: 1.25x slower                                                   |
| sphinx                     | 1.17 sec                                                 | 1.46 sec: 1.25x slower                                                  |
| nqueens                    | 100 ms                                                   | 125 ms: 1.25x slower                                                    |
| django_template            | 41.6 ms                                                  | 52.2 ms: 1.25x slower                                                   |
| sqlglot_transpile          | 1.73 ms                                                  | 2.17 ms: 1.25x slower                                                   |
| 2to3                       | 304 ms                                                   | 386 ms: 1.27x slower                                                    |
| chaos                      | 68.0 ms                                                  | 87.0 ms: 1.28x slower                                                   |
| docutils                   | 2.89 sec                                                 | 3.71 sec: 1.28x slower                                                  |
| sympy_expand               | 457 ms                                                   | 597 ms: 1.31x slower                                                    |
| sqlglot_optimize           | 62.2 ms                                                  | 82.8 ms: 1.33x slower                                                   |
| pprint_safe_repr           | 926 ms                                                   | 1.24 sec: 1.33x slower                                                  |
| sympy_str                  | 264 ms                                                   | 359 ms: 1.36x slower                                                    |
| pprint_pformat             | 1.90 sec                                                 | 2.63 sec: 1.39x slower                                                  |
| genshi_xml                 | 60.3 ms                                                  | 84.4 ms: 1.40x slower                                                   |
| sympy_integrate            | 20.8 ms                                                  | 29.2 ms: 1.40x slower                                                   |
| regex_compile              | 127 ms                                                   | 180 ms: 1.42x slower                                                    |
| hexiom                     | 7.11 ms                                                  | 10.2 ms: 1.43x slower                                                   |
| pylint                     | 342 ms                                                   | 492 ms: 1.44x slower                                                    |
| sympy_sum                  | 144 ms                                                   | 214 ms: 1.49x slower                                                    |
| generators                 | 37.6 ms                                                  | 59.1 ms: 1.57x slower                                                   |
| bench_mp_pool              | 7.68 ms                                                  | 1.43 sec: 186.55x slower                                                |
| Geometric mean             | (ref)                                                    | 1.16x slower                                                            |

Benchmark hidden because not significant (14): xml_etree_generate, json_loads, async_tree_cpu_io_mixed, scimark_fft, json, python_startup_no_site, telco, json_dumps, coverage, pidigits, asyncio_websockets, xml_etree_process, coroutines, float
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20241004-3.14.0a0-5e9e506-JIT/bm-20241004-arminc-aarch64-python-5e9e50612eb27aef8f74-3.14.0a0-5e9e506.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.092x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.04x

# Memory
- memory change: 1.07x