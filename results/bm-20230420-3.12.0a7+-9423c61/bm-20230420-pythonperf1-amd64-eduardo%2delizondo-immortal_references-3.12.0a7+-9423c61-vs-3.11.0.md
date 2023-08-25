
# Results vs. 3.11.0

- fork: eduardo-elizondo
- ref: immortal_references
- machine: windows-amd64
- commit hash: 9423c61
- commit date: 2023-04-20
- overall geometric mean: 1.07x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230420-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a7+-9423c61 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 204 ms: 1.02x faster                                                                   |
| chameleon      | 5.11 ms                                                     | 4.88 ms: 1.05x faster                                                                  |
| docutils       | 1.60 sec                                                    | 1.56 sec: 1.03x faster                                                                 |
| html5lib       | 37.5 ms                                                     | 36.4 ms: 1.03x faster                                                                  |
| tornado_http   | 91.8 ms                                                     | 88.8 ms: 1.03x faster                                                                  |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230420-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a7+-9423c61 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| float          | 54.6 ms                                                     | 50.9 ms: 1.07x faster                                                                  |
| nbody          | 70.0 ms                                                     | 68.3 ms: 1.03x faster                                                                  |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230420-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a7+-9423c61 |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 82.1 ms: 1.10x faster                                                                  |
| regex_v8       | 13.8 ms                                                     | 14.1 ms: 1.02x slower                                                                  |
| regex_dna      | 115 ms                                                      | 123 ms: 1.06x slower                                                                   |
| regex_effbot   | 1.50 ms                                                     | 1.60 ms: 1.07x slower                                                                  |
| Geometric mean | (ref)                                                       | 1.01x slower                                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230420-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a7+-9423c61 |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.36 ms: 1.41x faster                                                                  |
| unpickle_pure_python | 152 us                                                      | 132 us: 1.15x faster                                                                   |
| xml_etree_parse      | 95.9 ms                                                     | 88.1 ms: 1.09x faster                                                                  |
| pickle_pure_python   | 200 us                                                      | 188 us: 1.06x faster                                                                   |
| xml_etree_iterparse  | 62.6 ms                                                     | 60.0 ms: 1.04x faster                                                                  |
| xml_etree_process    | 37.1 ms                                                     | 36.2 ms: 1.02x faster                                                                  |
| json_loads           | 12.9 us                                                     | 13.0 us: 1.01x slower                                                                  |
| pickle               | 6.61 us                                                     | 6.82 us: 1.03x slower                                                                  |
| pickle_list          | 2.68 us                                                     | 2.80 us: 1.05x slower                                                                  |
| unpickle_list        | 2.55 us                                                     | 2.71 us: 1.06x slower                                                                  |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                                           |

Benchmark hidden because not significant (3): pickle_dict, xml_etree_generate, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230420-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a7+-9423c61 |
|------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 15.4 ms: 1.03x faster                                                                  |
| python_startup         | 18.7 ms                                                     | 18.2 ms: 1.03x faster                                                                  |
| Geometric mean         | (ref)                                                       | 1.03x faster                                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230420-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a7+-9423c61 |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| genshi_xml      | 37.3 ms                                                     | 31.9 ms: 1.17x faster                                                                  |
| genshi_text     | 17.0 ms                                                     | 14.9 ms: 1.14x faster                                                                  |
| django_template | 24.1 ms                                                     | 21.7 ms: 1.11x faster                                                                  |
| mako            | 7.26 ms                                                     | 6.62 ms: 1.10x faster                                                                  |
| Geometric mean  | (ref)                                                       | 1.13x faster                                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230420-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a7+-9423c61 |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| generators              | 33.8 ms                                                     | 21.5 ms: 1.57x faster                                                                  |
| asyncio_tcp             | 699 ms                                                      | 475 ms: 1.47x faster                                                                   |
| json_dumps              | 7.56 ms                                                     | 5.36 ms: 1.41x faster                                                                  |
| mdp                     | 1.67 sec                                                    | 1.34 sec: 1.25x faster                                                                 |
| sqlglot_parse           | 952 us                                                      | 787 us: 1.21x faster                                                                   |
| deltablue               | 2.61 ms                                                     | 2.17 ms: 1.20x faster                                                                  |
| unpack_sequence         | 46.1 ns                                                     | 38.4 ns: 1.20x faster                                                                  |
| pylint                  | 326 ms                                                      | 274 ms: 1.19x faster                                                                   |
| logging_silent          | 69.8 ns                                                     | 58.9 ns: 1.19x faster                                                                  |
| json                    | 3.25 ms                                                     | 2.74 ms: 1.19x faster                                                                  |
| sqlglot_transpile       | 1.16 ms                                                     | 988 us: 1.18x faster                                                                   |
| genshi_xml              | 37.3 ms                                                     | 31.9 ms: 1.17x faster                                                                  |
| scimark_lu              | 63.5 ms                                                     | 54.3 ms: 1.17x faster                                                                  |
| richards                | 30.6 ms                                                     | 26.5 ms: 1.16x faster                                                                  |
| raytrace                | 211 ms                                                      | 182 ms: 1.16x faster                                                                   |
| unpickle_pure_python    | 152 us                                                      | 132 us: 1.15x faster                                                                   |
| hexiom                  | 4.55 ms                                                     | 3.97 ms: 1.15x faster                                                                  |
| genshi_text             | 17.0 ms                                                     | 14.9 ms: 1.14x faster                                                                  |
| go                      | 97.3 ms                                                     | 86.2 ms: 1.13x faster                                                                  |
| spectral_norm           | 67.9 ms                                                     | 60.5 ms: 1.12x faster                                                                  |
| nqueens                 | 64.9 ms                                                     | 57.8 ms: 1.12x faster                                                                  |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.31 ms: 1.11x faster                                                                  |
| django_template         | 24.1 ms                                                     | 21.7 ms: 1.11x faster                                                                  |
| chaos                   | 47.1 ms                                                     | 42.5 ms: 1.11x faster                                                                  |
| coverage                | 55.9 ms                                                     | 50.6 ms: 1.10x faster                                                                  |
| regex_compile           | 90.6 ms                                                     | 82.1 ms: 1.10x faster                                                                  |
| deepcopy_memo           | 25.2 us                                                     | 22.9 us: 1.10x faster                                                                  |
| mako                    | 7.26 ms                                                     | 6.62 ms: 1.10x faster                                                                  |
| coroutines              | 14.6 ms                                                     | 13.4 ms: 1.09x faster                                                                  |
| xml_etree_parse         | 95.9 ms                                                     | 88.1 ms: 1.09x faster                                                                  |
| dulwich_log             | 44.5 ms                                                     | 40.9 ms: 1.09x faster                                                                  |
| sqlglot_optimize        | 34.9 ms                                                     | 32.2 ms: 1.08x faster                                                                  |
| sqlglot_normalize       | 190 ms                                                      | 176 ms: 1.08x faster                                                                   |
| sympy_expand            | 295 ms                                                      | 274 ms: 1.08x faster                                                                   |
| comprehensions          | 15.9 us                                                     | 14.8 us: 1.08x faster                                                                  |
| deepcopy                | 246 us                                                      | 228 us: 1.08x faster                                                                   |
| float                   | 54.6 ms                                                     | 50.9 ms: 1.07x faster                                                                  |
| mypy2                   | 229 ms                                                      | 214 ms: 1.07x faster                                                                   |
| logging_simple          | 6.61 us                                                     | 6.20 us: 1.07x faster                                                                  |
| logging_format          | 7.01 us                                                     | 6.58 us: 1.07x faster                                                                  |
| sympy_str               | 182 ms                                                      | 171 ms: 1.07x faster                                                                   |
| async_tree_cpu_io_mixed | 501 ms                                                      | 471 ms: 1.06x faster                                                                   |
| pickle_pure_python      | 200 us                                                      | 188 us: 1.06x faster                                                                   |
| scimark_monte_carlo     | 44.6 ms                                                     | 42.1 ms: 1.06x faster                                                                  |
| async_tree_memoization  | 371 ms                                                      | 350 ms: 1.06x faster                                                                   |
| deepcopy_reduce         | 2.07 us                                                     | 1.96 us: 1.06x faster                                                                  |
| pprint_safe_repr        | 512 ms                                                      | 484 ms: 1.06x faster                                                                   |
| async_tree_none         | 320 ms                                                      | 304 ms: 1.06x faster                                                                   |
| pyflate                 | 304 ms                                                      | 288 ms: 1.05x faster                                                                   |
| sympy_sum               | 99.9 ms                                                     | 94.7 ms: 1.05x faster                                                                  |
| bench_thread_pool       | 852 us                                                      | 809 us: 1.05x faster                                                                   |
| sympy_integrate         | 13.8 ms                                                     | 13.1 ms: 1.05x faster                                                                  |
| chameleon               | 5.11 ms                                                     | 4.88 ms: 1.05x faster                                                                  |
| pycparser               | 691 ms                                                      | 659 ms: 1.05x faster                                                                   |
| scimark_fft             | 178 ms                                                      | 170 ms: 1.05x faster                                                                   |
| xml_etree_iterparse     | 62.6 ms                                                     | 60.0 ms: 1.04x faster                                                                  |
| pprint_pformat          | 1.04 sec                                                    | 999 ms: 1.04x faster                                                                   |
| thrift                  | 491 us                                                      | 473 us: 1.04x faster                                                                   |
| crypto_pyaes            | 47.6 ms                                                     | 45.9 ms: 1.04x faster                                                                  |
| tornado_http            | 91.8 ms                                                     | 88.8 ms: 1.03x faster                                                                  |
| python_startup_no_site  | 15.9 ms                                                     | 15.4 ms: 1.03x faster                                                                  |
| html5lib                | 37.5 ms                                                     | 36.4 ms: 1.03x faster                                                                  |
| docutils                | 1.60 sec                                                    | 1.56 sec: 1.03x faster                                                                 |
| fannkuch                | 252 ms                                                      | 245 ms: 1.03x faster                                                                   |
| async_tree_io           | 779 ms                                                      | 759 ms: 1.03x faster                                                                   |
| python_startup          | 18.7 ms                                                     | 18.2 ms: 1.03x faster                                                                  |
| nbody                   | 70.0 ms                                                     | 68.3 ms: 1.03x faster                                                                  |
| 2to3                    | 209 ms                                                      | 204 ms: 1.02x faster                                                                   |
| xml_etree_process       | 37.1 ms                                                     | 36.2 ms: 1.02x faster                                                                  |
| telco                   | 3.90 ms                                                     | 3.82 ms: 1.02x faster                                                                  |
| gc_traversal            | 1.46 ms                                                     | 1.43 ms: 1.02x faster                                                                  |
| json_loads              | 12.9 us                                                     | 13.0 us: 1.01x slower                                                                  |
| meteor_contest          | 74.7 ms                                                     | 76.2 ms: 1.02x slower                                                                  |
| regex_v8                | 13.8 ms                                                     | 14.1 ms: 1.02x slower                                                                  |
| pickle                  | 6.61 us                                                     | 6.82 us: 1.03x slower                                                                  |
| scimark_sor             | 75.6 ms                                                     | 79.0 ms: 1.05x slower                                                                  |
| pickle_list             | 2.68 us                                                     | 2.80 us: 1.05x slower                                                                  |
| bench_mp_pool           | 62.5 ms                                                     | 66.3 ms: 1.06x slower                                                                  |
| unpickle_list           | 2.55 us                                                     | 2.71 us: 1.06x slower                                                                  |
| regex_dna               | 115 ms                                                      | 123 ms: 1.06x slower                                                                   |
| sqlite_synth            | 1.68 us                                                     | 1.79 us: 1.06x slower                                                                  |
| regex_effbot            | 1.50 ms                                                     | 1.60 ms: 1.07x slower                                                                  |
| pathlib                 | 71.4 ms                                                     | 81.2 ms: 1.14x slower                                                                  |
| async_generators        | 178 ms                                                      | 217 ms: 1.22x slower                                                                   |
| dask                    | 264 ms                                                      | 358 ms: 1.35x slower                                                                   |
| Geometric mean          | (ref)                                                       | 1.07x faster                                                                           |

Benchmark hidden because not significant (5): pickle_dict, create_gc_cycles, pidigits, xml_etree_generate, unpickle
Ignored benchmarks (8) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.04x
- 99% likely to have a speedup of 1.03x
