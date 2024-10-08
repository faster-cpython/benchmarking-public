# Results vs. base

- fork: faster-cpython
- ref: specialize_call_kw
- machine: linux-x86_64
- commit hash: 6b9055c
- commit date: 2024-08-14
- overall geometric mean: 1.00x slower
- HPT reliability: 63.57%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240813-pythonperf2-x86_64-python-7a65439b93d6ee4d4e32-3.14.0a0-7a65439 | bm-20240814-pythonperf2-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-6b9055c |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| 2to3           | 352 ms                                                                      | 353 ms: 1.00x slower                                                                |
| tornado_http   | 128 ms                                                                      | 127 ms: 1.01x faster                                                                |
| Geometric mean | (ref)                                                                       | 1.00x faster                                                                        |

Benchmark hidden because not significant (2): docutils, html5lib

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240813-pythonperf2-x86_64-python-7a65439b93d6ee4d4e32-3.14.0a0-7a65439 | bm-20240814-pythonperf2-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-6b9055c |
|-------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| async_generators        | 389 ms                                                                      | 385 ms: 1.01x faster                                                                |
| coroutines              | 22.6 ms                                                                     | 22.5 ms: 1.01x faster                                                               |
| asyncio_tcp_ssl         | 1.61 sec                                                                    | 1.60 sec: 1.00x faster                                                              |
| asyncio_tcp             | 386 ms                                                                      | 388 ms: 1.00x slower                                                                |
| asyncio_websockets      | 393 ms                                                                      | 398 ms: 1.01x slower                                                                |
| async_tree_memoization  | 434 ms                                                                      | 443 ms: 1.02x slower                                                                |
| async_tree_none         | 340 ms                                                                      | 348 ms: 1.03x slower                                                                |
| async_tree_cpu_io_mixed | 585 ms                                                                      | 604 ms: 1.03x slower                                                                |
| Geometric mean          | (ref)                                                                       | 1.01x slower                                                                        |

Benchmark hidden because not significant (5): async_tree_cpu_io_mixed_tg, async_tree_none_tg, async_tree_memoization_tg, async_tree_io, async_tree_io_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240813-pythonperf2-x86_64-python-7a65439b93d6ee4d4e32-3.14.0a0-7a65439 | bm-20240814-pythonperf2-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-6b9055c |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| float          | 92.6 ms                                                                     | 93.8 ms: 1.01x slower                                                               |
| nbody          | 125 ms                                                                      | 128 ms: 1.03x slower                                                                |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                        |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240813-pythonperf2-x86_64-python-7a65439b93d6ee4d4e32-3.14.0a0-7a65439 | bm-20240814-pythonperf2-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-6b9055c |
|----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| regex_dna      | 245 ms                                                                      | 240 ms: 1.02x faster                                                                |
| regex_compile  | 211 ms                                                                      | 208 ms: 1.01x faster                                                                |
| regex_v8       | 26.9 ms                                                                     | 26.8 ms: 1.00x faster                                                               |
| Geometric mean | (ref)                                                                       | 1.01x faster                                                                        |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240813-pythonperf2-x86_64-python-7a65439b93d6ee4d4e32-3.14.0a0-7a65439 | bm-20240814-pythonperf2-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-6b9055c |
|----------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| unpickle_pure_python | 276 us                                                                      | 272 us: 1.01x faster                                                                |
| json_loads           | 25.4 us                                                                     | 25.6 us: 1.01x slower                                                               |
| xml_etree_parse      | 142 ms                                                                      | 143 ms: 1.01x slower                                                                |
| xml_etree_iterparse  | 113 ms                                                                      | 116 ms: 1.02x slower                                                                |
| xml_etree_process    | 68.0 ms                                                                     | 70.0 ms: 1.03x slower                                                               |
| json_dumps           | 11.5 ms                                                                     | 11.9 ms: 1.03x slower                                                               |
| xml_etree_generate   | 97.6 ms                                                                     | 101 ms: 1.03x slower                                                                |
| Geometric mean       | (ref)                                                                       | 1.01x slower                                                                        |

Benchmark hidden because not significant (2): tomli_loads, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240813-pythonperf2-x86_64-python-7a65439b93d6ee4d4e32-3.14.0a0-7a65439 | bm-20240814-pythonperf2-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-6b9055c |
|------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| python_startup         | 13.3 ms                                                                     | 13.4 ms: 1.00x slower                                                               |
| python_startup_no_site | 9.08 ms                                                                     | 9.12 ms: 1.00x slower                                                               |
| Geometric mean         | (ref)                                                                       | 1.00x slower                                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240813-pythonperf2-x86_64-python-7a65439b93d6ee4d4e32-3.14.0a0-7a65439 | bm-20240814-pythonperf2-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-6b9055c |
|-----------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| django_template | 45.5 ms                                                                     | 44.4 ms: 1.02x faster                                                               |
| genshi_text     | 31.4 ms                                                                     | 30.8 ms: 1.02x faster                                                               |
| mako            | 14.3 ms                                                                     | 14.6 ms: 1.02x slower                                                               |
| Geometric mean  | (ref)                                                                       | 1.01x faster                                                                        |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20240813-pythonperf2-x86_64-python-7a65439b93d6ee4d4e32-3.14.0a0-7a65439 | bm-20240814-pythonperf2-x86_64-faster%2dcpython-specialize_call_kw-3.14.0a0-6b9055c |
|--------------------------|:---------------------------------------------------------------------------:|:-----------------------------------------------------------------------------------:|
| generators               | 47.1 ms                                                                     | 45.3 ms: 1.04x faster                                                               |
| deepcopy_reduce          | 3.33 us                                                                     | 3.23 us: 1.03x faster                                                               |
| scimark_lu               | 130 ms                                                                      | 127 ms: 1.03x faster                                                                |
| scimark_monte_carlo      | 96.1 ms                                                                     | 93.7 ms: 1.03x faster                                                               |
| django_template          | 45.5 ms                                                                     | 44.4 ms: 1.02x faster                                                               |
| thrift                   | 906 us                                                                      | 886 us: 1.02x faster                                                                |
| regex_dna                | 245 ms                                                                      | 240 ms: 1.02x faster                                                                |
| genshi_text              | 31.4 ms                                                                     | 30.8 ms: 1.02x faster                                                               |
| logging_format           | 7.40 us                                                                     | 7.27 us: 1.02x faster                                                               |
| deltablue                | 5.33 ms                                                                     | 5.24 ms: 1.02x faster                                                               |
| go                       | 202 ms                                                                      | 199 ms: 1.01x faster                                                                |
| unpickle_pure_python     | 276 us                                                                      | 272 us: 1.01x faster                                                                |
| regex_compile            | 211 ms                                                                      | 208 ms: 1.01x faster                                                                |
| logging_simple           | 6.76 us                                                                     | 6.67 us: 1.01x faster                                                               |
| sympy_sum                | 194 ms                                                                      | 192 ms: 1.01x faster                                                                |
| pycparser                | 1.56 sec                                                                    | 1.54 sec: 1.01x faster                                                              |
| telco                    | 9.05 ms                                                                     | 8.95 ms: 1.01x faster                                                               |
| async_generators         | 389 ms                                                                      | 385 ms: 1.01x faster                                                                |
| sqlglot_parse            | 1.75 ms                                                                     | 1.73 ms: 1.01x faster                                                               |
| tornado_http             | 128 ms                                                                      | 127 ms: 1.01x faster                                                                |
| sqlglot_optimize         | 73.2 ms                                                                     | 72.5 ms: 1.01x faster                                                               |
| coverage                 | 80.8 ms                                                                     | 80.0 ms: 1.01x faster                                                               |
| hexiom                   | 10.5 ms                                                                     | 10.4 ms: 1.01x faster                                                               |
| logging_silent           | 155 ns                                                                      | 154 ns: 1.01x faster                                                                |
| sqlglot_transpile        | 2.23 ms                                                                     | 2.21 ms: 1.01x faster                                                               |
| fannkuch                 | 500 ms                                                                      | 496 ms: 1.01x faster                                                                |
| meteor_contest           | 146 ms                                                                      | 145 ms: 1.01x faster                                                                |
| coroutines               | 22.6 ms                                                                     | 22.5 ms: 1.01x faster                                                               |
| spectral_norm            | 156 ms                                                                      | 155 ms: 1.01x faster                                                                |
| deepcopy_memo            | 47.8 us                                                                     | 47.5 us: 1.01x faster                                                               |
| richards                 | 63.9 ms                                                                     | 63.6 ms: 1.00x faster                                                               |
| pprint_safe_repr         | 1.03 sec                                                                    | 1.03 sec: 1.00x faster                                                              |
| sympy_integrate          | 28.6 ms                                                                     | 28.5 ms: 1.00x faster                                                               |
| pyflate                  | 615 ms                                                                      | 613 ms: 1.00x faster                                                                |
| richards_super           | 71.4 ms                                                                     | 71.2 ms: 1.00x faster                                                               |
| regex_v8                 | 26.9 ms                                                                     | 26.8 ms: 1.00x faster                                                               |
| asyncio_tcp_ssl          | 1.61 sec                                                                    | 1.60 sec: 1.00x faster                                                              |
| python_startup           | 13.3 ms                                                                     | 13.4 ms: 1.00x slower                                                               |
| 2to3                     | 352 ms                                                                      | 353 ms: 1.00x slower                                                                |
| sympy_str                | 372 ms                                                                      | 373 ms: 1.00x slower                                                                |
| bpe_tokeniser            | 5.75 sec                                                                    | 5.77 sec: 1.00x slower                                                              |
| deepcopy                 | 354 us                                                                      | 355 us: 1.00x slower                                                                |
| python_startup_no_site   | 9.08 ms                                                                     | 9.12 ms: 1.00x slower                                                               |
| asyncio_tcp              | 386 ms                                                                      | 388 ms: 1.00x slower                                                                |
| json_loads               | 25.4 us                                                                     | 25.6 us: 1.01x slower                                                               |
| xml_etree_parse          | 142 ms                                                                      | 143 ms: 1.01x slower                                                                |
| typing_runtime_protocols | 198 us                                                                      | 200 us: 1.01x slower                                                                |
| chaos                    | 78.9 ms                                                                     | 80.0 ms: 1.01x slower                                                               |
| asyncio_websockets       | 393 ms                                                                      | 398 ms: 1.01x slower                                                                |
| float                    | 92.6 ms                                                                     | 93.8 ms: 1.01x slower                                                               |
| raytrace                 | 321 ms                                                                      | 325 ms: 1.01x slower                                                                |
| comprehensions           | 26.6 us                                                                     | 27.2 us: 1.02x slower                                                               |
| scimark_fft              | 418 ms                                                                      | 426 ms: 1.02x slower                                                                |
| async_tree_memoization   | 434 ms                                                                      | 443 ms: 1.02x slower                                                                |
| mako                     | 14.3 ms                                                                     | 14.6 ms: 1.02x slower                                                               |
| xml_etree_iterparse      | 113 ms                                                                      | 116 ms: 1.02x slower                                                                |
| async_tree_none          | 340 ms                                                                      | 348 ms: 1.03x slower                                                                |
| nbody                    | 125 ms                                                                      | 128 ms: 1.03x slower                                                                |
| xml_etree_process        | 68.0 ms                                                                     | 70.0 ms: 1.03x slower                                                               |
| json_dumps               | 11.5 ms                                                                     | 11.9 ms: 1.03x slower                                                               |
| xml_etree_generate       | 97.6 ms                                                                     | 101 ms: 1.03x slower                                                                |
| json                     | 5.61 ms                                                                     | 5.78 ms: 1.03x slower                                                               |
| async_tree_cpu_io_mixed  | 585 ms                                                                      | 604 ms: 1.03x slower                                                                |
| scimark_sparse_mat_mult  | 6.42 ms                                                                     | 6.62 ms: 1.03x slower                                                               |
| crypto_pyaes             | 92.0 ms                                                                     | 95.2 ms: 1.03x slower                                                               |
| mdp                      | 2.71 sec                                                                    | 2.80 sec: 1.03x slower                                                              |
| gc_traversal             | 4.46 ms                                                                     | 4.76 ms: 1.07x slower                                                               |
| Geometric mean           | (ref)                                                                       | 1.00x slower                                                                        |

Benchmark hidden because not significant (22): bench_mp_pool, create_gc_cycles, bench_thread_pool, tomli_loads, pylint, pathlib, genshi_xml, sympy_expand, sqlglot_normalize, pidigits, pprint_pformat, nqueens, html5lib, docutils, async_tree_cpu_io_mixed_tg, pickle_pure_python, regex_effbot, scimark_sor, async_tree_none_tg, async_tree_memoization_tg, async_tree_io, async_tree_io_tg

# HPT report

- Reliability score: 63.57% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x