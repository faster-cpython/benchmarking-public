
# Results vs. 3.11.0

- fork: python
- ref: f3cb15c88afa2e87067d
- machine: windows-amd64
- commit hash: f3cb15c
- commit date: 2023-02-26
- overall geometric mean: 1.09x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230226-pythonperf1-amd64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 200 ms: 1.04x faster                                                        |
| chameleon      | 5.11 ms                                                     | 4.45 ms: 1.15x faster                                                       |
| docutils       | 1.60 sec                                                    | 1.55 sec: 1.04x faster                                                      |
| html5lib       | 37.5 ms                                                     | 35.1 ms: 1.07x faster                                                       |
| tornado_http   | 91.8 ms                                                     | 89.4 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230226-pythonperf1-amd64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 58.7 ms: 1.19x faster                                                       |
| float          | 54.6 ms                                                     | 48.0 ms: 1.14x faster                                                       |
| pidigits       | 148 ms                                                      | 149 ms: 1.00x slower                                                        |
| Geometric mean | (ref)                                                       | 1.11x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230226-pythonperf1-amd64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 81.3 ms: 1.12x faster                                                       |
| regex_effbot   | 1.50 ms                                                     | 1.52 ms: 1.02x slower                                                       |
| regex_dna      | 115 ms                                                      | 118 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230226-pythonperf1-amd64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.38 ms: 1.41x faster                                                       |
| unpickle_pure_python | 152 us                                                      | 118 us: 1.29x faster                                                        |
| pickle_pure_python   | 200 us                                                      | 167 us: 1.20x faster                                                        |
| xml_etree_process    | 37.1 ms                                                     | 34.6 ms: 1.07x faster                                                       |
| xml_etree_parse      | 95.9 ms                                                     | 92.2 ms: 1.04x faster                                                       |
| unpickle             | 8.09 us                                                     | 7.86 us: 1.03x faster                                                       |
| json_loads           | 12.9 us                                                     | 12.8 us: 1.01x faster                                                       |
| xml_etree_generate   | 52.2 ms                                                     | 52.9 ms: 1.01x slower                                                       |
| pickle_dict          | 18.5 us                                                     | 18.9 us: 1.02x slower                                                       |
| xml_etree_iterparse  | 62.6 ms                                                     | 63.9 ms: 1.02x slower                                                       |
| pickle_list          | 2.68 us                                                     | 2.78 us: 1.04x slower                                                       |
| pickle               | 6.61 us                                                     | 6.89 us: 1.04x slower                                                       |
| unpickle_list        | 2.55 us                                                     | 2.73 us: 1.07x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230226-pythonperf1-amd64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 17.0 ms                                                     | 13.7 ms: 1.24x faster                                                       |
| genshi_xml      | 37.3 ms                                                     | 30.8 ms: 1.21x faster                                                       |
| mako            | 7.26 ms                                                     | 6.22 ms: 1.17x faster                                                       |
| django_template | 24.1 ms                                                     | 20.8 ms: 1.16x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.19x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230226-pythonperf1-amd64-python-f3cb15c88afa2e87067d-3.12.0a5+-f3cb15c |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpack_sequence         | 46.1 ns                                                     | 26.2 ns: 1.75x faster                                                       |
| generators              | 33.8 ms                                                     | 21.5 ms: 1.57x faster                                                       |
| asyncio_tcp             | 699 ms                                                      | 486 ms: 1.44x faster                                                        |
| json_dumps              | 7.56 ms                                                     | 5.38 ms: 1.41x faster                                                       |
| deltablue               | 2.61 ms                                                     | 1.94 ms: 1.35x faster                                                       |
| richards                | 30.6 ms                                                     | 23.2 ms: 1.32x faster                                                       |
| unpickle_pure_python    | 152 us                                                      | 118 us: 1.29x faster                                                        |
| logging_silent          | 69.8 ns                                                     | 54.5 ns: 1.28x faster                                                       |
| deepcopy_memo           | 25.2 us                                                     | 20.0 us: 1.26x faster                                                       |
| genshi_text             | 17.0 ms                                                     | 13.7 ms: 1.24x faster                                                       |
| scimark_sor             | 75.6 ms                                                     | 61.6 ms: 1.23x faster                                                       |
| raytrace                | 211 ms                                                      | 173 ms: 1.22x faster                                                        |
| genshi_xml              | 37.3 ms                                                     | 30.8 ms: 1.21x faster                                                       |
| pickle_pure_python      | 200 us                                                      | 167 us: 1.20x faster                                                        |
| nbody                   | 70.0 ms                                                     | 58.7 ms: 1.19x faster                                                       |
| hexiom                  | 4.55 ms                                                     | 3.84 ms: 1.19x faster                                                       |
| deepcopy                | 246 us                                                      | 208 us: 1.18x faster                                                        |
| mako                    | 7.26 ms                                                     | 6.22 ms: 1.17x faster                                                       |
| json                    | 3.25 ms                                                     | 2.79 ms: 1.17x faster                                                       |
| fannkuch                | 252 ms                                                      | 216 ms: 1.16x faster                                                        |
| spectral_norm           | 67.9 ms                                                     | 58.4 ms: 1.16x faster                                                       |
| django_template         | 24.1 ms                                                     | 20.8 ms: 1.16x faster                                                       |
| chameleon               | 5.11 ms                                                     | 4.45 ms: 1.15x faster                                                       |
| sqlglot_parse           | 952 us                                                      | 831 us: 1.15x faster                                                        |
| deepcopy_reduce         | 2.07 us                                                     | 1.81 us: 1.14x faster                                                       |
| chaos                   | 47.1 ms                                                     | 41.3 ms: 1.14x faster                                                       |
| float                   | 54.6 ms                                                     | 48.0 ms: 1.14x faster                                                       |
| mdp                     | 1.67 sec                                                    | 1.47 sec: 1.13x faster                                                      |
| pyflate                 | 304 ms                                                      | 270 ms: 1.13x faster                                                        |
| regex_compile           | 90.6 ms                                                     | 81.3 ms: 1.12x faster                                                       |
| sqlglot_transpile       | 1.16 ms                                                     | 1.04 ms: 1.12x faster                                                       |
| go                      | 97.3 ms                                                     | 87.5 ms: 1.11x faster                                                       |
| sqlglot_normalize       | 190 ms                                                      | 171 ms: 1.11x faster                                                        |
| pprint_pformat          | 1.04 sec                                                    | 938 ms: 1.11x faster                                                        |
| sqlglot_optimize        | 34.9 ms                                                     | 31.5 ms: 1.11x faster                                                       |
| nqueens                 | 64.9 ms                                                     | 58.6 ms: 1.11x faster                                                       |
| scimark_lu              | 63.5 ms                                                     | 57.4 ms: 1.11x faster                                                       |
| pprint_safe_repr        | 512 ms                                                      | 464 ms: 1.10x faster                                                        |
| logging_format          | 7.01 us                                                     | 6.37 us: 1.10x faster                                                       |
| scimark_fft             | 178 ms                                                      | 162 ms: 1.10x faster                                                        |
| sympy_expand            | 295 ms                                                      | 269 ms: 1.10x faster                                                        |
| coverage                | 55.9 ms                                                     | 51.0 ms: 1.09x faster                                                       |
| scimark_monte_carlo     | 44.6 ms                                                     | 41.0 ms: 1.09x faster                                                       |
| logging_simple          | 6.61 us                                                     | 6.11 us: 1.08x faster                                                       |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.38 ms: 1.08x faster                                                       |
| sympy_integrate         | 13.8 ms                                                     | 12.8 ms: 1.08x faster                                                       |
| xml_etree_process       | 37.1 ms                                                     | 34.6 ms: 1.07x faster                                                       |
| crypto_pyaes            | 47.6 ms                                                     | 44.4 ms: 1.07x faster                                                       |
| html5lib                | 37.5 ms                                                     | 35.1 ms: 1.07x faster                                                       |
| mypy2                   | 229 ms                                                      | 215 ms: 1.06x faster                                                        |
| dulwich_log             | 44.5 ms                                                     | 41.9 ms: 1.06x faster                                                       |
| meteor_contest          | 74.7 ms                                                     | 70.6 ms: 1.06x faster                                                       |
| thrift                  | 491 us                                                      | 464 us: 1.06x faster                                                        |
| coroutines              | 14.6 ms                                                     | 13.9 ms: 1.05x faster                                                       |
| comprehensions          | 15.9 us                                                     | 15.2 us: 1.05x faster                                                       |
| 2to3                    | 209 ms                                                      | 200 ms: 1.04x faster                                                        |
| async_tree_memoization  | 371 ms                                                      | 356 ms: 1.04x faster                                                        |
| xml_etree_parse         | 95.9 ms                                                     | 92.2 ms: 1.04x faster                                                       |
| async_tree_none         | 320 ms                                                      | 308 ms: 1.04x faster                                                        |
| docutils                | 1.60 sec                                                    | 1.55 sec: 1.04x faster                                                      |
| async_tree_cpu_io_mixed | 501 ms                                                      | 484 ms: 1.04x faster                                                        |
| sympy_str               | 182 ms                                                      | 176 ms: 1.03x faster                                                        |
| sympy_sum               | 99.9 ms                                                     | 96.9 ms: 1.03x faster                                                       |
| unpickle                | 8.09 us                                                     | 7.86 us: 1.03x faster                                                       |
| tornado_http            | 91.8 ms                                                     | 89.4 ms: 1.03x faster                                                       |
| pycparser               | 691 ms                                                      | 677 ms: 1.02x faster                                                        |
| async_tree_io           | 779 ms                                                      | 764 ms: 1.02x faster                                                        |
| telco                   | 3.90 ms                                                     | 3.85 ms: 1.01x faster                                                       |
| json_loads              | 12.9 us                                                     | 12.8 us: 1.01x faster                                                       |
| pidigits                | 148 ms                                                      | 149 ms: 1.00x slower                                                        |
| xml_etree_generate      | 52.2 ms                                                     | 52.9 ms: 1.01x slower                                                       |
| regex_effbot            | 1.50 ms                                                     | 1.52 ms: 1.02x slower                                                       |
| pickle_dict             | 18.5 us                                                     | 18.9 us: 1.02x slower                                                       |
| xml_etree_iterparse     | 62.6 ms                                                     | 63.9 ms: 1.02x slower                                                       |
| regex_dna               | 115 ms                                                      | 118 ms: 1.02x slower                                                        |
| pathlib                 | 71.4 ms                                                     | 73.4 ms: 1.03x slower                                                       |
| pickle_list             | 2.68 us                                                     | 2.78 us: 1.04x slower                                                       |
| pickle                  | 6.61 us                                                     | 6.89 us: 1.04x slower                                                       |
| gc_traversal            | 1.46 ms                                                     | 1.53 ms: 1.05x slower                                                       |
| bench_mp_pool           | 62.5 ms                                                     | 65.8 ms: 1.05x slower                                                       |
| unpickle_list           | 2.55 us                                                     | 2.73 us: 1.07x slower                                                       |
| sqlite_synth            | 1.68 us                                                     | 1.86 us: 1.10x slower                                                       |
| async_generators        | 178 ms                                                      | 220 ms: 1.24x slower                                                        |
| dask                    | 264 ms                                                      | 353 ms: 1.33x slower                                                        |
| Geometric mean          | (ref)                                                       | 1.09x faster                                                                |

Benchmark hidden because not significant (5): regex_v8, bench_thread_pool, python_startup_no_site, create_gc_cycles, python_startup
Ignored benchmarks (9) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x
