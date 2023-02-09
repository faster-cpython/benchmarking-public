
# Results vs. base

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 827b81b
- commit date: 2023-02-09
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230208-linux-x86_64-python-d9de0792482d2ded364b-3.12.0a5+-d9de079 | bm-20230209-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-827b81b |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 252 ms: 1.00x slower                                                |
| docutils       | 2.52 sec                                                               | 2.54 sec: 1.01x slower                                              |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (3): chameleon, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230208-linux-x86_64-python-d9de0792482d2ded364b-3.12.0a5+-d9de079 | bm-20230209-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-827b81b |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 198 ms                                                                 | 191 ms: 1.04x faster                                                |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230208-linux-x86_64-python-d9de0792482d2ded364b-3.12.0a5+-d9de079 | bm-20230209-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-827b81b |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_compile  | 129 ms                                                                 | 128 ms: 1.01x faster                                                |
| regex_v8       | 21.6 ms                                                                | 21.4 ms: 1.01x faster                                               |
| regex_dna      | 211 ms                                                                 | 218 ms: 1.04x slower                                                |
| regex_effbot   | 3.33 ms                                                                | 3.46 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark          | bm-20230208-linux-x86_64-python-d9de0792482d2ded364b-3.12.0a5+-d9de079 | bm-20230209-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-827b81b |
|--------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_list      | 5.00 us                                                                | 4.88 us: 1.02x faster                                               |
| xml_etree_process  | 55.2 ms                                                                | 54.9 ms: 1.00x faster                                               |
| json_dumps         | 9.54 ms                                                                | 9.58 ms: 1.00x slower                                               |
| xml_etree_generate | 79.7 ms                                                                | 80.4 ms: 1.01x slower                                               |
| pickle             | 10.0 us                                                                | 10.1 us: 1.01x slower                                               |
| pickle_dict        | 30.1 us                                                                | 31.2 us: 1.04x slower                                               |
| pickle_list        | 3.98 us                                                                | 4.21 us: 1.06x slower                                               |
| Geometric mean     | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (6): xml_etree_parse, unpickle, json_loads, pickle_pure_python, unpickle_pure_python, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230208-linux-x86_64-python-d9de0792482d2ded364b-3.12.0a5+-d9de079 | bm-20230209-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-827b81b |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.43 ms                                                                | 6.47 ms: 1.01x slower                                               |
| python_startup         | 8.86 ms                                                                | 8.93 ms: 1.01x slower                                               |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20230208-linux-x86_64-python-d9de0792482d2ded364b-3.12.0a5+-d9de079 | bm-20230209-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-827b81b |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml     | 47.4 ms                                                                | 47.1 ms: 1.01x faster                                               |
| genshi_text    | 20.7 ms                                                                | 21.0 ms: 1.01x slower                                               |
| mako           | 9.61 ms                                                                | 9.73 ms: 1.01x slower                                               |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20230208-linux-x86_64-python-d9de0792482d2ded364b-3.12.0a5+-d9de079 | bm-20230209-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-827b81b |
|-------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                     | 2.68 sec                                                               | 2.49 sec: 1.08x faster                                              |
| pidigits                | 198 ms                                                                 | 191 ms: 1.04x faster                                                |
| unpack_sequence         | 43.8 ns                                                                | 42.3 ns: 1.04x faster                                               |
| unpickle_list           | 5.00 us                                                                | 4.88 us: 1.02x faster                                               |
| deepcopy_reduce         | 2.98 us                                                                | 2.92 us: 1.02x faster                                               |
| scimark_fft             | 307 ms                                                                 | 302 ms: 1.02x faster                                                |
| pycparser               | 1.10 sec                                                               | 1.09 sec: 1.01x faster                                              |
| coverage                | 99.0 ms                                                                | 97.9 ms: 1.01x faster                                               |
| async_generators        | 428 ms                                                                 | 424 ms: 1.01x faster                                                |
| regex_compile           | 129 ms                                                                 | 128 ms: 1.01x faster                                                |
| nqueens                 | 78.8 ms                                                                | 78.1 ms: 1.01x faster                                               |
| genshi_xml              | 47.4 ms                                                                | 47.1 ms: 1.01x faster                                               |
| sympy_str               | 273 ms                                                                 | 270 ms: 1.01x faster                                                |
| regex_v8                | 21.6 ms                                                                | 21.4 ms: 1.01x faster                                               |
| deepcopy_memo           | 34.5 us                                                                | 34.2 us: 1.01x faster                                               |
| chaos                   | 66.0 ms                                                                | 65.6 ms: 1.01x faster                                               |
| deepcopy                | 331 us                                                                 | 329 us: 1.01x faster                                                |
| xml_etree_process       | 55.2 ms                                                                | 54.9 ms: 1.00x faster                                               |
| dulwich_log             | 62.6 ms                                                                | 62.4 ms: 1.00x faster                                               |
| sympy_integrate         | 19.9 ms                                                                | 19.8 ms: 1.00x faster                                               |
| 2to3                    | 251 ms                                                                 | 252 ms: 1.00x slower                                                |
| bench_thread_pool       | 781 us                                                                 | 785 us: 1.00x slower                                                |
| json_dumps              | 9.54 ms                                                                | 9.58 ms: 1.00x slower                                               |
| docutils                | 2.52 sec                                                               | 2.54 sec: 1.01x slower                                              |
| python_startup_no_site  | 6.43 ms                                                                | 6.47 ms: 1.01x slower                                               |
| coroutines              | 25.4 ms                                                                | 25.5 ms: 1.01x slower                                               |
| sqlglot_transpile       | 1.71 ms                                                                | 1.73 ms: 1.01x slower                                               |
| generators              | 77.2 ms                                                                | 77.7 ms: 1.01x slower                                               |
| python_startup          | 8.86 ms                                                                | 8.93 ms: 1.01x slower                                               |
| sqlglot_parse           | 1.41 ms                                                                | 1.43 ms: 1.01x slower                                               |
| xml_etree_generate      | 79.7 ms                                                                | 80.4 ms: 1.01x slower                                               |
| pickle                  | 10.0 us                                                                | 10.1 us: 1.01x slower                                               |
| sqlite_synth            | 2.58 us                                                                | 2.61 us: 1.01x slower                                               |
| pathlib                 | 17.6 ms                                                                | 17.8 ms: 1.01x slower                                               |
| genshi_text             | 20.7 ms                                                                | 21.0 ms: 1.01x slower                                               |
| sqlglot_optimize        | 51.1 ms                                                                | 51.7 ms: 1.01x slower                                               |
| mako                    | 9.61 ms                                                                | 9.73 ms: 1.01x slower                                               |
| logging_format          | 6.26 us                                                                | 6.36 us: 1.02x slower                                               |
| asyncio_tcp             | 490 ms                                                                 | 498 ms: 1.02x slower                                                |
| deltablue               | 3.17 ms                                                                | 3.22 ms: 1.02x slower                                               |
| pyflate                 | 400 ms                                                                 | 407 ms: 1.02x slower                                                |
| scimark_sparse_mat_mult | 3.91 ms                                                                | 3.99 ms: 1.02x slower                                               |
| pprint_safe_repr        | 684 ms                                                                 | 699 ms: 1.02x slower                                                |
| telco                   | 6.34 ms                                                                | 6.49 ms: 1.02x slower                                               |
| pprint_pformat          | 1.39 sec                                                               | 1.42 sec: 1.02x slower                                              |
| regex_dna               | 211 ms                                                                 | 218 ms: 1.04x slower                                                |
| pickle_dict             | 30.1 us                                                                | 31.2 us: 1.04x slower                                               |
| regex_effbot            | 3.33 ms                                                                | 3.46 ms: 1.04x slower                                               |
| richards                | 41.5 ms                                                                | 43.3 ms: 1.04x slower                                               |
| gc_traversal            | 3.64 ms                                                                | 3.85 ms: 1.06x slower                                               |
| crypto_pyaes            | 73.5 ms                                                                | 77.7 ms: 1.06x slower                                               |
| pickle_list             | 3.98 us                                                                | 4.21 us: 1.06x slower                                               |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (40): async_tree_memoization, xml_etree_parse, thrift, async_tree_cpu_io_mixed, async_tree_io, djangocms, scimark_monte_carlo, unpickle, raytrace, gunicorn, json_loads, sympy_sum, meteor_contest, nbody, tornado_http, pickle_pure_python, aiohttp, fannkuch, sqlalchemy_imperative, bench_mp_pool, hexiom, scimark_sor, logging_simple, unpickle_pure_python, sqlalchemy_declarative, create_gc_cycles, sqlglot_normalize, go, sympy_expand, mypy2, chameleon, django_template, float, async_tree_none, spectral_norm, xml_etree_iterparse, html5lib, json, logging_silent, scimark_lu
