# Results vs. base

- fork: brandtbucher
- ref: justin_compact
- machine: linux-aarch64
- commit hash: e04d5ab
- commit date: 2024-06-19
- overall geometric mean: 1.01x faster
- HPT reliability: 99.94%
- HPT 99th percentile: 1.00x faster
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240618-arminc-aarch64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| docutils       | 3.49 sec                                                                | 3.56 sec: 1.02x slower                                                  |
| html5lib       | 72.3 ms                                                                 | 71.1 ms: 1.02x faster                                                   |
| tornado_http   | 144 ms                                                                  | 138 ms: 1.04x faster                                                    |
| Geometric mean | (ref)                                                                   | 1.01x faster                                                            |

Benchmark hidden because not significant (1): 2to3

Benchmarks with tag 'asyncio':
==============================

| Benchmark        | bm-20240618-arminc-aarch64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| async_tree_io_tg | 1.23 sec                                                                | 1.20 sec: 1.03x faster                                                  |
| Geometric mean   | (ref)                                                                   | 1.01x faster                                                            |

Benchmark hidden because not significant (7): async_tree_memoization_tg, async_tree_io, async_tree_none, async_tree_memoization, async_tree_cpu_io_mixed_tg, async_tree_cpu_io_mixed, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240618-arminc-aarch64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 91.4 ms                                                                 | 88.2 ms: 1.04x faster                                                   |
| Geometric mean | (ref)                                                                   | 1.01x faster                                                            |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240618-arminc-aarch64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_effbot   | 4.85 ms                                                                 | 4.90 ms: 1.01x slower                                                   |
| regex_dna      | 246 ms                                                                  | 258 ms: 1.05x slower                                                    |
| Geometric mean | (ref)                                                                   | 1.01x slower                                                            |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240618-arminc-aarch64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|---------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| tomli_loads         | 2.68 sec                                                                | 2.61 sec: 1.03x faster                                                  |
| json_loads          | 33.0 us                                                                 | 32.6 us: 1.01x faster                                                   |
| pickle_list         | 5.30 us                                                                 | 5.24 us: 1.01x faster                                                   |
| pickle              | 13.7 us                                                                 | 13.6 us: 1.01x faster                                                   |
| json_dumps          | 13.3 ms                                                                 | 13.2 ms: 1.01x faster                                                   |
| pickle_pure_python  | 394 us                                                                  | 392 us: 1.00x faster                                                    |
| xml_etree_iterparse | 148 ms                                                                  | 150 ms: 1.01x slower                                                    |
| Geometric mean      | (ref)                                                                   | 1.00x faster                                                            |

Benchmark hidden because not significant (7): xml_etree_parse, unpickle, unpickle_pure_python, xml_etree_process, unpickle_list, pickle_dict, xml_etree_generate

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240618-arminc-aarch64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|-----------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_text     | 35.6 ms                                                                 | 33.8 ms: 1.05x faster                                                   |
| genshi_xml      | 82.6 ms                                                                 | 78.6 ms: 1.05x faster                                                   |
| django_template | 50.8 ms                                                                 | 50.2 ms: 1.01x faster                                                   |
| Geometric mean  | (ref)                                                                   | 1.03x faster                                                            |

Benchmark hidden because not significant (1): mako

All benchmarks:
===============

| Benchmark                | bm-20240618-arminc-aarch64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240619-arminc-aarch64-brandtbucher-justin_compact-3.14.0a0-e04d5ab |
|--------------------------|:-----------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| asyncio_tcp              | 617 ms                                                                  | 577 ms: 1.07x faster                                                    |
| bench_mp_pool            | 8.00 ms                                                                 | 7.50 ms: 1.07x faster                                                   |
| genshi_text              | 35.6 ms                                                                 | 33.8 ms: 1.05x faster                                                   |
| genshi_xml               | 82.6 ms                                                                 | 78.6 ms: 1.05x faster                                                   |
| tornado_http             | 144 ms                                                                  | 138 ms: 1.04x faster                                                    |
| float                    | 91.4 ms                                                                 | 88.2 ms: 1.04x faster                                                   |
| bench_thread_pool        | 1.36 ms                                                                 | 1.31 ms: 1.04x faster                                                   |
| tomli_loads              | 2.68 sec                                                                | 2.61 sec: 1.03x faster                                                  |
| async_tree_io_tg         | 1.23 sec                                                                | 1.20 sec: 1.03x faster                                                  |
| sqlite_synth             | 3.96 us                                                                 | 3.85 us: 1.03x faster                                                   |
| gc_traversal             | 5.05 ms                                                                 | 4.92 ms: 1.03x faster                                                   |
| asyncio_tcp_ssl          | 2.25 sec                                                                | 2.19 sec: 1.03x faster                                                  |
| chaos                    | 87.6 ms                                                                 | 85.6 ms: 1.02x faster                                                   |
| typing_runtime_protocols | 215 us                                                                  | 211 us: 1.02x faster                                                    |
| deepcopy_reduce          | 4.16 us                                                                 | 4.08 us: 1.02x faster                                                   |
| nqueens                  | 118 ms                                                                  | 116 ms: 1.02x faster                                                    |
| scimark_monte_carlo      | 87.7 ms                                                                 | 86.1 ms: 1.02x faster                                                   |
| html5lib                 | 72.3 ms                                                                 | 71.1 ms: 1.02x faster                                                   |
| go                       | 179 ms                                                                  | 176 ms: 1.02x faster                                                    |
| crypto_pyaes             | 87.1 ms                                                                 | 85.9 ms: 1.01x faster                                                   |
| sympy_expand             | 546 ms                                                                  | 538 ms: 1.01x faster                                                    |
| comprehensions           | 23.3 us                                                                 | 23.0 us: 1.01x faster                                                   |
| dulwich_log              | 69.7 ms                                                                 | 68.8 ms: 1.01x faster                                                   |
| json_loads               | 33.0 us                                                                 | 32.6 us: 1.01x faster                                                   |
| django_template          | 50.8 ms                                                                 | 50.2 ms: 1.01x faster                                                   |
| bpe_tokeniser            | 6.07 sec                                                                | 6.00 sec: 1.01x faster                                                  |
| pprint_safe_repr         | 1.13 sec                                                                | 1.11 sec: 1.01x faster                                                  |
| pickle_list              | 5.30 us                                                                 | 5.24 us: 1.01x faster                                                   |
| logging_format           | 7.85 us                                                                 | 7.76 us: 1.01x faster                                                   |
| deepcopy                 | 377 us                                                                  | 373 us: 1.01x faster                                                    |
| json                     | 5.84 ms                                                                 | 5.79 ms: 1.01x faster                                                   |
| scimark_fft              | 460 ms                                                                  | 456 ms: 1.01x faster                                                    |
| pprint_pformat           | 2.33 sec                                                                | 2.31 sec: 1.01x faster                                                  |
| pickle                   | 13.7 us                                                                 | 13.6 us: 1.01x faster                                                   |
| async_generators         | 513 ms                                                                  | 510 ms: 1.01x faster                                                    |
| json_dumps               | 13.3 ms                                                                 | 13.2 ms: 1.01x faster                                                   |
| pickle_pure_python       | 394 us                                                                  | 392 us: 1.00x faster                                                    |
| logging_silent           | 138 ns                                                                  | 138 ns: 1.00x slower                                                    |
| sympy_integrate          | 25.7 ms                                                                 | 25.8 ms: 1.00x slower                                                   |
| fannkuch                 | 464 ms                                                                  | 469 ms: 1.01x slower                                                    |
| regex_effbot             | 4.85 ms                                                                 | 4.90 ms: 1.01x slower                                                   |
| spectral_norm            | 148 ms                                                                  | 150 ms: 1.01x slower                                                    |
| richards                 | 54.5 ms                                                                 | 55.2 ms: 1.01x slower                                                   |
| xml_etree_iterparse      | 148 ms                                                                  | 150 ms: 1.01x slower                                                    |
| scimark_sparse_mat_mult  | 6.92 ms                                                                 | 7.04 ms: 1.02x slower                                                   |
| docutils                 | 3.49 sec                                                                | 3.56 sec: 1.02x slower                                                  |
| regex_dna                | 246 ms                                                                  | 258 ms: 1.05x slower                                                    |
| Geometric mean           | (ref)                                                                   | 1.01x faster                                                            |

Benchmark hidden because not significant (50): sqlglot_normalize, async_tree_memoization_tg, deltablue, async_tree_io, regex_compile, logging_simple, xml_etree_parse, sympy_str, unpickle, raytrace, pycparser, coroutines, async_tree_none, thrift, async_tree_memoization, regex_v8, telco, asyncio_websockets, pidigits, nbody, async_tree_cpu_io_mixed_tg, mdp, async_tree_cpu_io_mixed, scimark_sor, mako, meteor_contest, async_tree_none_tg, sympy_sum, scimark_lu, python_startup_no_site, unpickle_pure_python, sqlglot_parse, hexiom, python_startup, sqlglot_optimize, richards_super, pyflate, deepcopy_memo, dask, 2to3, xml_etree_process, unpickle_list, pickle_dict, sqlglot_transpile, create_gc_cycles, generators, pylint, coverage, pathlib, xml_etree_generate

# HPT report

- Reliability score: 99.94% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x

# Memory
- memory change: 1.00x