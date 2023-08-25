
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 2e49bd0
- commit date: 2022-04-05
- overall geometric mean: 1.01x slower \*
- HPT reliability: 99.90%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220405-linux-x86_64-python-main-3.11.0a7-2e49bd0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 259 ms                                                 | 264 ms: 1.02x slower                                  |
| chameleon      | 6.47 ms                                                | 6.87 ms: 1.06x slower                                 |
| tornado_http   | 96.3 ms                                                | 95.4 ms: 1.01x faster                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                          |

Benchmark hidden because not significant (1): html5lib

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220405-linux-x86_64-python-main-3.11.0a7-2e49bd0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| float          | 77.2 ms                                                | 74.4 ms: 1.04x faster                                 |
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                  |
| nbody          | 93.1 ms                                                | 95.2 ms: 1.02x slower                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220405-linux-x86_64-python-main-3.11.0a7-2e49bd0 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.34 ms: 1.20x faster                                 |
| regex_compile  | 138 ms                                                 | 137 ms: 1.00x faster                                  |
| regex_dna      | 204 ms                                                 | 231 ms: 1.13x slower                                  |
| regex_v8       | 22.0 ms                                                | 25.9 ms: 1.17x slower                                 |
| Geometric mean | (ref)                                                  | 1.03x slower                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220405-linux-x86_64-python-main-3.11.0a7-2e49bd0 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_dict          | 31.1 us                                                | 27.6 us: 1.13x faster                                 |
| pickle               | 10.1 us                                                | 9.55 us: 1.05x faster                                 |
| xml_etree_parse      | 158 ms                                                 | 157 ms: 1.01x faster                                  |
| json_dumps           | 12.6 ms                                                | 12.5 ms: 1.01x faster                                 |
| unpickle_pure_python | 228 us                                                 | 231 us: 1.01x slower                                  |
| unpickle_list        | 4.91 us                                                | 4.97 us: 1.01x slower                                 |
| pickle_pure_python   | 306 us                                                 | 311 us: 1.02x slower                                  |
| xml_etree_process    | 53.9 ms                                                | 55.2 ms: 1.03x slower                                 |
| xml_etree_generate   | 76.2 ms                                                | 78.5 ms: 1.03x slower                                 |
| json_loads           | 26.5 us                                                | 28.1 us: 1.06x slower                                 |
| pickle_list          | 4.11 us                                                | 4.57 us: 1.11x slower                                 |
| Geometric mean       | (ref)                                                  | 1.01x slower                                          |

Benchmark hidden because not significant (2): xml_etree_iterparse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220405-linux-x86_64-python-main-3.11.0a7-2e49bd0 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.07 ms: 1.06x faster                                 |
| python_startup_no_site | 6.01 ms                                                | 5.98 ms: 1.00x faster                                 |
| Geometric mean         | (ref)                                                  | 1.03x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220405-linux-x86_64-python-main-3.11.0a7-2e49bd0 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako            | 10.1 ms                                                | 10.2 ms: 1.01x slower                                 |
| django_template | 32.6 ms                                                | 34.3 ms: 1.05x slower                                 |
| Geometric mean  | (ref)                                                  | 1.03x slower                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220405-linux-x86_64-python-main-3.11.0a7-2e49bd0 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot            | 3.99 ms                                                | 3.34 ms: 1.20x faster                                 |
| pickle_dict             | 31.1 us                                                | 27.6 us: 1.13x faster                                 |
| python_startup          | 8.52 ms                                                | 8.07 ms: 1.06x faster                                 |
| pickle                  | 10.1 us                                                | 9.55 us: 1.05x faster                                 |
| logging_format          | 6.68 us                                                | 6.35 us: 1.05x faster                                 |
| sympy_sum               | 167 ms                                                 | 160 ms: 1.04x faster                                  |
| logging_simple          | 6.03 us                                                | 5.80 us: 1.04x faster                                 |
| float                   | 77.2 ms                                                | 74.4 ms: 1.04x faster                                 |
| sympy_integrate         | 21.0 ms                                                | 20.5 ms: 1.02x faster                                 |
| scimark_lu              | 110 ms                                                 | 108 ms: 1.01x faster                                  |
| xml_etree_parse         | 158 ms                                                 | 157 ms: 1.01x faster                                  |
| tornado_http            | 96.3 ms                                                | 95.4 ms: 1.01x faster                                 |
| sympy_str               | 290 ms                                                 | 287 ms: 1.01x faster                                  |
| json_dumps              | 12.6 ms                                                | 12.5 ms: 1.01x faster                                 |
| pidigits                | 198 ms                                                 | 197 ms: 1.00x faster                                  |
| regex_compile           | 138 ms                                                 | 137 ms: 1.00x faster                                  |
| python_startup_no_site  | 6.01 ms                                                | 5.98 ms: 1.00x faster                                 |
| deltablue               | 3.67 ms                                                | 3.70 ms: 1.01x slower                                 |
| thrift                  | 756 us                                                 | 762 us: 1.01x slower                                  |
| mako                    | 10.1 ms                                                | 10.2 ms: 1.01x slower                                 |
| unpickle_pure_python    | 228 us                                                 | 231 us: 1.01x slower                                  |
| unpickle_list           | 4.91 us                                                | 4.97 us: 1.01x slower                                 |
| pathlib                 | 18.2 ms                                                | 18.5 ms: 1.01x slower                                 |
| chaos                   | 69.2 ms                                                | 70.2 ms: 1.02x slower                                 |
| pickle_pure_python      | 306 us                                                 | 311 us: 1.02x slower                                  |
| go                      | 140 ms                                                 | 143 ms: 1.02x slower                                  |
| scimark_fft             | 328 ms                                                 | 335 ms: 1.02x slower                                  |
| 2to3                    | 259 ms                                                 | 264 ms: 1.02x slower                                  |
| nbody                   | 93.1 ms                                                | 95.2 ms: 1.02x slower                                 |
| nqueens                 | 83.4 ms                                                | 85.2 ms: 1.02x slower                                 |
| json                    | 4.94 ms                                                | 5.07 ms: 1.03x slower                                 |
| xml_etree_process       | 53.9 ms                                                | 55.2 ms: 1.03x slower                                 |
| logging_silent          | 101 ns                                                 | 104 ns: 1.03x slower                                  |
| xml_etree_generate      | 76.2 ms                                                | 78.5 ms: 1.03x slower                                 |
| raytrace                | 297 ms                                                 | 306 ms: 1.03x slower                                  |
| fannkuch                | 388 ms                                                 | 401 ms: 1.03x slower                                  |
| richards                | 45.7 ms                                                | 47.5 ms: 1.04x slower                                 |
| scimark_monte_carlo     | 68.1 ms                                                | 70.8 ms: 1.04x slower                                 |
| scimark_sor             | 118 ms                                                 | 123 ms: 1.04x slower                                  |
| unpack_sequence         | 43.1 ns                                                | 44.9 ns: 1.04x slower                                 |
| spectral_norm           | 100 ms                                                 | 105 ms: 1.04x slower                                  |
| pyflate                 | 418 ms                                                 | 438 ms: 1.05x slower                                  |
| pycparser               | 1.18 sec                                               | 1.24 sec: 1.05x slower                                |
| django_template         | 32.6 ms                                                | 34.3 ms: 1.05x slower                                 |
| json_loads              | 26.5 us                                                | 28.1 us: 1.06x slower                                 |
| chameleon               | 6.47 ms                                                | 6.87 ms: 1.06x slower                                 |
| hexiom                  | 6.37 ms                                                | 6.84 ms: 1.07x slower                                 |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.85 ms: 1.08x slower                                 |
| crypto_pyaes            | 74.7 ms                                                | 82.7 ms: 1.11x slower                                 |
| pickle_list             | 4.11 us                                                | 4.57 us: 1.11x slower                                 |
| regex_dna               | 204 ms                                                 | 231 ms: 1.13x slower                                  |
| regex_v8                | 22.0 ms                                                | 25.9 ms: 1.17x slower                                 |
| Geometric mean          | (ref)                                                  | 1.01x slower                                          |

Benchmark hidden because not significant (8): sqlite_synth, xml_etree_iterparse, meteor_contest, telco, dulwich_log, sympy_expand, html5lib, unpickle
Ignored benchmarks (40) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 99.90% likely to be slow
- 90% likely to have a slowdown of 1.01x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
