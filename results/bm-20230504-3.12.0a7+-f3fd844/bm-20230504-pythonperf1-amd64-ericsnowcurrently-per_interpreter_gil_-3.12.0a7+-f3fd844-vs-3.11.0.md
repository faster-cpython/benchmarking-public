
# Results vs. 3.11.0

- fork: ericsnowcurrently
- ref: per_interpreter_gil_
- machine: windows-amd64
- commit hash: f3fd844
- commit date: 2023-05-04
- overall geometric mean: 1.04x faster \*
- HPT reliability: 99.99%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 208 ms: 1.01x faster                                                                   |
| tornado_http   | 91.8 ms                                                     | 89.0 ms: 1.03x faster                                                                  |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                           |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| float          | 54.6 ms                                                     | 52.1 ms: 1.05x faster                                                                  |
| nbody          | 70.0 ms                                                     | 68.6 ms: 1.02x faster                                                                  |
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                                                   |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 85.1 ms: 1.07x faster                                                                  |
| regex_dna      | 115 ms                                                      | 116 ms: 1.01x slower                                                                   |
| regex_v8       | 13.8 ms                                                     | 14.1 ms: 1.02x slower                                                                  |
| regex_effbot   | 1.50 ms                                                     | 1.58 ms: 1.05x slower                                                                  |
| Geometric mean | (ref)                                                       | 1.00x slower                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.60 ms: 1.35x faster                                                                  |
| unpickle_pure_python | 152 us                                                      | 136 us: 1.12x faster                                                                   |
| xml_etree_parse      | 95.9 ms                                                     | 91.3 ms: 1.05x faster                                                                  |
| pickle_pure_python   | 200 us                                                      | 191 us: 1.04x faster                                                                   |
| pickle_dict          | 18.5 us                                                     | 18.1 us: 1.03x faster                                                                  |
| xml_etree_iterparse  | 62.6 ms                                                     | 61.1 ms: 1.02x faster                                                                  |
| pickle_list          | 2.68 us                                                     | 2.76 us: 1.03x slower                                                                  |
| unpickle             | 8.09 us                                                     | 8.46 us: 1.05x slower                                                                  |
| xml_etree_generate   | 52.2 ms                                                     | 54.6 ms: 1.05x slower                                                                  |
| pickle               | 6.61 us                                                     | 6.95 us: 1.05x slower                                                                  |
| json_loads           | 12.9 us                                                     | 14.1 us: 1.10x slower                                                                  |
| unpickle_list        | 2.55 us                                                     | 2.82 us: 1.11x slower                                                                  |
| Geometric mean       | (ref)                                                       | 1.01x faster                                                                           |

Benchmark hidden because not significant (1): xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup | 18.7 ms                                                     | 18.8 ms: 1.01x slower                                                                  |
| Geometric mean | (ref)                                                       | 1.00x slower                                                                           |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|-----------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| mako      | 7.26 ms                                                     | 6.60 ms: 1.10x faster                                                                  |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230504-pythonperf1-amd64-ericsnowcurrently-per_interpreter_gil_-3.12.0a7+-f3fd844 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| generators              | 33.8 ms                                                     | 20.7 ms: 1.63x faster                                                                  |
| asyncio_tcp             | 699 ms                                                      | 456 ms: 1.53x faster                                                                   |
| json_dumps              | 7.56 ms                                                     | 5.60 ms: 1.35x faster                                                                  |
| deltablue               | 2.61 ms                                                     | 2.05 ms: 1.27x faster                                                                  |
| sqlglot_parse           | 952 us                                                      | 791 us: 1.20x faster                                                                   |
| logging_silent          | 69.8 ns                                                     | 58.1 ns: 1.20x faster                                                                  |
| richards                | 30.6 ms                                                     | 25.7 ms: 1.19x faster                                                                  |
| mdp                     | 1.67 sec                                                    | 1.42 sec: 1.18x faster                                                                 |
| sqlglot_transpile       | 1.16 ms                                                     | 999 us: 1.16x faster                                                                   |
| hexiom                  | 4.55 ms                                                     | 3.99 ms: 1.14x faster                                                                  |
| raytrace                | 211 ms                                                      | 185 ms: 1.14x faster                                                                   |
| scimark_lu              | 63.5 ms                                                     | 56.8 ms: 1.12x faster                                                                  |
| unpickle_pure_python    | 152 us                                                      | 136 us: 1.12x faster                                                                   |
| async_tree_none         | 320 ms                                                      | 289 ms: 1.11x faster                                                                   |
| go                      | 97.3 ms                                                     | 87.9 ms: 1.11x faster                                                                  |
| json                    | 3.25 ms                                                     | 2.96 ms: 1.10x faster                                                                  |
| mako                    | 7.26 ms                                                     | 6.60 ms: 1.10x faster                                                                  |
| unpack_sequence         | 46.1 ns                                                     | 42.2 ns: 1.09x faster                                                                  |
| async_tree_memoization  | 371 ms                                                      | 341 ms: 1.09x faster                                                                   |
| nqueens                 | 64.9 ms                                                     | 59.9 ms: 1.08x faster                                                                  |
| async_tree_cpu_io_mixed | 501 ms                                                      | 464 ms: 1.08x faster                                                                   |
| async_tree_io           | 779 ms                                                      | 727 ms: 1.07x faster                                                                   |
| mypy2                   | 229 ms                                                      | 214 ms: 1.07x faster                                                                   |
| coverage                | 55.9 ms                                                     | 52.3 ms: 1.07x faster                                                                  |
| regex_compile           | 90.6 ms                                                     | 85.1 ms: 1.07x faster                                                                  |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.42 ms: 1.06x faster                                                                  |
| spectral_norm           | 67.9 ms                                                     | 64.3 ms: 1.06x faster                                                                  |
| deepcopy_memo           | 25.2 us                                                     | 23.9 us: 1.05x faster                                                                  |
| chaos                   | 47.1 ms                                                     | 44.8 ms: 1.05x faster                                                                  |
| pyflate                 | 304 ms                                                      | 289 ms: 1.05x faster                                                                   |
| xml_etree_parse         | 95.9 ms                                                     | 91.3 ms: 1.05x faster                                                                  |
| float                   | 54.6 ms                                                     | 52.1 ms: 1.05x faster                                                                  |
| deepcopy                | 246 us                                                      | 234 us: 1.05x faster                                                                   |
| coroutines              | 14.6 ms                                                     | 14.0 ms: 1.05x faster                                                                  |
| pickle_pure_python      | 200 us                                                      | 191 us: 1.04x faster                                                                   |
| pycparser               | 691 ms                                                      | 666 ms: 1.04x faster                                                                   |
| fannkuch                | 252 ms                                                      | 244 ms: 1.03x faster                                                                   |
| dulwich_log             | 44.5 ms                                                     | 43.1 ms: 1.03x faster                                                                  |
| tornado_http            | 91.8 ms                                                     | 89.0 ms: 1.03x faster                                                                  |
| scimark_monte_carlo     | 44.6 ms                                                     | 43.3 ms: 1.03x faster                                                                  |
| sqlglot_normalize       | 190 ms                                                      | 185 ms: 1.03x faster                                                                   |
| sqlglot_optimize        | 34.9 ms                                                     | 34.0 ms: 1.03x faster                                                                  |
| pickle_dict             | 18.5 us                                                     | 18.1 us: 1.03x faster                                                                  |
| create_gc_cycles        | 693 us                                                      | 676 us: 1.03x faster                                                                   |
| xml_etree_iterparse     | 62.6 ms                                                     | 61.1 ms: 1.02x faster                                                                  |
| gc_traversal            | 1.46 ms                                                     | 1.43 ms: 1.02x faster                                                                  |
| scimark_fft             | 178 ms                                                      | 174 ms: 1.02x faster                                                                   |
| nbody                   | 70.0 ms                                                     | 68.6 ms: 1.02x faster                                                                  |
| logging_simple          | 6.61 us                                                     | 6.51 us: 1.02x faster                                                                  |
| bench_thread_pool       | 852 us                                                      | 843 us: 1.01x faster                                                                   |
| 2to3                    | 209 ms                                                      | 208 ms: 1.01x faster                                                                   |
| python_startup          | 18.7 ms                                                     | 18.8 ms: 1.01x slower                                                                  |
| regex_dna               | 115 ms                                                      | 116 ms: 1.01x slower                                                                   |
| pidigits                | 148 ms                                                      | 150 ms: 1.01x slower                                                                   |
| sqlite_synth            | 1.68 us                                                     | 1.71 us: 1.01x slower                                                                  |
| regex_v8                | 13.8 ms                                                     | 14.1 ms: 1.02x slower                                                                  |
| pickle_list             | 2.68 us                                                     | 2.76 us: 1.03x slower                                                                  |
| scimark_sor             | 75.6 ms                                                     | 78.1 ms: 1.03x slower                                                                  |
| unpickle                | 8.09 us                                                     | 8.46 us: 1.05x slower                                                                  |
| xml_etree_generate      | 52.2 ms                                                     | 54.6 ms: 1.05x slower                                                                  |
| pickle                  | 6.61 us                                                     | 6.95 us: 1.05x slower                                                                  |
| regex_effbot            | 1.50 ms                                                     | 1.58 ms: 1.05x slower                                                                  |
| meteor_contest          | 74.7 ms                                                     | 79.0 ms: 1.06x slower                                                                  |
| telco                   | 3.90 ms                                                     | 4.14 ms: 1.06x slower                                                                  |
| bench_mp_pool           | 62.5 ms                                                     | 67.1 ms: 1.07x slower                                                                  |
| json_loads              | 12.9 us                                                     | 14.1 us: 1.10x slower                                                                  |
| unpickle_list           | 2.55 us                                                     | 2.82 us: 1.11x slower                                                                  |
| pathlib                 | 71.4 ms                                                     | 81.7 ms: 1.14x slower                                                                  |
| async_generators        | 178 ms                                                      | 228 ms: 1.29x slower                                                                   |
| dask                    | 264 ms                                                      | 366 ms: 1.38x slower                                                                   |
| Geometric mean          | (ref)                                                       | 1.04x faster                                                                           |

Benchmark hidden because not significant (9): pprint_pformat, crypto_pyaes, docutils, deepcopy_reduce, comprehensions, pprint_safe_repr, python_startup_no_site, logging_format, xml_etree_process
Ignored benchmarks (19) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, chameleon, django_template, flaskblogging, genshi_text, genshi_xml, html5lib, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sympy_expand, sympy_integrate, sympy_str, sympy_sum, thrift, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
