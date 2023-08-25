
# Results vs. 3.11.0

- fork: python
- ref: 70be5e42f6e288de32e0
- machine: windows-amd64
- commit hash: 70be5e4
- commit date: 2022-12-11
- overall geometric mean: 1.06x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221211-pythonperf1-amd64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 201 ms: 1.04x faster                                                        |
| chameleon      | 5.11 ms                                                     | 4.68 ms: 1.09x faster                                                       |
| docutils       | 1.60 sec                                                    | 1.58 sec: 1.02x faster                                                      |
| html5lib       | 37.5 ms                                                     | 36.2 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221211-pythonperf1-amd64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 62.7 ms: 1.12x faster                                                       |
| float          | 54.6 ms                                                     | 49.7 ms: 1.10x faster                                                       |
| pidigits       | 148 ms                                                      | 147 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221211-pythonperf1-amd64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 84.9 ms: 1.07x faster                                                       |
| regex_v8       | 13.8 ms                                                     | 13.6 ms: 1.02x faster                                                       |
| regex_effbot   | 1.50 ms                                                     | 1.54 ms: 1.03x slower                                                       |
| regex_dna      | 115 ms                                                      | 120 ms: 1.04x slower                                                        |
| Geometric mean | (ref)                                                       | 1.00x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221211-pythonperf1-amd64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.41 ms: 1.40x faster                                                       |
| unpickle_pure_python | 152 us                                                      | 130 us: 1.16x faster                                                        |
| pickle_pure_python   | 200 us                                                      | 184 us: 1.09x faster                                                        |
| xml_etree_process    | 37.1 ms                                                     | 35.3 ms: 1.05x faster                                                       |
| xml_etree_parse      | 95.9 ms                                                     | 91.5 ms: 1.05x faster                                                       |
| xml_etree_generate   | 52.2 ms                                                     | 51.2 ms: 1.02x faster                                                       |
| unpickle_list        | 2.55 us                                                     | 2.60 us: 1.02x slower                                                       |
| json_loads           | 12.9 us                                                     | 13.3 us: 1.03x slower                                                       |
| pickle_dict          | 18.5 us                                                     | 19.2 us: 1.04x slower                                                       |
| pickle_list          | 2.68 us                                                     | 2.83 us: 1.05x slower                                                       |
| pickle               | 6.61 us                                                     | 7.21 us: 1.09x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                                |

Benchmark hidden because not significant (2): unpickle, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221211-pythonperf1-amd64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup | 18.7 ms                                                     | 19.0 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221211-pythonperf1-amd64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| mako            | 7.26 ms                                                     | 6.18 ms: 1.18x faster                                                       |
| genshi_text     | 17.0 ms                                                     | 14.4 ms: 1.17x faster                                                       |
| genshi_xml      | 37.3 ms                                                     | 32.6 ms: 1.14x faster                                                       |
| django_template | 24.1 ms                                                     | 22.2 ms: 1.08x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.14x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221211-pythonperf1-amd64-python-70be5e42f6e288de32e0-3.12.0a3+-70be5e4 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpack_sequence         | 46.1 ns                                                     | 29.1 ns: 1.58x faster                                                       |
| asyncio_tcp             | 699 ms                                                      | 499 ms: 1.40x faster                                                        |
| json_dumps              | 7.56 ms                                                     | 5.41 ms: 1.40x faster                                                       |
| deltablue               | 2.61 ms                                                     | 2.17 ms: 1.20x faster                                                       |
| mako                    | 7.26 ms                                                     | 6.18 ms: 1.18x faster                                                       |
| genshi_text             | 17.0 ms                                                     | 14.4 ms: 1.17x faster                                                       |
| logging_silent          | 69.8 ns                                                     | 59.5 ns: 1.17x faster                                                       |
| deepcopy_memo           | 25.2 us                                                     | 21.5 us: 1.17x faster                                                       |
| json                    | 3.25 ms                                                     | 2.78 ms: 1.17x faster                                                       |
| unpickle_pure_python    | 152 us                                                      | 130 us: 1.16x faster                                                        |
| richards                | 30.6 ms                                                     | 26.3 ms: 1.16x faster                                                       |
| deepcopy                | 246 us                                                      | 214 us: 1.15x faster                                                        |
| genshi_xml              | 37.3 ms                                                     | 32.6 ms: 1.14x faster                                                       |
| scimark_sor             | 75.6 ms                                                     | 66.7 ms: 1.13x faster                                                       |
| raytrace                | 211 ms                                                      | 189 ms: 1.12x faster                                                        |
| nbody                   | 70.0 ms                                                     | 62.7 ms: 1.12x faster                                                       |
| hexiom                  | 4.55 ms                                                     | 4.10 ms: 1.11x faster                                                       |
| deepcopy_reduce         | 2.07 us                                                     | 1.88 us: 1.10x faster                                                       |
| spectral_norm           | 67.9 ms                                                     | 61.6 ms: 1.10x faster                                                       |
| go                      | 97.3 ms                                                     | 88.5 ms: 1.10x faster                                                       |
| float                   | 54.6 ms                                                     | 49.7 ms: 1.10x faster                                                       |
| chameleon               | 5.11 ms                                                     | 4.68 ms: 1.09x faster                                                       |
| pickle_pure_python      | 200 us                                                      | 184 us: 1.09x faster                                                        |
| django_template         | 24.1 ms                                                     | 22.2 ms: 1.08x faster                                                       |
| sqlglot_parse           | 952 us                                                      | 878 us: 1.08x faster                                                        |
| scimark_monte_carlo     | 44.6 ms                                                     | 41.2 ms: 1.08x faster                                                       |
| logging_simple          | 6.61 us                                                     | 6.11 us: 1.08x faster                                                       |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.38 ms: 1.08x faster                                                       |
| pprint_safe_repr        | 512 ms                                                      | 474 ms: 1.08x faster                                                        |
| pyflate                 | 304 ms                                                      | 282 ms: 1.08x faster                                                        |
| mdp                     | 1.67 sec                                                    | 1.55 sec: 1.08x faster                                                      |
| nqueens                 | 64.9 ms                                                     | 60.4 ms: 1.07x faster                                                       |
| sqlglot_transpile       | 1.16 ms                                                     | 1.09 ms: 1.07x faster                                                       |
| pprint_pformat          | 1.04 sec                                                    | 972 ms: 1.07x faster                                                        |
| regex_compile           | 90.6 ms                                                     | 84.9 ms: 1.07x faster                                                       |
| thrift                  | 491 us                                                      | 460 us: 1.07x faster                                                        |
| fannkuch                | 252 ms                                                      | 237 ms: 1.06x faster                                                        |
| scimark_lu              | 63.5 ms                                                     | 59.8 ms: 1.06x faster                                                       |
| dulwich_log             | 44.5 ms                                                     | 41.9 ms: 1.06x faster                                                       |
| sqlglot_normalize       | 190 ms                                                      | 180 ms: 1.06x faster                                                        |
| sympy_integrate         | 13.8 ms                                                     | 13.1 ms: 1.05x faster                                                       |
| sqlglot_optimize        | 34.9 ms                                                     | 33.1 ms: 1.05x faster                                                       |
| xml_etree_process       | 37.1 ms                                                     | 35.3 ms: 1.05x faster                                                       |
| xml_etree_parse         | 95.9 ms                                                     | 91.5 ms: 1.05x faster                                                       |
| sympy_expand            | 295 ms                                                      | 282 ms: 1.05x faster                                                        |
| logging_format          | 7.01 us                                                     | 6.73 us: 1.04x faster                                                       |
| 2to3                    | 209 ms                                                      | 201 ms: 1.04x faster                                                        |
| mypy2                   | 229 ms                                                      | 221 ms: 1.04x faster                                                        |
| html5lib                | 37.5 ms                                                     | 36.2 ms: 1.04x faster                                                       |
| sympy_str               | 182 ms                                                      | 176 ms: 1.03x faster                                                        |
| chaos                   | 47.1 ms                                                     | 45.6 ms: 1.03x faster                                                       |
| meteor_contest          | 74.7 ms                                                     | 72.8 ms: 1.03x faster                                                       |
| coverage                | 55.9 ms                                                     | 54.5 ms: 1.03x faster                                                       |
| xml_etree_generate      | 52.2 ms                                                     | 51.2 ms: 1.02x faster                                                       |
| telco                   | 3.90 ms                                                     | 3.84 ms: 1.02x faster                                                       |
| regex_v8                | 13.8 ms                                                     | 13.6 ms: 1.02x faster                                                       |
| docutils                | 1.60 sec                                                    | 1.58 sec: 1.02x faster                                                      |
| create_gc_cycles        | 693 us                                                      | 683 us: 1.01x faster                                                        |
| crypto_pyaes            | 47.6 ms                                                     | 47.0 ms: 1.01x faster                                                       |
| comprehensions          | 15.9 us                                                     | 15.7 us: 1.01x faster                                                       |
| pidigits                | 148 ms                                                      | 147 ms: 1.01x faster                                                        |
| async_generators        | 178 ms                                                      | 179 ms: 1.01x slower                                                        |
| python_startup          | 18.7 ms                                                     | 19.0 ms: 1.01x slower                                                       |
| bench_mp_pool           | 62.5 ms                                                     | 63.6 ms: 1.02x slower                                                       |
| unpickle_list           | 2.55 us                                                     | 2.60 us: 1.02x slower                                                       |
| regex_effbot            | 1.50 ms                                                     | 1.54 ms: 1.03x slower                                                       |
| json_loads              | 12.9 us                                                     | 13.3 us: 1.03x slower                                                       |
| async_tree_io           | 779 ms                                                      | 803 ms: 1.03x slower                                                        |
| async_tree_none         | 320 ms                                                      | 331 ms: 1.03x slower                                                        |
| gc_traversal            | 1.46 ms                                                     | 1.51 ms: 1.03x slower                                                       |
| pickle_dict             | 18.5 us                                                     | 19.2 us: 1.04x slower                                                       |
| async_tree_memoization  | 371 ms                                                      | 387 ms: 1.04x slower                                                        |
| regex_dna               | 115 ms                                                      | 120 ms: 1.04x slower                                                        |
| pickle_list             | 2.68 us                                                     | 2.83 us: 1.05x slower                                                       |
| pathlib                 | 71.4 ms                                                     | 75.4 ms: 1.06x slower                                                       |
| sqlite_synth            | 1.68 us                                                     | 1.78 us: 1.06x slower                                                       |
| pickle                  | 6.61 us                                                     | 7.21 us: 1.09x slower                                                       |
| generators              | 33.8 ms                                                     | 38.0 ms: 1.13x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.06x faster                                                                |

Benchmark hidden because not significant (10): async_tree_cpu_io_mixed, unpickle, bench_thread_pool, sympy_sum, python_startup_no_site, pycparser, scimark_fft, dask, coroutines, xml_etree_iterparse
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
