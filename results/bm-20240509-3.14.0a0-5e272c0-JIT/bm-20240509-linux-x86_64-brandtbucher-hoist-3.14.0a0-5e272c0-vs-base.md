# Results vs. base

- fork: brandtbucher
- ref: hoist
- machine: linux-x86_64
- commit hash: 5e272c0
- commit date: 2024-05-09
- overall geometric mean: 1.00x faster
- HPT reliability: 95.50%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.01x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247 | bm-20240509-linux-x86_64-brandtbucher-hoist-3.14.0a0-5e272c0 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| docutils       | 2.96 sec                                                              | 2.97 sec: 1.00x slower                                       |
| html5lib       | 70.7 ms                                                               | 69.2 ms: 1.02x faster                                        |
| tornado_http   | 98.4 ms                                                               | 97.9 ms: 1.01x faster                                        |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                 |

Benchmark hidden because not significant (2): 2to3, chameleon

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_io_tg, async_tree_io, async_tree_memoization_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247 | bm-20240509-linux-x86_64-brandtbucher-hoist-3.14.0a0-5e272c0 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| nbody          | 84.0 ms                                                               | 81.0 ms: 1.04x faster                                        |
| pidigits       | 188 ms                                                                | 197 ms: 1.05x slower                                         |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                 |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247 | bm-20240509-linux-x86_64-brandtbucher-hoist-3.14.0a0-5e272c0 |
|----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| regex_dna      | 228 ms                                                                | 220 ms: 1.04x faster                                         |
| regex_v8       | 25.3 ms                                                               | 25.4 ms: 1.01x slower                                        |
| regex_effbot   | 3.68 ms                                                               | 3.82 ms: 1.04x slower                                        |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                 |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247 | bm-20240509-linux-x86_64-brandtbucher-hoist-3.14.0a0-5e272c0 |
|--------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| pickle_pure_python | 310 us                                                                | 304 us: 1.02x faster                                         |
| pickle_list        | 5.56 us                                                               | 5.47 us: 1.02x faster                                        |
| pickle_dict        | 34.7 us                                                               | 34.2 us: 1.02x faster                                        |
| tomli_loads        | 1.98 sec                                                              | 1.95 sec: 1.02x faster                                       |
| xml_etree_process  | 58.9 ms                                                               | 58.4 ms: 1.01x faster                                        |
| unpickle_list      | 5.21 us                                                               | 5.25 us: 1.01x slower                                        |
| Geometric mean     | (ref)                                                                 | 1.00x faster                                                 |

Benchmark hidden because not significant (8): xml_etree_parse, unpickle_pure_python, xml_etree_iterparse, json_loads, xml_etree_generate, json_dumps, pickle, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247 | bm-20240509-linux-x86_64-brandtbucher-hoist-3.14.0a0-5e272c0 |
|------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| python_startup         | 11.1 ms                                                               | 11.1 ms: 1.00x faster                                        |
| python_startup_no_site | 7.67 ms                                                               | 7.65 ms: 1.00x faster                                        |
| Geometric mean         | (ref)                                                                 | 1.00x faster                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247 | bm-20240509-linux-x86_64-brandtbucher-hoist-3.14.0a0-5e272c0 |
|-----------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| genshi_xml      | 59.9 ms                                                               | 57.4 ms: 1.04x faster                                        |
| mako            | 9.67 ms                                                               | 9.53 ms: 1.01x faster                                        |
| django_template | 37.1 ms                                                               | 36.6 ms: 1.01x faster                                        |
| genshi_text     | 25.1 ms                                                               | 24.8 ms: 1.01x faster                                        |
| Geometric mean  | (ref)                                                                 | 1.02x faster                                                 |

All benchmarks:
===============

| Benchmark                | bm-20240508-linux-x86_64-python-7b0c247f1c176e092777-3.14.0a0-7b0c247 | bm-20240509-linux-x86_64-brandtbucher-hoist-3.14.0a0-5e272c0 |
|--------------------------|:---------------------------------------------------------------------:|:------------------------------------------------------------:|
| spectral_norm            | 104 ms                                                                | 99.0 ms: 1.05x faster                                        |
| genshi_xml               | 59.9 ms                                                               | 57.4 ms: 1.04x faster                                        |
| nbody                    | 84.0 ms                                                               | 81.0 ms: 1.04x faster                                        |
| pyflate                  | 460 ms                                                                | 444 ms: 1.04x faster                                         |
| regex_dna                | 228 ms                                                                | 220 ms: 1.04x faster                                         |
| deepcopy_reduce          | 3.35 us                                                               | 3.26 us: 1.03x faster                                        |
| logging_silent           | 109 ns                                                                | 106 ns: 1.03x faster                                         |
| richards                 | 43.6 ms                                                               | 42.6 ms: 1.02x faster                                        |
| pickle_pure_python       | 310 us                                                                | 304 us: 1.02x faster                                         |
| deltablue                | 3.82 ms                                                               | 3.74 ms: 1.02x faster                                        |
| html5lib                 | 70.7 ms                                                               | 69.2 ms: 1.02x faster                                        |
| pickle_list              | 5.56 us                                                               | 5.47 us: 1.02x faster                                        |
| sqlglot_optimize         | 58.0 ms                                                               | 57.1 ms: 1.02x faster                                        |
| pickle_dict              | 34.7 us                                                               | 34.2 us: 1.02x faster                                        |
| richards_super           | 49.5 ms                                                               | 48.7 ms: 1.02x faster                                        |
| tomli_loads              | 1.98 sec                                                              | 1.95 sec: 1.02x faster                                       |
| mako                     | 9.67 ms                                                               | 9.53 ms: 1.01x faster                                        |
| django_template          | 37.1 ms                                                               | 36.6 ms: 1.01x faster                                        |
| genshi_text              | 25.1 ms                                                               | 24.8 ms: 1.01x faster                                        |
| logging_simple           | 5.85 us                                                               | 5.77 us: 1.01x faster                                        |
| meteor_contest           | 110 ms                                                                | 109 ms: 1.01x faster                                         |
| chaos                    | 59.1 ms                                                               | 58.4 ms: 1.01x faster                                        |
| coverage                 | 88.2 ms                                                               | 87.1 ms: 1.01x faster                                        |
| raytrace                 | 278 ms                                                                | 274 ms: 1.01x faster                                         |
| sympy_expand             | 513 ms                                                                | 507 ms: 1.01x faster                                         |
| sqlglot_normalize        | 116 ms                                                                | 114 ms: 1.01x faster                                         |
| coroutines               | 23.3 ms                                                               | 23.1 ms: 1.01x faster                                        |
| comprehensions           | 16.8 us                                                               | 16.6 us: 1.01x faster                                        |
| scimark_sor              | 130 ms                                                                | 129 ms: 1.01x faster                                         |
| logging_format           | 6.53 us                                                               | 6.48 us: 1.01x faster                                        |
| typing_runtime_protocols | 177 us                                                                | 176 us: 1.01x faster                                         |
| xml_etree_process        | 58.9 ms                                                               | 58.4 ms: 1.01x faster                                        |
| create_gc_cycles         | 1.83 ms                                                               | 1.82 ms: 1.01x faster                                        |
| deepcopy                 | 371 us                                                                | 369 us: 1.01x faster                                         |
| tornado_http             | 98.4 ms                                                               | 97.9 ms: 1.01x faster                                        |
| bench_thread_pool        | 874 us                                                                | 869 us: 1.01x faster                                         |
| python_startup           | 11.1 ms                                                               | 11.1 ms: 1.00x faster                                        |
| generators               | 30.0 ms                                                               | 29.9 ms: 1.00x faster                                        |
| asyncio_tcp_ssl          | 1.86 sec                                                              | 1.85 sec: 1.00x faster                                       |
| python_startup_no_site   | 7.67 ms                                                               | 7.65 ms: 1.00x faster                                        |
| async_generators         | 471 ms                                                                | 472 ms: 1.00x slower                                         |
| sqlglot_transpile        | 1.64 ms                                                               | 1.65 ms: 1.00x slower                                        |
| docutils                 | 2.96 sec                                                              | 2.97 sec: 1.00x slower                                       |
| telco                    | 172 ms                                                                | 173 ms: 1.00x slower                                         |
| sympy_str                | 302 ms                                                                | 304 ms: 1.01x slower                                         |
| regex_v8                 | 25.3 ms                                                               | 25.4 ms: 1.01x slower                                        |
| sympy_sum                | 173 ms                                                                | 174 ms: 1.01x slower                                         |
| sympy_integrate          | 22.7 ms                                                               | 22.8 ms: 1.01x slower                                        |
| crypto_pyaes             | 68.9 ms                                                               | 69.4 ms: 1.01x slower                                        |
| thrift                   | 808 us                                                                | 814 us: 1.01x slower                                         |
| unpickle_list            | 5.21 us                                                               | 5.25 us: 1.01x slower                                        |
| fannkuch                 | 362 ms                                                                | 365 ms: 1.01x slower                                         |
| nqueens                  | 86.6 ms                                                               | 87.7 ms: 1.01x slower                                        |
| scimark_lu               | 123 ms                                                                | 125 ms: 1.01x slower                                         |
| gc_traversal             | 3.94 ms                                                               | 4.01 ms: 1.02x slower                                        |
| scimark_fft              | 317 ms                                                                | 323 ms: 1.02x slower                                         |
| asyncio_tcp              | 505 ms                                                                | 521 ms: 1.03x slower                                         |
| regex_effbot             | 3.68 ms                                                               | 3.82 ms: 1.04x slower                                        |
| hexiom                   | 6.56 ms                                                               | 6.85 ms: 1.04x slower                                        |
| pidigits                 | 188 ms                                                                | 197 ms: 1.05x slower                                         |
| mdp                      | 2.60 sec                                                              | 2.81 sec: 1.08x slower                                       |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                 |

Benchmark hidden because not significant (39): async_tree_cpu_io_mixed, pprint_safe_repr, json, xml_etree_parse, async_tree_none, pylint, async_tree_memoization, chameleon, scimark_sparse_mat_mult, async_tree_cpu_io_mixed_tg, dask, scimark_monte_carlo, unpickle_pure_python, xml_etree_iterparse, dulwich_log, async_tree_io_tg, go, sqlite_synth, deepcopy_memo, gunicorn, regex_compile, asyncio_websockets, bench_mp_pool, json_loads, 2to3, aiohttp, pathlib, xml_etree_generate, float, flaskblogging, sqlglot_parse, pprint_pformat, json_dumps, async_tree_io, async_tree_memoization_tg, pycparser, pickle, unpickle, async_tree_none_tg

# HPT report

- Reliability score: 95.50% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.01x