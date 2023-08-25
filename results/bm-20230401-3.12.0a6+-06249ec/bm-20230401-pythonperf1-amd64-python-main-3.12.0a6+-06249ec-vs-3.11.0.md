
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: 06249ec
- commit date: 2023-04-01
- overall geometric mean: 1.07x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230401-pythonperf1-amd64-python-main-3.12.0a6+-06249ec |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 208 ms: 1.01x faster                                        |
| chameleon      | 5.11 ms                                                     | 4.75 ms: 1.08x faster                                       |
| docutils       | 1.60 sec                                                    | 1.55 sec: 1.04x faster                                      |
| html5lib       | 37.5 ms                                                     | 36.4 ms: 1.03x faster                                       |
| tornado_http   | 91.8 ms                                                     | 88.0 ms: 1.04x faster                                       |
| Geometric mean | (ref)                                                       | 1.04x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230401-pythonperf1-amd64-python-main-3.12.0a6+-06249ec |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 61.6 ms: 1.14x faster                                       |
| float          | 54.6 ms                                                     | 50.0 ms: 1.09x faster                                       |
| pidigits       | 148 ms                                                      | 146 ms: 1.01x faster                                        |
| Geometric mean | (ref)                                                       | 1.08x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230401-pythonperf1-amd64-python-main-3.12.0a6+-06249ec |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 84.0 ms: 1.08x faster                                       |
| regex_v8       | 13.8 ms                                                     | 13.2 ms: 1.05x faster                                       |
| regex_effbot   | 1.50 ms                                                     | 1.52 ms: 1.02x slower                                       |
| regex_dna      | 115 ms                                                      | 118 ms: 1.03x slower                                        |
| Geometric mean | (ref)                                                       | 1.02x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230401-pythonperf1-amd64-python-main-3.12.0a6+-06249ec |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.27 ms: 1.44x faster                                       |
| unpickle_pure_python | 152 us                                                      | 126 us: 1.20x faster                                        |
| pickle_pure_python   | 200 us                                                      | 185 us: 1.08x faster                                        |
| xml_etree_parse      | 95.9 ms                                                     | 91.4 ms: 1.05x faster                                       |
| xml_etree_process    | 37.1 ms                                                     | 35.9 ms: 1.03x faster                                       |
| xml_etree_iterparse  | 62.6 ms                                                     | 61.3 ms: 1.02x faster                                       |
| unpickle             | 8.09 us                                                     | 8.01 us: 1.01x faster                                       |
| xml_etree_generate   | 52.2 ms                                                     | 52.7 ms: 1.01x slower                                       |
| pickle_dict          | 18.5 us                                                     | 19.1 us: 1.03x slower                                       |
| json_loads           | 12.9 us                                                     | 13.7 us: 1.06x slower                                       |
| pickle               | 6.61 us                                                     | 7.08 us: 1.07x slower                                       |
| pickle_list          | 2.68 us                                                     | 2.89 us: 1.08x slower                                       |
| unpickle_list        | 2.55 us                                                     | 2.82 us: 1.11x slower                                       |
| Geometric mean       | (ref)                                                       | 1.03x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230401-pythonperf1-amd64-python-main-3.12.0a6+-06249ec |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 15.7 ms: 1.01x faster                                       |
| python_startup         | 18.7 ms                                                     | 18.9 ms: 1.01x slower                                       |
| Geometric mean         | (ref)                                                       | 1.00x slower                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230401-pythonperf1-amd64-python-main-3.12.0a6+-06249ec |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| genshi_xml      | 37.3 ms                                                     | 30.7 ms: 1.22x faster                                       |
| genshi_text     | 17.0 ms                                                     | 14.0 ms: 1.22x faster                                       |
| mako            | 7.26 ms                                                     | 6.19 ms: 1.17x faster                                       |
| django_template | 24.1 ms                                                     | 21.4 ms: 1.13x faster                                       |
| Geometric mean  | (ref)                                                       | 1.18x faster                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230401-pythonperf1-amd64-python-main-3.12.0a6+-06249ec |
|-------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| unpack_sequence         | 46.1 ns                                                     | 28.1 ns: 1.64x faster                                       |
| generators              | 33.8 ms                                                     | 21.2 ms: 1.60x faster                                       |
| json_dumps              | 7.56 ms                                                     | 5.27 ms: 1.44x faster                                       |
| asyncio_tcp             | 699 ms                                                      | 495 ms: 1.41x faster                                        |
| deltablue               | 2.61 ms                                                     | 1.95 ms: 1.34x faster                                       |
| logging_silent          | 69.8 ns                                                     | 54.3 ns: 1.29x faster                                       |
| genshi_xml              | 37.3 ms                                                     | 30.7 ms: 1.22x faster                                       |
| genshi_text             | 17.0 ms                                                     | 14.0 ms: 1.22x faster                                       |
| raytrace                | 211 ms                                                      | 174 ms: 1.21x faster                                        |
| scimark_lu              | 63.5 ms                                                     | 52.6 ms: 1.21x faster                                       |
| unpickle_pure_python    | 152 us                                                      | 126 us: 1.20x faster                                        |
| richards                | 30.6 ms                                                     | 25.5 ms: 1.20x faster                                       |
| go                      | 97.3 ms                                                     | 81.9 ms: 1.19x faster                                       |
| spectral_norm           | 67.9 ms                                                     | 57.2 ms: 1.19x faster                                       |
| json                    | 3.25 ms                                                     | 2.77 ms: 1.17x faster                                       |
| mako                    | 7.26 ms                                                     | 6.19 ms: 1.17x faster                                       |
| hexiom                  | 4.55 ms                                                     | 3.90 ms: 1.17x faster                                       |
| deepcopy_memo           | 25.2 us                                                     | 21.6 us: 1.17x faster                                       |
| mdp                     | 1.67 sec                                                    | 1.43 sec: 1.17x faster                                      |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.24 ms: 1.15x faster                                       |
| nbody                   | 70.0 ms                                                     | 61.6 ms: 1.14x faster                                       |
| chaos                   | 47.1 ms                                                     | 41.5 ms: 1.13x faster                                       |
| nqueens                 | 64.9 ms                                                     | 57.4 ms: 1.13x faster                                       |
| django_template         | 24.1 ms                                                     | 21.4 ms: 1.13x faster                                       |
| deepcopy                | 246 us                                                      | 218 us: 1.13x faster                                        |
| scimark_monte_carlo     | 44.6 ms                                                     | 39.9 ms: 1.12x faster                                       |
| sqlglot_normalize       | 190 ms                                                      | 173 ms: 1.10x faster                                        |
| sqlglot_optimize        | 34.9 ms                                                     | 31.7 ms: 1.10x faster                                       |
| sqlglot_parse           | 952 us                                                      | 869 us: 1.10x faster                                        |
| float                   | 54.6 ms                                                     | 50.0 ms: 1.09x faster                                       |
| fannkuch                | 252 ms                                                      | 232 ms: 1.09x faster                                        |
| sqlglot_transpile       | 1.16 ms                                                     | 1.07 ms: 1.08x faster                                       |
| pickle_pure_python      | 200 us                                                      | 185 us: 1.08x faster                                        |
| logging_simple          | 6.61 us                                                     | 6.11 us: 1.08x faster                                       |
| deepcopy_reduce         | 2.07 us                                                     | 1.91 us: 1.08x faster                                       |
| scimark_fft             | 178 ms                                                      | 165 ms: 1.08x faster                                        |
| regex_compile           | 90.6 ms                                                     | 84.0 ms: 1.08x faster                                       |
| chameleon               | 5.11 ms                                                     | 4.75 ms: 1.08x faster                                       |
| pprint_pformat          | 1.04 sec                                                    | 966 ms: 1.08x faster                                        |
| pprint_safe_repr        | 512 ms                                                      | 477 ms: 1.07x faster                                        |
| sympy_integrate         | 13.8 ms                                                     | 12.9 ms: 1.07x faster                                       |
| coroutines              | 14.6 ms                                                     | 13.8 ms: 1.06x faster                                       |
| sympy_expand            | 295 ms                                                      | 278 ms: 1.06x faster                                        |
| pyflate                 | 304 ms                                                      | 286 ms: 1.06x faster                                        |
| crypto_pyaes            | 47.6 ms                                                     | 44.9 ms: 1.06x faster                                       |
| coverage                | 55.9 ms                                                     | 52.8 ms: 1.06x faster                                       |
| dulwich_log             | 44.5 ms                                                     | 42.3 ms: 1.05x faster                                       |
| logging_format          | 7.01 us                                                     | 6.68 us: 1.05x faster                                       |
| xml_etree_parse         | 95.9 ms                                                     | 91.4 ms: 1.05x faster                                       |
| regex_v8                | 13.8 ms                                                     | 13.2 ms: 1.05x faster                                       |
| meteor_contest          | 74.7 ms                                                     | 71.4 ms: 1.05x faster                                       |
| comprehensions          | 15.9 us                                                     | 15.2 us: 1.05x faster                                       |
| tornado_http            | 91.8 ms                                                     | 88.0 ms: 1.04x faster                                       |
| async_tree_cpu_io_mixed | 501 ms                                                      | 480 ms: 1.04x faster                                        |
| mypy2                   | 229 ms                                                      | 220 ms: 1.04x faster                                        |
| docutils                | 1.60 sec                                                    | 1.55 sec: 1.04x faster                                      |
| html5lib                | 37.5 ms                                                     | 36.4 ms: 1.03x faster                                       |
| xml_etree_process       | 37.1 ms                                                     | 35.9 ms: 1.03x faster                                       |
| pycparser               | 691 ms                                                      | 672 ms: 1.03x faster                                        |
| sympy_str               | 182 ms                                                      | 177 ms: 1.03x faster                                        |
| xml_etree_iterparse     | 62.6 ms                                                     | 61.3 ms: 1.02x faster                                       |
| pidigits                | 148 ms                                                      | 146 ms: 1.01x faster                                        |
| python_startup_no_site  | 15.9 ms                                                     | 15.7 ms: 1.01x faster                                       |
| unpickle                | 8.09 us                                                     | 8.01 us: 1.01x faster                                       |
| thrift                  | 491 us                                                      | 487 us: 1.01x faster                                        |
| 2to3                    | 209 ms                                                      | 208 ms: 1.01x faster                                        |
| xml_etree_generate      | 52.2 ms                                                     | 52.7 ms: 1.01x slower                                       |
| python_startup          | 18.7 ms                                                     | 18.9 ms: 1.01x slower                                       |
| scimark_sor             | 75.6 ms                                                     | 76.7 ms: 1.01x slower                                       |
| regex_effbot            | 1.50 ms                                                     | 1.52 ms: 1.02x slower                                       |
| regex_dna               | 115 ms                                                      | 118 ms: 1.03x slower                                        |
| pickle_dict             | 18.5 us                                                     | 19.1 us: 1.03x slower                                       |
| gc_traversal            | 1.46 ms                                                     | 1.51 ms: 1.04x slower                                       |
| json_loads              | 12.9 us                                                     | 13.7 us: 1.06x slower                                       |
| pickle                  | 6.61 us                                                     | 7.08 us: 1.07x slower                                       |
| bench_mp_pool           | 62.5 ms                                                     | 67.0 ms: 1.07x slower                                       |
| pickle_list             | 2.68 us                                                     | 2.89 us: 1.08x slower                                       |
| unpickle_list           | 2.55 us                                                     | 2.82 us: 1.11x slower                                       |
| sqlite_synth            | 1.68 us                                                     | 1.87 us: 1.11x slower                                       |
| pathlib                 | 71.4 ms                                                     | 86.3 ms: 1.21x slower                                       |
| async_generators        | 178 ms                                                      | 215 ms: 1.21x slower                                        |
| dask                    | 264 ms                                                      | 362 ms: 1.37x slower                                        |
| Geometric mean          | (ref)                                                       | 1.07x faster                                                |

Benchmark hidden because not significant (7): bench_thread_pool, async_tree_io, async_tree_none, async_tree_memoization, sympy_sum, telco, create_gc_cycles
Ignored benchmarks (9) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x
