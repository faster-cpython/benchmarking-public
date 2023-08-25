
# Results vs. 3.11.0

- fork: python
- ref: 6dedf42527fddbed8ef6
- machine: windows-amd64
- commit hash: 6dedf42
- commit date: 2022-11-10
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221110-pythonperf1-amd64-python-6dedf42527fddbed8ef6-3.12.0a1+-6dedf42 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 198 ms: 1.05x faster                                                        |
| chameleon      | 5.11 ms                                                     | 4.64 ms: 1.10x faster                                                       |
| html5lib       | 37.5 ms                                                     | 35.4 ms: 1.06x faster                                                       |
| tornado_http   | 91.8 ms                                                     | 93.3 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                |

Benchmark hidden because not significant (1): docutils

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221110-pythonperf1-amd64-python-6dedf42527fddbed8ef6-3.12.0a1+-6dedf42 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 63.7 ms: 1.10x faster                                                       |
| float          | 54.6 ms                                                     | 51.1 ms: 1.07x faster                                                       |
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221110-pythonperf1-amd64-python-6dedf42527fddbed8ef6-3.12.0a1+-6dedf42 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 85.8 ms: 1.06x faster                                                       |
| regex_v8       | 13.8 ms                                                     | 14.4 ms: 1.04x slower                                                       |
| regex_dna      | 115 ms                                                      | 124 ms: 1.07x slower                                                        |
| regex_effbot   | 1.50 ms                                                     | 1.64 ms: 1.10x slower                                                       |
| Geometric mean | (ref)                                                       | 1.04x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221110-pythonperf1-amd64-python-6dedf42527fddbed8ef6-3.12.0a1+-6dedf42 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.26 ms: 1.44x faster                                                       |
| unpickle_pure_python | 152 us                                                      | 128 us: 1.18x faster                                                        |
| pickle_pure_python   | 200 us                                                      | 188 us: 1.07x faster                                                        |
| xml_etree_parse      | 95.9 ms                                                     | 90.3 ms: 1.06x faster                                                       |
| xml_etree_process    | 37.1 ms                                                     | 35.4 ms: 1.05x faster                                                       |
| xml_etree_generate   | 52.2 ms                                                     | 51.3 ms: 1.02x faster                                                       |
| unpickle_list        | 2.55 us                                                     | 2.59 us: 1.02x slower                                                       |
| xml_etree_iterparse  | 62.6 ms                                                     | 63.7 ms: 1.02x slower                                                       |
| pickle_dict          | 18.5 us                                                     | 18.9 us: 1.02x slower                                                       |
| pickle               | 6.61 us                                                     | 6.74 us: 1.02x slower                                                       |
| pickle_list          | 2.68 us                                                     | 2.76 us: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                                |

Benchmark hidden because not significant (2): unpickle, json_loads

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221110-pythonperf1-amd64-python-6dedf42527fddbed8ef6-3.12.0a1+-6dedf42 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 17.0 ms                                                     | 14.9 ms: 1.14x faster                                                       |
| mako            | 7.26 ms                                                     | 6.40 ms: 1.14x faster                                                       |
| django_template | 24.1 ms                                                     | 21.9 ms: 1.10x faster                                                       |
| genshi_xml      | 37.3 ms                                                     | 34.0 ms: 1.10x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.12x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221110-pythonperf1-amd64-python-6dedf42527fddbed8ef6-3.12.0a1+-6dedf42 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpack_sequence         | 46.1 ns                                                     | 32.0 ns: 1.44x faster                                                       |
| json_dumps              | 7.56 ms                                                     | 5.26 ms: 1.44x faster                                                       |
| json                    | 3.25 ms                                                     | 2.70 ms: 1.21x faster                                                       |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.17 ms: 1.18x faster                                                       |
| unpickle_pure_python    | 152 us                                                      | 128 us: 1.18x faster                                                        |
| scimark_monte_carlo     | 44.6 ms                                                     | 39.0 ms: 1.14x faster                                                       |
| logging_silent          | 69.8 ns                                                     | 61.2 ns: 1.14x faster                                                       |
| genshi_text             | 17.0 ms                                                     | 14.9 ms: 1.14x faster                                                       |
| mako                    | 7.26 ms                                                     | 6.40 ms: 1.14x faster                                                       |
| deltablue               | 2.61 ms                                                     | 2.31 ms: 1.13x faster                                                       |
| richards                | 30.6 ms                                                     | 27.1 ms: 1.13x faster                                                       |
| deepcopy_memo           | 25.2 us                                                     | 22.6 us: 1.12x faster                                                       |
| fannkuch                | 252 ms                                                      | 228 ms: 1.11x faster                                                        |
| pyflate                 | 304 ms                                                      | 275 ms: 1.11x faster                                                        |
| chameleon               | 5.11 ms                                                     | 4.64 ms: 1.10x faster                                                       |
| django_template         | 24.1 ms                                                     | 21.9 ms: 1.10x faster                                                       |
| nbody                   | 70.0 ms                                                     | 63.7 ms: 1.10x faster                                                       |
| genshi_xml              | 37.3 ms                                                     | 34.0 ms: 1.10x faster                                                       |
| go                      | 97.3 ms                                                     | 88.7 ms: 1.10x faster                                                       |
| raytrace                | 211 ms                                                      | 192 ms: 1.10x faster                                                        |
| hexiom                  | 4.55 ms                                                     | 4.17 ms: 1.09x faster                                                       |
| scimark_lu              | 63.5 ms                                                     | 58.4 ms: 1.09x faster                                                       |
| mdp                     | 1.67 sec                                                    | 1.55 sec: 1.08x faster                                                      |
| pprint_safe_repr        | 512 ms                                                      | 476 ms: 1.07x faster                                                        |
| scimark_sor             | 75.6 ms                                                     | 70.5 ms: 1.07x faster                                                       |
| nqueens                 | 64.9 ms                                                     | 60.6 ms: 1.07x faster                                                       |
| float                   | 54.6 ms                                                     | 51.1 ms: 1.07x faster                                                       |
| pickle_pure_python      | 200 us                                                      | 188 us: 1.07x faster                                                        |
| spectral_norm           | 67.9 ms                                                     | 63.8 ms: 1.06x faster                                                       |
| deepcopy                | 246 us                                                      | 231 us: 1.06x faster                                                        |
| xml_etree_parse         | 95.9 ms                                                     | 90.3 ms: 1.06x faster                                                       |
| pprint_pformat          | 1.04 sec                                                    | 979 ms: 1.06x faster                                                        |
| html5lib                | 37.5 ms                                                     | 35.4 ms: 1.06x faster                                                       |
| telco                   | 3.90 ms                                                     | 3.70 ms: 1.06x faster                                                       |
| regex_compile           | 90.6 ms                                                     | 85.8 ms: 1.06x faster                                                       |
| dulwich_log             | 44.5 ms                                                     | 42.1 ms: 1.06x faster                                                       |
| sqlglot_transpile       | 1.16 ms                                                     | 1.10 ms: 1.06x faster                                                       |
| 2to3                    | 209 ms                                                      | 198 ms: 1.05x faster                                                        |
| logging_simple          | 6.61 us                                                     | 6.29 us: 1.05x faster                                                       |
| deepcopy_reduce         | 2.07 us                                                     | 1.97 us: 1.05x faster                                                       |
| sqlglot_normalize       | 190 ms                                                      | 182 ms: 1.05x faster                                                        |
| xml_etree_process       | 37.1 ms                                                     | 35.4 ms: 1.05x faster                                                       |
| scimark_fft             | 178 ms                                                      | 171 ms: 1.04x faster                                                        |
| crypto_pyaes            | 47.6 ms                                                     | 45.7 ms: 1.04x faster                                                       |
| pycparser               | 691 ms                                                      | 665 ms: 1.04x faster                                                        |
| sqlglot_optimize        | 34.9 ms                                                     | 33.6 ms: 1.04x faster                                                       |
| sqlglot_parse           | 952 us                                                      | 918 us: 1.04x faster                                                        |
| sympy_str               | 182 ms                                                      | 176 ms: 1.04x faster                                                        |
| chaos                   | 47.1 ms                                                     | 45.5 ms: 1.04x faster                                                       |
| logging_format          | 7.01 us                                                     | 6.81 us: 1.03x faster                                                       |
| sympy_integrate         | 13.8 ms                                                     | 13.4 ms: 1.03x faster                                                       |
| coverage                | 55.9 ms                                                     | 54.4 ms: 1.03x faster                                                       |
| thrift                  | 491 us                                                      | 478 us: 1.03x faster                                                        |
| mypy2                   | 229 ms                                                      | 223 ms: 1.03x faster                                                        |
| meteor_contest          | 74.7 ms                                                     | 73.4 ms: 1.02x faster                                                       |
| xml_etree_generate      | 52.2 ms                                                     | 51.3 ms: 1.02x faster                                                       |
| bench_thread_pool       | 852 us                                                      | 838 us: 1.02x faster                                                        |
| create_gc_cycles        | 693 us                                                      | 684 us: 1.01x faster                                                        |
| sympy_expand            | 295 ms                                                      | 292 ms: 1.01x faster                                                        |
| sympy_sum               | 99.9 ms                                                     | 99.0 ms: 1.01x faster                                                       |
| gc_traversal            | 1.46 ms                                                     | 1.47 ms: 1.01x slower                                                       |
| async_tree_io           | 779 ms                                                      | 790 ms: 1.01x slower                                                        |
| unpickle_list           | 2.55 us                                                     | 2.59 us: 1.02x slower                                                       |
| tornado_http            | 91.8 ms                                                     | 93.3 ms: 1.02x slower                                                       |
| pidigits                | 148 ms                                                      | 151 ms: 1.02x slower                                                        |
| xml_etree_iterparse     | 62.6 ms                                                     | 63.7 ms: 1.02x slower                                                       |
| pickle_dict             | 18.5 us                                                     | 18.9 us: 1.02x slower                                                       |
| pickle                  | 6.61 us                                                     | 6.74 us: 1.02x slower                                                       |
| async_tree_cpu_io_mixed | 501 ms                                                      | 511 ms: 1.02x slower                                                        |
| comprehensions          | 15.9 us                                                     | 16.3 us: 1.02x slower                                                       |
| sqlite_synth            | 1.68 us                                                     | 1.72 us: 1.02x slower                                                       |
| coroutines              | 14.6 ms                                                     | 15.0 ms: 1.03x slower                                                       |
| pickle_list             | 2.68 us                                                     | 2.76 us: 1.03x slower                                                       |
| pathlib                 | 71.4 ms                                                     | 73.7 ms: 1.03x slower                                                       |
| async_generators        | 178 ms                                                      | 183 ms: 1.03x slower                                                        |
| regex_v8                | 13.8 ms                                                     | 14.4 ms: 1.04x slower                                                       |
| async_tree_memoization  | 371 ms                                                      | 391 ms: 1.05x slower                                                        |
| regex_dna               | 115 ms                                                      | 124 ms: 1.07x slower                                                        |
| generators              | 33.8 ms                                                     | 37.0 ms: 1.10x slower                                                       |
| regex_effbot            | 1.50 ms                                                     | 1.64 ms: 1.10x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.05x faster                                                                |

Benchmark hidden because not significant (9): python_startup_no_site, dask, docutils, python_startup, async_tree_none, unpickle, bench_mp_pool, json_loads, asyncio_tcp
Ignored benchmarks (9) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
