
# Results vs. 3.11.0

- fork: python
- ref: b1b375e2670a58fc37cb
- machine: windows-amd64
- commit hash: b1b375e
- commit date: 2023-02-19
- overall geometric mean: 1.09x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230219-pythonperf1-amd64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 199 ms: 1.05x faster                                                        |
| chameleon      | 5.11 ms                                                     | 4.63 ms: 1.10x faster                                                       |
| docutils       | 1.60 sec                                                    | 1.56 sec: 1.03x faster                                                      |
| html5lib       | 37.5 ms                                                     | 35.0 ms: 1.07x faster                                                       |
| Geometric mean | (ref)                                                       | 1.05x faster                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230219-pythonperf1-amd64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 61.9 ms: 1.13x faster                                                       |
| float          | 54.6 ms                                                     | 48.6 ms: 1.12x faster                                                       |
| pidigits       | 148 ms                                                      | 150 ms: 1.01x slower                                                        |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230219-pythonperf1-amd64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 79.1 ms: 1.15x faster                                                       |
| regex_v8       | 13.8 ms                                                     | 14.2 ms: 1.02x slower                                                       |
| regex_dna      | 115 ms                                                      | 120 ms: 1.04x slower                                                        |
| regex_effbot   | 1.50 ms                                                     | 1.58 ms: 1.05x slower                                                       |
| Geometric mean | (ref)                                                       | 1.01x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230219-pythonperf1-amd64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.37 ms: 1.41x faster                                                       |
| unpickle_pure_python | 152 us                                                      | 122 us: 1.24x faster                                                        |
| pickle_pure_python   | 200 us                                                      | 173 us: 1.16x faster                                                        |
| xml_etree_parse      | 95.9 ms                                                     | 92.5 ms: 1.04x faster                                                       |
| xml_etree_process    | 37.1 ms                                                     | 35.8 ms: 1.04x faster                                                       |
| unpickle             | 8.09 us                                                     | 7.87 us: 1.03x faster                                                       |
| xml_etree_generate   | 52.2 ms                                                     | 51.1 ms: 1.02x faster                                                       |
| xml_etree_iterparse  | 62.6 ms                                                     | 61.7 ms: 1.01x faster                                                       |
| json_loads           | 12.9 us                                                     | 12.8 us: 1.01x faster                                                       |
| pickle_list          | 2.68 us                                                     | 2.71 us: 1.01x slower                                                       |
| pickle               | 6.61 us                                                     | 7.13 us: 1.08x slower                                                       |
| unpickle_list        | 2.55 us                                                     | 2.75 us: 1.08x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.05x faster                                                                |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230219-pythonperf1-amd64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 17.0 ms                                                     | 14.0 ms: 1.21x faster                                                       |
| mako            | 7.26 ms                                                     | 6.19 ms: 1.17x faster                                                       |
| genshi_xml      | 37.3 ms                                                     | 32.0 ms: 1.17x faster                                                       |
| django_template | 24.1 ms                                                     | 21.3 ms: 1.13x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.17x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230219-pythonperf1-amd64-python-b1b375e2670a58fc37cb-3.12.0a5+-b1b375e |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpack_sequence         | 46.1 ns                                                     | 25.9 ns: 1.78x faster                                                       |
| generators              | 33.8 ms                                                     | 21.6 ms: 1.56x faster                                                       |
| asyncio_tcp             | 699 ms                                                      | 483 ms: 1.45x faster                                                        |
| json_dumps              | 7.56 ms                                                     | 5.37 ms: 1.41x faster                                                       |
| comprehensions          | 15.9 us                                                     | 11.9 us: 1.34x faster                                                       |
| deltablue               | 2.61 ms                                                     | 1.96 ms: 1.33x faster                                                       |
| logging_silent          | 69.8 ns                                                     | 54.2 ns: 1.29x faster                                                       |
| richards                | 30.6 ms                                                     | 23.9 ms: 1.28x faster                                                       |
| unpickle_pure_python    | 152 us                                                      | 122 us: 1.24x faster                                                        |
| genshi_text             | 17.0 ms                                                     | 14.0 ms: 1.21x faster                                                       |
| raytrace                | 211 ms                                                      | 176 ms: 1.20x faster                                                        |
| fannkuch                | 252 ms                                                      | 212 ms: 1.19x faster                                                        |
| scimark_sor             | 75.6 ms                                                     | 63.5 ms: 1.19x faster                                                       |
| hexiom                  | 4.55 ms                                                     | 3.84 ms: 1.19x faster                                                       |
| pyflate                 | 304 ms                                                      | 256 ms: 1.19x faster                                                        |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.17 ms: 1.18x faster                                                       |
| mako                    | 7.26 ms                                                     | 6.19 ms: 1.17x faster                                                       |
| genshi_xml              | 37.3 ms                                                     | 32.0 ms: 1.17x faster                                                       |
| go                      | 97.3 ms                                                     | 83.6 ms: 1.16x faster                                                       |
| pickle_pure_python      | 200 us                                                      | 173 us: 1.16x faster                                                        |
| deepcopy                | 246 us                                                      | 213 us: 1.16x faster                                                        |
| deepcopy_memo           | 25.2 us                                                     | 21.8 us: 1.15x faster                                                       |
| regex_compile           | 90.6 ms                                                     | 79.1 ms: 1.15x faster                                                       |
| nqueens                 | 64.9 ms                                                     | 57.1 ms: 1.14x faster                                                       |
| chaos                   | 47.1 ms                                                     | 41.6 ms: 1.13x faster                                                       |
| scimark_lu              | 63.5 ms                                                     | 56.1 ms: 1.13x faster                                                       |
| django_template         | 24.1 ms                                                     | 21.3 ms: 1.13x faster                                                       |
| nbody                   | 70.0 ms                                                     | 61.9 ms: 1.13x faster                                                       |
| json                    | 3.25 ms                                                     | 2.89 ms: 1.13x faster                                                       |
| scimark_monte_carlo     | 44.6 ms                                                     | 39.7 ms: 1.12x faster                                                       |
| float                   | 54.6 ms                                                     | 48.6 ms: 1.12x faster                                                       |
| sqlglot_optimize        | 34.9 ms                                                     | 31.3 ms: 1.11x faster                                                       |
| deepcopy_reduce         | 2.07 us                                                     | 1.87 us: 1.11x faster                                                       |
| sympy_str               | 182 ms                                                      | 164 ms: 1.11x faster                                                        |
| coverage                | 55.9 ms                                                     | 50.6 ms: 1.11x faster                                                       |
| spectral_norm           | 67.9 ms                                                     | 61.5 ms: 1.10x faster                                                       |
| chameleon               | 5.11 ms                                                     | 4.63 ms: 1.10x faster                                                       |
| dulwich_log             | 44.5 ms                                                     | 40.5 ms: 1.10x faster                                                       |
| logging_format          | 7.01 us                                                     | 6.41 us: 1.09x faster                                                       |
| sqlglot_normalize       | 190 ms                                                      | 174 ms: 1.09x faster                                                        |
| mdp                     | 1.67 sec                                                    | 1.53 sec: 1.09x faster                                                      |
| sympy_expand            | 295 ms                                                      | 272 ms: 1.09x faster                                                        |
| pprint_pformat          | 1.04 sec                                                    | 961 ms: 1.08x faster                                                        |
| sympy_sum               | 99.9 ms                                                     | 92.8 ms: 1.08x faster                                                       |
| pprint_safe_repr        | 512 ms                                                      | 476 ms: 1.07x faster                                                        |
| html5lib                | 37.5 ms                                                     | 35.0 ms: 1.07x faster                                                       |
| sqlglot_parse           | 952 us                                                      | 888 us: 1.07x faster                                                        |
| logging_simple          | 6.61 us                                                     | 6.19 us: 1.07x faster                                                       |
| sympy_integrate         | 13.8 ms                                                     | 12.9 ms: 1.07x faster                                                       |
| crypto_pyaes            | 47.6 ms                                                     | 44.6 ms: 1.07x faster                                                       |
| scimark_fft             | 178 ms                                                      | 167 ms: 1.07x faster                                                        |
| sqlglot_transpile       | 1.16 ms                                                     | 1.09 ms: 1.07x faster                                                       |
| mypy2                   | 229 ms                                                      | 217 ms: 1.05x faster                                                        |
| 2to3                    | 209 ms                                                      | 199 ms: 1.05x faster                                                        |
| telco                   | 3.90 ms                                                     | 3.72 ms: 1.05x faster                                                       |
| async_tree_cpu_io_mixed | 501 ms                                                      | 479 ms: 1.05x faster                                                        |
| thrift                  | 491 us                                                      | 470 us: 1.04x faster                                                        |
| meteor_contest          | 74.7 ms                                                     | 71.8 ms: 1.04x faster                                                       |
| xml_etree_parse         | 95.9 ms                                                     | 92.5 ms: 1.04x faster                                                       |
| coroutines              | 14.6 ms                                                     | 14.1 ms: 1.04x faster                                                       |
| xml_etree_process       | 37.1 ms                                                     | 35.8 ms: 1.04x faster                                                       |
| docutils                | 1.60 sec                                                    | 1.56 sec: 1.03x faster                                                      |
| unpickle                | 8.09 us                                                     | 7.87 us: 1.03x faster                                                       |
| pycparser               | 691 ms                                                      | 672 ms: 1.03x faster                                                        |
| xml_etree_generate      | 52.2 ms                                                     | 51.1 ms: 1.02x faster                                                       |
| async_tree_memoization  | 371 ms                                                      | 366 ms: 1.01x faster                                                        |
| xml_etree_iterparse     | 62.6 ms                                                     | 61.7 ms: 1.01x faster                                                       |
| json_loads              | 12.9 us                                                     | 12.8 us: 1.01x faster                                                       |
| pickle_list             | 2.68 us                                                     | 2.71 us: 1.01x slower                                                       |
| pidigits                | 148 ms                                                      | 150 ms: 1.01x slower                                                        |
| gc_traversal            | 1.46 ms                                                     | 1.48 ms: 1.02x slower                                                       |
| create_gc_cycles        | 693 us                                                      | 708 us: 1.02x slower                                                        |
| regex_v8                | 13.8 ms                                                     | 14.2 ms: 1.02x slower                                                       |
| bench_mp_pool           | 62.5 ms                                                     | 64.9 ms: 1.04x slower                                                       |
| regex_dna               | 115 ms                                                      | 120 ms: 1.04x slower                                                        |
| regex_effbot            | 1.50 ms                                                     | 1.58 ms: 1.05x slower                                                       |
| pathlib                 | 71.4 ms                                                     | 75.8 ms: 1.06x slower                                                       |
| sqlite_synth            | 1.68 us                                                     | 1.81 us: 1.08x slower                                                       |
| pickle                  | 6.61 us                                                     | 7.13 us: 1.08x slower                                                       |
| unpickle_list           | 2.55 us                                                     | 2.75 us: 1.08x slower                                                       |
| async_generators        | 178 ms                                                      | 220 ms: 1.24x slower                                                        |
| dask                    | 264 ms                                                      | 350 ms: 1.32x slower                                                        |
| Geometric mean          | (ref)                                                       | 1.09x faster                                                                |

Benchmark hidden because not significant (7): async_tree_none, bench_thread_pool, python_startup_no_site, tornado_http, async_tree_io, python_startup, pickle_dict
Ignored benchmarks (9) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x
