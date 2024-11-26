# Results vs. base

- fork: faster-cpython
- ref: mark_first_gc
- machine: linux-x86_64
- commit hash: 3c18fc8
- commit date: 2024-11-06
- overall geometric mean: 1.046x faster
- HPT reliability: 96.28%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241104-linux-x86_64-python-bfc1d2504c183a9464e6-3.14.0a1+-bfc1d25 | bm-20241106-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-3c18fc8 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 255 ms                                                                 | 258 ms: 1.01x slower                                                      |
| docutils       | 2.70 sec                                                               | 2.65 sec: 1.02x faster                                                    |
| html5lib       | 64.0 ms                                                                | 64.8 ms: 1.01x slower                                                     |
| sphinx         | 1.05 sec                                                               | 1.02 sec: 1.03x faster                                                    |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241104-linux-x86_64-python-bfc1d2504c183a9464e6-3.14.0a1+-bfc1d25 | bm-20241106-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-3c18fc8 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_io_tg           | 962 ms                                                                 | 594 ms: 1.62x faster                                                      |
| async_tree_io              | 855 ms                                                                 | 608 ms: 1.41x faster                                                      |
| async_tree_none_tg         | 321 ms                                                                 | 247 ms: 1.30x faster                                                      |
| async_tree_none            | 326 ms                                                                 | 261 ms: 1.25x faster                                                      |
| async_tree_memoization     | 413 ms                                                                 | 334 ms: 1.23x faster                                                      |
| async_tree_memoization_tg  | 375 ms                                                                 | 316 ms: 1.19x faster                                                      |
| async_tree_cpu_io_mixed_tg | 564 ms                                                                 | 480 ms: 1.17x faster                                                      |
| async_tree_cpu_io_mixed    | 577 ms                                                                 | 492 ms: 1.17x faster                                                      |
| coroutines                 | 23.4 ms                                                                | 23.0 ms: 1.01x faster                                                     |
| async_generators           | 431 ms                                                                 | 428 ms: 1.01x faster                                                      |
| Geometric mean             | (ref)                                                                  | 1.20x faster                                                              |

Benchmark hidden because not significant (1): asyncio_websockets

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241104-linux-x86_64-python-bfc1d2504c183a9464e6-3.14.0a1+-bfc1d25 | bm-20241106-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-3c18fc8 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| float          | 80.3 ms                                                                | 78.4 ms: 1.02x faster                                                     |
| pidigits       | 187 ms                                                                 | 187 ms: 1.00x faster                                                      |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241104-linux-x86_64-python-bfc1d2504c183a9464e6-3.14.0a1+-bfc1d25 | bm-20241106-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-3c18fc8 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_v8       | 25.3 ms                                                                | 24.8 ms: 1.02x faster                                                     |
| regex_compile  | 129 ms                                                                 | 130 ms: 1.01x slower                                                      |
| regex_dna      | 215 ms                                                                 | 216 ms: 1.01x slower                                                      |
| regex_effbot   | 3.65 ms                                                                | 3.75 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241104-linux-x86_64-python-bfc1d2504c183a9464e6-3.14.0a1+-bfc1d25 | bm-20241106-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-3c18fc8 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| xml_etree_parse      | 158 ms                                                                 | 145 ms: 1.09x faster                                                      |
| xml_etree_iterparse  | 105 ms                                                                 | 101 ms: 1.03x faster                                                      |
| unpickle_pure_python | 218 us                                                                 | 217 us: 1.01x faster                                                      |
| xml_etree_generate   | 85.7 ms                                                                | 85.4 ms: 1.00x faster                                                     |
| xml_etree_process    | 59.2 ms                                                                | 59.6 ms: 1.01x slower                                                     |
| pickle_pure_python   | 320 us                                                                 | 326 us: 1.02x slower                                                      |
| tomli_loads          | 2.06 sec                                                               | 2.13 sec: 1.03x slower                                                    |
| Geometric mean       | (ref)                                                                  | 1.01x faster                                                              |

Benchmark hidden because not significant (2): json_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241104-linux-x86_64-python-bfc1d2504c183a9464e6-3.14.0a1+-bfc1d25 | bm-20241106-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-3c18fc8 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 7.07 ms                                                                | 6.78 ms: 1.04x faster                                                     |
| python_startup         | 12.7 ms                                                                | 12.3 ms: 1.03x faster                                                     |
| Geometric mean         | (ref)                                                                  | 1.04x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241104-linux-x86_64-python-bfc1d2504c183a9464e6-3.14.0a1+-bfc1d25 | bm-20241106-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-3c18fc8 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                                | 22.3 ms: 1.01x faster                                                     |
| mako            | 11.5 ms                                                                | 11.4 ms: 1.01x faster                                                     |
| django_template | 34.0 ms                                                                | 34.2 ms: 1.01x slower                                                     |
| genshi_xml      | 49.5 ms                                                                | 49.9 ms: 1.01x slower                                                     |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241104-linux-x86_64-python-bfc1d2504c183a9464e6-3.14.0a1+-bfc1d25 | bm-20241106-linux-x86_64-faster%2dcpython-mark_first_gc-3.14.0a1+-3c18fc8 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| gc_traversal               | 4.80 ms                                                                | 2.32 ms: 2.07x faster                                                     |
| async_tree_io_tg           | 962 ms                                                                 | 594 ms: 1.62x faster                                                      |
| create_gc_cycles           | 2.70 ms                                                                | 1.71 ms: 1.58x faster                                                     |
| k_core                     | 3.63 sec                                                               | 2.31 sec: 1.57x faster                                                    |
| async_tree_io              | 855 ms                                                                 | 608 ms: 1.41x faster                                                      |
| async_tree_none_tg         | 321 ms                                                                 | 247 ms: 1.30x faster                                                      |
| async_tree_none            | 326 ms                                                                 | 261 ms: 1.25x faster                                                      |
| async_tree_memoization     | 413 ms                                                                 | 334 ms: 1.23x faster                                                      |
| pylint                     | 319 ms                                                                 | 262 ms: 1.22x faster                                                      |
| async_tree_memoization_tg  | 375 ms                                                                 | 316 ms: 1.19x faster                                                      |
| async_tree_cpu_io_mixed_tg | 564 ms                                                                 | 480 ms: 1.17x faster                                                      |
| async_tree_cpu_io_mixed    | 577 ms                                                                 | 492 ms: 1.17x faster                                                      |
| xml_etree_parse            | 158 ms                                                                 | 145 ms: 1.09x faster                                                      |
| pycparser                  | 1.19 sec                                                               | 1.12 sec: 1.06x faster                                                    |
| python_startup_no_site     | 7.07 ms                                                                | 6.78 ms: 1.04x faster                                                     |
| xml_etree_iterparse        | 105 ms                                                                 | 101 ms: 1.03x faster                                                      |
| bpe_tokeniser              | 4.78 sec                                                               | 4.62 sec: 1.03x faster                                                    |
| sphinx                     | 1.05 sec                                                               | 1.02 sec: 1.03x faster                                                    |
| python_startup             | 12.7 ms                                                                | 12.3 ms: 1.03x faster                                                     |
| float                      | 80.3 ms                                                                | 78.4 ms: 1.02x faster                                                     |
| go                         | 121 ms                                                                 | 118 ms: 1.02x faster                                                      |
| docutils                   | 2.70 sec                                                               | 2.65 sec: 1.02x faster                                                    |
| pyflate                    | 476 ms                                                                 | 467 ms: 1.02x faster                                                      |
| typing_runtime_protocols   | 162 us                                                                 | 160 us: 1.02x faster                                                      |
| regex_v8                   | 25.3 ms                                                                | 24.8 ms: 1.02x faster                                                     |
| richards                   | 46.3 ms                                                                | 45.5 ms: 1.02x faster                                                     |
| coroutines                 | 23.4 ms                                                                | 23.0 ms: 1.01x faster                                                     |
| genshi_text                | 22.6 ms                                                                | 22.3 ms: 1.01x faster                                                     |
| deltablue                  | 3.35 ms                                                                | 3.31 ms: 1.01x faster                                                     |
| generators                 | 27.1 ms                                                                | 26.7 ms: 1.01x faster                                                     |
| json                       | 4.82 ms                                                                | 4.76 ms: 1.01x faster                                                     |
| mako                       | 11.5 ms                                                                | 11.4 ms: 1.01x faster                                                     |
| comprehensions             | 16.9 us                                                                | 16.8 us: 1.01x faster                                                     |
| telco                      | 8.07 ms                                                                | 8.00 ms: 1.01x faster                                                     |
| async_generators           | 431 ms                                                                 | 428 ms: 1.01x faster                                                      |
| sqlglot_parse              | 1.30 ms                                                                | 1.29 ms: 1.01x faster                                                     |
| unpickle_pure_python       | 218 us                                                                 | 217 us: 1.01x faster                                                      |
| fannkuch                   | 403 ms                                                                 | 401 ms: 1.01x faster                                                      |
| xml_etree_generate         | 85.7 ms                                                                | 85.4 ms: 1.00x faster                                                     |
| pidigits                   | 187 ms                                                                 | 187 ms: 1.00x faster                                                      |
| hexiom                     | 6.27 ms                                                                | 6.28 ms: 1.00x slower                                                     |
| sympy_integrate            | 19.8 ms                                                                | 19.9 ms: 1.00x slower                                                     |
| sympy_sum                  | 146 ms                                                                 | 147 ms: 1.00x slower                                                      |
| bench_thread_pool          | 837 us                                                                 | 841 us: 1.00x slower                                                      |
| django_template            | 34.0 ms                                                                | 34.2 ms: 1.01x slower                                                     |
| xml_etree_process          | 59.2 ms                                                                | 59.6 ms: 1.01x slower                                                     |
| sqlite_synth               | 2.82 us                                                                | 2.84 us: 1.01x slower                                                     |
| regex_compile              | 129 ms                                                                 | 130 ms: 1.01x slower                                                      |
| sympy_str                  | 267 ms                                                                 | 269 ms: 1.01x slower                                                      |
| genshi_xml                 | 49.5 ms                                                                | 49.9 ms: 1.01x slower                                                     |
| regex_dna                  | 215 ms                                                                 | 216 ms: 1.01x slower                                                      |
| deepcopy_reduce            | 2.70 us                                                                | 2.72 us: 1.01x slower                                                     |
| sqlalchemy_declarative     | 127 ms                                                                 | 128 ms: 1.01x slower                                                      |
| pprint_safe_repr           | 725 ms                                                                 | 731 ms: 1.01x slower                                                      |
| sqlglot_optimize           | 53.4 ms                                                                | 53.9 ms: 1.01x slower                                                     |
| meteor_contest             | 106 ms                                                                 | 107 ms: 1.01x slower                                                      |
| scimark_sparse_mat_mult    | 5.12 ms                                                                | 5.19 ms: 1.01x slower                                                     |
| html5lib                   | 64.0 ms                                                                | 64.8 ms: 1.01x slower                                                     |
| coverage                   | 85.0 ms                                                                | 86.1 ms: 1.01x slower                                                     |
| 2to3                       | 255 ms                                                                 | 258 ms: 1.01x slower                                                      |
| spectral_norm              | 115 ms                                                                 | 116 ms: 1.01x slower                                                      |
| logging_format             | 6.06 us                                                                | 6.15 us: 1.01x slower                                                     |
| crypto_pyaes               | 72.1 ms                                                                | 73.4 ms: 1.02x slower                                                     |
| pickle_pure_python         | 320 us                                                                 | 326 us: 1.02x slower                                                      |
| logging_silent             | 105 ns                                                                 | 107 ns: 1.02x slower                                                      |
| deepcopy                   | 262 us                                                                 | 267 us: 1.02x slower                                                      |
| scimark_fft                | 368 ms                                                                 | 375 ms: 1.02x slower                                                      |
| deepcopy_memo              | 30.6 us                                                                | 31.3 us: 1.02x slower                                                     |
| scimark_lu                 | 116 ms                                                                 | 119 ms: 1.02x slower                                                      |
| bench_mp_pool              | 78.4 ms                                                                | 80.2 ms: 1.02x slower                                                     |
| scimark_sor                | 126 ms                                                                 | 129 ms: 1.02x slower                                                      |
| nqueens                    | 79.0 ms                                                                | 80.8 ms: 1.02x slower                                                     |
| regex_effbot               | 3.65 ms                                                                | 3.75 ms: 1.03x slower                                                     |
| mdp                        | 2.49 sec                                                               | 2.57 sec: 1.03x slower                                                    |
| tomli_loads                | 2.06 sec                                                               | 2.13 sec: 1.03x slower                                                    |
| Geometric mean             | (ref)                                                                  | 1.04x faster                                                              |

Benchmark hidden because not significant (19): sqlalchemy_imperative, connected_components, scimark_monte_carlo, sympy_expand, shortest_path, json_loads, richards_super, dulwich_log, json_dumps, asyncio_websockets, raytrace, chaos, sqlglot_transpile, pathlib, sqlglot_normalize, pprint_pformat, thrift, nbody, logging_simple

- Geometric mean (including insignificant results): 1.046x faster
# HPT report

- Reliability score: 96.28% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x