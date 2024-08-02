# Results vs. base

- fork: saulshanabrook
- ref: optimzer_type_versio
- machine: linux-x86_64
- commit hash: 1520928
- commit date: 2024-05-20
- overall geometric mean: 1.00x faster
- HPT reliability: 66.55%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20240520-linux-x86_64-python-642b25b9a82c368b0457-3.14.0a0-642b25b | bm-20240520-linux-x86_64-saulshanabrook-optimzer_type_versio-3.14.0a0-1520928 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| docutils       | 2.94 sec                                                              | 2.95 sec: 1.01x slower                                                        |
| html5lib       | 69.4 ms                                                               | 68.4 ms: 1.02x faster                                                         |
| tornado_http   | 96.5 ms                                                               | 97.0 ms: 1.01x slower                                                         |
| Geometric mean | (ref)                                                                 | 1.00x faster                                                                  |

Benchmark hidden because not significant (2): 2to3, chameleon

Benchmarks with tag 'asyncio':
==============================

Benchmark hidden because not significant (8): async_tree_io, async_tree_io_tg, async_tree_memoization_tg, async_tree_memoization, async_tree_none_tg, async_tree_cpu_io_mixed, async_tree_none, async_tree_cpu_io_mixed_tg

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20240520-linux-x86_64-python-642b25b9a82c368b0457-3.14.0a0-642b25b | bm-20240520-linux-x86_64-saulshanabrook-optimzer_type_versio-3.14.0a0-1520928 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| nbody          | 84.1 ms                                                               | 81.3 ms: 1.03x faster                                                         |
| float          | 72.8 ms                                                               | 72.4 ms: 1.01x faster                                                         |
| pidigits       | 188 ms                                                                | 188 ms: 1.00x faster                                                          |
| Geometric mean | (ref)                                                                 | 1.01x faster                                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20240520-linux-x86_64-python-642b25b9a82c368b0457-3.14.0a0-642b25b | bm-20240520-linux-x86_64-saulshanabrook-optimzer_type_versio-3.14.0a0-1520928 |
|----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot   | 3.86 ms                                                               | 3.67 ms: 1.05x faster                                                         |
| regex_v8       | 25.6 ms                                                               | 25.2 ms: 1.01x faster                                                         |
| regex_dna      | 229 ms                                                                | 226 ms: 1.01x faster                                                          |
| Geometric mean | (ref)                                                                 | 1.02x faster                                                                  |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20240520-linux-x86_64-python-642b25b9a82c368b0457-3.14.0a0-642b25b | bm-20240520-linux-x86_64-saulshanabrook-optimzer_type_versio-3.14.0a0-1520928 |
|---------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| pickle_pure_python  | 301 us                                                                | 295 us: 1.02x faster                                                          |
| json_loads          | 28.9 us                                                               | 28.6 us: 1.01x faster                                                         |
| pickle_dict         | 36.3 us                                                               | 36.1 us: 1.01x faster                                                         |
| xml_etree_iterparse | 101 ms                                                                | 101 ms: 1.00x slower                                                          |
| tomli_loads         | 1.94 sec                                                              | 1.96 sec: 1.01x slower                                                        |
| xml_etree_parse     | 150 ms                                                                | 153 ms: 1.02x slower                                                          |
| pickle_list         | 5.25 us                                                               | 5.38 us: 1.03x slower                                                         |
| unpickle_list       | 5.18 us                                                               | 5.33 us: 1.03x slower                                                         |
| unpickle            | 15.4 us                                                               | 16.7 us: 1.08x slower                                                         |
| Geometric mean      | (ref)                                                                 | 1.01x slower                                                                  |

Benchmark hidden because not significant (5): unpickle_pure_python, json_dumps, xml_etree_process, pickle, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20240520-linux-x86_64-python-642b25b9a82c368b0457-3.14.0a0-642b25b | bm-20240520-linux-x86_64-saulshanabrook-optimzer_type_versio-3.14.0a0-1520928 |
|------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| python_startup         | 10.9 ms                                                               | 10.9 ms: 1.01x slower                                                         |
| python_startup_no_site | 7.59 ms                                                               | 7.63 ms: 1.01x slower                                                         |
| Geometric mean         | (ref)                                                                 | 1.01x slower                                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20240520-linux-x86_64-python-642b25b9a82c368b0457-3.14.0a0-642b25b | bm-20240520-linux-x86_64-saulshanabrook-optimzer_type_versio-3.14.0a0-1520928 |
|-----------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| mako            | 10.4 ms                                                               | 9.99 ms: 1.04x faster                                                         |
| genshi_text     | 25.2 ms                                                               | 24.6 ms: 1.02x faster                                                         |
| django_template | 35.8 ms                                                               | 36.6 ms: 1.02x slower                                                         |
| Geometric mean  | (ref)                                                                 | 1.01x faster                                                                  |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark                | bm-20240520-linux-x86_64-python-642b25b9a82c368b0457-3.14.0a0-642b25b | bm-20240520-linux-x86_64-saulshanabrook-optimzer_type_versio-3.14.0a0-1520928 |
|--------------------------|:---------------------------------------------------------------------:|:-----------------------------------------------------------------------------:|
| regex_effbot             | 3.86 ms                                                               | 3.67 ms: 1.05x faster                                                         |
| mako                     | 10.4 ms                                                               | 9.99 ms: 1.04x faster                                                         |
| nbody                    | 84.1 ms                                                               | 81.3 ms: 1.03x faster                                                         |
| logging_format           | 6.47 us                                                               | 6.31 us: 1.03x faster                                                         |
| genshi_text              | 25.2 ms                                                               | 24.6 ms: 1.02x faster                                                         |
| pickle_pure_python       | 301 us                                                                | 295 us: 1.02x faster                                                          |
| logging_simple           | 5.76 us                                                               | 5.65 us: 1.02x faster                                                         |
| typing_runtime_protocols | 173 us                                                                | 170 us: 1.02x faster                                                          |
| spectral_norm            | 102 ms                                                                | 100 ms: 1.02x faster                                                          |
| scimark_fft              | 323 ms                                                                | 318 ms: 1.02x faster                                                          |
| async_generators         | 469 ms                                                                | 461 ms: 1.02x faster                                                          |
| html5lib                 | 69.4 ms                                                               | 68.4 ms: 1.02x faster                                                         |
| coverage                 | 94.8 ms                                                               | 93.4 ms: 1.02x faster                                                         |
| deepcopy                 | 369 us                                                                | 364 us: 1.02x faster                                                          |
| pprint_pformat           | 1.48 sec                                                              | 1.45 sec: 1.01x faster                                                        |
| regex_v8                 | 25.6 ms                                                               | 25.2 ms: 1.01x faster                                                         |
| pathlib                  | 16.8 ms                                                               | 16.5 ms: 1.01x faster                                                         |
| richards_super           | 48.1 ms                                                               | 47.5 ms: 1.01x faster                                                         |
| regex_dna                | 229 ms                                                                | 226 ms: 1.01x faster                                                          |
| deepcopy_memo            | 38.1 us                                                               | 37.7 us: 1.01x faster                                                         |
| json_loads               | 28.9 us                                                               | 28.6 us: 1.01x faster                                                         |
| richards                 | 41.7 ms                                                               | 41.3 ms: 1.01x faster                                                         |
| telco                    | 8.30 ms                                                               | 8.23 ms: 1.01x faster                                                         |
| thrift                   | 823 us                                                                | 816 us: 1.01x faster                                                          |
| pickle_dict              | 36.3 us                                                               | 36.1 us: 1.01x faster                                                         |
| float                    | 72.8 ms                                                               | 72.4 ms: 1.01x faster                                                         |
| pidigits                 | 188 ms                                                                | 188 ms: 1.00x faster                                                          |
| asyncio_tcp_ssl          | 1.86 sec                                                              | 1.86 sec: 1.00x slower                                                        |
| sympy_expand             | 510 ms                                                                | 512 ms: 1.00x slower                                                          |
| xml_etree_iterparse      | 101 ms                                                                | 101 ms: 1.00x slower                                                          |
| tornado_http             | 96.5 ms                                                               | 97.0 ms: 1.01x slower                                                         |
| docutils                 | 2.94 sec                                                              | 2.95 sec: 1.01x slower                                                        |
| sympy_str                | 302 ms                                                                | 303 ms: 1.01x slower                                                          |
| python_startup           | 10.9 ms                                                               | 10.9 ms: 1.01x slower                                                         |
| python_startup_no_site   | 7.59 ms                                                               | 7.63 ms: 1.01x slower                                                         |
| gc_traversal             | 3.89 ms                                                               | 3.92 ms: 1.01x slower                                                         |
| comprehensions           | 16.7 us                                                               | 16.8 us: 1.01x slower                                                         |
| go                       | 147 ms                                                                | 148 ms: 1.01x slower                                                          |
| sqlglot_optimize         | 56.6 ms                                                               | 57.0 ms: 1.01x slower                                                         |
| dulwich_log              | 68.9 ms                                                               | 69.5 ms: 1.01x slower                                                         |
| logging_silent           | 107 ns                                                                | 108 ns: 1.01x slower                                                          |
| chaos                    | 59.5 ms                                                               | 60.1 ms: 1.01x slower                                                         |
| asyncio_tcp              | 521 ms                                                                | 526 ms: 1.01x slower                                                          |
| sqlglot_normalize        | 113 ms                                                                | 115 ms: 1.01x slower                                                          |
| crypto_pyaes             | 67.6 ms                                                               | 68.5 ms: 1.01x slower                                                         |
| tomli_loads              | 1.94 sec                                                              | 1.96 sec: 1.01x slower                                                        |
| create_gc_cycles         | 1.79 ms                                                               | 1.82 ms: 1.02x slower                                                         |
| fannkuch                 | 353 ms                                                                | 361 ms: 1.02x slower                                                          |
| scimark_sparse_mat_mult  | 4.45 ms                                                               | 4.54 ms: 1.02x slower                                                         |
| xml_etree_parse          | 150 ms                                                                | 153 ms: 1.02x slower                                                          |
| django_template          | 35.8 ms                                                               | 36.6 ms: 1.02x slower                                                         |
| pickle_list              | 5.25 us                                                               | 5.38 us: 1.03x slower                                                         |
| coroutines               | 23.4 ms                                                               | 24.0 ms: 1.03x slower                                                         |
| unpickle_list            | 5.18 us                                                               | 5.33 us: 1.03x slower                                                         |
| pyflate                  | 445 ms                                                                | 470 ms: 1.06x slower                                                          |
| unpickle                 | 15.4 us                                                               | 16.7 us: 1.08x slower                                                         |
| Geometric mean           | (ref)                                                                 | 1.00x faster                                                                  |

Benchmark hidden because not significant (40): async_tree_io, async_tree_io_tg, pprint_safe_repr, deepcopy_reduce, unpickle_pure_python, pycparser, async_tree_memoization_tg, chameleon, json, scimark_lu, nqueens, generators, sqlite_synth, raytrace, bench_thread_pool, async_tree_memoization, json_dumps, sympy_sum, async_tree_none_tg, asyncio_websockets, deltablue, sqlglot_parse, scimark_sor, meteor_contest, scimark_monte_carlo, 2to3, async_tree_cpu_io_mixed, sympy_integrate, sqlglot_transpile, bench_mp_pool, regex_compile, async_tree_none, async_tree_cpu_io_mixed_tg, dask, genshi_xml, pylint, xml_etree_process, flaskblogging, pickle, xml_etree_generate
Ignored benchmarks (2) of results/bm-20240520-3.14.0a0-642b25b-JIT/bm-20240520-linux-x86_64-python-642b25b9a82c368b0457-3.14.0a0-642b25b.json: hexiom, mdp

# HPT report

- Reliability score: 66.55% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x