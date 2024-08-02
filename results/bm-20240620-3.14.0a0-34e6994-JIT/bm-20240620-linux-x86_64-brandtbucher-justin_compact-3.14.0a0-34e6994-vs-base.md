# Results vs. base

- fork: brandtbucher
- ref: justin_compact
- machine: linux-x86_64
- commit hash: 34e6994
- commit date: 2024-06-20
- overall geometric mean: 1.00x slower
- HPT reliability: 97.81%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 272 ms                                                                | 273 ms: 1.00x slower                                                  |
| docutils       | 2.86 sec                                                              | 2.87 sec: 1.01x slower                                                |
| html5lib       | 67.1 ms                                                               | 66.8 ms: 1.00x faster                                                 |
| Geometric mean | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed_tg, async_tree_none, async_tree_io, async_tree_cpu_io_mixed, async_tree_io_tg, async_tree_memoization, async_tree_memoization_tg, async_tree_none_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| pidigits       | 185 ms                                                                | 186 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_dna      | 221 ms                                                                | 223 ms: 1.01x slower                                                  |
| regex_effbot   | 3.56 ms                                                               | 3.66 ms: 1.03x slower                                                 |
| regex_v8       | 23.1 ms                                                               | 23.8 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                                 | 1.01x slower                                                          |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|----------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 10.5 ms                                                               | 10.2 ms: 1.03x faster                                                 |
| pickle_dict          | 35.7 us                                                               | 35.2 us: 1.02x faster                                                 |
| unpickle_pure_python | 218 us                                                                | 217 us: 1.01x faster                                                  |
| json_loads           | 28.5 us                                                               | 28.3 us: 1.01x faster                                                 |
| unpickle_list        | 5.15 us                                                               | 5.12 us: 1.01x faster                                                 |
| pickle               | 11.7 us                                                               | 11.7 us: 1.01x slower                                                 |
| tomli_loads          | 1.93 sec                                                              | 1.94 sec: 1.01x slower                                                |
| pickle_list          | 4.93 us                                                               | 4.99 us: 1.01x slower                                                 |
| xml_etree_iterparse  | 98.6 ms                                                               | 99.9 ms: 1.01x slower                                                 |
| pickle_pure_python   | 291 us                                                                | 297 us: 1.02x slower                                                  |
| Geometric mean       | (ref)                                                                 | 1.00x faster                                                          |

Benchmark hidden because not significant (4): xml_etree_parse, xml_etree_process, xml_etree_generate, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup_no_site | 7.41 ms                                                               | 7.43 ms: 1.00x slower                                                 |
| python_startup         | 10.8 ms                                                               | 10.9 ms: 1.00x slower                                                 |
| Geometric mean         | (ref)                                                                 | 1.00x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|-----------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| django_template | 37.4 ms                                                               | 36.3 ms: 1.03x faster                                                 |
| genshi_xml      | 56.8 ms                                                               | 57.4 ms: 1.01x slower                                                 |
| genshi_text     | 24.6 ms                                                               | 24.9 ms: 1.01x slower                                                 |
| mako            | 9.54 ms                                                               | 9.70 ms: 1.02x slower                                                 |
| Geometric mean  | (ref)                                                                 | 1.00x slower                                                          |

All benchmarks:
===============

| Benchmark               | bm-20240618-linux-x86_64-python-9f741e55c16376412c14-3.14.0a0-9f741e5 | bm-20240620-linux-x86_64-brandtbucher-justin_compact-3.14.0a0-34e6994 |
|-------------------------|:---------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mdp                     | 2.76 sec                                                              | 2.56 sec: 1.08x faster                                                |
| chaos                   | 60.4 ms                                                               | 58.6 ms: 1.03x faster                                                 |
| json_dumps              | 10.5 ms                                                               | 10.2 ms: 1.03x faster                                                 |
| django_template         | 37.4 ms                                                               | 36.3 ms: 1.03x faster                                                 |
| pickle_dict             | 35.7 us                                                               | 35.2 us: 1.02x faster                                                 |
| sympy_integrate         | 22.3 ms                                                               | 22.0 ms: 1.02x faster                                                 |
| sympy_expand            | 508 ms                                                                | 500 ms: 1.02x faster                                                  |
| richards                | 42.0 ms                                                               | 41.5 ms: 1.01x faster                                                 |
| spectral_norm           | 104 ms                                                                | 102 ms: 1.01x faster                                                  |
| coroutines              | 22.9 ms                                                               | 22.7 ms: 1.01x faster                                                 |
| raytrace                | 275 ms                                                                | 273 ms: 1.01x faster                                                  |
| unpickle_pure_python    | 218 us                                                                | 217 us: 1.01x faster                                                  |
| json_loads              | 28.5 us                                                               | 28.3 us: 1.01x faster                                                 |
| scimark_lu              | 125 ms                                                                | 125 ms: 1.01x faster                                                  |
| sympy_str               | 297 ms                                                                | 296 ms: 1.01x faster                                                  |
| fannkuch                | 350 ms                                                                | 348 ms: 1.01x faster                                                  |
| unpickle_list           | 5.15 us                                                               | 5.12 us: 1.01x faster                                                 |
| create_gc_cycles        | 1.75 ms                                                               | 1.74 ms: 1.00x faster                                                 |
| html5lib                | 67.1 ms                                                               | 66.8 ms: 1.00x faster                                                 |
| go                      | 145 ms                                                                | 145 ms: 1.00x faster                                                  |
| gc_traversal            | 3.74 ms                                                               | 3.73 ms: 1.00x faster                                                 |
| bench_thread_pool       | 834 us                                                                | 831 us: 1.00x faster                                                  |
| pidigits                | 185 ms                                                                | 186 ms: 1.00x slower                                                  |
| bpe_tokeniser           | 4.80 sec                                                              | 4.81 sec: 1.00x slower                                                |
| python_startup_no_site  | 7.41 ms                                                               | 7.43 ms: 1.00x slower                                                 |
| python_startup          | 10.8 ms                                                               | 10.9 ms: 1.00x slower                                                 |
| sqlglot_transpile       | 1.60 ms                                                               | 1.60 ms: 1.00x slower                                                 |
| 2to3                    | 272 ms                                                                | 273 ms: 1.00x slower                                                  |
| logging_silent          | 105 ns                                                                | 106 ns: 1.00x slower                                                  |
| asyncio_tcp_ssl         | 1.79 sec                                                              | 1.80 sec: 1.00x slower                                                |
| generators              | 29.4 ms                                                               | 29.6 ms: 1.01x slower                                                 |
| docutils                | 2.86 sec                                                              | 2.87 sec: 1.01x slower                                                |
| dulwich_log             | 67.6 ms                                                               | 68.0 ms: 1.01x slower                                                 |
| pyflate                 | 435 ms                                                                | 438 ms: 1.01x slower                                                  |
| regex_dna               | 221 ms                                                                | 223 ms: 1.01x slower                                                  |
| pickle                  | 11.7 us                                                               | 11.7 us: 1.01x slower                                                 |
| deepcopy_memo           | 28.6 us                                                               | 28.8 us: 1.01x slower                                                 |
| genshi_xml              | 56.8 ms                                                               | 57.4 ms: 1.01x slower                                                 |
| tomli_loads             | 1.93 sec                                                              | 1.94 sec: 1.01x slower                                                |
| genshi_text             | 24.6 ms                                                               | 24.9 ms: 1.01x slower                                                 |
| pickle_list             | 4.93 us                                                               | 4.99 us: 1.01x slower                                                 |
| logging_format          | 6.00 us                                                               | 6.08 us: 1.01x slower                                                 |
| xml_etree_iterparse     | 98.6 ms                                                               | 99.9 ms: 1.01x slower                                                 |
| crypto_pyaes            | 66.4 ms                                                               | 67.4 ms: 1.01x slower                                                 |
| logging_simple          | 5.46 us                                                               | 5.54 us: 1.01x slower                                                 |
| mako                    | 9.54 ms                                                               | 9.70 ms: 1.02x slower                                                 |
| pprint_safe_repr        | 695 ms                                                                | 707 ms: 1.02x slower                                                  |
| scimark_monte_carlo     | 62.2 ms                                                               | 63.2 ms: 1.02x slower                                                 |
| pickle_pure_python      | 291 us                                                                | 297 us: 1.02x slower                                                  |
| deepcopy                | 273 us                                                                | 278 us: 1.02x slower                                                  |
| scimark_sparse_mat_mult | 4.52 ms                                                               | 4.61 ms: 1.02x slower                                                 |
| nqueens                 | 83.5 ms                                                               | 85.5 ms: 1.02x slower                                                 |
| asyncio_tcp             | 481 ms                                                                | 493 ms: 1.02x slower                                                  |
| regex_effbot            | 3.56 ms                                                               | 3.66 ms: 1.03x slower                                                 |
| regex_v8                | 23.1 ms                                                               | 23.8 ms: 1.03x slower                                                 |
| Geometric mean          | (ref)                                                                 | 1.00x slower                                                          |

Benchmark hidden because not significant (42): xml_etree_parse, pycparser, nbody, richards_super, coverage, xml_etree_process, regex_compile, sympy_sum, pylint, async_generators, deepcopy_reduce, xml_etree_generate, sqlglot_optimize, asyncio_websockets, sqlglot_parse, pathlib, scimark_fft, bench_mp_pool, telco, comprehensions, thrift, sqlite_synth, hexiom, typing_runtime_protocols, async_tree_cpu_io_mixed_tg, meteor_contest, float, tornado_http, sqlglot_normalize, async_tree_none, scimark_sor, json, async_tree_io, unpickle, deltablue, async_tree_cpu_io_mixed, async_tree_io_tg, dask, async_tree_memoization, pprint_pformat, async_tree_memoization_tg, async_tree_none_tg

# HPT report

- Reliability score: 97.81% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x