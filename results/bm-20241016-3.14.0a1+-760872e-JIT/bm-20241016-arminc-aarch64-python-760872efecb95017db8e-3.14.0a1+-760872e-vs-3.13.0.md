# Results vs. 3.13.0

- fork: python
- ref: 760872efecb95017db8e
- machine: linux-aarch64
- commit hash: 760872e
- commit date: 2024-10-16
- overall geometric mean: 1.091x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x slower
- Memory change: 1.08x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 304 ms                                                   | 381 ms: 1.25x slower                                                     |
| docutils       | 2.89 sec                                                 | 3.65 sec: 1.26x slower                                                   |
| html5lib       | 66.4 ms                                                  | 71.5 ms: 1.08x slower                                                    |
| sphinx         | 1.17 sec                                                 | 1.45 sec: 1.24x slower                                                   |
| tornado_http   | 128 ms                                                   | 147 ms: 1.15x slower                                                     |
| Geometric mean | (ref)                                                    | 1.19x slower                                                             |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 649 ms                                                   | 540 ms: 1.20x faster                                                     |
| async_tree_none            | 497 ms                                                   | 455 ms: 1.09x faster                                                     |
| async_tree_memoization     | 651 ms                                                   | 597 ms: 1.09x faster                                                     |
| async_tree_none_tg         | 470 ms                                                   | 446 ms: 1.05x faster                                                     |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 734 ms: 1.05x faster                                                     |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 752 ms: 1.02x faster                                                     |
| async_generators           | 489 ms                                                   | 510 ms: 1.04x slower                                                     |
| async_tree_io              | 1.11 sec                                                 | 1.18 sec: 1.07x slower                                                   |
| async_tree_io_tg           | 1.13 sec                                                 | 1.25 sec: 1.10x slower                                                   |
| Geometric mean             | (ref)                                                    | 1.02x faster                                                             |

Benchmark hidden because not significant (2): asyncio_websockets, coroutines

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 93.3 ms                                                  | 98.0 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                    | 1.02x slower                                                             |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_dna      | 253 ms                                                   | 244 ms: 1.04x faster                                                     |
| regex_v8       | 31.8 ms                                                  | 31.4 ms: 1.01x faster                                                    |
| regex_compile  | 127 ms                                                   | 169 ms: 1.33x slower                                                     |
| Geometric mean | (ref)                                                    | 1.06x slower                                                             |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| xml_etree_parse      | 197 ms                                                   | 188 ms: 1.05x faster                                                     |
| xml_etree_generate   | 113 ms                                                   | 111 ms: 1.02x faster                                                     |
| tomli_loads          | 2.54 sec                                                 | 2.64 sec: 1.04x slower                                                   |
| json_dumps           | 13.6 ms                                                  | 14.3 ms: 1.05x slower                                                    |
| unpickle_pure_python | 251 us                                                   | 268 us: 1.07x slower                                                     |
| pickle_pure_python   | 357 us                                                   | 389 us: 1.09x slower                                                     |
| Geometric mean       | (ref)                                                    | 1.02x slower                                                             |

Benchmark hidden because not significant (3): json_loads, xml_etree_process, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup | 15.4 ms                                                  | 14.6 ms: 1.05x faster                                                    |
| Geometric mean | (ref)                                                    | 1.03x faster                                                             |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|-----------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| mako            | 13.4 ms                                                  | 13.1 ms: 1.02x faster                                                    |
| genshi_text     | 27.7 ms                                                  | 33.5 ms: 1.21x slower                                                    |
| django_template | 41.6 ms                                                  | 51.1 ms: 1.23x slower                                                    |
| genshi_xml      | 60.3 ms                                                  | 81.5 ms: 1.35x slower                                                    |
| Geometric mean  | (ref)                                                    | 1.18x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5 | bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e |
|----------------------------|:--------------------------------------------------------:|:------------------------------------------------------------------------:|
| deepcopy_memo              | 50.4 us                                                  | 38.9 us: 1.30x faster                                                    |
| async_tree_memoization_tg  | 649 ms                                                   | 540 ms: 1.20x faster                                                     |
| deepcopy                   | 447 us                                                   | 377 us: 1.19x faster                                                     |
| async_tree_none            | 497 ms                                                   | 455 ms: 1.09x faster                                                     |
| async_tree_memoization     | 651 ms                                                   | 597 ms: 1.09x faster                                                     |
| async_tree_none_tg         | 470 ms                                                   | 446 ms: 1.05x faster                                                     |
| python_startup             | 15.4 ms                                                  | 14.6 ms: 1.05x faster                                                    |
| pathlib                    | 22.7 ms                                                  | 21.6 ms: 1.05x faster                                                    |
| async_tree_cpu_io_mixed_tg | 769 ms                                                   | 734 ms: 1.05x faster                                                     |
| xml_etree_parse            | 197 ms                                                   | 188 ms: 1.05x faster                                                     |
| regex_dna                  | 253 ms                                                   | 244 ms: 1.04x faster                                                     |
| deepcopy_reduce            | 4.07 us                                                  | 3.96 us: 1.03x faster                                                    |
| json                       | 5.73 ms                                                  | 5.60 ms: 1.02x faster                                                    |
| async_tree_cpu_io_mixed    | 766 ms                                                   | 752 ms: 1.02x faster                                                     |
| xml_etree_generate         | 113 ms                                                   | 111 ms: 1.02x faster                                                     |
| mako                       | 13.4 ms                                                  | 13.1 ms: 1.02x faster                                                    |
| telco                      | 9.74 ms                                                  | 9.61 ms: 1.01x faster                                                    |
| regex_v8                   | 31.8 ms                                                  | 31.4 ms: 1.01x faster                                                    |
| thrift                     | 968 us                                                   | 957 us: 1.01x faster                                                     |
| bpe_tokeniser              | 5.87 sec                                                 | 5.92 sec: 1.01x slower                                                   |
| scimark_fft                | 447 ms                                                   | 456 ms: 1.02x slower                                                     |
| tomli_loads                | 2.54 sec                                                 | 2.64 sec: 1.04x slower                                                   |
| async_generators           | 489 ms                                                   | 510 ms: 1.04x slower                                                     |
| mdp                        | 3.34 sec                                                 | 3.49 sec: 1.05x slower                                                   |
| logging_format             | 7.82 us                                                  | 8.18 us: 1.05x slower                                                    |
| float                      | 93.3 ms                                                  | 98.0 ms: 1.05x slower                                                    |
| json_dumps                 | 13.6 ms                                                  | 14.3 ms: 1.05x slower                                                    |
| logging_simple             | 7.07 us                                                  | 7.47 us: 1.06x slower                                                    |
| async_tree_io              | 1.11 sec                                                 | 1.18 sec: 1.07x slower                                                   |
| unpickle_pure_python       | 251 us                                                   | 268 us: 1.07x slower                                                     |
| bench_thread_pool          | 1.27 ms                                                  | 1.37 ms: 1.07x slower                                                    |
| fannkuch                   | 461 ms                                                   | 495 ms: 1.07x slower                                                     |
| crypto_pyaes               | 83.7 ms                                                  | 90.2 ms: 1.08x slower                                                    |
| html5lib                   | 66.4 ms                                                  | 71.5 ms: 1.08x slower                                                    |
| scimark_monte_carlo        | 83.6 ms                                                  | 90.1 ms: 1.08x slower                                                    |
| scimark_lu                 | 139 ms                                                   | 151 ms: 1.08x slower                                                     |
| spectral_norm              | 143 ms                                                   | 155 ms: 1.09x slower                                                     |
| pickle_pure_python         | 357 us                                                   | 389 us: 1.09x slower                                                     |
| meteor_contest             | 114 ms                                                   | 125 ms: 1.10x slower                                                     |
| pyflate                    | 556 ms                                                   | 612 ms: 1.10x slower                                                     |
| async_tree_io_tg           | 1.13 sec                                                 | 1.25 sec: 1.10x slower                                                   |
| scimark_sparse_mat_mult    | 6.51 ms                                                  | 7.19 ms: 1.10x slower                                                    |
| typing_runtime_protocols   | 193 us                                                   | 214 us: 1.11x slower                                                     |
| create_gc_cycles           | 3.35 ms                                                  | 3.71 ms: 1.11x slower                                                    |
| gc_traversal               | 5.77 ms                                                  | 6.43 ms: 1.11x slower                                                    |
| go                         | 160 ms                                                   | 184 ms: 1.15x slower                                                     |
| tornado_http               | 128 ms                                                   | 147 ms: 1.15x slower                                                     |
| pycparser                  | 1.27 sec                                                 | 1.48 sec: 1.16x slower                                                   |
| deltablue                  | 3.82 ms                                                  | 4.52 ms: 1.18x slower                                                    |
| richards_super             | 60.1 ms                                                  | 71.5 ms: 1.19x slower                                                    |
| raytrace                   | 300 ms                                                   | 358 ms: 1.19x slower                                                     |
| richards                   | 53.6 ms                                                  | 64.3 ms: 1.20x slower                                                    |
| genshi_text                | 27.7 ms                                                  | 33.5 ms: 1.21x slower                                                    |
| comprehensions             | 20.4 us                                                  | 24.7 us: 1.21x slower                                                    |
| nqueens                    | 100 ms                                                   | 122 ms: 1.22x slower                                                     |
| sqlglot_normalize          | 127 ms                                                   | 156 ms: 1.23x slower                                                     |
| django_template            | 41.6 ms                                                  | 51.1 ms: 1.23x slower                                                    |
| sqlglot_parse              | 1.38 ms                                                  | 1.70 ms: 1.23x slower                                                    |
| sphinx                     | 1.17 sec                                                 | 1.45 sec: 1.24x slower                                                   |
| chaos                      | 68.0 ms                                                  | 85.0 ms: 1.25x slower                                                    |
| 2to3                       | 304 ms                                                   | 381 ms: 1.25x slower                                                     |
| sqlglot_transpile          | 1.73 ms                                                  | 2.18 ms: 1.26x slower                                                    |
| docutils                   | 2.89 sec                                                 | 3.65 sec: 1.26x slower                                                   |
| pprint_safe_repr           | 926 ms                                                   | 1.20 sec: 1.29x slower                                                   |
| sympy_expand               | 457 ms                                                   | 592 ms: 1.30x slower                                                     |
| sqlglot_optimize           | 62.2 ms                                                  | 81.8 ms: 1.32x slower                                                    |
| regex_compile              | 127 ms                                                   | 169 ms: 1.33x slower                                                     |
| pprint_pformat             | 1.90 sec                                                 | 2.54 sec: 1.34x slower                                                   |
| genshi_xml                 | 60.3 ms                                                  | 81.5 ms: 1.35x slower                                                    |
| sympy_str                  | 264 ms                                                   | 358 ms: 1.35x slower                                                     |
| sympy_integrate            | 20.8 ms                                                  | 29.1 ms: 1.40x slower                                                    |
| hexiom                     | 7.11 ms                                                  | 10.2 ms: 1.44x slower                                                    |
| pylint                     | 342 ms                                                   | 492 ms: 1.44x slower                                                     |
| sympy_sum                  | 144 ms                                                   | 215 ms: 1.50x slower                                                     |
| generators                 | 37.6 ms                                                  | 59.0 ms: 1.57x slower                                                    |
| bench_mp_pool              | 7.68 ms                                                  | 1.59 sec: 206.77x slower                                                 |
| Geometric mean             | (ref)                                                    | 1.16x slower                                                             |

Benchmark hidden because not significant (12): scimark_sor, regex_effbot, json_loads, logging_silent, coverage, xml_etree_process, asyncio_websockets, coroutines, python_startup_no_site, nbody, xml_etree_iterparse, pidigits
Ignored benchmarks (8) of results/bm-20241007-3.13.0-60403a5/bm-20241007-arminc-aarch64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (10) of results/bm-20241016-3.14.0a1+-760872e-JIT/bm-20241016-arminc-aarch64-python-760872efecb95017db8e-3.14.0a1+-760872e.json: asyncio_tcp, asyncio_tcp_ssl, dulwich_log, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.091x slower
# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.05x
- 95% likely to have a slowdown of 1.04x
- 99% likely to have a slowdown of 1.03x

# Memory
- memory change: 1.08x