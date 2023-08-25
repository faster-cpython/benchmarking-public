
# Results vs. 3.11.0

- fork: eduardo-elizondo
- ref: immortal_references
- machine: windows-amd64
- commit hash: 030016a
- commit date: 2023-04-06
- overall geometric mean: 1.09x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.05x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a6+-030016a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 234 ms: 1.12x slower                                                                   |
| chameleon      | 5.11 ms                                                     | 6.13 ms: 1.20x slower                                                                  |
| docutils       | 1.60 sec                                                    | 1.70 sec: 1.06x slower                                                                 |
| html5lib       | 37.5 ms                                                     | 42.8 ms: 1.14x slower                                                                  |
| tornado_http   | 91.8 ms                                                     | 95.8 ms: 1.04x slower                                                                  |
| Geometric mean | (ref)                                                       | 1.11x slower                                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a6+-030016a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| pidigits       | 148 ms                                                      | 152 ms: 1.03x slower                                                                   |
| float          | 54.6 ms                                                     | 62.4 ms: 1.14x slower                                                                  |
| nbody          | 70.0 ms                                                     | 92.3 ms: 1.32x slower                                                                  |
| Geometric mean | (ref)                                                       | 1.16x slower                                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a6+-030016a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 103 ms: 1.14x slower                                                                   |
| Geometric mean | (ref)                                                       | 1.03x slower                                                                           |

Benchmark hidden because not significant (3): regex_v8, regex_dna, regex_effbot

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a6+-030016a |
|----------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.78 ms: 1.31x faster                                                                  |
| unpickle             | 8.09 us                                                     | 7.80 us: 1.04x faster                                                                  |
| xml_etree_parse      | 95.9 ms                                                     | 94.4 ms: 1.02x faster                                                                  |
| unpickle_list        | 2.55 us                                                     | 2.59 us: 1.02x slower                                                                  |
| pickle_dict          | 18.5 us                                                     | 19.6 us: 1.06x slower                                                                  |
| xml_etree_iterparse  | 62.6 ms                                                     | 67.4 ms: 1.08x slower                                                                  |
| json_loads           | 12.9 us                                                     | 13.9 us: 1.08x slower                                                                  |
| pickle               | 6.61 us                                                     | 7.23 us: 1.09x slower                                                                  |
| unpickle_pure_python | 152 us                                                      | 173 us: 1.14x slower                                                                   |
| pickle_list          | 2.68 us                                                     | 3.10 us: 1.16x slower                                                                  |
| xml_etree_generate   | 52.2 ms                                                     | 60.6 ms: 1.16x slower                                                                  |
| xml_etree_process    | 37.1 ms                                                     | 44.2 ms: 1.19x slower                                                                  |
| pickle_pure_python   | 200 us                                                      | 239 us: 1.20x slower                                                                   |
| Geometric mean       | (ref)                                                       | 1.06x slower                                                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a6+-030016a |
|----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| python_startup | 18.7 ms                                                     | 18.9 ms: 1.01x slower                                                                  |
| Geometric mean | (ref)                                                       | 1.00x slower                                                                           |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a6+-030016a |
|-----------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| genshi_xml      | 37.3 ms                                                     | 38.2 ms: 1.02x slower                                                                  |
| genshi_text     | 17.0 ms                                                     | 17.5 ms: 1.03x slower                                                                  |
| django_template | 24.1 ms                                                     | 25.3 ms: 1.05x slower                                                                  |
| mako            | 7.26 ms                                                     | 7.79 ms: 1.07x slower                                                                  |
| Geometric mean  | (ref)                                                       | 1.04x slower                                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230406-pythonperf1-amd64-eduardo%2delizondo-immortal_references-3.12.0a6+-030016a |
|-------------------------|:-----------------------------------------------------------:|:--------------------------------------------------------------------------------------:|
| generators              | 33.8 ms                                                     | 22.5 ms: 1.50x faster                                                                  |
| asyncio_tcp             | 699 ms                                                      | 492 ms: 1.42x faster                                                                   |
| json_dumps              | 7.56 ms                                                     | 5.78 ms: 1.31x faster                                                                  |
| json                    | 3.25 ms                                                     | 2.78 ms: 1.17x faster                                                                  |
| mdp                     | 1.67 sec                                                    | 1.50 sec: 1.11x faster                                                                 |
| coverage                | 55.9 ms                                                     | 53.8 ms: 1.04x faster                                                                  |
| unpickle                | 8.09 us                                                     | 7.80 us: 1.04x faster                                                                  |
| xml_etree_parse         | 95.9 ms                                                     | 94.4 ms: 1.02x faster                                                                  |
| thrift                  | 491 us                                                      | 494 us: 1.01x slower                                                                   |
| dulwich_log             | 44.5 ms                                                     | 45.0 ms: 1.01x slower                                                                  |
| python_startup          | 18.7 ms                                                     | 18.9 ms: 1.01x slower                                                                  |
| unpickle_list           | 2.55 us                                                     | 2.59 us: 1.02x slower                                                                  |
| sympy_expand            | 295 ms                                                      | 302 ms: 1.02x slower                                                                   |
| genshi_xml              | 37.3 ms                                                     | 38.2 ms: 1.02x slower                                                                  |
| pidigits                | 148 ms                                                      | 152 ms: 1.03x slower                                                                   |
| create_gc_cycles        | 693 us                                                      | 711 us: 1.03x slower                                                                   |
| sqlglot_normalize       | 190 ms                                                      | 196 ms: 1.03x slower                                                                   |
| async_tree_io           | 779 ms                                                      | 802 ms: 1.03x slower                                                                   |
| genshi_text             | 17.0 ms                                                     | 17.5 ms: 1.03x slower                                                                  |
| deltablue               | 2.61 ms                                                     | 2.70 ms: 1.03x slower                                                                  |
| nqueens                 | 64.9 ms                                                     | 67.5 ms: 1.04x slower                                                                  |
| gc_traversal            | 1.46 ms                                                     | 1.52 ms: 1.04x slower                                                                  |
| tornado_http            | 91.8 ms                                                     | 95.8 ms: 1.04x slower                                                                  |
| sqlglot_optimize        | 34.9 ms                                                     | 36.6 ms: 1.05x slower                                                                  |
| django_template         | 24.1 ms                                                     | 25.3 ms: 1.05x slower                                                                  |
| bench_thread_pool       | 852 us                                                      | 897 us: 1.05x slower                                                                   |
| sympy_str               | 182 ms                                                      | 192 ms: 1.05x slower                                                                   |
| sympy_sum               | 99.9 ms                                                     | 106 ms: 1.06x slower                                                                   |
| logging_silent          | 69.8 ns                                                     | 73.9 ns: 1.06x slower                                                                  |
| raytrace                | 211 ms                                                      | 223 ms: 1.06x slower                                                                   |
| pickle_dict             | 18.5 us                                                     | 19.6 us: 1.06x slower                                                                  |
| docutils                | 1.60 sec                                                    | 1.70 sec: 1.06x slower                                                                 |
| async_tree_none         | 320 ms                                                      | 342 ms: 1.07x slower                                                                   |
| mako                    | 7.26 ms                                                     | 7.79 ms: 1.07x slower                                                                  |
| logging_format          | 7.01 us                                                     | 7.54 us: 1.07x slower                                                                  |
| mypy2                   | 229 ms                                                      | 246 ms: 1.07x slower                                                                   |
| xml_etree_iterparse     | 62.6 ms                                                     | 67.4 ms: 1.08x slower                                                                  |
| sympy_integrate         | 13.8 ms                                                     | 14.9 ms: 1.08x slower                                                                  |
| json_loads              | 12.9 us                                                     | 13.9 us: 1.08x slower                                                                  |
| pickle                  | 6.61 us                                                     | 7.23 us: 1.09x slower                                                                  |
| async_tree_memoization  | 371 ms                                                      | 407 ms: 1.10x slower                                                                   |
| bench_mp_pool           | 62.5 ms                                                     | 68.7 ms: 1.10x slower                                                                  |
| telco                   | 3.90 ms                                                     | 4.31 ms: 1.10x slower                                                                  |
| richards                | 30.6 ms                                                     | 33.9 ms: 1.11x slower                                                                  |
| logging_simple          | 6.61 us                                                     | 7.36 us: 1.11x slower                                                                  |
| sqlite_synth            | 1.68 us                                                     | 1.87 us: 1.11x slower                                                                  |
| 2to3                    | 209 ms                                                      | 234 ms: 1.12x slower                                                                   |
| coroutines              | 14.6 ms                                                     | 16.4 ms: 1.12x slower                                                                  |
| pycparser               | 691 ms                                                      | 776 ms: 1.12x slower                                                                   |
| deepcopy                | 246 us                                                      | 278 us: 1.13x slower                                                                   |
| go                      | 97.3 ms                                                     | 110 ms: 1.13x slower                                                                   |
| deepcopy_reduce         | 2.07 us                                                     | 2.35 us: 1.13x slower                                                                  |
| unpickle_pure_python    | 152 us                                                      | 173 us: 1.14x slower                                                                   |
| regex_compile           | 90.6 ms                                                     | 103 ms: 1.14x slower                                                                   |
| html5lib                | 37.5 ms                                                     | 42.8 ms: 1.14x slower                                                                  |
| meteor_contest          | 74.7 ms                                                     | 85.3 ms: 1.14x slower                                                                  |
| float                   | 54.6 ms                                                     | 62.4 ms: 1.14x slower                                                                  |
| pprint_safe_repr        | 512 ms                                                      | 588 ms: 1.15x slower                                                                   |
| scimark_lu              | 63.5 ms                                                     | 73.2 ms: 1.15x slower                                                                  |
| pickle_list             | 2.68 us                                                     | 3.10 us: 1.16x slower                                                                  |
| comprehensions          | 15.9 us                                                     | 18.5 us: 1.16x slower                                                                  |
| xml_etree_generate      | 52.2 ms                                                     | 60.6 ms: 1.16x slower                                                                  |
| chaos                   | 47.1 ms                                                     | 54.8 ms: 1.16x slower                                                                  |
| pprint_pformat          | 1.04 sec                                                    | 1.21 sec: 1.16x slower                                                                 |
| hexiom                  | 4.55 ms                                                     | 5.32 ms: 1.17x slower                                                                  |
| pyflate                 | 304 ms                                                      | 357 ms: 1.17x slower                                                                   |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 3.02 ms: 1.17x slower                                                                  |
| deepcopy_memo           | 25.2 us                                                     | 29.8 us: 1.18x slower                                                                  |
| crypto_pyaes            | 47.6 ms                                                     | 56.3 ms: 1.18x slower                                                                  |
| sqlglot_parse           | 952 us                                                      | 1.13 ms: 1.19x slower                                                                  |
| xml_etree_process       | 37.1 ms                                                     | 44.2 ms: 1.19x slower                                                                  |
| spectral_norm           | 67.9 ms                                                     | 81.1 ms: 1.19x slower                                                                  |
| sqlglot_transpile       | 1.16 ms                                                     | 1.39 ms: 1.19x slower                                                                  |
| pathlib                 | 71.4 ms                                                     | 85.3 ms: 1.20x slower                                                                  |
| pickle_pure_python      | 200 us                                                      | 239 us: 1.20x slower                                                                   |
| chameleon               | 5.11 ms                                                     | 6.13 ms: 1.20x slower                                                                  |
| scimark_fft             | 178 ms                                                      | 220 ms: 1.23x slower                                                                   |
| fannkuch                | 252 ms                                                      | 313 ms: 1.24x slower                                                                   |
| scimark_monte_carlo     | 44.6 ms                                                     | 56.0 ms: 1.25x slower                                                                  |
| nbody                   | 70.0 ms                                                     | 92.3 ms: 1.32x slower                                                                  |
| unpack_sequence         | 46.1 ns                                                     | 61.7 ns: 1.34x slower                                                                  |
| async_generators        | 178 ms                                                      | 239 ms: 1.35x slower                                                                   |
| scimark_sor             | 75.6 ms                                                     | 104 ms: 1.38x slower                                                                   |
| dask                    | 264 ms                                                      | 417 ms: 1.58x slower                                                                   |
| Geometric mean          | (ref)                                                       | 1.09x slower                                                                           |

Benchmark hidden because not significant (5): python_startup_no_site, regex_v8, async_tree_cpu_io_mixed, regex_dna, regex_effbot
Ignored benchmarks (9) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.06x
- 95% likely to have a slowdown of 1.06x
- 99% likely to have a slowdown of 1.05x
