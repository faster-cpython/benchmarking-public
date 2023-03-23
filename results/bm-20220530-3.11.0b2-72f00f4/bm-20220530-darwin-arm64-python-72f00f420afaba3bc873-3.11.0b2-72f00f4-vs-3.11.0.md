
# Results vs. 3.11.0

- fork: python
- ref: 72f00f420afaba3bc873
- machine: darwin-arm64
- commit hash: 72f00f4
- commit date: 2022-05-30
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-darwin-arm64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 162 ms: 1.01x slower                                                  |
| chameleon      | 4.57 ms                                                | 4.68 ms: 1.02x slower                                                 |
| docutils       | 1.47 sec                                               | 1.46 sec: 1.01x faster                                                |
| html5lib       | 34.7 ms                                                | 35.9 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-darwin-arm64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| nbody          | 65.5 ms                                                | 63.7 ms: 1.03x faster                                                 |
| float          | 53.0 ms                                                | 55.8 ms: 1.05x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-darwin-arm64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                | 2.39 ms: 1.10x faster                                                 |
| regex_dna      | 152 ms                                                 | 149 ms: 1.01x faster                                                  |
| regex_v8       | 16.2 ms                                                | 16.1 ms: 1.01x faster                                                 |
| regex_compile  | 76.7 ms                                                | 77.6 ms: 1.01x slower                                                 |
| Geometric mean | (ref)                                                  | 1.03x faster                                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-darwin-arm64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| pickle_dict          | 17.9 us                                                | 17.2 us: 1.04x faster                                                 |
| pickle_list          | 2.81 us                                                | 2.75 us: 1.02x faster                                                 |
| pickle               | 7.17 us                                                | 7.05 us: 1.02x faster                                                 |
| xml_etree_generate   | 48.8 ms                                                | 48.3 ms: 1.01x faster                                                 |
| xml_etree_process    | 35.2 ms                                                | 34.9 ms: 1.01x faster                                                 |
| json_dumps           | 7.72 ms                                                | 7.69 ms: 1.00x faster                                                 |
| json_loads           | 16.1 us                                                | 16.1 us: 1.00x slower                                                 |
| unpickle_list        | 2.63 us                                                | 2.70 us: 1.03x slower                                                 |
| unpickle             | 9.70 us                                                | 10.0 us: 1.03x slower                                                 |
| unpickle_pure_python | 159 us                                                 | 175 us: 1.10x slower                                                  |
| pickle_pure_python   | 199 us                                                 | 221 us: 1.11x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (2): xml_etree_iterparse, xml_etree_parse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-darwin-arm64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| python_startup         | 11.5 ms                                                | 12.2 ms: 1.05x slower                                                 |
| python_startup_no_site | 9.31 ms                                                | 9.88 ms: 1.06x slower                                                 |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                          |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-darwin-arm64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| mako           | 8.49 ms                                                | 8.44 ms: 1.01x faster                                                 |
| genshi_text    | 15.3 ms                                                | 15.5 ms: 1.02x slower                                                 |
| genshi_xml     | 29.8 ms                                                | 30.6 ms: 1.03x slower                                                 |
| Geometric mean | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20220530-darwin-arm64-python-72f00f420afaba3bc873-3.11.0b2-72f00f4 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------:|
| regex_effbot            | 2.63 ms                                                | 2.39 ms: 1.10x faster                                                 |
| scimark_sor             | 83.0 ms                                                | 76.0 ms: 1.09x faster                                                 |
| nqueens                 | 61.8 ms                                                | 58.3 ms: 1.06x faster                                                 |
| pickle_dict             | 17.9 us                                                | 17.2 us: 1.04x faster                                                 |
| logging_silent          | 68.0 ns                                                | 65.4 ns: 1.04x faster                                                 |
| sympy_sum               | 86.0 ms                                                | 82.8 ms: 1.04x faster                                                 |
| unpack_sequence         | 33.6 ns                                                | 32.4 ns: 1.04x faster                                                 |
| generators              | 28.8 ms                                                | 27.9 ms: 1.03x faster                                                 |
| nbody                   | 65.5 ms                                                | 63.7 ms: 1.03x faster                                                 |
| coroutines              | 17.7 ms                                                | 17.3 ms: 1.03x faster                                                 |
| go                      | 109 ms                                                 | 106 ms: 1.02x faster                                                  |
| pickle_list             | 2.81 us                                                | 2.75 us: 1.02x faster                                                 |
| pickle                  | 7.17 us                                                | 7.05 us: 1.02x faster                                                 |
| regex_dna               | 152 ms                                                 | 149 ms: 1.01x faster                                                  |
| scimark_lu              | 72.1 ms                                                | 71.2 ms: 1.01x faster                                                 |
| logging_simple          | 3.50 us                                                | 3.46 us: 1.01x faster                                                 |
| xml_etree_generate      | 48.8 ms                                                | 48.3 ms: 1.01x faster                                                 |
| sqlalchemy_declarative  | 62.7 ms                                                | 62.0 ms: 1.01x faster                                                 |
| logging_format          | 3.78 us                                                | 3.74 us: 1.01x faster                                                 |
| gc_traversal            | 2.43 ms                                                | 2.41 ms: 1.01x faster                                                 |
| xml_etree_process       | 35.2 ms                                                | 34.9 ms: 1.01x faster                                                 |
| docutils                | 1.47 sec                                               | 1.46 sec: 1.01x faster                                                |
| mdp                     | 1.54 sec                                               | 1.53 sec: 1.01x faster                                                |
| sqlalchemy_imperative   | 7.31 ms                                                | 7.26 ms: 1.01x faster                                                 |
| sympy_str               | 152 ms                                                 | 151 ms: 1.01x faster                                                  |
| hexiom                  | 4.73 ms                                                | 4.70 ms: 1.01x faster                                                 |
| regex_v8                | 16.2 ms                                                | 16.1 ms: 1.01x faster                                                 |
| mako                    | 8.49 ms                                                | 8.44 ms: 1.01x faster                                                 |
| spectral_norm           | 72.8 ms                                                | 72.4 ms: 1.00x faster                                                 |
| json_dumps              | 7.72 ms                                                | 7.69 ms: 1.00x faster                                                 |
| chaos                   | 49.5 ms                                                | 49.3 ms: 1.00x faster                                                 |
| crypto_pyaes            | 51.7 ms                                                | 51.6 ms: 1.00x faster                                                 |
| raytrace                | 207 ms                                                 | 207 ms: 1.00x slower                                                  |
| scimark_fft             | 199 ms                                                 | 200 ms: 1.00x slower                                                  |
| sympy_expand            | 243 ms                                                 | 244 ms: 1.00x slower                                                  |
| json_loads              | 16.1 us                                                | 16.1 us: 1.00x slower                                                 |
| deltablue               | 2.81 ms                                                | 2.82 ms: 1.01x slower                                                 |
| thrift                  | 433 us                                                 | 436 us: 1.01x slower                                                  |
| 2to3                    | 161 ms                                                 | 162 ms: 1.01x slower                                                  |
| telco                   | 3.39 ms                                                | 3.42 ms: 1.01x slower                                                 |
| bench_thread_pool       | 473 us                                                 | 477 us: 1.01x slower                                                  |
| sqlglot_optimize        | 31.2 ms                                                | 31.5 ms: 1.01x slower                                                 |
| async_tree_io           | 706 ms                                                 | 713 ms: 1.01x slower                                                  |
| async_tree_cpu_io_mixed | 534 ms                                                 | 540 ms: 1.01x slower                                                  |
| sympy_integrate         | 11.5 ms                                                | 11.6 ms: 1.01x slower                                                 |
| regex_compile           | 76.7 ms                                                | 77.6 ms: 1.01x slower                                                 |
| pyflate                 | 311 ms                                                 | 315 ms: 1.01x slower                                                  |
| async_generators        | 195 ms                                                 | 197 ms: 1.01x slower                                                  |
| dulwich_log             | 29.9 ms                                                | 30.3 ms: 1.02x slower                                                 |
| genshi_text             | 15.3 ms                                                | 15.5 ms: 1.02x slower                                                 |
| json                    | 2.77 ms                                                | 2.83 ms: 1.02x slower                                                 |
| async_tree_none         | 285 ms                                                 | 291 ms: 1.02x slower                                                  |
| chameleon               | 4.57 ms                                                | 4.68 ms: 1.02x slower                                                 |
| unpickle_list           | 2.63 us                                                | 2.70 us: 1.03x slower                                                 |
| genshi_xml              | 29.8 ms                                                | 30.6 ms: 1.03x slower                                                 |
| unpickle                | 9.70 us                                                | 10.0 us: 1.03x slower                                                 |
| html5lib                | 34.7 ms                                                | 35.9 ms: 1.03x slower                                                 |
| richards                | 32.2 ms                                                | 33.5 ms: 1.04x slower                                                 |
| sqlite_synth            | 1.27 us                                                | 1.33 us: 1.04x slower                                                 |
| async_tree_memoization  | 336 ms                                                 | 353 ms: 1.05x slower                                                  |
| meteor_contest          | 73.8 ms                                                | 77.7 ms: 1.05x slower                                                 |
| float                   | 53.0 ms                                                | 55.8 ms: 1.05x slower                                                 |
| pprint_safe_repr        | 465 ms                                                 | 489 ms: 1.05x slower                                                  |
| scimark_monte_carlo     | 46.4 ms                                                | 48.9 ms: 1.05x slower                                                 |
| python_startup          | 11.5 ms                                                | 12.2 ms: 1.05x slower                                                 |
| pprint_pformat          | 950 ms                                                 | 1.01 sec: 1.06x slower                                                |
| python_startup_no_site  | 9.31 ms                                                | 9.88 ms: 1.06x slower                                                 |
| deepcopy                | 224 us                                                 | 238 us: 1.06x slower                                                  |
| deepcopy_reduce         | 1.91 us                                                | 2.05 us: 1.07x slower                                                 |
| deepcopy_memo           | 26.3 us                                                | 28.5 us: 1.08x slower                                                 |
| unpickle_pure_python    | 159 us                                                 | 175 us: 1.10x slower                                                  |
| pickle_pure_python      | 199 us                                                 | 221 us: 1.11x slower                                                  |
| comprehensions          | 16.1 us                                                | 18.4 us: 1.14x slower                                                 |
| sqlglot_transpile       | 1.12 ms                                                | 1.36 ms: 1.21x slower                                                 |
| sqlglot_parse           | 957 us                                                 | 1.19 ms: 1.25x slower                                                 |
| Geometric mean          | (ref)                                                  | 1.01x slower                                                          |

Benchmark hidden because not significant (18): pathlib, tornado_http, mypy2, asyncio_tcp, sqlglot_normalize, pylint, django_template, aiohttp, fannkuch, scimark_sparse_mat_mult, pidigits, create_gc_cycles, pycparser, xml_etree_iterparse, xml_etree_parse, dask, gunicorn, bench_mp_pool
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: coverage, flaskblogging
