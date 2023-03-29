
# Results vs. 3.11.0

- fork: python
- ref: b6bd7ffcbc1ffaa68e34
- machine: darwin-arm64
- commit hash: b6bd7ff
- commit date: 2022-12-06
- overall geometric mean: 1.04x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221206-darwin-arm64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                              | 168 ms: 1.04x slower                                                  |
| chameleon      | 4.55 ms                                                             | 4.53 ms: 1.00x faster                                                 |
| docutils       | 1.47 sec                                                            | 1.48 sec: 1.01x slower                                                |
| html5lib       | 34.8 ms                                                             | 36.4 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                               | 1.02x slower                                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221206-darwin-arm64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 65.5 ms                                                             | 65.3 ms: 1.00x faster                                                 |
| pidigits       | 281 ms                                                              | 282 ms: 1.00x slower                                                  |
| float          | 53.0 ms                                                             | 57.9 ms: 1.09x slower                                                 |
| Geometric mean | (ref)                                                               | 1.03x slower                                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221206-darwin-arm64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_v8       | 16.1 ms                                                             | 15.7 ms: 1.02x faster                                                 |
| regex_dna      | 151 ms                                                              | 149 ms: 1.02x faster                                                  |
| regex_effbot   | 2.63 ms                                                             | 2.61 ms: 1.01x faster                                                 |
| regex_compile  | 76.6 ms                                                             | 77.2 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                               | 1.01x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221206-darwin-arm64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|----------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps           | 7.59 ms                                                             | 6.12 ms: 1.24x faster                                                 |
| xml_etree_parse      | 106 ms                                                              | 96.7 ms: 1.09x faster                                                 |
| unpickle_list        | 2.63 us                                                             | 2.57 us: 1.02x faster                                                 |
| xml_etree_iterparse  | 69.2 ms                                                             | 69.6 ms: 1.01x slower                                                 |
| pickle_dict          | 17.9 us                                                             | 18.0 us: 1.01x slower                                                 |
| json_loads           | 16.0 us                                                             | 16.3 us: 1.02x slower                                                 |
| unpickle_pure_python | 158 us                                                              | 161 us: 1.02x slower                                                  |
| xml_etree_process    | 35.0 ms                                                             | 36.3 ms: 1.04x slower                                                 |
| xml_etree_generate   | 48.2 ms                                                             | 50.4 ms: 1.05x slower                                                 |
| pickle               | 7.17 us                                                             | 7.60 us: 1.06x slower                                                 |
| pickle_pure_python   | 198 us                                                              | 214 us: 1.08x slower                                                  |
| Geometric mean       | (ref)                                                               | 1.01x faster                                                          |

Benchmark hidden because not significant (2): unpickle, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221206-darwin-arm64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 12.3 ms                                                             | 12.3 ms: 1.00x faster                                                 |
| python_startup_no_site | 10.1 ms                                                             | 10.2 ms: 1.01x slower                                                 |
| Geometric mean         | (ref)                                                               | 1.01x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221206-darwin-arm64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|-----------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako            | 8.42 ms                                                             | 7.24 ms: 1.16x faster                                                 |
| genshi_text     | 15.3 ms                                                             | 14.7 ms: 1.04x faster                                                 |
| genshi_xml      | 29.9 ms                                                             | 30.4 ms: 1.02x slower                                                 |
| django_template | 21.1 ms                                                             | 21.9 ms: 1.04x slower                                                 |
| Geometric mean  | (ref)                                                               | 1.03x faster                                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221206-darwin-arm64-python-b6bd7ffcbc1ffaa68e34-3.12.0a3-b6bd7ff |
|-------------------------|:-------------------------------------------------------------------:|:---------------------------------------------------------------------:|
| json_dumps              | 7.59 ms                                                             | 6.12 ms: 1.24x faster                                                 |
| mako                    | 8.42 ms                                                             | 7.24 ms: 1.16x faster                                                 |
| scimark_sparse_mat_mult | 3.19 ms                                                             | 2.78 ms: 1.15x faster                                                 |
| xml_etree_parse         | 106 ms                                                              | 96.7 ms: 1.09x faster                                                 |
| logging_silent          | 68.0 ns                                                             | 64.2 ns: 1.06x faster                                                 |
| create_gc_cycles        | 722 us                                                              | 694 us: 1.04x faster                                                  |
| genshi_text             | 15.3 ms                                                             | 14.7 ms: 1.04x faster                                                 |
| regex_v8                | 16.1 ms                                                             | 15.7 ms: 1.02x faster                                                 |
| unpickle_list           | 2.63 us                                                             | 2.57 us: 1.02x faster                                                 |
| scimark_lu              | 72.2 ms                                                             | 70.9 ms: 1.02x faster                                                 |
| regex_dna               | 151 ms                                                              | 149 ms: 1.02x faster                                                  |
| pathlib                 | 28.3 ms                                                             | 27.9 ms: 1.01x faster                                                 |
| scimark_fft             | 200 ms                                                              | 198 ms: 1.01x faster                                                  |
| regex_effbot            | 2.63 ms                                                             | 2.61 ms: 1.01x faster                                                 |
| chameleon               | 4.55 ms                                                             | 4.53 ms: 1.00x faster                                                 |
| nbody                   | 65.5 ms                                                             | 65.3 ms: 1.00x faster                                                 |
| python_startup          | 12.3 ms                                                             | 12.3 ms: 1.00x faster                                                 |
| gc_traversal            | 2.41 ms                                                             | 2.41 ms: 1.00x slower                                                 |
| telco                   | 3.40 ms                                                             | 3.41 ms: 1.00x slower                                                 |
| pidigits                | 281 ms                                                              | 282 ms: 1.00x slower                                                  |
| xml_etree_iterparse     | 69.2 ms                                                             | 69.6 ms: 1.01x slower                                                 |
| pickle_dict             | 17.9 us                                                             | 18.0 us: 1.01x slower                                                 |
| regex_compile           | 76.6 ms                                                             | 77.2 ms: 1.01x slower                                                 |
| docutils                | 1.47 sec                                                            | 1.48 sec: 1.01x slower                                                |
| pycparser               | 695 ms                                                              | 704 ms: 1.01x slower                                                  |
| deltablue               | 2.81 ms                                                             | 2.85 ms: 1.01x slower                                                 |
| python_startup_no_site  | 10.1 ms                                                             | 10.2 ms: 1.01x slower                                                 |
| json                    | 2.77 ms                                                             | 2.82 ms: 1.01x slower                                                 |
| json_loads              | 16.0 us                                                             | 16.3 us: 1.02x slower                                                 |
| dask                    | 226 ms                                                              | 230 ms: 1.02x slower                                                  |
| bench_mp_pool           | 43.8 ms                                                             | 44.6 ms: 1.02x slower                                                 |
| genshi_xml              | 29.9 ms                                                             | 30.4 ms: 1.02x slower                                                 |
| unpickle_pure_python    | 158 us                                                              | 161 us: 1.02x slower                                                  |
| sympy_sum               | 86.0 ms                                                             | 87.9 ms: 1.02x slower                                                 |
| dulwich_log             | 29.7 ms                                                             | 30.5 ms: 1.03x slower                                                 |
| spectral_norm           | 72.5 ms                                                             | 74.4 ms: 1.03x slower                                                 |
| sqlglot_normalize       | 171 ms                                                              | 176 ms: 1.03x slower                                                  |
| sqlglot_optimize        | 31.2 ms                                                             | 32.1 ms: 1.03x slower                                                 |
| sympy_expand            | 243 ms                                                              | 251 ms: 1.03x slower                                                  |
| sympy_str               | 151 ms                                                              | 157 ms: 1.03x slower                                                  |
| thrift                  | 431 us                                                              | 447 us: 1.04x slower                                                  |
| xml_etree_process       | 35.0 ms                                                             | 36.3 ms: 1.04x slower                                                 |
| django_template         | 21.1 ms                                                             | 21.9 ms: 1.04x slower                                                 |
| 2to3                    | 161 ms                                                              | 168 ms: 1.04x slower                                                  |
| coverage                | 58.4 ms                                                             | 60.7 ms: 1.04x slower                                                 |
| async_tree_cpu_io_mixed | 534 ms                                                              | 556 ms: 1.04x slower                                                  |
| async_tree_none         | 285 ms                                                              | 297 ms: 1.04x slower                                                  |
| chaos                   | 49.4 ms                                                             | 51.5 ms: 1.04x slower                                                 |
| crypto_pyaes            | 51.8 ms                                                             | 54.2 ms: 1.04x slower                                                 |
| sympy_integrate         | 11.5 ms                                                             | 12.0 ms: 1.05x slower                                                 |
| html5lib                | 34.8 ms                                                             | 36.4 ms: 1.05x slower                                                 |
| xml_etree_generate      | 48.2 ms                                                             | 50.4 ms: 1.05x slower                                                 |
| fannkuch                | 260 ms                                                              | 273 ms: 1.05x slower                                                  |
| sqlglot_parse           | 956 us                                                              | 1.00 ms: 1.05x slower                                                 |
| logging_format          | 3.77 us                                                             | 3.96 us: 1.05x slower                                                 |
| logging_simple          | 3.49 us                                                             | 3.68 us: 1.05x slower                                                 |
| hexiom                  | 4.73 ms                                                             | 5.01 ms: 1.06x slower                                                 |
| pickle                  | 7.17 us                                                             | 7.60 us: 1.06x slower                                                 |
| async_generators        | 195 ms                                                              | 207 ms: 1.06x slower                                                  |
| sqlglot_transpile       | 1.12 ms                                                             | 1.19 ms: 1.06x slower                                                 |
| async_tree_io           | 707 ms                                                              | 756 ms: 1.07x slower                                                  |
| raytrace                | 207 ms                                                              | 222 ms: 1.07x slower                                                  |
| meteor_contest          | 73.3 ms                                                             | 78.6 ms: 1.07x slower                                                 |
| mdp                     | 1.54 sec                                                            | 1.66 sec: 1.08x slower                                                |
| pickle_pure_python      | 198 us                                                              | 214 us: 1.08x slower                                                  |
| pprint_safe_repr        | 463 ms                                                              | 502 ms: 1.08x slower                                                  |
| go                      | 109 ms                                                              | 118 ms: 1.09x slower                                                  |
| pprint_pformat          | 946 ms                                                              | 1.03 sec: 1.09x slower                                                |
| sqlite_synth            | 1.28 us                                                             | 1.40 us: 1.09x slower                                                 |
| float                   | 53.0 ms                                                             | 57.9 ms: 1.09x slower                                                 |
| comprehensions          | 16.1 us                                                             | 17.8 us: 1.11x slower                                                 |
| coroutines              | 17.7 ms                                                             | 19.9 ms: 1.12x slower                                                 |
| deepcopy                | 224 us                                                              | 253 us: 1.13x slower                                                  |
| pyflate                 | 309 ms                                                              | 352 ms: 1.14x slower                                                  |
| deepcopy_reduce         | 1.91 us                                                             | 2.17 us: 1.14x slower                                                 |
| generators              | 28.6 ms                                                             | 33.6 ms: 1.18x slower                                                 |
| deepcopy_memo           | 26.3 us                                                             | 31.0 us: 1.18x slower                                                 |
| scimark_monte_carlo     | 46.5 ms                                                             | 56.2 ms: 1.21x slower                                                 |
| scimark_sor             | 82.9 ms                                                             | 104 ms: 1.25x slower                                                  |
| unpack_sequence         | 33.5 ns                                                             | 52.7 ns: 1.57x slower                                                 |
| Geometric mean          | (ref)                                                               | 1.04x slower                                                          |

Benchmark hidden because not significant (8): async_tree_memoization, nqueens, unpickle, richards, bench_thread_pool, pickle_list, asyncio_tcp, mypy2
Ignored benchmarks (7) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative, tornado_http
