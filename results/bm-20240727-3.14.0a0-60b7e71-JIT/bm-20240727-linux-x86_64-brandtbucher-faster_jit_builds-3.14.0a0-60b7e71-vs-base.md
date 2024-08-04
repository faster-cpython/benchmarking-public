# Results vs. base

- fork: brandtbucher
- ref: faster_jit_builds
- machine: linux-x86_64
- commit hash: 60b7e71
- commit date: 2024-07-27
- overall geometric mean: 1.00x slower
- HPT reliability: 71.57%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark       | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| coroutines      | 23.3 ms                                                               | 22.7 ms: 1.03x faster                                                    |
| asyncio_tcp_ssl | 1.80 sec                                                              | 1.79 sec: 1.00x faster                                                   |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (11): async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_io_tg, async_tree_none_tg, asyncio_websockets, async_tree_none, asyncio_tcp, async_generators, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 70.5 ms                                                               | 70.0 ms: 1.01x faster                                                    |
| pidigits       | 185 ms                                                                | 186 ms: 1.00x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_compile  | 134 ms                                                                | 132 ms: 1.01x faster                                                     |
| regex_dna      | 223 ms                                                                | 228 ms: 1.02x slower                                                     |
| regex_effbot   | 3.69 ms                                                               | 3.86 ms: 1.05x slower                                                    |
| regex_v8       | 23.7 ms                                                               | 25.1 ms: 1.06x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.03x slower                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|--------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| pickle_pure_python | 298 us                                                                | 294 us: 1.02x faster                                                     |
| xml_etree_generate | 80.3 ms                                                               | 80.7 ms: 1.01x slower                                                    |
| json_dumps         | 10.3 ms                                                               | 10.5 ms: 1.01x slower                                                    |
| Geometric mean     | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (6): unpickle_pure_python, xml_etree_iterparse, xml_etree_parse, tomli_loads, xml_etree_process, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 10.6 ms                                                               | 10.6 ms: 1.00x slower                                                    |
| python_startup_no_site | 7.16 ms                                                               | 7.16 ms: 1.00x slower                                                    |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_text    | 24.8 ms                                                               | 24.6 ms: 1.01x faster                                                    |
| genshi_xml     | 59.4 ms                                                               | 58.9 ms: 1.01x faster                                                    |
| mako           | 9.85 ms                                                               | 9.95 ms: 1.01x slower                                                    |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                             |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20240725-linux-x86_64-python-5f6001130f8ada871193-3.14.0a0-5f60011 | bm-20240727-linux-x86_64-brandtbucher-faster_jit_builds-3.14.0a0-60b7e71 |
|-------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------------------:|
| spectral_norm           | 102 ms                                                                | 98.4 ms: 1.04x faster                                                    |
| coroutines              | 23.3 ms                                                               | 22.7 ms: 1.03x faster                                                    |
| scimark_sor             | 130 ms                                                                | 128 ms: 1.02x faster                                                     |
| pickle_pure_python      | 298 us                                                                | 294 us: 1.02x faster                                                     |
| logging_simple          | 5.54 us                                                               | 5.47 us: 1.01x faster                                                    |
| logging_silent          | 102 ns                                                                | 101 ns: 1.01x faster                                                     |
| logging_format          | 6.07 us                                                               | 6.00 us: 1.01x faster                                                    |
| regex_compile           | 134 ms                                                                | 132 ms: 1.01x faster                                                     |
| genshi_text             | 24.8 ms                                                               | 24.6 ms: 1.01x faster                                                    |
| coverage                | 92.2 ms                                                               | 91.3 ms: 1.01x faster                                                    |
| genshi_xml              | 59.4 ms                                                               | 58.9 ms: 1.01x faster                                                    |
| float                   | 70.5 ms                                                               | 70.0 ms: 1.01x faster                                                    |
| sympy_sum               | 169 ms                                                                | 168 ms: 1.01x faster                                                     |
| sqlglot_parse           | 1.27 ms                                                               | 1.26 ms: 1.01x faster                                                    |
| go                      | 144 ms                                                                | 143 ms: 1.01x faster                                                     |
| thrift                  | 790 us                                                                | 785 us: 1.01x faster                                                     |
| deepcopy_memo           | 28.3 us                                                               | 28.1 us: 1.01x faster                                                    |
| mdp                     | 2.55 sec                                                              | 2.53 sec: 1.00x faster                                                   |
| sqlglot_optimize        | 56.0 ms                                                               | 55.8 ms: 1.00x faster                                                    |
| asyncio_tcp_ssl         | 1.80 sec                                                              | 1.79 sec: 1.00x faster                                                   |
| create_gc_cycles        | 1.76 ms                                                               | 1.75 ms: 1.00x faster                                                    |
| python_startup          | 10.6 ms                                                               | 10.6 ms: 1.00x slower                                                    |
| python_startup_no_site  | 7.16 ms                                                               | 7.16 ms: 1.00x slower                                                    |
| pidigits                | 185 ms                                                                | 186 ms: 1.00x slower                                                     |
| meteor_contest          | 104 ms                                                                | 104 ms: 1.00x slower                                                     |
| hexiom                  | 6.53 ms                                                               | 6.55 ms: 1.00x slower                                                    |
| generators              | 28.4 ms                                                               | 28.5 ms: 1.00x slower                                                    |
| deltablue               | 3.46 ms                                                               | 3.48 ms: 1.00x slower                                                    |
| xml_etree_generate      | 80.3 ms                                                               | 80.7 ms: 1.01x slower                                                    |
| scimark_fft             | 306 ms                                                                | 308 ms: 1.01x slower                                                     |
| comprehensions          | 16.4 us                                                               | 16.5 us: 1.01x slower                                                    |
| richards_super          | 46.3 ms                                                               | 46.7 ms: 1.01x slower                                                    |
| sympy_str               | 293 ms                                                                | 295 ms: 1.01x slower                                                     |
| sympy_expand            | 497 ms                                                                | 501 ms: 1.01x slower                                                     |
| richards                | 40.0 ms                                                               | 40.3 ms: 1.01x slower                                                    |
| chaos                   | 57.5 ms                                                               | 58.1 ms: 1.01x slower                                                    |
| mako                    | 9.85 ms                                                               | 9.95 ms: 1.01x slower                                                    |
| json_dumps              | 10.3 ms                                                               | 10.5 ms: 1.01x slower                                                    |
| scimark_sparse_mat_mult | 4.24 ms                                                               | 4.31 ms: 1.02x slower                                                    |
| gc_traversal            | 3.67 ms                                                               | 3.73 ms: 1.02x slower                                                    |
| regex_dna               | 223 ms                                                                | 228 ms: 1.02x slower                                                     |
| pycparser               | 1.11 sec                                                              | 1.16 sec: 1.04x slower                                                   |
| regex_effbot            | 3.69 ms                                                               | 3.86 ms: 1.05x slower                                                    |
| regex_v8                | 23.7 ms                                                               | 25.1 ms: 1.06x slower                                                    |
| Geometric mean          | (ref)                                                                 | 1.00x slower                                                             |

Benchmark hidden because not significant (46): unpickle_pure_python, async_tree_cpu_io_mixed_tg, typing_runtime_protocols, async_tree_io, async_tree_cpu_io_mixed, pprint_pformat, pprint_safe_repr, telco, dask, async_tree_memoization_tg, xml_etree_iterparse, json, html5lib, async_tree_io_tg, sympy_integrate, tornado_http, sqlglot_normalize, xml_etree_parse, async_tree_none_tg, tomli_loads, 2to3, django_template, xml_etree_process, pyflate, scimark_monte_carlo, bench_mp_pool, asyncio_websockets, sqlglot_transpile, nqueens, async_tree_none, bench_thread_pool, pathlib, pylint, asyncio_tcp, docutils, bpe_tokeniser, nbody, deepcopy, json_loads, async_generators, raytrace, scimark_lu, async_tree_memoization, deepcopy_reduce, crypto_pyaes, fannkuch

# HPT report

- Reliability score: 71.57% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x