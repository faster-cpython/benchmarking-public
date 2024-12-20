# Results vs. base

- fork: faster-cpython
- ref: use_stackrefs
- machine: linux-x86_64
- commit hash: ad7e1e6
- commit date: 2024-12-20
- overall geometric mean: 1.011x slower
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x slower
- Memory change: 1.00x

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20241220-linux-x86_64-python-128cc47fbd44e3e09c50-3.14.0a3+-128cc47 | bm-20241220-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a3+-ad7e1e6 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| 2to3           | 256 ms                                                                 | 257 ms: 1.01x slower                                                      |
| docutils       | 2.59 sec                                                               | 2.64 sec: 1.02x slower                                                    |
| html5lib       | 62.7 ms                                                                | 63.7 ms: 1.02x slower                                                     |
| sphinx         | 1.02 sec                                                               | 1.04 sec: 1.02x slower                                                    |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                              |

Benchmarks with tag 'asyncio':
==============================

| Benchmark                  | bm-20241220-linux-x86_64-python-128cc47fbd44e3e09c50-3.14.0a3+-128cc47 | bm-20241220-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a3+-ad7e1e6 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| async_tree_cpu_io_mixed_tg | 483 ms                                                                 | 478 ms: 1.01x faster                                                      |
| coroutines                 | 23.6 ms                                                                | 23.8 ms: 1.01x slower                                                     |
| async_generators           | 419 ms                                                                 | 429 ms: 1.02x slower                                                      |
| Geometric mean             | (ref)                                                                  | 1.00x slower                                                              |

Benchmark hidden because not significant (8): async_tree_cpu_io_mixed, async_tree_none_tg, asyncio_websockets, async_tree_io_tg, async_tree_memoization_tg, async_tree_none, async_tree_memoization, async_tree_io

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20241220-linux-x86_64-python-128cc47fbd44e3e09c50-3.14.0a3+-128cc47 | bm-20241220-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a3+-ad7e1e6 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| pidigits       | 187 ms                                                                 | 187 ms: 1.00x slower                                                      |
| float          | 76.5 ms                                                                | 78.1 ms: 1.02x slower                                                     |
| nbody          | 96.3 ms                                                                | 100 ms: 1.04x slower                                                      |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                              |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20241220-linux-x86_64-python-128cc47fbd44e3e09c50-3.14.0a3+-128cc47 | bm-20241220-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a3+-ad7e1e6 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| regex_dna      | 232 ms                                                                 | 223 ms: 1.04x faster                                                      |
| regex_compile  | 128 ms                                                                 | 129 ms: 1.01x slower                                                      |
| regex_v8       | 25.4 ms                                                                | 26.5 ms: 1.04x slower                                                     |
| regex_effbot   | 3.26 ms                                                                | 3.54 ms: 1.09x slower                                                     |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                              |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20241220-linux-x86_64-python-128cc47fbd44e3e09c50-3.14.0a3+-128cc47 | bm-20241220-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a3+-ad7e1e6 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| json_loads           | 26.6 us                                                                | 26.5 us: 1.01x faster                                                     |
| xml_etree_process    | 59.2 ms                                                                | 59.4 ms: 1.00x slower                                                     |
| xml_etree_parse      | 138 ms                                                                 | 138 ms: 1.01x slower                                                      |
| tomli_loads          | 1.97 sec                                                               | 1.98 sec: 1.01x slower                                                    |
| unpickle_pure_python | 218 us                                                                 | 221 us: 1.01x slower                                                      |
| json_dumps           | 11.4 ms                                                                | 11.6 ms: 1.02x slower                                                     |
| pickle_pure_python   | 325 us                                                                 | 331 us: 1.02x slower                                                      |
| xml_etree_iterparse  | 96.3 ms                                                                | 98.2 ms: 1.02x slower                                                     |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (1): xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20241220-linux-x86_64-python-128cc47fbd44e3e09c50-3.14.0a3+-128cc47 | bm-20241220-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a3+-ad7e1e6 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| python_startup_no_site | 7.04 ms                                                                | 7.08 ms: 1.01x slower                                                     |
| python_startup         | 12.8 ms                                                                | 12.9 ms: 1.01x slower                                                     |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                              |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20241220-linux-x86_64-python-128cc47fbd44e3e09c50-3.14.0a3+-128cc47 | bm-20241220-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a3+-ad7e1e6 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| genshi_text     | 22.2 ms                                                                | 22.3 ms: 1.01x slower                                                     |
| genshi_xml      | 49.6 ms                                                                | 50.6 ms: 1.02x slower                                                     |
| mako            | 11.7 ms                                                                | 12.2 ms: 1.04x slower                                                     |
| django_template | 31.6 ms                                                                | 33.0 ms: 1.04x slower                                                     |
| Geometric mean  | (ref)                                                                  | 1.03x slower                                                              |

All benchmarks:
===============

| Benchmark                  | bm-20241220-linux-x86_64-python-128cc47fbd44e3e09c50-3.14.0a3+-128cc47 | bm-20241220-linux-x86_64-faster%2dcpython-use_stackrefs-3.14.0a3+-ad7e1e6 |
|----------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------------:|
| logging_silent             | 109 ns                                                                 | 100 ns: 1.08x faster                                                      |
| mdp                        | 2.64 sec                                                               | 2.48 sec: 1.06x faster                                                    |
| regex_dna                  | 232 ms                                                                 | 223 ms: 1.04x faster                                                      |
| pycparser                  | 1.17 sec                                                               | 1.14 sec: 1.03x faster                                                    |
| spectral_norm              | 108 ms                                                                 | 106 ms: 1.01x faster                                                      |
| go                         | 119 ms                                                                 | 117 ms: 1.01x faster                                                      |
| richards                   | 45.0 ms                                                                | 44.5 ms: 1.01x faster                                                     |
| async_tree_cpu_io_mixed_tg | 483 ms                                                                 | 478 ms: 1.01x faster                                                      |
| pathlib                    | 16.9 ms                                                                | 16.8 ms: 1.01x faster                                                     |
| create_gc_cycles           | 2.46 ms                                                                | 2.44 ms: 1.01x faster                                                     |
| deepcopy_memo              | 31.2 us                                                                | 31.0 us: 1.01x faster                                                     |
| json_loads                 | 26.6 us                                                                | 26.5 us: 1.01x faster                                                     |
| gc_traversal               | 4.92 ms                                                                | 4.92 ms: 1.00x faster                                                     |
| pidigits                   | 187 ms                                                                 | 187 ms: 1.00x slower                                                      |
| meteor_contest             | 107 ms                                                                 | 107 ms: 1.00x slower                                                      |
| dulwich_log                | 64.4 ms                                                                | 64.7 ms: 1.00x slower                                                     |
| xml_etree_process          | 59.2 ms                                                                | 59.4 ms: 1.00x slower                                                     |
| sympy_integrate            | 20.0 ms                                                                | 20.0 ms: 1.00x slower                                                     |
| crypto_pyaes               | 73.3 ms                                                                | 73.7 ms: 1.01x slower                                                     |
| xml_etree_parse            | 138 ms                                                                 | 138 ms: 1.01x slower                                                      |
| python_startup_no_site     | 7.04 ms                                                                | 7.08 ms: 1.01x slower                                                     |
| 2to3                       | 256 ms                                                                 | 257 ms: 1.01x slower                                                      |
| coroutines                 | 23.6 ms                                                                | 23.8 ms: 1.01x slower                                                     |
| tomli_loads                | 1.97 sec                                                               | 1.98 sec: 1.01x slower                                                    |
| sqlite_synth               | 2.80 us                                                                | 2.81 us: 1.01x slower                                                     |
| telco                      | 7.82 ms                                                                | 7.88 ms: 1.01x slower                                                     |
| genshi_text                | 22.2 ms                                                                | 22.3 ms: 1.01x slower                                                     |
| bench_mp_pool              | 81.3 ms                                                                | 81.9 ms: 1.01x slower                                                     |
| python_startup             | 12.8 ms                                                                | 12.9 ms: 1.01x slower                                                     |
| sympy_sum                  | 148 ms                                                                 | 149 ms: 1.01x slower                                                      |
| logging_format             | 6.27 us                                                                | 6.33 us: 1.01x slower                                                     |
| regex_compile              | 128 ms                                                                 | 129 ms: 1.01x slower                                                      |
| many_optionals             | 952 us                                                                 | 962 us: 1.01x slower                                                      |
| sqlglot_transpile          | 1.59 ms                                                                | 1.61 ms: 1.01x slower                                                     |
| sqlalchemy_imperative      | 16.6 ms                                                                | 16.7 ms: 1.01x slower                                                     |
| sympy_str                  | 268 ms                                                                 | 272 ms: 1.01x slower                                                      |
| bench_thread_pool          | 863 us                                                                 | 873 us: 1.01x slower                                                      |
| sqlglot_parse              | 1.27 ms                                                                | 1.29 ms: 1.01x slower                                                     |
| sympy_expand               | 457 ms                                                                 | 463 ms: 1.01x slower                                                      |
| hexiom                     | 6.33 ms                                                                | 6.41 ms: 1.01x slower                                                     |
| deltablue                  | 3.29 ms                                                                | 3.34 ms: 1.01x slower                                                     |
| unpickle_pure_python       | 218 us                                                                 | 221 us: 1.01x slower                                                      |
| sqlglot_optimize           | 52.7 ms                                                                | 53.5 ms: 1.02x slower                                                     |
| typing_runtime_protocols   | 162 us                                                                 | 165 us: 1.02x slower                                                      |
| json_dumps                 | 11.4 ms                                                                | 11.6 ms: 1.02x slower                                                     |
| chaos                      | 61.6 ms                                                                | 62.6 ms: 1.02x slower                                                     |
| subparsers                 | 20.6 ms                                                                | 20.9 ms: 1.02x slower                                                     |
| generators                 | 27.9 ms                                                                | 28.3 ms: 1.02x slower                                                     |
| bpe_tokeniser              | 4.53 sec                                                               | 4.61 sec: 1.02x slower                                                    |
| html5lib                   | 62.7 ms                                                                | 63.7 ms: 1.02x slower                                                     |
| pickle_pure_python         | 325 us                                                                 | 331 us: 1.02x slower                                                      |
| scimark_fft                | 346 ms                                                                 | 353 ms: 1.02x slower                                                      |
| genshi_xml                 | 49.6 ms                                                                | 50.6 ms: 1.02x slower                                                     |
| sphinx                     | 1.02 sec                                                               | 1.04 sec: 1.02x slower                                                    |
| xml_etree_iterparse        | 96.3 ms                                                                | 98.2 ms: 1.02x slower                                                     |
| float                      | 76.5 ms                                                                | 78.1 ms: 1.02x slower                                                     |
| docutils                   | 2.59 sec                                                               | 2.64 sec: 1.02x slower                                                    |
| async_generators           | 419 ms                                                                 | 429 ms: 1.02x slower                                                      |
| deepcopy                   | 261 us                                                                 | 267 us: 1.02x slower                                                      |
| sqlalchemy_declarative     | 129 ms                                                                 | 132 ms: 1.02x slower                                                      |
| logging_simple             | 5.63 us                                                                | 5.77 us: 1.03x slower                                                     |
| sqlglot_normalize          | 104 ms                                                                 | 107 ms: 1.03x slower                                                      |
| scimark_monte_carlo        | 67.9 ms                                                                | 69.8 ms: 1.03x slower                                                     |
| scimark_sparse_mat_mult    | 4.76 ms                                                                | 4.90 ms: 1.03x slower                                                     |
| comprehensions             | 16.9 us                                                                | 17.5 us: 1.03x slower                                                     |
| pyflate                    | 458 ms                                                                 | 475 ms: 1.04x slower                                                      |
| pprint_pformat             | 1.50 sec                                                               | 1.55 sec: 1.04x slower                                                    |
| nbody                      | 96.3 ms                                                                | 100 ms: 1.04x slower                                                      |
| mako                       | 11.7 ms                                                                | 12.2 ms: 1.04x slower                                                     |
| nqueens                    | 80.1 ms                                                                | 83.5 ms: 1.04x slower                                                     |
| scimark_lu                 | 114 ms                                                                 | 119 ms: 1.04x slower                                                      |
| django_template            | 31.6 ms                                                                | 33.0 ms: 1.04x slower                                                     |
| regex_v8                   | 25.4 ms                                                                | 26.5 ms: 1.04x slower                                                     |
| pprint_safe_repr           | 729 ms                                                                 | 767 ms: 1.05x slower                                                      |
| fannkuch                   | 399 ms                                                                 | 427 ms: 1.07x slower                                                      |
| regex_effbot               | 3.26 ms                                                                | 3.54 ms: 1.09x slower                                                     |
| Geometric mean             | (ref)                                                                  | 1.01x slower                                                              |

Benchmark hidden because not significant (22): async_tree_cpu_io_mixed, deepcopy_reduce, richards_super, xml_etree_generate, raytrace, djangocms, async_tree_none_tg, asyncio_websockets, mypy2, shortest_path, coverage, async_tree_io_tg, thrift, json, connected_components, async_tree_memoization_tg, async_tree_none, scimark_sor, pylint, async_tree_memoization, k_core, async_tree_io

- Geometric mean (including insignificant results): 1.011x slower

# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x

# Memory
- memory change: 1.00x