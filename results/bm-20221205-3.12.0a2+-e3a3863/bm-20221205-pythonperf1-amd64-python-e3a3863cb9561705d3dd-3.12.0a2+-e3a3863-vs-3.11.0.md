
# Results vs. 3.11.0

- fork: python
- ref: e3a3863cb9561705d3dd
- machine: windows-amd64
- commit hash: e3a3863
- commit date: 2022-12-05
- overall geometric mean: 1.07x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221205-pythonperf1-amd64-python-e3a3863cb9561705d3dd-3.12.0a2+-e3a3863 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 199 ms: 1.05x faster                                                        |
| chameleon      | 5.11 ms                                                     | 4.68 ms: 1.09x faster                                                       |
| docutils       | 1.60 sec                                                    | 1.55 sec: 1.03x faster                                                      |
| html5lib       | 37.5 ms                                                     | 34.5 ms: 1.09x faster                                                       |
| tornado_http   | 91.8 ms                                                     | 90.7 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221205-pythonperf1-amd64-python-e3a3863cb9561705d3dd-3.12.0a2+-e3a3863 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 61.5 ms: 1.14x faster                                                       |
| float          | 54.6 ms                                                     | 49.8 ms: 1.10x faster                                                       |
| pidigits       | 148 ms                                                      | 147 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221205-pythonperf1-amd64-python-e3a3863cb9561705d3dd-3.12.0a2+-e3a3863 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 81.9 ms: 1.11x faster                                                       |
| regex_v8       | 13.8 ms                                                     | 13.8 ms: 1.00x faster                                                       |
| regex_dna      | 115 ms                                                      | 121 ms: 1.05x slower                                                        |
| regex_effbot   | 1.50 ms                                                     | 1.60 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                       | 1.00x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221205-pythonperf1-amd64-python-e3a3863cb9561705d3dd-3.12.0a2+-e3a3863 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.16 ms: 1.46x faster                                                       |
| unpickle_pure_python | 152 us                                                      | 124 us: 1.23x faster                                                        |
| pickle_pure_python   | 200 us                                                      | 172 us: 1.16x faster                                                        |
| xml_etree_process    | 37.1 ms                                                     | 34.3 ms: 1.08x faster                                                       |
| xml_etree_parse      | 95.9 ms                                                     | 89.7 ms: 1.07x faster                                                       |
| xml_etree_generate   | 52.2 ms                                                     | 50.6 ms: 1.03x faster                                                       |
| xml_etree_iterparse  | 62.6 ms                                                     | 63.3 ms: 1.01x slower                                                       |
| unpickle_list        | 2.55 us                                                     | 2.59 us: 1.02x slower                                                       |
| pickle_dict          | 18.5 us                                                     | 18.9 us: 1.02x slower                                                       |
| pickle_list          | 2.68 us                                                     | 2.84 us: 1.06x slower                                                       |
| pickle               | 6.61 us                                                     | 7.11 us: 1.08x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.06x faster                                                                |

Benchmark hidden because not significant (2): unpickle, json_loads

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221205-pythonperf1-amd64-python-e3a3863cb9561705d3dd-3.12.0a2+-e3a3863 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 17.0 ms                                                     | 14.4 ms: 1.18x faster                                                       |
| mako            | 7.26 ms                                                     | 6.20 ms: 1.17x faster                                                       |
| genshi_xml      | 37.3 ms                                                     | 32.1 ms: 1.16x faster                                                       |
| django_template | 24.1 ms                                                     | 21.8 ms: 1.10x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.15x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20221205-pythonperf1-amd64-python-e3a3863cb9561705d3dd-3.12.0a2+-e3a3863 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpack_sequence         | 46.1 ns                                                     | 26.3 ns: 1.75x faster                                                       |
| json_dumps              | 7.56 ms                                                     | 5.16 ms: 1.46x faster                                                       |
| logging_silent          | 69.8 ns                                                     | 55.3 ns: 1.26x faster                                                       |
| deltablue               | 2.61 ms                                                     | 2.07 ms: 1.26x faster                                                       |
| unpickle_pure_python    | 152 us                                                      | 124 us: 1.23x faster                                                        |
| richards                | 30.6 ms                                                     | 25.3 ms: 1.21x faster                                                       |
| deepcopy_memo           | 25.2 us                                                     | 20.9 us: 1.20x faster                                                       |
| json                    | 3.25 ms                                                     | 2.72 ms: 1.20x faster                                                       |
| go                      | 97.3 ms                                                     | 82.2 ms: 1.18x faster                                                       |
| genshi_text             | 17.0 ms                                                     | 14.4 ms: 1.18x faster                                                       |
| fannkuch                | 252 ms                                                      | 215 ms: 1.18x faster                                                        |
| mako                    | 7.26 ms                                                     | 6.20 ms: 1.17x faster                                                       |
| pickle_pure_python      | 200 us                                                      | 172 us: 1.16x faster                                                        |
| genshi_xml              | 37.3 ms                                                     | 32.1 ms: 1.16x faster                                                       |
| raytrace                | 211 ms                                                      | 182 ms: 1.16x faster                                                        |
| deepcopy                | 246 us                                                      | 213 us: 1.16x faster                                                        |
| hexiom                  | 4.55 ms                                                     | 3.98 ms: 1.14x faster                                                       |
| sqlglot_parse           | 952 us                                                      | 835 us: 1.14x faster                                                        |
| nbody                   | 70.0 ms                                                     | 61.5 ms: 1.14x faster                                                       |
| pyflate                 | 304 ms                                                      | 267 ms: 1.14x faster                                                        |
| scimark_monte_carlo     | 44.6 ms                                                     | 39.5 ms: 1.13x faster                                                       |
| spectral_norm           | 67.9 ms                                                     | 60.5 ms: 1.12x faster                                                       |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.29 ms: 1.12x faster                                                       |
| deepcopy_reduce         | 2.07 us                                                     | 1.85 us: 1.12x faster                                                       |
| scimark_sor             | 75.6 ms                                                     | 67.8 ms: 1.11x faster                                                       |
| pprint_pformat          | 1.04 sec                                                    | 934 ms: 1.11x faster                                                        |
| scimark_lu              | 63.5 ms                                                     | 57.2 ms: 1.11x faster                                                       |
| regex_compile           | 90.6 ms                                                     | 81.9 ms: 1.11x faster                                                       |
| sqlglot_transpile       | 1.16 ms                                                     | 1.05 ms: 1.10x faster                                                       |
| django_template         | 24.1 ms                                                     | 21.8 ms: 1.10x faster                                                       |
| float                   | 54.6 ms                                                     | 49.8 ms: 1.10x faster                                                       |
| pprint_safe_repr        | 512 ms                                                      | 467 ms: 1.09x faster                                                        |
| chameleon               | 5.11 ms                                                     | 4.68 ms: 1.09x faster                                                       |
| sqlglot_optimize        | 34.9 ms                                                     | 32.0 ms: 1.09x faster                                                       |
| html5lib                | 37.5 ms                                                     | 34.5 ms: 1.09x faster                                                       |
| sqlglot_normalize       | 190 ms                                                      | 176 ms: 1.08x faster                                                        |
| nqueens                 | 64.9 ms                                                     | 59.9 ms: 1.08x faster                                                       |
| xml_etree_process       | 37.1 ms                                                     | 34.3 ms: 1.08x faster                                                       |
| logging_simple          | 6.61 us                                                     | 6.12 us: 1.08x faster                                                       |
| xml_etree_parse         | 95.9 ms                                                     | 89.7 ms: 1.07x faster                                                       |
| sympy_integrate         | 13.8 ms                                                     | 12.9 ms: 1.07x faster                                                       |
| meteor_contest          | 74.7 ms                                                     | 70.4 ms: 1.06x faster                                                       |
| sympy_expand            | 295 ms                                                      | 278 ms: 1.06x faster                                                        |
| coverage                | 55.9 ms                                                     | 52.8 ms: 1.06x faster                                                       |
| thrift                  | 491 us                                                      | 465 us: 1.06x faster                                                        |
| mypy2                   | 229 ms                                                      | 218 ms: 1.05x faster                                                        |
| logging_format          | 7.01 us                                                     | 6.67 us: 1.05x faster                                                       |
| chaos                   | 47.1 ms                                                     | 44.8 ms: 1.05x faster                                                       |
| 2to3                    | 209 ms                                                      | 199 ms: 1.05x faster                                                        |
| dulwich_log             | 44.5 ms                                                     | 42.4 ms: 1.05x faster                                                       |
| mdp                     | 1.67 sec                                                    | 1.59 sec: 1.05x faster                                                      |
| pycparser               | 691 ms                                                      | 662 ms: 1.04x faster                                                        |
| comprehensions          | 15.9 us                                                     | 15.3 us: 1.04x faster                                                       |
| telco                   | 3.90 ms                                                     | 3.75 ms: 1.04x faster                                                       |
| scimark_fft             | 178 ms                                                      | 171 ms: 1.04x faster                                                        |
| crypto_pyaes            | 47.6 ms                                                     | 45.8 ms: 1.04x faster                                                       |
| docutils                | 1.60 sec                                                    | 1.55 sec: 1.03x faster                                                      |
| xml_etree_generate      | 52.2 ms                                                     | 50.6 ms: 1.03x faster                                                       |
| sympy_str               | 182 ms                                                      | 178 ms: 1.02x faster                                                        |
| create_gc_cycles        | 693 us                                                      | 682 us: 1.01x faster                                                        |
| tornado_http            | 91.8 ms                                                     | 90.7 ms: 1.01x faster                                                       |
| pidigits                | 148 ms                                                      | 147 ms: 1.01x faster                                                        |
| regex_v8                | 13.8 ms                                                     | 13.8 ms: 1.00x faster                                                       |
| xml_etree_iterparse     | 62.6 ms                                                     | 63.3 ms: 1.01x slower                                                       |
| unpickle_list           | 2.55 us                                                     | 2.59 us: 1.02x slower                                                       |
| async_tree_io           | 779 ms                                                      | 792 ms: 1.02x slower                                                        |
| async_generators        | 178 ms                                                      | 181 ms: 1.02x slower                                                        |
| bench_mp_pool           | 62.5 ms                                                     | 63.8 ms: 1.02x slower                                                       |
| async_tree_none         | 320 ms                                                      | 327 ms: 1.02x slower                                                        |
| gc_traversal            | 1.46 ms                                                     | 1.49 ms: 1.02x slower                                                       |
| pickle_dict             | 18.5 us                                                     | 18.9 us: 1.02x slower                                                       |
| coroutines              | 14.6 ms                                                     | 15.0 ms: 1.02x slower                                                       |
| async_tree_memoization  | 371 ms                                                      | 381 ms: 1.03x slower                                                        |
| regex_dna               | 115 ms                                                      | 121 ms: 1.05x slower                                                        |
| pathlib                 | 71.4 ms                                                     | 75.1 ms: 1.05x slower                                                       |
| sqlite_synth            | 1.68 us                                                     | 1.78 us: 1.06x slower                                                       |
| pickle_list             | 2.68 us                                                     | 2.84 us: 1.06x slower                                                       |
| regex_effbot            | 1.50 ms                                                     | 1.60 ms: 1.07x slower                                                       |
| generators              | 33.8 ms                                                     | 36.3 ms: 1.07x slower                                                       |
| pickle                  | 6.61 us                                                     | 7.11 us: 1.08x slower                                                       |
| asyncio_tcp             | 699 ms                                                      | 758 ms: 1.08x slower                                                        |
| Geometric mean          | (ref)                                                       | 1.07x faster                                                                |

Benchmark hidden because not significant (8): unpickle, async_tree_cpu_io_mixed, bench_thread_pool, sympy_sum, json_loads, dask, python_startup_no_site, python_startup
Ignored benchmarks (9) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.04x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x
