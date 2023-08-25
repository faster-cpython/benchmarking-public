
# Results vs. 3.11.0

- fork: python
- ref: edfbf56f4ca6588dfd20
- machine: windows-amd64
- commit hash: edfbf56
- commit date: 2023-01-01
- overall geometric mean: 1.06x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230101-pythonperf1-amd64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 205 ms: 1.02x faster                                                        |
| chameleon      | 5.11 ms                                                     | 4.59 ms: 1.12x faster                                                       |
| docutils       | 1.60 sec                                                    | 1.56 sec: 1.03x faster                                                      |
| html5lib       | 37.5 ms                                                     | 36.5 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230101-pythonperf1-amd64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 54.6 ms                                                     | 50.3 ms: 1.09x faster                                                       |
| nbody          | 70.0 ms                                                     | 66.2 ms: 1.06x faster                                                       |
| pidigits       | 148 ms                                                      | 152 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.04x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230101-pythonperf1-amd64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 86.2 ms: 1.05x faster                                                       |
| regex_v8       | 13.8 ms                                                     | 13.4 ms: 1.03x faster                                                       |
| regex_dna      | 115 ms                                                      | 117 ms: 1.02x slower                                                        |
| regex_effbot   | 1.50 ms                                                     | 1.53 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230101-pythonperf1-amd64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.21 ms: 1.45x faster                                                       |
| unpickle_pure_python | 152 us                                                      | 129 us: 1.17x faster                                                        |
| pickle_pure_python   | 200 us                                                      | 181 us: 1.10x faster                                                        |
| xml_etree_parse      | 95.9 ms                                                     | 89.5 ms: 1.07x faster                                                       |
| xml_etree_process    | 37.1 ms                                                     | 35.3 ms: 1.05x faster                                                       |
| xml_etree_generate   | 52.2 ms                                                     | 50.5 ms: 1.03x faster                                                       |
| unpickle             | 8.09 us                                                     | 7.94 us: 1.02x faster                                                       |
| pickle               | 6.61 us                                                     | 6.71 us: 1.02x slower                                                       |
| unpickle_list        | 2.55 us                                                     | 2.72 us: 1.07x slower                                                       |
| pickle_list          | 2.68 us                                                     | 2.88 us: 1.07x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                                |

Benchmark hidden because not significant (3): xml_etree_iterparse, pickle_dict, json_loads

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230101-pythonperf1-amd64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 17.0 ms                                                     | 14.6 ms: 1.16x faster                                                       |
| mako            | 7.26 ms                                                     | 6.34 ms: 1.15x faster                                                       |
| genshi_xml      | 37.3 ms                                                     | 34.4 ms: 1.09x faster                                                       |
| django_template | 24.1 ms                                                     | 22.7 ms: 1.06x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.11x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230101-pythonperf1-amd64-python-edfbf56f4ca6588dfd20-3.12.0a3+-edfbf56 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpack_sequence         | 46.1 ns                                                     | 29.8 ns: 1.54x faster                                                       |
| json_dumps              | 7.56 ms                                                     | 5.21 ms: 1.45x faster                                                       |
| asyncio_tcp             | 699 ms                                                      | 497 ms: 1.41x faster                                                        |
| json                    | 3.25 ms                                                     | 2.73 ms: 1.19x faster                                                       |
| logging_silent          | 69.8 ns                                                     | 59.0 ns: 1.18x faster                                                       |
| deltablue               | 2.61 ms                                                     | 2.21 ms: 1.18x faster                                                       |
| unpickle_pure_python    | 152 us                                                      | 129 us: 1.17x faster                                                        |
| raytrace                | 211 ms                                                      | 181 ms: 1.16x faster                                                        |
| genshi_text             | 17.0 ms                                                     | 14.6 ms: 1.16x faster                                                       |
| deepcopy_memo           | 25.2 us                                                     | 21.8 us: 1.16x faster                                                       |
| mako                    | 7.26 ms                                                     | 6.34 ms: 1.15x faster                                                       |
| scimark_monte_carlo     | 44.6 ms                                                     | 39.4 ms: 1.13x faster                                                       |
| scimark_sor             | 75.6 ms                                                     | 66.9 ms: 1.13x faster                                                       |
| deepcopy                | 246 us                                                      | 220 us: 1.12x faster                                                        |
| chameleon               | 5.11 ms                                                     | 4.59 ms: 1.12x faster                                                       |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.32 ms: 1.11x faster                                                       |
| go                      | 97.3 ms                                                     | 87.9 ms: 1.11x faster                                                       |
| pickle_pure_python      | 200 us                                                      | 181 us: 1.10x faster                                                        |
| deepcopy_reduce         | 2.07 us                                                     | 1.88 us: 1.10x faster                                                       |
| pyflate                 | 304 ms                                                      | 278 ms: 1.09x faster                                                        |
| fannkuch                | 252 ms                                                      | 232 ms: 1.09x faster                                                        |
| richards                | 30.6 ms                                                     | 28.1 ms: 1.09x faster                                                       |
| float                   | 54.6 ms                                                     | 50.3 ms: 1.09x faster                                                       |
| genshi_xml              | 37.3 ms                                                     | 34.4 ms: 1.09x faster                                                       |
| hexiom                  | 4.55 ms                                                     | 4.21 ms: 1.08x faster                                                       |
| scimark_lu              | 63.5 ms                                                     | 58.8 ms: 1.08x faster                                                       |
| mdp                     | 1.67 sec                                                    | 1.55 sec: 1.07x faster                                                      |
| spectral_norm           | 67.9 ms                                                     | 63.3 ms: 1.07x faster                                                       |
| xml_etree_parse         | 95.9 ms                                                     | 89.5 ms: 1.07x faster                                                       |
| nqueens                 | 64.9 ms                                                     | 60.6 ms: 1.07x faster                                                       |
| dulwich_log             | 44.5 ms                                                     | 41.7 ms: 1.07x faster                                                       |
| django_template         | 24.1 ms                                                     | 22.7 ms: 1.06x faster                                                       |
| chaos                   | 47.1 ms                                                     | 44.5 ms: 1.06x faster                                                       |
| nbody                   | 70.0 ms                                                     | 66.2 ms: 1.06x faster                                                       |
| sqlglot_normalize       | 190 ms                                                      | 180 ms: 1.06x faster                                                        |
| regex_compile           | 90.6 ms                                                     | 86.2 ms: 1.05x faster                                                       |
| pprint_pformat          | 1.04 sec                                                    | 990 ms: 1.05x faster                                                        |
| xml_etree_process       | 37.1 ms                                                     | 35.3 ms: 1.05x faster                                                       |
| meteor_contest          | 74.7 ms                                                     | 71.5 ms: 1.04x faster                                                       |
| sqlglot_optimize        | 34.9 ms                                                     | 33.4 ms: 1.04x faster                                                       |
| pycparser               | 691 ms                                                      | 662 ms: 1.04x faster                                                        |
| pprint_safe_repr        | 512 ms                                                      | 490 ms: 1.04x faster                                                        |
| sqlglot_transpile       | 1.16 ms                                                     | 1.12 ms: 1.04x faster                                                       |
| sympy_str               | 182 ms                                                      | 176 ms: 1.04x faster                                                        |
| sympy_expand            | 295 ms                                                      | 285 ms: 1.03x faster                                                        |
| regex_v8                | 13.8 ms                                                     | 13.4 ms: 1.03x faster                                                       |
| xml_etree_generate      | 52.2 ms                                                     | 50.5 ms: 1.03x faster                                                       |
| telco                   | 3.90 ms                                                     | 3.78 ms: 1.03x faster                                                       |
| sqlglot_parse           | 952 us                                                      | 923 us: 1.03x faster                                                        |
| coverage                | 55.9 ms                                                     | 54.2 ms: 1.03x faster                                                       |
| docutils                | 1.60 sec                                                    | 1.56 sec: 1.03x faster                                                      |
| sympy_integrate         | 13.8 ms                                                     | 13.4 ms: 1.03x faster                                                       |
| async_generators        | 178 ms                                                      | 173 ms: 1.03x faster                                                        |
| html5lib                | 37.5 ms                                                     | 36.5 ms: 1.03x faster                                                       |
| logging_format          | 7.01 us                                                     | 6.83 us: 1.03x faster                                                       |
| thrift                  | 491 us                                                      | 479 us: 1.02x faster                                                        |
| mypy2                   | 229 ms                                                      | 224 ms: 1.02x faster                                                        |
| logging_simple          | 6.61 us                                                     | 6.47 us: 1.02x faster                                                       |
| unpickle                | 8.09 us                                                     | 7.94 us: 1.02x faster                                                       |
| 2to3                    | 209 ms                                                      | 205 ms: 1.02x faster                                                        |
| dask                    | 264 ms                                                      | 260 ms: 1.02x faster                                                        |
| crypto_pyaes            | 47.6 ms                                                     | 47.1 ms: 1.01x faster                                                       |
| scimark_fft             | 178 ms                                                      | 177 ms: 1.01x faster                                                        |
| coroutines              | 14.6 ms                                                     | 14.5 ms: 1.01x faster                                                       |
| async_tree_io           | 779 ms                                                      | 789 ms: 1.01x slower                                                        |
| pickle                  | 6.61 us                                                     | 6.71 us: 1.02x slower                                                       |
| regex_dna               | 115 ms                                                      | 117 ms: 1.02x slower                                                        |
| regex_effbot            | 1.50 ms                                                     | 1.53 ms: 1.02x slower                                                       |
| comprehensions          | 15.9 us                                                     | 16.3 us: 1.02x slower                                                       |
| pidigits                | 148 ms                                                      | 152 ms: 1.02x slower                                                        |
| sqlite_synth            | 1.68 us                                                     | 1.76 us: 1.04x slower                                                       |
| async_tree_memoization  | 371 ms                                                      | 388 ms: 1.05x slower                                                        |
| pathlib                 | 71.4 ms                                                     | 75.2 ms: 1.05x slower                                                       |
| unpickle_list           | 2.55 us                                                     | 2.72 us: 1.07x slower                                                       |
| pickle_list             | 2.68 us                                                     | 2.88 us: 1.07x slower                                                       |
| generators              | 33.8 ms                                                     | 36.8 ms: 1.09x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.06x faster                                                                |

Benchmark hidden because not significant (12): async_tree_none, python_startup_no_site, gc_traversal, sympy_sum, create_gc_cycles, xml_etree_iterparse, pickle_dict, bench_thread_pool, bench_mp_pool, json_loads, python_startup, async_tree_cpu_io_mixed
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
