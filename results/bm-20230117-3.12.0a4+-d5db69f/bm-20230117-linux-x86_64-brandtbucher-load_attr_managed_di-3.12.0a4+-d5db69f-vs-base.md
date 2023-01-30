
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
| nbody          | 93.9 ms                                                                | 92.7 ms: 1.01x faster                                                        |
| float          | 72.1 ms                                                                | 72.8 ms: 1.01x slower                                                        |
| pidigits       | 189 ms                                                                 | 198 ms: 1.04x slower                                                         |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                                 |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230124-linux-x86_64-python-1a9d8c750be83e6abb65-3.12.0a4+-1a9d8c7 | bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4+-d5db69f |
|----------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8       | 22.4 ms                                                                | 21.2 ms: 1.06x faster                                                        |
| regex_compile  | 129 ms                                                                 | 126 ms: 1.02x faster                                                         |
| regex_dna      | 211 ms                                                                 | 208 ms: 1.01x faster                                                         |
| regex_effbot   | 3.57 ms                                                                | 3.60 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                                 |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230124-linux-x86_64-python-1a9d8c750be83e6abb65-3.12.0a4+-1a9d8c7 | bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4+-d5db69f |
|----------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| xml_etree_iterparse  | 107 ms                                                                 | 103 ms: 1.04x faster                                                         |
| unpickle_list        | 5.18 us                                                                | 5.07 us: 1.02x faster                                                        |
| xml_etree_generate   | 77.8 ms                                                                | 77.3 ms: 1.01x faster                                                        |
| unpickle_pure_python | 197 us                                                                 | 196 us: 1.00x faster                                                         |
| pickle_pure_python   | 283 us                                                                 | 284 us: 1.01x slower                                                         |
| json_loads           | 23.7 us                                                                | 23.9 us: 1.01x slower                                                        |
| unpickle             | 13.0 us                                                                | 13.1 us: 1.01x slower                                                        |
| json_dumps           | 9.30 ms                                                                | 9.42 ms: 1.01x slower                                                        |
| pickle               | 10.1 us                                                                | 10.3 us: 1.01x slower                                                        |
| pickle_list          | 4.00 us                                                                | 4.08 us: 1.02x slower                                                        |
| pickle_dict          | 30.0 us                                                                | 31.0 us: 1.03x slower                                                        |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (2): xml_etree_process, xml_etree_parse

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
| genshi_xml      | 47.4 ms                                                                | 46.8 ms: 1.01x faster                                                        |
| mako            | 9.64 ms                                                                | 9.56 ms: 1.01x faster                                                        |
| django_template | 32.7 ms                                                                | 33.2 ms: 1.02x slower                                                        |
| genshi_text     | 20.8 ms                                                                | 21.2 ms: 1.02x slower                                                        |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                                 |

All benchmarks:
===============

| Benchmark              | bm-20230124-linux-x86_64-python-1a9d8c750be83e6abb65-3.12.0a4+-1a9d8c7 | bm-20230117-linux-x86_64-brandtbucher-load_attr_managed_di-3.12.0a4+-d5db69f |
|------------------------|:----------------------------------------------------------------------:|:----------------------------------------------------------------------------:|
| regex_v8               | 22.4 ms                                                                | 21.2 ms: 1.06x faster                                                        |
| xml_etree_iterparse    | 107 ms                                                                 | 103 ms: 1.04x faster                                                         |
| logging_format         | 6.45 us                                                                | 6.20 us: 1.04x faster                                                        |
| async_tree_memoization | 639 ms                                                                 | 616 ms: 1.04x faster                                                         |
| mdp                    | 2.66 sec                                                               | 2.57 sec: 1.04x faster                                                       |
| pyflate                | 416 ms                                                                 | 405 ms: 1.03x faster                                                         |
| logging_simple         | 5.80 us                                                                | 5.65 us: 1.03x faster                                                        |
| coroutines             | 25.9 ms                                                                | 25.3 ms: 1.03x faster                                                        |
| docutils               | 2.58 sec                                                               | 2.52 sec: 1.02x faster                                                       |
| pycparser              | 1.14 sec                                                               | 1.12 sec: 1.02x faster                                                       |
| unpickle_list          | 5.18 us                                                                | 5.07 us: 1.02x faster                                                        |
| pprint_safe_repr       | 684 ms                                                                 | 671 ms: 1.02x faster                                                         |
| regex_compile          | 129 ms                                                                 | 126 ms: 1.02x faster                                                         |
| json                   | 4.63 ms                                                                | 4.56 ms: 1.02x faster                                                        |
| scimark_lu             | 107 ms                                                                 | 105 ms: 1.02x faster                                                         |
| deepcopy               | 330 us                                                                 | 325 us: 1.01x faster                                                         |
| genshi_xml             | 47.4 ms                                                                | 46.8 ms: 1.01x faster                                                        |
| nbody                  | 93.9 ms                                                                | 92.7 ms: 1.01x faster                                                        |
| regex_dna              | 211 ms                                                                 | 208 ms: 1.01x faster                                                         |
| gunicorn               | 1.08 ms                                                                | 1.07 ms: 1.01x faster                                                        |
| pprint_pformat         | 1.39 sec                                                               | 1.38 sec: 1.01x faster                                                       |
| mako                   | 9.64 ms                                                                | 9.56 ms: 1.01x faster                                                        |
| scimark_fft            | 305 ms                                                                 | 303 ms: 1.01x faster                                                         |
| sqlglot_optimize       | 51.2 ms                                                                | 50.8 ms: 1.01x faster                                                        |
| sympy_sum              | 155 ms                                                                 | 154 ms: 1.01x faster                                                         |
| bench_thread_pool      | 778 us                                                                 | 773 us: 1.01x faster                                                         |
| xml_etree_generate     | 77.8 ms                                                                | 77.3 ms: 1.01x faster                                                        |
| 2to3                   | 252 ms                                                                 | 250 ms: 1.01x faster                                                         |
| scimark_monte_carlo    | 65.8 ms                                                                | 65.5 ms: 1.01x faster                                                        |
| aiohttp                | 995 us                                                                 | 990 us: 1.01x faster                                                         |
| sympy_integrate        | 19.7 ms                                                                | 19.6 ms: 1.01x faster                                                        |
| sympy_expand           | 451 ms                                                                 | 449 ms: 1.01x faster                                                         |
| unpickle_pure_python   | 197 us                                                                 | 196 us: 1.00x faster                                                         |
| sqlglot_normalize      | 105 ms                                                                 | 104 ms: 1.00x faster                                                         |
| gc_traversal           | 3.82 ms                                                                | 3.81 ms: 1.00x faster                                                        |
| python_startup         | 8.93 ms                                                                | 8.97 ms: 1.00x slower                                                        |
| hexiom                 | 5.96 ms                                                                | 5.99 ms: 1.00x slower                                                        |
| pickle_pure_python     | 283 us                                                                 | 284 us: 1.01x slower                                                         |
| python_startup_no_site | 6.45 ms                                                                | 6.49 ms: 1.01x slower                                                        |
| json_loads             | 23.7 us                                                                | 23.9 us: 1.01x slower                                                        |
| regex_effbot           | 3.57 ms                                                                | 3.60 ms: 1.01x slower                                                        |
| asyncio_tcp            | 495 ms                                                                 | 498 ms: 1.01x slower                                                         |
| coverage               | 96.3 ms                                                                | 97.1 ms: 1.01x slower                                                        |
| unpack_sequence        | 41.3 ns                                                                | 41.7 ns: 1.01x slower                                                        |
| float                  | 72.1 ms                                                                | 72.8 ms: 1.01x slower                                                        |
| async_tree_io          | 1.31 sec                                                               | 1.33 sec: 1.01x slower                                                       |
| sqlite_synth           | 2.58 us                                                                | 2.61 us: 1.01x slower                                                        |
| unpickle               | 13.0 us                                                                | 13.1 us: 1.01x slower                                                        |
| json_dumps             | 9.30 ms                                                                | 9.42 ms: 1.01x slower                                                        |
| chaos                  | 63.9 ms                                                                | 64.7 ms: 1.01x slower                                                        |
| logging_silent         | 90.8 ns                                                                | 92.1 ns: 1.01x slower                                                        |
| pickle                 | 10.1 us                                                                | 10.3 us: 1.01x slower                                                        |
| django_template        | 32.7 ms                                                                | 33.2 ms: 1.02x slower                                                        |
| dask                   | 496 ms                                                                 | 504 ms: 1.02x slower                                                         |
| pathlib                | 17.6 ms                                                                | 17.9 ms: 1.02x slower                                                        |
| pickle_list            | 4.00 us                                                                | 4.08 us: 1.02x slower                                                        |
| genshi_text            | 20.8 ms                                                                | 21.2 ms: 1.02x slower                                                        |
| richards               | 42.3 ms                                                                | 43.1 ms: 1.02x slower                                                        |
| telco                  | 6.28 ms                                                                | 6.41 ms: 1.02x slower                                                        |
| generators             | 75.2 ms                                                                | 76.8 ms: 1.02x slower                                                        |
| crypto_pyaes           | 71.4 ms                                                                | 73.0 ms: 1.02x slower                                                        |
| create_gc_cycles       | 1.44 ms                                                                | 1.48 ms: 1.03x slower                                                        |
| nqueens                | 76.2 ms                                                                | 78.6 ms: 1.03x slower                                                        |
| spectral_norm          | 96.2 ms                                                                | 99.2 ms: 1.03x slower                                                        |
| pickle_dict            | 30.0 us                                                                | 31.0 us: 1.03x slower                                                        |
| pidigits               | 189 ms                                                                 | 198 ms: 1.04x slower                                                         |
| fannkuch               | 355 ms                                                                 | 382 ms: 1.07x slower                                                         |
| go                     | 138 ms                                                                 | 178 ms: 1.28x slower                                                         |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                 |

Benchmark hidden because not significant (23): html5lib, djangocms, meteor_contest, xml_etree_process, thrift, chameleon, async_generators, sqlglot_parse, deltablue, sympy_str, raytrace, deepcopy_memo, mypy, bench_mp_pool, sqlglot_transpile, dulwich_log, scimark_sparse_mat_mult, tornado_http, scimark_sor, xml_etree_parse, async_tree_none, deepcopy_reduce, async_tree_cpu_io_mixed
