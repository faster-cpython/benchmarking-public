# Results vs. base

- fork: brandtbucher
- ref: justin_compact
- machine: linux-x86_64
- commit hash: e04d5ab
- commit date: 2024-06-19
- overall geometric mean: 1.01x faster
- HPT reliability: 99.62%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| html5lib       | 69.0 ms                                                               | 67.2 ms: 1.03x faster                                                 |
| tornado_http   | 96.8 ms                                                               | 96.3 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                          |

Benchmark hidden because not significant (2): 2to3, docutils

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_none, async_tree_io_tg, async_tree_none_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_memoization_tg, async_tree_io, async_tree_cpu_io_mixed

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| float          | 72.4 ms                                                               | 71.8 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 24.4 ms                                                               | 23.8 ms: 1.03x faster                                                 |
| regex_compile  | 138 ms                                                                | 136 ms: 1.01x faster                                                  |
| regex_dna      | 228 ms                                                                | 230 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                          |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_dict          | 37.2 us                                                               | 35.6 us: 1.04x faster                                                 |
| pickle_list          | 5.34 us                                                               | 5.12 us: 1.04x faster                                                 |
| json_loads           | 29.2 us                                                               | 28.7 us: 1.02x faster                                                 |
| xml_etree_process    | 59.1 ms                                                               | 58.3 ms: 1.01x faster                                                 |
| xml_etree_generate   | 82.0 ms                                                               | 82.3 ms: 1.00x slower                                                 |
| xml_etree_iterparse  | 101 ms                                                                | 102 ms: 1.01x slower                                                  |
| unpickle_pure_python | 222 us                                                                | 224 us: 1.01x slower                                                  |
| pickle_pure_python   | 297 us                                                                | 301 us: 1.01x slower                                                  |
| Geometric mean       | (ref)                                                                 | 1.01x faster                                                          |

Benchmark hidden because not significant (6): unpickle_list, xml_etree_parse, tomli_loads, pickle, json_dumps, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                               | 11.1 ms: 1.00x faster                                                 |
| python_startup_no_site | 7.64 ms                                                               | 7.63 ms: 1.00x faster                                                 |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml      | 59.2 ms                                                               | 56.3 ms: 1.05x faster                                                 |
| django_template | 37.1 ms                                                               | 36.2 ms: 1.03x faster                                                 |
| genshi_text     | 25.2 ms                                                               | 24.7 ms: 1.02x faster                                                 |
| mako            | 10.1 ms                                                               | 10.0 ms: 1.00x faster                                                 |
| Geometric mean  | (ref)                                                                 | 1.02x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| scimark_sor             | 139 ms                                                                | 129 ms: 1.08x faster                                                  |
| genshi_xml              | 59.2 ms                                                               | 56.3 ms: 1.05x faster                                                 |
| pickle_dict             | 37.2 us                                                               | 35.6 us: 1.04x faster                                                 |
| pickle_list             | 5.34 us                                                               | 5.12 us: 1.04x faster                                                 |
| pycparser               | 1.20 sec                                                              | 1.16 sec: 1.04x faster                                                |
| coroutines              | 23.7 ms                                                               | 23.0 ms: 1.03x faster                                                 |
| pyflate                 | 458 ms                                                                | 445 ms: 1.03x faster                                                  |
| scimark_sparse_mat_mult | 4.55 ms                                                               | 4.43 ms: 1.03x faster                                                 |
| regex_v8                | 24.4 ms                                                               | 23.8 ms: 1.03x faster                                                 |
| spectral_norm           | 105 ms                                                                | 102 ms: 1.03x faster                                                  |
| html5lib                | 69.0 ms                                                               | 67.2 ms: 1.03x faster                                                 |
| django_template         | 37.1 ms                                                               | 36.2 ms: 1.03x faster                                                 |
| deepcopy_reduce         | 2.83 us                                                               | 2.77 us: 1.02x faster                                                 |
| scimark_fft             | 317 ms                                                                | 310 ms: 1.02x faster                                                  |
| json_loads              | 29.2 us                                                               | 28.7 us: 1.02x faster                                                 |
| genshi_text             | 25.2 ms                                                               | 24.7 ms: 1.02x faster                                                 |
| comprehensions          | 16.8 us                                                               | 16.5 us: 1.02x faster                                                 |
| raytrace                | 283 ms                                                                | 279 ms: 1.02x faster                                                  |
| telco                   | 8.15 ms                                                               | 8.03 ms: 1.01x faster                                                 |
| scimark_lu              | 126 ms                                                                | 125 ms: 1.01x faster                                                  |
| logging_simple          | 5.65 us                                                               | 5.57 us: 1.01x faster                                                 |
| xml_etree_process       | 59.1 ms                                                               | 58.3 ms: 1.01x faster                                                 |
| richards                | 43.3 ms                                                               | 42.8 ms: 1.01x faster                                                 |
| regex_compile           | 138 ms                                                                | 136 ms: 1.01x faster                                                  |
| sympy_expand            | 514 ms                                                                | 508 ms: 1.01x faster                                                  |
| sympy_str               | 304 ms                                                                | 301 ms: 1.01x faster                                                  |
| logging_format          | 6.23 us                                                               | 6.17 us: 1.01x faster                                                 |
| coverage                | 96.2 ms                                                               | 95.3 ms: 1.01x faster                                                 |
| crypto_pyaes            | 67.6 ms                                                               | 67.1 ms: 1.01x faster                                                 |
| float                   | 72.4 ms                                                               | 71.8 ms: 1.01x faster                                                 |
| generators              | 30.2 ms                                                               | 30.0 ms: 1.01x faster                                                 |
| chaos                   | 59.8 ms                                                               | 59.4 ms: 1.01x faster                                                 |
| tornado_http            | 96.8 ms                                                               | 96.3 ms: 1.01x faster                                                 |
| fannkuch                | 358 ms                                                                | 356 ms: 1.01x faster                                                  |
| pathlib                 | 16.4 ms                                                               | 16.3 ms: 1.00x faster                                                 |
| bench_thread_pool       | 858 us                                                                | 854 us: 1.00x faster                                                  |
| meteor_contest          | 109 ms                                                                | 108 ms: 1.00x faster                                                  |
| mako                    | 10.1 ms                                                               | 10.0 ms: 1.00x faster                                                 |
| python_startup          | 11.2 ms                                                               | 11.1 ms: 1.00x faster                                                 |
| python_startup_no_site  | 7.64 ms                                                               | 7.63 ms: 1.00x faster                                                 |
| xml_etree_generate      | 82.0 ms                                                               | 82.3 ms: 1.00x slower                                                 |
| sqlglot_transpile       | 1.64 ms                                                               | 1.65 ms: 1.00x slower                                                 |
| go                      | 148 ms                                                                | 149 ms: 1.00x slower                                                  |
| asyncio_tcp             | 513 ms                                                                | 516 ms: 1.00x slower                                                  |
| richards_super          | 49.1 ms                                                               | 49.4 ms: 1.01x slower                                                 |
| sqlglot_normalize       | 114 ms                                                                | 115 ms: 1.01x slower                                                  |
| deltablue               | 3.66 ms                                                               | 3.69 ms: 1.01x slower                                                 |
| sqlglot_optimize        | 56.8 ms                                                               | 57.2 ms: 1.01x slower                                                 |
| thrift                  | 826 us                                                                | 833 us: 1.01x slower                                                  |
| xml_etree_iterparse     | 101 ms                                                                | 102 ms: 1.01x slower                                                  |
| regex_dna               | 228 ms                                                                | 230 ms: 1.01x slower                                                  |
| pprint_safe_repr        | 714 ms                                                                | 722 ms: 1.01x slower                                                  |
| nqueens                 | 85.8 ms                                                               | 86.8 ms: 1.01x slower                                                 |
| unpickle_pure_python    | 222 us                                                                | 224 us: 1.01x slower                                                  |
| pickle_pure_python      | 297 us                                                                | 301 us: 1.01x slower                                                  |
| bpe_tokeniser           | 4.87 sec                                                              | 4.94 sec: 1.01x slower                                                |
| async_generators        | 463 ms                                                                | 471 ms: 1.02x slower                                                  |
| sqlite_synth            | 2.83 us                                                               | 2.89 us: 1.02x slower                                                 |
| logging_silent          | 107 ns                                                                | 110 ns: 1.03x slower                                                  |
| mdp                     | 2.65 sec                                                              | 2.77 sec: 1.05x slower                                                |
| Geometric mean          | (ref)                                                                 | 1.01x faster                                                          |

Benchmark hidden because not significant (37): async_tree_none, async_tree_io_tg, pprint_pformat, scimark_monte_carlo, sqlglot_parse, async_tree_none_tg, deepcopy, bench_mp_pool, unpickle_list, xml_etree_parse, async_tree_memoization, nbody, async_tree_cpu_io_mixed_tg, dulwich_log, gc_traversal, json, asyncio_tcp_ssl, pidigits, deepcopy_memo, 2to3, async_tree_memoization_tg, create_gc_cycles, asyncio_websockets, tomli_loads, sympy_integrate, pickle, async_tree_io, pylint, docutils, typing_runtime_protocols, sympy_sum, hexiom, json_dumps, regex_effbot, async_tree_cpu_io_mixed, dask, unpickle

# HPT report

- Reliability score: 99.62% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x