
# Results vs. 3.11.0

- fork: python
- ref: f533f216e6aaba3f3663
- machine: windows-amd64
- commit hash: f533f21
- commit date: 2023-03-06
- overall geometric mean: 1.06x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230306-pythonperf1-amd64-python-f533f216e6aaba3f3663-3.12.0a5+-f533f21 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 203 ms: 1.03x faster                                                        |
| chameleon      | 5.11 ms                                                     | 4.82 ms: 1.06x faster                                                       |
| docutils       | 1.60 sec                                                    | 1.56 sec: 1.03x faster                                                      |
| html5lib       | 37.5 ms                                                     | 36.7 ms: 1.02x faster                                                       |
| tornado_http   | 91.8 ms                                                     | 90.7 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230306-pythonperf1-amd64-python-f533f216e6aaba3f3663-3.12.0a5+-f533f21 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 54.6 ms                                                     | 50.4 ms: 1.08x faster                                                       |
| nbody          | 70.0 ms                                                     | 64.6 ms: 1.08x faster                                                       |
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230306-pythonperf1-amd64-python-f533f216e6aaba3f3663-3.12.0a5+-f533f21 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 82.1 ms: 1.10x faster                                                       |
| regex_v8       | 13.8 ms                                                     | 14.3 ms: 1.03x slower                                                       |
| regex_dna      | 115 ms                                                      | 123 ms: 1.07x slower                                                        |
| regex_effbot   | 1.50 ms                                                     | 1.65 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230306-pythonperf1-amd64-python-f533f216e6aaba3f3663-3.12.0a5+-f533f21 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.40 ms: 1.40x faster                                                       |
| unpickle_pure_python | 152 us                                                      | 126 us: 1.20x faster                                                        |
| pickle_pure_python   | 200 us                                                      | 176 us: 1.14x faster                                                        |
| xml_etree_parse      | 95.9 ms                                                     | 92.0 ms: 1.04x faster                                                       |
| json_loads           | 12.9 us                                                     | 12.7 us: 1.01x faster                                                       |
| xml_etree_process    | 37.1 ms                                                     | 37.7 ms: 1.02x slower                                                       |
| xml_etree_generate   | 52.2 ms                                                     | 53.9 ms: 1.03x slower                                                       |
| pickle_list          | 2.68 us                                                     | 2.80 us: 1.05x slower                                                       |
| pickle               | 6.61 us                                                     | 6.91 us: 1.05x slower                                                       |
| unpickle_list        | 2.55 us                                                     | 2.74 us: 1.08x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                                |

Benchmark hidden because not significant (3): unpickle, xml_etree_iterparse, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230306-pythonperf1-amd64-python-f533f216e6aaba3f3663-3.12.0a5+-f533f21 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 18.7 ms                                                     | 18.9 ms: 1.01x slower                                                       |
| python_startup_no_site | 15.9 ms                                                     | 16.0 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.01x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230306-pythonperf1-amd64-python-f533f216e6aaba3f3663-3.12.0a5+-f533f21 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 17.0 ms                                                     | 14.2 ms: 1.20x faster                                                       |
| genshi_xml      | 37.3 ms                                                     | 32.1 ms: 1.16x faster                                                       |
| mako            | 7.26 ms                                                     | 6.36 ms: 1.14x faster                                                       |
| django_template | 24.1 ms                                                     | 21.9 ms: 1.10x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.15x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230306-pythonperf1-amd64-python-f533f216e6aaba3f3663-3.12.0a5+-f533f21 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpack_sequence         | 46.1 ns                                                     | 28.6 ns: 1.61x faster                                                       |
| generators              | 33.8 ms                                                     | 21.8 ms: 1.55x faster                                                       |
| asyncio_tcp             | 699 ms                                                      | 476 ms: 1.47x faster                                                        |
| json_dumps              | 7.56 ms                                                     | 5.40 ms: 1.40x faster                                                       |
| deltablue               | 2.61 ms                                                     | 1.99 ms: 1.31x faster                                                       |
| logging_silent          | 69.8 ns                                                     | 56.1 ns: 1.24x faster                                                       |
| richards                | 30.6 ms                                                     | 25.4 ms: 1.20x faster                                                       |
| unpickle_pure_python    | 152 us                                                      | 126 us: 1.20x faster                                                        |
| genshi_text             | 17.0 ms                                                     | 14.2 ms: 1.20x faster                                                       |
| genshi_xml              | 37.3 ms                                                     | 32.1 ms: 1.16x faster                                                       |
| json                    | 3.25 ms                                                     | 2.80 ms: 1.16x faster                                                       |
| mako                    | 7.26 ms                                                     | 6.36 ms: 1.14x faster                                                       |
| raytrace                | 211 ms                                                      | 185 ms: 1.14x faster                                                        |
| fannkuch                | 252 ms                                                      | 221 ms: 1.14x faster                                                        |
| coverage                | 55.9 ms                                                     | 49.1 ms: 1.14x faster                                                       |
| pickle_pure_python      | 200 us                                                      | 176 us: 1.14x faster                                                        |
| hexiom                  | 4.55 ms                                                     | 4.02 ms: 1.13x faster                                                       |
| deepcopy                | 246 us                                                      | 218 us: 1.13x faster                                                        |
| deepcopy_memo           | 25.2 us                                                     | 22.4 us: 1.12x faster                                                       |
| mdp                     | 1.67 sec                                                    | 1.49 sec: 1.12x faster                                                      |
| pyflate                 | 304 ms                                                      | 272 ms: 1.12x faster                                                        |
| go                      | 97.3 ms                                                     | 87.4 ms: 1.11x faster                                                       |
| nqueens                 | 64.9 ms                                                     | 58.5 ms: 1.11x faster                                                       |
| chaos                   | 47.1 ms                                                     | 42.5 ms: 1.11x faster                                                       |
| regex_compile           | 90.6 ms                                                     | 82.1 ms: 1.10x faster                                                       |
| django_template         | 24.1 ms                                                     | 21.9 ms: 1.10x faster                                                       |
| sqlglot_normalize       | 190 ms                                                      | 173 ms: 1.10x faster                                                        |
| pprint_pformat          | 1.04 sec                                                    | 951 ms: 1.09x faster                                                        |
| float                   | 54.6 ms                                                     | 50.4 ms: 1.08x faster                                                       |
| deepcopy_reduce         | 2.07 us                                                     | 1.91 us: 1.08x faster                                                       |
| nbody                   | 70.0 ms                                                     | 64.6 ms: 1.08x faster                                                       |
| dulwich_log             | 44.5 ms                                                     | 41.2 ms: 1.08x faster                                                       |
| logging_simple          | 6.61 us                                                     | 6.13 us: 1.08x faster                                                       |
| sqlglot_optimize        | 34.9 ms                                                     | 32.5 ms: 1.07x faster                                                       |
| logging_format          | 7.01 us                                                     | 6.55 us: 1.07x faster                                                       |
| scimark_lu              | 63.5 ms                                                     | 59.5 ms: 1.07x faster                                                       |
| sympy_expand            | 295 ms                                                      | 277 ms: 1.07x faster                                                        |
| chameleon               | 5.11 ms                                                     | 4.82 ms: 1.06x faster                                                       |
| pprint_safe_repr        | 512 ms                                                      | 483 ms: 1.06x faster                                                        |
| mypy2                   | 229 ms                                                      | 216 ms: 1.06x faster                                                        |
| scimark_monte_carlo     | 44.6 ms                                                     | 42.3 ms: 1.06x faster                                                       |
| sqlglot_transpile       | 1.16 ms                                                     | 1.10 ms: 1.06x faster                                                       |
| scimark_sor             | 75.6 ms                                                     | 71.7 ms: 1.05x faster                                                       |
| sympy_integrate         | 13.8 ms                                                     | 13.1 ms: 1.05x faster                                                       |
| crypto_pyaes            | 47.6 ms                                                     | 45.3 ms: 1.05x faster                                                       |
| sqlglot_parse           | 952 us                                                      | 908 us: 1.05x faster                                                        |
| async_tree_none         | 320 ms                                                      | 306 ms: 1.05x faster                                                        |
| xml_etree_parse         | 95.9 ms                                                     | 92.0 ms: 1.04x faster                                                       |
| comprehensions          | 15.9 us                                                     | 15.4 us: 1.03x faster                                                       |
| meteor_contest          | 74.7 ms                                                     | 72.4 ms: 1.03x faster                                                       |
| coroutines              | 14.6 ms                                                     | 14.2 ms: 1.03x faster                                                       |
| sympy_str               | 182 ms                                                      | 177 ms: 1.03x faster                                                        |
| 2to3                    | 209 ms                                                      | 203 ms: 1.03x faster                                                        |
| docutils                | 1.60 sec                                                    | 1.56 sec: 1.03x faster                                                      |
| thrift                  | 491 us                                                      | 478 us: 1.03x faster                                                        |
| telco                   | 3.90 ms                                                     | 3.81 ms: 1.02x faster                                                       |
| html5lib                | 37.5 ms                                                     | 36.7 ms: 1.02x faster                                                       |
| async_tree_cpu_io_mixed | 501 ms                                                      | 493 ms: 1.02x faster                                                        |
| json_loads              | 12.9 us                                                     | 12.7 us: 1.01x faster                                                       |
| tornado_http            | 91.8 ms                                                     | 90.7 ms: 1.01x faster                                                       |
| spectral_norm           | 67.9 ms                                                     | 67.4 ms: 1.01x faster                                                       |
| python_startup          | 18.7 ms                                                     | 18.9 ms: 1.01x slower                                                       |
| python_startup_no_site  | 15.9 ms                                                     | 16.0 ms: 1.01x slower                                                       |
| pidigits                | 148 ms                                                      | 150 ms: 1.01x slower                                                        |
| create_gc_cycles        | 693 us                                                      | 701 us: 1.01x slower                                                        |
| xml_etree_process       | 37.1 ms                                                     | 37.7 ms: 1.02x slower                                                       |
| scimark_fft             | 178 ms                                                      | 182 ms: 1.02x slower                                                        |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.64 ms: 1.03x slower                                                       |
| regex_v8                | 13.8 ms                                                     | 14.3 ms: 1.03x slower                                                       |
| xml_etree_generate      | 52.2 ms                                                     | 53.9 ms: 1.03x slower                                                       |
| gc_traversal            | 1.46 ms                                                     | 1.51 ms: 1.04x slower                                                       |
| pickle_list             | 2.68 us                                                     | 2.80 us: 1.05x slower                                                       |
| pickle                  | 6.61 us                                                     | 6.91 us: 1.05x slower                                                       |
| pathlib                 | 71.4 ms                                                     | 75.0 ms: 1.05x slower                                                       |
| bench_mp_pool           | 62.5 ms                                                     | 65.7 ms: 1.05x slower                                                       |
| regex_dna               | 115 ms                                                      | 123 ms: 1.07x slower                                                        |
| unpickle_list           | 2.55 us                                                     | 2.74 us: 1.08x slower                                                       |
| sqlite_synth            | 1.68 us                                                     | 1.82 us: 1.08x slower                                                       |
| regex_effbot            | 1.50 ms                                                     | 1.65 ms: 1.10x slower                                                       |
| async_generators        | 178 ms                                                      | 224 ms: 1.26x slower                                                        |
| dask                    | 264 ms                                                      | 356 ms: 1.35x slower                                                        |
| Geometric mean          | (ref)                                                       | 1.06x faster                                                                |

Benchmark hidden because not significant (8): pycparser, unpickle, xml_etree_iterparse, async_tree_io, bench_thread_pool, sympy_sum, async_tree_memoization, pickle_dict
Ignored benchmarks (9) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
