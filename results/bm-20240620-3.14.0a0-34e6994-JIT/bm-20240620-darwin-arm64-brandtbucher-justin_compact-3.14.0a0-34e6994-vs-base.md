# Results vs. base

- fork: brandtbucher
- ref: justin_compact
- machine: darwin-arm64
- commit hash: 34e6994
- commit date: 2024-06-20
- overall geometric mean: 1.00x faster
- HPT reliability: 81.89%
- HPT 99th percentile: 1.00x slower
- Memory change: 0.98x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240618-darwin-arm64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 171 ms                                                                | 172 ms: 1.00x slower                                                  |
| docutils       | 1.51 sec                                                              | 1.50 sec: 1.00x faster                                                |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240618-darwin-arm64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| async_tree_eager | 63.4 ms                                                               | 63.7 ms: 1.01x slower                                                 |
| Geometric mean   | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (15): async_tree_io, async_tree_io_tg, async_tree_eager_cpu_io_mixed, async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_eager_tg, async_tree_eager_memoization_tg, async_tree_eager_memoization, async_tree_eager_io_tg, async_tree_none, async_tree_memoization_tg, async_tree_eager_io, async_tree_none_tg, async_tree_memoization

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240618-darwin-arm64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 63.9 ms                                                               | 63.5 ms: 1.01x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (2): pidigits, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240618-darwin-arm64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_compile  | 72.2 ms                                                               | 71.5 ms: 1.01x faster                                                 |
| regex_v8       | 17.3 ms                                                               | 17.4 ms: 1.00x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (2): regex_effbot, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240618-darwin-arm64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle               | 7.55 us                                                               | 7.50 us: 1.01x faster                                                 |
| tomli_loads          | 1.25 sec                                                              | 1.24 sec: 1.01x faster                                                |
| unpickle_pure_python | 132 us                                                                | 132 us: 1.00x slower                                                  |
| xml_etree_process    | 36.0 ms                                                               | 36.1 ms: 1.00x slower                                                 |
| xml_etree_generate   | 51.9 ms                                                               | 52.1 ms: 1.00x slower                                                 |
| pickle_list          | 2.96 us                                                               | 2.97 us: 1.00x slower                                                 |
| pickle_pure_python   | 172 us                                                                | 173 us: 1.01x slower                                                  |
| json_loads           | 16.9 us                                                               | 17.1 us: 1.01x slower                                                 |
| json_dumps           | 6.30 ms                                                               | 6.40 ms: 1.02x slower                                                 |
| Geometric mean       | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (5): unpickle, unpickle_list, xml_etree_parse, xml_etree_iterparse, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240618-darwin-arm64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 11.6 ms                                                               | 11.3 ms: 1.03x faster                                                 |
| Geometric mean         | (ref)                                                                 | 1.02x faster                                                          |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20240618-darwin-arm64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml     | 39.7 ms                                                               | 35.2 ms: 1.13x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.03x faster                                                          |

Benchmark hidden because not significant (3): genshi_text, django_template, mako

All benchmarks:
===============

| Benchmark               | bm-20240618-darwin-arm64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-darwin-arm64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| genshi_xml              | 39.7 ms                                                               | 35.2 ms: 1.13x faster                                                 |
| python_startup_no_site  | 11.6 ms                                                               | 11.3 ms: 1.03x faster                                                 |
| hexiom                  | 4.46 ms                                                               | 4.34 ms: 1.03x faster                                                 |
| go                      | 101 ms                                                                | 100 ms: 1.01x faster                                                  |
| deltablue               | 2.38 ms                                                               | 2.35 ms: 1.01x faster                                                 |
| mdp                     | 1.46 sec                                                              | 1.45 sec: 1.01x faster                                                |
| async_generators        | 297 ms                                                                | 294 ms: 1.01x faster                                                  |
| regex_compile           | 72.2 ms                                                               | 71.5 ms: 1.01x faster                                                 |
| spectral_norm           | 67.6 ms                                                               | 67.0 ms: 1.01x faster                                                 |
| richards_super          | 35.8 ms                                                               | 35.5 ms: 1.01x faster                                                 |
| logging_silent          | 63.1 ns                                                               | 62.6 ns: 1.01x faster                                                 |
| deepcopy                | 152 us                                                                | 151 us: 1.01x faster                                                  |
| pickle                  | 7.55 us                                                               | 7.50 us: 1.01x faster                                                 |
| nbody                   | 63.9 ms                                                               | 63.5 ms: 1.01x faster                                                 |
| tomli_loads             | 1.25 sec                                                              | 1.24 sec: 1.01x faster                                                |
| docutils                | 1.51 sec                                                              | 1.50 sec: 1.00x faster                                                |
| sqlglot_normalize       | 178 ms                                                                | 177 ms: 1.00x faster                                                  |
| raytrace                | 163 ms                                                                | 162 ms: 1.00x faster                                                  |
| pprint_pformat          | 965 ms                                                                | 962 ms: 1.00x faster                                                  |
| telco                   | 4.59 ms                                                               | 4.58 ms: 1.00x faster                                                 |
| meteor_contest          | 71.8 ms                                                               | 71.7 ms: 1.00x faster                                                 |
| sympy_expand            | 241 ms                                                                | 241 ms: 1.00x slower                                                  |
| unpickle_pure_python    | 132 us                                                                | 132 us: 1.00x slower                                                  |
| xml_etree_process       | 36.0 ms                                                               | 36.1 ms: 1.00x slower                                                 |
| pyflate                 | 313 ms                                                                | 314 ms: 1.00x slower                                                  |
| logging_format          | 3.30 us                                                               | 3.31 us: 1.00x slower                                                 |
| xml_etree_generate      | 51.9 ms                                                               | 52.1 ms: 1.00x slower                                                 |
| thrift                  | 440 us                                                                | 441 us: 1.00x slower                                                  |
| generators              | 23.2 ms                                                               | 23.3 ms: 1.00x slower                                                 |
| 2to3                    | 171 ms                                                                | 172 ms: 1.00x slower                                                  |
| scimark_sparse_mat_mult | 2.92 ms                                                               | 2.93 ms: 1.00x slower                                                 |
| regex_v8                | 17.3 ms                                                               | 17.4 ms: 1.00x slower                                                 |
| pickle_list             | 2.96 us                                                               | 2.97 us: 1.00x slower                                                 |
| sympy_sum               | 73.6 ms                                                               | 74.0 ms: 1.00x slower                                                 |
| deepcopy_memo           | 16.8 us                                                               | 16.9 us: 1.00x slower                                                 |
| gc_traversal            | 2.46 ms                                                               | 2.48 ms: 1.01x slower                                                 |
| async_tree_eager        | 63.4 ms                                                               | 63.7 ms: 1.01x slower                                                 |
| sympy_integrate         | 11.0 ms                                                               | 11.1 ms: 1.01x slower                                                 |
| sympy_str               | 139 ms                                                                | 140 ms: 1.01x slower                                                  |
| pickle_pure_python      | 172 us                                                                | 173 us: 1.01x slower                                                  |
| richards                | 31.4 ms                                                               | 31.6 ms: 1.01x slower                                                 |
| json_loads              | 16.9 us                                                               | 17.1 us: 1.01x slower                                                 |
| crypto_pyaes            | 51.8 ms                                                               | 52.2 ms: 1.01x slower                                                 |
| comprehensions          | 12.3 us                                                               | 12.4 us: 1.01x slower                                                 |
| pathlib                 | 22.9 ms                                                               | 23.2 ms: 1.01x slower                                                 |
| scimark_sor             | 102 ms                                                                | 103 ms: 1.01x slower                                                  |
| json_dumps              | 6.30 ms                                                               | 6.40 ms: 1.02x slower                                                 |
| scimark_monte_carlo     | 43.1 ms                                                               | 43.9 ms: 1.02x slower                                                 |
| scimark_lu              | 79.1 ms                                                               | 80.5 ms: 1.02x slower                                                 |
| fannkuch                | 241 ms                                                                | 246 ms: 1.02x slower                                                  |
| Geometric mean          | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (54): async_tree_io, async_tree_io_tg, python_startup, genshi_text, unpickle, asyncio_tcp_ssl, coverage, unpickle_list, logging_simple, sqlite_synth, deepcopy_reduce, dask, sqlglot_optimize, async_tree_eager_cpu_io_mixed, json, pycparser, chaos, regex_effbot, bpe_tokeniser, nqueens, xml_etree_parse, asyncio_websockets, pprint_safe_repr, xml_etree_iterparse, sqlglot_transpile, regex_dna, create_gc_cycles, bench_thread_pool, pickle_dict, django_template, asyncio_tcp, pidigits, mako, scimark_fft, coroutines, async_tree_cpu_io_mixed_tg, async_tree_eager_cpu_io_mixed_tg, float, pylint, html5lib, sqlglot_parse, async_tree_cpu_io_mixed, tornado_http, async_tree_eager_tg, async_tree_eager_memoization_tg, typing_runtime_protocols, async_tree_eager_memoization, async_tree_eager_io_tg, bench_mp_pool, async_tree_none, async_tree_memoization_tg, async_tree_eager_io, async_tree_none_tg, async_tree_memoization

# HPT report

- Reliability score: 81.89% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 0.98x