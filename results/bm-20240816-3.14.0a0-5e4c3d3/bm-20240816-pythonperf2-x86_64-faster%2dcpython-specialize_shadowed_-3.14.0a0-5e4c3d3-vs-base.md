# Results vs. base

- fork: faster-cpython
- ref: specialize_shadowed_
- machine: linux-x86_64
- commit hash: 5e4c3d3
- commit date: 2024-08-16
- overall geometric mean: 1.00x faster
- HPT reliability: 58.38%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c | bm-20240816-pythonperf2-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| 2to3           | 287 ms                                                                      | 281 ms: 1.02x faster                                                                  |
| html5lib       | 73.5 ms                                                                     | 72.7 ms: 1.01x faster                                                                 |
| tornado_http   | 117 ms                                                                      | 116 ms: 1.01x faster                                                                  |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                          |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c | bm-20240816-pythonperf2-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3 |
|------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| async_generators | 353 ms                                                                      | 355 ms: 1.00x slower                                                                  |
| coroutines       | 21.3 ms                                                                     | 22.0 ms: 1.03x slower                                                                 |
| async_tree_io_tg | 774 ms                                                                      | 804 ms: 1.04x slower                                                                  |
| Geometric mean   | (ref)                                                                       | 1.01x slower                                                                          |

Benchmark hidden because not significant (10): asyncio_tcp, asyncio_tcp_ssl, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, asyncio_websockets, async_tree_io, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_memoization, async_tree_none

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c | bm-20240816-pythonperf2-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| nbody          | 88.3 ms                                                                     | 85.9 ms: 1.03x faster                                                                 |
| float          | 81.6 ms                                                                     | 79.9 ms: 1.02x faster                                                                 |
| pidigits       | 252 ms                                                                      | 253 ms: 1.01x slower                                                                  |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c | bm-20240816-pythonperf2-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| regex_effbot   | 3.64 ms                                                                     | 3.57 ms: 1.02x faster                                                                 |
| regex_compile  | 141 ms                                                                      | 139 ms: 1.01x faster                                                                  |
| regex_v8       | 25.6 ms                                                                     | 27.1 ms: 1.06x slower                                                                 |
| regex_dna      | 239 ms                                                                      | 254 ms: 1.06x slower                                                                  |
| Geometric mean | (ref)                                                                       | 1.02x slower                                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c | bm-20240816-pythonperf2-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3 |
|----------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| json_dumps           | 10.7 ms                                                                     | 10.7 ms: 1.00x faster                                                                 |
| xml_etree_process    | 59.1 ms                                                                     | 59.4 ms: 1.00x slower                                                                 |
| json_loads           | 25.0 us                                                                     | 25.4 us: 1.01x slower                                                                 |
| xml_etree_generate   | 84.2 ms                                                                     | 85.7 ms: 1.02x slower                                                                 |
| tomli_loads          | 2.22 sec                                                                    | 2.27 sec: 1.03x slower                                                                |
| unpickle_pure_python | 220 us                                                                      | 231 us: 1.05x slower                                                                  |
| Geometric mean       | (ref)                                                                       | 1.01x slower                                                                          |

Benchmark hidden because not significant (3): xml_etree_parse, pickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c | bm-20240816-pythonperf2-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3 |
|------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| python_startup_no_site | 9.05 ms                                                                     | 9.00 ms: 1.01x faster                                                                 |
| python_startup         | 13.3 ms                                                                     | 13.3 ms: 1.01x faster                                                                 |
| Geometric mean         | (ref)                                                                       | 1.01x faster                                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c | bm-20240816-pythonperf2-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3 |
|----------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| genshi_xml     | 55.3 ms                                                                     | 53.2 ms: 1.04x faster                                                                 |
| genshi_text    | 25.0 ms                                                                     | 24.6 ms: 1.02x faster                                                                 |
| mako           | 10.2 ms                                                                     | 10.6 ms: 1.03x slower                                                                 |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                          |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark                | bm-20240816-pythonperf2-x86_64-python-a07cf4ce25205d836a6b-3.14.0a0-a07cf4c | bm-20240816-pythonperf2-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-5e4c3d3 |
|--------------------------|:---------------------------------------------------------------------------:|:-------------------------------------------------------------------------------------:|
| coverage                 | 85.5 ms                                                                     | 79.8 ms: 1.07x faster                                                                 |
| gc_traversal             | 4.68 ms                                                                     | 4.49 ms: 1.04x faster                                                                 |
| genshi_xml               | 55.3 ms                                                                     | 53.2 ms: 1.04x faster                                                                 |
| deepcopy_memo            | 30.3 us                                                                     | 29.2 us: 1.04x faster                                                                 |
| scimark_monte_carlo      | 66.6 ms                                                                     | 64.4 ms: 1.03x faster                                                                 |
| comprehensions           | 17.6 us                                                                     | 17.1 us: 1.03x faster                                                                 |
| nbody                    | 88.3 ms                                                                     | 85.9 ms: 1.03x faster                                                                 |
| pprint_pformat           | 1.73 sec                                                                    | 1.68 sec: 1.03x faster                                                                |
| typing_runtime_protocols | 176 us                                                                      | 171 us: 1.03x faster                                                                  |
| regex_effbot             | 3.64 ms                                                                     | 3.57 ms: 1.02x faster                                                                 |
| pprint_safe_repr         | 841 ms                                                                      | 824 ms: 1.02x faster                                                                  |
| float                    | 81.6 ms                                                                     | 79.9 ms: 1.02x faster                                                                 |
| 2to3                     | 287 ms                                                                      | 281 ms: 1.02x faster                                                                  |
| genshi_text              | 25.0 ms                                                                     | 24.6 ms: 1.02x faster                                                                 |
| pycparser                | 1.24 sec                                                                    | 1.22 sec: 1.02x faster                                                                |
| go                       | 164 ms                                                                      | 161 ms: 1.02x faster                                                                  |
| sqlglot_normalize        | 123 ms                                                                      | 121 ms: 1.01x faster                                                                  |
| deltablue                | 3.40 ms                                                                     | 3.36 ms: 1.01x faster                                                                 |
| html5lib                 | 73.5 ms                                                                     | 72.7 ms: 1.01x faster                                                                 |
| tornado_http             | 117 ms                                                                      | 116 ms: 1.01x faster                                                                  |
| generators               | 28.7 ms                                                                     | 28.4 ms: 1.01x faster                                                                 |
| chaos                    | 62.0 ms                                                                     | 61.3 ms: 1.01x faster                                                                 |
| pathlib                  | 16.1 ms                                                                     | 15.9 ms: 1.01x faster                                                                 |
| regex_compile            | 141 ms                                                                      | 139 ms: 1.01x faster                                                                  |
| hexiom                   | 6.30 ms                                                                     | 6.24 ms: 1.01x faster                                                                 |
| telco                    | 8.07 ms                                                                     | 8.00 ms: 1.01x faster                                                                 |
| deepcopy_reduce          | 2.99 us                                                                     | 2.96 us: 1.01x faster                                                                 |
| sqlglot_parse            | 1.42 ms                                                                     | 1.41 ms: 1.01x faster                                                                 |
| sympy_expand             | 505 ms                                                                      | 501 ms: 1.01x faster                                                                  |
| sympy_str                | 296 ms                                                                      | 294 ms: 1.01x faster                                                                  |
| sqlglot_optimize         | 60.1 ms                                                                     | 59.7 ms: 1.01x faster                                                                 |
| python_startup_no_site   | 9.05 ms                                                                     | 9.00 ms: 1.01x faster                                                                 |
| python_startup           | 13.3 ms                                                                     | 13.3 ms: 1.01x faster                                                                 |
| fannkuch                 | 359 ms                                                                      | 357 ms: 1.01x faster                                                                  |
| deepcopy                 | 293 us                                                                      | 292 us: 1.00x faster                                                                  |
| json_dumps               | 10.7 ms                                                                     | 10.7 ms: 1.00x faster                                                                 |
| mdp                      | 2.53 sec                                                                    | 2.52 sec: 1.00x faster                                                                |
| xml_etree_process        | 59.1 ms                                                                     | 59.4 ms: 1.00x slower                                                                 |
| async_generators         | 353 ms                                                                      | 355 ms: 1.00x slower                                                                  |
| pidigits                 | 252 ms                                                                      | 253 ms: 1.01x slower                                                                  |
| crypto_pyaes             | 72.4 ms                                                                     | 72.9 ms: 1.01x slower                                                                 |
| meteor_contest           | 126 ms                                                                      | 126 ms: 1.01x slower                                                                  |
| thrift                   | 864 us                                                                      | 871 us: 1.01x slower                                                                  |
| raytrace                 | 269 ms                                                                      | 271 ms: 1.01x slower                                                                  |
| json_loads               | 25.0 us                                                                     | 25.4 us: 1.01x slower                                                                 |
| scimark_sor              | 109 ms                                                                      | 110 ms: 1.01x slower                                                                  |
| logging_silent           | 96.5 ns                                                                     | 97.9 ns: 1.01x slower                                                                 |
| spectral_norm            | 96.0 ms                                                                     | 97.6 ms: 1.02x slower                                                                 |
| xml_etree_generate       | 84.2 ms                                                                     | 85.7 ms: 1.02x slower                                                                 |
| richards                 | 49.3 ms                                                                     | 50.1 ms: 1.02x slower                                                                 |
| create_gc_cycles         | 1.95 ms                                                                     | 1.98 ms: 1.02x slower                                                                 |
| nqueens                  | 89.9 ms                                                                     | 91.8 ms: 1.02x slower                                                                 |
| tomli_loads              | 2.22 sec                                                                    | 2.27 sec: 1.03x slower                                                                |
| scimark_fft              | 297 ms                                                                      | 306 ms: 1.03x slower                                                                  |
| scimark_sparse_mat_mult  | 4.13 ms                                                                     | 4.25 ms: 1.03x slower                                                                 |
| mako                     | 10.2 ms                                                                     | 10.6 ms: 1.03x slower                                                                 |
| coroutines               | 21.3 ms                                                                     | 22.0 ms: 1.03x slower                                                                 |
| async_tree_io_tg         | 774 ms                                                                      | 804 ms: 1.04x slower                                                                  |
| unpickle_pure_python     | 220 us                                                                      | 231 us: 1.05x slower                                                                  |
| regex_v8                 | 25.6 ms                                                                     | 27.1 ms: 1.06x slower                                                                 |
| regex_dna                | 239 ms                                                                      | 254 ms: 1.06x slower                                                                  |
| Geometric mean           | (ref)                                                                       | 1.00x faster                                                                          |

Benchmark hidden because not significant (28): bench_mp_pool, bench_thread_pool, xml_etree_parse, django_template, asyncio_tcp, pyflate, asyncio_tcp_ssl, bpe_tokeniser, async_tree_cpu_io_mixed_tg, richards_super, sqlglot_transpile, docutils, pylint, pickle_pure_python, sympy_sum, sympy_integrate, xml_etree_iterparse, async_tree_memoization_tg, logging_simple, asyncio_websockets, scimark_lu, async_tree_io, json, logging_format, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_memoization, async_tree_none

# HPT report

- Reliability score: 58.38% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x