
# Results vs. base

- fork: iritkatriel
- ref: int_freelist
- machine: linux-x86_64
- commit hash: 1134727
- commit date: 2023-02-08
- overall geometric mean: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230208-linux-x86_64-python-d9de0792482d2ded364b-3.12.0a5+-d9de079 | bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-1134727 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 251 ms                                                                 | 252 ms: 1.00x slower                                                |
| chameleon      | 6.37 ms                                                                | 6.30 ms: 1.01x faster                                               |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                        |

Benchmark hidden because not significant (3): docutils, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230208-linux-x86_64-python-d9de0792482d2ded364b-3.12.0a5+-d9de079 | bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-1134727 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 72.7 ms                                                                | 71.4 ms: 1.02x faster                                               |
| pidigits       | 198 ms                                                                 | 203 ms: 1.03x slower                                                |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230208-linux-x86_64-python-d9de0792482d2ded364b-3.12.0a5+-d9de079 | bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-1134727 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_v8       | 21.6 ms                                                                | 21.7 ms: 1.00x slower                                               |
| regex_dna      | 211 ms                                                                 | 212 ms: 1.01x slower                                                |
| regex_effbot   | 3.33 ms                                                                | 3.46 ms: 1.04x slower                                               |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230208-linux-x86_64-python-d9de0792482d2ded364b-3.12.0a5+-d9de079 | bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-1134727 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| unpickle_list        | 5.00 us                                                                | 4.89 us: 1.02x faster                                               |
| xml_etree_iterparse  | 103 ms                                                                 | 102 ms: 1.01x faster                                                |
| unpickle_pure_python | 198 us                                                                 | 197 us: 1.01x faster                                                |
| pickle_pure_python   | 290 us                                                                 | 288 us: 1.01x faster                                                |
| json_dumps           | 9.54 ms                                                                | 9.60 ms: 1.01x slower                                               |
| xml_etree_generate   | 79.7 ms                                                                | 80.4 ms: 1.01x slower                                               |
| pickle               | 10.0 us                                                                | 10.2 us: 1.01x slower                                               |
| pickle_list          | 3.98 us                                                                | 4.22 us: 1.06x slower                                               |
| pickle_dict          | 30.1 us                                                                | 32.0 us: 1.06x slower                                               |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                        |

Benchmark hidden because not significant (4): xml_etree_parse, unpickle, xml_etree_process, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230208-linux-x86_64-python-d9de0792482d2ded364b-3.12.0a5+-d9de079 | bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-1134727 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup         | 8.86 ms                                                                | 8.92 ms: 1.01x slower                                               |
| python_startup_no_site | 6.43 ms                                                                | 6.48 ms: 1.01x slower                                               |
| Geometric mean         | (ref)                                                                  | 1.01x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230208-linux-x86_64-python-d9de0792482d2ded364b-3.12.0a5+-d9de079 | bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-1134727 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| django_template | 33.5 ms                                                                | 32.9 ms: 1.02x faster                                               |
| genshi_xml      | 47.4 ms                                                                | 47.1 ms: 1.01x faster                                               |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                        |

Benchmark hidden because not significant (2): genshi_text, mako

All benchmarks:
===============

| Benchmark               | bm-20230208-linux-x86_64-python-d9de0792482d2ded364b-3.12.0a5+-d9de079 | bm-20230208-linux-x86_64-iritkatriel-int_freelist-3.12.0a5+-1134727 |
|-------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------------:|
| scimark_fft             | 307 ms                                                                 | 296 ms: 1.04x faster                                                |
| unpack_sequence         | 43.8 ns                                                                | 42.2 ns: 1.04x faster                                               |
| gc_traversal            | 3.64 ms                                                                | 3.52 ms: 1.03x faster                                               |
| spectral_norm           | 98.1 ms                                                                | 95.2 ms: 1.03x faster                                               |
| mdp                     | 2.68 sec                                                               | 2.60 sec: 1.03x faster                                              |
| scimark_sparse_mat_mult | 3.91 ms                                                                | 3.81 ms: 1.02x faster                                               |
| unpickle_list           | 5.00 us                                                                | 4.89 us: 1.02x faster                                               |
| scimark_monte_carlo     | 66.1 ms                                                                | 64.6 ms: 1.02x faster                                               |
| django_template         | 33.5 ms                                                                | 32.9 ms: 1.02x faster                                               |
| float                   | 72.7 ms                                                                | 71.4 ms: 1.02x faster                                               |
| chameleon               | 6.37 ms                                                                | 6.30 ms: 1.01x faster                                               |
| async_generators        | 428 ms                                                                 | 424 ms: 1.01x faster                                                |
| sqlglot_normalize       | 106 ms                                                                 | 105 ms: 1.01x faster                                                |
| sympy_str               | 273 ms                                                                 | 270 ms: 1.01x faster                                                |
| genshi_xml              | 47.4 ms                                                                | 47.1 ms: 1.01x faster                                               |
| xml_etree_iterparse     | 103 ms                                                                 | 102 ms: 1.01x faster                                                |
| deepcopy_reduce         | 2.98 us                                                                | 2.96 us: 1.01x faster                                               |
| sqlite_synth            | 2.58 us                                                                | 2.56 us: 1.01x faster                                               |
| pprint_safe_repr        | 684 ms                                                                 | 680 ms: 1.01x faster                                                |
| unpickle_pure_python    | 198 us                                                                 | 197 us: 1.01x faster                                                |
| thrift                  | 760 us                                                                 | 755 us: 1.01x faster                                                |
| pickle_pure_python      | 290 us                                                                 | 288 us: 1.01x faster                                                |
| logging_silent          | 92.3 ns                                                                | 91.8 ns: 1.01x faster                                               |
| gunicorn                | 1.08 ms                                                                | 1.07 ms: 1.01x faster                                               |
| chaos                   | 66.0 ms                                                                | 65.7 ms: 1.01x faster                                               |
| dulwich_log             | 62.6 ms                                                                | 62.3 ms: 1.00x faster                                               |
| sympy_integrate         | 19.9 ms                                                                | 19.8 ms: 1.00x faster                                               |
| sympy_sum               | 158 ms                                                                 | 157 ms: 1.00x faster                                                |
| hexiom                  | 5.97 ms                                                                | 5.96 ms: 1.00x faster                                               |
| sympy_expand            | 458 ms                                                                 | 457 ms: 1.00x faster                                                |
| go                      | 135 ms                                                                 | 135 ms: 1.00x slower                                                |
| create_gc_cycles        | 1.46 ms                                                                | 1.46 ms: 1.00x slower                                               |
| pyflate                 | 400 ms                                                                 | 402 ms: 1.00x slower                                                |
| 2to3                    | 251 ms                                                                 | 252 ms: 1.00x slower                                                |
| bench_thread_pool       | 781 us                                                                 | 785 us: 1.00x slower                                                |
| regex_v8                | 21.6 ms                                                                | 21.7 ms: 1.00x slower                                               |
| asyncio_tcp             | 490 ms                                                                 | 492 ms: 1.01x slower                                                |
| regex_dna               | 211 ms                                                                 | 212 ms: 1.01x slower                                                |
| fannkuch                | 364 ms                                                                 | 366 ms: 1.01x slower                                                |
| deepcopy_memo           | 34.5 us                                                                | 34.7 us: 1.01x slower                                               |
| python_startup          | 8.86 ms                                                                | 8.92 ms: 1.01x slower                                               |
| json_dumps              | 9.54 ms                                                                | 9.60 ms: 1.01x slower                                               |
| python_startup_no_site  | 6.43 ms                                                                | 6.48 ms: 1.01x slower                                               |
| scimark_sor             | 106 ms                                                                 | 107 ms: 1.01x slower                                                |
| xml_etree_generate      | 79.7 ms                                                                | 80.4 ms: 1.01x slower                                               |
| json                    | 4.59 ms                                                                | 4.63 ms: 1.01x slower                                               |
| deepcopy                | 331 us                                                                 | 334 us: 1.01x slower                                                |
| deltablue               | 3.17 ms                                                                | 3.21 ms: 1.01x slower                                               |
| pickle                  | 10.0 us                                                                | 10.2 us: 1.01x slower                                               |
| logging_simple          | 5.74 us                                                                | 5.82 us: 1.01x slower                                               |
| logging_format          | 6.26 us                                                                | 6.35 us: 1.01x slower                                               |
| meteor_contest          | 106 ms                                                                 | 108 ms: 1.02x slower                                                |
| coroutines              | 25.4 ms                                                                | 25.9 ms: 1.02x slower                                               |
| richards                | 41.5 ms                                                                | 42.4 ms: 1.02x slower                                               |
| telco                   | 6.34 ms                                                                | 6.50 ms: 1.02x slower                                               |
| pidigits                | 198 ms                                                                 | 203 ms: 1.03x slower                                                |
| generators              | 77.2 ms                                                                | 79.4 ms: 1.03x slower                                               |
| pycparser               | 1.10 sec                                                               | 1.14 sec: 1.03x slower                                              |
| regex_effbot            | 3.33 ms                                                                | 3.46 ms: 1.04x slower                                               |
| crypto_pyaes            | 73.5 ms                                                                | 76.5 ms: 1.04x slower                                               |
| pickle_list             | 3.98 us                                                                | 4.22 us: 1.06x slower                                               |
| pickle_dict             | 30.1 us                                                                | 32.0 us: 1.06x slower                                               |
| Geometric mean          | (ref)                                                                  | 1.00x slower                                                        |

Benchmark hidden because not significant (30): coverage, xml_etree_parse, sqlalchemy_declarative, sqlalchemy_imperative, raytrace, genshi_text, unpickle, async_tree_io, sqlglot_transpile, html5lib, scimark_lu, xml_etree_process, bench_mp_pool, aiohttp, sqlglot_optimize, mako, mypy2, docutils, async_tree_cpu_io_mixed, json_loads, tornado_http, sqlglot_parse, regex_compile, pprint_pformat, nqueens, pathlib, nbody, djangocms, async_tree_none, async_tree_memoization
