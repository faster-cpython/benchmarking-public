
# Results vs. 3.11.0

- fork: python
- ref: 594de165bf2f21d6b28e
- machine: darwin-arm64
- commit hash: 594de16
- commit date: 2022-11-28
- overall geometric mean: 1.03x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221128-darwin-arm64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 161 ms                                                              | 166 ms: 1.03x slower                                                   |
| chameleon      | 4.55 ms                                                             | 4.49 ms: 1.01x faster                                                  |
| docutils       | 1.47 sec                                                            | 1.47 sec: 1.00x slower                                                 |
| html5lib       | 34.8 ms                                                             | 36.2 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                               | 1.01x slower                                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221128-darwin-arm64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 65.5 ms                                                             | 64.7 ms: 1.01x faster                                                  |
| pidigits       | 281 ms                                                              | 281 ms: 1.00x slower                                                   |
| float          | 53.0 ms                                                             | 56.9 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                               | 1.02x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221128-darwin-arm64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 16.1 ms                                                             | 15.7 ms: 1.03x faster                                                  |
| regex_dna      | 151 ms                                                              | 149 ms: 1.01x faster                                                   |
| regex_compile  | 76.6 ms                                                             | 75.9 ms: 1.01x faster                                                  |
| regex_effbot   | 2.63 ms                                                             | 2.61 ms: 1.01x faster                                                  |
| Geometric mean | (ref)                                                               | 1.01x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221128-darwin-arm64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 7.59 ms                                                             | 6.08 ms: 1.25x faster                                                  |
| xml_etree_parse      | 106 ms                                                              | 96.2 ms: 1.10x faster                                                  |
| unpickle_list        | 2.63 us                                                             | 2.57 us: 1.02x faster                                                  |
| pickle_list          | 2.83 us                                                             | 2.81 us: 1.00x faster                                                  |
| pickle_dict          | 17.9 us                                                             | 17.8 us: 1.00x faster                                                  |
| xml_etree_process    | 35.0 ms                                                             | 35.4 ms: 1.01x slower                                                  |
| xml_etree_generate   | 48.2 ms                                                             | 48.7 ms: 1.01x slower                                                  |
| unpickle             | 9.66 us                                                             | 9.81 us: 1.02x slower                                                  |
| json_loads           | 16.0 us                                                             | 16.3 us: 1.02x slower                                                  |
| unpickle_pure_python | 158 us                                                              | 162 us: 1.02x slower                                                   |
| pickle               | 7.17 us                                                             | 7.61 us: 1.06x slower                                                  |
| pickle_pure_python   | 198 us                                                              | 212 us: 1.07x slower                                                   |
| Geometric mean       | (ref)                                                               | 1.01x faster                                                           |

Benchmark hidden because not significant (1): xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221128-darwin-arm64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.3 ms                                                             | 12.2 ms: 1.01x faster                                                  |
| python_startup_no_site | 10.1 ms                                                             | 10.2 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                               | 1.00x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221128-darwin-arm64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|-----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 8.42 ms                                                             | 7.31 ms: 1.15x faster                                                  |
| genshi_text     | 15.3 ms                                                             | 14.6 ms: 1.05x faster                                                  |
| genshi_xml      | 29.9 ms                                                             | 29.3 ms: 1.02x faster                                                  |
| django_template | 21.1 ms                                                             | 21.4 ms: 1.02x slower                                                  |
| Geometric mean  | (ref)                                                               | 1.05x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221128-darwin-arm64-python-594de165bf2f21d6b28e-3.12.0a2+-594de16 |
|-------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps              | 7.59 ms                                                             | 6.08 ms: 1.25x faster                                                  |
| scimark_sparse_mat_mult | 3.19 ms                                                             | 2.77 ms: 1.15x faster                                                  |
| mako                    | 8.42 ms                                                             | 7.31 ms: 1.15x faster                                                  |
| xml_etree_parse         | 106 ms                                                              | 96.2 ms: 1.10x faster                                                  |
| pathlib                 | 28.3 ms                                                             | 26.9 ms: 1.05x faster                                                  |
| genshi_text             | 15.3 ms                                                             | 14.6 ms: 1.05x faster                                                  |
| logging_silent          | 68.0 ns                                                             | 64.9 ns: 1.05x faster                                                  |
| create_gc_cycles        | 722 us                                                              | 698 us: 1.04x faster                                                   |
| regex_v8                | 16.1 ms                                                             | 15.7 ms: 1.03x faster                                                  |
| async_tree_memoization  | 338 ms                                                              | 329 ms: 1.03x faster                                                   |
| unpickle_list           | 2.63 us                                                             | 2.57 us: 1.02x faster                                                  |
| genshi_xml              | 29.9 ms                                                             | 29.3 ms: 1.02x faster                                                  |
| scimark_lu              | 72.2 ms                                                             | 71.1 ms: 1.01x faster                                                  |
| coverage                | 58.4 ms                                                             | 57.5 ms: 1.01x faster                                                  |
| regex_dna               | 151 ms                                                              | 149 ms: 1.01x faster                                                   |
| chameleon               | 4.55 ms                                                             | 4.49 ms: 1.01x faster                                                  |
| scimark_fft             | 200 ms                                                              | 198 ms: 1.01x faster                                                   |
| nbody                   | 65.5 ms                                                             | 64.7 ms: 1.01x faster                                                  |
| regex_compile           | 76.6 ms                                                             | 75.9 ms: 1.01x faster                                                  |
| deltablue               | 2.81 ms                                                             | 2.79 ms: 1.01x faster                                                  |
| python_startup          | 12.3 ms                                                             | 12.2 ms: 1.01x faster                                                  |
| regex_effbot            | 2.63 ms                                                             | 2.61 ms: 1.01x faster                                                  |
| pickle_list             | 2.83 us                                                             | 2.81 us: 1.00x faster                                                  |
| bench_thread_pool       | 474 us                                                              | 472 us: 1.00x faster                                                   |
| pickle_dict             | 17.9 us                                                             | 17.8 us: 1.00x faster                                                  |
| gc_traversal            | 2.41 ms                                                             | 2.42 ms: 1.00x slower                                                  |
| docutils                | 1.47 sec                                                            | 1.47 sec: 1.00x slower                                                 |
| pidigits                | 281 ms                                                              | 281 ms: 1.00x slower                                                   |
| telco                   | 3.40 ms                                                             | 3.41 ms: 1.00x slower                                                  |
| xml_etree_process       | 35.0 ms                                                             | 35.4 ms: 1.01x slower                                                  |
| sympy_sum               | 86.0 ms                                                             | 86.9 ms: 1.01x slower                                                  |
| json                    | 2.77 ms                                                             | 2.81 ms: 1.01x slower                                                  |
| xml_etree_generate      | 48.2 ms                                                             | 48.7 ms: 1.01x slower                                                  |
| python_startup_no_site  | 10.1 ms                                                             | 10.2 ms: 1.01x slower                                                  |
| unpickle                | 9.66 us                                                             | 9.81 us: 1.02x slower                                                  |
| json_loads              | 16.0 us                                                             | 16.3 us: 1.02x slower                                                  |
| django_template         | 21.1 ms                                                             | 21.4 ms: 1.02x slower                                                  |
| spectral_norm           | 72.5 ms                                                             | 73.7 ms: 1.02x slower                                                  |
| dulwich_log             | 29.7 ms                                                             | 30.2 ms: 1.02x slower                                                  |
| sqlglot_normalize       | 171 ms                                                              | 174 ms: 1.02x slower                                                   |
| async_tree_none         | 285 ms                                                              | 289 ms: 1.02x slower                                                   |
| sympy_expand            | 243 ms                                                              | 248 ms: 1.02x slower                                                   |
| sqlglot_optimize        | 31.2 ms                                                             | 31.8 ms: 1.02x slower                                                  |
| sympy_str               | 151 ms                                                              | 155 ms: 1.02x slower                                                   |
| thrift                  | 431 us                                                              | 440 us: 1.02x slower                                                   |
| unpickle_pure_python    | 158 us                                                              | 162 us: 1.02x slower                                                   |
| sympy_integrate         | 11.5 ms                                                             | 11.8 ms: 1.02x slower                                                  |
| logging_simple          | 3.49 us                                                             | 3.59 us: 1.03x slower                                                  |
| 2to3                    | 161 ms                                                              | 166 ms: 1.03x slower                                                   |
| chaos                   | 49.4 ms                                                             | 50.9 ms: 1.03x slower                                                  |
| crypto_pyaes            | 51.8 ms                                                             | 53.5 ms: 1.03x slower                                                  |
| logging_format          | 3.77 us                                                             | 3.89 us: 1.03x slower                                                  |
| async_tree_cpu_io_mixed | 534 ms                                                              | 552 ms: 1.03x slower                                                   |
| sqlglot_parse           | 956 us                                                              | 994 us: 1.04x slower                                                   |
| html5lib                | 34.8 ms                                                             | 36.2 ms: 1.04x slower                                                  |
| hexiom                  | 4.73 ms                                                             | 4.93 ms: 1.04x slower                                                  |
| sqlglot_transpile       | 1.12 ms                                                             | 1.17 ms: 1.04x slower                                                  |
| async_generators        | 195 ms                                                              | 205 ms: 1.05x slower                                                   |
| fannkuch                | 260 ms                                                              | 274 ms: 1.05x slower                                                   |
| meteor_contest          | 73.3 ms                                                             | 77.2 ms: 1.05x slower                                                  |
| async_tree_io           | 707 ms                                                              | 747 ms: 1.06x slower                                                   |
| raytrace                | 207 ms                                                              | 219 ms: 1.06x slower                                                   |
| pickle                  | 7.17 us                                                             | 7.61 us: 1.06x slower                                                  |
| pickle_pure_python      | 198 us                                                              | 212 us: 1.07x slower                                                   |
| pprint_safe_repr        | 463 ms                                                              | 497 ms: 1.07x slower                                                   |
| pprint_pformat          | 946 ms                                                              | 1.02 sec: 1.07x slower                                                 |
| float                   | 53.0 ms                                                             | 56.9 ms: 1.07x slower                                                  |
| sqlite_synth            | 1.28 us                                                             | 1.39 us: 1.08x slower                                                  |
| go                      | 109 ms                                                              | 118 ms: 1.09x slower                                                   |
| deepcopy                | 224 us                                                              | 243 us: 1.09x slower                                                   |
| deepcopy_reduce         | 1.91 us                                                             | 2.08 us: 1.09x slower                                                  |
| comprehensions          | 16.1 us                                                             | 17.8 us: 1.10x slower                                                  |
| deepcopy_memo           | 26.3 us                                                             | 29.6 us: 1.12x slower                                                  |
| coroutines              | 17.7 ms                                                             | 20.0 ms: 1.13x slower                                                  |
| pyflate                 | 309 ms                                                              | 354 ms: 1.14x slower                                                   |
| scimark_sor             | 82.9 ms                                                             | 97.5 ms: 1.18x slower                                                  |
| generators              | 28.6 ms                                                             | 33.7 ms: 1.18x slower                                                  |
| scimark_monte_carlo     | 46.5 ms                                                             | 56.2 ms: 1.21x slower                                                  |
| unpack_sequence         | 33.5 ns                                                             | 62.0 ns: 1.85x slower                                                  |
| Geometric mean          | (ref)                                                               | 1.03x slower                                                           |

Benchmark hidden because not significant (10): tornado_http, nqueens, richards, mdp, asyncio_tcp, xml_etree_iterparse, pycparser, bench_mp_pool, dask, mypy2
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative
