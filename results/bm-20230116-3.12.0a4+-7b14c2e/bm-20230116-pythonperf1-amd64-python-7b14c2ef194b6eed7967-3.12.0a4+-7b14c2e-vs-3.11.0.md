
# Results vs. 3.11.0

- fork: python
- ref: 7b14c2ef194b6eed7967
- machine: windows-amd64
- commit hash: 7b14c2e
- commit date: 2023-01-16
- overall geometric mean: 1.10x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230116-pythonperf1-amd64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 200 ms: 1.05x faster                                                        |
| chameleon      | 5.11 ms                                                     | 4.49 ms: 1.14x faster                                                       |
| docutils       | 1.60 sec                                                    | 1.53 sec: 1.05x faster                                                      |
| html5lib       | 37.5 ms                                                     | 33.0 ms: 1.14x faster                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230116-pythonperf1-amd64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 58.5 ms: 1.20x faster                                                       |
| float          | 54.6 ms                                                     | 47.9 ms: 1.14x faster                                                       |
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230116-pythonperf1-amd64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 78.3 ms: 1.16x faster                                                       |
| regex_v8       | 13.8 ms                                                     | 13.8 ms: 1.00x faster                                                       |
| regex_dna      | 115 ms                                                      | 124 ms: 1.07x slower                                                        |
| regex_effbot   | 1.50 ms                                                     | 1.61 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                       | 1.00x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230116-pythonperf1-amd64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.24 ms: 1.44x faster                                                       |
| unpickle_pure_python | 152 us                                                      | 119 us: 1.28x faster                                                        |
| pickle_pure_python   | 200 us                                                      | 173 us: 1.16x faster                                                        |
| xml_etree_process    | 37.1 ms                                                     | 33.9 ms: 1.09x faster                                                       |
| xml_etree_parse      | 95.9 ms                                                     | 89.1 ms: 1.08x faster                                                       |
| xml_etree_generate   | 52.2 ms                                                     | 50.0 ms: 1.04x faster                                                       |
| xml_etree_iterparse  | 62.6 ms                                                     | 63.5 ms: 1.01x slower                                                       |
| pickle_list          | 2.68 us                                                     | 2.74 us: 1.02x slower                                                       |
| pickle_dict          | 18.5 us                                                     | 19.0 us: 1.03x slower                                                       |
| pickle               | 6.61 us                                                     | 6.84 us: 1.04x slower                                                       |
| unpickle_list        | 2.55 us                                                     | 2.71 us: 1.06x slower                                                       |
| json_loads           | 12.9 us                                                     | 14.0 us: 1.08x slower                                                       |
| unpickle             | 8.09 us                                                     | 8.82 us: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230116-pythonperf1-amd64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 17.0 ms                                                     | 13.9 ms: 1.22x faster                                                       |
| genshi_xml      | 37.3 ms                                                     | 31.0 ms: 1.20x faster                                                       |
| mako            | 7.26 ms                                                     | 6.12 ms: 1.19x faster                                                       |
| django_template | 24.1 ms                                                     | 20.4 ms: 1.18x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.20x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230116-pythonperf1-amd64-python-7b14c2ef194b6eed7967-3.12.0a4+-7b14c2e |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpack_sequence         | 46.1 ns                                                     | 26.4 ns: 1.74x faster                                                       |
| asyncio_tcp             | 699 ms                                                      | 475 ms: 1.47x faster                                                        |
| json_dumps              | 7.56 ms                                                     | 5.24 ms: 1.44x faster                                                       |
| deltablue               | 2.61 ms                                                     | 1.93 ms: 1.35x faster                                                       |
| unpickle_pure_python    | 152 us                                                      | 119 us: 1.28x faster                                                        |
| deepcopy_memo           | 25.2 us                                                     | 19.7 us: 1.28x faster                                                       |
| logging_silent          | 69.8 ns                                                     | 54.9 ns: 1.27x faster                                                       |
| richards                | 30.6 ms                                                     | 24.1 ms: 1.27x faster                                                       |
| raytrace                | 211 ms                                                      | 168 ms: 1.25x faster                                                        |
| hexiom                  | 4.55 ms                                                     | 3.67 ms: 1.24x faster                                                       |
| scimark_sor             | 75.6 ms                                                     | 61.1 ms: 1.24x faster                                                       |
| genshi_text             | 17.0 ms                                                     | 13.9 ms: 1.22x faster                                                       |
| deepcopy                | 246 us                                                      | 201 us: 1.22x faster                                                        |
| genshi_xml              | 37.3 ms                                                     | 31.0 ms: 1.20x faster                                                       |
| go                      | 97.3 ms                                                     | 81.1 ms: 1.20x faster                                                       |
| nbody                   | 70.0 ms                                                     | 58.5 ms: 1.20x faster                                                       |
| scimark_monte_carlo     | 44.6 ms                                                     | 37.3 ms: 1.20x faster                                                       |
| json                    | 3.25 ms                                                     | 2.74 ms: 1.19x faster                                                       |
| mako                    | 7.26 ms                                                     | 6.12 ms: 1.19x faster                                                       |
| django_template         | 24.1 ms                                                     | 20.4 ms: 1.18x faster                                                       |
| fannkuch                | 252 ms                                                      | 214 ms: 1.18x faster                                                        |
| nqueens                 | 64.9 ms                                                     | 55.3 ms: 1.17x faster                                                       |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.21 ms: 1.16x faster                                                       |
| pickle_pure_python      | 200 us                                                      | 173 us: 1.16x faster                                                        |
| regex_compile           | 90.6 ms                                                     | 78.3 ms: 1.16x faster                                                       |
| deepcopy_reduce         | 2.07 us                                                     | 1.80 us: 1.15x faster                                                       |
| pyflate                 | 304 ms                                                      | 265 ms: 1.15x faster                                                        |
| spectral_norm           | 67.9 ms                                                     | 59.2 ms: 1.15x faster                                                       |
| sqlglot_normalize       | 190 ms                                                      | 167 ms: 1.14x faster                                                        |
| float                   | 54.6 ms                                                     | 47.9 ms: 1.14x faster                                                       |
| logging_simple          | 6.61 us                                                     | 5.80 us: 1.14x faster                                                       |
| chameleon               | 5.11 ms                                                     | 4.49 ms: 1.14x faster                                                       |
| scimark_lu              | 63.5 ms                                                     | 55.8 ms: 1.14x faster                                                       |
| html5lib                | 37.5 ms                                                     | 33.0 ms: 1.14x faster                                                       |
| pprint_safe_repr        | 512 ms                                                      | 450 ms: 1.14x faster                                                        |
| chaos                   | 47.1 ms                                                     | 41.8 ms: 1.13x faster                                                       |
| pprint_pformat          | 1.04 sec                                                    | 933 ms: 1.11x faster                                                        |
| sqlglot_parse           | 952 us                                                      | 858 us: 1.11x faster                                                        |
| scimark_fft             | 178 ms                                                      | 161 ms: 1.11x faster                                                        |
| sqlglot_optimize        | 34.9 ms                                                     | 31.5 ms: 1.11x faster                                                       |
| sqlglot_transpile       | 1.16 ms                                                     | 1.06 ms: 1.10x faster                                                       |
| xml_etree_process       | 37.1 ms                                                     | 33.9 ms: 1.09x faster                                                       |
| mdp                     | 1.67 sec                                                    | 1.53 sec: 1.09x faster                                                      |
| pycparser               | 691 ms                                                      | 634 ms: 1.09x faster                                                        |
| logging_format          | 7.01 us                                                     | 6.44 us: 1.09x faster                                                       |
| sympy_expand            | 295 ms                                                      | 273 ms: 1.08x faster                                                        |
| meteor_contest          | 74.7 ms                                                     | 69.2 ms: 1.08x faster                                                       |
| xml_etree_parse         | 95.9 ms                                                     | 89.1 ms: 1.08x faster                                                       |
| dulwich_log             | 44.5 ms                                                     | 41.9 ms: 1.06x faster                                                       |
| sympy_str               | 182 ms                                                      | 172 ms: 1.06x faster                                                        |
| mypy2                   | 229 ms                                                      | 216 ms: 1.06x faster                                                        |
| async_tree_cpu_io_mixed | 501 ms                                                      | 474 ms: 1.06x faster                                                        |
| async_tree_memoization  | 371 ms                                                      | 351 ms: 1.06x faster                                                        |
| sympy_integrate         | 13.8 ms                                                     | 13.1 ms: 1.06x faster                                                       |
| comprehensions          | 15.9 us                                                     | 15.1 us: 1.05x faster                                                       |
| coverage                | 55.9 ms                                                     | 53.1 ms: 1.05x faster                                                       |
| sympy_sum               | 99.9 ms                                                     | 95.0 ms: 1.05x faster                                                       |
| docutils                | 1.60 sec                                                    | 1.53 sec: 1.05x faster                                                      |
| 2to3                    | 209 ms                                                      | 200 ms: 1.05x faster                                                        |
| xml_etree_generate      | 52.2 ms                                                     | 50.0 ms: 1.04x faster                                                       |
| async_tree_none         | 320 ms                                                      | 307 ms: 1.04x faster                                                        |
| telco                   | 3.90 ms                                                     | 3.75 ms: 1.04x faster                                                       |
| thrift                  | 491 us                                                      | 474 us: 1.03x faster                                                        |
| crypto_pyaes            | 47.6 ms                                                     | 46.0 ms: 1.03x faster                                                       |
| create_gc_cycles        | 693 us                                                      | 670 us: 1.03x faster                                                        |
| dask                    | 264 ms                                                      | 256 ms: 1.03x faster                                                        |
| async_generators        | 178 ms                                                      | 173 ms: 1.02x faster                                                        |
| gc_traversal            | 1.46 ms                                                     | 1.43 ms: 1.02x faster                                                       |
| bench_thread_pool       | 852 us                                                      | 839 us: 1.02x faster                                                        |
| async_tree_io           | 779 ms                                                      | 768 ms: 1.01x faster                                                        |
| regex_v8                | 13.8 ms                                                     | 13.8 ms: 1.00x faster                                                       |
| bench_mp_pool           | 62.5 ms                                                     | 63.1 ms: 1.01x slower                                                       |
| generators              | 33.8 ms                                                     | 34.2 ms: 1.01x slower                                                       |
| xml_etree_iterparse     | 62.6 ms                                                     | 63.5 ms: 1.01x slower                                                       |
| pidigits                | 148 ms                                                      | 151 ms: 1.02x slower                                                        |
| pickle_list             | 2.68 us                                                     | 2.74 us: 1.02x slower                                                       |
| pickle_dict             | 18.5 us                                                     | 19.0 us: 1.03x slower                                                       |
| pickle                  | 6.61 us                                                     | 6.84 us: 1.04x slower                                                       |
| sqlite_synth            | 1.68 us                                                     | 1.76 us: 1.05x slower                                                       |
| pathlib                 | 71.4 ms                                                     | 74.9 ms: 1.05x slower                                                       |
| unpickle_list           | 2.55 us                                                     | 2.71 us: 1.06x slower                                                       |
| regex_dna               | 115 ms                                                      | 124 ms: 1.07x slower                                                        |
| regex_effbot            | 1.50 ms                                                     | 1.61 ms: 1.07x slower                                                       |
| json_loads              | 12.9 us                                                     | 14.0 us: 1.08x slower                                                       |
| unpickle                | 8.09 us                                                     | 8.82 us: 1.09x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.10x faster                                                                |

Benchmark hidden because not significant (4): python_startup_no_site, tornado_http, python_startup, coroutines
Ignored benchmarks (9) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x
