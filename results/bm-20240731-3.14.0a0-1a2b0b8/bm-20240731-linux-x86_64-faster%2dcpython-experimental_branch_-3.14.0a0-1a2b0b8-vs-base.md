# Results vs. base

- fork: faster-cpython
- ref: experimental_branch_
- machine: linux-x86_64
- commit hash: 1a2b0b8
- commit date: 2024-07-31
- overall geometric mean: 1.01x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| 2to3           | 263 ms                                                                | 266 ms: 1.01x slower                                                            |
| docutils       | 2.72 sec                                                              | 2.73 sec: 1.00x slower                                                          |
| html5lib       | 64.6 ms                                                               | 65.9 ms: 1.02x slower                                                           |
| tornado_http   | 89.7 ms                                                               | 90.6 ms: 1.01x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmarks with tag 'asyncio':
==============================

| Benchmark          | bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|--------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| asyncio_websockets | 559 ms                                                                | 554 ms: 1.01x faster                                                            |
| asyncio_tcp        | 491 ms                                                                | 488 ms: 1.01x faster                                                            |
| asyncio_tcp_ssl    | 1.79 sec                                                              | 1.80 sec: 1.00x slower                                                          |
| coroutines         | 22.3 ms                                                               | 22.7 ms: 1.02x slower                                                           |
| Geometric mean     | (ref)                                                                 | 1.00x slower                                                                    |

Benchmark hidden because not significant (9): async_tree_none, async_tree_io_tg, async_generators, async_tree_cpu_io_mixed, async_tree_none_tg, async_tree_io, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| float          | 78.4 ms                                                               | 76.4 ms: 1.03x faster                                                           |
| pidigits       | 187 ms                                                                | 187 ms: 1.00x faster                                                            |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                    |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| regex_dna      | 219 ms                                                                | 216 ms: 1.01x faster                                                            |
| regex_effbot   | 3.66 ms                                                               | 3.70 ms: 1.01x slower                                                           |
| regex_compile  | 132 ms                                                                | 135 ms: 1.02x slower                                                            |
| regex_v8       | 24.5 ms                                                               | 25.1 ms: 1.02x slower                                                           |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                                    |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| xml_etree_process    | 60.0 ms                                                               | 58.7 ms: 1.02x faster                                                           |
| xml_etree_generate   | 86.1 ms                                                               | 85.2 ms: 1.01x faster                                                           |
| unpickle_pure_python | 212 us                                                                | 213 us: 1.00x slower                                                            |
| pickle_pure_python   | 303 us                                                                | 307 us: 1.01x slower                                                            |
| tomli_loads          | 2.07 sec                                                              | 2.10 sec: 1.02x slower                                                          |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                                    |

Benchmark hidden because not significant (4): xml_etree_parse, json_loads, json_dumps, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| python_startup_no_site | 7.05 ms                                                               | 7.06 ms: 1.00x slower                                                           |
| python_startup         | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                           |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| genshi_xml      | 51.7 ms                                                               | 50.2 ms: 1.03x faster                                                           |
| genshi_text     | 23.5 ms                                                               | 22.8 ms: 1.03x faster                                                           |
| django_template | 34.3 ms                                                               | 35.5 ms: 1.03x slower                                                           |
| mako            | 10.9 ms                                                               | 11.4 ms: 1.05x slower                                                           |
| Geometric mean  | (ref)                                                                 | 1.01x slower                                                                    |

All benchmarks:
===============

| Benchmark               | bm-20240730-linux-x86_64-python-d27a53fc02a87e76066f-3.14.0a0-d27a53f | bm-20240731-linux-x86_64-faster%2dcpython-experimental_branch_-3.14.0a0-1a2b0b8 |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------------:|
| mdp                     | 2.71 sec                                                              | 2.52 sec: 1.07x faster                                                          |
| genshi_xml              | 51.7 ms                                                               | 50.2 ms: 1.03x faster                                                           |
| genshi_text             | 23.5 ms                                                               | 22.8 ms: 1.03x faster                                                           |
| float                   | 78.4 ms                                                               | 76.4 ms: 1.03x faster                                                           |
| xml_etree_process       | 60.0 ms                                                               | 58.7 ms: 1.02x faster                                                           |
| generators              | 28.5 ms                                                               | 27.9 ms: 1.02x faster                                                           |
| regex_dna               | 219 ms                                                                | 216 ms: 1.01x faster                                                            |
| richards                | 46.9 ms                                                               | 46.5 ms: 1.01x faster                                                           |
| xml_etree_generate      | 86.1 ms                                                               | 85.2 ms: 1.01x faster                                                           |
| asyncio_websockets      | 559 ms                                                                | 554 ms: 1.01x faster                                                            |
| asyncio_tcp             | 491 ms                                                                | 488 ms: 1.01x faster                                                            |
| deepcopy                | 265 us                                                                | 263 us: 1.00x faster                                                            |
| nqueens                 | 80.2 ms                                                               | 80.0 ms: 1.00x faster                                                           |
| pidigits                | 187 ms                                                                | 187 ms: 1.00x faster                                                            |
| python_startup_no_site  | 7.05 ms                                                               | 7.06 ms: 1.00x slower                                                           |
| python_startup          | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                           |
| sqlglot_normalize       | 108 ms                                                                | 108 ms: 1.00x slower                                                            |
| bench_thread_pool       | 784 us                                                                | 787 us: 1.00x slower                                                            |
| sqlglot_optimize        | 53.6 ms                                                               | 53.8 ms: 1.00x slower                                                           |
| create_gc_cycles        | 1.73 ms                                                               | 1.73 ms: 1.00x slower                                                           |
| asyncio_tcp_ssl         | 1.79 sec                                                              | 1.80 sec: 1.00x slower                                                          |
| docutils                | 2.72 sec                                                              | 2.73 sec: 1.00x slower                                                          |
| unpickle_pure_python    | 212 us                                                                | 213 us: 1.00x slower                                                            |
| sympy_integrate         | 19.7 ms                                                               | 19.8 ms: 1.00x slower                                                           |
| scimark_sparse_mat_mult | 4.68 ms                                                               | 4.71 ms: 1.01x slower                                                           |
| pprint_safe_repr        | 736 ms                                                                | 740 ms: 1.01x slower                                                            |
| fannkuch                | 407 ms                                                                | 409 ms: 1.01x slower                                                            |
| pprint_pformat          | 1.50 sec                                                              | 1.51 sec: 1.01x slower                                                          |
| deltablue               | 3.19 ms                                                               | 3.22 ms: 1.01x slower                                                           |
| pathlib                 | 15.7 ms                                                               | 15.9 ms: 1.01x slower                                                           |
| deepcopy_reduce         | 2.74 us                                                               | 2.77 us: 1.01x slower                                                           |
| 2to3                    | 263 ms                                                                | 266 ms: 1.01x slower                                                            |
| logging_simple          | 5.58 us                                                               | 5.63 us: 1.01x slower                                                           |
| tornado_http            | 89.7 ms                                                               | 90.6 ms: 1.01x slower                                                           |
| sqlglot_parse           | 1.27 ms                                                               | 1.29 ms: 1.01x slower                                                           |
| regex_effbot            | 3.66 ms                                                               | 3.70 ms: 1.01x slower                                                           |
| pickle_pure_python      | 303 us                                                                | 307 us: 1.01x slower                                                            |
| sympy_str               | 271 ms                                                                | 275 ms: 1.01x slower                                                            |
| chaos                   | 58.7 ms                                                               | 59.5 ms: 1.01x slower                                                           |
| sympy_sum               | 150 ms                                                                | 152 ms: 1.02x slower                                                            |
| thrift                  | 782 us                                                                | 794 us: 1.02x slower                                                            |
| sqlglot_transpile       | 1.57 ms                                                               | 1.59 ms: 1.02x slower                                                           |
| bpe_tokeniser           | 4.81 sec                                                              | 4.89 sec: 1.02x slower                                                          |
| tomli_loads             | 2.07 sec                                                              | 2.10 sec: 1.02x slower                                                          |
| sympy_expand            | 459 ms                                                                | 467 ms: 1.02x slower                                                            |
| spectral_norm           | 110 ms                                                                | 112 ms: 1.02x slower                                                            |
| comprehensions          | 16.5 us                                                               | 16.8 us: 1.02x slower                                                           |
| coroutines              | 22.3 ms                                                               | 22.7 ms: 1.02x slower                                                           |
| pycparser               | 1.13 sec                                                              | 1.15 sec: 1.02x slower                                                          |
| scimark_fft             | 360 ms                                                                | 367 ms: 1.02x slower                                                            |
| html5lib                | 64.6 ms                                                               | 65.9 ms: 1.02x slower                                                           |
| scimark_lu              | 113 ms                                                                | 116 ms: 1.02x slower                                                            |
| go                      | 141 ms                                                                | 144 ms: 1.02x slower                                                            |
| regex_compile           | 132 ms                                                                | 135 ms: 1.02x slower                                                            |
| deepcopy_memo           | 29.6 us                                                               | 30.3 us: 1.02x slower                                                           |
| regex_v8                | 24.5 ms                                                               | 25.1 ms: 1.02x slower                                                           |
| raytrace                | 257 ms                                                                | 264 ms: 1.02x slower                                                            |
| hexiom                  | 6.16 ms                                                               | 6.33 ms: 1.03x slower                                                           |
| scimark_monte_carlo     | 67.4 ms                                                               | 69.4 ms: 1.03x slower                                                           |
| gc_traversal            | 3.53 ms                                                               | 3.65 ms: 1.03x slower                                                           |
| django_template         | 34.3 ms                                                               | 35.5 ms: 1.03x slower                                                           |
| pyflate                 | 469 ms                                                                | 490 ms: 1.04x slower                                                            |
| crypto_pyaes            | 71.4 ms                                                               | 74.8 ms: 1.05x slower                                                           |
| logging_silent          | 99.4 ns                                                               | 104 ns: 1.05x slower                                                            |
| mako                    | 10.9 ms                                                               | 11.4 ms: 1.05x slower                                                           |
| scimark_sor             | 124 ms                                                                | 134 ms: 1.08x slower                                                            |
| Geometric mean          | (ref)                                                                 | 1.01x slower                                                                    |

Benchmark hidden because not significant (24): xml_etree_parse, json_loads, typing_runtime_protocols, async_tree_none, async_tree_io_tg, meteor_contest, richards_super, async_generators, async_tree_cpu_io_mixed, coverage, async_tree_none_tg, telco, async_tree_io, logging_format, bench_mp_pool, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, json_dumps, json, nbody, pylint, xml_etree_iterparse, dask, async_tree_memoization

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x