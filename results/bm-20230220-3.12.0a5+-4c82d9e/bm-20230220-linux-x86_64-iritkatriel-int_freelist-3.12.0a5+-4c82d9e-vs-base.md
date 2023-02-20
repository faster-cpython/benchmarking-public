
# Results vs. base

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 4c82d9e
- commit date: 2023-02-20
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230208-linux-x86_64-python-d9de0792482d2ded364b-3.12.0a5+-d9de079 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| chameleon      | 6.37 ms                                                                | 6.25 ms: 1.02x faster                                               |
| docutils       | 2.52 sec                                                               | 2.53 sec: 1.00x slower                                              |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (3): 2to3, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230208-linux-x86_64-python-d9de0792482d2ded364b-3.12.0a5+-d9de079 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| pidigits       | 198 ms                                                                 | 191 ms: 1.04x faster                                                |
| float          | 72.7 ms                                                                | 72.2 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230208-linux-x86_64-python-d9de0792482d2ded364b-3.12.0a5+-d9de079 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_dna      | 211 ms                                                                 | 199 ms: 1.06x faster                                                |
| regex_v8       | 21.6 ms                                                                | 21.2 ms: 1.02x faster                                               |
| regex_compile  | 129 ms                                                                 | 127 ms: 1.01x faster                                                |
| regex_effbot   | 3.33 ms                                                                | 3.46 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                                  | 1.01x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230208-linux-x86_64-python-d9de0792482d2ded364b-3.12.0a5+-d9de079 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_list        | 5.00 us                                                                | 4.80 us: 1.04x faster                                               |
| json_dumps           | 9.54 ms                                                                | 9.44 ms: 1.01x faster                                               |
| json_loads           | 24.1 us                                                                | 23.8 us: 1.01x faster                                               |
| xml_etree_iterparse  | 103 ms                                                                 | 102 ms: 1.01x faster                                                |
| unpickle_pure_python | 198 us                                                                 | 197 us: 1.01x faster                                                |
| pickle_list          | 3.98 us                                                                | 4.08 us: 1.03x slower                                               |
| xml_etree_generate   | 79.7 ms                                                                | 82.2 ms: 1.03x slower                                               |
| xml_etree_process    | 55.2 ms                                                                | 57.2 ms: 1.04x slower                                               |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (5): pickle_dict, xml_etree_parse, unpickle, pickle, pickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230208-linux-x86_64-python-d9de0792482d2ded364b-3.12.0a5+-d9de079 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.86 ms                                                                | 8.95 ms: 1.01x slower                                               |
| python_startup_no_site | 6.43 ms                                                                | 6.50 ms: 1.01x slower                                               |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230208-linux-x86_64-python-d9de0792482d2ded364b-3.12.0a5+-d9de079 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 33.5 ms                                                                | 32.9 ms: 1.02x faster                                               |
| mako            | 9.61 ms                                                                | 9.51 ms: 1.01x faster                                               |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (2): genshi_text, genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20230208-linux-x86_64-python-d9de0792482d2ded364b-3.12.0a5+-d9de079 | bm-20230220-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-4c82d9e |
|-------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                     | 2.68 sec                                                               | 2.52 sec: 1.06x faster                                              |
| regex_dna               | 211 ms                                                                 | 199 ms: 1.06x faster                                                |
| spectral_norm           | 98.1 ms                                                                | 93.8 ms: 1.05x faster                                               |
| unpickle_list           | 5.00 us                                                                | 4.80 us: 1.04x faster                                               |
| pidigits                | 198 ms                                                                 | 191 ms: 1.04x faster                                                |
| unpack_sequence         | 43.8 ns                                                                | 42.5 ns: 1.03x faster                                               |
| raytrace                | 287 ms                                                                 | 281 ms: 1.02x faster                                                |
| chameleon               | 6.37 ms                                                                | 6.25 ms: 1.02x faster                                               |
| django_template         | 33.5 ms                                                                | 32.9 ms: 1.02x faster                                               |
| deepcopy_reduce         | 2.98 us                                                                | 2.93 us: 1.02x faster                                               |
| regex_v8                | 21.6 ms                                                                | 21.2 ms: 1.02x faster                                               |
| chaos                   | 66.0 ms                                                                | 65.0 ms: 1.02x faster                                               |
| scimark_fft             | 307 ms                                                                 | 303 ms: 1.01x faster                                                |
| async_generators        | 428 ms                                                                 | 423 ms: 1.01x faster                                                |
| scimark_monte_carlo     | 66.1 ms                                                                | 65.3 ms: 1.01x faster                                               |
| regex_compile           | 129 ms                                                                 | 127 ms: 1.01x faster                                                |
| gunicorn                | 1.08 ms                                                                | 1.07 ms: 1.01x faster                                               |
| coverage                | 99.0 ms                                                                | 97.9 ms: 1.01x faster                                               |
| mako                    | 9.61 ms                                                                | 9.51 ms: 1.01x faster                                               |
| json_dumps              | 9.54 ms                                                                | 9.44 ms: 1.01x faster                                               |
| sympy_str               | 273 ms                                                                 | 270 ms: 1.01x faster                                                |
| json_loads              | 24.1 us                                                                | 23.8 us: 1.01x faster                                               |
| sqlite_synth            | 2.58 us                                                                | 2.56 us: 1.01x faster                                               |
| dulwich_log             | 62.6 ms                                                                | 62.0 ms: 1.01x faster                                               |
| xml_etree_iterparse     | 103 ms                                                                 | 102 ms: 1.01x faster                                                |
| nqueens                 | 78.8 ms                                                                | 78.2 ms: 1.01x faster                                               |
| logging_silent          | 92.3 ns                                                                | 91.6 ns: 1.01x faster                                               |
| float                   | 72.7 ms                                                                | 72.2 ms: 1.01x faster                                               |
| unpickle_pure_python    | 198 us                                                                 | 197 us: 1.01x faster                                                |
| aiohttp                 | 1.00 ms                                                                | 997 us: 1.01x faster                                                |
| bench_thread_pool       | 781 us                                                                 | 783 us: 1.00x slower                                                |
| docutils                | 2.52 sec                                                               | 2.53 sec: 1.00x slower                                              |
| deepcopy                | 331 us                                                                 | 332 us: 1.01x slower                                                |
| sqlglot_normalize       | 106 ms                                                                 | 107 ms: 1.01x slower                                                |
| deepcopy_memo           | 34.5 us                                                                | 34.7 us: 1.01x slower                                               |
| go                      | 135 ms                                                                 | 136 ms: 1.01x slower                                                |
| create_gc_cycles        | 1.46 ms                                                                | 1.47 ms: 1.01x slower                                               |
| deltablue               | 3.17 ms                                                                | 3.20 ms: 1.01x slower                                               |
| python_startup          | 8.86 ms                                                                | 8.95 ms: 1.01x slower                                               |
| sqlglot_optimize        | 51.1 ms                                                                | 51.7 ms: 1.01x slower                                               |
| python_startup_no_site  | 6.43 ms                                                                | 6.50 ms: 1.01x slower                                               |
| coroutines              | 25.4 ms                                                                | 25.7 ms: 1.01x slower                                               |
| richards                | 41.5 ms                                                                | 42.0 ms: 1.01x slower                                               |
| async_tree_none         | 525 ms                                                                 | 532 ms: 1.01x slower                                                |
| asyncio_tcp             | 490 ms                                                                 | 496 ms: 1.01x slower                                                |
| scimark_sparse_mat_mult | 3.91 ms                                                                | 3.96 ms: 1.01x slower                                               |
| pathlib                 | 17.6 ms                                                                | 17.9 ms: 1.01x slower                                               |
| fannkuch                | 364 ms                                                                 | 370 ms: 1.02x slower                                                |
| pickle_list             | 3.98 us                                                                | 4.08 us: 1.03x slower                                               |
| xml_etree_generate      | 79.7 ms                                                                | 82.2 ms: 1.03x slower                                               |
| xml_etree_process       | 55.2 ms                                                                | 57.2 ms: 1.04x slower                                               |
| regex_effbot            | 3.33 ms                                                                | 3.46 ms: 1.04x slower                                               |
| crypto_pyaes            | 73.5 ms                                                                | 76.4 ms: 1.04x slower                                               |
| gc_traversal            | 3.64 ms                                                                | 4.29 ms: 1.18x slower                                               |
| Geometric mean          | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (38): djangocms, pickle_dict, meteor_contest, xml_etree_parse, async_tree_io, scimark_sor, sqlglot_transpile, pyflate, pycparser, sqlalchemy_declarative, unpickle, pickle, thrift, sympy_integrate, tornado_http, sqlglot_parse, async_tree_cpu_io_mixed, sympy_sum, sympy_expand, genshi_text, pickle_pure_python, bench_mp_pool, nbody, pprint_safe_repr, 2to3, hexiom, pprint_pformat, generators, logging_format, logging_simple, genshi_xml, mypy2, sqlalchemy_imperative, telco, json, scimark_lu, html5lib, async_tree_memoization
