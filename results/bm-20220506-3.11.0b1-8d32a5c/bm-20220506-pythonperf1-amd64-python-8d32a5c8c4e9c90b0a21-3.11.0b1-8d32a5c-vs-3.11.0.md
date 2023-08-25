
# Results vs. 3.11.0

- fork: python
- ref: 8d32a5c8c4e9c90b0a21
- machine: windows-amd64
- commit hash: 8d32a5c
- commit date: 2022-05-06
- overall geometric mean: 1.01x slower \*
- HPT reliability: 77.38%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-pythonperf1-amd64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 203 ms: 1.03x faster                                                       |
| chameleon      | 5.11 ms                                                     | 5.45 ms: 1.07x slower                                                      |
| docutils       | 1.60 sec                                                    | 1.57 sec: 1.02x faster                                                     |
| html5lib       | 37.5 ms                                                     | 38.3 ms: 1.02x slower                                                      |
| tornado_http   | 91.8 ms                                                     | 89.7 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                       | 1.00x slower                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-pythonperf1-amd64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 67.9 ms: 1.03x faster                                                      |
| float          | 54.6 ms                                                     | 53.5 ms: 1.02x faster                                                      |
| pidigits       | 148 ms                                                      | 147 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-pythonperf1-amd64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 1.50 ms                                                     | 1.47 ms: 1.02x faster                                                      |
| regex_v8       | 13.8 ms                                                     | 13.9 ms: 1.01x slower                                                      |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark           | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-pythonperf1-amd64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|---------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| pickle_dict         | 18.5 us                                                     | 17.1 us: 1.08x faster                                                      |
| xml_etree_parse     | 95.9 ms                                                     | 93.1 ms: 1.03x faster                                                      |
| unpickle            | 8.09 us                                                     | 7.87 us: 1.03x faster                                                      |
| xml_etree_iterparse | 62.6 ms                                                     | 61.1 ms: 1.02x faster                                                      |
| unpickle_list       | 2.55 us                                                     | 2.58 us: 1.01x slower                                                      |
| xml_etree_process   | 37.1 ms                                                     | 37.6 ms: 1.01x slower                                                      |
| xml_etree_generate  | 52.2 ms                                                     | 53.0 ms: 1.01x slower                                                      |
| pickle_pure_python  | 200 us                                                      | 204 us: 1.02x slower                                                       |
| json_dumps          | 7.56 ms                                                     | 7.72 ms: 1.02x slower                                                      |
| json_loads          | 12.9 us                                                     | 13.4 us: 1.04x slower                                                      |
| Geometric mean      | (ref)                                                       | 1.00x faster                                                               |

Benchmark hidden because not significant (3): pickle, pickle_list, unpickle_pure_python

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-pythonperf1-amd64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 15.2 ms: 1.04x faster                                                      |
| python_startup         | 18.7 ms                                                     | 18.4 ms: 1.02x faster                                                      |
| Geometric mean         | (ref)                                                       | 1.03x faster                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-pythonperf1-amd64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| mako           | 7.26 ms                                                     | 7.13 ms: 1.02x faster                                                      |
| genshi_text    | 17.0 ms                                                     | 17.7 ms: 1.04x slower                                                      |
| genshi_xml     | 37.3 ms                                                     | 39.8 ms: 1.07x slower                                                      |
| Geometric mean | (ref)                                                       | 1.02x slower                                                               |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20220506-pythonperf1-amd64-python-8d32a5c8c4e9c90b0a21-3.11.0b1-8d32a5c |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------:|
| logging_simple          | 6.61 us                                                     | 5.80 us: 1.14x faster                                                      |
| logging_format          | 7.01 us                                                     | 6.25 us: 1.12x faster                                                      |
| unpack_sequence         | 46.1 ns                                                     | 42.2 ns: 1.09x faster                                                      |
| pickle_dict             | 18.5 us                                                     | 17.1 us: 1.08x faster                                                      |
| aiohttp                 | 899 us                                                      | 854 us: 1.05x faster                                                       |
| dulwich_log             | 44.5 ms                                                     | 42.5 ms: 1.05x faster                                                      |
| create_gc_cycles        | 693 us                                                      | 663 us: 1.05x faster                                                       |
| python_startup_no_site  | 15.9 ms                                                     | 15.2 ms: 1.04x faster                                                      |
| pylint                  | 326 ms                                                      | 314 ms: 1.04x faster                                                       |
| async_tree_io           | 779 ms                                                      | 751 ms: 1.04x faster                                                       |
| raytrace                | 211 ms                                                      | 203 ms: 1.04x faster                                                       |
| bench_mp_pool           | 62.5 ms                                                     | 60.6 ms: 1.03x faster                                                      |
| sympy_sum               | 99.9 ms                                                     | 96.9 ms: 1.03x faster                                                      |
| nbody                   | 70.0 ms                                                     | 67.9 ms: 1.03x faster                                                      |
| xml_etree_parse         | 95.9 ms                                                     | 93.1 ms: 1.03x faster                                                      |
| async_tree_none         | 320 ms                                                      | 311 ms: 1.03x faster                                                       |
| gc_traversal            | 1.46 ms                                                     | 1.42 ms: 1.03x faster                                                      |
| unpickle                | 8.09 us                                                     | 7.87 us: 1.03x faster                                                      |
| 2to3                    | 209 ms                                                      | 203 ms: 1.03x faster                                                       |
| tornado_http            | 91.8 ms                                                     | 89.7 ms: 1.02x faster                                                      |
| xml_etree_iterparse     | 62.6 ms                                                     | 61.1 ms: 1.02x faster                                                      |
| float                   | 54.6 ms                                                     | 53.5 ms: 1.02x faster                                                      |
| mdp                     | 1.67 sec                                                    | 1.63 sec: 1.02x faster                                                     |
| docutils                | 1.60 sec                                                    | 1.57 sec: 1.02x faster                                                     |
| mako                    | 7.26 ms                                                     | 7.13 ms: 1.02x faster                                                      |
| regex_effbot            | 1.50 ms                                                     | 1.47 ms: 1.02x faster                                                      |
| python_startup          | 18.7 ms                                                     | 18.4 ms: 1.02x faster                                                      |
| richards                | 30.6 ms                                                     | 30.1 ms: 1.02x faster                                                      |
| sympy_integrate         | 13.8 ms                                                     | 13.6 ms: 1.01x faster                                                      |
| scimark_lu              | 63.5 ms                                                     | 62.7 ms: 1.01x faster                                                      |
| pidigits                | 148 ms                                                      | 147 ms: 1.01x faster                                                       |
| sympy_expand            | 295 ms                                                      | 293 ms: 1.01x faster                                                       |
| flaskblogging           | 2.04 sec                                                    | 2.05 sec: 1.00x slower                                                     |
| logging_silent          | 69.8 ns                                                     | 70.2 ns: 1.00x slower                                                      |
| go                      | 97.3 ms                                                     | 97.9 ms: 1.01x slower                                                      |
| regex_v8                | 13.8 ms                                                     | 13.9 ms: 1.01x slower                                                      |
| hexiom                  | 4.55 ms                                                     | 4.59 ms: 1.01x slower                                                      |
| scimark_fft             | 178 ms                                                      | 180 ms: 1.01x slower                                                       |
| scimark_monte_carlo     | 44.6 ms                                                     | 45.0 ms: 1.01x slower                                                      |
| telco                   | 3.90 ms                                                     | 3.94 ms: 1.01x slower                                                      |
| meteor_contest          | 74.7 ms                                                     | 75.5 ms: 1.01x slower                                                      |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.60 ms: 1.01x slower                                                      |
| unpickle_list           | 2.55 us                                                     | 2.58 us: 1.01x slower                                                      |
| xml_etree_process       | 37.1 ms                                                     | 37.6 ms: 1.01x slower                                                      |
| xml_etree_generate      | 52.2 ms                                                     | 53.0 ms: 1.01x slower                                                      |
| dask                    | 264 ms                                                      | 268 ms: 1.02x slower                                                       |
| pickle_pure_python      | 200 us                                                      | 204 us: 1.02x slower                                                       |
| deltablue               | 2.61 ms                                                     | 2.66 ms: 1.02x slower                                                      |
| html5lib                | 37.5 ms                                                     | 38.3 ms: 1.02x slower                                                      |
| sqlglot_optimize        | 34.9 ms                                                     | 35.6 ms: 1.02x slower                                                      |
| scimark_sor             | 75.6 ms                                                     | 77.1 ms: 1.02x slower                                                      |
| deepcopy_reduce         | 2.07 us                                                     | 2.12 us: 1.02x slower                                                      |
| json_dumps              | 7.56 ms                                                     | 7.72 ms: 1.02x slower                                                      |
| spectral_norm           | 67.9 ms                                                     | 69.6 ms: 1.02x slower                                                      |
| pprint_safe_repr        | 512 ms                                                      | 525 ms: 1.03x slower                                                       |
| deepcopy                | 246 us                                                      | 252 us: 1.03x slower                                                       |
| thrift                  | 491 us                                                      | 504 us: 1.03x slower                                                       |
| sqlglot_normalize       | 190 ms                                                      | 196 ms: 1.03x slower                                                       |
| async_generators        | 178 ms                                                      | 182 ms: 1.03x slower                                                       |
| crypto_pyaes            | 47.6 ms                                                     | 49.1 ms: 1.03x slower                                                      |
| coroutines              | 14.6 ms                                                     | 15.2 ms: 1.04x slower                                                      |
| chaos                   | 47.1 ms                                                     | 48.9 ms: 1.04x slower                                                      |
| pprint_pformat          | 1.04 sec                                                    | 1.08 sec: 1.04x slower                                                     |
| json_loads              | 12.9 us                                                     | 13.4 us: 1.04x slower                                                      |
| nqueens                 | 64.9 ms                                                     | 67.6 ms: 1.04x slower                                                      |
| genshi_text             | 17.0 ms                                                     | 17.7 ms: 1.04x slower                                                      |
| bench_thread_pool       | 852 us                                                      | 888 us: 1.04x slower                                                       |
| regex_dna               | 115 ms                                                      | 121 ms: 1.05x slower                                                       |
| chameleon               | 5.11 ms                                                     | 5.45 ms: 1.07x slower                                                      |
| genshi_xml              | 37.3 ms                                                     | 39.8 ms: 1.07x slower                                                      |
| pycparser               | 691 ms                                                      | 748 ms: 1.08x slower                                                       |
| comprehensions          | 15.9 us                                                     | 17.8 us: 1.12x slower                                                      |
| sqlglot_transpile       | 1.16 ms                                                     | 1.37 ms: 1.17x slower                                                      |
| mypy2                   | 229 ms                                                      | 277 ms: 1.21x slower                                                       |
| sqlglot_parse           | 952 us                                                      | 1.15 ms: 1.21x slower                                                      |
| coverage                | 55.9 ms                                                     | 103 ms: 1.84x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.01x slower                                                               |

Benchmark hidden because not significant (16): asyncio_tcp, django_template, async_tree_cpu_io_mixed, pickle, async_tree_memoization, deepcopy_memo, pyflate, pickle_list, regex_compile, json, pathlib, fannkuch, generators, sqlite_synth, unpickle_pure_python, sympy_str
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 77.38% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
