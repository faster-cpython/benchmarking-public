
# Results vs. base

- fork: iritkatriel
- ref: reg_base
- machine: linux-x86_64
- commit hash: 762745a
- commit date: 2023-01-11
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230111-linux-x86_64-python-762745a124cbc297cf2f-3.12.0a4+-762745a | bm-20230111-linux-x86_64-iritkatriel-reg_base-3.12.0a4+-762745a |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| 2to3           | 253 ms                                                                 | 254 ms: 1.00x slower                                            |
| chameleon      | 6.31 ms                                                                | 6.22 ms: 1.01x faster                                           |
| docutils       | 2.50 sec                                                               | 2.52 sec: 1.01x slower                                          |
| Geometric mean | (ref)                                                                  | 1.00x slower                                                    |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230111-linux-x86_64-python-762745a124cbc297cf2f-3.12.0a4+-762745a | bm-20230111-linux-x86_64-iritkatriel-reg_base-3.12.0a4+-762745a |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| pidigits       | 192 ms                                                                 | 193 ms: 1.00x slower                                            |
| Geometric mean | (ref)                                                                  | 1.00x faster                                                    |

Benchmark hidden because not significant (2): nbody, float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230111-linux-x86_64-python-762745a124cbc297cf2f-3.12.0a4+-762745a | bm-20230111-linux-x86_64-iritkatriel-reg_base-3.12.0a4+-762745a |
|----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| regex_dna      | 211 ms                                                                 | 217 ms: 1.03x slower                                            |
| regex_effbot   | 3.60 ms                                                                | 3.76 ms: 1.04x slower                                           |
| Geometric mean | (ref)                                                                  | 1.02x slower                                                    |

Benchmark hidden because not significant (2): regex_compile, regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230111-linux-x86_64-python-762745a124cbc297cf2f-3.12.0a4+-762745a | bm-20230111-linux-x86_64-iritkatriel-reg_base-3.12.0a4+-762745a |
|----------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| unpickle_list        | 4.98 us                                                                | 4.85 us: 1.03x faster                                           |
| xml_etree_iterparse  | 109 ms                                                                 | 106 ms: 1.02x faster                                            |
| xml_etree_process    | 53.8 ms                                                                | 54.2 ms: 1.01x slower                                           |
| pickle_pure_python   | 281 us                                                                 | 284 us: 1.01x slower                                            |
| unpickle_pure_python | 200 us                                                                 | 202 us: 1.01x slower                                            |
| xml_etree_generate   | 76.8 ms                                                                | 77.5 ms: 1.01x slower                                           |
| unpickle             | 12.9 us                                                                | 13.4 us: 1.04x slower                                           |
| pickle_list          | 4.07 us                                                                | 4.25 us: 1.04x slower                                           |
| pickle_dict          | 30.4 us                                                                | 32.0 us: 1.05x slower                                           |
| pickle               | 10.1 us                                                                | 10.7 us: 1.07x slower                                           |
| Geometric mean       | (ref)                                                                  | 1.01x slower                                                    |

Benchmark hidden because not significant (3): xml_etree_parse, json_loads, json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20230111-linux-x86_64-python-762745a124cbc297cf2f-3.12.0a4+-762745a | bm-20230111-linux-x86_64-iritkatriel-reg_base-3.12.0a4+-762745a |
|------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| python_startup_no_site | 6.06 ms                                                                | 6.08 ms: 1.00x slower                                           |
| python_startup         | 8.50 ms                                                                | 8.54 ms: 1.01x slower                                           |
| Geometric mean         | (ref)                                                                  | 1.00x slower                                                    |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230111-linux-x86_64-python-762745a124cbc297cf2f-3.12.0a4+-762745a | bm-20230111-linux-x86_64-iritkatriel-reg_base-3.12.0a4+-762745a |
|-----------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| mako            | 9.78 ms                                                                | 9.75 ms: 1.00x faster                                           |
| genshi_text     | 20.2 ms                                                                | 20.5 ms: 1.01x slower                                           |
| django_template | 32.3 ms                                                                | 32.9 ms: 1.02x slower                                           |
| Geometric mean  | (ref)                                                                  | 1.01x slower                                                    |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20230111-linux-x86_64-python-762745a124cbc297cf2f-3.12.0a4+-762745a | bm-20230111-linux-x86_64-iritkatriel-reg_base-3.12.0a4+-762745a |
|-------------------------|:----------------------------------------------------------------------:|:---------------------------------------------------------------:|
| generators              | 79.3 ms                                                                | 75.4 ms: 1.05x faster                                           |
| coverage                | 98.4 ms                                                                | 95.1 ms: 1.03x faster                                           |
| unpickle_list           | 4.98 us                                                                | 4.85 us: 1.03x faster                                           |
| logging_simple          | 5.75 us                                                                | 5.62 us: 1.02x faster                                           |
| telco                   | 6.37 ms                                                                | 6.24 ms: 1.02x faster                                           |
| xml_etree_iterparse     | 109 ms                                                                 | 106 ms: 1.02x faster                                            |
| unpack_sequence         | 43.8 ns                                                                | 43.1 ns: 1.02x faster                                           |
| chameleon               | 6.31 ms                                                                | 6.22 ms: 1.01x faster                                           |
| sqlglot_parse           | 1.41 ms                                                                | 1.40 ms: 1.01x faster                                           |
| sqlglot_transpile       | 1.71 ms                                                                | 1.69 ms: 1.01x faster                                           |
| coroutines              | 24.7 ms                                                                | 24.4 ms: 1.01x faster                                           |
| sqlglot_normalize       | 105 ms                                                                 | 105 ms: 1.01x faster                                            |
| logging_format          | 6.28 us                                                                | 6.24 us: 1.01x faster                                           |
| raytrace                | 282 ms                                                                 | 281 ms: 1.01x faster                                            |
| pprint_pformat          | 1.38 sec                                                               | 1.37 sec: 1.01x faster                                          |
| async_generators        | 357 ms                                                                 | 354 ms: 1.01x faster                                            |
| pyflate                 | 393 ms                                                                 | 391 ms: 1.01x faster                                            |
| crypto_pyaes            | 75.1 ms                                                                | 74.8 ms: 1.00x faster                                           |
| sqlglot_optimize        | 51.0 ms                                                                | 50.8 ms: 1.00x faster                                           |
| mako                    | 9.78 ms                                                                | 9.75 ms: 1.00x faster                                           |
| pidigits                | 192 ms                                                                 | 193 ms: 1.00x slower                                            |
| python_startup_no_site  | 6.06 ms                                                                | 6.08 ms: 1.00x slower                                           |
| 2to3                    | 253 ms                                                                 | 254 ms: 1.00x slower                                            |
| hexiom                  | 6.07 ms                                                                | 6.09 ms: 1.00x slower                                           |
| sympy_sum               | 162 ms                                                                 | 163 ms: 1.00x slower                                            |
| create_gc_cycles        | 1.45 ms                                                                | 1.45 ms: 1.00x slower                                           |
| python_startup          | 8.50 ms                                                                | 8.54 ms: 1.01x slower                                           |
| sympy_integrate         | 20.2 ms                                                                | 20.3 ms: 1.01x slower                                           |
| docutils                | 2.50 sec                                                               | 2.52 sec: 1.01x slower                                          |
| xml_etree_process       | 53.8 ms                                                                | 54.2 ms: 1.01x slower                                           |
| thrift                  | 751 us                                                                 | 757 us: 1.01x slower                                            |
| pickle_pure_python      | 281 us                                                                 | 284 us: 1.01x slower                                            |
| pycparser               | 1.14 sec                                                               | 1.15 sec: 1.01x slower                                          |
| unpickle_pure_python    | 200 us                                                                 | 202 us: 1.01x slower                                            |
| sympy_str               | 280 ms                                                                 | 283 ms: 1.01x slower                                            |
| xml_etree_generate      | 76.8 ms                                                                | 77.5 ms: 1.01x slower                                           |
| deltablue               | 3.24 ms                                                                | 3.27 ms: 1.01x slower                                           |
| deepcopy                | 331 us                                                                 | 334 us: 1.01x slower                                            |
| chaos                   | 66.7 ms                                                                | 67.4 ms: 1.01x slower                                           |
| scimark_sor             | 106 ms                                                                 | 108 ms: 1.01x slower                                            |
| nqueens                 | 79.6 ms                                                                | 80.6 ms: 1.01x slower                                           |
| async_tree_io           | 1.31 sec                                                               | 1.33 sec: 1.01x slower                                          |
| sympy_expand            | 453 ms                                                                 | 460 ms: 1.01x slower                                            |
| genshi_text             | 20.2 ms                                                                | 20.5 ms: 1.01x slower                                           |
| dask                    | 491 ms                                                                 | 500 ms: 1.02x slower                                            |
| django_template         | 32.3 ms                                                                | 32.9 ms: 1.02x slower                                           |
| scimark_fft             | 312 ms                                                                 | 319 ms: 1.02x slower                                            |
| fannkuch                | 365 ms                                                                 | 373 ms: 1.02x slower                                            |
| scimark_lu              | 107 ms                                                                 | 110 ms: 1.02x slower                                            |
| deepcopy_reduce         | 2.88 us                                                                | 2.95 us: 1.02x slower                                           |
| mdp                     | 2.44 sec                                                               | 2.51 sec: 1.03x slower                                          |
| regex_dna               | 211 ms                                                                 | 217 ms: 1.03x slower                                            |
| scimark_sparse_mat_mult | 4.03 ms                                                                | 4.17 ms: 1.03x slower                                           |
| unpickle                | 12.9 us                                                                | 13.4 us: 1.04x slower                                           |
| regex_effbot            | 3.60 ms                                                                | 3.76 ms: 1.04x slower                                           |
| pickle_list             | 4.07 us                                                                | 4.25 us: 1.04x slower                                           |
| meteor_contest          | 103 ms                                                                 | 108 ms: 1.05x slower                                            |
| pickle_dict             | 30.4 us                                                                | 32.0 us: 1.05x slower                                           |
| gc_traversal            | 3.57 ms                                                                | 3.79 ms: 1.06x slower                                           |
| pickle                  | 10.1 us                                                                | 10.7 us: 1.07x slower                                           |
| async_tree_memoization  | 622 ms                                                                 | 670 ms: 1.08x slower                                            |
| Geometric mean          | (ref)                                                                  | 1.01x slower                                                    |

Benchmark hidden because not significant (27): logging_silent, nbody, xml_etree_parse, go, spectral_norm, sqlite_synth, regex_compile, bench_thread_pool, regex_v8, json, bench_mp_pool, deepcopy_memo, json_loads, dulwich_log, pprint_safe_repr, float, scimark_monte_carlo, json_dumps, asyncio_tcp, mypy, genshi_xml, html5lib, pathlib, async_tree_cpu_io_mixed, richards, async_tree_none, djangocms
