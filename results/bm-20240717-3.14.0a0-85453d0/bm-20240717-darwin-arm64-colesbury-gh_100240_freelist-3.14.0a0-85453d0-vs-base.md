# Results vs. base

- fork: colesbury
- ref: gh_100240_freelist
- machine: darwin-arm64
- commit hash: 85453d0
- commit date: 2024-07-17
- overall geometric mean: 1.00x faster
- HPT reliability: 59.10%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark           | bm-20240717-darwin-arm64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d | bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|---------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_eager    | 64.1 ms                                                               | 64.2 ms: 1.00x slower                                                  |
| async_tree_eager_tg | 41.5 ms                                                               | 42.3 ms: 1.02x slower                                                  |
| Geometric mean      | (ref)                                                                 | 1.00x slower                                                           |

Benchmark hidden because not significant (14): async_tree_io, async_tree_memoization, async_tree_io_tg, async_tree_memoization_tg, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_memoization_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_eager_io_tg, async_tree_eager_io, async_tree_eager_cpu_io_mixed, async_tree_none, async_tree_eager_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240717-darwin-arm64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d | bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 62.2 ms                                                               | 61.7 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                           |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240717-darwin-arm64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d | bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 68.3 ms                                                               | 68.6 ms: 1.00x slower                                                  |
| regex_v8       | 17.1 ms                                                               | 17.3 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                           |

Benchmark hidden because not significant (2): regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240717-darwin-arm64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d | bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|--------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse    | 108 ms                                                                | 106 ms: 1.01x faster                                                   |
| pickle_pure_python | 181 us                                                                | 180 us: 1.01x faster                                                   |
| xml_etree_generate | 53.1 ms                                                               | 53.2 ms: 1.00x slower                                                  |
| Geometric mean     | (ref)                                                                 | 1.00x faster                                                           |

Benchmark hidden because not significant (6): tomli_loads, xml_etree_iterparse, json_dumps, json_loads, xml_etree_process, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240717-darwin-arm64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d | bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 10.8 ms                                                               | 10.5 ms: 1.03x faster                                                  |
| python_startup         | 13.6 ms                                                               | 13.4 ms: 1.02x faster                                                  |
| Geometric mean         | (ref)                                                                 | 1.02x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240717-darwin-arm64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d | bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|-----------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 19.8 ms                                                               | 19.8 ms: 1.00x slower                                                  |
| genshi_xml      | 30.3 ms                                                               | 30.4 ms: 1.00x slower                                                  |
| genshi_text     | 14.0 ms                                                               | 14.0 ms: 1.00x slower                                                  |
| mako            | 7.05 ms                                                               | 7.13 ms: 1.01x slower                                                  |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                           |

All benchmarks:
===============

| Benchmark               | bm-20240717-darwin-arm64-python-f4bc84d261c828ed81f1-3.14.0a0-f4bc84d | bm-20240717-darwin-arm64-colesbury-gh_100240_freelist-3.14.0a0-85453d0 |
|-------------------------|:---------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site  | 10.8 ms                                                               | 10.5 ms: 1.03x faster                                                  |
| python_startup          | 13.6 ms                                                               | 13.4 ms: 1.02x faster                                                  |
| xml_etree_parse         | 108 ms                                                                | 106 ms: 1.01x faster                                                   |
| scimark_sparse_mat_mult | 2.89 ms                                                               | 2.86 ms: 1.01x faster                                                  |
| nbody                   | 62.2 ms                                                               | 61.7 ms: 1.01x faster                                                  |
| richards                | 31.4 ms                                                               | 31.2 ms: 1.01x faster                                                  |
| scimark_lu              | 70.7 ms                                                               | 70.2 ms: 1.01x faster                                                  |
| bench_thread_pool       | 453 us                                                                | 450 us: 1.01x faster                                                   |
| pickle_pure_python      | 181 us                                                                | 180 us: 1.01x faster                                                   |
| scimark_fft             | 187 ms                                                                | 186 ms: 1.01x faster                                                   |
| scimark_sor             | 96.5 ms                                                               | 96.0 ms: 1.00x faster                                                  |
| raytrace                | 149 ms                                                                | 148 ms: 1.00x faster                                                   |
| pprint_pformat          | 952 ms                                                                | 948 ms: 1.00x faster                                                   |
| logging_format          | 3.35 us                                                               | 3.33 us: 1.00x faster                                                  |
| deepcopy_reduce         | 1.50 us                                                               | 1.49 us: 1.00x faster                                                  |
| create_gc_cycles        | 896 us                                                                | 893 us: 1.00x faster                                                   |
| scimark_monte_carlo     | 43.3 ms                                                               | 43.2 ms: 1.00x faster                                                  |
| deltablue               | 2.10 ms                                                               | 2.09 ms: 1.00x faster                                                  |
| richards_super          | 34.3 ms                                                               | 34.2 ms: 1.00x faster                                                  |
| logging_simple          | 3.04 us                                                               | 3.03 us: 1.00x faster                                                  |
| xml_etree_generate      | 53.1 ms                                                               | 53.2 ms: 1.00x slower                                                  |
| django_template         | 19.8 ms                                                               | 19.8 ms: 1.00x slower                                                  |
| bpe_tokeniser           | 3.11 sec                                                              | 3.11 sec: 1.00x slower                                                 |
| sqlglot_parse           | 739 us                                                                | 741 us: 1.00x slower                                                   |
| async_tree_eager        | 64.1 ms                                                               | 64.2 ms: 1.00x slower                                                  |
| coroutines              | 16.2 ms                                                               | 16.2 ms: 1.00x slower                                                  |
| hexiom                  | 4.11 ms                                                               | 4.12 ms: 1.00x slower                                                  |
| sympy_integrate         | 10.4 ms                                                               | 10.4 ms: 1.00x slower                                                  |
| genshi_xml              | 30.3 ms                                                               | 30.4 ms: 1.00x slower                                                  |
| sqlglot_optimize        | 31.4 ms                                                               | 31.6 ms: 1.00x slower                                                  |
| genshi_text             | 14.0 ms                                                               | 14.0 ms: 1.00x slower                                                  |
| pyflate                 | 320 ms                                                                | 321 ms: 1.00x slower                                                   |
| sqlglot_transpile       | 899 us                                                                | 902 us: 1.00x slower                                                   |
| fannkuch                | 262 ms                                                                | 263 ms: 1.00x slower                                                   |
| asyncio_tcp_ssl         | 1.27 sec                                                              | 1.27 sec: 1.00x slower                                                 |
| sqlglot_normalize       | 169 ms                                                                | 170 ms: 1.00x slower                                                   |
| coverage                | 45.1 ms                                                               | 45.3 ms: 1.00x slower                                                  |
| regex_compile           | 68.3 ms                                                               | 68.6 ms: 1.00x slower                                                  |
| pathlib                 | 23.1 ms                                                               | 23.2 ms: 1.01x slower                                                  |
| mdp                     | 1.42 sec                                                              | 1.43 sec: 1.01x slower                                                 |
| comprehensions          | 10.8 us                                                               | 10.9 us: 1.01x slower                                                  |
| meteor_contest          | 71.2 ms                                                               | 71.7 ms: 1.01x slower                                                  |
| regex_v8                | 17.1 ms                                                               | 17.3 ms: 1.01x slower                                                  |
| logging_silent          | 59.1 ns                                                               | 59.6 ns: 1.01x slower                                                  |
| mako                    | 7.05 ms                                                               | 7.13 ms: 1.01x slower                                                  |
| async_tree_eager_tg     | 41.5 ms                                                               | 42.3 ms: 1.02x slower                                                  |
| Geometric mean          | (ref)                                                                 | 1.00x faster                                                           |

Benchmark hidden because not significant (51): async_tree_io, 2to3, float, async_tree_memoization, pycparser, tomli_loads, xml_etree_iterparse, async_tree_io_tg, html5lib, async_tree_memoization_tg, async_tree_none_tg, async_tree_cpu_io_mixed_tg, async_tree_eager_memoization_tg, async_tree_eager_cpu_io_mixed_tg, sympy_sum, async_tree_cpu_io_mixed, crypto_pyaes, async_generators, deepcopy, bench_mp_pool, generators, json_dumps, spectral_norm, telco, gc_traversal, sympy_str, nqueens, asyncio_websockets, chaos, pidigits, go, regex_dna, sympy_expand, json_loads, docutils, xml_etree_process, async_tree_eager_io_tg, async_tree_eager_io, thrift, pylint, pprint_safe_repr, deepcopy_memo, async_tree_eager_cpu_io_mixed, json, tornado_http, regex_effbot, typing_runtime_protocols, async_tree_none, unpickle_pure_python, async_tree_eager_memoization, asyncio_tcp

# HPT report

- Reliability score: 59.10% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x