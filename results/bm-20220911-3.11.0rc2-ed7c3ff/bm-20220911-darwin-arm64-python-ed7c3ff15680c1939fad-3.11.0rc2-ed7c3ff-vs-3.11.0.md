
# Results vs. 3.11.0

- fork: python
- ref: ed7c3ff15680c1939fad
- machine: darwin-arm64
- commit hash: ed7c3ff
- commit date: 2022-09-11
- overall geometric mean: 1.00x faster

Benchmarks with tag 'apps':
===========================

Benchmark hidden because not significant (5): 2to3, chameleon, docutils, html5lib, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220911-darwin-arm64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float          | 53.0 ms                                                | 51.9 ms: 1.02x faster                                                  |
| pidigits       | 281 ms                                                 | 281 ms: 1.00x slower                                                   |
| Geometric mean | (ref)                                                  | 1.01x faster                                                           |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220911-darwin-arm64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 16.2 ms                                                | 16.1 ms: 1.01x faster                                                  |
| regex_compile  | 76.7 ms                                                | 76.5 ms: 1.00x faster                                                  |
| regex_dna      | 152 ms                                                 | 151 ms: 1.00x faster                                                   |
| Geometric mean | (ref)                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (1): regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220911-darwin-arm64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| xml_etree_generate   | 48.8 ms                                                | 48.4 ms: 1.01x faster                                                  |
| xml_etree_parse      | 106 ms                                                 | 105 ms: 1.01x faster                                                   |
| json_dumps           | 7.72 ms                                                | 7.66 ms: 1.01x faster                                                  |
| xml_etree_iterparse  | 69.2 ms                                                | 68.7 ms: 1.01x faster                                                  |
| xml_etree_process    | 35.2 ms                                                | 35.0 ms: 1.01x faster                                                  |
| unpickle_pure_python | 159 us                                                 | 158 us: 1.00x faster                                                   |
| pickle_list          | 2.81 us                                                | 2.82 us: 1.00x slower                                                  |
| unpickle_list        | 2.63 us                                                | 2.65 us: 1.01x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (5): unpickle, pickle_dict, pickle_pure_python, json_loads, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220911-darwin-arm64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                | 12.3 ms: 1.07x slower                                                  |
| python_startup_no_site | 9.31 ms                                                | 10.0 ms: 1.08x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220911-darwin-arm64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| django_template | 21.0 ms                                                | 21.0 ms: 1.00x faster                                                  |
| mako            | 8.49 ms                                                | 8.51 ms: 1.00x slower                                                  |
| genshi_text     | 15.3 ms                                                | 15.3 ms: 1.00x slower                                                  |
| genshi_xml      | 29.8 ms                                                | 29.9 ms: 1.00x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.00x slower                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220911-darwin-arm64-python-ed7c3ff15680c1939fad-3.11.0rc2-ed7c3ff |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| float                   | 53.0 ms                                                | 51.9 ms: 1.02x faster                                                  |
| generators              | 28.8 ms                                                | 28.5 ms: 1.01x faster                                                  |
| xml_etree_generate      | 48.8 ms                                                | 48.4 ms: 1.01x faster                                                  |
| gc_traversal            | 2.43 ms                                                | 2.41 ms: 1.01x faster                                                  |
| xml_etree_parse         | 106 ms                                                 | 105 ms: 1.01x faster                                                   |
| json_dumps              | 7.72 ms                                                | 7.66 ms: 1.01x faster                                                  |
| regex_v8                | 16.2 ms                                                | 16.1 ms: 1.01x faster                                                  |
| xml_etree_iterparse     | 69.2 ms                                                | 68.7 ms: 1.01x faster                                                  |
| sqlalchemy_imperative   | 7.31 ms                                                | 7.27 ms: 1.01x faster                                                  |
| xml_etree_process       | 35.2 ms                                                | 35.0 ms: 1.01x faster                                                  |
| thrift                  | 433 us                                                 | 432 us: 1.00x faster                                                   |
| create_gc_cycles        | 726 us                                                 | 724 us: 1.00x faster                                                   |
| logging_simple          | 3.50 us                                                | 3.49 us: 1.00x faster                                                  |
| spectral_norm           | 72.8 ms                                                | 72.5 ms: 1.00x faster                                                  |
| pprint_safe_repr        | 465 ms                                                 | 463 ms: 1.00x faster                                                   |
| sqlite_synth            | 1.27 us                                                | 1.27 us: 1.00x faster                                                  |
| logging_format          | 3.78 us                                                | 3.77 us: 1.00x faster                                                  |
| regex_compile           | 76.7 ms                                                | 76.5 ms: 1.00x faster                                                  |
| sympy_expand            | 243 ms                                                 | 242 ms: 1.00x faster                                                   |
| unpickle_pure_python    | 159 us                                                 | 158 us: 1.00x faster                                                   |
| django_template         | 21.0 ms                                                | 21.0 ms: 1.00x faster                                                  |
| dulwich_log             | 29.9 ms                                                | 29.8 ms: 1.00x faster                                                  |
| pyflate                 | 311 ms                                                 | 310 ms: 1.00x faster                                                   |
| pprint_pformat          | 950 ms                                                 | 948 ms: 1.00x faster                                                   |
| regex_dna               | 152 ms                                                 | 151 ms: 1.00x faster                                                   |
| pidigits                | 281 ms                                                 | 281 ms: 1.00x slower                                                   |
| scimark_sparse_mat_mult | 3.20 ms                                                | 3.20 ms: 1.00x slower                                                  |
| coroutines              | 17.7 ms                                                | 17.7 ms: 1.00x slower                                                  |
| mako                    | 8.49 ms                                                | 8.51 ms: 1.00x slower                                                  |
| hexiom                  | 4.73 ms                                                | 4.74 ms: 1.00x slower                                                  |
| deepcopy                | 224 us                                                 | 224 us: 1.00x slower                                                   |
| bench_thread_pool       | 473 us                                                 | 474 us: 1.00x slower                                                   |
| fannkuch                | 261 ms                                                 | 262 ms: 1.00x slower                                                   |
| raytrace                | 207 ms                                                 | 208 ms: 1.00x slower                                                   |
| genshi_text             | 15.3 ms                                                | 15.3 ms: 1.00x slower                                                  |
| genshi_xml              | 29.8 ms                                                | 29.9 ms: 1.00x slower                                                  |
| async_generators        | 195 ms                                                 | 196 ms: 1.00x slower                                                   |
| pickle_list             | 2.81 us                                                | 2.82 us: 1.00x slower                                                  |
| go                      | 109 ms                                                 | 109 ms: 1.01x slower                                                   |
| json                    | 2.77 ms                                                | 2.79 ms: 1.01x slower                                                  |
| unpickle_list           | 2.63 us                                                | 2.65 us: 1.01x slower                                                  |
| python_startup          | 11.5 ms                                                | 12.3 ms: 1.07x slower                                                  |
| python_startup_no_site  | 9.31 ms                                                | 10.0 ms: 1.08x slower                                                  |
| Geometric mean          | (ref)                                                  | 1.00x faster                                                           |

Benchmark hidden because not significant (51): async_tree_memoization, tornado_http, aiohttp, pathlib, unpickle, gunicorn, asyncio_tcp, pycparser, sympy_sum, logging_silent, nqueens, sympy_str, deepcopy_reduce, dask, scimark_sor, pickle_dict, telco, sqlglot_parse, crypto_pyaes, mypy2, chameleon, chaos, docutils, flaskblogging, regex_effbot, richards, sqlglot_normalize, comprehensions, sqlglot_optimize, meteor_contest, pickle_pure_python, scimark_lu, pylint, unpack_sequence, mdp, scimark_fft, nbody, json_loads, sqlglot_transpile, 2to3, scimark_monte_carlo, async_tree_cpu_io_mixed, html5lib, deltablue, pickle, sqlalchemy_declarative, sympy_integrate, deepcopy_memo, async_tree_io, async_tree_none, bench_mp_pool
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: coverage
