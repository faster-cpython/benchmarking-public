# Results vs. base

- fork: faster-cpython
- ref: variable_offset_inli
- machine: linux-x86_64
- commit hash: a3e6464
- commit date: 2024-08-20
- overall geometric mean: 1.00x slower
- HPT reliability: 75.35%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240820-pythonperf2-x86_64-python-bb1d30336e83837d4191-3.14.0a0-bb1d303 | bm-20240820-pythonperf2-x86_64-faster%2dcpython-variable_offset_inli-3.14.0a0-a3e6464 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 285 ms                                                                      | 288 ms: 1.01x slower                                                                  |
| docutils       | 2.98 sec                                                                    | 2.94 sec: 1.01x faster                                                                |
| tornado_http   | 116 ms                                                                      | 118 ms: 1.02x slower                                                                  |
| Geometric mean | (ref)                                                                       | 1.00x slower                                                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20240820-pythonperf2-x86_64-python-bb1d30336e83837d4191-3.14.0a0-bb1d303 | bm-20240820-pythonperf2-x86_64-faster%2dcpython-variable_offset_inli-3.14.0a0-a3e6464 |
|----------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_tree_none            | 334 ms                                                                      | 320 ms: 1.04x faster                                                                  |
| coroutines                 | 22.0 ms                                                                     | 21.4 ms: 1.03x faster                                                                 |
| asyncio_websockets         | 394 ms                                                                      | 384 ms: 1.03x faster                                                                  |
| asyncio_tcp                | 375 ms                                                                      | 368 ms: 1.02x faster                                                                  |
| async_tree_memoization_tg  | 384 ms                                                                      | 393 ms: 1.02x slower                                                                  |
| async_tree_cpu_io_mixed_tg | 539 ms                                                                      | 552 ms: 1.02x slower                                                                  |
| async_tree_io_tg           | 764 ms                                                                      | 787 ms: 1.03x slower                                                                  |
| async_generators           | 357 ms                                                                      | 368 ms: 1.03x slower                                                                  |
| Geometric mean             | (ref)                                                                       | 1.00x slower                                                                          |

Benchmark hidden because not significant (5): async_tree_memoization, async_tree_io, asyncio_tcp_ssl, async_tree_cpu_io_mixed, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240820-pythonperf2-x86_64-python-bb1d30336e83837d4191-3.14.0a0-bb1d303 | bm-20240820-pythonperf2-x86_64-faster%2dcpython-variable_offset_inli-3.14.0a0-a3e6464 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| float          | 79.4 ms                                                                     | 79.7 ms: 1.00x slower                                                                 |
| pidigits       | 253 ms                                                                      | 256 ms: 1.01x slower                                                                  |
| nbody          | 86.3 ms                                                                     | 87.7 ms: 1.02x slower                                                                 |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240820-pythonperf2-x86_64-python-bb1d30336e83837d4191-3.14.0a0-bb1d303 | bm-20240820-pythonperf2-x86_64-faster%2dcpython-variable_offset_inli-3.14.0a0-a3e6464 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_effbot   | 3.61 ms                                                                     | 3.52 ms: 1.03x faster                                                                 |
| regex_v8       | 26.0 ms                                                                     | 27.6 ms: 1.06x slower                                                                 |
| regex_dna      | 239 ms                                                                      | 255 ms: 1.07x slower                                                                  |
| Geometric mean | (ref)                                                                       | 1.03x slower                                                                          |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240820-pythonperf2-x86_64-python-bb1d30336e83837d4191-3.14.0a0-bb1d303 | bm-20240820-pythonperf2-x86_64-faster%2dcpython-variable_offset_inli-3.14.0a0-a3e6464 |
|----------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| tomli_loads          | 2.27 sec                                                                    | 2.24 sec: 1.02x faster                                                                |
| xml_etree_process    | 58.9 ms                                                                     | 58.4 ms: 1.01x faster                                                                 |
| json_loads           | 25.1 us                                                                     | 25.0 us: 1.01x faster                                                                 |
| xml_etree_parse      | 142 ms                                                                      | 144 ms: 1.01x slower                                                                  |
| json_dumps           | 10.5 ms                                                                     | 10.7 ms: 1.01x slower                                                                 |
| xml_etree_iterparse  | 100 ms                                                                      | 103 ms: 1.02x slower                                                                  |
| unpickle_pure_python | 213 us                                                                      | 218 us: 1.03x slower                                                                  |
| Geometric mean       | (ref)                                                                       | 1.00x slower                                                                          |

Benchmark hidden because not significant (2): xml_etree_generate, pickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240820-pythonperf2-x86_64-python-bb1d30336e83837d4191-3.14.0a0-bb1d303 | bm-20240820-pythonperf2-x86_64-faster%2dcpython-variable_offset_inli-3.14.0a0-a3e6464 |
|-----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| django_template | 40.2 ms                                                                     | 39.4 ms: 1.02x faster                                                                 |
| mako            | 10.6 ms                                                                     | 10.4 ms: 1.01x faster                                                                 |
| genshi_xml      | 54.6 ms                                                                     | 54.9 ms: 1.01x slower                                                                 |
| genshi_text     | 25.2 ms                                                                     | 25.9 ms: 1.03x slower                                                                 |
| Geometric mean  | (ref)                                                                       | 1.00x faster                                                                          |

All benchmarks:
===============

| Benchmark                  | bm-20240820-pythonperf2-x86_64-python-bb1d30336e83837d4191-3.14.0a0-bb1d303 | bm-20240820-pythonperf2-x86_64-faster%2dcpython-variable_offset_inli-3.14.0a0-a3e6464 |
|----------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| coverage                   | 83.6 ms                                                                     | 78.4 ms: 1.07x faster                                                                 |
| async_tree_none            | 334 ms                                                                      | 320 ms: 1.04x faster                                                                  |
| deepcopy_memo              | 30.3 us                                                                     | 29.2 us: 1.04x faster                                                                 |
| coroutines                 | 22.0 ms                                                                     | 21.4 ms: 1.03x faster                                                                 |
| asyncio_websockets         | 394 ms                                                                      | 384 ms: 1.03x faster                                                                  |
| pycparser                  | 1.26 sec                                                                    | 1.23 sec: 1.03x faster                                                                |
| regex_effbot               | 3.61 ms                                                                     | 3.52 ms: 1.03x faster                                                                 |
| mdp                        | 2.55 sec                                                                    | 2.49 sec: 1.02x faster                                                                |
| sympy_str                  | 296 ms                                                                      | 290 ms: 1.02x faster                                                                  |
| nqueens                    | 90.5 ms                                                                     | 88.6 ms: 1.02x faster                                                                 |
| django_template            | 40.2 ms                                                                     | 39.4 ms: 1.02x faster                                                                 |
| typing_runtime_protocols   | 176 us                                                                      | 173 us: 1.02x faster                                                                  |
| asyncio_tcp                | 375 ms                                                                      | 368 ms: 1.02x faster                                                                  |
| scimark_fft                | 307 ms                                                                      | 301 ms: 1.02x faster                                                                  |
| meteor_contest             | 128 ms                                                                      | 126 ms: 1.02x faster                                                                  |
| sympy_integrate            | 23.3 ms                                                                     | 22.9 ms: 1.02x faster                                                                 |
| tomli_loads                | 2.27 sec                                                                    | 2.24 sec: 1.02x faster                                                                |
| fannkuch                   | 359 ms                                                                      | 353 ms: 1.01x faster                                                                  |
| mako                       | 10.6 ms                                                                     | 10.4 ms: 1.01x faster                                                                 |
| sympy_expand               | 505 ms                                                                      | 497 ms: 1.01x faster                                                                  |
| docutils                   | 2.98 sec                                                                    | 2.94 sec: 1.01x faster                                                                |
| xml_etree_process          | 58.9 ms                                                                     | 58.4 ms: 1.01x faster                                                                 |
| sqlglot_normalize          | 120 ms                                                                      | 119 ms: 1.01x faster                                                                  |
| sympy_sum                  | 153 ms                                                                      | 152 ms: 1.01x faster                                                                  |
| sqlglot_optimize           | 58.9 ms                                                                     | 58.4 ms: 1.01x faster                                                                 |
| sqlglot_parse              | 1.40 ms                                                                     | 1.39 ms: 1.01x faster                                                                 |
| sqlglot_transpile          | 1.77 ms                                                                     | 1.76 ms: 1.01x faster                                                                 |
| json_loads                 | 25.1 us                                                                     | 25.0 us: 1.01x faster                                                                 |
| spectral_norm              | 96.6 ms                                                                     | 96.1 ms: 1.01x faster                                                                 |
| deepcopy                   | 287 us                                                                      | 286 us: 1.00x faster                                                                  |
| bpe_tokeniser              | 4.90 sec                                                                    | 4.92 sec: 1.00x slower                                                                |
| float                      | 79.4 ms                                                                     | 79.7 ms: 1.00x slower                                                                 |
| pathlib                    | 15.9 ms                                                                     | 16.0 ms: 1.00x slower                                                                 |
| scimark_sparse_mat_mult    | 4.26 ms                                                                     | 4.28 ms: 1.01x slower                                                                 |
| genshi_xml                 | 54.6 ms                                                                     | 54.9 ms: 1.01x slower                                                                 |
| scimark_lu                 | 94.8 ms                                                                     | 95.3 ms: 1.01x slower                                                                 |
| richards_super             | 56.2 ms                                                                     | 56.5 ms: 1.01x slower                                                                 |
| thrift                     | 859 us                                                                      | 864 us: 1.01x slower                                                                  |
| richards                   | 49.8 ms                                                                     | 50.1 ms: 1.01x slower                                                                 |
| xml_etree_parse            | 142 ms                                                                      | 144 ms: 1.01x slower                                                                  |
| crypto_pyaes               | 72.9 ms                                                                     | 73.6 ms: 1.01x slower                                                                 |
| pidigits                   | 253 ms                                                                      | 256 ms: 1.01x slower                                                                  |
| pprint_pformat             | 1.68 sec                                                                    | 1.70 sec: 1.01x slower                                                                |
| json_dumps                 | 10.5 ms                                                                     | 10.7 ms: 1.01x slower                                                                 |
| 2to3                       | 285 ms                                                                      | 288 ms: 1.01x slower                                                                  |
| pprint_safe_repr           | 821 ms                                                                      | 834 ms: 1.02x slower                                                                  |
| deepcopy_reduce            | 2.86 us                                                                     | 2.91 us: 1.02x slower                                                                 |
| generators                 | 29.7 ms                                                                     | 30.2 ms: 1.02x slower                                                                 |
| tornado_http               | 116 ms                                                                      | 118 ms: 1.02x slower                                                                  |
| logging_format             | 6.83 us                                                                     | 6.95 us: 1.02x slower                                                                 |
| nbody                      | 86.3 ms                                                                     | 87.7 ms: 1.02x slower                                                                 |
| logging_simple             | 6.33 us                                                                     | 6.44 us: 1.02x slower                                                                 |
| go                         | 157 ms                                                                      | 160 ms: 1.02x slower                                                                  |
| hexiom                     | 6.21 ms                                                                     | 6.34 ms: 1.02x slower                                                                 |
| gc_traversal               | 4.49 ms                                                                     | 4.58 ms: 1.02x slower                                                                 |
| pyflate                    | 476 ms                                                                      | 487 ms: 1.02x slower                                                                  |
| async_tree_memoization_tg  | 384 ms                                                                      | 393 ms: 1.02x slower                                                                  |
| xml_etree_iterparse        | 100 ms                                                                      | 103 ms: 1.02x slower                                                                  |
| async_tree_cpu_io_mixed_tg | 539 ms                                                                      | 552 ms: 1.02x slower                                                                  |
| unpickle_pure_python       | 213 us                                                                      | 218 us: 1.03x slower                                                                  |
| genshi_text                | 25.2 ms                                                                     | 25.9 ms: 1.03x slower                                                                 |
| create_gc_cycles           | 1.99 ms                                                                     | 2.05 ms: 1.03x slower                                                                 |
| async_tree_io_tg           | 764 ms                                                                      | 787 ms: 1.03x slower                                                                  |
| async_generators           | 357 ms                                                                      | 368 ms: 1.03x slower                                                                  |
| deltablue                  | 3.34 ms                                                                     | 3.46 ms: 1.03x slower                                                                 |
| chaos                      | 61.5 ms                                                                     | 63.8 ms: 1.04x slower                                                                 |
| scimark_monte_carlo        | 65.5 ms                                                                     | 68.2 ms: 1.04x slower                                                                 |
| regex_v8                   | 26.0 ms                                                                     | 27.6 ms: 1.06x slower                                                                 |
| regex_dna                  | 239 ms                                                                      | 255 ms: 1.07x slower                                                                  |
| logging_silent             | 96.3 ns                                                                     | 103 ns: 1.07x slower                                                                  |
| raytrace                   | 266 ms                                                                      | 291 ms: 1.09x slower                                                                  |
| Geometric mean             | (ref)                                                                       | 1.00x slower                                                                          |

Benchmark hidden because not significant (18): async_tree_memoization, comprehensions, json, html5lib, bench_thread_pool, regex_compile, async_tree_io, xml_etree_generate, python_startup, telco, bench_mp_pool, python_startup_no_site, asyncio_tcp_ssl, async_tree_cpu_io_mixed, pickle_pure_python, scimark_sor, pylint, async_tree_none_tg

# HPT report

- Reliability score: 75.35% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x