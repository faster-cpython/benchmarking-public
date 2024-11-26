# Results vs. 3.13.0

- fork: python
- ref: 401fff7423ca3c8bf1d0
- machine: linux-aarch64
- commit hash: 401fff7
- commit date: 2024-09-14
- overall geometric mean: 1.081x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 380 ms: 1.25x slower                                                    |
| docutils       | 2.89 sec                                                 | 3.98 sec: 1.38x slower                                                  |
| html5lib       | 66.4 ms                                                  | 71.3 ms: 1.07x slower                                                   |
| tornado_http   | 128 ms                                                   | 147 ms: 1.15x slower                                                    |
| Geometric mean | (ref)                                                    | 1.21x slower                                                            |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 564 ms: 1.15x faster                                                    |
| async_tree_none            | 497 ms                                                   | 444 ms: 1.12x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 588 ms: 1.11x faster                                                    |
| async_tree_none_tg         | 470 ms                                                   | 426 ms: 1.10x faster                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 742 ms: 1.04x faster                                                    |
| async_generators           | 489 ms                                                   | 501 ms: 1.03x slower                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.14 sec: 1.03x slower                                                  |
| async_tree_io_tg           | 1.13 sec                                                 | 1.17 sec: 1.03x slower                                                  |
| Geometric mean             | (ref)                                                    | 1.04x faster                                                            |

Benchmark hidden because not significant (3): async_tree_cpu_io_mixed, coroutines, asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 93.3 ms                                                  | 87.5 ms: 1.07x faster                                                   |
| Geometric mean | (ref)                                                    | 1.02x faster                                                            |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_dna      | 253 ms                                                   | 242 ms: 1.05x faster                                                    |
| regex_v8       | 31.8 ms                                                  | 31.5 ms: 1.01x faster                                                   |
| regex_compile  | 127 ms                                                   | 190 ms: 1.50x slower                                                    |
| Geometric mean | (ref)                                                    | 1.09x slower                                                            |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                   | 188 ms: 1.04x faster                                                    |
| xml_etree_generate   | 113 ms                                                   | 111 ms: 1.02x faster                                                    |
| tomli_loads          | 2.54 sec                                                 | 2.63 sec: 1.03x slower                                                  |
| pickle_pure_python   | 357 us                                                   | 380 us: 1.07x slower                                                    |
| unpickle_pure_python | 251 us                                                   | 267 us: 1.07x slower                                                    |
| Geometric mean       | (ref)                                                    | 1.01x slower                                                            |

Benchmark hidden because not significant (4): xml_etree_process, json_loads, json_dumps, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 13.0 ms: 1.19x faster                                                   |
| Geometric mean | (ref)                                                    | 1.08x faster                                                            |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|-----------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| mako            | 13.4 ms                                                  | 13.1 ms: 1.02x faster                                                   |
| django_template | 41.6 ms                                                  | 50.8 ms: 1.22x slower                                                   |
| genshi_text     | 27.7 ms                                                  | 35.7 ms: 1.29x slower                                                   |
| genshi_xml      | 60.3 ms                                                  | 82.2 ms: 1.36x slower                                                   |
| Geometric mean  | (ref)                                                    | 1.20x slower                                                            |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7 |
|----------------------------|:--------------------------------------------------------:|:-----------------------------------------------------------------------:|
| create_gc_cycles           | 3.35 ms                                                  | 2.29 ms: 1.46x faster                                                   |
| deepcopy_memo              | 50.4 us                                                  | 37.2 us: 1.36x faster                                                   |
| python_startup             | 15.4 ms                                                  | 13.0 ms: 1.19x faster                                                   |
| async_tree_memoization_tg  | 649 ms                                                   | 564 ms: 1.15x faster                                                    |
| deepcopy                   | 447 us                                                   | 394 us: 1.14x faster                                                    |
| gc_traversal               | 5.77 ms                                                  | 5.10 ms: 1.13x faster                                                   |
| async_tree_none            | 497 ms                                                   | 444 ms: 1.12x faster                                                    |
| async_tree_memoization     | 651 ms                                                   | 588 ms: 1.11x faster                                                    |
| async_tree_none_tg         | 470 ms                                                   | 426 ms: 1.10x faster                                                    |
| float                      | 93.3 ms                                                  | 87.5 ms: 1.07x faster                                                   |
| pathlib                    | 22.7 ms                                                  | 21.5 ms: 1.05x faster                                                   |
| deepcopy_reduce            | 4.07 us                                                  | 3.86 us: 1.05x faster                                                   |
| scimark_sor                | 160 ms                                                   | 152 ms: 1.05x faster                                                    |
| regex_dna                  | 253 ms                                                   | 242 ms: 1.05x faster                                                    |
| xml_etree_parse            | 197 ms                                                   | 188 ms: 1.04x faster                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 742 ms: 1.04x faster                                                    |
| xml_etree_generate         | 113 ms                                                   | 111 ms: 1.02x faster                                                    |
| mako                       | 13.4 ms                                                  | 13.1 ms: 1.02x faster                                                   |
| bench_mp_pool              | 7.68 ms                                                  | 7.57 ms: 1.01x faster                                                   |
| regex_v8                   | 31.8 ms                                                  | 31.5 ms: 1.01x faster                                                   |
| bpe_tokeniser              | 5.87 sec                                                 | 5.94 sec: 1.01x slower                                                  |
| thrift                     | 968 us                                                   | 981 us: 1.01x slower                                                    |
| spectral_norm              | 143 ms                                                   | 145 ms: 1.02x slower                                                    |
| async_generators           | 489 ms                                                   | 501 ms: 1.03x slower                                                    |
| scimark_fft                | 447 ms                                                   | 459 ms: 1.03x slower                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.14 sec: 1.03x slower                                                  |
| async_tree_io_tg           | 1.13 sec                                                 | 1.17 sec: 1.03x slower                                                  |
| tomli_loads                | 2.54 sec                                                 | 2.63 sec: 1.03x slower                                                  |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 6.82 ms: 1.05x slower                                                   |
| logging_format             | 7.82 us                                                  | 8.20 us: 1.05x slower                                                   |
| mdp                        | 3.34 sec                                                 | 3.50 sec: 1.05x slower                                                  |
| logging_silent             | 133 ns                                                   | 140 ns: 1.05x slower                                                    |
| logging_simple             | 7.07 us                                                  | 7.52 us: 1.06x slower                                                   |
| pickle_pure_python         | 357 us                                                   | 380 us: 1.07x slower                                                    |
| unpickle_pure_python       | 251 us                                                   | 267 us: 1.07x slower                                                    |
| bench_thread_pool          | 1.27 ms                                                  | 1.36 ms: 1.07x slower                                                   |
| crypto_pyaes               | 83.7 ms                                                  | 89.4 ms: 1.07x slower                                                   |
| scimark_lu                 | 139 ms                                                   | 149 ms: 1.07x slower                                                    |
| typing_runtime_protocols   | 193 us                                                   | 207 us: 1.07x slower                                                    |
| html5lib                   | 66.4 ms                                                  | 71.3 ms: 1.07x slower                                                   |
| telco                      | 9.74 ms                                                  | 10.5 ms: 1.07x slower                                                   |
| fannkuch                   | 461 ms                                                   | 503 ms: 1.09x slower                                                    |
| meteor_contest             | 114 ms                                                   | 124 ms: 1.09x slower                                                    |
| scimark_monte_carlo        | 83.6 ms                                                  | 92.5 ms: 1.11x slower                                                   |
| deltablue                  | 3.82 ms                                                  | 4.36 ms: 1.14x slower                                                   |
| tornado_http               | 128 ms                                                   | 147 ms: 1.15x slower                                                    |
| go                         | 160 ms                                                   | 186 ms: 1.16x slower                                                    |
| raytrace                   | 300 ms                                                   | 350 ms: 1.17x slower                                                    |
| pyflate                    | 556 ms                                                   | 654 ms: 1.17x slower                                                    |
| sqlglot_normalize          | 127 ms                                                   | 151 ms: 1.19x slower                                                    |
| comprehensions             | 20.4 us                                                  | 24.5 us: 1.20x slower                                                   |
| pycparser                  | 1.27 sec                                                 | 1.54 sec: 1.21x slower                                                  |
| django_template            | 41.6 ms                                                  | 50.8 ms: 1.22x slower                                                   |
| richards                   | 53.6 ms                                                  | 66.3 ms: 1.24x slower                                                   |
| 2to3                       | 304 ms                                                   | 380 ms: 1.25x slower                                                    |
| richards_super             | 60.1 ms                                                  | 75.3 ms: 1.25x slower                                                   |
| sqlglot_optimize           | 62.2 ms                                                  | 78.9 ms: 1.27x slower                                                   |
| sqlglot_transpile          | 1.73 ms                                                  | 2.21 ms: 1.28x slower                                                   |
| nqueens                    | 100 ms                                                   | 128 ms: 1.28x slower                                                    |
| sqlglot_parse              | 1.38 ms                                                  | 1.77 ms: 1.28x slower                                                   |
| genshi_text                | 27.7 ms                                                  | 35.7 ms: 1.29x slower                                                   |
| pprint_safe_repr           | 926 ms                                                   | 1.25 sec: 1.35x slower                                                  |
| sympy_expand               | 457 ms                                                   | 618 ms: 1.35x slower                                                    |
| chaos                      | 68.0 ms                                                  | 92.1 ms: 1.35x slower                                                   |
| genshi_xml                 | 60.3 ms                                                  | 82.2 ms: 1.36x slower                                                   |
| pprint_pformat             | 1.90 sec                                                 | 2.60 sec: 1.37x slower                                                  |
| docutils                   | 2.89 sec                                                 | 3.98 sec: 1.38x slower                                                  |
| pylint                     | 342 ms                                                   | 473 ms: 1.38x slower                                                    |
| sympy_integrate            | 20.8 ms                                                  | 29.0 ms: 1.39x slower                                                   |
| sympy_str                  | 264 ms                                                   | 368 ms: 1.39x slower                                                    |
| hexiom                     | 7.11 ms                                                  | 10.2 ms: 1.44x slower                                                   |
| regex_compile              | 127 ms                                                   | 190 ms: 1.50x slower                                                    |
| sympy_sum                  | 144 ms                                                   | 216 ms: 1.50x slower                                                    |
| generators                 | 37.6 ms                                                  | 57.4 ms: 1.53x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.09x slower                                                            |

Benchmark hidden because not significant (13): async_tree_cpu_io_mixed, xml_etree_process, json_loads, nbody, json_dumps, regex_effbot, xml_etree_iterparse, json, pidigits, coroutines, asyncio_websockets, python_startup_no_site, coverage
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20240914-3.14.0a0-401fff7-JIT/bm-20240914-arminc-aarch64-python-401fff7423ca3c8bf1d0-3.14.0a0-401fff7.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.081x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.04x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x

# Memory
- memory change: 0.98x