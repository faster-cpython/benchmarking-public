
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: windows-amd64
- commit hash: 4fe1c4b
- commit date: 2023-04-15
- overall geometric mean: 1.09x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230415-pythonperf1-amd64-python-main-3.12.0a7+-4fe1c4b |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 198 ms: 1.05x faster                                        |
| chameleon      | 5.11 ms                                                     | 4.67 ms: 1.10x faster                                       |
| docutils       | 1.60 sec                                                    | 1.49 sec: 1.08x faster                                      |
| html5lib       | 37.5 ms                                                     | 35.4 ms: 1.06x faster                                       |
| tornado_http   | 91.8 ms                                                     | 85.4 ms: 1.08x faster                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230415-pythonperf1-amd64-python-main-3.12.0a7+-4fe1c4b |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 57.8 ms: 1.21x faster                                       |
| float          | 54.6 ms                                                     | 48.3 ms: 1.13x faster                                       |
| pidigits       | 148 ms                                                      | 146 ms: 1.02x faster                                        |
| Geometric mean | (ref)                                                       | 1.12x faster                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230415-pythonperf1-amd64-python-main-3.12.0a7+-4fe1c4b |
|----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 80.9 ms: 1.12x faster                                       |
| regex_v8       | 13.8 ms                                                     | 14.0 ms: 1.01x slower                                       |
| regex_dna      | 115 ms                                                      | 119 ms: 1.03x slower                                        |
| regex_effbot   | 1.50 ms                                                     | 1.56 ms: 1.04x slower                                       |
| Geometric mean | (ref)                                                       | 1.01x faster                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230415-pythonperf1-amd64-python-main-3.12.0a7+-4fe1c4b |
|----------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.35 ms: 1.41x faster                                       |
| unpickle_pure_python | 152 us                                                      | 127 us: 1.20x faster                                        |
| pickle_pure_python   | 200 us                                                      | 183 us: 1.09x faster                                        |
| xml_etree_parse      | 95.9 ms                                                     | 89.2 ms: 1.07x faster                                       |
| xml_etree_iterparse  | 62.6 ms                                                     | 60.1 ms: 1.04x faster                                       |
| xml_etree_process    | 37.1 ms                                                     | 36.1 ms: 1.03x faster                                       |
| json_loads           | 12.9 us                                                     | 12.7 us: 1.02x faster                                       |
| xml_etree_generate   | 52.2 ms                                                     | 52.7 ms: 1.01x slower                                       |
| pickle_list          | 2.68 us                                                     | 2.82 us: 1.05x slower                                       |
| unpickle_list        | 2.55 us                                                     | 2.68 us: 1.05x slower                                       |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                |

Benchmark hidden because not significant (3): unpickle, pickle_dict, pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230415-pythonperf1-amd64-python-main-3.12.0a7+-4fe1c4b |
|------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| python_startup         | 18.7 ms                                                     | 18.1 ms: 1.03x faster                                       |
| python_startup_no_site | 15.9 ms                                                     | 15.4 ms: 1.03x faster                                       |
| Geometric mean         | (ref)                                                       | 1.03x faster                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230415-pythonperf1-amd64-python-main-3.12.0a7+-4fe1c4b |
|-----------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| genshi_xml      | 37.3 ms                                                     | 31.5 ms: 1.19x faster                                       |
| genshi_text     | 17.0 ms                                                     | 14.3 ms: 1.18x faster                                       |
| mako            | 7.26 ms                                                     | 6.53 ms: 1.11x faster                                       |
| django_template | 24.1 ms                                                     | 21.7 ms: 1.11x faster                                       |
| Geometric mean  | (ref)                                                       | 1.15x faster                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230415-pythonperf1-amd64-python-main-3.12.0a7+-4fe1c4b |
|-------------------------|:-----------------------------------------------------------:|:-----------------------------------------------------------:|
| generators              | 33.8 ms                                                     | 20.0 ms: 1.69x faster                                       |
| asyncio_tcp             | 699 ms                                                      | 471 ms: 1.48x faster                                        |
| json_dumps              | 7.56 ms                                                     | 5.35 ms: 1.41x faster                                       |
| unpack_sequence         | 46.1 ns                                                     | 32.8 ns: 1.41x faster                                       |
| sqlglot_parse           | 952 us                                                      | 755 us: 1.26x faster                                        |
| sqlglot_transpile       | 1.16 ms                                                     | 930 us: 1.25x faster                                        |
| mdp                     | 1.67 sec                                                    | 1.37 sec: 1.22x faster                                      |
| raytrace                | 211 ms                                                      | 173 ms: 1.22x faster                                        |
| json                    | 3.25 ms                                                     | 2.68 ms: 1.21x faster                                       |
| deltablue               | 2.61 ms                                                     | 2.15 ms: 1.21x faster                                       |
| nbody                   | 70.0 ms                                                     | 57.8 ms: 1.21x faster                                       |
| pylint                  | 326 ms                                                      | 270 ms: 1.21x faster                                        |
| unpickle_pure_python    | 152 us                                                      | 127 us: 1.20x faster                                        |
| genshi_xml              | 37.3 ms                                                     | 31.5 ms: 1.19x faster                                       |
| genshi_text             | 17.0 ms                                                     | 14.3 ms: 1.18x faster                                       |
| richards                | 30.6 ms                                                     | 25.9 ms: 1.18x faster                                       |
| logging_silent          | 69.8 ns                                                     | 59.7 ns: 1.17x faster                                       |
| scimark_lu              | 63.5 ms                                                     | 54.8 ms: 1.16x faster                                       |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.24 ms: 1.15x faster                                       |
| hexiom                  | 4.55 ms                                                     | 3.97 ms: 1.15x faster                                       |
| deepcopy_memo           | 25.2 us                                                     | 22.0 us: 1.14x faster                                       |
| scimark_fft             | 178 ms                                                      | 157 ms: 1.13x faster                                        |
| float                   | 54.6 ms                                                     | 48.3 ms: 1.13x faster                                       |
| deepcopy                | 246 us                                                      | 219 us: 1.12x faster                                        |
| regex_compile           | 90.6 ms                                                     | 80.9 ms: 1.12x faster                                       |
| spectral_norm           | 67.9 ms                                                     | 60.7 ms: 1.12x faster                                       |
| sqlglot_optimize        | 34.9 ms                                                     | 31.3 ms: 1.12x faster                                       |
| mypy2                   | 229 ms                                                      | 206 ms: 1.11x faster                                        |
| scimark_monte_carlo     | 44.6 ms                                                     | 40.1 ms: 1.11x faster                                       |
| mako                    | 7.26 ms                                                     | 6.53 ms: 1.11x faster                                       |
| nqueens                 | 64.9 ms                                                     | 58.4 ms: 1.11x faster                                       |
| django_template         | 24.1 ms                                                     | 21.7 ms: 1.11x faster                                       |
| sqlglot_normalize       | 190 ms                                                      | 172 ms: 1.11x faster                                        |
| dulwich_log             | 44.5 ms                                                     | 40.3 ms: 1.10x faster                                       |
| chaos                   | 47.1 ms                                                     | 42.8 ms: 1.10x faster                                       |
| comprehensions          | 15.9 us                                                     | 14.5 us: 1.10x faster                                       |
| go                      | 97.3 ms                                                     | 88.8 ms: 1.10x faster                                       |
| chameleon               | 5.11 ms                                                     | 4.67 ms: 1.10x faster                                       |
| sympy_expand            | 295 ms                                                      | 269 ms: 1.10x faster                                        |
| pickle_pure_python      | 200 us                                                      | 183 us: 1.09x faster                                        |
| deepcopy_reduce         | 2.07 us                                                     | 1.91 us: 1.09x faster                                       |
| sympy_integrate         | 13.8 ms                                                     | 12.7 ms: 1.08x faster                                       |
| pycparser               | 691 ms                                                      | 639 ms: 1.08x faster                                        |
| bench_thread_pool       | 852 us                                                      | 789 us: 1.08x faster                                        |
| docutils                | 1.60 sec                                                    | 1.49 sec: 1.08x faster                                      |
| tornado_http            | 91.8 ms                                                     | 85.4 ms: 1.08x faster                                       |
| xml_etree_parse         | 95.9 ms                                                     | 89.2 ms: 1.07x faster                                       |
| coverage                | 55.9 ms                                                     | 52.1 ms: 1.07x faster                                       |
| sympy_str               | 182 ms                                                      | 170 ms: 1.07x faster                                        |
| sympy_sum               | 99.9 ms                                                     | 93.7 ms: 1.07x faster                                       |
| pprint_safe_repr        | 512 ms                                                      | 480 ms: 1.07x faster                                        |
| html5lib                | 37.5 ms                                                     | 35.4 ms: 1.06x faster                                       |
| async_tree_none         | 320 ms                                                      | 303 ms: 1.06x faster                                        |
| pprint_pformat          | 1.04 sec                                                    | 985 ms: 1.06x faster                                        |
| logging_simple          | 6.61 us                                                     | 6.27 us: 1.05x faster                                       |
| 2to3                    | 209 ms                                                      | 198 ms: 1.05x faster                                        |
| pyflate                 | 304 ms                                                      | 289 ms: 1.05x faster                                        |
| coroutines              | 14.6 ms                                                     | 13.9 ms: 1.05x faster                                       |
| meteor_contest          | 74.7 ms                                                     | 71.2 ms: 1.05x faster                                       |
| crypto_pyaes            | 47.6 ms                                                     | 45.3 ms: 1.05x faster                                       |
| async_tree_cpu_io_mixed | 501 ms                                                      | 478 ms: 1.05x faster                                        |
| scimark_sor             | 75.6 ms                                                     | 72.5 ms: 1.04x faster                                       |
| thrift                  | 491 us                                                      | 471 us: 1.04x faster                                        |
| xml_etree_iterparse     | 62.6 ms                                                     | 60.1 ms: 1.04x faster                                       |
| async_tree_io           | 779 ms                                                      | 749 ms: 1.04x faster                                        |
| telco                   | 3.90 ms                                                     | 3.76 ms: 1.04x faster                                       |
| logging_format          | 7.01 us                                                     | 6.78 us: 1.04x faster                                       |
| fannkuch                | 252 ms                                                      | 245 ms: 1.03x faster                                        |
| python_startup          | 18.7 ms                                                     | 18.1 ms: 1.03x faster                                       |
| async_tree_memoization  | 371 ms                                                      | 360 ms: 1.03x faster                                        |
| python_startup_no_site  | 15.9 ms                                                     | 15.4 ms: 1.03x faster                                       |
| xml_etree_process       | 37.1 ms                                                     | 36.1 ms: 1.03x faster                                       |
| create_gc_cycles        | 693 us                                                      | 677 us: 1.02x faster                                        |
| json_loads              | 12.9 us                                                     | 12.7 us: 1.02x faster                                       |
| pidigits                | 148 ms                                                      | 146 ms: 1.02x faster                                        |
| xml_etree_generate      | 52.2 ms                                                     | 52.7 ms: 1.01x slower                                       |
| regex_v8                | 13.8 ms                                                     | 14.0 ms: 1.01x slower                                       |
| bench_mp_pool           | 62.5 ms                                                     | 64.4 ms: 1.03x slower                                       |
| regex_dna               | 115 ms                                                      | 119 ms: 1.03x slower                                        |
| regex_effbot            | 1.50 ms                                                     | 1.56 ms: 1.04x slower                                       |
| pickle_list             | 2.68 us                                                     | 2.82 us: 1.05x slower                                       |
| unpickle_list           | 2.55 us                                                     | 2.68 us: 1.05x slower                                       |
| sqlite_synth            | 1.68 us                                                     | 1.80 us: 1.07x slower                                       |
| pathlib                 | 71.4 ms                                                     | 82.3 ms: 1.15x slower                                       |
| async_generators        | 178 ms                                                      | 211 ms: 1.19x slower                                        |
| dask                    | 264 ms                                                      | 352 ms: 1.33x slower                                        |
| Geometric mean          | (ref)                                                       | 1.09x faster                                                |

Benchmark hidden because not significant (4): unpickle, gc_traversal, pickle_dict, pickle
Ignored benchmarks (8) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.06x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.05x
