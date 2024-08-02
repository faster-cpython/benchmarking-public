# Results vs. base

- fork: brandtbucher
- ref: no_trace_too_short
- machine: linux-x86_64
- commit hash: 1f7ad74
- commit date: 2024-06-06
- overall geometric mean: 1.00x slower
- HPT reliability: 99.59%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-1f7ad74 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 277 ms                                                                | 280 ms: 1.01x slower                                                      |
| docutils       | 2.93 sec                                                              | 2.97 sec: 1.01x slower                                                    |
| html5lib       | 66.6 ms                                                               | 69.5 ms: 1.04x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.02x slower                                                              |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io_tg, async_tree_none, async_tree_none_tg, async_tree_memoization_tg, async_tree_io, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-1f7ad74 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 84.0 ms                                                               | 81.8 ms: 1.03x faster                                                     |
| pidigits       | 188 ms                                                                | 189 ms: 1.00x slower                                                      |
| float          | 72.3 ms                                                               | 73.0 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-1f7ad74 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_compile  | 138 ms                                                                | 138 ms: 1.00x slower                                                      |
| regex_dna      | 230 ms                                                                | 238 ms: 1.03x slower                                                      |
| regex_v8       | 24.5 ms                                                               | 26.6 ms: 1.08x slower                                                     |
| regex_effbot   | 3.65 ms                                                               | 4.01 ms: 1.10x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.05x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-1f7ad74 |
|--------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pickle_list        | 5.23 us                                                               | 5.05 us: 1.04x faster                                                     |
| pickle             | 12.2 us                                                               | 12.0 us: 1.02x faster                                                     |
| json_dumps         | 10.4 ms                                                               | 10.3 ms: 1.01x faster                                                     |
| xml_etree_generate | 82.0 ms                                                               | 81.3 ms: 1.01x faster                                                     |
| unpickle_list      | 5.39 us                                                               | 5.43 us: 1.01x slower                                                     |
| tomli_loads        | 1.93 sec                                                              | 1.95 sec: 1.01x slower                                                    |
| pickle_pure_python | 298 us                                                                | 305 us: 1.02x slower                                                      |
| Geometric mean     | (ref)                                                                 | 1.00x faster                                                              |

Benchmark hidden because not significant (7): pickle_dict, unpickle, xml_etree_iterparse, xml_etree_parse, xml_etree_process, json_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-1f7ad74 |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_xml     | 59.0 ms                                                               | 58.1 ms: 1.02x faster                                                     |
| mako           | 10.0 ms                                                               | 10.0 ms: 1.00x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                              |

Benchmark hidden because not significant (2): django_template, genshi_text

All benchmarks:
===============

| Benchmark               | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-1f7ad74 |
|-------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| gc_traversal            | 4.04 ms                                                               | 3.83 ms: 1.05x faster                                                     |
| pickle_list             | 5.23 us                                                               | 5.05 us: 1.04x faster                                                     |
| nbody                   | 84.0 ms                                                               | 81.8 ms: 1.03x faster                                                     |
| mdp                     | 2.63 sec                                                              | 2.58 sec: 1.02x faster                                                    |
| fannkuch                | 356 ms                                                                | 350 ms: 1.02x faster                                                      |
| nqueens                 | 87.3 ms                                                               | 85.7 ms: 1.02x faster                                                     |
| pickle                  | 12.2 us                                                               | 12.0 us: 1.02x faster                                                     |
| genshi_xml              | 59.0 ms                                                               | 58.1 ms: 1.02x faster                                                     |
| json_dumps              | 10.4 ms                                                               | 10.3 ms: 1.01x faster                                                     |
| pyflate                 | 452 ms                                                                | 446 ms: 1.01x faster                                                      |
| xml_etree_generate      | 82.0 ms                                                               | 81.3 ms: 1.01x faster                                                     |
| generators              | 30.8 ms                                                               | 30.5 ms: 1.01x faster                                                     |
| async_generators        | 465 ms                                                                | 462 ms: 1.01x faster                                                      |
| sqlite_synth            | 2.85 us                                                               | 2.84 us: 1.01x faster                                                     |
| sqlglot_optimize        | 57.3 ms                                                               | 57.0 ms: 1.01x faster                                                     |
| mako                    | 10.0 ms                                                               | 10.0 ms: 1.00x faster                                                     |
| hexiom                  | 6.61 ms                                                               | 6.59 ms: 1.00x faster                                                     |
| spectral_norm           | 102 ms                                                                | 102 ms: 1.00x faster                                                      |
| asyncio_tcp_ssl         | 1.85 sec                                                              | 1.85 sec: 1.00x slower                                                    |
| asyncio_tcp             | 515 ms                                                                | 517 ms: 1.00x slower                                                      |
| coroutines              | 22.9 ms                                                               | 23.0 ms: 1.00x slower                                                     |
| regex_compile           | 138 ms                                                                | 138 ms: 1.00x slower                                                      |
| pidigits                | 188 ms                                                                | 189 ms: 1.00x slower                                                      |
| sympy_str               | 302 ms                                                                | 303 ms: 1.01x slower                                                      |
| bench_mp_pool           | 24.0 ms                                                               | 24.1 ms: 1.01x slower                                                     |
| unpickle_list           | 5.39 us                                                               | 5.43 us: 1.01x slower                                                     |
| comprehensions          | 16.7 us                                                               | 16.8 us: 1.01x slower                                                     |
| meteor_contest          | 108 ms                                                                | 109 ms: 1.01x slower                                                      |
| pathlib                 | 16.4 ms                                                               | 16.6 ms: 1.01x slower                                                     |
| coverage                | 92.9 ms                                                               | 93.8 ms: 1.01x slower                                                     |
| sympy_expand            | 510 ms                                                                | 515 ms: 1.01x slower                                                      |
| thrift                  | 810 us                                                                | 818 us: 1.01x slower                                                      |
| sqlglot_transpile       | 1.64 ms                                                               | 1.66 ms: 1.01x slower                                                     |
| tomli_loads             | 1.93 sec                                                              | 1.95 sec: 1.01x slower                                                    |
| 2to3                    | 277 ms                                                                | 280 ms: 1.01x slower                                                      |
| sympy_integrate         | 22.5 ms                                                               | 22.7 ms: 1.01x slower                                                     |
| float                   | 72.3 ms                                                               | 73.0 ms: 1.01x slower                                                     |
| logging_silent          | 107 ns                                                                | 108 ns: 1.01x slower                                                      |
| go                      | 146 ms                                                                | 148 ms: 1.01x slower                                                      |
| bench_thread_pool       | 873 us                                                                | 882 us: 1.01x slower                                                      |
| sqlglot_parse           | 1.30 ms                                                               | 1.32 ms: 1.01x slower                                                     |
| docutils                | 2.93 sec                                                              | 2.97 sec: 1.01x slower                                                    |
| pprint_pformat          | 1.47 sec                                                              | 1.49 sec: 1.01x slower                                                    |
| scimark_sparse_mat_mult | 4.49 ms                                                               | 4.55 ms: 1.01x slower                                                     |
| deepcopy_reduce         | 3.30 us                                                               | 3.36 us: 1.02x slower                                                     |
| pickle_pure_python      | 298 us                                                                | 305 us: 1.02x slower                                                      |
| deltablue               | 3.70 ms                                                               | 3.82 ms: 1.03x slower                                                     |
| richards_super          | 47.6 ms                                                               | 49.2 ms: 1.03x slower                                                     |
| regex_dna               | 230 ms                                                                | 238 ms: 1.03x slower                                                      |
| richards                | 41.1 ms                                                               | 42.5 ms: 1.04x slower                                                     |
| html5lib                | 66.6 ms                                                               | 69.5 ms: 1.04x slower                                                     |
| pycparser               | 1.15 sec                                                              | 1.22 sec: 1.06x slower                                                    |
| scimark_sor             | 129 ms                                                                | 138 ms: 1.07x slower                                                      |
| regex_v8                | 24.5 ms                                                               | 26.6 ms: 1.08x slower                                                     |
| regex_effbot            | 3.65 ms                                                               | 4.01 ms: 1.10x slower                                                     |
| Geometric mean          | (ref)                                                                 | 1.00x slower                                                              |

Benchmark hidden because not significant (41): pickle_dict, chaos, async_tree_io_tg, deepcopy_memo, deepcopy, async_tree_none, telco, django_template, logging_simple, unpickle, async_tree_none_tg, dulwich_log, logging_format, scimark_fft, genshi_text, xml_etree_iterparse, python_startup_no_site, xml_etree_parse, create_gc_cycles, asyncio_websockets, sqlglot_normalize, python_startup, xml_etree_process, async_tree_memoization_tg, scimark_monte_carlo, scimark_lu, async_tree_io, tornado_http, dask, crypto_pyaes, typing_runtime_protocols, json, sympy_sum, async_tree_cpu_io_mixed, raytrace, json_loads, async_tree_cpu_io_mixed_tg, unpickle_pure_python, pprint_safe_repr, pylint, async_tree_memoization

# HPT report

- Reliability score: 99.59% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x