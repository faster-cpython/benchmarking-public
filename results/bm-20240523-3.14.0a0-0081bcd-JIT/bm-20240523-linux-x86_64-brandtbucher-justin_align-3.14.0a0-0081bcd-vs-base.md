# Results vs. base

- fork: brandtbucher
- ref: justin_align
- machine: linux-x86_64
- commit hash: 0081bcd
- commit date: 2024-05-23
- overall geometric mean: 1.00x faster
- HPT reliability: 52.33%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240522-linux-x86_64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-linux-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 279 ms                                                                | 280 ms: 1.00x slower                                                |
| html5lib       | 66.8 ms                                                               | 68.0 ms: 1.02x slower                                               |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                        |

Benchmark hidden because not significant (3): chameleon, docutils, tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_memoization, async_tree_io_tg, async_tree_memoization_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_none_tg, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240522-linux-x86_64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-linux-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| nbody          | 82.4 ms                                                               | 80.3 ms: 1.03x faster                                               |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                        |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240522-linux-x86_64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-linux-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_dna      | 234 ms                                                                | 230 ms: 1.01x faster                                                |
| regex_compile  | 139 ms                                                                | 138 ms: 1.01x faster                                                |
| regex_v8       | 25.3 ms                                                               | 25.7 ms: 1.02x slower                                               |
| regex_effbot   | 3.81 ms                                                               | 3.94 ms: 1.03x slower                                               |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240522-linux-x86_64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-linux-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|----------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pickle               | 12.1 us                                                               | 11.8 us: 1.03x faster                                               |
| unpickle_list        | 5.39 us                                                               | 5.28 us: 1.02x faster                                               |
| xml_etree_generate   | 83.3 ms                                                               | 82.8 ms: 1.01x faster                                               |
| json_loads           | 28.8 us                                                               | 28.6 us: 1.00x faster                                               |
| unpickle_pure_python | 221 us                                                                | 220 us: 1.00x faster                                                |
| xml_etree_process    | 58.2 ms                                                               | 58.6 ms: 1.01x slower                                               |
| tomli_loads          | 1.94 sec                                                              | 1.96 sec: 1.01x slower                                              |
| pickle_dict          | 34.3 us                                                               | 34.6 us: 1.01x slower                                               |
| unpickle             | 15.0 us                                                               | 15.8 us: 1.05x slower                                               |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                        |

Benchmark hidden because not significant (5): xml_etree_parse, pickle_pure_python, json_dumps, pickle_list, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240522-linux-x86_64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-linux-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 7.59 ms                                                               | 7.61 ms: 1.00x slower                                               |
| python_startup         | 10.9 ms                                                               | 10.9 ms: 1.00x slower                                               |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240522-linux-x86_64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-linux-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|-----------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mako            | 10.1 ms                                                               | 10.00 ms: 1.01x faster                                              |
| genshi_text     | 24.1 ms                                                               | 24.6 ms: 1.02x slower                                               |
| django_template | 36.1 ms                                                               | 36.9 ms: 1.02x slower                                               |
| genshi_xml      | 56.3 ms                                                               | 58.2 ms: 1.03x slower                                               |
| Geometric mean  | (ref)                                                                 | 1.02x slower                                                        |

All benchmarks:
===============

| Benchmark                | bm-20240522-linux-x86_64-python-d472b4f9fa4fb6061588-3.14.0a0-d472b4f | bm-20240523-linux-x86_64-brandtbucher-justin_align-3.14.0a0-0081bcd |
|--------------------------|:---------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                      | 2.76 sec                                                              | 2.59 sec: 1.07x faster                                              |
| pyflate                  | 455 ms                                                                | 437 ms: 1.04x faster                                                |
| pickle                   | 12.1 us                                                               | 11.8 us: 1.03x faster                                               |
| nbody                    | 82.4 ms                                                               | 80.3 ms: 1.03x faster                                               |
| typing_runtime_protocols | 173 us                                                                | 169 us: 1.02x faster                                                |
| logging_simple           | 5.75 us                                                               | 5.62 us: 1.02x faster                                               |
| logging_format           | 6.39 us                                                               | 6.26 us: 1.02x faster                                               |
| unpickle_list            | 5.39 us                                                               | 5.28 us: 1.02x faster                                               |
| fannkuch                 | 356 ms                                                                | 350 ms: 1.02x faster                                                |
| regex_dna                | 234 ms                                                                | 230 ms: 1.01x faster                                                |
| sqlite_synth             | 2.89 us                                                               | 2.85 us: 1.01x faster                                               |
| mako                     | 10.1 ms                                                               | 10.00 ms: 1.01x faster                                              |
| coroutines               | 23.2 ms                                                               | 23.0 ms: 1.01x faster                                               |
| telco                    | 8.23 ms                                                               | 8.16 ms: 1.01x faster                                               |
| meteor_contest           | 109 ms                                                                | 108 ms: 1.01x faster                                                |
| regex_compile            | 139 ms                                                                | 138 ms: 1.01x faster                                                |
| coverage                 | 93.3 ms                                                               | 92.7 ms: 1.01x faster                                               |
| xml_etree_generate       | 83.3 ms                                                               | 82.8 ms: 1.01x faster                                               |
| sympy_integrate          | 22.6 ms                                                               | 22.4 ms: 1.01x faster                                               |
| hexiom                   | 6.62 ms                                                               | 6.58 ms: 1.01x faster                                               |
| json_loads               | 28.8 us                                                               | 28.6 us: 1.00x faster                                               |
| richards_super           | 47.5 ms                                                               | 47.3 ms: 1.00x faster                                               |
| unpickle_pure_python     | 221 us                                                                | 220 us: 1.00x faster                                                |
| sqlglot_optimize         | 56.6 ms                                                               | 56.4 ms: 1.00x faster                                               |
| bench_thread_pool        | 866 us                                                                | 864 us: 1.00x faster                                                |
| asyncio_tcp_ssl          | 1.86 sec                                                              | 1.86 sec: 1.00x faster                                              |
| logging_silent           | 106 ns                                                                | 107 ns: 1.00x slower                                                |
| 2to3                     | 279 ms                                                                | 280 ms: 1.00x slower                                                |
| python_startup_no_site   | 7.59 ms                                                               | 7.61 ms: 1.00x slower                                               |
| python_startup           | 10.9 ms                                                               | 10.9 ms: 1.00x slower                                               |
| create_gc_cycles         | 1.81 ms                                                               | 1.82 ms: 1.01x slower                                               |
| xml_etree_process        | 58.2 ms                                                               | 58.6 ms: 1.01x slower                                               |
| tomli_loads              | 1.94 sec                                                              | 1.96 sec: 1.01x slower                                              |
| pickle_dict              | 34.3 us                                                               | 34.6 us: 1.01x slower                                               |
| scimark_fft              | 311 ms                                                                | 314 ms: 1.01x slower                                                |
| comprehensions           | 16.6 us                                                               | 16.8 us: 1.01x slower                                               |
| pprint_safe_repr         | 703 ms                                                                | 711 ms: 1.01x slower                                                |
| deepcopy                 | 367 us                                                                | 372 us: 1.01x slower                                                |
| regex_v8                 | 25.3 ms                                                               | 25.7 ms: 1.02x slower                                               |
| scimark_lu               | 123 ms                                                                | 126 ms: 1.02x slower                                                |
| html5lib                 | 66.8 ms                                                               | 68.0 ms: 1.02x slower                                               |
| genshi_text              | 24.1 ms                                                               | 24.6 ms: 1.02x slower                                               |
| django_template          | 36.1 ms                                                               | 36.9 ms: 1.02x slower                                               |
| regex_effbot             | 3.81 ms                                                               | 3.94 ms: 1.03x slower                                               |
| genshi_xml               | 56.3 ms                                                               | 58.2 ms: 1.03x slower                                               |
| scimark_sparse_mat_mult  | 4.39 ms                                                               | 4.59 ms: 1.05x slower                                               |
| unpickle                 | 15.0 us                                                               | 15.8 us: 1.05x slower                                               |
| gc_traversal             | 3.66 ms                                                               | 3.86 ms: 1.05x slower                                               |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                        |

Benchmark hidden because not significant (50): async_tree_memoization, deepcopy_memo, xml_etree_parse, pickle_pure_python, async_tree_io_tg, async_tree_memoization_tg, deltablue, scimark_monte_carlo, flaskblogging, async_tree_cpu_io_mixed, nqueens, deepcopy_reduce, sqlglot_parse, dulwich_log, json_dumps, spectral_norm, async_tree_cpu_io_mixed_tg, json, pylint, go, bench_mp_pool, raytrace, sqlglot_normalize, crypto_pyaes, sympy_sum, chameleon, pidigits, tornado_http, pycparser, asyncio_tcp, chaos, sympy_expand, asyncio_websockets, dask, pickle_list, docutils, async_tree_none, scimark_sor, sympy_str, generators, async_generators, float, xml_etree_iterparse, sqlglot_transpile, async_tree_none_tg, thrift, pathlib, richards, pprint_pformat, async_tree_io

# HPT report

- Reliability score: 52.33% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x