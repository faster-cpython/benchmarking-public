
# Results vs. base

- fork: carljm
- ref: inlinecomp2
- machine: linux-x86_64
- commit hash: ae0bd02
- commit date: 2023-02-13
- overall geometric mean: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230213-linux-x86_64-python-95cbb3d908175ccd8550-3.12.0a5+-95cbb3d | bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| docutils       | 2.55 sec                                                               | 2.54 sec: 1.00x faster                                        |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                  |

Benchmark hidden because not significant (4): 2to3, chameleon, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230213-linux-x86_64-python-95cbb3d908175ccd8550-3.12.0a5+-95cbb3d | bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| pidigits       | 197 ms                                                                 | 189 ms: 1.04x faster                                          |
| float          | 73.8 ms                                                                | 72.7 ms: 1.02x faster                                         |
| nbody          | 92.7 ms                                                                | 99.9 ms: 1.08x slower                                         |
| Geometric mean | (ref)                                                                  | 1.01x slower                                                  |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230213-linux-x86_64-python-95cbb3d908175ccd8550-3.12.0a5+-95cbb3d | bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02 |
|----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| regex_effbot   | 3.63 ms                                                                | 3.50 ms: 1.04x faster                                         |
| regex_compile  | 131 ms                                                                 | 129 ms: 1.02x faster                                          |
| regex_dna      | 198 ms                                                                 | 200 ms: 1.01x slower                                          |
| regex_v8       | 21.1 ms                                                                | 21.9 ms: 1.04x slower                                         |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                  |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230213-linux-x86_64-python-95cbb3d908175ccd8550-3.12.0a5+-95cbb3d | bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02 |
|----------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| pickle_list          | 4.26 us                                                                | 4.13 us: 1.03x faster                                         |
| pickle_dict          | 31.4 us                                                                | 30.7 us: 1.02x faster                                         |
| unpickle_list        | 5.11 us                                                                | 5.04 us: 1.01x faster                                         |
| xml_etree_process    | 55.7 ms                                                                | 55.2 ms: 1.01x faster                                         |
| xml_etree_generate   | 81.0 ms                                                                | 80.4 ms: 1.01x faster                                         |
| pickle_pure_python   | 288 us                                                                 | 286 us: 1.01x faster                                          |
| json_dumps           | 9.42 ms                                                                | 9.51 ms: 1.01x slower                                         |
| unpickle_pure_python | 197 us                                                                 | 200 us: 1.01x slower                                          |
| json_loads           | 23.7 us                                                                | 24.2 us: 1.02x slower                                         |
| Geometric mean       | (ref)                                                                  | 1.00x faster                                                  |

Benchmark hidden because not significant (4): unpickle, xml_etree_parse, xml_etree_iterparse, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230213-linux-x86_64-python-95cbb3d908175ccd8550-3.12.0a5+-95cbb3d | bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02 |
|------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| python_startup         | 8.96 ms                                                                | 8.89 ms: 1.01x faster                                         |
| python_startup_no_site | 6.50 ms                                                                | 6.45 ms: 1.01x faster                                         |
| Geometric mean         | (ref)                                                                  | 1.01x faster                                                  |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230213-linux-x86_64-python-95cbb3d908175ccd8550-3.12.0a5+-95cbb3d | bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02 |
|-----------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| genshi_text     | 21.4 ms                                                                | 20.8 ms: 1.03x faster                                         |
| genshi_xml      | 47.6 ms                                                                | 46.8 ms: 1.02x faster                                         |
| django_template | 33.9 ms                                                                | 33.3 ms: 1.02x faster                                         |
| mako            | 9.78 ms                                                                | 10.0 ms: 1.03x slower                                         |
| Geometric mean  | (ref)                                                                  | 1.01x faster                                                  |

All benchmarks:
===============

| Benchmark               | bm-20230213-linux-x86_64-python-95cbb3d908175ccd8550-3.12.0a5+-95cbb3d | bm-20230213-linux-x86_64-carljm-inlinecomp2-3.12.0a5+-ae0bd02 |
|-------------------------|:----------------------------------------------------------------------:|:-------------------------------------------------------------:|
| sqlglot_normalize       | 105 ms                                                                 | 99.7 ms: 1.05x faster                                         |
| spectral_norm           | 98.0 ms                                                                | 93.5 ms: 1.05x faster                                         |
| coroutines              | 23.9 ms                                                                | 22.9 ms: 1.04x faster                                         |
| pidigits                | 197 ms                                                                 | 189 ms: 1.04x faster                                          |
| async_tree_memoization  | 639 ms                                                                 | 615 ms: 1.04x faster                                          |
| async_tree_none         | 527 ms                                                                 | 507 ms: 1.04x faster                                          |
| regex_effbot            | 3.63 ms                                                                | 3.50 ms: 1.04x faster                                         |
| sqlalchemy_imperative   | 18.0 ms                                                                | 17.4 ms: 1.04x faster                                         |
| pickle_list             | 4.26 us                                                                | 4.13 us: 1.03x faster                                         |
| sqlglot_optimize        | 51.5 ms                                                                | 49.9 ms: 1.03x faster                                         |
| scimark_fft             | 309 ms                                                                 | 300 ms: 1.03x faster                                          |
| create_gc_cycles        | 1.48 ms                                                                | 1.44 ms: 1.03x faster                                         |
| genshi_text             | 21.4 ms                                                                | 20.8 ms: 1.03x faster                                         |
| sympy_expand            | 457 ms                                                                 | 446 ms: 1.02x faster                                          |
| crypto_pyaes            | 75.1 ms                                                                | 73.4 ms: 1.02x faster                                         |
| sqlalchemy_declarative  | 138 ms                                                                 | 135 ms: 1.02x faster                                          |
| thrift                  | 770 us                                                                 | 754 us: 1.02x faster                                          |
| meteor_contest          | 106 ms                                                                 | 104 ms: 1.02x faster                                          |
| pickle_dict             | 31.4 us                                                                | 30.7 us: 1.02x faster                                         |
| deltablue               | 3.24 ms                                                                | 3.18 ms: 1.02x faster                                         |
| mypy2                   | 331 ms                                                                 | 325 ms: 1.02x faster                                          |
| genshi_xml              | 47.6 ms                                                                | 46.8 ms: 1.02x faster                                         |
| deepcopy                | 338 us                                                                 | 332 us: 1.02x faster                                          |
| sympy_integrate         | 19.9 ms                                                                | 19.6 ms: 1.02x faster                                         |
| django_template         | 33.9 ms                                                                | 33.3 ms: 1.02x faster                                         |
| sympy_str               | 273 ms                                                                 | 268 ms: 1.02x faster                                          |
| async_tree_io           | 1.30 sec                                                               | 1.27 sec: 1.02x faster                                        |
| sqlite_synth            | 2.67 us                                                                | 2.63 us: 1.02x faster                                         |
| regex_compile           | 131 ms                                                                 | 129 ms: 1.02x faster                                          |
| pprint_pformat          | 1.41 sec                                                               | 1.39 sec: 1.02x faster                                        |
| sympy_sum               | 159 ms                                                                 | 156 ms: 1.02x faster                                          |
| float                   | 73.8 ms                                                                | 72.7 ms: 1.02x faster                                         |
| sqlglot_parse           | 1.44 ms                                                                | 1.42 ms: 1.01x faster                                         |
| raytrace                | 288 ms                                                                 | 284 ms: 1.01x faster                                          |
| async_tree_cpu_io_mixed | 754 ms                                                                 | 743 ms: 1.01x faster                                          |
| unpickle_list           | 5.11 us                                                                | 5.04 us: 1.01x faster                                         |
| generators              | 31.0 ms                                                                | 30.6 ms: 1.01x faster                                         |
| scimark_lu              | 111 ms                                                                 | 109 ms: 1.01x faster                                          |
| sqlglot_transpile       | 1.74 ms                                                                | 1.72 ms: 1.01x faster                                         |
| logging_silent          | 94.6 ns                                                                | 93.8 ns: 1.01x faster                                         |
| xml_etree_process       | 55.7 ms                                                                | 55.2 ms: 1.01x faster                                         |
| pprint_safe_repr        | 685 ms                                                                 | 679 ms: 1.01x faster                                          |
| python_startup          | 8.96 ms                                                                | 8.89 ms: 1.01x faster                                         |
| xml_etree_generate      | 81.0 ms                                                                | 80.4 ms: 1.01x faster                                         |
| bench_thread_pool       | 792 us                                                                 | 786 us: 1.01x faster                                          |
| pickle_pure_python      | 288 us                                                                 | 286 us: 1.01x faster                                          |
| python_startup_no_site  | 6.50 ms                                                                | 6.45 ms: 1.01x faster                                         |
| aiohttp                 | 1.01 ms                                                                | 1.00 ms: 1.01x faster                                         |
| docutils                | 2.55 sec                                                               | 2.54 sec: 1.00x faster                                        |
| mdp                     | 2.53 sec                                                               | 2.53 sec: 1.00x faster                                        |
| dulwich_log             | 62.6 ms                                                                | 62.9 ms: 1.00x slower                                         |
| asyncio_tcp             | 500 ms                                                                 | 502 ms: 1.00x slower                                          |
| deepcopy_memo           | 34.6 us                                                                | 34.9 us: 1.01x slower                                         |
| json_dumps              | 9.42 ms                                                                | 9.51 ms: 1.01x slower                                         |
| async_generators        | 410 ms                                                                 | 414 ms: 1.01x slower                                          |
| regex_dna               | 198 ms                                                                 | 200 ms: 1.01x slower                                          |
| deepcopy_reduce         | 2.99 us                                                                | 3.03 us: 1.01x slower                                         |
| logging_simple          | 5.75 us                                                                | 5.82 us: 1.01x slower                                         |
| scimark_monte_carlo     | 64.7 ms                                                                | 65.5 ms: 1.01x slower                                         |
| unpickle_pure_python    | 197 us                                                                 | 200 us: 1.01x slower                                          |
| pycparser               | 1.09 sec                                                               | 1.11 sec: 1.02x slower                                        |
| json_loads              | 23.7 us                                                                | 24.2 us: 1.02x slower                                         |
| scimark_sparse_mat_mult | 3.96 ms                                                                | 4.06 ms: 1.02x slower                                         |
| mako                    | 9.78 ms                                                                | 10.0 ms: 1.03x slower                                         |
| gc_traversal            | 3.91 ms                                                                | 4.04 ms: 1.03x slower                                         |
| regex_v8                | 21.1 ms                                                                | 21.9 ms: 1.04x slower                                         |
| fannkuch                | 361 ms                                                                 | 376 ms: 1.04x slower                                          |
| go                      | 133 ms                                                                 | 139 ms: 1.05x slower                                          |
| json                    | 4.57 ms                                                                | 4.85 ms: 1.06x slower                                         |
| nbody                   | 92.7 ms                                                                | 99.9 ms: 1.08x slower                                         |
| unpack_sequence         | 42.2 ns                                                                | 45.5 ns: 1.08x slower                                         |
| Geometric mean          | (ref)                                                                  | 1.01x faster                                                  |

Benchmark hidden because not significant (21): unpickle, html5lib, tornado_http, telco, gunicorn, xml_etree_parse, xml_etree_iterparse, chaos, scimark_sor, nqueens, pathlib, pyflate, bench_mp_pool, pickle, richards, 2to3, hexiom, logging_format, coverage, chameleon, djangocms
