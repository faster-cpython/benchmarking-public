
# Results vs. 3.11.0

- fork: python
- ref: ed7c3ff15680c1939fad
- machine: darwin-arm64
- commit hash: ed7c3ff
- commit date: 2022-09-11
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220911-darwin-arm64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| chameleon      | 4.55 ms                                                             | 4.57 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                               | 1.00x faster                                                           |

Benchmark hidden because not significant (4): 2to3, docutils, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220911-darwin-arm64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 53.0 ms                                                             | 51.9 ms: 1.02x faster                                                  |
| Geometric mean | (ref)                                                               | 1.01x faster                                                           |

Benchmark hidden because not significant (2): pidigits, nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220911-darwin-arm64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_compile  | 76.6 ms                                                             | 76.5 ms: 1.00x faster                                                  |
| regex_effbot   | 2.63 ms                                                             | 2.63 ms: 1.00x slower                                                  |
| Geometric mean | (ref)                                                               | 1.00x faster                                                           |

Benchmark hidden because not significant (2): regex_v8, regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220911-darwin-arm64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|---------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_iterparse | 69.2 ms                                                             | 68.7 ms: 1.01x faster                                                  |
| pickle_pure_python  | 198 us                                                              | 199 us: 1.00x slower                                                   |
| xml_etree_generate  | 48.2 ms                                                             | 48.4 ms: 1.00x slower                                                  |
| unpickle_list       | 2.63 us                                                             | 2.65 us: 1.01x slower                                                  |
| json_dumps          | 7.59 ms                                                             | 7.66 ms: 1.01x slower                                                  |
| Geometric mean      | (ref)                                                               | 1.00x slower                                                           |

Benchmark hidden because not significant (8): xml_etree_parse, pickle_list, unpickle, unpickle_pure_python, pickle_dict, pickle, xml_etree_process, json_loads

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220911-darwin-arm64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.3 ms                                                             | 12.3 ms: 1.00x faster                                                  |
| python_startup_no_site | 10.1 ms                                                             | 10.0 ms: 1.00x faster                                                  |
| Geometric mean         | (ref)                                                               | 1.00x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220911-darwin-arm64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|-----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 21.1 ms                                                             | 21.0 ms: 1.00x faster                                                  |
| mako            | 8.42 ms                                                             | 8.51 ms: 1.01x slower                                                  |
| Geometric mean  | (ref)                                                               | 1.00x slower                                                           |

Benchmark hidden because not significant (2): genshi_xml, genshi_text

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220911-darwin-arm64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|-------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| async_tree_memoization  | 338 ms                                                              | 328 ms: 1.03x faster                                                   |
| pathlib                 | 28.3 ms                                                             | 27.6 ms: 1.03x faster                                                  |
| float                   | 53.0 ms                                                             | 51.9 ms: 1.02x faster                                                  |
| sqlite_synth            | 1.28 us                                                             | 1.27 us: 1.01x faster                                                  |
| xml_etree_iterparse     | 69.2 ms                                                             | 68.7 ms: 1.01x faster                                                  |
| python_startup          | 12.3 ms                                                             | 12.3 ms: 1.00x faster                                                  |
| django_template         | 21.1 ms                                                             | 21.0 ms: 1.00x faster                                                  |
| sympy_expand            | 243 ms                                                              | 242 ms: 1.00x faster                                                   |
| python_startup_no_site  | 10.1 ms                                                             | 10.0 ms: 1.00x faster                                                  |
| logging_silent          | 68.0 ns                                                             | 67.8 ns: 1.00x faster                                                  |
| crypto_pyaes            | 51.8 ms                                                             | 51.7 ms: 1.00x faster                                                  |
| telco                   | 3.40 ms                                                             | 3.39 ms: 1.00x faster                                                  |
| generators              | 28.6 ms                                                             | 28.5 ms: 1.00x faster                                                  |
| regex_compile           | 76.6 ms                                                             | 76.5 ms: 1.00x faster                                                  |
| comprehensions          | 16.1 us                                                             | 16.1 us: 1.00x faster                                                  |
| sqlglot_normalize       | 171 ms                                                              | 171 ms: 1.00x faster                                                   |
| scimark_fft             | 200 ms                                                              | 200 ms: 1.00x faster                                                   |
| regex_effbot            | 2.63 ms                                                             | 2.63 ms: 1.00x slower                                                  |
| unpack_sequence         | 33.5 ns                                                             | 33.6 ns: 1.00x slower                                                  |
| gc_traversal            | 2.41 ms                                                             | 2.41 ms: 1.00x slower                                                  |
| hexiom                  | 4.73 ms                                                             | 4.74 ms: 1.00x slower                                                  |
| coroutines              | 17.7 ms                                                             | 17.7 ms: 1.00x slower                                                  |
| pickle_pure_python      | 198 us                                                              | 199 us: 1.00x slower                                                   |
| pprint_pformat          | 946 ms                                                              | 948 ms: 1.00x slower                                                   |
| async_generators        | 195 ms                                                              | 196 ms: 1.00x slower                                                   |
| dulwich_log             | 29.7 ms                                                             | 29.8 ms: 1.00x slower                                                  |
| scimark_sparse_mat_mult | 3.19 ms                                                             | 3.20 ms: 1.00x slower                                                  |
| pyflate                 | 309 ms                                                              | 310 ms: 1.00x slower                                                   |
| sqlalchemy_declarative  | 62.6 ms                                                             | 62.8 ms: 1.00x slower                                                  |
| deepcopy                | 224 us                                                              | 224 us: 1.00x slower                                                   |
| go                      | 109 ms                                                              | 109 ms: 1.00x slower                                                   |
| xml_etree_generate      | 48.2 ms                                                             | 48.4 ms: 1.00x slower                                                  |
| chameleon               | 4.55 ms                                                             | 4.57 ms: 1.00x slower                                                  |
| raytrace                | 207 ms                                                              | 208 ms: 1.00x slower                                                   |
| fannkuch                | 260 ms                                                              | 262 ms: 1.01x slower                                                   |
| json                    | 2.77 ms                                                             | 2.79 ms: 1.01x slower                                                  |
| meteor_contest          | 73.3 ms                                                             | 73.8 ms: 1.01x slower                                                  |
| unpickle_list           | 2.63 us                                                             | 2.65 us: 1.01x slower                                                  |
| json_dumps              | 7.59 ms                                                             | 7.66 ms: 1.01x slower                                                  |
| mako                    | 8.42 ms                                                             | 8.51 ms: 1.01x slower                                                  |
| Geometric mean          | (ref)                                                               | 1.00x faster                                                           |

Benchmark hidden because not significant (54): nqueens, tornado_http, xml_etree_parse, aiohttp, asyncio_tcp, sympy_sum, html5lib, pickle_list, sympy_str, logging_format, scimark_lu, unpickle, scimark_monte_carlo, logging_simple, sqlglot_optimize, pycparser, richards, deltablue, docutils, mdp, unpickle_pure_python, flaskblogging, dask, sympy_integrate, 2to3, regex_v8, pylint, genshi_xml, spectral_norm, pickle_dict, thrift, pidigits, deepcopy_reduce, sqlglot_parse, mypy2, pickle, async_tree_io, nbody, sqlalchemy_imperative, genshi_text, pprint_safe_repr, regex_dna, scimark_sor, chaos, bench_thread_pool, xml_etree_process, async_tree_cpu_io_mixed, create_gc_cycles, bench_mp_pool, sqlglot_transpile, deepcopy_memo, json_loads, async_tree_none, gunicorn
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: coverage
