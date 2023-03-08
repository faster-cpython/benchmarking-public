
# Results vs. base

- fork: ericsnowcurrently
- ref: isolate_dict_global_
- machine: linux-x86_64
- commit hash: f707a1b
- commit date: 2023-02-28
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230228-linux-x86_64-python-f300a1fa4c121f7807cb-3.12.0a5+-f300a1f | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_global_-3.12.0a5+-f707a1b |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| chameleon      | 6.38 ms                                                                | 6.28 ms: 1.02x faster                                                             |
| docutils       | 2.56 sec                                                               | 2.57 sec: 1.00x slower                                                            |
| tornado_http   | 94.9 ms                                                                | 95.5 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                      |

Benchmark hidden because not significant (2): 2to3, html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230228-linux-x86_64-python-f300a1fa4c121f7807cb-3.12.0a5+-f300a1f | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_global_-3.12.0a5+-f707a1b |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 189 ms                                                                 | 189 ms: 1.00x slower                                                              |
| float          | 73.9 ms                                                                | 74.3 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                      |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230228-linux-x86_64-python-f300a1fa4c121f7807cb-3.12.0a5+-f300a1f | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_global_-3.12.0a5+-f707a1b |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_dna      | 218 ms                                                                 | 210 ms: 1.04x faster                                                              |
| regex_compile  | 135 ms                                                                 | 133 ms: 1.01x faster                                                              |
| regex_v8       | 21.6 ms                                                                | 21.9 ms: 1.01x slower                                                             |
| regex_effbot   | 3.53 ms                                                                | 3.63 ms: 1.03x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                      |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230228-linux-x86_64-python-f300a1fa4c121f7807cb-3.12.0a5+-f300a1f | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_global_-3.12.0a5+-f707a1b |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_pure_python   | 290 us                                                                 | 282 us: 1.03x faster                                                              |
| xml_etree_process    | 56.3 ms                                                                | 55.6 ms: 1.01x faster                                                             |
| unpickle_pure_python | 202 us                                                                 | 199 us: 1.01x faster                                                              |
| xml_etree_generate   | 81.5 ms                                                                | 80.8 ms: 1.01x faster                                                             |
| pickle_dict          | 30.7 us                                                                | 30.8 us: 1.00x slower                                                             |
| json_dumps           | 9.51 ms                                                                | 9.55 ms: 1.00x slower                                                             |
| json_loads           | 23.9 us                                                                | 24.3 us: 1.02x slower                                                             |
| pickle_list          | 4.02 us                                                                | 4.09 us: 1.02x slower                                                             |
| pickle               | 9.90 us                                                                | 10.2 us: 1.03x slower                                                             |
| xml_etree_iterparse  | 100 ms                                                                 | 104 ms: 1.04x slower                                                              |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                                      |

Benchmark hidden because not significant (3): unpickle_list, xml_etree_parse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230228-linux-x86_64-python-f300a1fa4c121f7807cb-3.12.0a5+-f300a1f | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_global_-3.12.0a5+-f707a1b |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 8.98 ms                                                                | 9.06 ms: 1.01x slower                                                             |
| python_startup_no_site | 6.51 ms                                                                | 6.57 ms: 1.01x slower                                                             |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230228-linux-x86_64-python-f300a1fa4c121f7807cb-3.12.0a5+-f300a1f | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_global_-3.12.0a5+-f707a1b |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_text     | 21.8 ms                                                                | 21.4 ms: 1.02x faster                                                             |
| django_template | 33.4 ms                                                                | 33.0 ms: 1.01x faster                                                             |
| mako            | 9.92 ms                                                                | 9.81 ms: 1.01x faster                                                             |
| genshi_xml      | 49.0 ms                                                                | 48.6 ms: 1.01x faster                                                             |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                                      |

All benchmarks:
===============

| Benchmark              | bm-20230228-linux-x86_64-python-f300a1fa4c121f7807cb-3.12.0a5+-f300a1f | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_dict_global_-3.12.0a5+-f707a1b |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| gc_traversal           | 4.18 ms                                                                | 3.83 ms: 1.09x faster                                                             |
| regex_dna              | 218 ms                                                                 | 210 ms: 1.04x faster                                                              |
| pickle_pure_python     | 290 us                                                                 | 282 us: 1.03x faster                                                              |
| pycparser              | 1.15 sec                                                               | 1.12 sec: 1.03x faster                                                            |
| coverage               | 95.6 ms                                                                | 93.1 ms: 1.03x faster                                                             |
| nqueens                | 82.5 ms                                                                | 80.5 ms: 1.03x faster                                                             |
| generators             | 31.3 ms                                                                | 30.6 ms: 1.02x faster                                                             |
| genshi_text            | 21.8 ms                                                                | 21.4 ms: 1.02x faster                                                             |
| chameleon              | 6.38 ms                                                                | 6.28 ms: 1.02x faster                                                             |
| logging_simple         | 5.87 us                                                                | 5.78 us: 1.02x faster                                                             |
| deepcopy_memo          | 34.6 us                                                                | 34.1 us: 1.01x faster                                                             |
| xml_etree_process      | 56.3 ms                                                                | 55.6 ms: 1.01x faster                                                             |
| go                     | 137 ms                                                                 | 135 ms: 1.01x faster                                                              |
| django_template        | 33.4 ms                                                                | 33.0 ms: 1.01x faster                                                             |
| logging_format         | 6.35 us                                                                | 6.27 us: 1.01x faster                                                             |
| unpickle_pure_python   | 202 us                                                                 | 199 us: 1.01x faster                                                              |
| regex_compile          | 135 ms                                                                 | 133 ms: 1.01x faster                                                              |
| deepcopy_reduce        | 2.99 us                                                                | 2.95 us: 1.01x faster                                                             |
| mdp                    | 2.42 sec                                                               | 2.40 sec: 1.01x faster                                                            |
| mako                   | 9.92 ms                                                                | 9.81 ms: 1.01x faster                                                             |
| gunicorn               | 1.09 ms                                                                | 1.08 ms: 1.01x faster                                                             |
| deltablue              | 3.24 ms                                                                | 3.21 ms: 1.01x faster                                                             |
| scimark_lu             | 111 ms                                                                 | 110 ms: 1.01x faster                                                              |
| pprint_safe_repr       | 684 ms                                                                 | 679 ms: 1.01x faster                                                              |
| scimark_sor            | 107 ms                                                                 | 106 ms: 1.01x faster                                                              |
| xml_etree_generate     | 81.5 ms                                                                | 80.8 ms: 1.01x faster                                                             |
| richards               | 43.5 ms                                                                | 43.2 ms: 1.01x faster                                                             |
| genshi_xml             | 49.0 ms                                                                | 48.6 ms: 1.01x faster                                                             |
| hexiom                 | 6.20 ms                                                                | 6.16 ms: 1.01x faster                                                             |
| async_generators       | 419 ms                                                                 | 417 ms: 1.01x faster                                                              |
| raytrace               | 290 ms                                                                 | 289 ms: 1.01x faster                                                              |
| mypy2                  | 336 ms                                                                 | 334 ms: 1.00x faster                                                              |
| scimark_fft            | 313 ms                                                                 | 312 ms: 1.00x faster                                                              |
| sympy_expand           | 468 ms                                                                 | 466 ms: 1.00x faster                                                              |
| pidigits               | 189 ms                                                                 | 189 ms: 1.00x slower                                                              |
| aiohttp                | 1.01 ms                                                                | 1.01 ms: 1.00x slower                                                             |
| pickle_dict            | 30.7 us                                                                | 30.8 us: 1.00x slower                                                             |
| sympy_integrate        | 20.7 ms                                                                | 20.8 ms: 1.00x slower                                                             |
| json_dumps             | 9.51 ms                                                                | 9.55 ms: 1.00x slower                                                             |
| docutils               | 2.56 sec                                                               | 2.57 sec: 1.00x slower                                                            |
| dulwich_log            | 63.5 ms                                                                | 63.8 ms: 1.00x slower                                                             |
| bench_thread_pool      | 794 us                                                                 | 797 us: 1.00x slower                                                              |
| tornado_http           | 94.9 ms                                                                | 95.5 ms: 1.01x slower                                                             |
| asyncio_tcp            | 501 ms                                                                 | 503 ms: 1.01x slower                                                              |
| float                  | 73.9 ms                                                                | 74.3 ms: 1.01x slower                                                             |
| python_startup         | 8.98 ms                                                                | 9.06 ms: 1.01x slower                                                             |
| python_startup_no_site | 6.51 ms                                                                | 6.57 ms: 1.01x slower                                                             |
| sqlglot_optimize       | 51.2 ms                                                                | 51.6 ms: 1.01x slower                                                             |
| sqlglot_transpile      | 1.73 ms                                                                | 1.75 ms: 1.01x slower                                                             |
| comprehensions         | 24.0 us                                                                | 24.2 us: 1.01x slower                                                             |
| fannkuch               | 358 ms                                                                 | 362 ms: 1.01x slower                                                              |
| regex_v8               | 21.6 ms                                                                | 21.9 ms: 1.01x slower                                                             |
| sqlglot_normalize      | 104 ms                                                                 | 106 ms: 1.01x slower                                                              |
| create_gc_cycles       | 1.47 ms                                                                | 1.50 ms: 1.02x slower                                                             |
| json                   | 4.54 ms                                                                | 4.62 ms: 1.02x slower                                                             |
| telco                  | 6.29 ms                                                                | 6.40 ms: 1.02x slower                                                             |
| json_loads             | 23.9 us                                                                | 24.3 us: 1.02x slower                                                             |
| pickle_list            | 4.02 us                                                                | 4.09 us: 1.02x slower                                                             |
| sqlglot_parse          | 1.43 ms                                                                | 1.46 ms: 1.02x slower                                                             |
| chaos                  | 67.2 ms                                                                | 68.5 ms: 1.02x slower                                                             |
| pyflate                | 408 ms                                                                 | 417 ms: 1.02x slower                                                              |
| regex_effbot           | 3.53 ms                                                                | 3.63 ms: 1.03x slower                                                             |
| pickle                 | 9.90 us                                                                | 10.2 us: 1.03x slower                                                             |
| unpack_sequence        | 42.7 ns                                                                | 44.3 ns: 1.04x slower                                                             |
| thrift                 | 762 us                                                                 | 793 us: 1.04x slower                                                              |
| xml_etree_iterparse    | 100 ms                                                                 | 104 ms: 1.04x slower                                                              |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                      |

Benchmark hidden because not significant (28): sqlalchemy_imperative, html5lib, unpickle_list, scimark_monte_carlo, sqlite_synth, logging_silent, spectral_norm, scimark_sparse_mat_mult, async_tree_none, deepcopy, bench_mp_pool, async_tree_cpu_io_mixed, pathlib, sympy_sum, sqlalchemy_declarative, 2to3, pprint_pformat, nbody, sympy_str, coroutines, async_tree_io, crypto_pyaes, meteor_contest, dask, xml_etree_parse, unpickle, async_tree_memoization, djangocms
