
# Results vs. base

- fork: ericsnowcurrently
- ref: isolate_interned_dic
- machine: linux-x86_64
- commit hash: 969caba
- commit date: 2023-02-28
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230228-linux-x86_64-python-880437d4ec65ef35d505-3.12.0a5+-880437d | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 252 ms                                                                 | 252 ms: 1.00x slower                                                              |
| chameleon      | 6.35 ms                                                                | 6.44 ms: 1.01x slower                                                             |
| docutils       | 2.56 sec                                                               | 2.55 sec: 1.00x faster                                                            |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                      |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230228-linux-x86_64-python-880437d4ec65ef35d505-3.12.0a5+-880437d | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 94.6 ms                                                                | 92.4 ms: 1.02x faster                                                             |
| float          | 74.2 ms                                                                | 73.4 ms: 1.01x faster                                                             |
| pidigits       | 189 ms                                                                 | 198 ms: 1.04x slower                                                              |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230228-linux-x86_64-python-880437d4ec65ef35d505-3.12.0a5+-880437d | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 3.70 ms                                                                | 3.67 ms: 1.01x faster                                                             |
| regex_compile  | 135 ms                                                                 | 134 ms: 1.01x faster                                                              |
| regex_v8       | 21.8 ms                                                                | 21.7 ms: 1.00x faster                                                             |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                                      |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20230228-linux-x86_64-python-880437d4ec65ef35d505-3.12.0a5+-880437d | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|---------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pickle_list         | 4.26 us                                                                | 4.17 us: 1.02x faster                                                             |
| pickle_dict         | 32.1 us                                                                | 31.6 us: 1.02x faster                                                             |
| json_dumps          | 9.62 ms                                                                | 9.47 ms: 1.02x faster                                                             |
| xml_etree_iterparse | 99.7 ms                                                                | 99.0 ms: 1.01x faster                                                             |
| pickle              | 10.4 us                                                                | 10.4 us: 1.01x slower                                                             |
| unpickle_list       | 4.96 us                                                                | 5.01 us: 1.01x slower                                                             |
| unpickle            | 13.2 us                                                                | 13.5 us: 1.02x slower                                                             |
| json_loads          | 23.9 us                                                                | 24.4 us: 1.02x slower                                                             |
| pickle_pure_python  | 287 us                                                                 | 293 us: 1.02x slower                                                              |
| Geometric mean      | (ref)                                                                  | 1.00x slower                                                                      |

Benchmark hidden because not significant (4): xml_etree_generate, xml_etree_parse, unpickle_pure_python, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230228-linux-x86_64-python-880437d4ec65ef35d505-3.12.0a5+-880437d | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 9.02 ms                                                                | 9.00 ms: 1.00x faster                                                             |
| python_startup_no_site | 6.53 ms                                                                | 6.53 ms: 1.00x slower                                                             |
| Geometric mean         | (ref)                                                                  | 1.00x faster                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230228-linux-x86_64-python-880437d4ec65ef35d505-3.12.0a5+-880437d | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mako            | 9.89 ms                                                                | 9.93 ms: 1.00x slower                                                             |
| genshi_text     | 21.5 ms                                                                | 21.7 ms: 1.01x slower                                                             |
| genshi_xml      | 48.2 ms                                                                | 48.7 ms: 1.01x slower                                                             |
| django_template | 33.3 ms                                                                | 33.9 ms: 1.02x slower                                                             |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20230228-linux-x86_64-python-880437d4ec65ef35d505-3.12.0a5+-880437d | bm-20230228-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a5+-969caba |
|-------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| mdp                     | 2.63 sec                                                               | 2.47 sec: 1.06x faster                                                            |
| logging_silent          | 98.0 ns                                                                | 93.8 ns: 1.05x faster                                                             |
| nbody                   | 94.6 ms                                                                | 92.4 ms: 1.02x faster                                                             |
| telco                   | 6.49 ms                                                                | 6.34 ms: 1.02x faster                                                             |
| pickle_list             | 4.26 us                                                                | 4.17 us: 1.02x faster                                                             |
| pickle_dict             | 32.1 us                                                                | 31.6 us: 1.02x faster                                                             |
| sqlalchemy_declarative  | 140 ms                                                                 | 138 ms: 1.02x faster                                                              |
| scimark_fft             | 315 ms                                                                 | 310 ms: 1.02x faster                                                              |
| json_dumps              | 9.62 ms                                                                | 9.47 ms: 1.02x faster                                                             |
| scimark_monte_carlo     | 67.5 ms                                                                | 66.7 ms: 1.01x faster                                                             |
| pycparser               | 1.12 sec                                                               | 1.11 sec: 1.01x faster                                                            |
| float                   | 74.2 ms                                                                | 73.4 ms: 1.01x faster                                                             |
| go                      | 140 ms                                                                 | 138 ms: 1.01x faster                                                              |
| xml_etree_iterparse     | 99.7 ms                                                                | 99.0 ms: 1.01x faster                                                             |
| nqueens                 | 81.7 ms                                                                | 81.1 ms: 1.01x faster                                                             |
| regex_effbot            | 3.70 ms                                                                | 3.67 ms: 1.01x faster                                                             |
| regex_compile           | 135 ms                                                                 | 134 ms: 1.01x faster                                                              |
| deltablue               | 3.26 ms                                                                | 3.25 ms: 1.01x faster                                                             |
| asyncio_tcp             | 501 ms                                                                 | 499 ms: 1.01x faster                                                              |
| crypto_pyaes            | 74.3 ms                                                                | 73.9 ms: 1.00x faster                                                             |
| docutils                | 2.56 sec                                                               | 2.55 sec: 1.00x faster                                                            |
| regex_v8                | 21.8 ms                                                                | 21.7 ms: 1.00x faster                                                             |
| python_startup          | 9.02 ms                                                                | 9.00 ms: 1.00x faster                                                             |
| python_startup_no_site  | 6.53 ms                                                                | 6.53 ms: 1.00x slower                                                             |
| create_gc_cycles        | 1.47 ms                                                                | 1.48 ms: 1.00x slower                                                             |
| 2to3                    | 252 ms                                                                 | 252 ms: 1.00x slower                                                              |
| sympy_str               | 288 ms                                                                 | 289 ms: 1.00x slower                                                              |
| mako                    | 9.89 ms                                                                | 9.93 ms: 1.00x slower                                                             |
| sqlglot_optimize        | 51.0 ms                                                                | 51.3 ms: 1.01x slower                                                             |
| logging_simple          | 5.86 us                                                                | 5.89 us: 1.01x slower                                                             |
| bench_thread_pool       | 793 us                                                                 | 798 us: 1.01x slower                                                              |
| sqlglot_parse           | 1.44 ms                                                                | 1.45 ms: 1.01x slower                                                             |
| sympy_integrate         | 20.6 ms                                                                | 20.7 ms: 1.01x slower                                                             |
| hexiom                  | 6.21 ms                                                                | 6.25 ms: 1.01x slower                                                             |
| pickle                  | 10.4 us                                                                | 10.4 us: 1.01x slower                                                             |
| sqlglot_transpile       | 1.74 ms                                                                | 1.75 ms: 1.01x slower                                                             |
| sympy_expand            | 465 ms                                                                 | 469 ms: 1.01x slower                                                              |
| coverage                | 95.8 ms                                                                | 96.7 ms: 1.01x slower                                                             |
| unpickle_list           | 4.96 us                                                                | 5.01 us: 1.01x slower                                                             |
| genshi_text             | 21.5 ms                                                                | 21.7 ms: 1.01x slower                                                             |
| async_tree_io           | 1.29 sec                                                               | 1.30 sec: 1.01x slower                                                            |
| coroutines              | 23.1 ms                                                                | 23.3 ms: 1.01x slower                                                             |
| genshi_xml              | 48.2 ms                                                                | 48.7 ms: 1.01x slower                                                             |
| sqlglot_normalize       | 103 ms                                                                 | 105 ms: 1.01x slower                                                              |
| pprint_safe_repr        | 677 ms                                                                 | 686 ms: 1.01x slower                                                              |
| raytrace                | 289 ms                                                                 | 293 ms: 1.01x slower                                                              |
| deepcopy_reduce         | 2.98 us                                                                | 3.02 us: 1.01x slower                                                             |
| chameleon               | 6.35 ms                                                                | 6.44 ms: 1.01x slower                                                             |
| pprint_pformat          | 1.39 sec                                                               | 1.41 sec: 1.02x slower                                                            |
| richards                | 43.6 ms                                                                | 44.3 ms: 1.02x slower                                                             |
| unpickle                | 13.2 us                                                                | 13.5 us: 1.02x slower                                                             |
| pyflate                 | 406 ms                                                                 | 413 ms: 1.02x slower                                                              |
| json                    | 4.60 ms                                                                | 4.68 ms: 1.02x slower                                                             |
| django_template         | 33.3 ms                                                                | 33.9 ms: 1.02x slower                                                             |
| deepcopy                | 333 us                                                                 | 339 us: 1.02x slower                                                              |
| json_loads              | 23.9 us                                                                | 24.4 us: 1.02x slower                                                             |
| pickle_pure_python      | 287 us                                                                 | 293 us: 1.02x slower                                                              |
| spectral_norm           | 93.7 ms                                                                | 95.8 ms: 1.02x slower                                                             |
| fannkuch                | 357 ms                                                                 | 365 ms: 1.02x slower                                                              |
| scimark_sparse_mat_mult | 4.43 ms                                                                | 4.56 ms: 1.03x slower                                                             |
| pidigits                | 189 ms                                                                 | 198 ms: 1.04x slower                                                              |
| gc_traversal            | 3.83 ms                                                                | 4.31 ms: 1.13x slower                                                             |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                                      |

Benchmark hidden because not significant (32): scimark_lu, thrift, html5lib, sqlite_synth, xml_etree_generate, deepcopy_memo, xml_etree_parse, chaos, regex_dna, aiohttp, async_generators, scimark_sor, logging_format, dask, tornado_http, pathlib, dulwich_log, unpickle_pure_python, bench_mp_pool, generators, mypy2, comprehensions, sympy_sum, xml_etree_process, gunicorn, djangocms, async_tree_none, unpack_sequence, sqlalchemy_imperative, meteor_contest, async_tree_memoization, async_tree_cpu_io_mixed
