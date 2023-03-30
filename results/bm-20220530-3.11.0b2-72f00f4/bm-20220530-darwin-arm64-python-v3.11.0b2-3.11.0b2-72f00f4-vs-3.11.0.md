
# Results vs. 3.11.0

- fork: python
- ref: v3.11.0b2
- machine: darwin-arm64
- commit hash: 72f00f4
- commit date: 2022-05-30
- overall geometric mean: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220530-darwin-arm64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------:|
| 2to3           | 161 ms                                                              | 162 ms: 1.00x slower                                       |
| chameleon      | 4.55 ms                                                             | 4.60 ms: 1.01x slower                                      |
| docutils       | 1.47 sec                                                            | 1.46 sec: 1.01x faster                                     |
| html5lib       | 34.8 ms                                                             | 36.0 ms: 1.03x slower                                      |
| Geometric mean | (ref)                                                               | 1.01x slower                                               |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220530-darwin-arm64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------:|
| nbody          | 65.5 ms                                                             | 63.7 ms: 1.03x faster                                      |
| float          | 53.0 ms                                                             | 55.2 ms: 1.04x slower                                      |
| Geometric mean | (ref)                                                               | 1.00x slower                                               |

Benchmark hidden because not significant (1): pidigits

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220530-darwin-arm64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot   | 2.63 ms                                                             | 2.40 ms: 1.10x faster                                      |
| regex_dna      | 151 ms                                                              | 150 ms: 1.01x faster                                       |
| regex_v8       | 16.1 ms                                                             | 16.1 ms: 1.00x slower                                      |
| regex_compile  | 76.6 ms                                                             | 77.9 ms: 1.02x slower                                      |
| Geometric mean | (ref)                                                               | 1.02x faster                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220530-darwin-arm64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|----------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------:|
| pickle_dict          | 17.9 us                                                             | 17.2 us: 1.04x faster                                      |
| pickle_list          | 2.83 us                                                             | 2.76 us: 1.02x faster                                      |
| pickle               | 7.17 us                                                             | 7.06 us: 1.02x faster                                      |
| xml_etree_process    | 35.0 ms                                                             | 34.9 ms: 1.00x faster                                      |
| json_loads           | 16.0 us                                                             | 16.1 us: 1.00x slower                                      |
| json_dumps           | 7.59 ms                                                             | 7.63 ms: 1.01x slower                                      |
| unpickle_list        | 2.63 us                                                             | 2.70 us: 1.02x slower                                      |
| unpickle             | 9.66 us                                                             | 9.98 us: 1.03x slower                                      |
| pickle_pure_python   | 198 us                                                              | 217 us: 1.09x slower                                       |
| unpickle_pure_python | 158 us                                                              | 176 us: 1.11x slower                                       |
| Geometric mean       | (ref)                                                               | 1.01x slower                                               |

Benchmark hidden because not significant (3): xml_etree_parse, xml_etree_iterparse, xml_etree_generate

Benchmarks with tag 'startup':
==============================

Benchmark hidden because not significant (2): python_startup_no_site, python_startup

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220530-darwin-arm64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|-----------------|:-------------------------------------------------------------------:|:----------------------------------------------------------:|
| django_template | 21.1 ms                                                             | 20.9 ms: 1.01x faster                                      |
| mako            | 8.42 ms                                                             | 8.36 ms: 1.01x faster                                      |
| genshi_text     | 15.3 ms                                                             | 15.2 ms: 1.00x faster                                      |
| genshi_xml      | 29.9 ms                                                             | 30.3 ms: 1.01x slower                                      |
| Geometric mean  | (ref)                                                               | 1.00x faster                                               |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509 | bm-20220530-darwin-arm64-python-v3.11.0b2-3.11.0b2-72f00f4 |
|-------------------------|:-------------------------------------------------------------------:|:----------------------------------------------------------:|
| regex_effbot            | 2.63 ms                                                             | 2.40 ms: 1.10x faster                                      |
| nqueens                 | 62.4 ms                                                             | 58.5 ms: 1.07x faster                                      |
| scimark_sor             | 82.9 ms                                                             | 78.7 ms: 1.05x faster                                      |
| sympy_sum               | 86.0 ms                                                             | 82.7 ms: 1.04x faster                                      |
| logging_silent          | 68.0 ns                                                             | 65.3 ns: 1.04x faster                                      |
| pickle_dict             | 17.9 us                                                             | 17.2 us: 1.04x faster                                      |
| unpack_sequence         | 33.5 ns                                                             | 32.4 ns: 1.04x faster                                      |
| pathlib                 | 28.3 ms                                                             | 27.4 ms: 1.03x faster                                      |
| generators              | 28.6 ms                                                             | 27.7 ms: 1.03x faster                                      |
| nbody                   | 65.5 ms                                                             | 63.7 ms: 1.03x faster                                      |
| coroutines              | 17.7 ms                                                             | 17.3 ms: 1.03x faster                                      |
| go                      | 109 ms                                                              | 106 ms: 1.03x faster                                       |
| pickle_list             | 2.83 us                                                             | 2.76 us: 1.02x faster                                      |
| pickle                  | 7.17 us                                                             | 7.06 us: 1.02x faster                                      |
| bench_thread_pool       | 474 us                                                              | 468 us: 1.01x faster                                       |
| scimark_lu              | 72.2 ms                                                             | 71.3 ms: 1.01x faster                                      |
| regex_dna               | 151 ms                                                              | 150 ms: 1.01x faster                                       |
| sqlalchemy_declarative  | 62.6 ms                                                             | 61.9 ms: 1.01x faster                                      |
| raytrace                | 207 ms                                                              | 205 ms: 1.01x faster                                       |
| deltablue               | 2.81 ms                                                             | 2.79 ms: 1.01x faster                                      |
| docutils                | 1.47 sec                                                            | 1.46 sec: 1.01x faster                                     |
| sympy_str               | 151 ms                                                              | 150 ms: 1.01x faster                                       |
| django_template         | 21.1 ms                                                             | 20.9 ms: 1.01x faster                                      |
| mako                    | 8.42 ms                                                             | 8.36 ms: 1.01x faster                                      |
| crypto_pyaes            | 51.8 ms                                                             | 51.5 ms: 1.01x faster                                      |
| spectral_norm           | 72.5 ms                                                             | 72.1 ms: 1.01x faster                                      |
| logging_simple          | 3.49 us                                                             | 3.48 us: 1.01x faster                                      |
| genshi_text             | 15.3 ms                                                             | 15.2 ms: 1.00x faster                                      |
| hexiom                  | 4.73 ms                                                             | 4.71 ms: 1.00x faster                                      |
| mdp                     | 1.54 sec                                                            | 1.54 sec: 1.00x faster                                     |
| sqlalchemy_imperative   | 7.26 ms                                                             | 7.25 ms: 1.00x faster                                      |
| xml_etree_process       | 35.0 ms                                                             | 34.9 ms: 1.00x faster                                      |
| fannkuch                | 260 ms                                                              | 260 ms: 1.00x faster                                       |
| scimark_sparse_mat_mult | 3.19 ms                                                             | 3.19 ms: 1.00x faster                                      |
| regex_v8                | 16.1 ms                                                             | 16.1 ms: 1.00x slower                                      |
| scimark_fft             | 200 ms                                                              | 200 ms: 1.00x slower                                       |
| gc_traversal            | 2.41 ms                                                             | 2.41 ms: 1.00x slower                                      |
| chaos                   | 49.4 ms                                                             | 49.5 ms: 1.00x slower                                      |
| 2to3                    | 161 ms                                                              | 162 ms: 1.00x slower                                       |
| sqlglot_normalize       | 171 ms                                                              | 172 ms: 1.00x slower                                       |
| json_loads              | 16.0 us                                                             | 16.1 us: 1.00x slower                                      |
| sympy_expand            | 243 ms                                                              | 244 ms: 1.00x slower                                       |
| thrift                  | 431 us                                                              | 434 us: 1.01x slower                                       |
| async_tree_io           | 707 ms                                                              | 711 ms: 1.01x slower                                       |
| telco                   | 3.40 ms                                                             | 3.42 ms: 1.01x slower                                      |
| json_dumps              | 7.59 ms                                                             | 7.63 ms: 1.01x slower                                      |
| sympy_integrate         | 11.5 ms                                                             | 11.6 ms: 1.01x slower                                      |
| async_tree_cpu_io_mixed | 534 ms                                                              | 539 ms: 1.01x slower                                       |
| create_gc_cycles        | 722 us                                                              | 730 us: 1.01x slower                                       |
| chameleon               | 4.55 ms                                                             | 4.60 ms: 1.01x slower                                      |
| genshi_xml              | 29.9 ms                                                             | 30.3 ms: 1.01x slower                                      |
| regex_compile           | 76.6 ms                                                             | 77.9 ms: 1.02x slower                                      |
| pyflate                 | 309 ms                                                              | 315 ms: 1.02x slower                                       |
| async_generators        | 195 ms                                                              | 199 ms: 1.02x slower                                       |
| json                    | 2.77 ms                                                             | 2.83 ms: 1.02x slower                                      |
| async_tree_none         | 285 ms                                                              | 291 ms: 1.02x slower                                       |
| dulwich_log             | 29.7 ms                                                             | 30.4 ms: 1.02x slower                                      |
| unpickle_list           | 2.63 us                                                             | 2.70 us: 1.02x slower                                      |
| sqlglot_optimize        | 31.2 ms                                                             | 32.0 ms: 1.03x slower                                      |
| unpickle                | 9.66 us                                                             | 9.98 us: 1.03x slower                                      |
| html5lib                | 34.8 ms                                                             | 36.0 ms: 1.03x slower                                      |
| richards                | 32.2 ms                                                             | 33.5 ms: 1.04x slower                                      |
| float                   | 53.0 ms                                                             | 55.2 ms: 1.04x slower                                      |
| async_tree_memoization  | 338 ms                                                              | 352 ms: 1.04x slower                                       |
| sqlite_synth            | 1.28 us                                                             | 1.34 us: 1.04x slower                                      |
| scimark_monte_carlo     | 46.5 ms                                                             | 48.7 ms: 1.05x slower                                      |
| meteor_contest          | 73.3 ms                                                             | 77.4 ms: 1.06x slower                                      |
| pprint_safe_repr        | 463 ms                                                              | 490 ms: 1.06x slower                                       |
| pprint_pformat          | 946 ms                                                              | 1.01 sec: 1.06x slower                                     |
| deepcopy                | 224 us                                                              | 238 us: 1.07x slower                                       |
| deepcopy_reduce         | 1.91 us                                                             | 2.06 us: 1.08x slower                                      |
| pickle_pure_python      | 198 us                                                              | 217 us: 1.09x slower                                       |
| deepcopy_memo           | 26.3 us                                                             | 28.8 us: 1.09x slower                                      |
| unpickle_pure_python    | 158 us                                                              | 176 us: 1.11x slower                                       |
| comprehensions          | 16.1 us                                                             | 18.3 us: 1.14x slower                                      |
| sqlglot_transpile       | 1.12 ms                                                             | 1.37 ms: 1.22x slower                                      |
| sqlglot_parse           | 956 us                                                              | 1.19 ms: 1.25x slower                                      |
| Geometric mean          | (ref)                                                               | 1.01x slower                                               |

Benchmark hidden because not significant (16): tornado_http, xml_etree_parse, xml_etree_iterparse, mypy2, logging_format, bench_mp_pool, pylint, pidigits, python_startup_no_site, xml_etree_generate, asyncio_tcp, dask, pycparser, gunicorn, python_startup, aiohttp
Ignored benchmarks (2) of /home/runner/work/benchmarking/benchmarking/results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-deaf509e8fc6e0363bd6-3.11.0-deaf509.json: coverage, flaskblogging
