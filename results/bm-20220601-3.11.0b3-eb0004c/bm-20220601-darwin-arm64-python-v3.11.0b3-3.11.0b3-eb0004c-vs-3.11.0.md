
# Results vs. 3.11.0

- fork: python
- ref: v3.11.0b3
- machine: darwin-arm64
- commit hash: eb0004c
- commit date: 2022-06-01
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220601-darwin-arm64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------:|
| chameleon      | 4.55 ms                                                             | 4.60 ms: 1.01x slower                                      |
| docutils       | 1.47 sec                                                            | 1.46 sec: 1.01x faster                                     |
| html5lib       | 34.8 ms                                                             | 35.9 ms: 1.03x slower                                      |
| Geometric mean | (ref)                                                               | 1.00x slower                                               |

Benchmark hidden because not significant (2): 2to3, tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220601-darwin-arm64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 65.5 ms                                                             | 63.7 ms: 1.03x faster                                      |
| pidigits       | 281 ms                                                              | 281 ms: 1.00x slower                                       |
| float          | 53.0 ms                                                             | 55.0 ms: 1.04x slower                                      |
| Geometric mean | (ref)                                                               | 1.00x slower                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220601-darwin-arm64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                             | 2.40 ms: 1.10x faster                                      |
| regex_dna      | 151 ms                                                              | 149 ms: 1.01x faster                                       |
| regex_v8       | 16.1 ms                                                             | 16.2 ms: 1.01x slower                                      |
| regex_compile  | 76.6 ms                                                             | 77.8 ms: 1.01x slower                                      |
| Geometric mean | (ref)                                                               | 1.02x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220601-darwin-arm64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_dict          | 17.9 us                                                             | 17.1 us: 1.04x faster                                      |
| pickle_list          | 2.83 us                                                             | 2.72 us: 1.04x faster                                      |
| pickle               | 7.17 us                                                             | 7.07 us: 1.01x faster                                      |
| xml_etree_process    | 35.0 ms                                                             | 34.8 ms: 1.01x faster                                      |
| xml_etree_generate   | 48.2 ms                                                             | 48.1 ms: 1.00x faster                                      |
| json_loads           | 16.0 us                                                             | 16.2 us: 1.01x slower                                      |
| json_dumps           | 7.59 ms                                                             | 7.69 ms: 1.01x slower                                      |
| unpickle_list        | 2.63 us                                                             | 2.69 us: 1.02x slower                                      |
| unpickle             | 9.66 us                                                             | 10.0 us: 1.04x slower                                      |
| unpickle_pure_python | 158 us                                                              | 175 us: 1.11x slower                                       |
| pickle_pure_python   | 198 us                                                              | 222 us: 1.12x slower                                       |
| Geometric mean       | (ref)                                                               | 1.01x slower                                               |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220601-darwin-arm64-python-v3.11.0b3-3.11.0b3-eb0004c |
|------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------:|
| python_startup         | 12.3 ms                                                             | 12.4 ms: 1.00x slower                                      |
| python_startup_no_site | 10.1 ms                                                             | 10.1 ms: 1.01x slower                                      |
| Geometric mean         | (ref)                                                               | 1.00x slower                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220601-darwin-arm64-python-v3.11.0b3-3.11.0b3-eb0004c |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------:|
| genshi_text    | 15.3 ms                                                             | 15.2 ms: 1.01x faster                                      |
| genshi_xml     | 29.9 ms                                                             | 30.4 ms: 1.02x slower                                      |
| Geometric mean | (ref)                                                               | 1.00x slower                                               |

Benchmark hidden because not significant (2): django_template, mako

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220601-darwin-arm64-python-v3.11.0b3-3.11.0b3-eb0004c |
|-------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot            | 2.63 ms                                                             | 2.40 ms: 1.10x faster                                      |
| scimark_sor             | 82.9 ms                                                             | 76.7 ms: 1.08x faster                                      |
| nqueens                 | 62.4 ms                                                             | 58.6 ms: 1.06x faster                                      |
| pickle_dict             | 17.9 us                                                             | 17.1 us: 1.04x faster                                      |
| sympy_sum               | 86.0 ms                                                             | 82.8 ms: 1.04x faster                                      |
| unpack_sequence         | 33.5 ns                                                             | 32.3 ns: 1.04x faster                                      |
| logging_silent          | 68.0 ns                                                             | 65.5 ns: 1.04x faster                                      |
| pickle_list             | 2.83 us                                                             | 2.72 us: 1.04x faster                                      |
| generators              | 28.6 ms                                                             | 27.6 ms: 1.04x faster                                      |
| nbody                   | 65.5 ms                                                             | 63.7 ms: 1.03x faster                                      |
| coroutines              | 17.7 ms                                                             | 17.4 ms: 1.02x faster                                      |
| pathlib                 | 28.3 ms                                                             | 27.8 ms: 1.02x faster                                      |
| pickle                  | 7.17 us                                                             | 7.07 us: 1.01x faster                                      |
| regex_dna               | 151 ms                                                              | 149 ms: 1.01x faster                                       |
| scimark_lu              | 72.2 ms                                                             | 71.3 ms: 1.01x faster                                      |
| sqlalchemy_imperative   | 7.26 ms                                                             | 7.19 ms: 1.01x faster                                      |
| bench_thread_pool       | 474 us                                                              | 469 us: 1.01x faster                                       |
| hexiom                  | 4.73 ms                                                             | 4.69 ms: 1.01x faster                                      |
| genshi_text             | 15.3 ms                                                             | 15.2 ms: 1.01x faster                                      |
| docutils                | 1.47 sec                                                            | 1.46 sec: 1.01x faster                                     |
| go                      | 109 ms                                                              | 108 ms: 1.01x faster                                       |
| xml_etree_process       | 35.0 ms                                                             | 34.8 ms: 1.01x faster                                      |
| logging_simple          | 3.49 us                                                             | 3.47 us: 1.01x faster                                      |
| sqlalchemy_declarative  | 62.6 ms                                                             | 62.2 ms: 1.01x faster                                      |
| logging_format          | 3.77 us                                                             | 3.75 us: 1.01x faster                                      |
| mdp                     | 1.54 sec                                                            | 1.53 sec: 1.01x faster                                     |
| sympy_str               | 151 ms                                                              | 151 ms: 1.00x faster                                       |
| fannkuch                | 260 ms                                                              | 260 ms: 1.00x faster                                       |
| xml_etree_generate      | 48.2 ms                                                             | 48.1 ms: 1.00x faster                                      |
| spectral_norm           | 72.5 ms                                                             | 72.4 ms: 1.00x faster                                      |
| pidigits                | 281 ms                                                              | 281 ms: 1.00x slower                                       |
| scimark_fft             | 200 ms                                                              | 200 ms: 1.00x slower                                       |
| deltablue               | 2.81 ms                                                             | 2.82 ms: 1.00x slower                                      |
| raytrace                | 207 ms                                                              | 207 ms: 1.00x slower                                       |
| python_startup          | 12.3 ms                                                             | 12.4 ms: 1.00x slower                                      |
| telco                   | 3.40 ms                                                             | 3.41 ms: 1.00x slower                                      |
| scimark_sparse_mat_mult | 3.19 ms                                                             | 3.21 ms: 1.00x slower                                      |
| thrift                  | 431 us                                                              | 434 us: 1.01x slower                                       |
| create_gc_cycles        | 722 us                                                              | 727 us: 1.01x slower                                       |
| python_startup_no_site  | 10.1 ms                                                             | 10.1 ms: 1.01x slower                                      |
| json_loads              | 16.0 us                                                             | 16.2 us: 1.01x slower                                      |
| regex_v8                | 16.1 ms                                                             | 16.2 ms: 1.01x slower                                      |
| async_tree_cpu_io_mixed | 534 ms                                                              | 540 ms: 1.01x slower                                       |
| chameleon               | 4.55 ms                                                             | 4.60 ms: 1.01x slower                                      |
| sqlglot_optimize        | 31.2 ms                                                             | 31.6 ms: 1.01x slower                                      |
| json_dumps              | 7.59 ms                                                             | 7.69 ms: 1.01x slower                                      |
| sympy_integrate         | 11.5 ms                                                             | 11.7 ms: 1.01x slower                                      |
| regex_compile           | 76.6 ms                                                             | 77.8 ms: 1.01x slower                                      |
| pyflate                 | 309 ms                                                              | 314 ms: 1.02x slower                                       |
| genshi_xml              | 29.9 ms                                                             | 30.4 ms: 1.02x slower                                      |
| async_generators        | 195 ms                                                              | 199 ms: 1.02x slower                                       |
| async_tree_none         | 285 ms                                                              | 290 ms: 1.02x slower                                       |
| unpickle_list           | 2.63 us                                                             | 2.69 us: 1.02x slower                                      |
| json                    | 2.77 ms                                                             | 2.84 ms: 1.02x slower                                      |
| dulwich_log             | 29.7 ms                                                             | 30.4 ms: 1.02x slower                                      |
| html5lib                | 34.8 ms                                                             | 35.9 ms: 1.03x slower                                      |
| async_tree_memoization  | 338 ms                                                              | 350 ms: 1.03x slower                                       |
| richards                | 32.2 ms                                                             | 33.3 ms: 1.03x slower                                      |
| unpickle                | 9.66 us                                                             | 10.0 us: 1.04x slower                                      |
| float                   | 53.0 ms                                                             | 55.0 ms: 1.04x slower                                      |
| sqlite_synth            | 1.28 us                                                             | 1.34 us: 1.04x slower                                      |
| scimark_monte_carlo     | 46.5 ms                                                             | 48.7 ms: 1.05x slower                                      |
| pprint_safe_repr        | 463 ms                                                              | 489 ms: 1.06x slower                                       |
| meteor_contest          | 73.3 ms                                                             | 77.6 ms: 1.06x slower                                      |
| pprint_pformat          | 946 ms                                                              | 1.00 sec: 1.06x slower                                     |
| deepcopy                | 224 us                                                              | 238 us: 1.07x slower                                       |
| deepcopy_reduce         | 1.91 us                                                             | 2.04 us: 1.07x slower                                      |
| deepcopy_memo           | 26.3 us                                                             | 28.9 us: 1.10x slower                                      |
| unpickle_pure_python    | 158 us                                                              | 175 us: 1.11x slower                                       |
| pickle_pure_python      | 198 us                                                              | 222 us: 1.12x slower                                       |
| comprehensions          | 16.1 us                                                             | 18.3 us: 1.14x slower                                      |
| sqlglot_transpile       | 1.12 ms                                                             | 1.35 ms: 1.21x slower                                      |
| sqlglot_parse           | 956 us                                                              | 1.19 ms: 1.24x slower                                      |
| Geometric mean          | (ref)                                                               | 1.01x slower                                               |

Benchmark hidden because not significant (21): tornado_http, bench_mp_pool, mypy2, crypto_pyaes, 2to3, django_template, pylint, mako, xml_etree_iterparse, sqlglot_normalize, gc_traversal, sympy_expand, chaos, xml_etree_parse, dask, flaskblogging, asyncio_tcp, async_tree_io, pycparser, gunicorn, aiohttp
Ignored benchmarks (1) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: coverage
