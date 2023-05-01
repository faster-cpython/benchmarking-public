
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 2d526cd
- commit date: 2023-05-01
- overall geometric mean: 1.04x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230501-darwin-arm64-python-main-3.12.0a7+-2d526cd |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 161 ms                                                              | 173 ms: 1.07x slower                                   |
| docutils       | 1.47 sec                                                            | 1.56 sec: 1.06x slower                                 |
| html5lib       | 34.8 ms                                                             | 37.2 ms: 1.07x slower                                  |
| Geometric mean | (ref)                                                               | 1.04x slower                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230501-darwin-arm64-python-main-3.12.0a7+-2d526cd |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 65.5 ms                                                             | 69.7 ms: 1.06x slower                                  |
| float          | 53.0 ms                                                             | 58.1 ms: 1.10x slower                                  |
| Geometric mean | (ref)                                                               | 1.05x slower                                           |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230501-darwin-arm64-python-main-3.12.0a7+-2d526cd |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| regex_dna      | 151 ms                                                              | 149 ms: 1.01x faster                                   |
| regex_compile  | 76.6 ms                                                             | 77.6 ms: 1.01x slower                                  |
| regex_v8       | 16.1 ms                                                             | 16.3 ms: 1.01x slower                                  |
| regex_effbot   | 2.63 ms                                                             | 2.69 ms: 1.02x slower                                  |
| Geometric mean | (ref)                                                               | 1.01x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230501-darwin-arm64-python-main-3.12.0a7+-2d526cd |
|----------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 7.59 ms                                                             | 6.84 ms: 1.11x faster                                  |
| unpickle_pure_python | 158 us                                                              | 151 us: 1.05x faster                                   |
| pickle_pure_python   | 198 us                                                              | 194 us: 1.02x faster                                   |
| xml_etree_parse      | 106 ms                                                              | 109 ms: 1.03x slower                                   |
| unpickle             | 9.66 us                                                             | 10.2 us: 1.05x slower                                  |
| pickle_dict          | 17.9 us                                                             | 19.0 us: 1.06x slower                                  |
| xml_etree_iterparse  | 69.2 ms                                                             | 74.2 ms: 1.07x slower                                  |
| pickle               | 7.17 us                                                             | 7.83 us: 1.09x slower                                  |
| json_loads           | 16.0 us                                                             | 17.7 us: 1.10x slower                                  |
| pickle_list          | 2.83 us                                                             | 3.13 us: 1.11x slower                                  |
| xml_etree_process    | 35.0 ms                                                             | 39.8 ms: 1.14x slower                                  |
| xml_etree_generate   | 48.2 ms                                                             | 57.7 ms: 1.20x slower                                  |
| unpickle_list        | 2.63 us                                                             | 3.16 us: 1.20x slower                                  |
| Geometric mean       | (ref)                                                               | 1.06x slower                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230501-darwin-arm64-python-main-3.12.0a7+-2d526cd |
|------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 12.3 ms                                                             | 12.5 ms: 1.01x slower                                  |
| python_startup_no_site | 10.1 ms                                                             | 10.4 ms: 1.03x slower                                  |
| Geometric mean         | (ref)                                                               | 1.02x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230501-darwin-arm64-python-main-3.12.0a7+-2d526cd |
|----------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| mako           | 8.42 ms                                                             | 7.80 ms: 1.08x faster                                  |
| genshi_text    | 15.3 ms                                                             | 15.0 ms: 1.02x faster                                  |
| genshi_xml     | 29.9 ms                                                             | 30.9 ms: 1.03x slower                                  |
| Geometric mean | (ref)                                                               | 1.02x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20230501-darwin-arm64-python-main-3.12.0a7+-2d526cd |
|-------------------------|:-------------------------------------------------------------------:|:------------------------------------------------------:|
| asyncio_tcp             | 651 ms                                                              | 449 ms: 1.45x faster                                   |
| unpack_sequence         | 33.5 ns                                                             | 28.1 ns: 1.19x faster                                  |
| generators              | 28.6 ms                                                             | 25.0 ms: 1.14x faster                                  |
| deltablue               | 2.81 ms                                                             | 2.47 ms: 1.14x faster                                  |
| json_dumps              | 7.59 ms                                                             | 6.84 ms: 1.11x faster                                  |
| hexiom                  | 4.73 ms                                                             | 4.32 ms: 1.10x faster                                  |
| mako                    | 8.42 ms                                                             | 7.80 ms: 1.08x faster                                  |
| sqlglot_parse           | 956 us                                                              | 897 us: 1.07x faster                                   |
| unpickle_pure_python    | 158 us                                                              | 151 us: 1.05x faster                                   |
| sqlglot_transpile       | 1.12 ms                                                             | 1.07 ms: 1.04x faster                                  |
| create_gc_cycles        | 722 us                                                              | 698 us: 1.03x faster                                   |
| genshi_text             | 15.3 ms                                                             | 15.0 ms: 1.02x faster                                  |
| pickle_pure_python      | 198 us                                                              | 194 us: 1.02x faster                                   |
| chaos                   | 49.4 ms                                                             | 48.4 ms: 1.02x faster                                  |
| pathlib                 | 28.3 ms                                                             | 27.8 ms: 1.02x faster                                  |
| richards                | 32.2 ms                                                             | 31.6 ms: 1.02x faster                                  |
| coverage                | 58.4 ms                                                             | 57.4 ms: 1.02x faster                                  |
| regex_dna               | 151 ms                                                              | 149 ms: 1.01x faster                                   |
| async_tree_none         | 285 ms                                                              | 281 ms: 1.01x faster                                   |
| go                      | 109 ms                                                              | 109 ms: 1.00x faster                                   |
| gc_traversal            | 2.41 ms                                                             | 2.42 ms: 1.00x slower                                  |
| sqlalchemy_imperative   | 7.26 ms                                                             | 7.33 ms: 1.01x slower                                  |
| regex_compile           | 76.6 ms                                                             | 77.6 ms: 1.01x slower                                  |
| python_startup          | 12.3 ms                                                             | 12.5 ms: 1.01x slower                                  |
| regex_v8                | 16.1 ms                                                             | 16.3 ms: 1.01x slower                                  |
| mdp                     | 1.54 sec                                                            | 1.57 sec: 1.02x slower                                 |
| coroutines              | 17.7 ms                                                             | 18.0 ms: 1.02x slower                                  |
| regex_effbot            | 2.63 ms                                                             | 2.69 ms: 1.02x slower                                  |
| scimark_sparse_mat_mult | 3.19 ms                                                             | 3.27 ms: 1.02x slower                                  |
| dulwich_log             | 29.7 ms                                                             | 30.5 ms: 1.03x slower                                  |
| xml_etree_parse         | 106 ms                                                              | 109 ms: 1.03x slower                                   |
| python_startup_no_site  | 10.1 ms                                                             | 10.4 ms: 1.03x slower                                  |
| genshi_xml              | 29.9 ms                                                             | 30.9 ms: 1.03x slower                                  |
| scimark_fft             | 200 ms                                                              | 207 ms: 1.03x slower                                   |
| scimark_sor             | 82.9 ms                                                             | 86.0 ms: 1.04x slower                                  |
| logging_silent          | 68.0 ns                                                             | 70.8 ns: 1.04x slower                                  |
| unpickle                | 9.66 us                                                             | 10.2 us: 1.05x slower                                  |
| bench_thread_pool       | 474 us                                                              | 498 us: 1.05x slower                                   |
| meteor_contest          | 73.3 ms                                                             | 77.4 ms: 1.06x slower                                  |
| logging_format          | 3.77 us                                                             | 3.98 us: 1.06x slower                                  |
| logging_simple          | 3.49 us                                                             | 3.70 us: 1.06x slower                                  |
| docutils                | 1.47 sec                                                            | 1.56 sec: 1.06x slower                                 |
| pickle_dict             | 17.9 us                                                             | 19.0 us: 1.06x slower                                  |
| spectral_norm           | 72.5 ms                                                             | 77.2 ms: 1.06x slower                                  |
| nbody                   | 65.5 ms                                                             | 69.7 ms: 1.06x slower                                  |
| deepcopy                | 224 us                                                              | 238 us: 1.07x slower                                   |
| html5lib                | 34.8 ms                                                             | 37.2 ms: 1.07x slower                                  |
| fannkuch                | 260 ms                                                              | 278 ms: 1.07x slower                                   |
| 2to3                    | 161 ms                                                              | 173 ms: 1.07x slower                                   |
| scimark_lu              | 72.2 ms                                                             | 77.3 ms: 1.07x slower                                  |
| xml_etree_iterparse     | 69.2 ms                                                             | 74.2 ms: 1.07x slower                                  |
| crypto_pyaes            | 51.8 ms                                                             | 56.0 ms: 1.08x slower                                  |
| pprint_pformat          | 946 ms                                                              | 1.02 sec: 1.08x slower                                 |
| sqlalchemy_declarative  | 62.6 ms                                                             | 68.0 ms: 1.09x slower                                  |
| json                    | 2.77 ms                                                             | 3.02 ms: 1.09x slower                                  |
| pickle                  | 7.17 us                                                             | 7.83 us: 1.09x slower                                  |
| float                   | 53.0 ms                                                             | 58.1 ms: 1.10x slower                                  |
| pprint_safe_repr        | 463 ms                                                              | 509 ms: 1.10x slower                                   |
| json_loads              | 16.0 us                                                             | 17.7 us: 1.10x slower                                  |
| pyflate                 | 309 ms                                                              | 342 ms: 1.11x slower                                   |
| pickle_list             | 2.83 us                                                             | 3.13 us: 1.11x slower                                  |
| scimark_monte_carlo     | 46.5 ms                                                             | 51.5 ms: 1.11x slower                                  |
| bench_mp_pool           | 43.8 ms                                                             | 48.6 ms: 1.11x slower                                  |
| deepcopy_reduce         | 1.91 us                                                             | 2.13 us: 1.11x slower                                  |
| comprehensions          | 16.1 us                                                             | 18.0 us: 1.12x slower                                  |
| xml_etree_process       | 35.0 ms                                                             | 39.8 ms: 1.14x slower                                  |
| sqlglot_normalize       | 171 ms                                                              | 196 ms: 1.15x slower                                   |
| sqlglot_optimize        | 31.2 ms                                                             | 35.8 ms: 1.15x slower                                  |
| telco                   | 3.40 ms                                                             | 3.92 ms: 1.15x slower                                  |
| thrift                  | 431 us                                                              | 513 us: 1.19x slower                                   |
| xml_etree_generate      | 48.2 ms                                                             | 57.7 ms: 1.20x slower                                  |
| unpickle_list           | 2.63 us                                                             | 3.16 us: 1.20x slower                                  |
| raytrace                | 207 ms                                                              | 248 ms: 1.20x slower                                   |
| sqlite_synth            | 1.28 us                                                             | 1.59 us: 1.24x slower                                  |
| dask                    | 226 ms                                                              | 329 ms: 1.46x slower                                   |
| async_generators        | 195 ms                                                              | 311 ms: 1.60x slower                                   |
| Geometric mean          | (ref)                                                               | 1.04x slower                                           |

Benchmark hidden because not significant (9): tornado_http, async_tree_memoization, deepcopy_memo, async_tree_cpu_io_mixed, pidigits, pycparser, async_tree_io, nqueens, mypy2
Ignored benchmarks (10) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, chameleon, django_template, flaskblogging, gunicorn, pylint, sympy_expand, sympy_integrate, sympy_str, sympy_sum
