
# Results vs. 3.11.0

- fork: python
- ref: d717be04dc7876696cb2
- machine: windows-amd64
- commit hash: d717be0
- commit date: 2023-01-22
- overall geometric mean: 1.09x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.04x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230122-pythonperf1-amd64-python-d717be04dc7876696cb2-3.12.0a4+-d717be0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 209 ms                                                      | 202 ms: 1.03x faster                                                        |
| chameleon      | 5.11 ms                                                     | 4.37 ms: 1.17x faster                                                       |
| docutils       | 1.60 sec                                                    | 1.55 sec: 1.04x faster                                                      |
| html5lib       | 37.5 ms                                                     | 35.7 ms: 1.05x faster                                                       |
| tornado_http   | 91.8 ms                                                     | 88.8 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                       | 1.06x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230122-pythonperf1-amd64-python-d717be04dc7876696cb2-3.12.0a4+-d717be0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 70.0 ms                                                     | 59.7 ms: 1.17x faster                                                       |
| float          | 54.6 ms                                                     | 47.2 ms: 1.16x faster                                                       |
| pidigits       | 148 ms                                                      | 151 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                       | 1.10x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230122-pythonperf1-amd64-python-d717be04dc7876696cb2-3.12.0a4+-d717be0 |
|----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_compile  | 90.6 ms                                                     | 78.1 ms: 1.16x faster                                                       |
| regex_v8       | 13.8 ms                                                     | 13.6 ms: 1.02x faster                                                       |
| regex_dna      | 115 ms                                                      | 117 ms: 1.02x slower                                                        |
| regex_effbot   | 1.50 ms                                                     | 1.54 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                       | 1.03x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230122-pythonperf1-amd64-python-d717be04dc7876696cb2-3.12.0a4+-d717be0 |
|----------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 7.56 ms                                                     | 5.43 ms: 1.39x faster                                                       |
| unpickle_pure_python | 152 us                                                      | 121 us: 1.26x faster                                                        |
| pickle_pure_python   | 200 us                                                      | 171 us: 1.17x faster                                                        |
| xml_etree_process    | 37.1 ms                                                     | 35.0 ms: 1.06x faster                                                       |
| xml_etree_generate   | 52.2 ms                                                     | 49.7 ms: 1.05x faster                                                       |
| xml_etree_parse      | 95.9 ms                                                     | 94.7 ms: 1.01x faster                                                       |
| json_loads           | 12.9 us                                                     | 12.8 us: 1.01x faster                                                       |
| xml_etree_iterparse  | 62.6 ms                                                     | 63.3 ms: 1.01x slower                                                       |
| pickle_list          | 2.68 us                                                     | 2.72 us: 1.01x slower                                                       |
| pickle               | 6.61 us                                                     | 6.94 us: 1.05x slower                                                       |
| unpickle_list        | 2.55 us                                                     | 2.76 us: 1.08x slower                                                       |
| unpickle             | 8.09 us                                                     | 9.15 us: 1.13x slower                                                       |
| Geometric mean       | (ref)                                                       | 1.04x faster                                                                |

Benchmark hidden because not significant (1): pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230122-pythonperf1-amd64-python-d717be04dc7876696cb2-3.12.0a4+-d717be0 |
|------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 18.7 ms                                                     | 19.2 ms: 1.03x slower                                                       |
| python_startup_no_site | 15.9 ms                                                     | 16.5 ms: 1.04x slower                                                       |
| Geometric mean         | (ref)                                                       | 1.03x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230122-pythonperf1-amd64-python-d717be04dc7876696cb2-3.12.0a4+-d717be0 |
|-----------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 17.0 ms                                                     | 13.4 ms: 1.27x faster                                                       |
| django_template | 24.1 ms                                                     | 20.4 ms: 1.18x faster                                                       |
| mako            | 7.26 ms                                                     | 6.21 ms: 1.17x faster                                                       |
| genshi_xml      | 37.3 ms                                                     | 33.0 ms: 1.13x faster                                                       |
| Geometric mean  | (ref)                                                       | 1.19x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509 | bm-20230122-pythonperf1-amd64-python-d717be04dc7876696cb2-3.12.0a4+-d717be0 |
|-------------------------|:-----------------------------------------------------------:|:---------------------------------------------------------------------------:|
| unpack_sequence         | 46.1 ns                                                     | 25.7 ns: 1.79x faster                                                       |
| asyncio_tcp             | 699 ms                                                      | 483 ms: 1.45x faster                                                        |
| json_dumps              | 7.56 ms                                                     | 5.43 ms: 1.39x faster                                                       |
| deltablue               | 2.61 ms                                                     | 2.02 ms: 1.30x faster                                                       |
| genshi_text             | 17.0 ms                                                     | 13.4 ms: 1.27x faster                                                       |
| richards                | 30.6 ms                                                     | 24.2 ms: 1.26x faster                                                       |
| unpickle_pure_python    | 152 us                                                      | 121 us: 1.26x faster                                                        |
| deepcopy_memo           | 25.2 us                                                     | 20.2 us: 1.24x faster                                                       |
| logging_silent          | 69.8 ns                                                     | 56.5 ns: 1.24x faster                                                       |
| raytrace                | 211 ms                                                      | 173 ms: 1.22x faster                                                        |
| deepcopy                | 246 us                                                      | 201 us: 1.22x faster                                                        |
| hexiom                  | 4.55 ms                                                     | 3.73 ms: 1.22x faster                                                       |
| scimark_sparse_mat_mult | 2.57 ms                                                     | 2.16 ms: 1.19x faster                                                       |
| json                    | 3.25 ms                                                     | 2.75 ms: 1.19x faster                                                       |
| django_template         | 24.1 ms                                                     | 20.4 ms: 1.18x faster                                                       |
| pyflate                 | 304 ms                                                      | 258 ms: 1.18x faster                                                        |
| scimark_sor             | 75.6 ms                                                     | 64.2 ms: 1.18x faster                                                       |
| chaos                   | 47.1 ms                                                     | 40.1 ms: 1.17x faster                                                       |
| nbody                   | 70.0 ms                                                     | 59.7 ms: 1.17x faster                                                       |
| chameleon               | 5.11 ms                                                     | 4.37 ms: 1.17x faster                                                       |
| mako                    | 7.26 ms                                                     | 6.21 ms: 1.17x faster                                                       |
| pickle_pure_python      | 200 us                                                      | 171 us: 1.17x faster                                                        |
| go                      | 97.3 ms                                                     | 83.7 ms: 1.16x faster                                                       |
| nqueens                 | 64.9 ms                                                     | 55.9 ms: 1.16x faster                                                       |
| regex_compile           | 90.6 ms                                                     | 78.1 ms: 1.16x faster                                                       |
| float                   | 54.6 ms                                                     | 47.2 ms: 1.16x faster                                                       |
| fannkuch                | 252 ms                                                      | 218 ms: 1.16x faster                                                        |
| deepcopy_reduce         | 2.07 us                                                     | 1.80 us: 1.15x faster                                                       |
| genshi_xml              | 37.3 ms                                                     | 33.0 ms: 1.13x faster                                                       |
| spectral_norm           | 67.9 ms                                                     | 60.5 ms: 1.12x faster                                                       |
| scimark_monte_carlo     | 44.6 ms                                                     | 40.2 ms: 1.11x faster                                                       |
| scimark_lu              | 63.5 ms                                                     | 57.6 ms: 1.10x faster                                                       |
| sqlglot_parse           | 952 us                                                      | 863 us: 1.10x faster                                                        |
| sqlglot_transpile       | 1.16 ms                                                     | 1.06 ms: 1.10x faster                                                       |
| pprint_pformat          | 1.04 sec                                                    | 945 ms: 1.10x faster                                                        |
| logging_format          | 7.01 us                                                     | 6.38 us: 1.10x faster                                                       |
| sqlglot_normalize       | 190 ms                                                      | 174 ms: 1.10x faster                                                        |
| pprint_safe_repr        | 512 ms                                                      | 469 ms: 1.09x faster                                                        |
| sympy_expand            | 295 ms                                                      | 271 ms: 1.09x faster                                                        |
| telco                   | 3.90 ms                                                     | 3.61 ms: 1.08x faster                                                       |
| sympy_integrate         | 13.8 ms                                                     | 12.8 ms: 1.08x faster                                                       |
| thrift                  | 491 us                                                      | 456 us: 1.08x faster                                                        |
| sympy_str               | 182 ms                                                      | 169 ms: 1.08x faster                                                        |
| sqlglot_optimize        | 34.9 ms                                                     | 32.5 ms: 1.07x faster                                                       |
| scimark_fft             | 178 ms                                                      | 167 ms: 1.07x faster                                                        |
| comprehensions          | 15.9 us                                                     | 15.0 us: 1.06x faster                                                       |
| meteor_contest          | 74.7 ms                                                     | 70.3 ms: 1.06x faster                                                       |
| coverage                | 55.9 ms                                                     | 52.6 ms: 1.06x faster                                                       |
| logging_simple          | 6.61 us                                                     | 6.23 us: 1.06x faster                                                       |
| mdp                     | 1.67 sec                                                    | 1.57 sec: 1.06x faster                                                      |
| mypy2                   | 229 ms                                                      | 216 ms: 1.06x faster                                                        |
| xml_etree_process       | 37.1 ms                                                     | 35.0 ms: 1.06x faster                                                       |
| pycparser               | 691 ms                                                      | 653 ms: 1.06x faster                                                        |
| crypto_pyaes            | 47.6 ms                                                     | 45.2 ms: 1.05x faster                                                       |
| html5lib                | 37.5 ms                                                     | 35.7 ms: 1.05x faster                                                       |
| xml_etree_generate      | 52.2 ms                                                     | 49.7 ms: 1.05x faster                                                       |
| dulwich_log             | 44.5 ms                                                     | 42.5 ms: 1.05x faster                                                       |
| sympy_sum               | 99.9 ms                                                     | 95.6 ms: 1.04x faster                                                       |
| async_tree_none         | 320 ms                                                      | 308 ms: 1.04x faster                                                        |
| async_generators        | 178 ms                                                      | 171 ms: 1.04x faster                                                        |
| docutils                | 1.60 sec                                                    | 1.55 sec: 1.04x faster                                                      |
| 2to3                    | 209 ms                                                      | 202 ms: 1.03x faster                                                        |
| tornado_http            | 91.8 ms                                                     | 88.8 ms: 1.03x faster                                                       |
| dask                    | 264 ms                                                      | 257 ms: 1.03x faster                                                        |
| regex_v8                | 13.8 ms                                                     | 13.6 ms: 1.02x faster                                                       |
| xml_etree_parse         | 95.9 ms                                                     | 94.7 ms: 1.01x faster                                                       |
| json_loads              | 12.9 us                                                     | 12.8 us: 1.01x faster                                                       |
| xml_etree_iterparse     | 62.6 ms                                                     | 63.3 ms: 1.01x slower                                                       |
| bench_mp_pool           | 62.5 ms                                                     | 63.3 ms: 1.01x slower                                                       |
| create_gc_cycles        | 693 us                                                      | 702 us: 1.01x slower                                                        |
| pickle_list             | 2.68 us                                                     | 2.72 us: 1.01x slower                                                       |
| pidigits                | 148 ms                                                      | 151 ms: 1.02x slower                                                        |
| regex_dna               | 115 ms                                                      | 117 ms: 1.02x slower                                                        |
| python_startup          | 18.7 ms                                                     | 19.2 ms: 1.03x slower                                                       |
| regex_effbot            | 1.50 ms                                                     | 1.54 ms: 1.03x slower                                                       |
| sqlite_synth            | 1.68 us                                                     | 1.74 us: 1.03x slower                                                       |
| gc_traversal            | 1.46 ms                                                     | 1.51 ms: 1.04x slower                                                       |
| python_startup_no_site  | 15.9 ms                                                     | 16.5 ms: 1.04x slower                                                       |
| pathlib                 | 71.4 ms                                                     | 74.8 ms: 1.05x slower                                                       |
| pickle                  | 6.61 us                                                     | 6.94 us: 1.05x slower                                                       |
| unpickle_list           | 2.55 us                                                     | 2.76 us: 1.08x slower                                                       |
| unpickle                | 8.09 us                                                     | 9.15 us: 1.13x slower                                                       |
| Geometric mean          | (ref)                                                       | 1.09x faster                                                                |

Benchmark hidden because not significant (7): async_tree_io, pickle_dict, bench_thread_pool, coroutines, async_tree_cpu_io_mixed, generators, async_tree_memoization
Ignored benchmarks (9) of results/bm-20221024-3.11.0-deaf509/bm-20221024-pythonperf1-amd64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.05x
- 95% likely to have a speedup of 1.05x
- 99% likely to have a speedup of 1.04x
