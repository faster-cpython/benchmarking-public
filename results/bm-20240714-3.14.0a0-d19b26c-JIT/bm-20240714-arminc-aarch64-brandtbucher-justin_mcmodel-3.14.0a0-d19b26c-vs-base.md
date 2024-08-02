# Results vs. base

- fork: brandtbucher
- ref: justin_mcmodel
- machine: linux-aarch64
- commit hash: d19b26c
- commit date: 2024-07-14
- overall geometric mean: 1.01x slower
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-arminc-aarch64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 3.58 sec                                                                | 3.55 sec: 1.01x faster                                                  |
| tornado_http   | 139 ms                                                                  | 144 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                            |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_none_tg, async_tree_io, async_tree_io_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization_tg, async_tree_memoization, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-arminc-aarch64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 89.9 ms                                                                 | 89.2 ms: 1.01x faster                                                   |
| nbody          | 116 ms                                                                  | 122 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                            |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-arminc-aarch64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile  | 180 ms                                                                  | 175 ms: 1.03x faster                                                    |
| regex_v8       | 30.5 ms                                                                 | 30.3 ms: 1.01x faster                                                   |
| regex_effbot   | 4.85 ms                                                                 | 4.95 ms: 1.02x slower                                                   |
| regex_dna      | 248 ms                                                                  | 259 ms: 1.04x slower                                                    |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-arminc-aarch64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| xml_etree_iterparse  | 150 ms                                                                  | 148 ms: 1.02x faster                                                    |
| xml_etree_generate   | 112 ms                                                                  | 111 ms: 1.01x faster                                                    |
| json_dumps           | 13.3 ms                                                                 | 13.5 ms: 1.01x slower                                                   |
| unpickle_pure_python | 275 us                                                                  | 279 us: 1.02x slower                                                    |
| tomli_loads          | 2.61 sec                                                                | 2.67 sec: 1.02x slower                                                  |
| Geometric mean       | (ref)                                                                   | 1.00x slower                                                            |

Benchmark hidden because not significant (4): xml_etree_parse, pickle_pure_python, xml_etree_process, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-arminc-aarch64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 13.0 ms                                                                 | 13.1 ms: 1.01x slower                                                   |
| python_startup_no_site | 8.78 ms                                                                 | 8.90 ms: 1.01x slower                                                   |
| Geometric mean         | (ref)                                                                   | 1.01x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-arminc-aarch64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml     | 80.2 ms                                                                 | 84.9 ms: 1.06x slower                                                   |
| Geometric mean | (ref)                                                                   | 1.02x slower                                                            |

Benchmark hidden because not significant (3): mako, genshi_text, django_template

All benchmarks:
===============

| Benchmark              | bm-20240708-arminc-aarch64-python-006b53a42f72be83ecdf-3.14.0a0-006b53a | bm-20240714-arminc-aarch64-brandtbucher-justin_mcmodel-3.14.0a0-d19b26c |
|------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_compile          | 180 ms                                                                  | 175 ms: 1.03x faster                                                    |
| hexiom                 | 9.04 ms                                                                 | 8.81 ms: 1.03x faster                                                   |
| sympy_sum              | 187 ms                                                                  | 183 ms: 1.02x faster                                                    |
| xml_etree_iterparse    | 150 ms                                                                  | 148 ms: 1.02x faster                                                    |
| docutils               | 3.58 sec                                                                | 3.55 sec: 1.01x faster                                                  |
| float                  | 89.9 ms                                                                 | 89.2 ms: 1.01x faster                                                   |
| regex_v8               | 30.5 ms                                                                 | 30.3 ms: 1.01x faster                                                   |
| xml_etree_generate     | 112 ms                                                                  | 111 ms: 1.01x faster                                                    |
| sympy_integrate        | 26.4 ms                                                                 | 26.3 ms: 1.01x faster                                                   |
| bpe_tokeniser          | 6.00 sec                                                                | 6.02 sec: 1.00x slower                                                  |
| python_startup         | 13.0 ms                                                                 | 13.1 ms: 1.01x slower                                                   |
| richards               | 54.2 ms                                                                 | 54.8 ms: 1.01x slower                                                   |
| deepcopy_memo          | 38.4 us                                                                 | 38.8 us: 1.01x slower                                                   |
| nqueens                | 116 ms                                                                  | 117 ms: 1.01x slower                                                    |
| pprint_pformat         | 2.39 sec                                                                | 2.42 sec: 1.01x slower                                                  |
| json_dumps             | 13.3 ms                                                                 | 13.5 ms: 1.01x slower                                                   |
| richards_super         | 61.3 ms                                                                 | 62.1 ms: 1.01x slower                                                   |
| python_startup_no_site | 8.78 ms                                                                 | 8.90 ms: 1.01x slower                                                   |
| thrift                 | 965 us                                                                  | 978 us: 1.01x slower                                                    |
| pycparser              | 1.34 sec                                                                | 1.36 sec: 1.01x slower                                                  |
| sqlglot_parse          | 1.59 ms                                                                 | 1.61 ms: 1.02x slower                                                   |
| crypto_pyaes           | 88.5 ms                                                                 | 90.0 ms: 1.02x slower                                                   |
| unpickle_pure_python   | 275 us                                                                  | 279 us: 1.02x slower                                                    |
| scimark_fft            | 463 ms                                                                  | 472 ms: 1.02x slower                                                    |
| logging_simple         | 7.14 us                                                                 | 7.28 us: 1.02x slower                                                   |
| pprint_safe_repr       | 1.14 sec                                                                | 1.16 sec: 1.02x slower                                                  |
| pyflate                | 608 ms                                                                  | 621 ms: 1.02x slower                                                    |
| regex_effbot           | 4.85 ms                                                                 | 4.95 ms: 1.02x slower                                                   |
| tomli_loads            | 2.61 sec                                                                | 2.67 sec: 1.02x slower                                                  |
| meteor_contest         | 115 ms                                                                  | 118 ms: 1.03x slower                                                    |
| deepcopy               | 372 us                                                                  | 382 us: 1.03x slower                                                    |
| gc_traversal           | 4.90 ms                                                                 | 5.04 ms: 1.03x slower                                                   |
| scimark_monte_carlo    | 88.7 ms                                                                 | 91.5 ms: 1.03x slower                                                   |
| pathlib                | 21.8 ms                                                                 | 22.6 ms: 1.03x slower                                                   |
| tornado_http           | 139 ms                                                                  | 144 ms: 1.04x slower                                                    |
| logging_silent         | 137 ns                                                                  | 142 ns: 1.04x slower                                                    |
| chaos                  | 89.6 ms                                                                 | 93.3 ms: 1.04x slower                                                   |
| regex_dna              | 248 ms                                                                  | 259 ms: 1.04x slower                                                    |
| dulwich_log            | 69.4 ms                                                                 | 72.6 ms: 1.05x slower                                                   |
| nbody                  | 116 ms                                                                  | 122 ms: 1.05x slower                                                    |
| genshi_xml             | 80.2 ms                                                                 | 84.9 ms: 1.06x slower                                                   |
| bench_mp_pool          | 8.18 ms                                                                 | 13.2 ms: 1.62x slower                                                   |
| Geometric mean         | (ref)                                                                   | 1.01x slower                                                            |

Benchmark hidden because not significant (49): xml_etree_parse, generators, sympy_str, coverage, logging_format, fannkuch, go, async_tree_none_tg, async_tree_io, scimark_lu, mako, raytrace, mdp, bench_thread_pool, asyncio_tcp_ssl, async_generators, typing_runtime_protocols, sqlglot_optimize, json, deltablue, sympy_expand, pickle_pure_python, pidigits, async_tree_io_tg, scimark_sparse_mat_mult, genshi_text, scimark_sor, django_template, 2to3, telco, comprehensions, asyncio_websockets, deepcopy_reduce, async_tree_cpu_io_mixed, async_tree_none, async_tree_memoization_tg, pylint, async_tree_memoization, xml_etree_process, dask, coroutines, async_tree_cpu_io_mixed_tg, sqlglot_normalize, json_loads, create_gc_cycles, asyncio_tcp, sqlglot_transpile, html5lib, spectral_norm

# HPT report

- Reliability score: 99.99% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x