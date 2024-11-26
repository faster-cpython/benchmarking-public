# Results vs. 3.13.0

- fork: faster-cpython
- ref: use_stackrefs
- machine: linux-x86_64
- commit hash: f03f745
- commit date: 2024-10-29
- overall geometric mean: 1.005x slower
- HPT reliability: 99.86%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.02x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 260 ms: 1.03x faster                                                      |
| docutils       | 2.59 sec                                               | 2.71 sec: 1.05x slower                                                    |
| sphinx         | 1.03 sec                                               | 1.07 sec: 1.03x slower                                                    |
| Geometric mean | (ref)                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 384 ms: 1.21x faster                                                      |
| async_tree_none            | 351 ms                                                 | 334 ms: 1.05x faster                                                      |
| async_tree_memoization     | 442 ms                                                 | 422 ms: 1.05x faster                                                      |
| async_generators           | 436 ms                                                 | 439 ms: 1.01x slower                                                      |
| asyncio_websockets         | 552 ms                                                 | 556 ms: 1.01x slower                                                      |
| async_tree_io              | 842 ms                                                 | 882 ms: 1.05x slower                                                      |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 574 ms: 1.05x slower                                                      |
| coroutines                 | 22.7 ms                                                | 24.3 ms: 1.07x slower                                                     |
| async_tree_io_tg           | 857 ms                                                 | 989 ms: 1.15x slower                                                      |
| Geometric mean             | (ref)                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (2): async_tree_cpu_io_mixed, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                      |
| float          | 79.2 ms                                                | 81.1 ms: 1.02x slower                                                     |
| nbody          | 87.0 ms                                                | 94.3 ms: 1.08x slower                                                     |
| Geometric mean | (ref)                                                  | 1.04x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 25.7 ms: 1.02x faster                                                     |
| regex_compile  | 132 ms                                                 | 130 ms: 1.01x faster                                                      |
| regex_effbot   | 3.73 ms                                                | 3.76 ms: 1.01x slower                                                     |
| regex_dna      | 218 ms                                                 | 221 ms: 1.01x slower                                                      |
| Geometric mean | (ref)                                                  | 1.00x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_loads           | 27.2 us                                                | 26.5 us: 1.03x faster                                                     |
| tomli_loads          | 2.14 sec                                               | 2.09 sec: 1.02x faster                                                    |
| xml_etree_generate   | 86.7 ms                                                | 87.4 ms: 1.01x slower                                                     |
| unpickle_pure_python | 216 us                                                 | 219 us: 1.01x slower                                                      |
| xml_etree_parse      | 156 ms                                                 | 158 ms: 1.02x slower                                                      |
| pickle_pure_python   | 310 us                                                 | 317 us: 1.02x slower                                                      |
| xml_etree_iterparse  | 101 ms                                                 | 105 ms: 1.04x slower                                                      |
| json_dumps           | 10.6 ms                                                | 11.6 ms: 1.10x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.02x slower                                                              |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 7.07 ms: 1.02x slower                                                     |
| python_startup         | 12.5 ms                                                | 12.8 ms: 1.02x slower                                                     |
| Geometric mean         | (ref)                                                  | 1.02x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 23.5 ms                                                | 22.6 ms: 1.04x faster                                                     |
| genshi_xml      | 50.9 ms                                                | 50.5 ms: 1.01x faster                                                     |
| django_template | 35.2 ms                                                | 35.6 ms: 1.01x slower                                                     |
| mako            | 11.1 ms                                                | 11.6 ms: 1.05x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| deepcopy                   | 358 us                                                 | 266 us: 1.35x faster                                                      |
| deepcopy_memo              | 39.1 us                                                | 30.7 us: 1.27x faster                                                     |
| async_tree_memoization_tg  | 464 ms                                                 | 384 ms: 1.21x faster                                                      |
| go                         | 144 ms                                                 | 120 ms: 1.20x faster                                                      |
| deepcopy_reduce            | 3.20 us                                                | 2.81 us: 1.14x faster                                                     |
| json                       | 5.36 ms                                                | 4.89 ms: 1.10x faster                                                     |
| pathlib                    | 17.5 ms                                                | 16.2 ms: 1.09x faster                                                     |
| mdp                        | 2.72 sec                                               | 2.51 sec: 1.08x faster                                                    |
| telco                      | 8.54 ms                                                | 7.96 ms: 1.07x faster                                                     |
| richards                   | 48.7 ms                                                | 46.2 ms: 1.05x faster                                                     |
| async_tree_none            | 351 ms                                                 | 334 ms: 1.05x faster                                                      |
| async_tree_memoization     | 442 ms                                                 | 422 ms: 1.05x faster                                                      |
| pycparser                  | 1.20 sec                                               | 1.15 sec: 1.05x faster                                                    |
| richards_super             | 54.9 ms                                                | 52.5 ms: 1.04x faster                                                     |
| genshi_text                | 23.5 ms                                                | 22.6 ms: 1.04x faster                                                     |
| crypto_pyaes               | 75.3 ms                                                | 73.3 ms: 1.03x faster                                                     |
| 2to3                       | 267 ms                                                 | 260 ms: 1.03x faster                                                      |
| json_loads                 | 27.2 us                                                | 26.5 us: 1.03x faster                                                     |
| tomli_loads                | 2.14 sec                                               | 2.09 sec: 1.02x faster                                                    |
| regex_v8                   | 26.2 ms                                                | 25.7 ms: 1.02x faster                                                     |
| logging_format             | 6.40 us                                                | 6.27 us: 1.02x faster                                                     |
| sqlalchemy_declarative     | 133 ms                                                 | 131 ms: 1.02x faster                                                      |
| regex_compile              | 132 ms                                                 | 130 ms: 1.01x faster                                                      |
| logging_silent             | 102 ns                                                 | 101 ns: 1.01x faster                                                      |
| genshi_xml                 | 50.9 ms                                                | 50.5 ms: 1.01x faster                                                     |
| meteor_contest             | 109 ms                                                 | 108 ms: 1.01x faster                                                      |
| logging_simple             | 5.72 us                                                | 5.68 us: 1.01x faster                                                     |
| thrift                     | 809 us                                                 | 803 us: 1.01x faster                                                      |
| generators                 | 29.0 ms                                                | 28.8 ms: 1.01x faster                                                     |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                      |
| dulwich_log                | 64.3 ms                                                | 64.5 ms: 1.00x slower                                                     |
| spectral_norm              | 115 ms                                                 | 116 ms: 1.00x slower                                                      |
| async_generators           | 436 ms                                                 | 439 ms: 1.01x slower                                                      |
| sympy_str                  | 275 ms                                                 | 277 ms: 1.01x slower                                                      |
| xml_etree_generate         | 86.7 ms                                                | 87.4 ms: 1.01x slower                                                     |
| asyncio_websockets         | 552 ms                                                 | 556 ms: 1.01x slower                                                      |
| regex_effbot               | 3.73 ms                                                | 3.76 ms: 1.01x slower                                                     |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 5.09 ms: 1.01x slower                                                     |
| hexiom                     | 6.16 ms                                                | 6.22 ms: 1.01x slower                                                     |
| regex_dna                  | 218 ms                                                 | 221 ms: 1.01x slower                                                      |
| django_template            | 35.2 ms                                                | 35.6 ms: 1.01x slower                                                     |
| sqlglot_transpile          | 1.58 ms                                                | 1.60 ms: 1.01x slower                                                     |
| unpickle_pure_python       | 216 us                                                 | 219 us: 1.01x slower                                                      |
| python_startup_no_site     | 6.96 ms                                                | 7.07 ms: 1.02x slower                                                     |
| xml_etree_parse            | 156 ms                                                 | 158 ms: 1.02x slower                                                      |
| connected_components       | 444 ms                                                 | 451 ms: 1.02x slower                                                      |
| scimark_fft                | 364 ms                                                 | 370 ms: 1.02x slower                                                      |
| sqlglot_optimize           | 53.7 ms                                                | 54.7 ms: 1.02x slower                                                     |
| shortest_path              | 481 ms                                                 | 489 ms: 1.02x slower                                                      |
| sympy_expand               | 463 ms                                                 | 472 ms: 1.02x slower                                                      |
| sqlglot_parse              | 1.27 ms                                                | 1.30 ms: 1.02x slower                                                     |
| pickle_pure_python         | 310 us                                                 | 317 us: 1.02x slower                                                      |
| sympy_integrate            | 19.9 ms                                                | 20.3 ms: 1.02x slower                                                     |
| sqlglot_normalize          | 108 ms                                                 | 110 ms: 1.02x slower                                                      |
| python_startup             | 12.5 ms                                                | 12.8 ms: 1.02x slower                                                     |
| float                      | 79.2 ms                                                | 81.1 ms: 1.02x slower                                                     |
| pyflate                    | 471 ms                                                 | 482 ms: 1.02x slower                                                      |
| bpe_tokeniser              | 4.75 sec                                               | 4.86 sec: 1.02x slower                                                    |
| deltablue                  | 3.23 ms                                                | 3.31 ms: 1.03x slower                                                     |
| scimark_monte_carlo        | 67.4 ms                                                | 69.5 ms: 1.03x slower                                                     |
| sphinx                     | 1.03 sec                                               | 1.07 sec: 1.03x slower                                                    |
| comprehensions             | 16.5 us                                                | 17.1 us: 1.04x slower                                                     |
| scimark_lu                 | 113 ms                                                 | 117 ms: 1.04x slower                                                      |
| xml_etree_iterparse        | 101 ms                                                 | 105 ms: 1.04x slower                                                      |
| raytrace                   | 267 ms                                                 | 278 ms: 1.04x slower                                                      |
| gc_traversal               | 4.37 ms                                                | 4.55 ms: 1.04x slower                                                     |
| bench_thread_pool          | 822 us                                                 | 858 us: 1.04x slower                                                      |
| docutils                   | 2.59 sec                                               | 2.71 sec: 1.05x slower                                                    |
| mako                       | 11.1 ms                                                | 11.6 ms: 1.05x slower                                                     |
| async_tree_io              | 842 ms                                                 | 882 ms: 1.05x slower                                                      |
| pprint_safe_repr           | 728 ms                                                 | 763 ms: 1.05x slower                                                      |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 574 ms: 1.05x slower                                                      |
| pprint_pformat             | 1.49 sec                                               | 1.57 sec: 1.05x slower                                                    |
| fannkuch                   | 404 ms                                                 | 427 ms: 1.06x slower                                                      |
| nqueens                    | 78.4 ms                                                | 82.9 ms: 1.06x slower                                                     |
| coroutines                 | 22.7 ms                                                | 24.3 ms: 1.07x slower                                                     |
| chaos                      | 58.1 ms                                                | 62.5 ms: 1.08x slower                                                     |
| nbody                      | 87.0 ms                                                | 94.3 ms: 1.08x slower                                                     |
| scimark_sor                | 124 ms                                                 | 135 ms: 1.09x slower                                                      |
| json_dumps                 | 10.6 ms                                                | 11.6 ms: 1.10x slower                                                     |
| create_gc_cycles           | 2.41 ms                                                | 2.67 ms: 1.11x slower                                                     |
| async_tree_io_tg           | 857 ms                                                 | 989 ms: 1.15x slower                                                      |
| k_core                     | 2.35 sec                                               | 3.61 sec: 1.53x slower                                                    |
| bench_mp_pool              | 24.0 ms                                                | 79.1 ms: 3.30x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.02x slower                                                              |

Benchmark hidden because not significant (10): html5lib, typing_runtime_protocols, coverage, xml_etree_process, sympy_sum, tornado_http, sqlalchemy_imperative, async_tree_cpu_io_mixed, async_tree_none_tg, pylint
Ignored benchmarks (3) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2
Ignored benchmarks (1) of results/bm-20241029-3.14.0a1+-f03f745/bm-20241029-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a1+-f03f745.json: sqlite_synth

- Geometric mean (including insignificant results): 1.005x slower
# HPT report

- Reliability score: 99.86% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.02x