
# Results vs. base

- fork: ericsnowcurrently
- ref: isolate_func_state_n
- machine: linux-x86_64
- commit hash: 27d7df6
- commit date: 2023-02-28
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230228-linux-x86_64-python-f300a1fa4c121f7807cb-3.12.0a5+-f300a1f | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_func_state_n-3.12.0a5+-27d7df6 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| chameleon      | 6.38 ms                                                                | 6.34 ms: 1.01x faster                                                             |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                      |

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

Benchmark hidden because not significant (3): pidigits, float, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230228-linux-x86_64-python-f300a1fa4c121f7807cb-3.12.0a5+-f300a1f | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_func_state_n-3.12.0a5+-27d7df6 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_dna      | 218 ms                                                                 | 199 ms: 1.10x faster                                                              |
| regex_v8       | 21.6 ms                                                                | 21.8 ms: 1.01x slower                                                             |
| regex_compile  | 135 ms                                                                 | 136 ms: 1.01x slower                                                              |
| regex_effbot   | 3.53 ms                                                                | 3.57 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.02x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20230228-linux-x86_64-python-f300a1fa4c121f7807cb-3.12.0a5+-f300a1f | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_func_state_n-3.12.0a5+-27d7df6 |
|---------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_dict         | 30.7 us                                                                | 30.6 us: 1.00x faster                                                             |
| json_loads          | 23.9 us                                                                | 24.0 us: 1.00x slower                                                             |
| json_dumps          | 9.51 ms                                                                | 9.58 ms: 1.01x slower                                                             |
| pickle_pure_python  | 290 us                                                                 | 293 us: 1.01x slower                                                              |
| xml_etree_parse     | 149 ms                                                                 | 150 ms: 1.01x slower                                                              |
| pickle_list         | 4.02 us                                                                | 4.07 us: 1.01x slower                                                             |
| pickle              | 9.90 us                                                                | 10.2 us: 1.03x slower                                                             |
| xml_etree_iterparse | 100 ms                                                                 | 104 ms: 1.04x slower                                                              |
| Geometric mean      | (ref)                                                                  | 1.01x slower                                                                      |

Benchmark hidden because not significant (5): unpickle_list, xml_etree_process, xml_etree_generate, unpickle_pure_python, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230228-linux-x86_64-python-f300a1fa4c121f7807cb-3.12.0a5+-f300a1f | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_func_state_n-3.12.0a5+-27d7df6 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 8.98 ms                                                                | 9.04 ms: 1.01x slower                                                             |
| python_startup_no_site | 6.51 ms                                                                | 6.56 ms: 1.01x slower                                                             |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230228-linux-x86_64-python-f300a1fa4c121f7807cb-3.12.0a5+-f300a1f | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_func_state_n-3.12.0a5+-27d7df6 |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 9.92 ms                                                                | 9.88 ms: 1.00x faster                                                             |
| django_template | 33.4 ms                                                                | 33.6 ms: 1.01x slower                                                             |
| Geometric mean  | (ref)                                                                  | 1.00x slower                                                                      |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark              | bm-20230228-linux-x86_64-python-f300a1fa4c121f7807cb-3.12.0a5+-f300a1f | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_func_state_n-3.12.0a5+-27d7df6 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_dna              | 218 ms                                                                 | 199 ms: 1.10x faster                                                              |
| gc_traversal           | 4.18 ms                                                                | 3.84 ms: 1.09x faster                                                             |
| pycparser              | 1.15 sec                                                               | 1.10 sec: 1.04x faster                                                            |
| unpack_sequence        | 42.7 ns                                                                | 41.2 ns: 1.03x faster                                                             |
| nqueens                | 82.5 ms                                                                | 80.8 ms: 1.02x faster                                                             |
| generators             | 31.3 ms                                                                | 30.8 ms: 1.02x faster                                                             |
| spectral_norm          | 94.3 ms                                                                | 93.0 ms: 1.01x faster                                                             |
| logging_silent         | 95.0 ns                                                                | 94.0 ns: 1.01x faster                                                             |
| hexiom                 | 6.20 ms                                                                | 6.14 ms: 1.01x faster                                                             |
| sqlite_synth           | 2.64 us                                                                | 2.62 us: 1.01x faster                                                             |
| gunicorn               | 1.09 ms                                                                | 1.08 ms: 1.01x faster                                                             |
| pyflate                | 408 ms                                                                 | 405 ms: 1.01x faster                                                              |
| chameleon              | 6.38 ms                                                                | 6.34 ms: 1.01x faster                                                             |
| scimark_fft            | 313 ms                                                                 | 311 ms: 1.01x faster                                                              |
| sympy_str              | 288 ms                                                                 | 287 ms: 1.01x faster                                                              |
| sympy_expand           | 468 ms                                                                 | 466 ms: 1.01x faster                                                              |
| sympy_integrate        | 20.7 ms                                                                | 20.6 ms: 1.00x faster                                                             |
| comprehensions         | 24.0 us                                                                | 23.9 us: 1.00x faster                                                             |
| mako                   | 9.92 ms                                                                | 9.88 ms: 1.00x faster                                                             |
| pickle_dict            | 30.7 us                                                                | 30.6 us: 1.00x faster                                                             |
| sqlglot_optimize       | 51.2 ms                                                                | 51.3 ms: 1.00x slower                                                             |
| raytrace               | 290 ms                                                                 | 291 ms: 1.00x slower                                                              |
| json_loads             | 23.9 us                                                                | 24.0 us: 1.00x slower                                                             |
| bench_thread_pool      | 794 us                                                                 | 797 us: 1.00x slower                                                              |
| django_template        | 33.4 ms                                                                | 33.6 ms: 1.01x slower                                                             |
| python_startup         | 8.98 ms                                                                | 9.04 ms: 1.01x slower                                                             |
| sqlglot_transpile      | 1.73 ms                                                                | 1.74 ms: 1.01x slower                                                             |
| json_dumps             | 9.51 ms                                                                | 9.58 ms: 1.01x slower                                                             |
| chaos                  | 67.2 ms                                                                | 67.7 ms: 1.01x slower                                                             |
| python_startup_no_site | 6.51 ms                                                                | 6.56 ms: 1.01x slower                                                             |
| regex_v8               | 21.6 ms                                                                | 21.8 ms: 1.01x slower                                                             |
| richards               | 43.5 ms                                                                | 43.9 ms: 1.01x slower                                                             |
| regex_compile          | 135 ms                                                                 | 136 ms: 1.01x slower                                                              |
| go                     | 137 ms                                                                 | 138 ms: 1.01x slower                                                              |
| pickle_pure_python     | 290 us                                                                 | 293 us: 1.01x slower                                                              |
| sqlglot_parse          | 1.43 ms                                                                | 1.44 ms: 1.01x slower                                                             |
| logging_simple         | 5.87 us                                                                | 5.93 us: 1.01x slower                                                             |
| regex_effbot           | 3.53 ms                                                                | 3.57 ms: 1.01x slower                                                             |
| xml_etree_parse        | 149 ms                                                                 | 150 ms: 1.01x slower                                                              |
| crypto_pyaes           | 73.3 ms                                                                | 74.2 ms: 1.01x slower                                                             |
| sqlalchemy_declarative | 139 ms                                                                 | 141 ms: 1.01x slower                                                              |
| thrift                 | 762 us                                                                 | 772 us: 1.01x slower                                                              |
| pickle_list            | 4.02 us                                                                | 4.07 us: 1.01x slower                                                             |
| deepcopy_reduce        | 2.99 us                                                                | 3.03 us: 1.01x slower                                                             |
| mdp                    | 2.42 sec                                                               | 2.46 sec: 1.01x slower                                                            |
| pprint_safe_repr       | 684 ms                                                                 | 694 ms: 1.01x slower                                                              |
| logging_format         | 6.35 us                                                                | 6.45 us: 1.02x slower                                                             |
| deepcopy_memo          | 34.6 us                                                                | 35.4 us: 1.02x slower                                                             |
| create_gc_cycles       | 1.47 ms                                                                | 1.51 ms: 1.02x slower                                                             |
| pprint_pformat         | 1.40 sec                                                               | 1.43 sec: 1.02x slower                                                            |
| fannkuch               | 358 ms                                                                 | 367 ms: 1.03x slower                                                              |
| pickle                 | 9.90 us                                                                | 10.2 us: 1.03x slower                                                             |
| telco                  | 6.29 ms                                                                | 6.45 ms: 1.03x slower                                                             |
| json                   | 4.54 ms                                                                | 4.66 ms: 1.03x slower                                                             |
| deepcopy               | 331 us                                                                 | 340 us: 1.03x slower                                                              |
| coverage               | 95.6 ms                                                                | 98.3 ms: 1.03x slower                                                             |
| xml_etree_iterparse    | 100 ms                                                                 | 104 ms: 1.04x slower                                                              |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                      |

Benchmark hidden because not significant (37): djangocms, sqlalchemy_imperative, scimark_monte_carlo, async_tree_none, coroutines, docutils, mypy2, deltablue, dulwich_log, sympy_sum, bench_mp_pool, genshi_text, asyncio_tcp, dask, genshi_xml, unpickle_list, scimark_sparse_mat_mult, sqlglot_normalize, aiohttp, pidigits, pathlib, meteor_contest, 2to3, xml_etree_process, float, xml_etree_generate, tornado_http, unpickle_pure_python, nbody, async_generators, scimark_sor, html5lib, async_tree_io, async_tree_cpu_io_mixed, scimark_lu, unpickle, async_tree_memoization
