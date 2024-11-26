# Results vs. base

- fork: faster-cpython
- ref: load_fast_can_be_def
- machine: linux-x86_64
- commit hash: cb9433d
- commit date: 2024-10-04
- overall geometric mean: 1.009x slower
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241003-linux-x86_64-python-1f9025a4e7819bb4f779-3.14.0a0-1f9025a | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 254 ms                                                                | 257 ms: 1.01x slower                                                            |
| docutils       | 2.63 sec                                                              | 2.64 sec: 1.00x slower                                                          |
| html5lib       | 61.2 ms                                                               | 62.2 ms: 1.02x slower                                                           |
| tornado_http   | 90.2 ms                                                               | 91.7 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241003-linux-x86_64-python-1f9025a4e7819bb4f779-3.14.0a0-1f9025a | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| coroutines                 | 23.7 ms                                                               | 22.4 ms: 1.06x faster                                                           |
| asyncio_tcp                | 479 ms                                                                | 469 ms: 1.02x faster                                                            |
| async_generators           | 439 ms                                                                | 433 ms: 1.01x faster                                                            |
| async_tree_cpu_io_mixed_tg | 556 ms                                                                | 550 ms: 1.01x faster                                                            |
| asyncio_tcp_ssl            | 1.78 sec                                                              | 1.77 sec: 1.00x faster                                                          |
| Geometric mean             | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (8): async_tree_io_tg, async_tree_io, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_memoization, async_tree_memoization_tg, asyncio_websockets, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241003-linux-x86_64-python-1f9025a4e7819bb4f779-3.14.0a0-1f9025a | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                | 187 ms: 1.00x slower                                                            |
| float          | 76.3 ms                                                               | 77.1 ms: 1.01x slower                                                           |
| nbody          | 85.8 ms                                                               | 88.0 ms: 1.03x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241003-linux-x86_64-python-1f9025a4e7819bb4f779-3.14.0a0-1f9025a | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 224 ms                                                                | 223 ms: 1.01x faster                                                            |
| regex_effbot   | 3.76 ms                                                               | 3.75 ms: 1.00x faster                                                           |
| regex_v8       | 24.8 ms                                                               | 25.3 ms: 1.02x slower                                                           |
| regex_compile  | 128 ms                                                                | 131 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241003-linux-x86_64-python-1f9025a4e7819bb4f779-3.14.0a0-1f9025a | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| json_dumps           | 10.3 ms                                                               | 10.2 ms: 1.02x faster                                                           |
| xml_etree_process    | 59.1 ms                                                               | 59.3 ms: 1.00x slower                                                           |
| json_loads           | 26.9 us                                                               | 27.1 us: 1.01x slower                                                           |
| tomli_loads          | 2.08 sec                                                              | 2.10 sec: 1.01x slower                                                          |
| pickle_dict          | 33.8 us                                                               | 34.1 us: 1.01x slower                                                           |
| unpickle_list        | 5.25 us                                                               | 5.32 us: 1.01x slower                                                           |
| unpickle_pure_python | 212 us                                                                | 216 us: 1.02x slower                                                            |
| pickle_pure_python   | 301 us                                                                | 308 us: 1.02x slower                                                            |
| pickle_list          | 4.87 us                                                               | 5.06 us: 1.04x slower                                                           |
| pickle               | 11.2 us                                                               | 11.7 us: 1.05x slower                                                           |
| Geometric mean       | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (4): xml_etree_parse, unpickle, xml_etree_iterparse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241003-linux-x86_64-python-1f9025a4e7819bb4f779-3.14.0a0-1f9025a | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                                           |
| python_startup_no_site | 7.02 ms                                                               | 6.99 ms: 1.00x faster                                                           |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241003-linux-x86_64-python-1f9025a4e7819bb4f779-3.14.0a0-1f9025a | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 51.2 ms                                                               | 50.5 ms: 1.01x faster                                                           |
| django_template | 34.1 ms                                                               | 34.5 ms: 1.01x slower                                                           |
| mako            | 11.2 ms                                                               | 11.3 ms: 1.01x slower                                                           |
| genshi_text     | 22.2 ms                                                               | 22.7 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                                    |

All benchmarks:
===============

| Benchmark                  | bm-20241003-linux-x86_64-python-1f9025a4e7819bb4f779-3.14.0a0-1f9025a | bm-20241004-linux-x86_64-faster%2dcpython-load_fast_can_be_def-3.14.0a0-cb9433d |
|----------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| gc_traversal               | 3.97 ms                                                               | 3.72 ms: 1.07x faster                                                           |
| coroutines                 | 23.7 ms                                                               | 22.4 ms: 1.06x faster                                                           |
| asyncio_tcp                | 479 ms                                                                | 469 ms: 1.02x faster                                                            |
| json_dumps                 | 10.3 ms                                                               | 10.2 ms: 1.02x faster                                                           |
| genshi_xml                 | 51.2 ms                                                               | 50.5 ms: 1.01x faster                                                           |
| async_generators           | 439 ms                                                                | 433 ms: 1.01x faster                                                            |
| async_tree_cpu_io_mixed_tg | 556 ms                                                                | 550 ms: 1.01x faster                                                            |
| create_gc_cycles           | 1.73 ms                                                               | 1.71 ms: 1.01x faster                                                           |
| crypto_pyaes               | 72.9 ms                                                               | 72.3 ms: 1.01x faster                                                           |
| thrift                     | 769 us                                                                | 763 us: 1.01x faster                                                            |
| regex_dna                  | 224 ms                                                                | 223 ms: 1.01x faster                                                            |
| python_startup             | 10.6 ms                                                               | 10.5 ms: 1.01x faster                                                           |
| fannkuch                   | 405 ms                                                                | 403 ms: 1.00x faster                                                            |
| sqlglot_parse              | 1.29 ms                                                               | 1.28 ms: 1.00x faster                                                           |
| python_startup_no_site     | 7.02 ms                                                               | 6.99 ms: 1.00x faster                                                           |
| bench_thread_pool          | 854 us                                                                | 850 us: 1.00x faster                                                            |
| regex_effbot               | 3.76 ms                                                               | 3.75 ms: 1.00x faster                                                           |
| asyncio_tcp_ssl            | 1.78 sec                                                              | 1.77 sec: 1.00x faster                                                          |
| sqlglot_transpile          | 1.58 ms                                                               | 1.58 ms: 1.00x faster                                                           |
| pidigits                   | 187 ms                                                                | 187 ms: 1.00x slower                                                            |
| xml_etree_process          | 59.1 ms                                                               | 59.3 ms: 1.00x slower                                                           |
| docutils                   | 2.63 sec                                                              | 2.64 sec: 1.00x slower                                                          |
| pprint_safe_repr           | 712 ms                                                                | 716 ms: 1.01x slower                                                            |
| deepcopy_reduce            | 2.73 us                                                               | 2.75 us: 1.01x slower                                                           |
| scimark_lu                 | 113 ms                                                                | 114 ms: 1.01x slower                                                            |
| generators                 | 27.6 ms                                                               | 27.8 ms: 1.01x slower                                                           |
| json_loads                 | 26.9 us                                                               | 27.1 us: 1.01x slower                                                           |
| tomli_loads                | 2.08 sec                                                              | 2.10 sec: 1.01x slower                                                          |
| sympy_sum                  | 147 ms                                                                | 148 ms: 1.01x slower                                                            |
| pyflate                    | 473 ms                                                                | 477 ms: 1.01x slower                                                            |
| deepcopy_memo              | 30.0 us                                                               | 30.3 us: 1.01x slower                                                           |
| django_template            | 34.1 ms                                                               | 34.5 ms: 1.01x slower                                                           |
| pickle_dict                | 33.8 us                                                               | 34.1 us: 1.01x slower                                                           |
| float                      | 76.3 ms                                                               | 77.1 ms: 1.01x slower                                                           |
| sympy_expand               | 455 ms                                                                | 460 ms: 1.01x slower                                                            |
| pprint_pformat             | 1.46 sec                                                              | 1.48 sec: 1.01x slower                                                          |
| dulwich_log                | 64.7 ms                                                               | 65.5 ms: 1.01x slower                                                           |
| comprehensions             | 16.4 us                                                               | 16.6 us: 1.01x slower                                                           |
| 2to3                       | 254 ms                                                                | 257 ms: 1.01x slower                                                            |
| mako                       | 11.2 ms                                                               | 11.3 ms: 1.01x slower                                                           |
| sympy_str                  | 267 ms                                                                | 271 ms: 1.01x slower                                                            |
| unpickle_list              | 5.25 us                                                               | 5.32 us: 1.01x slower                                                           |
| raytrace                   | 264 ms                                                                | 267 ms: 1.01x slower                                                            |
| richards_super             | 52.5 ms                                                               | 53.2 ms: 1.01x slower                                                           |
| sqlglot_optimize           | 52.9 ms                                                               | 53.6 ms: 1.01x slower                                                           |
| sympy_integrate            | 19.7 ms                                                               | 20.0 ms: 1.02x slower                                                           |
| tornado_http               | 90.2 ms                                                               | 91.7 ms: 1.02x slower                                                           |
| html5lib                   | 61.2 ms                                                               | 62.2 ms: 1.02x slower                                                           |
| pycparser                  | 1.14 sec                                                              | 1.16 sec: 1.02x slower                                                          |
| unpickle_pure_python       | 212 us                                                                | 216 us: 1.02x slower                                                            |
| regex_v8                   | 24.8 ms                                                               | 25.3 ms: 1.02x slower                                                           |
| genshi_text                | 22.2 ms                                                               | 22.7 ms: 1.02x slower                                                           |
| sqlglot_normalize          | 106 ms                                                                | 108 ms: 1.02x slower                                                            |
| richards                   | 46.0 ms                                                               | 46.9 ms: 1.02x slower                                                           |
| bpe_tokeniser              | 4.74 sec                                                              | 4.83 sec: 1.02x slower                                                          |
| pickle_pure_python         | 301 us                                                                | 308 us: 1.02x slower                                                            |
| scimark_monte_carlo        | 66.7 ms                                                               | 68.3 ms: 1.02x slower                                                           |
| logging_silent             | 101 ns                                                                | 104 ns: 1.02x slower                                                            |
| scimark_fft                | 360 ms                                                                | 368 ms: 1.02x slower                                                            |
| typing_runtime_protocols   | 159 us                                                                | 163 us: 1.03x slower                                                            |
| nbody                      | 85.8 ms                                                               | 88.0 ms: 1.03x slower                                                           |
| regex_compile              | 128 ms                                                                | 131 ms: 1.03x slower                                                            |
| scimark_sor                | 124 ms                                                                | 127 ms: 1.03x slower                                                            |
| hexiom                     | 6.11 ms                                                               | 6.29 ms: 1.03x slower                                                           |
| spectral_norm              | 111 ms                                                                | 115 ms: 1.03x slower                                                            |
| go                         | 116 ms                                                                | 120 ms: 1.03x slower                                                            |
| logging_format             | 6.10 us                                                               | 6.30 us: 1.03x slower                                                           |
| logging_simple             | 5.49 us                                                               | 5.69 us: 1.04x slower                                                           |
| meteor_contest             | 107 ms                                                                | 111 ms: 1.04x slower                                                            |
| pickle_list                | 4.87 us                                                               | 5.06 us: 1.04x slower                                                           |
| deltablue                  | 3.14 ms                                                               | 3.28 ms: 1.04x slower                                                           |
| pickle                     | 11.2 us                                                               | 11.7 us: 1.05x slower                                                           |
| chaos                      | 59.0 ms                                                               | 61.7 ms: 1.05x slower                                                           |
| nqueens                    | 77.8 ms                                                               | 81.5 ms: 1.05x slower                                                           |
| scimark_sparse_mat_mult    | 4.70 ms                                                               | 5.08 ms: 1.08x slower                                                           |
| unpack_sequence            | 47.2 ns                                                               | 50.9 ns: 1.08x slower                                                           |
| Geometric mean             | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (21): async_tree_io_tg, async_tree_io, async_tree_none_tg, async_tree_cpu_io_mixed, xml_etree_parse, coverage, async_tree_memoization, async_tree_memoization_tg, deepcopy, asyncio_websockets, async_tree_none, telco, mdp, bench_mp_pool, unpickle, json, xml_etree_iterparse, pathlib, xml_etree_generate, sqlite_synth, pylint

- Geometric mean (including insignificant results): 1.009x slower
# HPT report

- Reliability score: 99.98% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x