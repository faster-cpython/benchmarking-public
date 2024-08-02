# Results vs. base

- fork: brandtbucher
- ref: no_trace_too_short
- machine: linux-x86_64
- commit hash: ea1e85d
- commit date: 2024-06-06
- overall geometric mean: 1.01x slower
- HPT reliability: 91.81%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-ea1e85d |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 277 ms                                                                | 281 ms: 1.02x slower                                                      |
| html5lib       | 66.6 ms                                                               | 68.7 ms: 1.03x slower                                                     |
| tornado_http   | 96.7 ms                                                               | 97.1 ms: 1.00x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                              |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_none, async_tree_none_tg, async_tree_memoization_tg, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_io, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-ea1e85d |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| nbody          | 84.0 ms                                                               | 80.5 ms: 1.04x faster                                                     |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                              |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-ea1e85d |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 230 ms                                                                | 226 ms: 1.02x faster                                                      |
| regex_v8       | 24.5 ms                                                               | 24.1 ms: 1.02x faster                                                     |
| regex_effbot   | 3.65 ms                                                               | 3.68 ms: 1.01x slower                                                     |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                              |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-ea1e85d |
|--------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| unpickle_list      | 5.39 us                                                               | 5.20 us: 1.04x faster                                                     |
| xml_etree_generate | 82.0 ms                                                               | 81.4 ms: 1.01x faster                                                     |
| json_dumps         | 10.4 ms                                                               | 10.5 ms: 1.01x slower                                                     |
| json_loads         | 28.7 us                                                               | 29.0 us: 1.01x slower                                                     |
| pickle_dict        | 35.7 us                                                               | 36.3 us: 1.02x slower                                                     |
| pickle_pure_python | 298 us                                                                | 303 us: 1.02x slower                                                      |
| tomli_loads        | 1.93 sec                                                              | 1.96 sec: 1.02x slower                                                    |
| pickle_list        | 5.23 us                                                               | 5.34 us: 1.02x slower                                                     |
| Geometric mean     | (ref)                                                                 | 1.00x slower                                                              |

Benchmark hidden because not significant (6): unpickle, xml_etree_process, pickle, unpickle_pure_python, xml_etree_parse, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-ea1e85d |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 11.1 ms: 1.00x faster                                                     |
| python_startup_no_site | 7.62 ms                                                               | 7.60 ms: 1.00x faster                                                     |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-ea1e85d |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| django_template | 37.0 ms                                                               | 36.2 ms: 1.02x faster                                                     |
| genshi_xml      | 59.0 ms                                                               | 59.8 ms: 1.01x slower                                                     |
| Geometric mean  | (ref)                                                                 | 1.00x faster                                                              |

Benchmark hidden because not significant (2): mako, genshi_text

All benchmarks:
===============

| Benchmark              | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240606-linux-x86_64-brandtbucher-no_trace_too_short-3.14.0a0-ea1e85d |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| gc_traversal           | 4.04 ms                                                               | 3.84 ms: 1.05x faster                                                     |
| nbody                  | 84.0 ms                                                               | 80.5 ms: 1.04x faster                                                     |
| unpickle_list          | 5.39 us                                                               | 5.20 us: 1.04x faster                                                     |
| django_template        | 37.0 ms                                                               | 36.2 ms: 1.02x faster                                                     |
| regex_dna              | 230 ms                                                                | 226 ms: 1.02x faster                                                      |
| mdp                    | 2.63 sec                                                              | 2.58 sec: 1.02x faster                                                    |
| regex_v8               | 24.5 ms                                                               | 24.1 ms: 1.02x faster                                                     |
| logging_format         | 6.32 us                                                               | 6.22 us: 1.02x faster                                                     |
| pprint_pformat         | 1.47 sec                                                              | 1.45 sec: 1.01x faster                                                    |
| spectral_norm          | 102 ms                                                                | 101 ms: 1.01x faster                                                      |
| deepcopy               | 376 us                                                                | 372 us: 1.01x faster                                                      |
| coroutines             | 22.9 ms                                                               | 22.7 ms: 1.01x faster                                                     |
| scimark_lu             | 126 ms                                                                | 125 ms: 1.01x faster                                                      |
| logging_simple         | 5.69 us                                                               | 5.65 us: 1.01x faster                                                     |
| xml_etree_generate     | 82.0 ms                                                               | 81.4 ms: 1.01x faster                                                     |
| pyflate                | 452 ms                                                                | 449 ms: 1.01x faster                                                      |
| sqlite_synth           | 2.85 us                                                               | 2.84 us: 1.01x faster                                                     |
| fannkuch               | 356 ms                                                                | 355 ms: 1.00x faster                                                      |
| async_generators       | 465 ms                                                                | 462 ms: 1.00x faster                                                      |
| sqlglot_transpile      | 1.64 ms                                                               | 1.63 ms: 1.00x faster                                                     |
| logging_silent         | 107 ns                                                                | 107 ns: 1.00x faster                                                      |
| python_startup         | 11.2 ms                                                               | 11.1 ms: 1.00x faster                                                     |
| python_startup_no_site | 7.62 ms                                                               | 7.60 ms: 1.00x faster                                                     |
| sympy_integrate        | 22.5 ms                                                               | 22.6 ms: 1.00x slower                                                     |
| tornado_http           | 96.7 ms                                                               | 97.1 ms: 1.00x slower                                                     |
| hexiom                 | 6.61 ms                                                               | 6.64 ms: 1.01x slower                                                     |
| bench_thread_pool      | 873 us                                                                | 878 us: 1.01x slower                                                      |
| richards_super         | 47.6 ms                                                               | 47.9 ms: 1.01x slower                                                     |
| sqlglot_normalize      | 114 ms                                                                | 114 ms: 1.01x slower                                                      |
| asyncio_tcp_ssl        | 1.85 sec                                                              | 1.87 sec: 1.01x slower                                                    |
| dulwich_log            | 68.5 ms                                                               | 68.9 ms: 1.01x slower                                                     |
| json_dumps             | 10.4 ms                                                               | 10.5 ms: 1.01x slower                                                     |
| regex_effbot           | 3.65 ms                                                               | 3.68 ms: 1.01x slower                                                     |
| crypto_pyaes           | 67.7 ms                                                               | 68.4 ms: 1.01x slower                                                     |
| richards               | 41.1 ms                                                               | 41.5 ms: 1.01x slower                                                     |
| scimark_monte_carlo    | 62.6 ms                                                               | 63.3 ms: 1.01x slower                                                     |
| json_loads             | 28.7 us                                                               | 29.0 us: 1.01x slower                                                     |
| genshi_xml             | 59.0 ms                                                               | 59.8 ms: 1.01x slower                                                     |
| asyncio_tcp            | 515 ms                                                                | 523 ms: 1.02x slower                                                      |
| pickle_dict            | 35.7 us                                                               | 36.3 us: 1.02x slower                                                     |
| pickle_pure_python     | 298 us                                                                | 303 us: 1.02x slower                                                      |
| 2to3                   | 277 ms                                                                | 281 ms: 1.02x slower                                                      |
| thrift                 | 810 us                                                                | 824 us: 1.02x slower                                                      |
| tomli_loads            | 1.93 sec                                                              | 1.96 sec: 1.02x slower                                                    |
| go                     | 146 ms                                                                | 149 ms: 1.02x slower                                                      |
| pickle_list            | 5.23 us                                                               | 5.34 us: 1.02x slower                                                     |
| deepcopy_reduce        | 3.30 us                                                               | 3.38 us: 1.02x slower                                                     |
| scimark_fft            | 319 ms                                                                | 327 ms: 1.03x slower                                                      |
| html5lib               | 66.6 ms                                                               | 68.7 ms: 1.03x slower                                                     |
| scimark_sor            | 129 ms                                                                | 137 ms: 1.07x slower                                                      |
| generators             | 30.8 ms                                                               | 49.4 ms: 1.61x slower                                                     |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                              |

Benchmark hidden because not significant (45): chaos, pprint_safe_repr, unpickle, sqlglot_parse, async_tree_none, mako, deepcopy_memo, xml_etree_process, nqueens, pycparser, float, pickle, create_gc_cycles, scimark_sparse_mat_mult, comprehensions, genshi_text, sympy_sum, coverage, dask, async_tree_none_tg, sympy_str, asyncio_websockets, meteor_contest, sqlglot_optimize, regex_compile, raytrace, pathlib, sympy_expand, unpickle_pure_python, pidigits, bench_mp_pool, docutils, typing_runtime_protocols, async_tree_memoization_tg, xml_etree_parse, telco, xml_etree_iterparse, async_tree_io_tg, async_tree_cpu_io_mixed, json, async_tree_cpu_io_mixed_tg, pylint, async_tree_io, deltablue, async_tree_memoization

# HPT report

- Reliability score: 91.81% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x