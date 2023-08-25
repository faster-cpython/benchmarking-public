
# Results vs. 3.11.0

- fork: python
- ref: 52bc2e7b9d451821513a
- machine: windows-amd64
- commit hash: 52bc2e7
- commit date: 2023-04-06
- overall geometric mean: 1.08x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-pythonperf1-amd64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 202 ms: 1.03x faster                                                        |
| chameleon      | 5.11 ms                                                     | 4.75 ms: 1.08x faster                                                       |
| docutils       | 1.60 sec                                                    | 1.57 sec: 1.02x faster                                                      |
| html5lib       | 37.5 ms                                                     | 36.4 ms: 1.03x faster                                                       |
| tornado_http   | 91.8 ms                                                     | 86.4 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-pythonperf1-amd64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 57.8 ms: 1.21x faster                                                       |
| float          | 54.6 ms                                                     | 48.6 ms: 1.12x faster                                                       |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-pythonperf1-amd64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 82.3 ms: 1.10x faster                                                       |
| regex_v8       | 13.8 ms                                                     | 13.8 ms: 1.01x faster                                                       |
| regex_dna      | 115 ms                                                      | 117 ms: 1.01x slower                                                        |
| regex_effbot   | 1.50 ms                                                     | 1.56 ms: 1.04x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-pythonperf1-amd64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.36 ms: 1.41x faster                                                       |
| unpickle_pure_python | 152 us                                                      | 129 us: 1.18x faster                                                        |
| pickle_pure_python   | 200 us                                                      | 176 us: 1.14x faster                                                        |
| xml_etree_parse      | 95.9 ms                                                     | 90.9 ms: 1.05x faster                                                       |
| xml_etree_iterparse  | 62.6 ms                                                     | 60.9 ms: 1.03x faster                                                       |
| json_loads           | 12.9 us                                                     | 12.8 us: 1.01x faster                                                       |
| xml_etree_generate   | 52.2 ms                                                     | 51.9 ms: 1.01x faster                                                       |
| pickle_dict          | 18.5 us                                                     | 19.1 us: 1.03x slower                                                       |
| pickle_list          | 2.68 us                                                     | 2.78 us: 1.04x slower                                                       |
| pickle               | 6.61 us                                                     | 6.97 us: 1.05x slower                                                       |
| unpickle_list        | 2.55 us                                                     | 2.77 us: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                                |

Benchmark hidden because not significant (2): xml_etree_process, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-pythonperf1-amd64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 18.7 ms                                                     | 18.9 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-pythonperf1-amd64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 17.0 ms                                                     | 13.7 ms: 1.24x faster                                                       |
| genshi_xml      | 37.3 ms                                                     | 30.8 ms: 1.21x faster                                                       |
| mako            | 7.26 ms                                                     | 6.15 ms: 1.18x faster                                                       |
| django_template | 24.1 ms                                                     | 21.7 ms: 1.11x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.18x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-pythonperf1-amd64-python-52bc2e7b9d451821513a-3.12.0a7+-52bc2e7 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpack_sequence         | 46.1 ns                                                     | 27.4 ns: 1.68x faster                                                       |
| generators              | 33.8 ms                                                     | 20.9 ms: 1.62x faster                                                       |
| asyncio_tcp             | 699 ms                                                      | 482 ms: 1.45x faster                                                        |
| json_dumps              | 7.56 ms                                                     | 5.36 ms: 1.41x faster                                                       |
| deltablue               | 2.61 ms                                                     | 1.97 ms: 1.32x faster                                                       |
| logging_silent          | 69.8 ns                                                     | 55.8 ns: 1.25x faster                                                       |
| genshi_text             | 17.0 ms                                                     | 13.7 ms: 1.24x faster                                                       |
| sqlglot_parse           | 952 us                                                      | 773 us: 1.23x faster                                                        |
| mdp                     | 1.67 sec                                                    | 1.37 sec: 1.21x faster                                                      |
| genshi_xml              | 37.3 ms                                                     | 30.8 ms: 1.21x faster                                                       |
| nbody                   | 70.0 ms                                                     | 57.8 ms: 1.21x faster                                                       |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.13 ms: 1.21x faster                                                       |
| sqlglot_transpile       | 1.16 ms                                                     | 964 us: 1.21x faster                                                        |
| richards                | 30.6 ms                                                     | 25.5 ms: 1.20x faster                                                       |
| json                    | 3.25 ms                                                     | 2.72 ms: 1.19x faster                                                       |
| raytrace                | 211 ms                                                      | 178 ms: 1.19x faster                                                        |
| hexiom                  | 4.55 ms                                                     | 3.86 ms: 1.18x faster                                                       |
| mako                    | 7.26 ms                                                     | 6.15 ms: 1.18x faster                                                       |
| scimark_lu              | 63.5 ms                                                     | 53.9 ms: 1.18x faster                                                       |
| unpickle_pure_python    | 152 us                                                      | 129 us: 1.18x faster                                                        |
| go                      | 97.3 ms                                                     | 83.9 ms: 1.16x faster                                                       |
| chaos                   | 47.1 ms                                                     | 41.2 ms: 1.14x faster                                                       |
| comprehensions          | 15.9 us                                                     | 13.9 us: 1.14x faster                                                       |
| deepcopy                | 246 us                                                      | 215 us: 1.14x faster                                                        |
| pickle_pure_python      | 200 us                                                      | 176 us: 1.14x faster                                                        |
| spectral_norm           | 67.9 ms                                                     | 59.8 ms: 1.14x faster                                                       |
| deepcopy_memo           | 25.2 us                                                     | 22.2 us: 1.13x faster                                                       |
| float                   | 54.6 ms                                                     | 48.6 ms: 1.12x faster                                                       |
| sqlglot_optimize        | 34.9 ms                                                     | 31.3 ms: 1.11x faster                                                       |
| sqlglot_normalize       | 190 ms                                                      | 171 ms: 1.11x faster                                                        |
| django_template         | 24.1 ms                                                     | 21.7 ms: 1.11x faster                                                       |
| scimark_fft             | 178 ms                                                      | 162 ms: 1.10x faster                                                        |
| regex_compile           | 90.6 ms                                                     | 82.3 ms: 1.10x faster                                                       |
| deepcopy_reduce         | 2.07 us                                                     | 1.90 us: 1.09x faster                                                       |
| scimark_monte_carlo     | 44.6 ms                                                     | 41.2 ms: 1.08x faster                                                       |
| chameleon               | 5.11 ms                                                     | 4.75 ms: 1.08x faster                                                       |
| nqueens                 | 64.9 ms                                                     | 60.3 ms: 1.08x faster                                                       |
| logging_format          | 7.01 us                                                     | 6.52 us: 1.08x faster                                                       |
| fannkuch                | 252 ms                                                      | 235 ms: 1.07x faster                                                        |
| pprint_pformat          | 1.04 sec                                                    | 969 ms: 1.07x faster                                                        |
| pprint_safe_repr        | 512 ms                                                      | 478 ms: 1.07x faster                                                        |
| pyflate                 | 304 ms                                                      | 285 ms: 1.07x faster                                                        |
| logging_simple          | 6.61 us                                                     | 6.20 us: 1.07x faster                                                       |
| tornado_http            | 91.8 ms                                                     | 86.4 ms: 1.06x faster                                                       |
| coroutines              | 14.6 ms                                                     | 13.8 ms: 1.06x faster                                                       |
| async_tree_none         | 320 ms                                                      | 302 ms: 1.06x faster                                                        |
| coverage                | 55.9 ms                                                     | 52.8 ms: 1.06x faster                                                       |
| crypto_pyaes            | 47.6 ms                                                     | 45.0 ms: 1.06x faster                                                       |
| xml_etree_parse         | 95.9 ms                                                     | 90.9 ms: 1.05x faster                                                       |
| sympy_expand            | 295 ms                                                      | 280 ms: 1.05x faster                                                        |
| pycparser               | 691 ms                                                      | 657 ms: 1.05x faster                                                        |
| mypy2                   | 229 ms                                                      | 218 ms: 1.05x faster                                                        |
| thrift                  | 491 us                                                      | 469 us: 1.05x faster                                                        |
| dulwich_log             | 44.5 ms                                                     | 42.6 ms: 1.04x faster                                                       |
| sympy_str               | 182 ms                                                      | 175 ms: 1.04x faster                                                        |
| async_tree_cpu_io_mixed | 501 ms                                                      | 482 ms: 1.04x faster                                                        |
| meteor_contest          | 74.7 ms                                                     | 72.1 ms: 1.04x faster                                                       |
| 2to3                    | 209 ms                                                      | 202 ms: 1.03x faster                                                        |
| sympy_integrate         | 13.8 ms                                                     | 13.3 ms: 1.03x faster                                                       |
| scimark_sor             | 75.6 ms                                                     | 73.1 ms: 1.03x faster                                                       |
| html5lib                | 37.5 ms                                                     | 36.4 ms: 1.03x faster                                                       |
| async_tree_memoization  | 371 ms                                                      | 361 ms: 1.03x faster                                                        |
| xml_etree_iterparse     | 62.6 ms                                                     | 60.9 ms: 1.03x faster                                                       |
| async_tree_io           | 779 ms                                                      | 762 ms: 1.02x faster                                                        |
| docutils                | 1.60 sec                                                    | 1.57 sec: 1.02x faster                                                      |
| sympy_sum               | 99.9 ms                                                     | 98.5 ms: 1.01x faster                                                       |
| json_loads              | 12.9 us                                                     | 12.8 us: 1.01x faster                                                       |
| xml_etree_generate      | 52.2 ms                                                     | 51.9 ms: 1.01x faster                                                       |
| telco                   | 3.90 ms                                                     | 3.88 ms: 1.01x faster                                                       |
| regex_v8                | 13.8 ms                                                     | 13.8 ms: 1.01x faster                                                       |
| python_startup          | 18.7 ms                                                     | 18.9 ms: 1.01x slower                                                       |
| create_gc_cycles        | 693 us                                                      | 702 us: 1.01x slower                                                        |
| regex_dna               | 115 ms                                                      | 117 ms: 1.01x slower                                                        |
| gc_traversal            | 1.46 ms                                                     | 1.49 ms: 1.02x slower                                                       |
| pickle_dict             | 18.5 us                                                     | 19.1 us: 1.03x slower                                                       |
| pickle_list             | 2.68 us                                                     | 2.78 us: 1.04x slower                                                       |
| regex_effbot            | 1.50 ms                                                     | 1.56 ms: 1.04x slower                                                       |
| pickle                  | 6.61 us                                                     | 6.97 us: 1.05x slower                                                       |
| bench_mp_pool           | 62.5 ms                                                     | 66.9 ms: 1.07x slower                                                       |
| unpickle_list           | 2.55 us                                                     | 2.77 us: 1.09x slower                                                       |
| sqlite_synth            | 1.68 us                                                     | 1.85 us: 1.10x slower                                                       |
| async_generators        | 178 ms                                                      | 213 ms: 1.20x slower                                                        |
| pathlib                 | 71.4 ms                                                     | 86.6 ms: 1.21x slower                                                       |
| dask                    | 264 ms                                                      | 358 ms: 1.36x slower                                                        |
| Geometric mean          | (ref)                                                       | 1.08x faster                                                                |

Benchmark hidden because not significant (5): bench_thread_pool, xml_etree_process, pidigits, unpickle, python_startup_no_site
Ignored benchmarks (9) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x
