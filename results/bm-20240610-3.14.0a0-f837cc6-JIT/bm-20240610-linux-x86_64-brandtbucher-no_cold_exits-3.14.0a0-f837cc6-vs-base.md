# Results vs. base

- fork: brandtbucher
- ref: no_cold_exits
- machine: linux-x86_64
- commit hash: f837cc6
- commit date: 2024-06-10
- overall geometric mean: 1.00x faster
- HPT reliability: 99.74%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 279 ms                                                                | 277 ms: 1.01x faster                                                 |
| docutils       | 2.95 sec                                                              | 2.93 sec: 1.01x faster                                               |
| html5lib       | 67.3 ms                                                               | 68.5 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                         |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, async_tree_memoization_tg, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_none_tg, async_tree_io, async_tree_io_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| nbody          | 81.6 ms                                                               | 82.5 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                         |

Benchmark hidden because not significant (2): float, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot   | 3.81 ms                                                               | 3.55 ms: 1.07x faster                                                |
| regex_v8       | 24.9 ms                                                               | 24.4 ms: 1.02x faster                                                |
| regex_compile  | 138 ms                                                                | 136 ms: 1.01x faster                                                 |
| regex_dna      | 228 ms                                                                | 226 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| tomli_loads          | 1.96 sec                                                              | 1.92 sec: 1.02x faster                                               |
| json_loads           | 29.2 us                                                               | 28.9 us: 1.01x faster                                                |
| pickle_pure_python   | 300 us                                                                | 297 us: 1.01x faster                                                 |
| pickle               | 12.1 us                                                               | 12.0 us: 1.01x faster                                                |
| unpickle_pure_python | 223 us                                                                | 222 us: 1.00x faster                                                 |
| json_dumps           | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                |
| xml_etree_process    | 58.3 ms                                                               | 59.0 ms: 1.01x slower                                                |
| xml_etree_generate   | 81.2 ms                                                               | 82.2 ms: 1.01x slower                                                |
| unpickle_list        | 5.30 us                                                               | 5.44 us: 1.03x slower                                                |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                         |

Benchmark hidden because not significant (5): xml_etree_iterparse, pickle_list, pickle_dict, unpickle, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 7.59 ms                                                               | 7.20 ms: 1.05x faster                                                |
| python_startup         | 11.1 ms                                                               | 10.8 ms: 1.03x faster                                                |
| Geometric mean         | (ref)                                                                 | 1.04x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako           | 9.95 ms                                                               | 9.83 ms: 1.01x faster                                                |
| genshi_xml     | 57.3 ms                                                               | 58.2 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                         |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark               | bm-20240605-linux-x86_64-python-e83ce850f433fd8bbf8f-3.14.0a0-e83ce85 | bm-20240610-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-f837cc6 |
|-------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_effbot            | 3.81 ms                                                               | 3.55 ms: 1.07x faster                                                |
| python_startup_no_site  | 7.59 ms                                                               | 7.20 ms: 1.05x faster                                                |
| scimark_sparse_mat_mult | 4.64 ms                                                               | 4.41 ms: 1.05x faster                                                |
| pycparser               | 1.20 sec                                                              | 1.14 sec: 1.05x faster                                               |
| deepcopy_memo           | 39.1 us                                                               | 37.8 us: 1.03x faster                                                |
| deepcopy_reduce         | 3.41 us                                                               | 3.30 us: 1.03x faster                                                |
| python_startup          | 11.1 ms                                                               | 10.8 ms: 1.03x faster                                                |
| json                    | 5.45 ms                                                               | 5.32 ms: 1.02x faster                                                |
| go                      | 151 ms                                                                | 147 ms: 1.02x faster                                                 |
| tomli_loads             | 1.96 sec                                                              | 1.92 sec: 1.02x faster                                               |
| regex_v8                | 24.9 ms                                                               | 24.4 ms: 1.02x faster                                                |
| spectral_norm           | 103 ms                                                                | 101 ms: 1.02x faster                                                 |
| sympy_expand            | 514 ms                                                                | 507 ms: 1.01x faster                                                 |
| regex_compile           | 138 ms                                                                | 136 ms: 1.01x faster                                                 |
| raytrace                | 281 ms                                                                | 277 ms: 1.01x faster                                                 |
| regex_dna               | 228 ms                                                                | 226 ms: 1.01x faster                                                 |
| json_loads              | 29.2 us                                                               | 28.9 us: 1.01x faster                                                |
| coverage                | 93.9 ms                                                               | 92.8 ms: 1.01x faster                                                |
| mako                    | 9.95 ms                                                               | 9.83 ms: 1.01x faster                                                |
| pickle_pure_python      | 300 us                                                                | 297 us: 1.01x faster                                                 |
| richards_super          | 47.8 ms                                                               | 47.3 ms: 1.01x faster                                                |
| crypto_pyaes            | 68.4 ms                                                               | 67.7 ms: 1.01x faster                                                |
| sympy_str               | 302 ms                                                                | 299 ms: 1.01x faster                                                 |
| pickle                  | 12.1 us                                                               | 12.0 us: 1.01x faster                                                |
| docutils                | 2.95 sec                                                              | 2.93 sec: 1.01x faster                                               |
| pathlib                 | 16.4 ms                                                               | 16.3 ms: 1.01x faster                                                |
| comprehensions          | 16.7 us                                                               | 16.6 us: 1.01x faster                                                |
| 2to3                    | 279 ms                                                                | 277 ms: 1.01x faster                                                 |
| async_generators        | 467 ms                                                                | 464 ms: 1.01x faster                                                 |
| sqlglot_optimize        | 57.1 ms                                                               | 56.8 ms: 1.00x faster                                                |
| sqlglot_normalize       | 113 ms                                                                | 113 ms: 1.00x faster                                                 |
| sympy_sum               | 172 ms                                                                | 171 ms: 1.00x faster                                                 |
| unpickle_pure_python    | 223 us                                                                | 222 us: 1.00x faster                                                 |
| generators              | 30.7 ms                                                               | 30.8 ms: 1.00x slower                                                |
| hexiom                  | 6.60 ms                                                               | 6.63 ms: 1.00x slower                                                |
| meteor_contest          | 108 ms                                                                | 108 ms: 1.01x slower                                                 |
| pyflate                 | 453 ms                                                                | 456 ms: 1.01x slower                                                 |
| json_dumps              | 10.3 ms                                                               | 10.4 ms: 1.01x slower                                                |
| sqlglot_transpile       | 1.63 ms                                                               | 1.64 ms: 1.01x slower                                                |
| mdp                     | 2.57 sec                                                              | 2.58 sec: 1.01x slower                                               |
| sqlite_synth            | 2.83 us                                                               | 2.86 us: 1.01x slower                                                |
| create_gc_cycles        | 1.79 ms                                                               | 1.81 ms: 1.01x slower                                                |
| fannkuch                | 354 ms                                                                | 358 ms: 1.01x slower                                                 |
| nbody                   | 81.6 ms                                                               | 82.5 ms: 1.01x slower                                                |
| xml_etree_process       | 58.3 ms                                                               | 59.0 ms: 1.01x slower                                                |
| xml_etree_generate      | 81.2 ms                                                               | 82.2 ms: 1.01x slower                                                |
| genshi_xml              | 57.3 ms                                                               | 58.2 ms: 1.01x slower                                                |
| html5lib                | 67.3 ms                                                               | 68.5 ms: 1.02x slower                                                |
| unpickle_list           | 5.30 us                                                               | 5.44 us: 1.03x slower                                                |
| asyncio_tcp             | 505 ms                                                                | 519 ms: 1.03x slower                                                 |
| gc_traversal            | 3.60 ms                                                               | 4.06 ms: 1.13x slower                                                |
| Geometric mean          | (ref)                                                                 | 1.00x faster                                                         |

Benchmark hidden because not significant (45): scimark_monte_carlo, pprint_safe_repr, dulwich_log, async_tree_cpu_io_mixed, deepcopy, telco, deltablue, logging_simple, async_tree_memoization_tg, dask, float, pprint_pformat, xml_etree_iterparse, scimark_sor, scimark_fft, bench_thread_pool, async_tree_cpu_io_mixed_tg, tornado_http, genshi_text, pickle_list, pickle_dict, async_tree_none, pylint, async_tree_none_tg, sympy_integrate, asyncio_websockets, asyncio_tcp_ssl, pidigits, logging_format, scimark_lu, bench_mp_pool, coroutines, thrift, nqueens, logging_silent, typing_runtime_protocols, unpickle, sqlglot_parse, django_template, xml_etree_parse, richards, async_tree_io, async_tree_io_tg, async_tree_memoization, chaos

# HPT report

- Reliability score: 99.74% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x