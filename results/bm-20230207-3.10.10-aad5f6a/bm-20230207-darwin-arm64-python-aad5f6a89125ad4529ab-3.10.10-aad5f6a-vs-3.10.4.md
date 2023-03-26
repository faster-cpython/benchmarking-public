
# Results vs. 3.10.4

- fork: python
- ref: aad5f6a89125ad4529ab
- machine: darwin-arm64
- commit hash: aad5f6a
- commit date: 2023-02-07
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-darwin-arm64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| 2to3           | 201 ms                                                 | 203 ms: 1.01x slower                                                 |
| docutils       | 1.78 sec                                               | 1.79 sec: 1.01x slower                                               |
| html5lib       | 44.2 ms                                                | 47.8 ms: 1.08x slower                                                |
| Geometric mean | (ref)                                                  | 1.02x slower                                                         |

Benchmark hidden because not significant (2): chameleon, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-darwin-arm64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| pidigits       | 282 ms                                                 | 282 ms: 1.00x faster                                                 |
| nbody          | 93.3 ms                                                | 94.1 ms: 1.01x slower                                                |
| Geometric mean | (ref)                                                  | 1.00x slower                                                         |

Benchmark hidden because not significant (1): float

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-darwin-arm64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| regex_compile  | 96.4 ms                                                | 96.9 ms: 1.01x slower                                                |
| regex_v8       | 17.6 ms                                                | 18.2 ms: 1.04x slower                                                |
| regex_effbot   | 2.46 ms                                                | 2.75 ms: 1.12x slower                                                |
| regex_dna      | 162 ms                                                 | 187 ms: 1.16x slower                                                 |
| Geometric mean | (ref)                                                  | 1.08x slower                                                         |

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-darwin-arm64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|---------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| json_dumps          | 8.40 ms                                                | 8.29 ms: 1.01x faster                                                |
| xml_etree_process   | 44.8 ms                                                | 45.0 ms: 1.01x slower                                                |
| xml_etree_parse     | 106 ms                                                 | 107 ms: 1.01x slower                                                 |
| xml_etree_iterparse | 72.3 ms                                                | 73.1 ms: 1.01x slower                                                |
| pickle_pure_python  | 283 us                                                 | 287 us: 1.01x slower                                                 |
| xml_etree_generate  | 54.2 ms                                                | 55.0 ms: 1.02x slower                                                |
| pickle              | 7.35 us                                                | 7.54 us: 1.03x slower                                                |
| pickle_list         | 2.80 us                                                | 2.93 us: 1.04x slower                                                |
| pickle_dict         | 17.9 us                                                | 18.7 us: 1.05x slower                                                |
| Geometric mean      | (ref)                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (4): unpickle, unpickle_list, json_loads, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-darwin-arm64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| python_startup         | 11.9 ms                                                | 12.7 ms: 1.07x slower                                                |
| python_startup_no_site | 8.88 ms                                                | 9.82 ms: 1.11x slower                                                |
| Geometric mean         | (ref)                                                  | 1.09x slower                                                         |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-darwin-arm64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| genshi_text     | 18.4 ms                                                | 18.2 ms: 1.01x faster                                                |
| django_template | 27.3 ms                                                | 27.2 ms: 1.00x faster                                                |
| genshi_xml      | 37.2 ms                                                | 37.3 ms: 1.00x slower                                                |
| mako            | 10.5 ms                                                | 10.5 ms: 1.00x slower                                                |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                         |

All benchmarks:
===============

| Benchmark               | bm-20220323-darwin-arm64-python-v3.10.4-3.10.4-9d38120 | bm-20230207-darwin-arm64-python-aad5f6a89125ad4529ab-3.10.10-aad5f6a |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------:|
| sqlglot_parse           | 1.37 ms                                                | 1.33 ms: 1.03x faster                                                |
| bench_thread_pool       | 546 us                                                 | 534 us: 1.02x faster                                                 |
| richards                | 51.4 ms                                                | 50.2 ms: 1.02x faster                                                |
| sqlglot_transpile       | 1.57 ms                                                | 1.54 ms: 1.02x faster                                                |
| json_dumps              | 8.40 ms                                                | 8.29 ms: 1.01x faster                                                |
| logging_silent          | 119 ns                                                 | 118 ns: 1.01x faster                                                 |
| genshi_text             | 18.4 ms                                                | 18.2 ms: 1.01x faster                                                |
| deepcopy_reduce         | 2.37 us                                                | 2.35 us: 1.01x faster                                                |
| pprint_safe_repr        | 606 ms                                                 | 600 ms: 1.01x faster                                                 |
| coverage                | 42.0 ms                                                | 41.8 ms: 1.01x faster                                                |
| meteor_contest          | 78.1 ms                                                | 77.6 ms: 1.01x faster                                                |
| go                      | 165 ms                                                 | 165 ms: 1.00x faster                                                 |
| sqlite_synth            | 1.47 us                                                | 1.47 us: 1.00x faster                                                |
| django_template         | 27.3 ms                                                | 27.2 ms: 1.00x faster                                                |
| fannkuch                | 317 ms                                                 | 317 ms: 1.00x faster                                                 |
| pidigits                | 282 ms                                                 | 282 ms: 1.00x faster                                                 |
| crypto_pyaes            | 78.1 ms                                                | 78.0 ms: 1.00x faster                                                |
| gc_traversal            | 2.39 ms                                                | 2.40 ms: 1.00x slower                                                |
| pyflate                 | 453 ms                                                 | 455 ms: 1.00x slower                                                 |
| dulwich_log             | 37.1 ms                                                | 37.2 ms: 1.00x slower                                                |
| genshi_xml              | 37.2 ms                                                | 37.3 ms: 1.00x slower                                                |
| mako                    | 10.5 ms                                                | 10.5 ms: 1.00x slower                                                |
| mdp                     | 1.66 sec                                               | 1.67 sec: 1.01x slower                                               |
| xml_etree_process       | 44.8 ms                                                | 45.0 ms: 1.01x slower                                                |
| docutils                | 1.78 sec                                               | 1.79 sec: 1.01x slower                                               |
| spectral_norm           | 95.8 ms                                                | 96.3 ms: 1.01x slower                                                |
| regex_compile           | 96.4 ms                                                | 96.9 ms: 1.01x slower                                                |
| scimark_lu              | 109 ms                                                 | 110 ms: 1.01x slower                                                 |
| chaos                   | 66.7 ms                                                | 67.1 ms: 1.01x slower                                                |
| scimark_fft             | 230 ms                                                 | 232 ms: 1.01x slower                                                 |
| telco                   | 3.63 ms                                                | 3.65 ms: 1.01x slower                                                |
| xml_etree_parse         | 106 ms                                                 | 107 ms: 1.01x slower                                                 |
| scimark_sparse_mat_mult | 3.46 ms                                                | 3.48 ms: 1.01x slower                                                |
| deltablue               | 5.14 ms                                                | 5.18 ms: 1.01x slower                                                |
| comprehensions          | 17.6 us                                                | 17.7 us: 1.01x slower                                                |
| nbody                   | 93.3 ms                                                | 94.1 ms: 1.01x slower                                                |
| 2to3                    | 201 ms                                                 | 203 ms: 1.01x slower                                                 |
| logging_format          | 4.97 us                                                | 5.01 us: 1.01x slower                                                |
| sympy_expand            | 275 ms                                                 | 278 ms: 1.01x slower                                                 |
| thrift                  | 580 us                                                 | 586 us: 1.01x slower                                                 |
| sympy_str               | 169 ms                                                 | 171 ms: 1.01x slower                                                 |
| sympy_integrate         | 13.3 ms                                                | 13.4 ms: 1.01x slower                                                |
| xml_etree_iterparse     | 72.3 ms                                                | 73.1 ms: 1.01x slower                                                |
| pickle_pure_python      | 283 us                                                 | 287 us: 1.01x slower                                                 |
| raytrace                | 325 ms                                                 | 330 ms: 1.02x slower                                                 |
| xml_etree_generate      | 54.2 ms                                                | 55.0 ms: 1.02x slower                                                |
| unpack_sequence         | 37.4 ns                                                | 38.3 ns: 1.02x slower                                                |
| sqlalchemy_imperative   | 8.89 ms                                                | 9.10 ms: 1.02x slower                                                |
| pickle                  | 7.35 us                                                | 7.54 us: 1.03x slower                                                |
| bench_mp_pool           | 39.7 ms                                                | 40.9 ms: 1.03x slower                                                |
| sympy_sum               | 93.6 ms                                                | 96.8 ms: 1.03x slower                                                |
| regex_v8                | 17.6 ms                                                | 18.2 ms: 1.04x slower                                                |
| pickle_list             | 2.80 us                                                | 2.93 us: 1.04x slower                                                |
| pickle_dict             | 17.9 us                                                | 18.7 us: 1.05x slower                                                |
| python_startup          | 11.9 ms                                                | 12.7 ms: 1.07x slower                                                |
| html5lib                | 44.2 ms                                                | 47.8 ms: 1.08x slower                                                |
| python_startup_no_site  | 8.88 ms                                                | 9.82 ms: 1.11x slower                                                |
| regex_effbot            | 2.46 ms                                                | 2.75 ms: 1.12x slower                                                |
| regex_dna               | 162 ms                                                 | 187 ms: 1.16x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.01x slower                                                         |

Benchmark hidden because not significant (36): gunicorn, aiohttp, async_tree_memoization, pycparser, async_tree_cpu_io_mixed, pathlib, chameleon, flaskblogging, async_tree_io, unpickle, logging_simple, deepcopy, pprint_pformat, unpickle_list, create_gc_cycles, deepcopy_memo, sqlalchemy_declarative, nqueens, generators, float, dask, pylint, sqlglot_normalize, json_loads, async_tree_none, coroutines, hexiom, json, async_generators, sqlglot_optimize, unpickle_pure_python, scimark_sor, mypy2, scimark_monte_carlo, asyncio_tcp, tornado_http
