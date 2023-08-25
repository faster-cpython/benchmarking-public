
# Results vs. 3.11.0

- fork: python
- ref: 010576c6ea7e687cf2cb
- machine: windows-amd64
- commit hash: 010576c
- commit date: 2023-01-13
- overall geometric mean: 1.08x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-pythonperf1-amd64-python-010576c6ea7e687cf2cb-3.12.0a4+-010576c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 202 ms: 1.04x faster                                                        |
| chameleon      | 5.11 ms                                                     | 4.60 ms: 1.11x faster                                                       |
| docutils       | 1.60 sec                                                    | 1.52 sec: 1.05x faster                                                      |
| html5lib       | 37.5 ms                                                     | 33.5 ms: 1.12x faster                                                       |
| Geometric mean | (ref)                                                       | 1.07x faster                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-pythonperf1-amd64-python-010576c6ea7e687cf2cb-3.12.0a4+-010576c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 61.2 ms: 1.14x faster                                                       |
| float          | 54.6 ms                                                     | 49.3 ms: 1.11x faster                                                       |
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.08x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-pythonperf1-amd64-python-010576c6ea7e687cf2cb-3.12.0a4+-010576c |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 80.4 ms: 1.13x faster                                                       |
| regex_v8       | 13.8 ms                                                     | 14.0 ms: 1.01x slower                                                       |
| regex_dna      | 115 ms                                                      | 122 ms: 1.06x slower                                                        |
| regex_effbot   | 1.50 ms                                                     | 1.60 ms: 1.07x slower                                                       |
| Geometric mean | (ref)                                                       | 1.00x slower                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-pythonperf1-amd64-python-010576c6ea7e687cf2cb-3.12.0a4+-010576c |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.26 ms: 1.44x faster                                                       |
| unpickle_pure_python | 152 us                                                      | 122 us: 1.25x faster                                                        |
| pickle_pure_python   | 200 us                                                      | 176 us: 1.14x faster                                                        |
| xml_etree_process    | 37.1 ms                                                     | 34.1 ms: 1.09x faster                                                       |
| xml_etree_parse      | 95.9 ms                                                     | 90.3 ms: 1.06x faster                                                       |
| xml_etree_generate   | 52.2 ms                                                     | 49.5 ms: 1.05x faster                                                       |
| xml_etree_iterparse  | 62.6 ms                                                     | 64.0 ms: 1.02x slower                                                       |
| pickle_dict          | 18.5 us                                                     | 19.3 us: 1.04x slower                                                       |
| unpickle_list        | 2.55 us                                                     | 2.65 us: 1.04x slower                                                       |
| pickle_list          | 2.68 us                                                     | 2.79 us: 1.04x slower                                                       |
| unpickle             | 8.09 us                                                     | 8.48 us: 1.05x slower                                                       |
| pickle               | 6.61 us                                                     | 7.18 us: 1.09x slower                                                       |
| json_loads           | 12.9 us                                                     | 14.4 us: 1.12x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-pythonperf1-amd64-python-010576c6ea7e687cf2cb-3.12.0a4+-010576c |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup_no_site | 15.9 ms                                                     | 15.7 ms: 1.01x faster                                                       |
| Geometric mean         | (ref)                                                       | 1.01x faster                                                                |

Benchmark hidden because not significant (1): python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-pythonperf1-amd64-python-010576c6ea7e687cf2cb-3.12.0a4+-010576c |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 17.0 ms                                                     | 13.8 ms: 1.23x faster                                                       |
| genshi_xml      | 37.3 ms                                                     | 30.8 ms: 1.21x faster                                                       |
| mako            | 7.26 ms                                                     | 6.07 ms: 1.20x faster                                                       |
| django_template | 24.1 ms                                                     | 20.7 ms: 1.16x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.20x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230113-pythonperf1-amd64-python-010576c6ea7e687cf2cb-3.12.0a4+-010576c |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpack_sequence         | 46.1 ns                                                     | 26.4 ns: 1.74x faster                                                       |
| asyncio_tcp             | 699 ms                                                      | 484 ms: 1.44x faster                                                        |
| json_dumps              | 7.56 ms                                                     | 5.26 ms: 1.44x faster                                                       |
| deltablue               | 2.61 ms                                                     | 1.96 ms: 1.33x faster                                                       |
| richards                | 30.6 ms                                                     | 24.1 ms: 1.27x faster                                                       |
| unpickle_pure_python    | 152 us                                                      | 122 us: 1.25x faster                                                        |
| logging_silent          | 69.8 ns                                                     | 56.7 ns: 1.23x faster                                                       |
| genshi_text             | 17.0 ms                                                     | 13.8 ms: 1.23x faster                                                       |
| hexiom                  | 4.55 ms                                                     | 3.73 ms: 1.22x faster                                                       |
| deepcopy_memo           | 25.2 us                                                     | 20.7 us: 1.22x faster                                                       |
| genshi_xml              | 37.3 ms                                                     | 30.8 ms: 1.21x faster                                                       |
| mako                    | 7.26 ms                                                     | 6.07 ms: 1.20x faster                                                       |
| deepcopy                | 246 us                                                      | 206 us: 1.20x faster                                                        |
| raytrace                | 211 ms                                                      | 177 ms: 1.19x faster                                                        |
| go                      | 97.3 ms                                                     | 83.6 ms: 1.16x faster                                                       |
| django_template         | 24.1 ms                                                     | 20.7 ms: 1.16x faster                                                       |
| json                    | 3.25 ms                                                     | 2.81 ms: 1.16x faster                                                       |
| nqueens                 | 64.9 ms                                                     | 56.6 ms: 1.15x faster                                                       |
| scimark_monte_carlo     | 44.6 ms                                                     | 39.0 ms: 1.15x faster                                                       |
| scimark_sor             | 75.6 ms                                                     | 66.0 ms: 1.15x faster                                                       |
| nbody                   | 70.0 ms                                                     | 61.2 ms: 1.14x faster                                                       |
| pickle_pure_python      | 200 us                                                      | 176 us: 1.14x faster                                                        |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.26 ms: 1.14x faster                                                       |
| sqlglot_optimize        | 34.9 ms                                                     | 30.9 ms: 1.13x faster                                                       |
| regex_compile           | 90.6 ms                                                     | 80.4 ms: 1.13x faster                                                       |
| html5lib                | 37.5 ms                                                     | 33.5 ms: 1.12x faster                                                       |
| deepcopy_reduce         | 2.07 us                                                     | 1.86 us: 1.12x faster                                                       |
| pprint_safe_repr        | 512 ms                                                      | 459 ms: 1.11x faster                                                        |
| chameleon               | 5.11 ms                                                     | 4.60 ms: 1.11x faster                                                       |
| spectral_norm           | 67.9 ms                                                     | 61.2 ms: 1.11x faster                                                       |
| float                   | 54.6 ms                                                     | 49.3 ms: 1.11x faster                                                       |
| scimark_lu              | 63.5 ms                                                     | 57.3 ms: 1.11x faster                                                       |
| fannkuch                | 252 ms                                                      | 228 ms: 1.10x faster                                                        |
| sqlglot_normalize       | 190 ms                                                      | 173 ms: 1.10x faster                                                        |
| pyflate                 | 304 ms                                                      | 276 ms: 1.10x faster                                                        |
| logging_format          | 7.01 us                                                     | 6.38 us: 1.10x faster                                                       |
| sqlglot_transpile       | 1.16 ms                                                     | 1.06 ms: 1.10x faster                                                       |
| pprint_pformat          | 1.04 sec                                                    | 952 ms: 1.09x faster                                                        |
| sqlglot_parse           | 952 us                                                      | 874 us: 1.09x faster                                                        |
| xml_etree_process       | 37.1 ms                                                     | 34.1 ms: 1.09x faster                                                       |
| logging_simple          | 6.61 us                                                     | 6.12 us: 1.08x faster                                                       |
| pycparser               | 691 ms                                                      | 640 ms: 1.08x faster                                                        |
| chaos                   | 47.1 ms                                                     | 43.8 ms: 1.08x faster                                                       |
| mdp                     | 1.67 sec                                                    | 1.56 sec: 1.07x faster                                                      |
| sympy_expand            | 295 ms                                                      | 276 ms: 1.07x faster                                                        |
| sympy_integrate         | 13.8 ms                                                     | 12.9 ms: 1.07x faster                                                       |
| xml_etree_parse         | 95.9 ms                                                     | 90.3 ms: 1.06x faster                                                       |
| dulwich_log             | 44.5 ms                                                     | 41.9 ms: 1.06x faster                                                       |
| telco                   | 3.90 ms                                                     | 3.69 ms: 1.06x faster                                                       |
| scimark_fft             | 178 ms                                                      | 169 ms: 1.06x faster                                                        |
| sympy_str               | 182 ms                                                      | 173 ms: 1.05x faster                                                        |
| xml_etree_generate      | 52.2 ms                                                     | 49.5 ms: 1.05x faster                                                       |
| docutils                | 1.60 sec                                                    | 1.52 sec: 1.05x faster                                                      |
| sympy_sum               | 99.9 ms                                                     | 94.9 ms: 1.05x faster                                                       |
| coverage                | 55.9 ms                                                     | 53.2 ms: 1.05x faster                                                       |
| mypy2                   | 229 ms                                                      | 219 ms: 1.05x faster                                                        |
| meteor_contest          | 74.7 ms                                                     | 71.9 ms: 1.04x faster                                                       |
| comprehensions          | 15.9 us                                                     | 15.3 us: 1.04x faster                                                       |
| 2to3                    | 209 ms                                                      | 202 ms: 1.04x faster                                                        |
| crypto_pyaes            | 47.6 ms                                                     | 46.0 ms: 1.03x faster                                                       |
| create_gc_cycles        | 693 us                                                      | 669 us: 1.03x faster                                                        |
| thrift                  | 491 us                                                      | 475 us: 1.03x faster                                                        |
| async_tree_cpu_io_mixed | 501 ms                                                      | 487 ms: 1.03x faster                                                        |
| async_tree_memoization  | 371 ms                                                      | 363 ms: 1.02x faster                                                        |
| coroutines              | 14.6 ms                                                     | 14.3 ms: 1.02x faster                                                       |
| dask                    | 264 ms                                                      | 260 ms: 1.02x faster                                                        |
| async_generators        | 178 ms                                                      | 175 ms: 1.01x faster                                                        |
| python_startup_no_site  | 15.9 ms                                                     | 15.7 ms: 1.01x faster                                                       |
| regex_v8                | 13.8 ms                                                     | 14.0 ms: 1.01x slower                                                       |
| pidigits                | 148 ms                                                      | 151 ms: 1.02x slower                                                        |
| xml_etree_iterparse     | 62.6 ms                                                     | 64.0 ms: 1.02x slower                                                       |
| generators              | 33.8 ms                                                     | 34.6 ms: 1.03x slower                                                       |
| gc_traversal            | 1.46 ms                                                     | 1.51 ms: 1.03x slower                                                       |
| pickle_dict             | 18.5 us                                                     | 19.3 us: 1.04x slower                                                       |
| unpickle_list           | 2.55 us                                                     | 2.65 us: 1.04x slower                                                       |
| pickle_list             | 2.68 us                                                     | 2.79 us: 1.04x slower                                                       |
| unpickle                | 8.09 us                                                     | 8.48 us: 1.05x slower                                                       |
| pathlib                 | 71.4 ms                                                     | 75.0 ms: 1.05x slower                                                       |
| regex_dna               | 115 ms                                                      | 122 ms: 1.06x slower                                                        |
| regex_effbot            | 1.50 ms                                                     | 1.60 ms: 1.07x slower                                                       |
| sqlite_synth            | 1.68 us                                                     | 1.80 us: 1.07x slower                                                       |
| pickle                  | 6.61 us                                                     | 7.18 us: 1.09x slower                                                       |
| json_loads              | 12.9 us                                                     | 14.4 us: 1.12x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.08x faster                                                                |

Benchmark hidden because not significant (6): bench_thread_pool, tornado_http, python_startup, async_tree_none, async_tree_io, bench_mp_pool
Ignored benchmarks (9) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x
