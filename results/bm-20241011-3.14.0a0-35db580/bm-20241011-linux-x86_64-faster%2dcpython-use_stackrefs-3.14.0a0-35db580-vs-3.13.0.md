# Results vs. 3.13.0

- fork: faster-cpython
- ref: use_stackrefs
- machine: linux-x86_64
- commit hash: 35db580
- commit date: 2024-10-11
- overall geometric mean: 1.011x faster
- HPT reliability: 94.82%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.91x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 259 ms: 1.03x faster                                                     |
| docutils       | 2.59 sec                                               | 2.66 sec: 1.03x slower                                                   |
| html5lib       | 64.2 ms                                                | 62.5 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                  | 1.01x faster                                                             |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 417 ms: 1.11x faster                                                     |
| async_tree_none            | 351 ms                                                 | 334 ms: 1.05x faster                                                     |
| async_tree_memoization     | 442 ms                                                 | 427 ms: 1.04x faster                                                     |
| asyncio_websockets         | 552 ms                                                 | 554 ms: 1.00x slower                                                     |
| async_generators           | 436 ms                                                 | 444 ms: 1.02x slower                                                     |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 560 ms: 1.03x slower                                                     |
| async_tree_io_tg           | 857 ms                                                 | 886 ms: 1.03x slower                                                     |
| coroutines                 | 22.7 ms                                                | 25.3 ms: 1.11x slower                                                    |
| async_tree_io              | 842 ms                                                 | 960 ms: 1.14x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                             |

Benchmark hidden because not significant (2): async_tree_none_tg, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 188 ms: 1.01x slower                                                     |
| nbody          | 87.0 ms                                                | 93.2 ms: 1.07x slower                                                    |
| Geometric mean | (ref)                                                  | 1.03x slower                                                             |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.3 ms: 1.08x faster                                                    |
| regex_effbot   | 3.73 ms                                                | 3.56 ms: 1.05x faster                                                    |
| regex_compile  | 132 ms                                                 | 131 ms: 1.01x faster                                                     |
| Geometric mean | (ref)                                                  | 1.04x faster                                                             |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_loads           | 27.2 us                                                | 26.7 us: 1.02x faster                                                    |
| tomli_loads          | 2.14 sec                                               | 2.12 sec: 1.01x faster                                                   |
| xml_etree_process    | 60.6 ms                                                | 60.3 ms: 1.01x faster                                                    |
| unpickle_pure_python | 216 us                                                 | 217 us: 1.00x slower                                                     |
| pickle_pure_python   | 310 us                                                 | 315 us: 1.01x slower                                                     |
| xml_etree_iterparse  | 101 ms                                                 | 105 ms: 1.04x slower                                                     |
| json_dumps           | 10.6 ms                                                | 11.8 ms: 1.11x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                             |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 12.5 ms                                                | 10.6 ms: 1.18x faster                                                    |
| python_startup_no_site | 6.96 ms                                                | 7.03 ms: 1.01x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.08x faster                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text     | 23.5 ms                                                | 22.5 ms: 1.05x faster                                                    |
| genshi_xml      | 50.9 ms                                                | 50.1 ms: 1.02x faster                                                    |
| django_template | 35.2 ms                                                | 35.5 ms: 1.01x slower                                                    |
| mako            | 11.1 ms                                                | 11.8 ms: 1.07x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                             |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580 |
|----------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| create_gc_cycles           | 2.41 ms                                                | 1.78 ms: 1.36x faster                                                    |
| deepcopy                   | 358 us                                                 | 266 us: 1.35x faster                                                     |
| deepcopy_memo              | 39.1 us                                                | 31.2 us: 1.25x faster                                                    |
| go                         | 144 ms                                                 | 121 ms: 1.19x faster                                                     |
| python_startup             | 12.5 ms                                                | 10.6 ms: 1.18x faster                                                    |
| gc_traversal               | 4.37 ms                                                | 3.77 ms: 1.16x faster                                                    |
| deepcopy_reduce            | 3.20 us                                                | 2.78 us: 1.15x faster                                                    |
| async_tree_memoization_tg  | 464 ms                                                 | 417 ms: 1.11x faster                                                     |
| regex_v8                   | 26.2 ms                                                | 24.3 ms: 1.08x faster                                                    |
| pathlib                    | 17.5 ms                                                | 16.3 ms: 1.07x faster                                                    |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 4.70 ms: 1.07x faster                                                    |
| telco                      | 8.54 ms                                                | 8.06 ms: 1.06x faster                                                    |
| json                       | 5.36 ms                                                | 5.09 ms: 1.05x faster                                                    |
| regex_effbot               | 3.73 ms                                                | 3.56 ms: 1.05x faster                                                    |
| async_tree_none            | 351 ms                                                 | 334 ms: 1.05x faster                                                     |
| genshi_text                | 23.5 ms                                                | 22.5 ms: 1.05x faster                                                    |
| mdp                        | 2.72 sec                                               | 2.61 sec: 1.04x faster                                                   |
| async_tree_memoization     | 442 ms                                                 | 427 ms: 1.04x faster                                                     |
| 2to3                       | 267 ms                                                 | 259 ms: 1.03x faster                                                     |
| richards                   | 48.7 ms                                                | 47.3 ms: 1.03x faster                                                    |
| html5lib                   | 64.2 ms                                                | 62.5 ms: 1.03x faster                                                    |
| json_loads                 | 27.2 us                                                | 26.7 us: 1.02x faster                                                    |
| richards_super             | 54.9 ms                                                | 54.0 ms: 1.02x faster                                                    |
| genshi_xml                 | 50.9 ms                                                | 50.1 ms: 1.02x faster                                                    |
| spectral_norm              | 115 ms                                                 | 114 ms: 1.01x faster                                                     |
| regex_compile              | 132 ms                                                 | 131 ms: 1.01x faster                                                     |
| meteor_contest             | 109 ms                                                 | 108 ms: 1.01x faster                                                     |
| tomli_loads                | 2.14 sec                                               | 2.12 sec: 1.01x faster                                                   |
| thrift                     | 809 us                                                 | 802 us: 1.01x faster                                                     |
| xml_etree_process          | 60.6 ms                                                | 60.3 ms: 1.01x faster                                                    |
| crypto_pyaes               | 75.3 ms                                                | 75.5 ms: 1.00x slower                                                    |
| unpickle_pure_python       | 216 us                                                 | 217 us: 1.00x slower                                                     |
| asyncio_websockets         | 552 ms                                                 | 554 ms: 1.00x slower                                                     |
| generators                 | 29.0 ms                                                | 29.2 ms: 1.01x slower                                                    |
| coverage                   | 84.0 ms                                                | 84.7 ms: 1.01x slower                                                    |
| pidigits                   | 186 ms                                                 | 188 ms: 1.01x slower                                                     |
| bpe_tokeniser              | 4.75 sec                                               | 4.79 sec: 1.01x slower                                                   |
| python_startup_no_site     | 6.96 ms                                                | 7.03 ms: 1.01x slower                                                    |
| django_template            | 35.2 ms                                                | 35.5 ms: 1.01x slower                                                    |
| pickle_pure_python         | 310 us                                                 | 315 us: 1.01x slower                                                     |
| sympy_integrate            | 19.9 ms                                                | 20.2 ms: 1.01x slower                                                    |
| logging_simple             | 5.72 us                                                | 5.80 us: 1.01x slower                                                    |
| sqlglot_normalize          | 108 ms                                                 | 109 ms: 1.01x slower                                                     |
| dulwich_log                | 64.3 ms                                                | 65.4 ms: 1.02x slower                                                    |
| async_generators           | 436 ms                                                 | 444 ms: 1.02x slower                                                     |
| sympy_expand               | 463 ms                                                 | 472 ms: 1.02x slower                                                     |
| deltablue                  | 3.23 ms                                                | 3.29 ms: 1.02x slower                                                    |
| sqlglot_optimize           | 53.7 ms                                                | 54.9 ms: 1.02x slower                                                    |
| scimark_monte_carlo        | 67.4 ms                                                | 69.0 ms: 1.02x slower                                                    |
| hexiom                     | 6.16 ms                                                | 6.32 ms: 1.03x slower                                                    |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 560 ms: 1.03x slower                                                     |
| sqlglot_transpile          | 1.58 ms                                                | 1.63 ms: 1.03x slower                                                    |
| docutils                   | 2.59 sec                                               | 2.66 sec: 1.03x slower                                                   |
| fannkuch                   | 404 ms                                                 | 418 ms: 1.03x slower                                                     |
| async_tree_io_tg           | 857 ms                                                 | 886 ms: 1.03x slower                                                     |
| sqlglot_parse              | 1.27 ms                                                | 1.32 ms: 1.04x slower                                                    |
| comprehensions             | 16.5 us                                                | 17.1 us: 1.04x slower                                                    |
| xml_etree_iterparse        | 101 ms                                                 | 105 ms: 1.04x slower                                                     |
| pyflate                    | 471 ms                                                 | 490 ms: 1.04x slower                                                     |
| bench_thread_pool          | 822 us                                                 | 858 us: 1.04x slower                                                     |
| nqueens                    | 78.4 ms                                                | 82.0 ms: 1.05x slower                                                    |
| pprint_pformat             | 1.49 sec                                               | 1.57 sec: 1.05x slower                                                   |
| pprint_safe_repr           | 728 ms                                                 | 763 ms: 1.05x slower                                                     |
| scimark_sor                | 124 ms                                                 | 131 ms: 1.06x slower                                                     |
| mako                       | 11.1 ms                                                | 11.8 ms: 1.07x slower                                                    |
| chaos                      | 58.1 ms                                                | 62.1 ms: 1.07x slower                                                    |
| nbody                      | 87.0 ms                                                | 93.2 ms: 1.07x slower                                                    |
| coroutines                 | 22.7 ms                                                | 25.3 ms: 1.11x slower                                                    |
| json_dumps                 | 10.6 ms                                                | 11.8 ms: 1.11x slower                                                    |
| async_tree_io              | 842 ms                                                 | 960 ms: 1.14x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 56.2 ms: 2.34x slower                                                    |
| Geometric mean             | (ref)                                                  | 1.00x faster                                                             |

Benchmark hidden because not significant (17): scimark_fft, pycparser, scimark_lu, xml_etree_parse, typing_runtime_protocols, xml_etree_generate, async_tree_none_tg, regex_dna, sympy_sum, tornado_http, logging_format, raytrace, async_tree_cpu_io_mixed, float, sympy_str, logging_silent, pylint
Ignored benchmarks (9) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, connected_components, gevent_hub, k_core, mypy2, shortest_path, sphinx, sqlalchemy_declarative, sqlalchemy_imperative
Ignored benchmarks (9) of results/bm-20241011-3.14.0a0-35db580/bm-20241011-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a0-35db580.json: asyncio_tcp, asyncio_tcp_ssl, pickle, pickle_dict, pickle_list, sqlite_synth, unpack_sequence, unpickle, unpickle_list

- Geometric mean (including insignificant results): 1.011x faster
# HPT report

- Reliability score: 94.82% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.91x