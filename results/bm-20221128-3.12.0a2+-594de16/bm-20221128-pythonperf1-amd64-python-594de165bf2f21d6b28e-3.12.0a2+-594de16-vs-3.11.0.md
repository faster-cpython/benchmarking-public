
# Results vs. 3.11.0

- fork: python
- ref: 594de165bf2f21d6b28e
- machine: windows-amd64
- commit hash: 594de16
- commit date: 2022-11-28
- overall geometric mean: 1.09x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221128-pythonperf1-amd64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 193 ms: 1.08x faster                                                        |
| chameleon      | 5.11 ms                                                     | 4.45 ms: 1.15x faster                                                       |
| docutils       | 1.60 sec                                                    | 1.56 sec: 1.03x faster                                                      |
| html5lib       | 37.5 ms                                                     | 35.7 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221128-pythonperf1-amd64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 57.1 ms: 1.23x faster                                                       |
| float          | 54.6 ms                                                     | 48.3 ms: 1.13x faster                                                       |
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221128-pythonperf1-amd64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 79.4 ms: 1.14x faster                                                       |
| regex_v8       | 13.8 ms                                                     | 14.1 ms: 1.02x slower                                                       |
| regex_effbot   | 1.50 ms                                                     | 1.57 ms: 1.05x slower                                                       |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                                        |
| Geometric mean | (ref)                                                       | 1.00x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221128-pythonperf1-amd64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.36 ms: 1.41x faster                                                       |
| unpickle_pure_python | 152 us                                                      | 121 us: 1.25x faster                                                        |
| pickle_pure_python   | 200 us                                                      | 176 us: 1.13x faster                                                        |
| xml_etree_process    | 37.1 ms                                                     | 33.7 ms: 1.10x faster                                                       |
| xml_etree_parse      | 95.9 ms                                                     | 88.8 ms: 1.08x faster                                                       |
| xml_etree_generate   | 52.2 ms                                                     | 49.2 ms: 1.06x faster                                                       |
| unpickle             | 8.09 us                                                     | 7.78 us: 1.04x faster                                                       |
| xml_etree_iterparse  | 62.6 ms                                                     | 60.8 ms: 1.03x faster                                                       |
| json_loads           | 12.9 us                                                     | 13.2 us: 1.02x slower                                                       |
| unpickle_list        | 2.55 us                                                     | 2.61 us: 1.03x slower                                                       |
| pickle_dict          | 18.5 us                                                     | 19.0 us: 1.03x slower                                                       |
| pickle               | 6.61 us                                                     | 6.81 us: 1.03x slower                                                       |
| pickle_list          | 2.68 us                                                     | 2.85 us: 1.07x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.07x faster                                                                |

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221128-pythonperf1-amd64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 17.0 ms                                                     | 13.9 ms: 1.22x faster                                                       |
| mako            | 7.26 ms                                                     | 6.14 ms: 1.18x faster                                                       |
| django_template | 24.1 ms                                                     | 20.5 ms: 1.17x faster                                                       |
| genshi_xml      | 37.3 ms                                                     | 32.0 ms: 1.17x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.19x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221128-pythonperf1-amd64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpack_sequence         | 46.1 ns                                                     | 26.4 ns: 1.74x faster                                                       |
| json_dumps              | 7.56 ms                                                     | 5.36 ms: 1.41x faster                                                       |
| deltablue               | 2.61 ms                                                     | 1.97 ms: 1.32x faster                                                       |
| richards                | 30.6 ms                                                     | 23.8 ms: 1.28x faster                                                       |
| unpickle_pure_python    | 152 us                                                      | 121 us: 1.25x faster                                                        |
| deepcopy_memo           | 25.2 us                                                     | 20.3 us: 1.24x faster                                                       |
| logging_silent          | 69.8 ns                                                     | 56.7 ns: 1.23x faster                                                       |
| nbody                   | 70.0 ms                                                     | 57.1 ms: 1.23x faster                                                       |
| json                    | 3.25 ms                                                     | 2.65 ms: 1.23x faster                                                       |
| genshi_text             | 17.0 ms                                                     | 13.9 ms: 1.22x faster                                                       |
| scimark_monte_carlo     | 44.6 ms                                                     | 36.9 ms: 1.21x faster                                                       |
| raytrace                | 211 ms                                                      | 177 ms: 1.19x faster                                                        |
| hexiom                  | 4.55 ms                                                     | 3.85 ms: 1.18x faster                                                       |
| mako                    | 7.26 ms                                                     | 6.14 ms: 1.18x faster                                                       |
| fannkuch                | 252 ms                                                      | 215 ms: 1.18x faster                                                        |
| django_template         | 24.1 ms                                                     | 20.5 ms: 1.17x faster                                                       |
| scimark_sor             | 75.6 ms                                                     | 64.4 ms: 1.17x faster                                                       |
| genshi_xml              | 37.3 ms                                                     | 32.0 ms: 1.17x faster                                                       |
| pprint_safe_repr        | 512 ms                                                      | 443 ms: 1.16x faster                                                        |
| pprint_pformat          | 1.04 sec                                                    | 900 ms: 1.16x faster                                                        |
| scimark_lu              | 63.5 ms                                                     | 55.0 ms: 1.15x faster                                                       |
| go                      | 97.3 ms                                                     | 84.3 ms: 1.15x faster                                                       |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.24 ms: 1.15x faster                                                       |
| chameleon               | 5.11 ms                                                     | 4.45 ms: 1.15x faster                                                       |
| deepcopy                | 246 us                                                      | 214 us: 1.15x faster                                                        |
| pyflate                 | 304 ms                                                      | 266 ms: 1.14x faster                                                        |
| regex_compile           | 90.6 ms                                                     | 79.4 ms: 1.14x faster                                                       |
| nqueens                 | 64.9 ms                                                     | 57.1 ms: 1.14x faster                                                       |
| sqlglot_parse           | 952 us                                                      | 838 us: 1.14x faster                                                        |
| pickle_pure_python      | 200 us                                                      | 176 us: 1.13x faster                                                        |
| sqlglot_normalize       | 190 ms                                                      | 168 ms: 1.13x faster                                                        |
| float                   | 54.6 ms                                                     | 48.3 ms: 1.13x faster                                                       |
| sqlglot_transpile       | 1.16 ms                                                     | 1.03 ms: 1.13x faster                                                       |
| deepcopy_reduce         | 2.07 us                                                     | 1.84 us: 1.13x faster                                                       |
| meteor_contest          | 74.7 ms                                                     | 66.7 ms: 1.12x faster                                                       |
| spectral_norm           | 67.9 ms                                                     | 61.0 ms: 1.11x faster                                                       |
| chaos                   | 47.1 ms                                                     | 42.5 ms: 1.11x faster                                                       |
| xml_etree_process       | 37.1 ms                                                     | 33.7 ms: 1.10x faster                                                       |
| dulwich_log             | 44.5 ms                                                     | 40.5 ms: 1.10x faster                                                       |
| sqlglot_optimize        | 34.9 ms                                                     | 31.8 ms: 1.10x faster                                                       |
| crypto_pyaes            | 47.6 ms                                                     | 43.4 ms: 1.10x faster                                                       |
| mdp                     | 1.67 sec                                                    | 1.52 sec: 1.10x faster                                                      |
| scimark_fft             | 178 ms                                                      | 163 ms: 1.09x faster                                                        |
| 2to3                    | 209 ms                                                      | 193 ms: 1.08x faster                                                        |
| pycparser               | 691 ms                                                      | 638 ms: 1.08x faster                                                        |
| xml_etree_parse         | 95.9 ms                                                     | 88.8 ms: 1.08x faster                                                       |
| mypy2                   | 229 ms                                                      | 215 ms: 1.07x faster                                                        |
| coverage                | 55.9 ms                                                     | 52.5 ms: 1.06x faster                                                       |
| xml_etree_generate      | 52.2 ms                                                     | 49.2 ms: 1.06x faster                                                       |
| sympy_expand            | 295 ms                                                      | 278 ms: 1.06x faster                                                        |
| sympy_integrate         | 13.8 ms                                                     | 13.0 ms: 1.06x faster                                                       |
| async_generators        | 178 ms                                                      | 168 ms: 1.06x faster                                                        |
| logging_simple          | 6.61 us                                                     | 6.27 us: 1.05x faster                                                       |
| comprehensions          | 15.9 us                                                     | 15.1 us: 1.05x faster                                                       |
| thrift                  | 491 us                                                      | 466 us: 1.05x faster                                                        |
| html5lib                | 37.5 ms                                                     | 35.7 ms: 1.05x faster                                                       |
| telco                   | 3.90 ms                                                     | 3.73 ms: 1.05x faster                                                       |
| sympy_str               | 182 ms                                                      | 174 ms: 1.05x faster                                                        |
| logging_format          | 7.01 us                                                     | 6.73 us: 1.04x faster                                                       |
| unpickle                | 8.09 us                                                     | 7.78 us: 1.04x faster                                                       |
| xml_etree_iterparse     | 62.6 ms                                                     | 60.8 ms: 1.03x faster                                                       |
| bench_thread_pool       | 852 us                                                      | 830 us: 1.03x faster                                                        |
| sympy_sum               | 99.9 ms                                                     | 97.4 ms: 1.03x faster                                                       |
| docutils                | 1.60 sec                                                    | 1.56 sec: 1.03x faster                                                      |
| async_tree_none         | 320 ms                                                      | 315 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed | 501 ms                                                      | 493 ms: 1.02x faster                                                        |
| async_tree_io           | 779 ms                                                      | 767 ms: 1.02x faster                                                        |
| dask                    | 264 ms                                                      | 261 ms: 1.01x faster                                                        |
| bench_mp_pool           | 62.5 ms                                                     | 62.9 ms: 1.01x slower                                                       |
| create_gc_cycles        | 693 us                                                      | 700 us: 1.01x slower                                                        |
| pidigits                | 148 ms                                                      | 150 ms: 1.01x slower                                                        |
| regex_v8                | 13.8 ms                                                     | 14.1 ms: 1.02x slower                                                       |
| json_loads              | 12.9 us                                                     | 13.2 us: 1.02x slower                                                       |
| unpickle_list           | 2.55 us                                                     | 2.61 us: 1.03x slower                                                       |
| pickle_dict             | 18.5 us                                                     | 19.0 us: 1.03x slower                                                       |
| generators              | 33.8 ms                                                     | 34.8 ms: 1.03x slower                                                       |
| pickle                  | 6.61 us                                                     | 6.81 us: 1.03x slower                                                       |
| pathlib                 | 71.4 ms                                                     | 73.7 ms: 1.03x slower                                                       |
| sqlite_synth            | 1.68 us                                                     | 1.74 us: 1.03x slower                                                       |
| regex_effbot            | 1.50 ms                                                     | 1.57 ms: 1.05x slower                                                       |
| regex_dna               | 115 ms                                                      | 121 ms: 1.05x slower                                                        |
| pickle_list             | 2.68 us                                                     | 2.85 us: 1.07x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.09x faster                                                                |

Benchmark hidden because not significant (7): python_startup_no_site, python_startup, coroutines, tornado_http, gc_traversal, async_tree_memoization, asyncio_tcp
Ignored benchmarks (9) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x
