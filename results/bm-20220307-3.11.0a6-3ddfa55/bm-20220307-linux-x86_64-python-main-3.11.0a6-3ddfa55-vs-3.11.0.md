
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 3ddfa55
- commit date: 2022-03-07
- overall geometric mean: 1.05x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220307-linux-x86_64-python-main-3.11.0a6-3ddfa55 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 259 ms                                                 | 268 ms: 1.03x slower                                  |
| chameleon      | 6.47 ms                                                | 6.93 ms: 1.07x slower                                 |
| html5lib       | 64.5 ms                                                | 68.6 ms: 1.06x slower                                 |
| tornado_http   | 96.3 ms                                                | 99.2 ms: 1.03x slower                                 |
| Geometric mean | (ref)                                                  | 1.05x slower                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220307-linux-x86_64-python-main-3.11.0a6-3ddfa55 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| float          | 77.2 ms                                                | 78.7 ms: 1.02x slower                                 |
| nbody          | 93.1 ms                                                | 97.7 ms: 1.05x slower                                 |
| pidigits       | 198 ms                                                 | 208 ms: 1.05x slower                                  |
| Geometric mean | (ref)                                                  | 1.04x slower                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220307-linux-x86_64-python-main-3.11.0a6-3ddfa55 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.49 ms: 1.15x faster                                 |
| regex_compile  | 138 ms                                                 | 140 ms: 1.01x slower                                  |
| regex_v8       | 22.0 ms                                                | 23.0 ms: 1.04x slower                                 |
| regex_dna      | 204 ms                                                 | 221 ms: 1.08x slower                                  |
| Geometric mean | (ref)                                                  | 1.00x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220307-linux-x86_64-python-main-3.11.0a6-3ddfa55 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_dict          | 31.1 us                                                | 28.1 us: 1.11x faster                                 |
| pickle               | 10.1 us                                                | 9.69 us: 1.04x faster                                 |
| xml_etree_parse      | 158 ms                                                 | 156 ms: 1.01x faster                                  |
| xml_etree_iterparse  | 104 ms                                                 | 105 ms: 1.01x slower                                  |
| unpickle             | 13.7 us                                                | 14.2 us: 1.04x slower                                 |
| xml_etree_process    | 53.9 ms                                                | 56.0 ms: 1.04x slower                                 |
| xml_etree_generate   | 76.2 ms                                                | 79.6 ms: 1.04x slower                                 |
| json_loads           | 26.5 us                                                | 28.1 us: 1.06x slower                                 |
| unpickle_pure_python | 228 us                                                 | 246 us: 1.08x slower                                  |
| pickle_list          | 4.11 us                                                | 4.51 us: 1.10x slower                                 |
| pickle_pure_python   | 306 us                                                 | 335 us: 1.10x slower                                  |
| Geometric mean       | (ref)                                                  | 1.02x slower                                          |

Benchmark hidden because not significant (2): json_dumps, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220307-linux-x86_64-python-main-3.11.0a6-3ddfa55 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.20 ms: 1.04x faster                                 |
| python_startup_no_site | 6.01 ms                                                | 6.07 ms: 1.01x slower                                 |
| Geometric mean         | (ref)                                                  | 1.01x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220307-linux-x86_64-python-main-3.11.0a6-3ddfa55 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| mako            | 10.1 ms                                                | 10.6 ms: 1.05x slower                                 |
| django_template | 32.6 ms                                                | 36.0 ms: 1.10x slower                                 |
| Geometric mean  | (ref)                                                  | 1.08x slower                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220307-linux-x86_64-python-main-3.11.0a6-3ddfa55 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot            | 3.99 ms                                                | 3.49 ms: 1.15x faster                                 |
| pickle_dict             | 31.1 us                                                | 28.1 us: 1.11x faster                                 |
| logging_format          | 6.68 us                                                | 6.08 us: 1.10x faster                                 |
| logging_simple          | 6.03 us                                                | 5.52 us: 1.09x faster                                 |
| python_startup          | 8.52 ms                                                | 8.20 ms: 1.04x faster                                 |
| pickle                  | 10.1 us                                                | 9.69 us: 1.04x faster                                 |
| sympy_sum               | 167 ms                                                 | 163 ms: 1.02x faster                                  |
| xml_etree_parse         | 158 ms                                                 | 156 ms: 1.01x faster                                  |
| sympy_integrate         | 21.0 ms                                                | 20.9 ms: 1.01x faster                                 |
| xml_etree_iterparse     | 104 ms                                                 | 105 ms: 1.01x slower                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.07 ms: 1.01x slower                                 |
| json                    | 4.94 ms                                                | 5.00 ms: 1.01x slower                                 |
| regex_compile           | 138 ms                                                 | 140 ms: 1.01x slower                                  |
| sympy_expand            | 475 ms                                                 | 481 ms: 1.01x slower                                  |
| float                   | 77.2 ms                                                | 78.7 ms: 1.02x slower                                 |
| scimark_fft             | 328 ms                                                 | 336 ms: 1.02x slower                                  |
| fannkuch                | 388 ms                                                 | 398 ms: 1.03x slower                                  |
| pycparser               | 1.18 sec                                               | 1.21 sec: 1.03x slower                                |
| tornado_http            | 96.3 ms                                                | 99.2 ms: 1.03x slower                                 |
| 2to3                    | 259 ms                                                 | 268 ms: 1.03x slower                                  |
| unpickle                | 13.7 us                                                | 14.2 us: 1.04x slower                                 |
| xml_etree_process       | 53.9 ms                                                | 56.0 ms: 1.04x slower                                 |
| regex_v8                | 22.0 ms                                                | 23.0 ms: 1.04x slower                                 |
| thrift                  | 756 us                                                 | 789 us: 1.04x slower                                  |
| nqueens                 | 83.4 ms                                                | 87.0 ms: 1.04x slower                                 |
| xml_etree_generate      | 76.2 ms                                                | 79.6 ms: 1.04x slower                                 |
| dulwich_log             | 63.7 ms                                                | 66.5 ms: 1.05x slower                                 |
| scimark_sor             | 118 ms                                                 | 123 ms: 1.05x slower                                  |
| nbody                   | 93.1 ms                                                | 97.7 ms: 1.05x slower                                 |
| telco                   | 6.58 ms                                                | 6.92 ms: 1.05x slower                                 |
| pidigits                | 198 ms                                                 | 208 ms: 1.05x slower                                  |
| mako                    | 10.1 ms                                                | 10.6 ms: 1.05x slower                                 |
| scimark_lu              | 110 ms                                                 | 115 ms: 1.05x slower                                  |
| go                      | 140 ms                                                 | 148 ms: 1.05x slower                                  |
| richards                | 45.7 ms                                                | 48.5 ms: 1.06x slower                                 |
| json_loads              | 26.5 us                                                | 28.1 us: 1.06x slower                                 |
| chaos                   | 69.2 ms                                                | 73.5 ms: 1.06x slower                                 |
| html5lib                | 64.5 ms                                                | 68.6 ms: 1.06x slower                                 |
| chameleon               | 6.47 ms                                                | 6.93 ms: 1.07x slower                                 |
| scimark_monte_carlo     | 68.1 ms                                                | 72.9 ms: 1.07x slower                                 |
| raytrace                | 297 ms                                                 | 318 ms: 1.07x slower                                  |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.82 ms: 1.07x slower                                 |
| spectral_norm           | 100 ms                                                 | 107 ms: 1.07x slower                                  |
| unpickle_pure_python    | 228 us                                                 | 246 us: 1.08x slower                                  |
| regex_dna               | 204 ms                                                 | 221 ms: 1.08x slower                                  |
| pyflate                 | 418 ms                                                 | 453 ms: 1.08x slower                                  |
| pickle_list             | 4.11 us                                                | 4.51 us: 1.10x slower                                 |
| pickle_pure_python      | 306 us                                                 | 335 us: 1.10x slower                                  |
| hexiom                  | 6.37 ms                                                | 7.04 ms: 1.10x slower                                 |
| django_template         | 32.6 ms                                                | 36.0 ms: 1.10x slower                                 |
| logging_silent          | 101 ns                                                 | 113 ns: 1.11x slower                                  |
| crypto_pyaes            | 74.7 ms                                                | 84.6 ms: 1.13x slower                                 |
| deltablue               | 3.67 ms                                                | 4.16 ms: 1.13x slower                                 |
| unpack_sequence         | 43.1 ns                                                | 131 ns: 3.04x slower                                  |
| Geometric mean          | (ref)                                                  | 1.05x slower                                          |

Benchmark hidden because not significant (6): meteor_contest, sqlite_synth, sympy_str, pathlib, json_dumps, unpickle_list
Ignored benchmarks (40) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x
