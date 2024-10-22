# Results vs. base

- fork: faster-cpython
- ref: specialize_shadowed_
- machine: linux-x86_64
- commit hash: 975089f
- commit date: 2024-08-21
- overall geometric mean: 1.01x faster
- HPT reliability: 99.98%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa | bm-20240821-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-975089f |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 264 ms                                                                | 255 ms: 1.04x faster                                                            |
| html5lib       | 63.6 ms                                                               | 66.2 ms: 1.04x slower                                                           |
| tornado_http   | 90.5 ms                                                               | 90.1 ms: 1.00x faster                                                           |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

| Benchmark               | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa | bm-20240821-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-975089f |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed | 566 ms                                                                | 558 ms: 1.01x faster                                                            |
| async_tree_io           | 936 ms                                                                | 927 ms: 1.01x faster                                                            |
| asyncio_tcp_ssl         | 1.78 sec                                                              | 1.79 sec: 1.00x slower                                                          |
| asyncio_websockets      | 555 ms                                                                | 558 ms: 1.00x slower                                                            |
| asyncio_tcp             | 474 ms                                                                | 477 ms: 1.01x slower                                                            |
| coroutines              | 23.1 ms                                                               | 23.3 ms: 1.01x slower                                                           |
| async_generators        | 432 ms                                                                | 435 ms: 1.01x slower                                                            |
| Geometric mean          | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (6): async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa | bm-20240821-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-975089f |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.1 ms                                                               | 77.7 ms: 1.01x faster                                                           |
| pidigits       | 186 ms                                                                | 187 ms: 1.00x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa | bm-20240821-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-975089f |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8       | 26.2 ms                                                               | 23.7 ms: 1.11x faster                                                           |
| regex_effbot   | 3.77 ms                                                               | 3.69 ms: 1.02x faster                                                           |
| regex_compile  | 129 ms                                                                | 128 ms: 1.01x faster                                                            |
| regex_dna      | 223 ms                                                                | 225 ms: 1.01x slower                                                            |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa | bm-20240821-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-975089f |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| unpickle_pure_python | 214 us                                                                | 211 us: 1.02x faster                                                            |
| pickle_pure_python   | 306 us                                                                | 302 us: 1.01x faster                                                            |
| xml_etree_generate   | 85.0 ms                                                               | 84.4 ms: 1.01x faster                                                           |
| xml_etree_process    | 58.9 ms                                                               | 58.6 ms: 1.01x faster                                                           |
| json_loads           | 28.4 us                                                               | 28.6 us: 1.00x slower                                                           |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (4): tomli_loads, json_dumps, xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa | bm-20240821-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-975089f |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 7.08 ms                                                               | 7.05 ms: 1.01x faster                                                           |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                           |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa | bm-20240821-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-975089f |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| django_template | 33.8 ms                                                               | 33.6 ms: 1.01x faster                                                           |
| genshi_xml      | 49.9 ms                                                               | 50.5 ms: 1.01x slower                                                           |
| mako            | 11.2 ms                                                               | 11.4 ms: 1.02x slower                                                           |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark                | bm-20240821-linux-x86_64-python-a4fd7aa4a6420cef1c22-3.14.0a0-a4fd7aa | bm-20240821-linux-x86_64-faster%2dcpython-specialize_shadowed_-3.14.0a0-975089f |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_v8                 | 26.2 ms                                                               | 23.7 ms: 1.11x faster                                                           |
| logging_silent           | 105 ns                                                                | 99.3 ns: 1.05x faster                                                           |
| pycparser                | 1.19 sec                                                              | 1.14 sec: 1.04x faster                                                          |
| 2to3                     | 264 ms                                                                | 255 ms: 1.04x faster                                                            |
| pprint_safe_repr         | 743 ms                                                                | 717 ms: 1.04x faster                                                            |
| pprint_pformat           | 1.51 sec                                                              | 1.47 sec: 1.03x faster                                                          |
| scimark_sparse_mat_mult  | 4.92 ms                                                               | 4.78 ms: 1.03x faster                                                           |
| richards                 | 47.4 ms                                                               | 46.1 ms: 1.03x faster                                                           |
| richards_super           | 53.3 ms                                                               | 52.0 ms: 1.02x faster                                                           |
| typing_runtime_protocols | 162 us                                                                | 159 us: 1.02x faster                                                            |
| regex_effbot             | 3.77 ms                                                               | 3.69 ms: 1.02x faster                                                           |
| sqlglot_transpile        | 1.60 ms                                                               | 1.57 ms: 1.02x faster                                                           |
| sqlglot_parse            | 1.30 ms                                                               | 1.28 ms: 1.02x faster                                                           |
| meteor_contest           | 109 ms                                                                | 107 ms: 1.02x faster                                                            |
| scimark_sor              | 126 ms                                                                | 124 ms: 1.02x faster                                                            |
| spectral_norm            | 114 ms                                                                | 113 ms: 1.02x faster                                                            |
| thrift                   | 779 us                                                                | 766 us: 1.02x faster                                                            |
| deltablue                | 3.26 ms                                                               | 3.20 ms: 1.02x faster                                                           |
| unpickle_pure_python     | 214 us                                                                | 211 us: 1.02x faster                                                            |
| scimark_lu               | 114 ms                                                                | 112 ms: 1.02x faster                                                            |
| raytrace                 | 264 ms                                                                | 260 ms: 1.01x faster                                                            |
| sympy_integrate          | 19.7 ms                                                               | 19.4 ms: 1.01x faster                                                           |
| pickle_pure_python       | 306 us                                                                | 302 us: 1.01x faster                                                            |
| chaos                    | 59.6 ms                                                               | 58.7 ms: 1.01x faster                                                           |
| hexiom                   | 6.30 ms                                                               | 6.22 ms: 1.01x faster                                                           |
| async_tree_cpu_io_mixed  | 566 ms                                                                | 558 ms: 1.01x faster                                                            |
| pathlib                  | 16.1 ms                                                               | 15.9 ms: 1.01x faster                                                           |
| scimark_fft              | 368 ms                                                                | 364 ms: 1.01x faster                                                            |
| async_tree_io            | 936 ms                                                                | 927 ms: 1.01x faster                                                            |
| deepcopy_memo            | 29.8 us                                                               | 29.6 us: 1.01x faster                                                           |
| generators               | 28.1 ms                                                               | 27.9 ms: 1.01x faster                                                           |
| xml_etree_generate       | 85.0 ms                                                               | 84.4 ms: 1.01x faster                                                           |
| deepcopy                 | 262 us                                                                | 260 us: 1.01x faster                                                            |
| scimark_monte_carlo      | 68.3 ms                                                               | 67.8 ms: 1.01x faster                                                           |
| bench_thread_pool        | 789 us                                                                | 783 us: 1.01x faster                                                            |
| fannkuch                 | 407 ms                                                                | 404 ms: 1.01x faster                                                            |
| sympy_sum                | 148 ms                                                                | 147 ms: 1.01x faster                                                            |
| float                    | 78.1 ms                                                               | 77.7 ms: 1.01x faster                                                           |
| regex_compile            | 129 ms                                                                | 128 ms: 1.01x faster                                                            |
| django_template          | 33.8 ms                                                               | 33.6 ms: 1.01x faster                                                           |
| python_startup_no_site   | 7.08 ms                                                               | 7.05 ms: 1.01x faster                                                           |
| mdp                      | 2.53 sec                                                              | 2.52 sec: 1.01x faster                                                          |
| xml_etree_process        | 58.9 ms                                                               | 58.6 ms: 1.01x faster                                                           |
| tornado_http             | 90.5 ms                                                               | 90.1 ms: 1.00x faster                                                           |
| python_startup           | 10.5 ms                                                               | 10.5 ms: 1.00x faster                                                           |
| create_gc_cycles         | 1.76 ms                                                               | 1.76 ms: 1.00x faster                                                           |
| pidigits                 | 186 ms                                                                | 187 ms: 1.00x slower                                                            |
| asyncio_tcp_ssl          | 1.78 sec                                                              | 1.79 sec: 1.00x slower                                                          |
| json_loads               | 28.4 us                                                               | 28.6 us: 1.00x slower                                                           |
| asyncio_websockets       | 555 ms                                                                | 558 ms: 1.00x slower                                                            |
| asyncio_tcp              | 474 ms                                                                | 477 ms: 1.01x slower                                                            |
| coroutines               | 23.1 ms                                                               | 23.3 ms: 1.01x slower                                                           |
| async_generators         | 432 ms                                                                | 435 ms: 1.01x slower                                                            |
| pyflate                  | 466 ms                                                                | 470 ms: 1.01x slower                                                            |
| regex_dna                | 223 ms                                                                | 225 ms: 1.01x slower                                                            |
| genshi_xml               | 49.9 ms                                                               | 50.5 ms: 1.01x slower                                                           |
| logging_simple           | 5.47 us                                                               | 5.54 us: 1.01x slower                                                           |
| mako                     | 11.2 ms                                                               | 11.4 ms: 1.02x slower                                                           |
| nqueens                  | 79.7 ms                                                               | 81.3 ms: 1.02x slower                                                           |
| html5lib                 | 63.6 ms                                                               | 66.2 ms: 1.04x slower                                                           |
| go                       | 142 ms                                                                | 161 ms: 1.13x slower                                                            |
| Geometric mean           | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (28): async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_memoization, telco, coverage, async_tree_memoization_tg, pylint, sympy_expand, sympy_str, async_tree_none, logging_format, tomli_loads, sqlglot_optimize, async_tree_none_tg, sqlglot_normalize, docutils, bpe_tokeniser, genshi_text, gc_traversal, json_dumps, crypto_pyaes, xml_etree_iterparse, bench_mp_pool, nbody, comprehensions, deepcopy_reduce, xml_etree_parse, json

# HPT report

- Reliability score: 99.98% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x