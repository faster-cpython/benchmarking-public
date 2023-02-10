
# Results vs. base

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: cfb886d
- commit date: 2023-02-10
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230208-linux-x86_64-python-d9de0792482d2ded364b-3.12.0a5+-d9de079 | bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 252 ms: 1.00x slower                                                |
| chameleon      | 6.37 ms                                                                | 6.28 ms: 1.01x faster                                               |
| docutils       | 2.52 sec                                                               | 2.52 sec: 1.00x faster                                              |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (2): html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230208-linux-x86_64-python-d9de0792482d2ded364b-3.12.0a5+-d9de079 | bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 72.7 ms                                                                | 71.9 ms: 1.01x faster                                               |
| pidigits       | 198 ms                                                                 | 203 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230208-linux-x86_64-python-d9de0792482d2ded364b-3.12.0a5+-d9de079 | bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 21.6 ms                                                                | 21.0 ms: 1.03x faster                                               |
| regex_compile  | 129 ms                                                                 | 127 ms: 1.01x faster                                                |
| regex_effbot   | 3.33 ms                                                                | 3.43 ms: 1.03x slower                                               |
| regex_dna      | 211 ms                                                                 | 219 ms: 1.04x slower                                                |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230208-linux-x86_64-python-d9de0792482d2ded364b-3.12.0a5+-d9de079 | bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_list        | 5.00 us                                                                | 4.87 us: 1.03x faster                                               |
| json_loads           | 24.1 us                                                                | 23.8 us: 1.01x faster                                               |
| pickle_pure_python   | 290 us                                                                 | 287 us: 1.01x faster                                                |
| unpickle_pure_python | 198 us                                                                 | 197 us: 1.01x faster                                                |
| xml_etree_iterparse  | 103 ms                                                                 | 103 ms: 1.01x slower                                                |
| pickle               | 10.0 us                                                                | 10.1 us: 1.01x slower                                               |
| xml_etree_process    | 55.2 ms                                                                | 55.7 ms: 1.01x slower                                               |
| xml_etree_generate   | 79.7 ms                                                                | 80.8 ms: 1.01x slower                                               |
| pickle_dict          | 30.1 us                                                                | 30.9 us: 1.03x slower                                               |
| pickle_list          | 3.98 us                                                                | 4.09 us: 1.03x slower                                               |
| Geometric mean       | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (3): xml_etree_parse, unpickle, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230208-linux-x86_64-python-d9de0792482d2ded364b-3.12.0a5+-d9de079 | bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.86 ms                                                                | 8.92 ms: 1.01x slower                                               |
| python_startup_no_site | 6.43 ms                                                                | 6.48 ms: 1.01x slower                                               |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230208-linux-x86_64-python-d9de0792482d2ded364b-3.12.0a5+-d9de079 | bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 33.5 ms                                                                | 33.1 ms: 1.01x faster                                               |
| genshi_xml      | 47.4 ms                                                                | 46.9 ms: 1.01x faster                                               |
| genshi_text     | 20.7 ms                                                                | 20.6 ms: 1.01x faster                                               |
| mako            | 9.61 ms                                                                | 9.81 ms: 1.02x slower                                               |
| Geometric mean  | (ref)                                                                  | 1.00x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20230208-linux-x86_64-python-d9de0792482d2ded364b-3.12.0a5+-d9de079 | bm-20230210-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-cfb886d |
|-------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| mdp                     | 2.68 sec                                                               | 2.44 sec: 1.10x faster                                              |
| gc_traversal            | 3.64 ms                                                                | 3.53 ms: 1.03x faster                                               |
| coverage                | 99.0 ms                                                                | 95.9 ms: 1.03x faster                                               |
| regex_v8                | 21.6 ms                                                                | 21.0 ms: 1.03x faster                                               |
| unpickle_list           | 5.00 us                                                                | 4.87 us: 1.03x faster                                               |
| generators              | 77.2 ms                                                                | 75.4 ms: 1.02x faster                                               |
| raytrace                | 287 ms                                                                 | 281 ms: 1.02x faster                                                |
| chameleon               | 6.37 ms                                                                | 6.28 ms: 1.01x faster                                               |
| deepcopy_reduce         | 2.98 us                                                                | 2.93 us: 1.01x faster                                               |
| scimark_fft             | 307 ms                                                                 | 303 ms: 1.01x faster                                                |
| sqlglot_normalize       | 106 ms                                                                 | 105 ms: 1.01x faster                                                |
| django_template         | 33.5 ms                                                                | 33.1 ms: 1.01x faster                                               |
| regex_compile           | 129 ms                                                                 | 127 ms: 1.01x faster                                                |
| json_loads              | 24.1 us                                                                | 23.8 us: 1.01x faster                                               |
| genshi_xml              | 47.4 ms                                                                | 46.9 ms: 1.01x faster                                               |
| float                   | 72.7 ms                                                                | 71.9 ms: 1.01x faster                                               |
| pyflate                 | 400 ms                                                                 | 395 ms: 1.01x faster                                                |
| meteor_contest          | 106 ms                                                                 | 105 ms: 1.01x faster                                                |
| unpack_sequence         | 43.8 ns                                                                | 43.3 ns: 1.01x faster                                               |
| sympy_str               | 273 ms                                                                 | 270 ms: 1.01x faster                                                |
| pickle_pure_python      | 290 us                                                                 | 287 us: 1.01x faster                                                |
| scimark_sor             | 106 ms                                                                 | 105 ms: 1.01x faster                                                |
| genshi_text             | 20.7 ms                                                                | 20.6 ms: 1.01x faster                                               |
| unpickle_pure_python    | 198 us                                                                 | 197 us: 1.01x faster                                                |
| dulwich_log             | 62.6 ms                                                                | 62.3 ms: 1.00x faster                                               |
| sympy_integrate         | 19.9 ms                                                                | 19.8 ms: 1.00x faster                                               |
| gunicorn                | 1.08 ms                                                                | 1.08 ms: 1.00x faster                                               |
| docutils                | 2.52 sec                                                               | 2.52 sec: 1.00x faster                                              |
| 2to3                    | 251 ms                                                                 | 252 ms: 1.00x slower                                                |
| nqueens                 | 78.8 ms                                                                | 79.1 ms: 1.00x slower                                               |
| create_gc_cycles        | 1.46 ms                                                                | 1.46 ms: 1.00x slower                                               |
| logging_simple          | 5.74 us                                                                | 5.77 us: 1.01x slower                                               |
| python_startup          | 8.86 ms                                                                | 8.92 ms: 1.01x slower                                               |
| python_startup_no_site  | 6.43 ms                                                                | 6.48 ms: 1.01x slower                                               |
| xml_etree_iterparse     | 103 ms                                                                 | 103 ms: 1.01x slower                                                |
| coroutines              | 25.4 ms                                                                | 25.6 ms: 1.01x slower                                               |
| pickle                  | 10.0 us                                                                | 10.1 us: 1.01x slower                                               |
| deltablue               | 3.17 ms                                                                | 3.20 ms: 1.01x slower                                               |
| pathlib                 | 17.6 ms                                                                | 17.8 ms: 1.01x slower                                               |
| xml_etree_process       | 55.2 ms                                                                | 55.7 ms: 1.01x slower                                               |
| fannkuch                | 364 ms                                                                 | 368 ms: 1.01x slower                                                |
| telco                   | 6.34 ms                                                                | 6.42 ms: 1.01x slower                                               |
| xml_etree_generate      | 79.7 ms                                                                | 80.8 ms: 1.01x slower                                               |
| asyncio_tcp             | 490 ms                                                                 | 496 ms: 1.01x slower                                                |
| json                    | 4.59 ms                                                                | 4.67 ms: 1.02x slower                                               |
| pycparser               | 1.10 sec                                                               | 1.13 sec: 1.02x slower                                              |
| mako                    | 9.61 ms                                                                | 9.81 ms: 1.02x slower                                               |
| logging_format          | 6.26 us                                                                | 6.41 us: 1.02x slower                                               |
| pidigits                | 198 ms                                                                 | 203 ms: 1.03x slower                                                |
| pickle_dict             | 30.1 us                                                                | 30.9 us: 1.03x slower                                               |
| scimark_sparse_mat_mult | 3.91 ms                                                                | 4.02 ms: 1.03x slower                                               |
| pickle_list             | 3.98 us                                                                | 4.09 us: 1.03x slower                                               |
| regex_effbot            | 3.33 ms                                                                | 3.43 ms: 1.03x slower                                               |
| regex_dna               | 211 ms                                                                 | 219 ms: 1.04x slower                                                |
| crypto_pyaes            | 73.5 ms                                                                | 76.5 ms: 1.04x slower                                               |
| richards                | 41.5 ms                                                                | 43.6 ms: 1.05x slower                                               |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (36): html5lib, async_tree_cpu_io_mixed, pprint_safe_repr, sqlglot_transpile, sympy_sum, hexiom, thrift, chaos, sympy_expand, sqlite_synth, async_tree_io, sqlalchemy_declarative, deepcopy, aiohttp, sqlglot_optimize, xml_etree_parse, bench_mp_pool, bench_thread_pool, sqlglot_parse, mypy2, pprint_pformat, deepcopy_memo, async_generators, logging_silent, scimark_monte_carlo, scimark_lu, unpickle, tornado_http, async_tree_none, go, json_dumps, djangocms, spectral_norm, nbody, async_tree_memoization, sqlalchemy_imperative
