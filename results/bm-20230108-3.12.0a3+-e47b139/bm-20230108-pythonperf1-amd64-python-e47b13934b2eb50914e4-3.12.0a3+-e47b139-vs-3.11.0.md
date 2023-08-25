
# Results vs. 3.11.0

- fork: python
- ref: e47b13934b2eb50914e4
- machine: windows-amd64
- commit hash: e47b139
- commit date: 2023-01-08
- overall geometric mean: 1.09x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230108-pythonperf1-amd64-python-e47b13934b2eb50914e4-3.12.0a3+-e47b139 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 201 ms: 1.04x faster                                                        |
| chameleon      | 5.11 ms                                                     | 4.58 ms: 1.12x faster                                                       |
| docutils       | 1.60 sec                                                    | 1.55 sec: 1.03x faster                                                      |
| html5lib       | 37.5 ms                                                     | 35.5 ms: 1.06x faster                                                       |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230108-pythonperf1-amd64-python-e47b13934b2eb50914e4-3.12.0a3+-e47b139 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 60.2 ms: 1.16x faster                                                       |
| float          | 54.6 ms                                                     | 48.3 ms: 1.13x faster                                                       |
| pidigits       | 148 ms                                                      | 152 ms: 1.03x slower                                                        |
| Geometric mean | (ref)                                                       | 1.09x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230108-pythonperf1-amd64-python-e47b13934b2eb50914e4-3.12.0a3+-e47b139 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 80.3 ms: 1.13x faster                                                       |
| regex_v8       | 13.8 ms                                                     | 14.0 ms: 1.01x slower                                                       |
| regex_dna      | 115 ms                                                      | 117 ms: 1.01x slower                                                        |
| regex_effbot   | 1.50 ms                                                     | 1.54 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230108-pythonperf1-amd64-python-e47b13934b2eb50914e4-3.12.0a3+-e47b139 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.13 ms: 1.47x faster                                                       |
| unpickle_pure_python | 152 us                                                      | 122 us: 1.24x faster                                                        |
| pickle_pure_python   | 200 us                                                      | 169 us: 1.18x faster                                                        |
| xml_etree_parse      | 95.9 ms                                                     | 87.9 ms: 1.09x faster                                                       |
| xml_etree_process    | 37.1 ms                                                     | 34.0 ms: 1.09x faster                                                       |
| xml_etree_generate   | 52.2 ms                                                     | 51.2 ms: 1.02x faster                                                       |
| json_loads           | 12.9 us                                                     | 12.8 us: 1.01x faster                                                       |
| unpickle             | 8.09 us                                                     | 8.33 us: 1.03x slower                                                       |
| pickle_list          | 2.68 us                                                     | 2.77 us: 1.03x slower                                                       |
| unpickle_list        | 2.55 us                                                     | 2.69 us: 1.06x slower                                                       |
| pickle               | 6.61 us                                                     | 6.98 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.06x faster                                                                |

Benchmark hidden because not significant (2): xml_etree_iterparse, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230108-pythonperf1-amd64-python-e47b13934b2eb50914e4-3.12.0a3+-e47b139 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 15.7 ms: 1.01x faster                                                       |
| Geometric mean         | (ref)                                                       | 1.00x slower                                                                |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230108-pythonperf1-amd64-python-e47b13934b2eb50914e4-3.12.0a3+-e47b139 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 17.0 ms                                                     | 13.4 ms: 1.27x faster                                                       |
| genshi_xml      | 37.3 ms                                                     | 30.6 ms: 1.22x faster                                                       |
| mako            | 7.26 ms                                                     | 6.23 ms: 1.17x faster                                                       |
| django_template | 24.1 ms                                                     | 21.1 ms: 1.14x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.20x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230108-pythonperf1-amd64-python-e47b13934b2eb50914e4-3.12.0a3+-e47b139 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpack_sequence         | 46.1 ns                                                     | 25.9 ns: 1.78x faster                                                       |
| json_dumps              | 7.56 ms                                                     | 5.13 ms: 1.47x faster                                                       |
| asyncio_tcp             | 699 ms                                                      | 498 ms: 1.40x faster                                                        |
| deltablue               | 2.61 ms                                                     | 2.01 ms: 1.30x faster                                                       |
| logging_silent          | 69.8 ns                                                     | 54.7 ns: 1.28x faster                                                       |
| genshi_text             | 17.0 ms                                                     | 13.4 ms: 1.27x faster                                                       |
| richards                | 30.6 ms                                                     | 24.2 ms: 1.26x faster                                                       |
| deepcopy_memo           | 25.2 us                                                     | 20.0 us: 1.26x faster                                                       |
| unpickle_pure_python    | 152 us                                                      | 122 us: 1.24x faster                                                        |
| genshi_xml              | 37.3 ms                                                     | 30.6 ms: 1.22x faster                                                       |
| raytrace                | 211 ms                                                      | 176 ms: 1.20x faster                                                        |
| scimark_sor             | 75.6 ms                                                     | 63.1 ms: 1.20x faster                                                       |
| hexiom                  | 4.55 ms                                                     | 3.82 ms: 1.19x faster                                                       |
| deepcopy                | 246 us                                                      | 207 us: 1.19x faster                                                        |
| pickle_pure_python      | 200 us                                                      | 169 us: 1.18x faster                                                        |
| spectral_norm           | 67.9 ms                                                     | 57.5 ms: 1.18x faster                                                       |
| go                      | 97.3 ms                                                     | 82.4 ms: 1.18x faster                                                       |
| json                    | 3.25 ms                                                     | 2.76 ms: 1.18x faster                                                       |
| scimark_monte_carlo     | 44.6 ms                                                     | 38.0 ms: 1.17x faster                                                       |
| mako                    | 7.26 ms                                                     | 6.23 ms: 1.17x faster                                                       |
| nbody                   | 70.0 ms                                                     | 60.2 ms: 1.16x faster                                                       |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.22 ms: 1.16x faster                                                       |
| fannkuch                | 252 ms                                                      | 219 ms: 1.15x faster                                                        |
| django_template         | 24.1 ms                                                     | 21.1 ms: 1.14x faster                                                       |
| pyflate                 | 304 ms                                                      | 267 ms: 1.14x faster                                                        |
| nqueens                 | 64.9 ms                                                     | 57.1 ms: 1.14x faster                                                       |
| float                   | 54.6 ms                                                     | 48.3 ms: 1.13x faster                                                       |
| regex_compile           | 90.6 ms                                                     | 80.3 ms: 1.13x faster                                                       |
| chaos                   | 47.1 ms                                                     | 41.8 ms: 1.13x faster                                                       |
| chameleon               | 5.11 ms                                                     | 4.58 ms: 1.12x faster                                                       |
| sqlglot_parse           | 952 us                                                      | 860 us: 1.11x faster                                                        |
| pprint_pformat          | 1.04 sec                                                    | 940 ms: 1.11x faster                                                        |
| logging_format          | 7.01 us                                                     | 6.35 us: 1.10x faster                                                       |
| deepcopy_reduce         | 2.07 us                                                     | 1.88 us: 1.10x faster                                                       |
| comprehensions          | 15.9 us                                                     | 14.5 us: 1.10x faster                                                       |
| sqlglot_transpile       | 1.16 ms                                                     | 1.06 ms: 1.10x faster                                                       |
| scimark_lu              | 63.5 ms                                                     | 58.1 ms: 1.09x faster                                                       |
| sqlglot_optimize        | 34.9 ms                                                     | 31.9 ms: 1.09x faster                                                       |
| xml_etree_parse         | 95.9 ms                                                     | 87.9 ms: 1.09x faster                                                       |
| xml_etree_process       | 37.1 ms                                                     | 34.0 ms: 1.09x faster                                                       |
| sympy_expand            | 295 ms                                                      | 272 ms: 1.08x faster                                                        |
| logging_simple          | 6.61 us                                                     | 6.10 us: 1.08x faster                                                       |
| thrift                  | 491 us                                                      | 454 us: 1.08x faster                                                        |
| pprint_safe_repr        | 512 ms                                                      | 475 ms: 1.08x faster                                                        |
| sqlglot_normalize       | 190 ms                                                      | 177 ms: 1.08x faster                                                        |
| meteor_contest          | 74.7 ms                                                     | 69.5 ms: 1.07x faster                                                       |
| scimark_fft             | 178 ms                                                      | 168 ms: 1.06x faster                                                        |
| sympy_str               | 182 ms                                                      | 171 ms: 1.06x faster                                                        |
| pycparser               | 691 ms                                                      | 651 ms: 1.06x faster                                                        |
| html5lib                | 37.5 ms                                                     | 35.5 ms: 1.06x faster                                                       |
| sympy_integrate         | 13.8 ms                                                     | 13.1 ms: 1.06x faster                                                       |
| async_tree_none         | 320 ms                                                      | 305 ms: 1.05x faster                                                        |
| mypy2                   | 229 ms                                                      | 218 ms: 1.05x faster                                                        |
| coverage                | 55.9 ms                                                     | 53.2 ms: 1.05x faster                                                       |
| sympy_sum               | 99.9 ms                                                     | 95.2 ms: 1.05x faster                                                       |
| dulwich_log             | 44.5 ms                                                     | 42.5 ms: 1.05x faster                                                       |
| mdp                     | 1.67 sec                                                    | 1.60 sec: 1.05x faster                                                      |
| 2to3                    | 209 ms                                                      | 201 ms: 1.04x faster                                                        |
| telco                   | 3.90 ms                                                     | 3.77 ms: 1.04x faster                                                       |
| docutils                | 1.60 sec                                                    | 1.55 sec: 1.03x faster                                                      |
| crypto_pyaes            | 47.6 ms                                                     | 46.1 ms: 1.03x faster                                                       |
| coroutines              | 14.6 ms                                                     | 14.3 ms: 1.02x faster                                                       |
| async_tree_io           | 779 ms                                                      | 761 ms: 1.02x faster                                                        |
| dask                    | 264 ms                                                      | 259 ms: 1.02x faster                                                        |
| generators              | 33.8 ms                                                     | 33.1 ms: 1.02x faster                                                       |
| xml_etree_generate      | 52.2 ms                                                     | 51.2 ms: 1.02x faster                                                       |
| async_generators        | 178 ms                                                      | 175 ms: 1.01x faster                                                        |
| json_loads              | 12.9 us                                                     | 12.8 us: 1.01x faster                                                       |
| python_startup_no_site  | 15.9 ms                                                     | 15.7 ms: 1.01x faster                                                       |
| bench_mp_pool           | 62.5 ms                                                     | 62.9 ms: 1.01x slower                                                       |
| regex_v8                | 13.8 ms                                                     | 14.0 ms: 1.01x slower                                                       |
| regex_dna               | 115 ms                                                      | 117 ms: 1.01x slower                                                        |
| pidigits                | 148 ms                                                      | 152 ms: 1.03x slower                                                        |
| unpickle                | 8.09 us                                                     | 8.33 us: 1.03x slower                                                       |
| regex_effbot            | 1.50 ms                                                     | 1.54 ms: 1.03x slower                                                       |
| pickle_list             | 2.68 us                                                     | 2.77 us: 1.03x slower                                                       |
| sqlite_synth            | 1.68 us                                                     | 1.76 us: 1.04x slower                                                       |
| pathlib                 | 71.4 ms                                                     | 75.0 ms: 1.05x slower                                                       |
| unpickle_list           | 2.55 us                                                     | 2.69 us: 1.06x slower                                                       |
| pickle                  | 6.61 us                                                     | 6.98 us: 1.06x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.09x faster                                                                |

Benchmark hidden because not significant (8): async_tree_memoization, async_tree_cpu_io_mixed, xml_etree_iterparse, gc_traversal, create_gc_cycles, pickle_dict, bench_thread_pool, python_startup
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x
