# Results vs. 3.13.0

- fork: faster-cpython
- ref: mark_first_gc
- machine: linux-x86_64
- commit hash: 3c18fc8
- commit date: 2024-11-06
- overall geometric mean: 1.056x faster
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241106-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-3c18fc8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 267 ms                                                 | 258 ms: 1.03x faster                                                      |
| docutils       | 2.59 sec                                               | 2.65 sec: 1.02x slower                                                    |
| html5lib       | 64.2 ms                                                | 64.8 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (1): sphinx

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241106-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-3c18fc8 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_memoization_tg  | 464 ms                                                 | 316 ms: 1.47x faster                                                      |
| async_tree_io_tg           | 857 ms                                                 | 594 ms: 1.44x faster                                                      |
| async_tree_io              | 842 ms                                                 | 608 ms: 1.38x faster                                                      |
| async_tree_none            | 351 ms                                                 | 261 ms: 1.35x faster                                                      |
| async_tree_memoization     | 442 ms                                                 | 334 ms: 1.32x faster                                                      |
| async_tree_none_tg         | 321 ms                                                 | 247 ms: 1.30x faster                                                      |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 492 ms: 1.17x faster                                                      |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 480 ms: 1.14x faster                                                      |
| async_generators           | 436 ms                                                 | 428 ms: 1.02x faster                                                      |
| asyncio_websockets         | 552 ms                                                 | 556 ms: 1.01x slower                                                      |
| coroutines                 | 22.7 ms                                                | 23.0 ms: 1.02x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.22x faster                                                              |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241106-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-3c18fc8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 79.2 ms                                                | 78.4 ms: 1.01x faster                                                     |
| pidigits       | 186 ms                                                 | 187 ms: 1.00x slower                                                      |
| nbody          | 87.0 ms                                                | 95.3 ms: 1.10x slower                                                     |
| Geometric mean | (ref)                                                  | 1.03x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241106-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-3c18fc8 |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                | 24.8 ms: 1.06x faster                                                     |
| regex_compile  | 132 ms                                                 | 130 ms: 1.02x faster                                                      |
| regex_dna      | 218 ms                                                 | 216 ms: 1.01x faster                                                      |
| regex_effbot   | 3.73 ms                                                | 3.75 ms: 1.00x slower                                                     |
| Geometric mean | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241106-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-3c18fc8 |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_parse      | 156 ms                                                 | 145 ms: 1.07x faster                                                      |
| json_loads           | 27.2 us                                                | 26.1 us: 1.04x faster                                                     |
| xml_etree_process    | 60.6 ms                                                | 59.6 ms: 1.02x faster                                                     |
| xml_etree_generate   | 86.7 ms                                                | 85.4 ms: 1.02x faster                                                     |
| tomli_loads          | 2.14 sec                                               | 2.13 sec: 1.01x faster                                                    |
| unpickle_pure_python | 216 us                                                 | 217 us: 1.00x slower                                                      |
| pickle_pure_python   | 310 us                                                 | 326 us: 1.05x slower                                                      |
| json_dumps           | 10.6 ms                                                | 11.2 ms: 1.06x slower                                                     |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                              |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241106-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-3c18fc8 |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 6.96 ms                                                | 6.78 ms: 1.03x faster                                                     |
| python_startup         | 12.5 ms                                                | 12.3 ms: 1.01x faster                                                     |
| Geometric mean         | (ref)                                                  | 1.02x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241106-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-3c18fc8 |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 23.5 ms                                                | 22.3 ms: 1.05x faster                                                     |
| django_template | 35.2 ms                                                | 34.2 ms: 1.03x faster                                                     |
| genshi_xml      | 50.9 ms                                                | 49.9 ms: 1.02x faster                                                     |
| mako            | 11.1 ms                                                | 11.4 ms: 1.03x slower                                                     |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5 | bm-20241106-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-3c18fc8 |
|----------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------------:|
| gc_traversal               | 4.37 ms                                                | 2.32 ms: 1.89x faster                                                     |
| async_tree_memoization_tg  | 464 ms                                                 | 316 ms: 1.47x faster                                                      |
| async_tree_io_tg           | 857 ms                                                 | 594 ms: 1.44x faster                                                      |
| create_gc_cycles           | 2.41 ms                                                | 1.71 ms: 1.41x faster                                                     |
| async_tree_io              | 842 ms                                                 | 608 ms: 1.38x faster                                                      |
| async_tree_none            | 351 ms                                                 | 261 ms: 1.35x faster                                                      |
| deepcopy                   | 358 us                                                 | 267 us: 1.34x faster                                                      |
| async_tree_memoization     | 442 ms                                                 | 334 ms: 1.32x faster                                                      |
| async_tree_none_tg         | 321 ms                                                 | 247 ms: 1.30x faster                                                      |
| deepcopy_memo              | 39.1 us                                                | 31.3 us: 1.25x faster                                                     |
| go                         | 144 ms                                                 | 118 ms: 1.22x faster                                                      |
| pylint                     | 313 ms                                                 | 262 ms: 1.19x faster                                                      |
| deepcopy_reduce            | 3.20 us                                                | 2.72 us: 1.18x faster                                                     |
| async_tree_cpu_io_mixed    | 577 ms                                                 | 492 ms: 1.17x faster                                                      |
| async_tree_cpu_io_mixed_tg | 546 ms                                                 | 480 ms: 1.14x faster                                                      |
| json                       | 5.36 ms                                                | 4.76 ms: 1.13x faster                                                     |
| pathlib                    | 17.5 ms                                                | 15.9 ms: 1.10x faster                                                     |
| generators                 | 29.0 ms                                                | 26.7 ms: 1.08x faster                                                     |
| pycparser                  | 1.20 sec                                               | 1.12 sec: 1.08x faster                                                    |
| xml_etree_parse            | 156 ms                                                 | 145 ms: 1.07x faster                                                      |
| richards                   | 48.7 ms                                                | 45.5 ms: 1.07x faster                                                     |
| telco                      | 8.54 ms                                                | 8.00 ms: 1.07x faster                                                     |
| mdp                        | 2.72 sec                                               | 2.57 sec: 1.06x faster                                                    |
| regex_v8                   | 26.2 ms                                                | 24.8 ms: 1.06x faster                                                     |
| genshi_text                | 23.5 ms                                                | 22.3 ms: 1.05x faster                                                     |
| thrift                     | 809 us                                                 | 768 us: 1.05x faster                                                      |
| richards_super             | 54.9 ms                                                | 52.3 ms: 1.05x faster                                                     |
| json_loads                 | 27.2 us                                                | 26.1 us: 1.04x faster                                                     |
| sqlalchemy_declarative     | 133 ms                                                 | 128 ms: 1.04x faster                                                      |
| logging_format             | 6.40 us                                                | 6.15 us: 1.04x faster                                                     |
| 2to3                       | 267 ms                                                 | 258 ms: 1.03x faster                                                      |
| typing_runtime_protocols   | 165 us                                                 | 160 us: 1.03x faster                                                      |
| logging_simple             | 5.72 us                                                | 5.55 us: 1.03x faster                                                     |
| django_template            | 35.2 ms                                                | 34.2 ms: 1.03x faster                                                     |
| python_startup_no_site     | 6.96 ms                                                | 6.78 ms: 1.03x faster                                                     |
| bpe_tokeniser              | 4.75 sec                                               | 4.62 sec: 1.03x faster                                                    |
| crypto_pyaes               | 75.3 ms                                                | 73.4 ms: 1.03x faster                                                     |
| sympy_sum                  | 150 ms                                                 | 147 ms: 1.03x faster                                                      |
| sympy_str                  | 275 ms                                                 | 269 ms: 1.02x faster                                                      |
| genshi_xml                 | 50.9 ms                                                | 49.9 ms: 1.02x faster                                                     |
| k_core                     | 2.35 sec                                               | 2.31 sec: 1.02x faster                                                    |
| async_generators           | 436 ms                                                 | 428 ms: 1.02x faster                                                      |
| xml_etree_process          | 60.6 ms                                                | 59.6 ms: 1.02x faster                                                     |
| sqlalchemy_imperative      | 17.1 ms                                                | 16.8 ms: 1.02x faster                                                     |
| regex_compile              | 132 ms                                                 | 130 ms: 1.02x faster                                                      |
| xml_etree_generate         | 86.7 ms                                                | 85.4 ms: 1.02x faster                                                     |
| sympy_expand               | 463 ms                                                 | 457 ms: 1.01x faster                                                      |
| meteor_contest             | 109 ms                                                 | 107 ms: 1.01x faster                                                      |
| python_startup             | 12.5 ms                                                | 12.3 ms: 1.01x faster                                                     |
| regex_dna                  | 218 ms                                                 | 216 ms: 1.01x faster                                                      |
| float                      | 79.2 ms                                                | 78.4 ms: 1.01x faster                                                     |
| connected_components       | 444 ms                                                 | 439 ms: 1.01x faster                                                      |
| pyflate                    | 471 ms                                                 | 467 ms: 1.01x faster                                                      |
| sqlglot_normalize          | 108 ms                                                 | 107 ms: 1.01x faster                                                      |
| pprint_pformat             | 1.49 sec                                               | 1.49 sec: 1.01x faster                                                    |
| tomli_loads                | 2.14 sec                                               | 2.13 sec: 1.01x faster                                                    |
| pidigits                   | 186 ms                                                 | 187 ms: 1.00x slower                                                      |
| unpickle_pure_python       | 216 us                                                 | 217 us: 1.00x slower                                                      |
| pprint_safe_repr           | 728 ms                                                 | 731 ms: 1.00x slower                                                      |
| regex_effbot               | 3.73 ms                                                | 3.75 ms: 1.00x slower                                                     |
| asyncio_websockets         | 552 ms                                                 | 556 ms: 1.01x slower                                                      |
| spectral_norm              | 115 ms                                                 | 116 ms: 1.01x slower                                                      |
| html5lib                   | 64.2 ms                                                | 64.8 ms: 1.01x slower                                                     |
| sqlglot_transpile          | 1.58 ms                                                | 1.60 ms: 1.01x slower                                                     |
| sqlglot_parse              | 1.27 ms                                                | 1.29 ms: 1.01x slower                                                     |
| coroutines                 | 22.7 ms                                                | 23.0 ms: 1.02x slower                                                     |
| comprehensions             | 16.5 us                                                | 16.8 us: 1.02x slower                                                     |
| hexiom                     | 6.16 ms                                                | 6.28 ms: 1.02x slower                                                     |
| scimark_monte_carlo        | 67.4 ms                                                | 68.8 ms: 1.02x slower                                                     |
| docutils                   | 2.59 sec                                               | 2.65 sec: 1.02x slower                                                    |
| bench_thread_pool          | 822 us                                                 | 841 us: 1.02x slower                                                      |
| coverage                   | 84.0 ms                                                | 86.1 ms: 1.02x slower                                                     |
| deltablue                  | 3.23 ms                                                | 3.31 ms: 1.02x slower                                                     |
| raytrace                   | 267 ms                                                 | 274 ms: 1.03x slower                                                      |
| scimark_sparse_mat_mult    | 5.04 ms                                                | 5.19 ms: 1.03x slower                                                     |
| mako                       | 11.1 ms                                                | 11.4 ms: 1.03x slower                                                     |
| scimark_fft                | 364 ms                                                 | 375 ms: 1.03x slower                                                      |
| nqueens                    | 78.4 ms                                                | 80.8 ms: 1.03x slower                                                     |
| scimark_sor                | 124 ms                                                 | 129 ms: 1.05x slower                                                      |
| pickle_pure_python         | 310 us                                                 | 326 us: 1.05x slower                                                      |
| scimark_lu                 | 113 ms                                                 | 119 ms: 1.05x slower                                                      |
| chaos                      | 58.1 ms                                                | 61.1 ms: 1.05x slower                                                     |
| logging_silent             | 102 ns                                                 | 107 ns: 1.05x slower                                                      |
| json_dumps                 | 10.6 ms                                                | 11.2 ms: 1.06x slower                                                     |
| nbody                      | 87.0 ms                                                | 95.3 ms: 1.10x slower                                                     |
| bench_mp_pool              | 24.0 ms                                                | 80.2 ms: 3.34x slower                                                     |
| Geometric mean             | (ref)                                                  | 1.04x faster                                                              |

Benchmark hidden because not significant (7): sphinx, fannkuch, sympy_integrate, dulwich_log, xml_etree_iterparse, sqlglot_optimize, shortest_path
Ignored benchmarks (4) of results/bm-20241007-3.13.0-60403a5/bm-20241007-linux-x86_64-python-v3.13.0-3.13.0-60403a5.json: chameleon, gevent_hub, mypy2, tornado_http
Ignored benchmarks (1) of results/bm-20241106-3.14.0a1+-3c18fc8/bm-20241106-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-3c18fc8.json: sqlite_synth

- Geometric mean (including insignificant results): 1.056x faster
# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x