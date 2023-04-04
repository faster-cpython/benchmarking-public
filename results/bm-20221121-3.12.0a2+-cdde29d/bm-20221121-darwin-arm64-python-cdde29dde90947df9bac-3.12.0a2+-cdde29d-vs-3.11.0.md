
# Results vs. 3.11.0

- fork: python
- ref: cdde29dde90947df9bac
- machine: darwin-arm64
- commit hash: cdde29d
- commit date: 2022-11-21
- overall geometric mean: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221121-darwin-arm64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 161 ms                                                              | 165 ms: 1.02x slower                                                   |
| chameleon      | 4.55 ms                                                             | 4.42 ms: 1.03x faster                                                  |
| html5lib       | 34.8 ms                                                             | 36.1 ms: 1.04x slower                                                  |
| Geometric mean | (ref)                                                               | 1.00x slower                                                           |

Benchmark hidden because not significant (2): docutils, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221121-darwin-arm64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 65.5 ms                                                             | 65.1 ms: 1.01x faster                                                  |
| pidigits       | 281 ms                                                              | 281 ms: 1.00x slower                                                   |
| float          | 53.0 ms                                                             | 57.0 ms: 1.07x slower                                                  |
| Geometric mean | (ref)                                                               | 1.02x slower                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221121-darwin-arm64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_v8       | 16.1 ms                                                             | 15.8 ms: 1.02x faster                                                  |
| regex_dna      | 151 ms                                                              | 149 ms: 1.01x faster                                                   |
| regex_compile  | 76.6 ms                                                             | 75.7 ms: 1.01x faster                                                  |
| regex_effbot   | 2.63 ms                                                             | 2.65 ms: 1.01x slower                                                  |
| Geometric mean | (ref)                                                               | 1.01x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221121-darwin-arm64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 7.59 ms                                                             | 6.04 ms: 1.26x faster                                                  |
| xml_etree_parse      | 106 ms                                                              | 96.3 ms: 1.10x faster                                                  |
| pickle_list          | 2.83 us                                                             | 2.81 us: 1.01x faster                                                  |
| pickle_dict          | 17.9 us                                                             | 17.9 us: 1.01x slower                                                  |
| xml_etree_process    | 35.0 ms                                                             | 35.5 ms: 1.01x slower                                                  |
| unpickle_pure_python | 158 us                                                              | 161 us: 1.02x slower                                                   |
| json_loads           | 16.0 us                                                             | 16.3 us: 1.02x slower                                                  |
| unpickle             | 9.66 us                                                             | 9.85 us: 1.02x slower                                                  |
| xml_etree_generate   | 48.2 ms                                                             | 49.3 ms: 1.02x slower                                                  |
| pickle               | 7.17 us                                                             | 7.51 us: 1.05x slower                                                  |
| pickle_pure_python   | 198 us                                                              | 208 us: 1.05x slower                                                   |
| Geometric mean       | (ref)                                                               | 1.01x faster                                                           |

Benchmark hidden because not significant (2): xml_etree_iterparse, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221121-darwin-arm64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 12.3 ms                                                             | 12.2 ms: 1.01x faster                                                  |
| python_startup_no_site | 10.1 ms                                                             | 10.2 ms: 1.01x slower                                                  |
| Geometric mean         | (ref)                                                               | 1.00x faster                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221121-darwin-arm64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|-----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| mako            | 8.42 ms                                                             | 7.21 ms: 1.17x faster                                                  |
| genshi_text     | 15.3 ms                                                             | 14.6 ms: 1.05x faster                                                  |
| genshi_xml      | 29.9 ms                                                             | 29.2 ms: 1.02x faster                                                  |
| django_template | 21.1 ms                                                             | 21.4 ms: 1.01x slower                                                  |
| Geometric mean  | (ref)                                                               | 1.06x faster                                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20221121-darwin-arm64-python-cdde29dde90947df9bac-3.12.0a2+-cdde29d |
|-------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps              | 7.59 ms                                                             | 6.04 ms: 1.26x faster                                                  |
| mako                    | 8.42 ms                                                             | 7.21 ms: 1.17x faster                                                  |
| scimark_sparse_mat_mult | 3.19 ms                                                             | 2.82 ms: 1.13x faster                                                  |
| xml_etree_parse         | 106 ms                                                              | 96.3 ms: 1.10x faster                                                  |
| logging_silent          | 68.0 ns                                                             | 64.6 ns: 1.05x faster                                                  |
| genshi_text             | 15.3 ms                                                             | 14.6 ms: 1.05x faster                                                  |
| pathlib                 | 28.3 ms                                                             | 27.1 ms: 1.04x faster                                                  |
| create_gc_cycles        | 722 us                                                              | 695 us: 1.04x faster                                                   |
| richards                | 32.2 ms                                                             | 31.2 ms: 1.03x faster                                                  |
| chameleon               | 4.55 ms                                                             | 4.42 ms: 1.03x faster                                                  |
| genshi_xml              | 29.9 ms                                                             | 29.2 ms: 1.02x faster                                                  |
| async_tree_memoization  | 338 ms                                                              | 330 ms: 1.02x faster                                                   |
| coverage                | 58.4 ms                                                             | 57.4 ms: 1.02x faster                                                  |
| scimark_lu              | 72.2 ms                                                             | 70.9 ms: 1.02x faster                                                  |
| regex_v8                | 16.1 ms                                                             | 15.8 ms: 1.02x faster                                                  |
| regex_dna               | 151 ms                                                              | 149 ms: 1.01x faster                                                   |
| regex_compile           | 76.6 ms                                                             | 75.7 ms: 1.01x faster                                                  |
| deltablue               | 2.81 ms                                                             | 2.78 ms: 1.01x faster                                                  |
| python_startup          | 12.3 ms                                                             | 12.2 ms: 1.01x faster                                                  |
| bench_thread_pool       | 474 us                                                              | 470 us: 1.01x faster                                                   |
| pickle_list             | 2.83 us                                                             | 2.81 us: 1.01x faster                                                  |
| scimark_fft             | 200 ms                                                              | 198 ms: 1.01x faster                                                   |
| telco                   | 3.40 ms                                                             | 3.37 ms: 1.01x faster                                                  |
| nbody                   | 65.5 ms                                                             | 65.1 ms: 1.01x faster                                                  |
| mdp                     | 1.54 sec                                                            | 1.54 sec: 1.00x faster                                                 |
| pidigits                | 281 ms                                                              | 281 ms: 1.00x slower                                                   |
| gc_traversal            | 2.41 ms                                                             | 2.42 ms: 1.00x slower                                                  |
| pickle_dict             | 17.9 us                                                             | 17.9 us: 1.01x slower                                                  |
| sqlglot_optimize        | 31.2 ms                                                             | 31.4 ms: 1.01x slower                                                  |
| regex_effbot            | 2.63 ms                                                             | 2.65 ms: 1.01x slower                                                  |
| sqlglot_normalize       | 171 ms                                                              | 173 ms: 1.01x slower                                                   |
| python_startup_no_site  | 10.1 ms                                                             | 10.2 ms: 1.01x slower                                                  |
| spectral_norm           | 72.5 ms                                                             | 73.2 ms: 1.01x slower                                                  |
| sympy_sum               | 86.0 ms                                                             | 87.0 ms: 1.01x slower                                                  |
| async_tree_none         | 285 ms                                                              | 289 ms: 1.01x slower                                                   |
| xml_etree_process       | 35.0 ms                                                             | 35.5 ms: 1.01x slower                                                  |
| django_template         | 21.1 ms                                                             | 21.4 ms: 1.01x slower                                                  |
| json                    | 2.77 ms                                                             | 2.82 ms: 1.01x slower                                                  |
| dulwich_log             | 29.7 ms                                                             | 30.2 ms: 1.02x slower                                                  |
| sympy_expand            | 243 ms                                                              | 247 ms: 1.02x slower                                                   |
| unpickle_pure_python    | 158 us                                                              | 161 us: 1.02x slower                                                   |
| json_loads              | 16.0 us                                                             | 16.3 us: 1.02x slower                                                  |
| sympy_str               | 151 ms                                                              | 154 ms: 1.02x slower                                                   |
| sympy_integrate         | 11.5 ms                                                             | 11.7 ms: 1.02x slower                                                  |
| async_tree_cpu_io_mixed | 534 ms                                                              | 544 ms: 1.02x slower                                                   |
| unpickle                | 9.66 us                                                             | 9.85 us: 1.02x slower                                                  |
| raytrace                | 207 ms                                                              | 211 ms: 1.02x slower                                                   |
| xml_etree_generate      | 48.2 ms                                                             | 49.3 ms: 1.02x slower                                                  |
| 2to3                    | 161 ms                                                              | 165 ms: 1.02x slower                                                   |
| thrift                  | 431 us                                                              | 442 us: 1.02x slower                                                   |
| crypto_pyaes            | 51.8 ms                                                             | 53.1 ms: 1.02x slower                                                  |
| chaos                   | 49.4 ms                                                             | 50.7 ms: 1.03x slower                                                  |
| logging_simple          | 3.49 us                                                             | 3.60 us: 1.03x slower                                                  |
| html5lib                | 34.8 ms                                                             | 36.1 ms: 1.04x slower                                                  |
| sqlglot_transpile       | 1.12 ms                                                             | 1.16 ms: 1.04x slower                                                  |
| logging_format          | 3.77 us                                                             | 3.91 us: 1.04x slower                                                  |
| sqlglot_parse           | 956 us                                                              | 994 us: 1.04x slower                                                   |
| hexiom                  | 4.73 ms                                                             | 4.93 ms: 1.04x slower                                                  |
| fannkuch                | 260 ms                                                              | 271 ms: 1.04x slower                                                   |
| pickle                  | 7.17 us                                                             | 7.51 us: 1.05x slower                                                  |
| pickle_pure_python      | 198 us                                                              | 208 us: 1.05x slower                                                   |
| async_generators        | 195 ms                                                              | 205 ms: 1.05x slower                                                   |
| meteor_contest          | 73.3 ms                                                             | 77.2 ms: 1.05x slower                                                  |
| async_tree_io           | 707 ms                                                              | 745 ms: 1.05x slower                                                   |
| pprint_pformat          | 946 ms                                                              | 1.01 sec: 1.07x slower                                                 |
| pprint_safe_repr        | 463 ms                                                              | 497 ms: 1.07x slower                                                   |
| float                   | 53.0 ms                                                             | 57.0 ms: 1.07x slower                                                  |
| deepcopy_reduce         | 1.91 us                                                             | 2.07 us: 1.08x slower                                                  |
| go                      | 109 ms                                                              | 118 ms: 1.08x slower                                                   |
| sqlite_synth            | 1.28 us                                                             | 1.39 us: 1.09x slower                                                  |
| deepcopy                | 224 us                                                              | 244 us: 1.09x slower                                                   |
| deepcopy_memo           | 26.3 us                                                             | 29.0 us: 1.10x slower                                                  |
| comprehensions          | 16.1 us                                                             | 17.8 us: 1.10x slower                                                  |
| coroutines              | 17.7 ms                                                             | 19.9 ms: 1.12x slower                                                  |
| pyflate                 | 309 ms                                                              | 350 ms: 1.13x slower                                                   |
| scimark_monte_carlo     | 46.5 ms                                                             | 54.7 ms: 1.18x slower                                                  |
| generators              | 28.6 ms                                                             | 34.3 ms: 1.20x slower                                                  |
| scimark_sor             | 82.9 ms                                                             | 104 ms: 1.25x slower                                                   |
| unpack_sequence         | 33.5 ns                                                             | 62.4 ns: 1.86x slower                                                  |
| Geometric mean          | (ref)                                                               | 1.02x slower                                                           |

Benchmark hidden because not significant (10): tornado_http, nqueens, xml_etree_iterparse, pycparser, unpickle_list, docutils, asyncio_tcp, dask, bench_mp_pool, mypy2
Ignored benchmarks (6) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: aiohttp, flaskblogging, gunicorn, pylint, sqlalchemy_declarative, sqlalchemy_imperative
