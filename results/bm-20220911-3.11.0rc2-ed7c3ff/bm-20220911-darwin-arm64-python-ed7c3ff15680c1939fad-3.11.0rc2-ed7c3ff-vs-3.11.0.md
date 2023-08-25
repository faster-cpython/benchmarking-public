
# Results vs. 3.11.0

- fork: python
- ref: ed7c3ff15680c1939fad
- machine: darwin-arm64
- commit hash: ed7c3ff
- commit date: 2022-09-11
- overall geometric mean: 1.00x slower \*
- HPT reliability: 79.55%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220911-darwin-arm64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| chameleon      | 4.60 ms                                                | 4.57 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220911-darwin-arm64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 53.0 ms                                                | 51.9 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (2): nbody, pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220911-darwin-arm64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_dna      | 152 ms                                                 | 151 ms: 1.00x faster                                                   |
| regex_compile  | 76.7 ms                                                | 76.5 ms: 1.00x faster                                                  |
| regex_v8       | 16.1 ms                                                | 16.1 ms: 1.00x faster                                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220911-darwin-arm64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse      | 108 ms                                                 | 105 ms: 1.03x faster                                                   |
| xml_etree_iterparse  | 70.1 ms                                                | 68.7 ms: 1.02x faster                                                  |
| pickle_pure_python   | 201 us                                                 | 199 us: 1.01x faster                                                   |
| pickle_dict          | 18.0 us                                                | 17.9 us: 1.01x faster                                                  |
| unpickle_pure_python | 159 us                                                 | 158 us: 1.01x faster                                                   |
| unpickle_list        | 2.65 us                                                | 2.65 us: 1.00x slower                                                  |
| xml_etree_generate   | 48.3 ms                                                | 48.4 ms: 1.00x slower                                                  |
| pickle_list          | 2.81 us                                                | 2.82 us: 1.00x slower                                                  |
| pickle               | 7.15 us                                                | 7.17 us: 1.00x slower                                                  |
| json_dumps           | 7.63 ms                                                | 7.66 ms: 1.00x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (3): unpickle, xml_etree_process, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220911-darwin-arm64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup_no_site | 10.2 ms                                                | 10.0 ms: 1.01x faster                                                  |
| python_startup         | 12.4 ms                                                | 12.3 ms: 1.01x faster                                                  |
| Geometric mean         | (ref)                                                  | 1.01x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220911-darwin-arm64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml     | 29.8 ms                                                | 29.9 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (3): mako, django_template, genshi_text

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220911-darwin-arm64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_parse         | 108 ms                                                 | 105 ms: 1.03x faster                                                   |
| thrift                  | 442 us                                                 | 432 us: 1.02x faster                                                   |
| xml_etree_iterparse     | 70.1 ms                                                | 68.7 ms: 1.02x faster                                                  |
| float                   | 53.0 ms                                                | 51.9 ms: 1.02x faster                                                  |
| scimark_lu              | 73.3 ms                                                | 72.1 ms: 1.02x faster                                                  |
| dulwich_log             | 30.3 ms                                                | 29.8 ms: 1.02x faster                                                  |
| unpack_sequence         | 34.1 ns                                                | 33.6 ns: 1.02x faster                                                  |
| logging_simple          | 3.55 us                                                | 3.49 us: 1.02x faster                                                  |
| python_startup_no_site  | 10.2 ms                                                | 10.0 ms: 1.01x faster                                                  |
| python_startup          | 12.4 ms                                                | 12.3 ms: 1.01x faster                                                  |
| pickle_pure_python      | 201 us                                                 | 199 us: 1.01x faster                                                   |
| generators              | 28.8 ms                                                | 28.5 ms: 1.01x faster                                                  |
| pprint_safe_repr        | 466 ms                                                 | 463 ms: 1.01x faster                                                   |
| chameleon               | 4.60 ms                                                | 4.57 ms: 1.01x faster                                                  |
| pickle_dict             | 18.0 us                                                | 17.9 us: 1.01x faster                                                  |
| unpickle_pure_python    | 159 us                                                 | 158 us: 1.01x faster                                                   |
| pprint_pformat          | 954 ms                                                 | 948 ms: 1.01x faster                                                   |
| telco                   | 3.41 ms                                                | 3.39 ms: 1.00x faster                                                  |
| logging_silent          | 68.1 ns                                                | 67.8 ns: 1.00x faster                                                  |
| logging_format          | 3.78 us                                                | 3.77 us: 1.00x faster                                                  |
| regex_dna               | 152 ms                                                 | 151 ms: 1.00x faster                                                   |
| regex_compile           | 76.7 ms                                                | 76.5 ms: 1.00x faster                                                  |
| sqlglot_parse           | 959 us                                                 | 956 us: 1.00x faster                                                   |
| comprehensions          | 16.1 us                                                | 16.1 us: 1.00x faster                                                  |
| mdp                     | 1.55 sec                                               | 1.54 sec: 1.00x faster                                                 |
| sympy_integrate         | 11.5 ms                                                | 11.5 ms: 1.00x faster                                                  |
| deltablue               | 2.81 ms                                                | 2.81 ms: 1.00x faster                                                  |
| coroutines              | 17.8 ms                                                | 17.7 ms: 1.00x faster                                                  |
| regex_v8                | 16.1 ms                                                | 16.1 ms: 1.00x faster                                                  |
| spectral_norm           | 72.6 ms                                                | 72.5 ms: 1.00x faster                                                  |
| unpickle_list           | 2.65 us                                                | 2.65 us: 1.00x slower                                                  |
| xml_etree_generate      | 48.3 ms                                                | 48.4 ms: 1.00x slower                                                  |
| sqlglot_optimize        | 31.1 ms                                                | 31.2 ms: 1.00x slower                                                  |
| sqlalchemy_declarative  | 62.6 ms                                                | 62.8 ms: 1.00x slower                                                  |
| sympy_sum               | 85.5 ms                                                | 85.8 ms: 1.00x slower                                                  |
| pickle_list             | 2.81 us                                                | 2.82 us: 1.00x slower                                                  |
| genshi_xml              | 29.8 ms                                                | 29.9 ms: 1.00x slower                                                  |
| pickle                  | 7.15 us                                                | 7.17 us: 1.00x slower                                                  |
| scimark_sparse_mat_mult | 3.19 ms                                                | 3.20 ms: 1.00x slower                                                  |
| raytrace                | 207 ms                                                 | 208 ms: 1.00x slower                                                   |
| meteor_contest          | 73.5 ms                                                | 73.8 ms: 1.00x slower                                                  |
| async_tree_io           | 704 ms                                                 | 707 ms: 1.00x slower                                                   |
| scimark_sor             | 82.6 ms                                                | 82.9 ms: 1.00x slower                                                  |
| hexiom                  | 4.72 ms                                                | 4.74 ms: 1.00x slower                                                  |
| json_dumps              | 7.63 ms                                                | 7.66 ms: 1.00x slower                                                  |
| json                    | 2.78 ms                                                | 2.79 ms: 1.00x slower                                                  |
| deepcopy                | 223 us                                                 | 224 us: 1.01x slower                                                   |
| go                      | 109 ms                                                 | 109 ms: 1.01x slower                                                   |
| sqlalchemy_imperative   | 7.20 ms                                                | 7.27 ms: 1.01x slower                                                  |
| create_gc_cycles        | 716 us                                                 | 724 us: 1.01x slower                                                   |
| nqueens                 | 59.8 ms                                                | 61.7 ms: 1.03x slower                                                  |
| mypy2                   | 195 ms                                                 | 249 ms: 1.28x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.00x slower                                                           |

Benchmark hidden because not significant (41): async_tree_memoization, tornado_http, pycparser, pylint, flaskblogging, async_generators, asyncio_tcp, unpickle, mako, bench_mp_pool, sqlglot_transpile, sqlite_synth, django_template, aiohttp, richards, nbody, deepcopy_reduce, docutils, 2to3, xml_etree_process, json_loads, crypto_pyaes, gc_traversal, bench_thread_pool, scimark_monte_carlo, scimark_fft, pidigits, chaos, regex_effbot, html5lib, sympy_str, pyflate, async_tree_none, deepcopy_memo, sqlglot_normalize, fannkuch, sympy_expand, async_tree_cpu_io_mixed, genshi_text, pathlib, gunicorn
Ignored benchmarks (5) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, coverage, richards_super, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20220911-3.11.0rc2-ed7c3ff/bm-20220911-darwin-arm64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff.json: dask


# HPT report

- Reliability score: 79.55% likely to be faster
- 90% likely to have a speedup of 1.00x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
