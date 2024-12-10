# Results vs. base

- fork: faster-cpython
- ref: use_stackrefs
- machine: linux-x86_64
- commit hash: 1069d98
- commit date: 2024-12-10
- overall geometric mean: 1.008x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241210-linux-x86_64-python-cef0a90d8f3a94aa5345-3.14.0a2+-cef0a90 | bm-20241210-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-1069d98 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 256 ms                                                                 | 257 ms: 1.00x slower                                                      |
| docutils       | 2.58 sec                                                               | 2.64 sec: 1.02x slower                                                    |
| html5lib       | 61.9 ms                                                                | 63.1 ms: 1.02x slower                                                     |
| sphinx         | 1.01 sec                                                               | 1.03 sec: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241210-linux-x86_64-python-cef0a90d8f3a94aa5345-3.14.0a2+-cef0a90 | bm-20241210-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-1069d98 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 488 ms                                                                 | 482 ms: 1.01x faster                                                      |
| async_tree_memoization_tg  | 315 ms                                                                 | 318 ms: 1.01x slower                                                      |
| coroutines                 | 23.7 ms                                                                | 23.9 ms: 1.01x slower                                                     |
| async_tree_none            | 271 ms                                                                 | 275 ms: 1.01x slower                                                      |
| async_tree_memoization     | 340 ms                                                                 | 345 ms: 1.01x slower                                                      |
| async_tree_none_tg         | 255 ms                                                                 | 258 ms: 1.01x slower                                                      |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (5): async_tree_cpu_io_mixed, asyncio_websockets, async_generators, async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241210-linux-x86_64-python-cef0a90d8f3a94aa5345-3.14.0a2+-cef0a90 | bm-20241210-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-1069d98 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 186 ms                                                                 | 189 ms: 1.01x slower                                                      |
| float          | 77.9 ms                                                                | 79.3 ms: 1.02x slower                                                     |
| nbody          | 96.3 ms                                                                | 99.3 ms: 1.03x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241210-linux-x86_64-python-cef0a90d8f3a94aa5345-3.14.0a2+-cef0a90 | bm-20241210-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-1069d98 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                                 | 128 ms: 1.01x faster                                                      |
| regex_dna      | 221 ms                                                                 | 226 ms: 1.02x slower                                                      |
| regex_effbot   | 3.23 ms                                                                | 3.40 ms: 1.05x slower                                                     |
| regex_v8       | 25.3 ms                                                                | 26.9 ms: 1.07x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.03x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241210-linux-x86_64-python-cef0a90d8f3a94aa5345-3.14.0a2+-cef0a90 | bm-20241210-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-1069d98 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_pure_python | 219 us                                                                 | 217 us: 1.01x faster                                                      |
| xml_etree_parse      | 139 ms                                                                 | 138 ms: 1.01x faster                                                      |
| json_loads           | 26.6 us                                                                | 26.7 us: 1.01x slower                                                     |
| xml_etree_process    | 59.1 ms                                                                | 59.5 ms: 1.01x slower                                                     |
| xml_etree_iterparse  | 97.9 ms                                                                | 98.6 ms: 1.01x slower                                                     |
| pickle_pure_python   | 323 us                                                                 | 326 us: 1.01x slower                                                      |
| json_dumps           | 11.3 ms                                                                | 11.5 ms: 1.01x slower                                                     |
| xml_etree_generate   | 84.6 ms                                                                | 85.8 ms: 1.01x slower                                                     |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (1): tomli_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241210-linux-x86_64-python-cef0a90d8f3a94aa5345-3.14.0a2+-cef0a90 | bm-20241210-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-1069d98 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 7.03 ms                                                                | 7.02 ms: 1.00x faster                                                     |
| python_startup         | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                                     |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241210-linux-x86_64-python-cef0a90d8f3a94aa5345-3.14.0a2+-cef0a90 | bm-20241210-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-1069d98 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 22.6 ms                                                                | 22.2 ms: 1.02x faster                                                     |
| genshi_xml      | 50.0 ms                                                                | 51.1 ms: 1.02x slower                                                     |
| django_template | 31.8 ms                                                                | 32.6 ms: 1.02x slower                                                     |
| mako            | 11.5 ms                                                                | 11.9 ms: 1.04x slower                                                     |
| Geometric mean  | (ref)                                                                  | 1.02x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241210-linux-x86_64-python-cef0a90d8f3a94aa5345-3.14.0a2+-cef0a90 | bm-20241210-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a2+-1069d98 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| logging_silent             | 107 ns                                                                 | 101 ns: 1.06x faster                                                      |
| scimark_sparse_mat_mult    | 5.17 ms                                                                | 5.00 ms: 1.03x faster                                                     |
| scimark_fft                | 380 ms                                                                 | 368 ms: 1.03x faster                                                      |
| coverage                   | 85.2 ms                                                                | 83.1 ms: 1.03x faster                                                     |
| hexiom                     | 6.34 ms                                                                | 6.18 ms: 1.02x faster                                                     |
| genshi_text                | 22.6 ms                                                                | 22.2 ms: 1.02x faster                                                     |
| raytrace                   | 275 ms                                                                 | 271 ms: 1.02x faster                                                      |
| spectral_norm              | 117 ms                                                                 | 116 ms: 1.01x faster                                                      |
| richards                   | 46.7 ms                                                                | 46.0 ms: 1.01x faster                                                     |
| scimark_lu                 | 119 ms                                                                 | 117 ms: 1.01x faster                                                      |
| shortest_path              | 481 ms                                                                 | 475 ms: 1.01x faster                                                      |
| async_tree_cpu_io_mixed_tg | 488 ms                                                                 | 482 ms: 1.01x faster                                                      |
| logging_format             | 6.19 us                                                                | 6.13 us: 1.01x faster                                                     |
| richards_super             | 53.2 ms                                                                | 52.7 ms: 1.01x faster                                                     |
| go                         | 119 ms                                                                 | 117 ms: 1.01x faster                                                      |
| unpickle_pure_python       | 219 us                                                                 | 217 us: 1.01x faster                                                      |
| connected_components       | 437 ms                                                                 | 433 ms: 1.01x faster                                                      |
| crypto_pyaes               | 73.0 ms                                                                | 72.5 ms: 1.01x faster                                                     |
| regex_compile              | 129 ms                                                                 | 128 ms: 1.01x faster                                                      |
| xml_etree_parse            | 139 ms                                                                 | 138 ms: 1.01x faster                                                      |
| python_startup_no_site     | 7.03 ms                                                                | 7.02 ms: 1.00x faster                                                     |
| python_startup             | 12.8 ms                                                                | 12.8 ms: 1.00x slower                                                     |
| 2to3                       | 256 ms                                                                 | 257 ms: 1.00x slower                                                      |
| dulwich_log                | 65.3 ms                                                                | 65.5 ms: 1.00x slower                                                     |
| sqlglot_transpile          | 1.60 ms                                                                | 1.61 ms: 1.00x slower                                                     |
| sqlglot_optimize           | 53.5 ms                                                                | 53.8 ms: 1.00x slower                                                     |
| json_loads                 | 26.6 us                                                                | 26.7 us: 1.01x slower                                                     |
| sqlglot_parse              | 1.29 ms                                                                | 1.30 ms: 1.01x slower                                                     |
| xml_etree_process          | 59.1 ms                                                                | 59.5 ms: 1.01x slower                                                     |
| sympy_integrate            | 19.9 ms                                                                | 20.1 ms: 1.01x slower                                                     |
| logging_simple             | 5.54 us                                                                | 5.58 us: 1.01x slower                                                     |
| xml_etree_iterparse        | 97.9 ms                                                                | 98.6 ms: 1.01x slower                                                     |
| deltablue                  | 3.25 ms                                                                | 3.27 ms: 1.01x slower                                                     |
| scimark_sor                | 127 ms                                                                 | 128 ms: 1.01x slower                                                      |
| sympy_sum                  | 148 ms                                                                 | 149 ms: 1.01x slower                                                      |
| async_tree_memoization_tg  | 315 ms                                                                 | 318 ms: 1.01x slower                                                      |
| pickle_pure_python         | 323 us                                                                 | 326 us: 1.01x slower                                                      |
| coroutines                 | 23.7 ms                                                                | 23.9 ms: 1.01x slower                                                     |
| json_dumps                 | 11.3 ms                                                                | 11.5 ms: 1.01x slower                                                     |
| json                       | 5.02 ms                                                                | 5.07 ms: 1.01x slower                                                     |
| bench_thread_pool          | 854 us                                                                 | 863 us: 1.01x slower                                                      |
| meteor_contest             | 107 ms                                                                 | 108 ms: 1.01x slower                                                      |
| pidigits                   | 186 ms                                                                 | 189 ms: 1.01x slower                                                      |
| async_tree_none            | 271 ms                                                                 | 275 ms: 1.01x slower                                                      |
| sympy_str                  | 269 ms                                                                 | 272 ms: 1.01x slower                                                      |
| thrift                     | 772 us                                                                 | 782 us: 1.01x slower                                                      |
| async_tree_memoization     | 340 ms                                                                 | 345 ms: 1.01x slower                                                      |
| chaos                      | 61.1 ms                                                                | 62.0 ms: 1.01x slower                                                     |
| sqlalchemy_imperative      | 16.3 ms                                                                | 16.5 ms: 1.01x slower                                                     |
| xml_etree_generate         | 84.6 ms                                                                | 85.8 ms: 1.01x slower                                                     |
| async_tree_none_tg         | 255 ms                                                                 | 258 ms: 1.01x slower                                                      |
| bpe_tokeniser              | 4.52 sec                                                               | 4.59 sec: 1.02x slower                                                    |
| sphinx                     | 1.01 sec                                                               | 1.03 sec: 1.02x slower                                                    |
| float                      | 77.9 ms                                                                | 79.3 ms: 1.02x slower                                                     |
| typing_runtime_protocols   | 161 us                                                                 | 164 us: 1.02x slower                                                      |
| sqlalchemy_declarative     | 127 ms                                                                 | 130 ms: 1.02x slower                                                      |
| html5lib                   | 61.9 ms                                                                | 63.1 ms: 1.02x slower                                                     |
| generators                 | 27.6 ms                                                                | 28.1 ms: 1.02x slower                                                     |
| sqlite_synth               | 2.87 us                                                                | 2.92 us: 1.02x slower                                                     |
| docutils                   | 2.58 sec                                                               | 2.64 sec: 1.02x slower                                                    |
| sympy_expand               | 456 ms                                                                 | 465 ms: 1.02x slower                                                      |
| genshi_xml                 | 50.0 ms                                                                | 51.1 ms: 1.02x slower                                                     |
| pprint_safe_repr           | 733 ms                                                                 | 750 ms: 1.02x slower                                                      |
| regex_dna                  | 221 ms                                                                 | 226 ms: 1.02x slower                                                      |
| django_template            | 31.8 ms                                                                | 32.6 ms: 1.02x slower                                                     |
| many_optionals             | 943 us                                                                 | 967 us: 1.03x slower                                                      |
| subparsers                 | 21.0 ms                                                                | 21.5 ms: 1.03x slower                                                     |
| pathlib                    | 16.1 ms                                                                | 16.6 ms: 1.03x slower                                                     |
| comprehensions             | 16.9 us                                                                | 17.4 us: 1.03x slower                                                     |
| nbody                      | 96.3 ms                                                                | 99.3 ms: 1.03x slower                                                     |
| deepcopy_reduce            | 2.64 us                                                                | 2.72 us: 1.03x slower                                                     |
| pprint_pformat             | 1.50 sec                                                               | 1.55 sec: 1.03x slower                                                    |
| nqueens                    | 81.8 ms                                                                | 84.6 ms: 1.03x slower                                                     |
| mako                       | 11.5 ms                                                                | 11.9 ms: 1.04x slower                                                     |
| fannkuch                   | 408 ms                                                                 | 424 ms: 1.04x slower                                                      |
| pyflate                    | 463 ms                                                                 | 481 ms: 1.04x slower                                                      |
| regex_effbot               | 3.23 ms                                                                | 3.40 ms: 1.05x slower                                                     |
| mdp                        | 2.56 sec                                                               | 2.71 sec: 1.06x slower                                                    |
| regex_v8                   | 25.3 ms                                                                | 26.9 ms: 1.07x slower                                                     |
| gc_traversal               | 4.70 ms                                                                | 5.03 ms: 1.07x slower                                                     |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (18): deepcopy_memo, async_tree_cpu_io_mixed, deepcopy, tomli_loads, asyncio_websockets, bench_mp_pool, scimark_monte_carlo, create_gc_cycles, sqlglot_normalize, async_generators, k_core, telco, djangocms, pycparser, async_tree_io, mypy2, pylint, async_tree_io_tg

- Geometric mean (including insignificant results): 1.008x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x