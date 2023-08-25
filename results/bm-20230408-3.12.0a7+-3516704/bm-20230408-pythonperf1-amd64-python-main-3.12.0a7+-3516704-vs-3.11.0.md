
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: 3516704
- commit date: 2023-04-08
- overall geometric mean: 1.08x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230408-pythonperf1-amd64-python-main-3.12.0a7+-3516704 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 207 ms: 1.01x faster                                        |
| chameleon      | 5.11 ms                                                     | 4.62 ms: 1.11x faster                                       |
| docutils       | 1.60 sec                                                    | 1.56 sec: 1.03x faster                                      |
| html5lib       | 37.5 ms                                                     | 36.7 ms: 1.02x faster                                       |
| tornado_http   | 91.8 ms                                                     | 89.7 ms: 1.02x faster                                       |
| Geometric mean | (ref)                                                       | 1.04x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230408-pythonperf1-amd64-python-main-3.12.0a7+-3516704 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 56.5 ms: 1.24x faster                                       |
| float          | 54.6 ms                                                     | 48.1 ms: 1.14x faster                                       |
| Geometric mean | (ref)                                                       | 1.12x faster                                                |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230408-pythonperf1-amd64-python-main-3.12.0a7+-3516704 |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 83.5 ms: 1.08x faster                                       |
| regex_v8       | 13.8 ms                                                     | 13.2 ms: 1.05x faster                                       |
| regex_effbot   | 1.50 ms                                                     | 1.53 ms: 1.03x slower                                       |
| regex_dna      | 115 ms                                                      | 123 ms: 1.06x slower                                        |
| Geometric mean | (ref)                                                       | 1.01x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230408-pythonperf1-amd64-python-main-3.12.0a7+-3516704 |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.39 ms: 1.40x faster                                       |
| unpickle_pure_python | 152 us                                                      | 127 us: 1.19x faster                                        |
| pickle_pure_python   | 200 us                                                      | 184 us: 1.09x faster                                        |
| xml_etree_parse      | 95.9 ms                                                     | 89.9 ms: 1.07x faster                                       |
| xml_etree_process    | 37.1 ms                                                     | 35.2 ms: 1.05x faster                                       |
| xml_etree_iterparse  | 62.6 ms                                                     | 61.3 ms: 1.02x faster                                       |
| xml_etree_generate   | 52.2 ms                                                     | 51.7 ms: 1.01x faster                                       |
| json_loads           | 12.9 us                                                     | 13.0 us: 1.01x slower                                       |
| unpickle             | 8.09 us                                                     | 8.29 us: 1.02x slower                                       |
| pickle_dict          | 18.5 us                                                     | 19.1 us: 1.03x slower                                       |
| pickle               | 6.61 us                                                     | 6.93 us: 1.05x slower                                       |
| pickle_list          | 2.68 us                                                     | 2.82 us: 1.05x slower                                       |
| unpickle_list        | 2.55 us                                                     | 2.74 us: 1.08x slower                                       |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230408-pythonperf1-amd64-python-main-3.12.0a7+-3516704 |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 16.1 ms: 1.01x slower                                       |
| Geometric mean         | (ref)                                                       | 1.01x slower                                                |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230408-pythonperf1-amd64-python-main-3.12.0a7+-3516704 |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| genshi_text     | 17.0 ms                                                     | 13.8 ms: 1.23x faster                                       |
| genshi_xml      | 37.3 ms                                                     | 30.5 ms: 1.22x faster                                       |
| mako            | 7.26 ms                                                     | 6.22 ms: 1.17x faster                                       |
| django_template | 24.1 ms                                                     | 21.1 ms: 1.14x faster                                       |
| Geometric mean  | (ref)                                                       | 1.19x faster                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230408-pythonperf1-amd64-python-main-3.12.0a7+-3516704 |
|-------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| unpack_sequence         | 46.1 ns                                                     | 28.2 ns: 1.63x faster                                       |
| generators              | 33.8 ms                                                     | 20.7 ms: 1.63x faster                                       |
| asyncio_tcp             | 699 ms                                                      | 487 ms: 1.44x faster                                        |
| json_dumps              | 7.56 ms                                                     | 5.39 ms: 1.40x faster                                       |
| deltablue               | 2.61 ms                                                     | 1.94 ms: 1.34x faster                                       |
| logging_silent          | 69.8 ns                                                     | 54.4 ns: 1.28x faster                                       |
| sqlglot_parse           | 952 us                                                      | 747 us: 1.27x faster                                        |
| nbody                   | 70.0 ms                                                     | 56.5 ms: 1.24x faster                                       |
| sqlglot_transpile       | 1.16 ms                                                     | 947 us: 1.23x faster                                        |
| genshi_text             | 17.0 ms                                                     | 13.8 ms: 1.23x faster                                       |
| genshi_xml              | 37.3 ms                                                     | 30.5 ms: 1.22x faster                                       |
| richards                | 30.6 ms                                                     | 25.2 ms: 1.21x faster                                       |
| raytrace                | 211 ms                                                      | 176 ms: 1.20x faster                                        |
| mdp                     | 1.67 sec                                                    | 1.39 sec: 1.20x faster                                      |
| json                    | 3.25 ms                                                     | 2.72 ms: 1.20x faster                                       |
| unpickle_pure_python    | 152 us                                                      | 127 us: 1.19x faster                                        |
| deepcopy_memo           | 25.2 us                                                     | 21.3 us: 1.18x faster                                       |
| scimark_lu              | 63.5 ms                                                     | 53.8 ms: 1.18x faster                                       |
| hexiom                  | 4.55 ms                                                     | 3.87 ms: 1.18x faster                                       |
| mako                    | 7.26 ms                                                     | 6.22 ms: 1.17x faster                                       |
| go                      | 97.3 ms                                                     | 83.8 ms: 1.16x faster                                       |
| nqueens                 | 64.9 ms                                                     | 56.4 ms: 1.15x faster                                       |
| django_template         | 24.1 ms                                                     | 21.1 ms: 1.14x faster                                       |
| float                   | 54.6 ms                                                     | 48.1 ms: 1.14x faster                                       |
| deepcopy                | 246 us                                                      | 218 us: 1.13x faster                                        |
| spectral_norm           | 67.9 ms                                                     | 60.4 ms: 1.12x faster                                       |
| comprehensions          | 15.9 us                                                     | 14.2 us: 1.12x faster                                       |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.29 ms: 1.12x faster                                       |
| logging_simple          | 6.61 us                                                     | 5.94 us: 1.11x faster                                       |
| chaos                   | 47.1 ms                                                     | 42.6 ms: 1.11x faster                                       |
| chameleon               | 5.11 ms                                                     | 4.62 ms: 1.11x faster                                       |
| coverage                | 55.9 ms                                                     | 50.8 ms: 1.10x faster                                       |
| pprint_safe_repr        | 512 ms                                                      | 467 ms: 1.10x faster                                        |
| deepcopy_reduce         | 2.07 us                                                     | 1.89 us: 1.10x faster                                       |
| sqlglot_normalize       | 190 ms                                                      | 174 ms: 1.09x faster                                        |
| sqlglot_optimize        | 34.9 ms                                                     | 32.0 ms: 1.09x faster                                       |
| scimark_fft             | 178 ms                                                      | 164 ms: 1.09x faster                                        |
| pickle_pure_python      | 200 us                                                      | 184 us: 1.09x faster                                        |
| regex_compile           | 90.6 ms                                                     | 83.5 ms: 1.08x faster                                       |
| coroutines              | 14.6 ms                                                     | 13.6 ms: 1.08x faster                                       |
| pprint_pformat          | 1.04 sec                                                    | 963 ms: 1.08x faster                                        |
| sympy_integrate         | 13.8 ms                                                     | 12.8 ms: 1.08x faster                                       |
| scimark_monte_carlo     | 44.6 ms                                                     | 41.6 ms: 1.07x faster                                       |
| logging_format          | 7.01 us                                                     | 6.55 us: 1.07x faster                                       |
| fannkuch                | 252 ms                                                      | 236 ms: 1.07x faster                                        |
| xml_etree_parse         | 95.9 ms                                                     | 89.9 ms: 1.07x faster                                       |
| async_tree_cpu_io_mixed | 501 ms                                                      | 470 ms: 1.07x faster                                        |
| meteor_contest          | 74.7 ms                                                     | 70.5 ms: 1.06x faster                                       |
| sympy_expand            | 295 ms                                                      | 279 ms: 1.06x faster                                        |
| pyflate                 | 304 ms                                                      | 287 ms: 1.06x faster                                        |
| pycparser               | 691 ms                                                      | 655 ms: 1.05x faster                                        |
| xml_etree_process       | 37.1 ms                                                     | 35.2 ms: 1.05x faster                                       |
| dulwich_log             | 44.5 ms                                                     | 42.3 ms: 1.05x faster                                       |
| regex_v8                | 13.8 ms                                                     | 13.2 ms: 1.05x faster                                       |
| mypy2                   | 229 ms                                                      | 219 ms: 1.05x faster                                        |
| sympy_str               | 182 ms                                                      | 174 ms: 1.05x faster                                        |
| thrift                  | 491 us                                                      | 473 us: 1.04x faster                                        |
| crypto_pyaes            | 47.6 ms                                                     | 46.0 ms: 1.03x faster                                       |
| docutils                | 1.60 sec                                                    | 1.56 sec: 1.03x faster                                      |
| scimark_sor             | 75.6 ms                                                     | 73.7 ms: 1.03x faster                                       |
| async_tree_io           | 779 ms                                                      | 760 ms: 1.02x faster                                        |
| tornado_http            | 91.8 ms                                                     | 89.7 ms: 1.02x faster                                       |
| html5lib                | 37.5 ms                                                     | 36.7 ms: 1.02x faster                                       |
| xml_etree_iterparse     | 62.6 ms                                                     | 61.3 ms: 1.02x faster                                       |
| async_tree_none         | 320 ms                                                      | 314 ms: 1.02x faster                                        |
| sympy_sum               | 99.9 ms                                                     | 98.4 ms: 1.01x faster                                       |
| 2to3                    | 209 ms                                                      | 207 ms: 1.01x faster                                        |
| xml_etree_generate      | 52.2 ms                                                     | 51.7 ms: 1.01x faster                                       |
| json_loads              | 12.9 us                                                     | 13.0 us: 1.01x slower                                       |
| python_startup_no_site  | 15.9 ms                                                     | 16.1 ms: 1.01x slower                                       |
| unpickle                | 8.09 us                                                     | 8.29 us: 1.02x slower                                       |
| regex_effbot            | 1.50 ms                                                     | 1.53 ms: 1.03x slower                                       |
| pickle_dict             | 18.5 us                                                     | 19.1 us: 1.03x slower                                       |
| gc_traversal            | 1.46 ms                                                     | 1.51 ms: 1.04x slower                                       |
| pickle                  | 6.61 us                                                     | 6.93 us: 1.05x slower                                       |
| pickle_list             | 2.68 us                                                     | 2.82 us: 1.05x slower                                       |
| regex_dna               | 115 ms                                                      | 123 ms: 1.06x slower                                        |
| bench_mp_pool           | 62.5 ms                                                     | 67.1 ms: 1.07x slower                                       |
| unpickle_list           | 2.55 us                                                     | 2.74 us: 1.08x slower                                       |
| sqlite_synth            | 1.68 us                                                     | 1.87 us: 1.11x slower                                       |
| async_generators        | 178 ms                                                      | 211 ms: 1.19x slower                                        |
| pathlib                 | 71.4 ms                                                     | 85.9 ms: 1.20x slower                                       |
| dask                    | 264 ms                                                      | 360 ms: 1.36x slower                                        |
| Geometric mean          | (ref)                                                       | 1.08x faster                                                |

Benchmark hidden because not significant (6): create_gc_cycles, pidigits, async_tree_memoization, telco, bench_thread_pool, python_startup
Ignored benchmarks (9) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x
