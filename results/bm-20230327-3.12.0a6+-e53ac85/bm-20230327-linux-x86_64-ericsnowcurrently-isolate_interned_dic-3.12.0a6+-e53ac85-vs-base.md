
# Results vs. base

- fork: ericsnowcurrently
- ref: isolate_interned_dic
- machine: linux-x86_64
- commit hash: e53ac85
- commit date: 2023-03-27
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230327-linux-x86_64-python-89e67ada6958cfd8d4ee-3.12.0a6+-89e67ad | bm-20230327-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a6+-e53ac85 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 253 ms: 1.00x slower                                                              |
| docutils       | 2.53 sec                                                               | 2.53 sec: 1.00x slower                                                            |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                      |

Benchmark hidden because not significant (3): chameleon, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230327-linux-x86_64-python-89e67ada6958cfd8d4ee-3.12.0a6+-89e67ad | bm-20230327-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a6+-e53ac85 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| pidigits       | 188 ms                                                                 | 188 ms: 1.00x slower                                                              |
| float          | 73.4 ms                                                                | 73.8 ms: 1.01x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                                      |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230327-linux-x86_64-python-89e67ada6958cfd8d4ee-3.12.0a6+-89e67ad | bm-20230327-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a6+-e53ac85 |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_v8       | 21.8 ms                                                                | 21.7 ms: 1.01x faster                                                             |
| regex_dna      | 203 ms                                                                 | 205 ms: 1.01x slower                                                              |
| regex_effbot   | 3.43 ms                                                                | 3.73 ms: 1.09x slower                                                             |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                                      |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230327-linux-x86_64-python-89e67ada6958cfd8d4ee-3.12.0a6+-89e67ad | bm-20230327-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a6+-e53ac85 |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| xml_etree_iterparse  | 100 ms                                                                 | 98.5 ms: 1.02x faster                                                             |
| unpickle_list        | 5.08 us                                                                | 4.99 us: 1.02x faster                                                             |
| xml_etree_process    | 56.0 ms                                                                | 55.4 ms: 1.01x faster                                                             |
| pickle_pure_python   | 288 us                                                                 | 285 us: 1.01x faster                                                              |
| xml_etree_generate   | 80.9 ms                                                                | 80.2 ms: 1.01x faster                                                             |
| xml_etree_parse      | 149 ms                                                                 | 148 ms: 1.01x faster                                                              |
| pickle_list          | 4.15 us                                                                | 4.13 us: 1.01x faster                                                             |
| pickle_dict          | 31.2 us                                                                | 31.1 us: 1.00x faster                                                             |
| json_loads           | 24.1 us                                                                | 24.3 us: 1.01x slower                                                             |
| pickle               | 10.2 us                                                                | 10.3 us: 1.01x slower                                                             |
| unpickle             | 13.3 us                                                                | 13.5 us: 1.01x slower                                                             |
| unpickle_pure_python | 200 us                                                                 | 203 us: 1.02x slower                                                              |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                                      |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230327-linux-x86_64-python-89e67ada6958cfd8d4ee-3.12.0a6+-89e67ad | bm-20230327-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a6+-e53ac85 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup_no_site | 6.50 ms                                                                | 6.54 ms: 1.01x slower                                                             |
| python_startup         | 8.80 ms                                                                | 8.85 ms: 1.01x slower                                                             |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230327-linux-x86_64-python-89e67ada6958cfd8d4ee-3.12.0a6+-89e67ad | bm-20230327-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a6+-e53ac85 |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_text     | 21.8 ms                                                                | 21.0 ms: 1.03x faster                                                             |
| genshi_xml      | 47.4 ms                                                                | 47.1 ms: 1.01x faster                                                             |
| mako            | 9.95 ms                                                                | 9.99 ms: 1.00x slower                                                             |
| django_template | 33.1 ms                                                                | 33.7 ms: 1.02x slower                                                             |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                                      |

All benchmarks:
===============

| Benchmark              | bm-20230327-linux-x86_64-python-89e67ada6958cfd8d4ee-3.12.0a6+-89e67ad | bm-20230327-linux-x86_64-ericsnowcurrently-isolate_interned_dic-3.12.0a6+-e53ac85 |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| scimark_monte_carlo    | 69.1 ms                                                                | 66.3 ms: 1.04x faster                                                             |
| gc_traversal           | 3.67 ms                                                                | 3.53 ms: 1.04x faster                                                             |
| genshi_text            | 21.8 ms                                                                | 21.0 ms: 1.03x faster                                                             |
| scimark_fft            | 313 ms                                                                 | 303 ms: 1.03x faster                                                              |
| fannkuch               | 383 ms                                                                 | 375 ms: 1.02x faster                                                              |
| xml_etree_iterparse    | 100 ms                                                                 | 98.5 ms: 1.02x faster                                                             |
| unpickle_list          | 5.08 us                                                                | 4.99 us: 1.02x faster                                                             |
| meteor_contest         | 105 ms                                                                 | 103 ms: 1.02x faster                                                              |
| scimark_lu             | 110 ms                                                                 | 109 ms: 1.01x faster                                                              |
| xml_etree_process      | 56.0 ms                                                                | 55.4 ms: 1.01x faster                                                             |
| logging_format         | 6.37 us                                                                | 6.31 us: 1.01x faster                                                             |
| pickle_pure_python     | 288 us                                                                 | 285 us: 1.01x faster                                                              |
| xml_etree_generate     | 80.9 ms                                                                | 80.2 ms: 1.01x faster                                                             |
| sqlglot_transpile      | 1.73 ms                                                                | 1.71 ms: 1.01x faster                                                             |
| genshi_xml             | 47.4 ms                                                                | 47.1 ms: 1.01x faster                                                             |
| nqueens                | 80.4 ms                                                                | 79.8 ms: 1.01x faster                                                             |
| xml_etree_parse        | 149 ms                                                                 | 148 ms: 1.01x faster                                                              |
| sqlglot_parse          | 1.43 ms                                                                | 1.42 ms: 1.01x faster                                                             |
| regex_v8               | 21.8 ms                                                                | 21.7 ms: 1.01x faster                                                             |
| pickle_list            | 4.15 us                                                                | 4.13 us: 1.01x faster                                                             |
| raytrace               | 282 ms                                                                 | 280 ms: 1.01x faster                                                              |
| sqlglot_normalize      | 107 ms                                                                 | 106 ms: 1.01x faster                                                              |
| mdp                    | 2.51 sec                                                               | 2.50 sec: 1.00x faster                                                            |
| pickle_dict            | 31.2 us                                                                | 31.1 us: 1.00x faster                                                             |
| pidigits               | 188 ms                                                                 | 188 ms: 1.00x slower                                                              |
| docutils               | 2.53 sec                                                               | 2.53 sec: 1.00x slower                                                            |
| create_gc_cycles       | 1.47 ms                                                                | 1.47 ms: 1.00x slower                                                             |
| aiohttp                | 1.01 ms                                                                | 1.01 ms: 1.00x slower                                                             |
| gunicorn               | 1.09 ms                                                                | 1.10 ms: 1.00x slower                                                             |
| mako                   | 9.95 ms                                                                | 9.99 ms: 1.00x slower                                                             |
| 2to3                   | 251 ms                                                                 | 253 ms: 1.00x slower                                                              |
| python_startup_no_site | 6.50 ms                                                                | 6.54 ms: 1.01x slower                                                             |
| float                  | 73.4 ms                                                                | 73.8 ms: 1.01x slower                                                             |
| python_startup         | 8.80 ms                                                                | 8.85 ms: 1.01x slower                                                             |
| unpack_sequence        | 41.8 ns                                                                | 42.0 ns: 1.01x slower                                                             |
| pyflate                | 418 ms                                                                 | 420 ms: 1.01x slower                                                              |
| async_generators       | 410 ms                                                                 | 413 ms: 1.01x slower                                                              |
| bench_thread_pool      | 788 us                                                                 | 793 us: 1.01x slower                                                              |
| sqlite_synth           | 2.60 us                                                                | 2.61 us: 1.01x slower                                                             |
| regex_dna              | 203 ms                                                                 | 205 ms: 1.01x slower                                                              |
| deltablue              | 3.20 ms                                                                | 3.23 ms: 1.01x slower                                                             |
| json_loads             | 24.1 us                                                                | 24.3 us: 1.01x slower                                                             |
| asyncio_tcp            | 502 ms                                                                 | 506 ms: 1.01x slower                                                              |
| hexiom                 | 6.02 ms                                                                | 6.08 ms: 1.01x slower                                                             |
| pickle                 | 10.2 us                                                                | 10.3 us: 1.01x slower                                                             |
| sympy_sum              | 164 ms                                                                 | 166 ms: 1.01x slower                                                              |
| chaos                  | 66.7 ms                                                                | 67.4 ms: 1.01x slower                                                             |
| richards               | 43.5 ms                                                                | 44.0 ms: 1.01x slower                                                             |
| crypto_pyaes           | 73.6 ms                                                                | 74.5 ms: 1.01x slower                                                             |
| unpickle               | 13.3 us                                                                | 13.5 us: 1.01x slower                                                             |
| dulwich_log            | 63.1 ms                                                                | 64.0 ms: 1.01x slower                                                             |
| spectral_norm          | 91.8 ms                                                                | 93.1 ms: 1.01x slower                                                             |
| sqlalchemy_imperative  | 17.5 ms                                                                | 17.7 ms: 1.01x slower                                                             |
| unpickle_pure_python   | 200 us                                                                 | 203 us: 1.02x slower                                                              |
| django_template        | 33.1 ms                                                                | 33.7 ms: 1.02x slower                                                             |
| coroutines             | 22.9 ms                                                                | 23.4 ms: 1.02x slower                                                             |
| scimark_sor            | 111 ms                                                                 | 113 ms: 1.02x slower                                                              |
| pathlib                | 17.6 ms                                                                | 18.1 ms: 1.02x slower                                                             |
| deepcopy_memo          | 33.6 us                                                                | 34.6 us: 1.03x slower                                                             |
| regex_effbot           | 3.43 ms                                                                | 3.73 ms: 1.09x slower                                                             |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                                      |

Benchmark hidden because not significant (34): djangocms, generators, pprint_safe_repr, chameleon, scimark_sparse_mat_mult, deepcopy_reduce, nbody, thrift, deepcopy, pprint_pformat, dask, regex_compile, bench_mp_pool, comprehensions, async_tree_memoization, sqlglot_optimize, sympy_integrate, logging_simple, sympy_str, json, json_dumps, sympy_expand, go, mypy2, pycparser, sqlalchemy_declarative, html5lib, tornado_http, coverage, async_tree_io, async_tree_none, logging_silent, async_tree_cpu_io_mixed, telco
