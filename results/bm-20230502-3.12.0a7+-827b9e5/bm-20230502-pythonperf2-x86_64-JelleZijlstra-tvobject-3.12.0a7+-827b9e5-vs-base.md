
# Results vs. base

- fork: JelleZijlstra
- ref: tvobject
- machine: linux-x86_64
- commit hash: 827b9e5
- commit date: 2023-05-02
- overall geometric mean: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230502-pythonperf2-x86_64-python-872cbc613245db7a1fc5-3.12.0a7+-872cbc6 | bm-20230502-pythonperf2-x86_64-JelleZijlstra-tvobject-3.12.0a7+-827b9e5 |
|----------------|:----------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| 2to3           | 285 ms                                                                       | 284 ms: 1.00x faster                                                    |
| html5lib       | 70.2 ms                                                                      | 69.2 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                            |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230502-pythonperf2-x86_64-python-872cbc613245db7a1fc5-3.12.0a7+-872cbc6 | bm-20230502-pythonperf2-x86_64-JelleZijlstra-tvobject-3.12.0a7+-827b9e5 |
|----------------|:----------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| float          | 79.4 ms                                                                      | 78.0 ms: 1.02x faster                                                   |
| pidigits       | 260 ms                                                                       | 260 ms: 1.00x faster                                                    |
| nbody          | 86.2 ms                                                                      | 87.7 ms: 1.02x slower                                                   |
| Geometric mean | (ref)                                                                        | 1.00x faster                                                            |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230502-pythonperf2-x86_64-python-872cbc613245db7a1fc5-3.12.0a7+-872cbc6 | bm-20230502-pythonperf2-x86_64-JelleZijlstra-tvobject-3.12.0a7+-827b9e5 |
|----------------|:----------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| regex_v8       | 23.9 ms                                                                      | 23.4 ms: 1.02x faster                                                   |
| regex_compile  | 144 ms                                                                       | 144 ms: 1.00x faster                                                    |
| regex_effbot   | 3.46 ms                                                                      | 3.50 ms: 1.01x slower                                                   |
| regex_dna      | 227 ms                                                                       | 234 ms: 1.03x slower                                                    |
| Geometric mean | (ref)                                                                        | 1.00x slower                                                            |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230502-pythonperf2-x86_64-python-872cbc613245db7a1fc5-3.12.0a7+-872cbc6 | bm-20230502-pythonperf2-x86_64-JelleZijlstra-tvobject-3.12.0a7+-827b9e5 |
|----------------------|:----------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpickle             | 15.0 us                                                                      | 14.3 us: 1.05x faster                                                   |
| pickle               | 10.3 us                                                                      | 10.0 us: 1.03x faster                                                   |
| xml_etree_parse      | 148 ms                                                                       | 145 ms: 1.02x faster                                                    |
| unpickle_pure_python | 208 us                                                                       | 204 us: 1.02x faster                                                    |
| unpickle_list        | 4.87 us                                                                      | 4.83 us: 1.01x faster                                                   |
| xml_etree_generate   | 86.3 ms                                                                      | 86.0 ms: 1.00x faster                                                   |
| json_dumps           | 10.4 ms                                                                      | 10.5 ms: 1.00x slower                                                   |
| pickle_dict          | 31.5 us                                                                      | 31.9 us: 1.01x slower                                                   |
| Geometric mean       | (ref)                                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (5): pickle_pure_python, pickle_list, xml_etree_iterparse, xml_etree_process, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230502-pythonperf2-x86_64-python-872cbc613245db7a1fc5-3.12.0a7+-872cbc6 | bm-20230502-pythonperf2-x86_64-JelleZijlstra-tvobject-3.12.0a7+-827b9e5 |
|------------------------|:----------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| python_startup         | 11.2 ms                                                                      | 11.3 ms: 1.01x slower                                                   |
| python_startup_no_site | 8.37 ms                                                                      | 8.47 ms: 1.01x slower                                                   |
| Geometric mean         | (ref)                                                                        | 1.01x slower                                                            |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20230502-pythonperf2-x86_64-python-872cbc613245db7a1fc5-3.12.0a7+-872cbc6 | bm-20230502-pythonperf2-x86_64-JelleZijlstra-tvobject-3.12.0a7+-827b9e5 |
|----------------|:----------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| genshi_xml     | 54.3 ms                                                                      | 53.5 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (2): mako, genshi_text

All benchmarks:
===============

| Benchmark              | bm-20230502-pythonperf2-x86_64-python-872cbc613245db7a1fc5-3.12.0a7+-872cbc6 | bm-20230502-pythonperf2-x86_64-JelleZijlstra-tvobject-3.12.0a7+-827b9e5 |
|------------------------|:----------------------------------------------------------------------------:|:-----------------------------------------------------------------------:|
| unpack_sequence        | 52.3 ns                                                                      | 47.6 ns: 1.10x faster                                                   |
| unpickle               | 15.0 us                                                                      | 14.3 us: 1.05x faster                                                   |
| logging_silent         | 99.5 ns                                                                      | 94.7 ns: 1.05x faster                                                   |
| scimark_fft            | 304 ms                                                                       | 291 ms: 1.05x faster                                                    |
| pycparser              | 1.27 sec                                                                     | 1.22 sec: 1.04x faster                                                  |
| comprehensions         | 25.2 us                                                                      | 24.3 us: 1.04x faster                                                   |
| deepcopy_memo          | 38.4 us                                                                      | 37.0 us: 1.04x faster                                                   |
| scimark_sor            | 113 ms                                                                       | 110 ms: 1.03x faster                                                    |
| pickle                 | 10.3 us                                                                      | 10.0 us: 1.03x faster                                                   |
| dulwich_log            | 65.6 ms                                                                      | 63.5 ms: 1.03x faster                                                   |
| logging_simple         | 6.71 us                                                                      | 6.53 us: 1.03x faster                                                   |
| spectral_norm          | 91.3 ms                                                                      | 88.9 ms: 1.03x faster                                                   |
| scimark_lu             | 98.7 ms                                                                      | 96.2 ms: 1.03x faster                                                   |
| thrift                 | 917 us                                                                       | 896 us: 1.02x faster                                                    |
| regex_v8               | 23.9 ms                                                                      | 23.4 ms: 1.02x faster                                                   |
| coroutines             | 22.9 ms                                                                      | 22.5 ms: 1.02x faster                                                   |
| raytrace               | 306 ms                                                                       | 300 ms: 1.02x faster                                                    |
| xml_etree_parse        | 148 ms                                                                       | 145 ms: 1.02x faster                                                    |
| sqlglot_normalize      | 121 ms                                                                       | 119 ms: 1.02x faster                                                    |
| float                  | 79.4 ms                                                                      | 78.0 ms: 1.02x faster                                                   |
| unpickle_pure_python   | 208 us                                                                       | 204 us: 1.02x faster                                                    |
| crypto_pyaes           | 81.5 ms                                                                      | 80.3 ms: 1.01x faster                                                   |
| meteor_contest         | 139 ms                                                                       | 137 ms: 1.01x faster                                                    |
| genshi_xml             | 54.3 ms                                                                      | 53.5 ms: 1.01x faster                                                   |
| html5lib               | 70.2 ms                                                                      | 69.2 ms: 1.01x faster                                                   |
| deepcopy_reduce        | 3.49 us                                                                      | 3.44 us: 1.01x faster                                                   |
| chaos                  | 67.1 ms                                                                      | 66.2 ms: 1.01x faster                                                   |
| richards               | 43.2 ms                                                                      | 42.7 ms: 1.01x faster                                                   |
| sqlglot_parse          | 1.40 ms                                                                      | 1.38 ms: 1.01x faster                                                   |
| go                     | 148 ms                                                                       | 147 ms: 1.01x faster                                                    |
| sqlglot_transpile      | 1.81 ms                                                                      | 1.79 ms: 1.01x faster                                                   |
| hexiom                 | 5.98 ms                                                                      | 5.91 ms: 1.01x faster                                                   |
| pprint_pformat         | 1.66 sec                                                                     | 1.64 sec: 1.01x faster                                                  |
| json                   | 5.17 ms                                                                      | 5.12 ms: 1.01x faster                                                   |
| pyflate                | 444 ms                                                                       | 439 ms: 1.01x faster                                                    |
| unpickle_list          | 4.87 us                                                                      | 4.83 us: 1.01x faster                                                   |
| generators             | 36.2 ms                                                                      | 35.9 ms: 1.01x faster                                                   |
| sqlglot_optimize       | 59.1 ms                                                                      | 58.7 ms: 1.01x faster                                                   |
| nqueens                | 89.5 ms                                                                      | 88.9 ms: 1.01x faster                                                   |
| regex_compile          | 144 ms                                                                       | 144 ms: 1.00x faster                                                    |
| xml_etree_generate     | 86.3 ms                                                                      | 86.0 ms: 1.00x faster                                                   |
| mdp                    | 2.55 sec                                                                     | 2.54 sec: 1.00x faster                                                  |
| pidigits               | 260 ms                                                                       | 260 ms: 1.00x faster                                                    |
| 2to3                   | 285 ms                                                                       | 284 ms: 1.00x faster                                                    |
| json_dumps             | 10.4 ms                                                                      | 10.5 ms: 1.00x slower                                                   |
| python_startup         | 11.2 ms                                                                      | 11.3 ms: 1.01x slower                                                   |
| regex_effbot           | 3.46 ms                                                                      | 3.50 ms: 1.01x slower                                                   |
| asyncio_tcp            | 377 ms                                                                       | 381 ms: 1.01x slower                                                    |
| deltablue              | 3.22 ms                                                                      | 3.25 ms: 1.01x slower                                                   |
| deepcopy               | 382 us                                                                       | 386 us: 1.01x slower                                                    |
| python_startup_no_site | 8.37 ms                                                                      | 8.47 ms: 1.01x slower                                                   |
| pickle_dict            | 31.5 us                                                                      | 31.9 us: 1.01x slower                                                   |
| pathlib                | 19.3 ms                                                                      | 19.7 ms: 1.02x slower                                                   |
| nbody                  | 86.2 ms                                                                      | 87.7 ms: 1.02x slower                                                   |
| regex_dna              | 227 ms                                                                       | 234 ms: 1.03x slower                                                    |
| create_gc_cycles       | 1.65 ms                                                                      | 1.71 ms: 1.03x slower                                                   |
| gc_traversal           | 3.80 ms                                                                      | 4.02 ms: 1.06x slower                                                   |
| coverage               | 89.9 ms                                                                      | 96.0 ms: 1.07x slower                                                   |
| bench_mp_pool          | 5.16 ms                                                                      | 5.54 ms: 1.07x slower                                                   |
| Geometric mean         | (ref)                                                                        | 1.01x faster                                                            |

Benchmark hidden because not significant (24): bench_thread_pool, mako, async_tree_none, pickle_pure_python, dask, async_tree_memoization, genshi_text, pickle_list, async_generators, docutils, async_tree_cpu_io_mixed, pprint_safe_repr, xml_etree_iterparse, logging_format, mypy2, xml_etree_process, fannkuch, async_tree_io, sqlite_synth, telco, scimark_monte_carlo, json_loads, tornado_http, scimark_sparse_mat_mult
