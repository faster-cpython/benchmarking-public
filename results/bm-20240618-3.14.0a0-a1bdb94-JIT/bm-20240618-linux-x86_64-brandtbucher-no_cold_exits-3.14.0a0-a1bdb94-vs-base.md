# Results vs. base

- fork: brandtbucher
- ref: no_cold_exits
- machine: linux-x86_64
- commit hash: a1bdb94
- commit date: 2024-06-18
- overall geometric mean: 1.00x slower
- HPT reliability: 52.91%
- HPT 99th percentile: 1.00x faster
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 281 ms                                                                | 279 ms: 1.01x faster                                                 |
| html5lib       | 68.0 ms                                                               | 68.9 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                         |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io, async_tree_memoization, async_tree_io_tg, async_tree_memoization_tg, async_tree_none, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 188 ms                                                                | 189 ms: 1.00x slower                                                 |
| nbody          | 80.3 ms                                                               | 82.2 ms: 1.02x slower                                                |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                         |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_v8       | 27.0 ms                                                               | 26.4 ms: 1.02x faster                                                |
| regex_compile  | 137 ms                                                                | 138 ms: 1.01x slower                                                 |
| regex_effbot   | 3.95 ms                                                               | 3.99 ms: 1.01x slower                                                |
| regex_dna      | 229 ms                                                                | 236 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|--------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| unpickle           | 16.0 us                                                               | 14.8 us: 1.08x faster                                                |
| xml_etree_parse    | 150 ms                                                                | 148 ms: 1.01x faster                                                 |
| pickle_pure_python | 301 us                                                                | 297 us: 1.01x faster                                                 |
| json_dumps         | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                |
| unpickle_list      | 5.16 us                                                               | 5.20 us: 1.01x slower                                                |
| xml_etree_process  | 58.7 ms                                                               | 59.3 ms: 1.01x slower                                                |
| tomli_loads        | 1.93 sec                                                              | 1.97 sec: 1.02x slower                                               |
| pickle_list        | 5.17 us                                                               | 5.29 us: 1.02x slower                                                |
| pickle_dict        | 34.6 us                                                               | 36.1 us: 1.04x slower                                                |
| Geometric mean     | (ref)                                                                 | 1.00x slower                                                         |

Benchmark hidden because not significant (5): json_loads, pickle, xml_etree_generate, xml_etree_iterparse, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup_no_site | 7.63 ms                                                               | 7.25 ms: 1.05x faster                                                |
| python_startup         | 11.2 ms                                                               | 10.8 ms: 1.04x faster                                                |
| Geometric mean         | (ref)                                                                 | 1.04x faster                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|----------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| mako           | 9.86 ms                                                               | 9.92 ms: 1.01x slower                                                |
| genshi_xml     | 57.6 ms                                                               | 58.2 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                         |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark                | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240618-linux-x86_64-brandtbucher-no_cold_exits-3.14.0a0-a1bdb94 |
|--------------------------|:---------------------------------------------------------------------:|:--------------------------------------------------------------------:|
| unpickle                 | 16.0 us                                                               | 14.8 us: 1.08x faster                                                |
| coroutines               | 24.3 ms                                                               | 22.9 ms: 1.06x faster                                                |
| python_startup_no_site   | 7.63 ms                                                               | 7.25 ms: 1.05x faster                                                |
| python_startup           | 11.2 ms                                                               | 10.8 ms: 1.04x faster                                                |
| richards_super           | 49.9 ms                                                               | 48.3 ms: 1.03x faster                                                |
| typing_runtime_protocols | 172 us                                                                | 168 us: 1.02x faster                                                 |
| regex_v8                 | 27.0 ms                                                               | 26.4 ms: 1.02x faster                                                |
| deepcopy_reduce          | 2.79 us                                                               | 2.73 us: 1.02x faster                                                |
| chaos                    | 61.3 ms                                                               | 60.0 ms: 1.02x faster                                                |
| logging_simple           | 5.65 us                                                               | 5.54 us: 1.02x faster                                                |
| json                     | 5.43 ms                                                               | 5.33 ms: 1.02x faster                                                |
| go                       | 151 ms                                                                | 148 ms: 1.02x faster                                                 |
| raytrace                 | 280 ms                                                                | 275 ms: 1.02x faster                                                 |
| logging_format           | 6.32 us                                                               | 6.23 us: 1.01x faster                                                |
| richards                 | 43.1 ms                                                               | 42.6 ms: 1.01x faster                                                |
| deltablue                | 3.67 ms                                                               | 3.63 ms: 1.01x faster                                                |
| xml_etree_parse          | 150 ms                                                                | 148 ms: 1.01x faster                                                 |
| pickle_pure_python       | 301 us                                                                | 297 us: 1.01x faster                                                 |
| scimark_monte_carlo      | 63.2 ms                                                               | 62.6 ms: 1.01x faster                                                |
| generators               | 30.3 ms                                                               | 30.0 ms: 1.01x faster                                                |
| scimark_lu               | 126 ms                                                                | 125 ms: 1.01x faster                                                 |
| nqueens                  | 85.0 ms                                                               | 84.3 ms: 1.01x faster                                                |
| bpe_tokeniser            | 4.90 sec                                                              | 4.86 sec: 1.01x faster                                               |
| 2to3                     | 281 ms                                                                | 279 ms: 1.01x faster                                                 |
| bench_thread_pool        | 853 us                                                                | 850 us: 1.00x faster                                                 |
| async_generators         | 467 ms                                                                | 465 ms: 1.00x faster                                                 |
| create_gc_cycles         | 1.78 ms                                                               | 1.79 ms: 1.00x slower                                                |
| dulwich_log              | 68.5 ms                                                               | 68.8 ms: 1.00x slower                                                |
| json_dumps               | 10.5 ms                                                               | 10.5 ms: 1.00x slower                                                |
| pidigits                 | 188 ms                                                                | 189 ms: 1.00x slower                                                 |
| regex_compile            | 137 ms                                                                | 138 ms: 1.01x slower                                                 |
| mako                     | 9.86 ms                                                               | 9.92 ms: 1.01x slower                                                |
| hexiom                   | 6.68 ms                                                               | 6.72 ms: 1.01x slower                                                |
| unpickle_list            | 5.16 us                                                               | 5.20 us: 1.01x slower                                                |
| sympy_integrate          | 22.5 ms                                                               | 22.7 ms: 1.01x slower                                                |
| sqlite_synth             | 2.83 us                                                               | 2.85 us: 1.01x slower                                                |
| comprehensions           | 16.6 us                                                               | 16.8 us: 1.01x slower                                                |
| xml_etree_process        | 58.7 ms                                                               | 59.3 ms: 1.01x slower                                                |
| genshi_xml               | 57.6 ms                                                               | 58.2 ms: 1.01x slower                                                |
| crypto_pyaes             | 67.8 ms                                                               | 68.5 ms: 1.01x slower                                                |
| meteor_contest           | 108 ms                                                                | 109 ms: 1.01x slower                                                 |
| sqlglot_transpile        | 1.63 ms                                                               | 1.65 ms: 1.01x slower                                                |
| deepcopy_memo            | 28.7 us                                                               | 29.0 us: 1.01x slower                                                |
| logging_silent           | 107 ns                                                                | 108 ns: 1.01x slower                                                 |
| regex_effbot             | 3.95 ms                                                               | 3.99 ms: 1.01x slower                                                |
| spectral_norm            | 104 ms                                                                | 106 ms: 1.01x slower                                                 |
| html5lib                 | 68.0 ms                                                               | 68.9 ms: 1.01x slower                                                |
| thrift                   | 816 us                                                                | 830 us: 1.02x slower                                                 |
| tomli_loads              | 1.93 sec                                                              | 1.97 sec: 1.02x slower                                               |
| nbody                    | 80.3 ms                                                               | 82.2 ms: 1.02x slower                                                |
| pickle_list              | 5.17 us                                                               | 5.29 us: 1.02x slower                                                |
| regex_dna                | 229 ms                                                                | 236 ms: 1.03x slower                                                 |
| scimark_fft              | 315 ms                                                                | 326 ms: 1.03x slower                                                 |
| pickle_dict              | 34.6 us                                                               | 36.1 us: 1.04x slower                                                |
| pyflate                  | 438 ms                                                                | 459 ms: 1.05x slower                                                 |
| gc_traversal             | 3.64 ms                                                               | 3.92 ms: 1.08x slower                                                |
| scimark_sparse_mat_mult  | 4.21 ms                                                               | 4.57 ms: 1.08x slower                                                |
| Geometric mean           | (ref)                                                                 | 1.00x slower                                                         |

Benchmark hidden because not significant (39): async_tree_io, async_tree_memoization, async_tree_io_tg, json_loads, async_tree_memoization_tg, async_tree_none, coverage, async_tree_none_tg, pprint_pformat, float, pickle, bench_mp_pool, pathlib, tornado_http, mdp, deepcopy, asyncio_websockets, xml_etree_generate, sympy_sum, asyncio_tcp_ssl, genshi_text, asyncio_tcp, sympy_expand, telco, dask, fannkuch, sympy_str, sqlglot_optimize, pycparser, xml_etree_iterparse, unpickle_pure_python, pylint, sqlglot_parse, scimark_sor, sqlglot_normalize, django_template, pprint_safe_repr, async_tree_cpu_io_mixed, async_tree_cpu_io_mixed_tg
Ignored benchmarks (1) of results/bm-20240618-3.14.0a0-9f741e5-JIT/bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5.json: docutils

# HPT report

- Reliability score: 52.91% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 0.98x