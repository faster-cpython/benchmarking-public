
# Results vs. base

- fork: faster-cpython
- ref: no_predict
- machine: windows-amd64
- commit hash: ed869aa
- commit date: 2023-03-23
- overall geometric mean: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 | bm-20230323-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a6+-ed869aa |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 194 ms                                                                      | 196 ms: 1.01x slower                                                        |
| chameleon      | 4.30 ms                                                                     | 4.54 ms: 1.05x slower                                                       |
| docutils       | 1.51 sec                                                                    | 1.52 sec: 1.01x slower                                                      |
| html5lib       | 35.5 ms                                                                     | 35.8 ms: 1.01x slower                                                       |
| Geometric mean | (ref)                                                                       | 1.02x slower                                                                |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 | bm-20230323-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a6+-ed869aa |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| pidigits       | 146 ms                                                                      | 145 ms: 1.01x faster                                                        |
| nbody          | 55.6 ms                                                                     | 56.6 ms: 1.02x slower                                                       |
| float          | 46.0 ms                                                                     | 47.2 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                                       | 1.01x slower                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 | bm-20230323-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a6+-ed869aa |
|----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 1.83 ms                                                                     | 1.70 ms: 1.08x faster                                                       |
| regex_v8       | 13.8 ms                                                                     | 13.5 ms: 1.03x faster                                                       |
| regex_dna      | 122 ms                                                                      | 121 ms: 1.01x faster                                                        |
| regex_compile  | 79.6 ms                                                                     | 82.3 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                                       | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 | bm-20230323-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a6+-ed869aa |
|----------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 5.44 ms                                                                     | 5.41 ms: 1.00x faster                                                       |
| json_loads           | 13.4 us                                                                     | 13.5 us: 1.01x slower                                                       |
| unpickle_list        | 2.70 us                                                                     | 2.72 us: 1.01x slower                                                       |
| unpickle             | 7.96 us                                                                     | 8.01 us: 1.01x slower                                                       |
| pickle               | 6.65 us                                                                     | 6.78 us: 1.02x slower                                                       |
| xml_etree_parse      | 87.3 ms                                                                     | 90.4 ms: 1.04x slower                                                       |
| xml_etree_generate   | 50.0 ms                                                                     | 51.8 ms: 1.04x slower                                                       |
| pickle_pure_python   | 168 us                                                                      | 175 us: 1.04x slower                                                        |
| xml_etree_iterparse  | 59.2 ms                                                                     | 61.7 ms: 1.04x slower                                                       |
| xml_etree_process    | 33.9 ms                                                                     | 35.7 ms: 1.05x slower                                                       |
| unpickle_pure_python | 117 us                                                                      | 127 us: 1.09x slower                                                        |
| Geometric mean       | (ref)                                                                       | 1.03x slower                                                                |

Benchmark hidden because not significant (2): pickle_dict, pickle_list

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup, python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 | bm-20230323-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a6+-ed869aa |
|-----------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_text     | 13.8 ms                                                                     | 13.5 ms: 1.02x faster                                                       |
| mako            | 6.10 ms                                                                     | 6.21 ms: 1.02x slower                                                       |
| django_template | 19.9 ms                                                                     | 20.5 ms: 1.03x slower                                                       |
| Geometric mean  | (ref)                                                                       | 1.01x slower                                                                |

Benchmark hidden because not significant (1): genshi_xml

All benchmarks:
===============

| Benchmark               | bm-20230324-pythonperf1-amd64-python-d49409196e0c73c38e3f-3.12.0a6+-d494091 | bm-20230323-pythonperf1-amd64-faster%2dcpython-no_predict-3.12.0a6+-ed869aa |
|-------------------------|:---------------------------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot            | 1.83 ms                                                                     | 1.70 ms: 1.08x faster                                                       |
| regex_v8                | 13.8 ms                                                                     | 13.5 ms: 1.03x faster                                                       |
| genshi_text             | 13.8 ms                                                                     | 13.5 ms: 1.02x faster                                                       |
| telco                   | 3.85 ms                                                                     | 3.80 ms: 1.01x faster                                                       |
| regex_dna               | 122 ms                                                                      | 121 ms: 1.01x faster                                                        |
| gc_traversal            | 1.47 ms                                                                     | 1.46 ms: 1.01x faster                                                       |
| pidigits                | 146 ms                                                                      | 145 ms: 1.01x faster                                                        |
| meteor_contest          | 70.4 ms                                                                     | 69.8 ms: 1.01x faster                                                       |
| bench_mp_pool           | 64.8 ms                                                                     | 64.5 ms: 1.00x faster                                                       |
| json_dumps              | 5.44 ms                                                                     | 5.41 ms: 1.00x faster                                                       |
| sympy_integrate         | 12.8 ms                                                                     | 12.8 ms: 1.00x faster                                                       |
| pathlib                 | 82.2 ms                                                                     | 82.7 ms: 1.01x slower                                                       |
| json_loads              | 13.4 us                                                                     | 13.5 us: 1.01x slower                                                       |
| unpickle_list           | 2.70 us                                                                     | 2.72 us: 1.01x slower                                                       |
| unpickle                | 7.96 us                                                                     | 8.01 us: 1.01x slower                                                       |
| html5lib                | 35.5 ms                                                                     | 35.8 ms: 1.01x slower                                                       |
| sympy_sum               | 95.6 ms                                                                     | 96.3 ms: 1.01x slower                                                       |
| logging_format          | 6.41 us                                                                     | 6.46 us: 1.01x slower                                                       |
| sympy_str               | 169 ms                                                                      | 171 ms: 1.01x slower                                                        |
| mypy2                   | 209 ms                                                                      | 211 ms: 1.01x slower                                                        |
| sqlite_synth            | 1.76 us                                                                     | 1.78 us: 1.01x slower                                                       |
| docutils                | 1.51 sec                                                                    | 1.52 sec: 1.01x slower                                                      |
| bench_thread_pool       | 818 us                                                                      | 825 us: 1.01x slower                                                        |
| async_tree_cpu_io_mixed | 473 ms                                                                      | 478 ms: 1.01x slower                                                        |
| 2to3                    | 194 ms                                                                      | 196 ms: 1.01x slower                                                        |
| generators              | 20.9 ms                                                                     | 21.2 ms: 1.01x slower                                                       |
| sqlglot_normalize       | 166 ms                                                                      | 168 ms: 1.02x slower                                                        |
| nbody                   | 55.6 ms                                                                     | 56.6 ms: 1.02x slower                                                       |
| async_tree_io           | 723 ms                                                                      | 736 ms: 1.02x slower                                                        |
| pycparser               | 640 ms                                                                      | 653 ms: 1.02x slower                                                        |
| pickle                  | 6.65 us                                                                     | 6.78 us: 1.02x slower                                                       |
| mako                    | 6.10 ms                                                                     | 6.21 ms: 1.02x slower                                                       |
| sqlglot_optimize        | 30.8 ms                                                                     | 31.4 ms: 1.02x slower                                                       |
| deepcopy_reduce         | 1.82 us                                                                     | 1.86 us: 1.02x slower                                                       |
| crypto_pyaes            | 44.3 ms                                                                     | 45.2 ms: 1.02x slower                                                       |
| unpack_sequence         | 27.4 ns                                                                     | 28.1 ns: 1.03x slower                                                       |
| sqlglot_transpile       | 1.03 ms                                                                     | 1.06 ms: 1.03x slower                                                       |
| float                   | 46.0 ms                                                                     | 47.2 ms: 1.03x slower                                                       |
| dulwich_log             | 42.1 ms                                                                     | 43.2 ms: 1.03x slower                                                       |
| async_generators        | 202 ms                                                                      | 208 ms: 1.03x slower                                                        |
| django_template         | 19.9 ms                                                                     | 20.5 ms: 1.03x slower                                                       |
| coroutines              | 13.9 ms                                                                     | 14.3 ms: 1.03x slower                                                       |
| comprehensions          | 14.8 us                                                                     | 15.2 us: 1.03x slower                                                       |
| logging_simple          | 5.91 us                                                                     | 6.10 us: 1.03x slower                                                       |
| sqlglot_parse           | 843 us                                                                      | 871 us: 1.03x slower                                                        |
| regex_compile           | 79.6 ms                                                                     | 82.3 ms: 1.03x slower                                                       |
| xml_etree_parse         | 87.3 ms                                                                     | 90.4 ms: 1.04x slower                                                       |
| deltablue               | 1.91 ms                                                                     | 1.98 ms: 1.04x slower                                                       |
| xml_etree_generate      | 50.0 ms                                                                     | 51.8 ms: 1.04x slower                                                       |
| pickle_pure_python      | 168 us                                                                      | 175 us: 1.04x slower                                                        |
| pprint_pformat          | 902 ms                                                                      | 936 ms: 1.04x slower                                                        |
| pyflate                 | 271 ms                                                                      | 282 ms: 1.04x slower                                                        |
| chaos                   | 39.6 ms                                                                     | 41.2 ms: 1.04x slower                                                       |
| spectral_norm           | 61.1 ms                                                                     | 63.6 ms: 1.04x slower                                                       |
| xml_etree_iterparse     | 59.2 ms                                                                     | 61.7 ms: 1.04x slower                                                       |
| pprint_safe_repr        | 443 ms                                                                      | 462 ms: 1.04x slower                                                        |
| scimark_monte_carlo     | 39.3 ms                                                                     | 41.1 ms: 1.04x slower                                                       |
| fannkuch                | 222 ms                                                                      | 233 ms: 1.05x slower                                                        |
| raytrace                | 164 ms                                                                      | 172 ms: 1.05x slower                                                        |
| deepcopy                | 204 us                                                                      | 215 us: 1.05x slower                                                        |
| scimark_fft             | 159 ms                                                                      | 167 ms: 1.05x slower                                                        |
| scimark_sparse_mat_mult | 2.20 ms                                                                     | 2.32 ms: 1.05x slower                                                       |
| chameleon               | 4.30 ms                                                                     | 4.54 ms: 1.05x slower                                                       |
| xml_etree_process       | 33.9 ms                                                                     | 35.7 ms: 1.05x slower                                                       |
| coverage                | 50.1 ms                                                                     | 52.9 ms: 1.06x slower                                                       |
| logging_silent          | 54.5 ns                                                                     | 57.7 ns: 1.06x slower                                                       |
| scimark_sor             | 70.6 ms                                                                     | 74.8 ms: 1.06x slower                                                       |
| nqueens                 | 54.1 ms                                                                     | 57.5 ms: 1.06x slower                                                       |
| hexiom                  | 3.66 ms                                                                     | 3.90 ms: 1.06x slower                                                       |
| mdp                     | 1.36 sec                                                                    | 1.44 sec: 1.06x slower                                                      |
| scimark_lu              | 50.5 ms                                                                     | 54.4 ms: 1.08x slower                                                       |
| go                      | 80.6 ms                                                                     | 87.3 ms: 1.08x slower                                                       |
| unpickle_pure_python    | 117 us                                                                      | 127 us: 1.09x slower                                                        |
| richards                | 24.3 ms                                                                     | 26.7 ms: 1.10x slower                                                       |
| deepcopy_memo           | 19.6 us                                                                     | 21.9 us: 1.11x slower                                                       |
| Geometric mean          | (ref)                                                                       | 1.02x slower                                                                |

Benchmark hidden because not significant (14): thrift, json, sympy_expand, python_startup, genshi_xml, create_gc_cycles, pickle_dict, asyncio_tcp, async_tree_none, python_startup_no_site, tornado_http, dask, async_tree_memoization, pickle_list
