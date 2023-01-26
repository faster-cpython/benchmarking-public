
# Results vs. base

- fork: brandtbucher
- ref: load_attr_managed_di
- machine: linux-x86_64
- commit hash: d5db69f
- commit date: 2023-01-17
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230124-linux-x86_64-python-1a9d8c750be83e6abb65-3.12.0a4+-1a9d8c7 | bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4+-d5db69f |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3           | 252 ms                                                                 | 250 ms: 1.01x faster                                                         |
| docutils       | 2.58 sec                                                               | 2.52 sec: 1.02x faster                                                       |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                                 |

Benchmark hidden because not significant (3): chameleon, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230124-linux-x86_64-python-1a9d8c750be83e6abb65-3.12.0a4+-1a9d8c7 | bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4+-d5db69f |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| float          | 72.1 ms                                                                | 72.8 ms: 1.01x slower                                                        |
| nbody          | 93.9 ms                                                                | 92.7 ms: 1.01x faster                                                        |
| pidigits       | 189 ms                                                                 | 198 ms: 1.04x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230124-linux-x86_64-python-1a9d8c750be83e6abb65-3.12.0a4+-1a9d8c7 | bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4+-d5db69f |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                                 | 126 ms: 1.02x faster                                                         |
| regex_dna      | 211 ms                                                                 | 208 ms: 1.01x faster                                                         |
| regex_effbot   | 3.57 ms                                                                | 3.60 ms: 1.01x slower                                                        |
| regex_v8       | 22.4 ms                                                                | 21.2 ms: 1.06x faster                                                        |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230124-linux-x86_64-python-1a9d8c750be83e6abb65-3.12.0a4+-1a9d8c7 | bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4+-d5db69f |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| json_dumps           | 9.30 ms                                                                | 9.42 ms: 1.01x slower                                                        |
| json_loads           | 23.7 us                                                                | 23.9 us: 1.01x slower                                                        |
| pickle               | 10.1 us                                                                | 10.3 us: 1.01x slower                                                        |
| pickle_dict          | 30.0 us                                                                | 31.0 us: 1.03x slower                                                        |
| pickle_list          | 4.00 us                                                                | 4.08 us: 1.02x slower                                                        |
| pickle_pure_python   | 283 us                                                                 | 284 us: 1.01x slower                                                         |
| unpickle             | 13.0 us                                                                | 13.1 us: 1.01x slower                                                        |
| unpickle_list        | 5.18 us                                                                | 5.07 us: 1.02x faster                                                        |
| unpickle_pure_python | 197 us                                                                 | 196 us: 1.00x faster                                                         |
| xml_etree_iterparse  | 107 ms                                                                 | 103 ms: 1.04x faster                                                         |
| xml_etree_generate   | 77.8 ms                                                                | 77.3 ms: 1.01x faster                                                        |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (2): xml_etree_parse, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230124-linux-x86_64-python-1a9d8c750be83e6abb65-3.12.0a4+-1a9d8c7 | bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4+-d5db69f |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| python_startup         | 8.93 ms                                                                | 8.97 ms: 1.00x slower                                                        |
| python_startup_no_site | 6.45 ms                                                                | 6.49 ms: 1.01x slower                                                        |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230124-linux-x86_64-python-1a9d8c750be83e6abb65-3.12.0a4+-1a9d8c7 | bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4+-d5db69f |
|-----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| django_template | 32.7 ms                                                                | 33.2 ms: 1.02x slower                                                        |
| genshi_text     | 20.8 ms                                                                | 21.2 ms: 1.02x slower                                                        |
| genshi_xml      | 47.4 ms                                                                | 46.8 ms: 1.01x faster                                                        |
| mako            | 9.64 ms                                                                | 9.56 ms: 1.01x faster                                                        |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                                 |

All benchmarks:
===============

| Benchmark              | bm-20230124-linux-x86_64-python-1a9d8c750be83e6abb65-3.12.0a4+-1a9d8c7 | bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4+-d5db69f |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| 2to3                   | 252 ms                                                                 | 250 ms: 1.01x faster                                                         |
| aiohttp                | 995 us                                                                 | 990 us: 1.01x faster                                                         |
| async_tree_io          | 1.31 sec                                                               | 1.33 sec: 1.01x slower                                                       |
| async_tree_memoization | 639 ms                                                                 | 616 ms: 1.04x faster                                                         |
| asyncio_tcp            | 495 ms                                                                 | 498 ms: 1.01x slower                                                         |
| chaos                  | 63.9 ms                                                                | 64.7 ms: 1.01x slower                                                        |
| bench_thread_pool      | 778 us                                                                 | 773 us: 1.01x faster                                                         |
| coroutines             | 25.9 ms                                                                | 25.3 ms: 1.03x faster                                                        |
| coverage               | 96.3 ms                                                                | 97.1 ms: 1.01x slower                                                        |
| crypto_pyaes           | 71.4 ms                                                                | 73.0 ms: 1.02x slower                                                        |
| dask                   | 496 ms                                                                 | 504 ms: 1.02x slower                                                         |
| deepcopy               | 330 us                                                                 | 325 us: 1.01x faster                                                         |
| django_template        | 32.7 ms                                                                | 33.2 ms: 1.02x slower                                                        |
| docutils               | 2.58 sec                                                               | 2.52 sec: 1.02x faster                                                       |
| fannkuch               | 355 ms                                                                 | 382 ms: 1.07x slower                                                         |
| float                  | 72.1 ms                                                                | 72.8 ms: 1.01x slower                                                        |
| create_gc_cycles       | 1.44 ms                                                                | 1.48 ms: 1.03x slower                                                        |
| gc_traversal           | 3.82 ms                                                                | 3.81 ms: 1.00x faster                                                        |
| generators             | 75.2 ms                                                                | 76.8 ms: 1.02x slower                                                        |
| genshi_text            | 20.8 ms                                                                | 21.2 ms: 1.02x slower                                                        |
| genshi_xml             | 47.4 ms                                                                | 46.8 ms: 1.01x faster                                                        |
| go                     | 138 ms                                                                 | 178 ms: 1.28x slower                                                         |
| gunicorn               | 1.08 ms                                                                | 1.07 ms: 1.01x faster                                                        |
| hexiom                 | 5.96 ms                                                                | 5.99 ms: 1.00x slower                                                        |
| json                   | 4.63 ms                                                                | 4.56 ms: 1.02x faster                                                        |
| json_dumps             | 9.30 ms                                                                | 9.42 ms: 1.01x slower                                                        |
| json_loads             | 23.7 us                                                                | 23.9 us: 1.01x slower                                                        |
| logging_format         | 6.45 us                                                                | 6.20 us: 1.04x faster                                                        |
| logging_silent         | 90.8 ns                                                                | 92.1 ns: 1.01x slower                                                        |
| logging_simple         | 5.80 us                                                                | 5.65 us: 1.03x faster                                                        |
| mako                   | 9.64 ms                                                                | 9.56 ms: 1.01x faster                                                        |
| mdp                    | 2.66 sec                                                               | 2.57 sec: 1.04x faster                                                       |
| nbody                  | 93.9 ms                                                                | 92.7 ms: 1.01x faster                                                        |
| nqueens                | 76.2 ms                                                                | 78.6 ms: 1.03x slower                                                        |
| pathlib                | 17.6 ms                                                                | 17.9 ms: 1.02x slower                                                        |
| pickle                 | 10.1 us                                                                | 10.3 us: 1.01x slower                                                        |
| pickle_dict            | 30.0 us                                                                | 31.0 us: 1.03x slower                                                        |
| pickle_list            | 4.00 us                                                                | 4.08 us: 1.02x slower                                                        |
| pickle_pure_python     | 283 us                                                                 | 284 us: 1.01x slower                                                         |
| pidigits               | 189 ms                                                                 | 198 ms: 1.04x slower                                                         |
| pprint_safe_repr       | 684 ms                                                                 | 671 ms: 1.02x faster                                                         |
| pprint_pformat         | 1.39 sec                                                               | 1.38 sec: 1.01x faster                                                       |
| pycparser              | 1.14 sec                                                               | 1.12 sec: 1.02x faster                                                       |
| pyflate                | 416 ms                                                                 | 405 ms: 1.03x faster                                                         |
| python_startup         | 8.93 ms                                                                | 8.97 ms: 1.00x slower                                                        |
| python_startup_no_site | 6.45 ms                                                                | 6.49 ms: 1.01x slower                                                        |
| regex_compile          | 129 ms                                                                 | 126 ms: 1.02x faster                                                         |
| regex_dna              | 211 ms                                                                 | 208 ms: 1.01x faster                                                         |
| regex_effbot           | 3.57 ms                                                                | 3.60 ms: 1.01x slower                                                        |
| regex_v8               | 22.4 ms                                                                | 21.2 ms: 1.06x faster                                                        |
| richards               | 42.3 ms                                                                | 43.1 ms: 1.02x slower                                                        |
| scimark_fft            | 305 ms                                                                 | 303 ms: 1.01x faster                                                         |
| scimark_lu             | 107 ms                                                                 | 105 ms: 1.02x faster                                                         |
| scimark_monte_carlo    | 65.8 ms                                                                | 65.5 ms: 1.01x faster                                                        |
| spectral_norm          | 96.2 ms                                                                | 99.2 ms: 1.03x slower                                                        |
| sqlglot_optimize       | 51.2 ms                                                                | 50.8 ms: 1.01x faster                                                        |
| sqlglot_normalize      | 105 ms                                                                 | 104 ms: 1.00x faster                                                         |
| sqlite_synth           | 2.58 us                                                                | 2.61 us: 1.01x slower                                                        |
| sympy_expand           | 451 ms                                                                 | 449 ms: 1.01x faster                                                         |
| sympy_integrate        | 19.7 ms                                                                | 19.6 ms: 1.01x faster                                                        |
| sympy_sum              | 155 ms                                                                 | 154 ms: 1.01x faster                                                         |
| telco                  | 6.28 ms                                                                | 6.41 ms: 1.02x slower                                                        |
| unpack_sequence        | 41.3 ns                                                                | 41.7 ns: 1.01x slower                                                        |
| unpickle               | 13.0 us                                                                | 13.1 us: 1.01x slower                                                        |
| unpickle_list          | 5.18 us                                                                | 5.07 us: 1.02x faster                                                        |
| unpickle_pure_python   | 197 us                                                                 | 196 us: 1.00x faster                                                         |
| xml_etree_iterparse    | 107 ms                                                                 | 103 ms: 1.04x faster                                                         |
| xml_etree_generate     | 77.8 ms                                                                | 77.3 ms: 1.01x faster                                                        |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (23): async_generators, async_tree_none, async_tree_cpu_io_mixed, chameleon, bench_mp_pool, deepcopy_reduce, deepcopy_memo, deltablue, djangocms, dulwich_log, html5lib, meteor_contest, mypy, raytrace, scimark_sor, scimark_sparse_mat_mult, sqlglot_parse, sqlglot_transpile, sympy_str, thrift, tornado_http, xml_etree_parse, xml_etree_process
