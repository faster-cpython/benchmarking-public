
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 733e15f
- commit date: 2022-06-11
- overall geometric mean: 1.03x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220611-linux-x86_64-python-main-3.12.0a1+-733e15f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                   |
| chameleon      | 6.47 ms                                                | 6.40 ms: 1.01x faster                                  |
| html5lib       | 64.5 ms                                                | 63.4 ms: 1.02x faster                                  |
| tornado_http   | 96.3 ms                                                | 91.3 ms: 1.06x faster                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220611-linux-x86_64-python-main-3.12.0a1+-733e15f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 77.2 ms                                                | 71.0 ms: 1.09x faster                                  |
| nbody          | 93.1 ms                                                | 91.3 ms: 1.02x faster                                  |
| pidigits       | 198 ms                                                 | 197 ms: 1.01x faster                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220611-linux-x86_64-python-main-3.12.0a1+-733e15f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.01 ms: 1.33x faster                                  |
| regex_compile  | 138 ms                                                 | 132 ms: 1.04x faster                                   |
| regex_v8       | 22.0 ms                                                | 21.3 ms: 1.04x faster                                  |
| regex_dna      | 204 ms                                                 | 198 ms: 1.03x faster                                   |
| Geometric mean | (ref)                                                  | 1.10x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220611-linux-x86_64-python-main-3.12.0a1+-733e15f |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| unpickle_pure_python | 228 us                                                 | 212 us: 1.07x faster                                   |
| json_loads           | 26.5 us                                                | 25.1 us: 1.06x faster                                  |
| json_dumps           | 12.6 ms                                                | 12.0 ms: 1.05x faster                                  |
| pickle_pure_python   | 306 us                                                 | 293 us: 1.04x faster                                   |
| xml_etree_process    | 53.9 ms                                                | 52.1 ms: 1.03x faster                                  |
| pickle_dict          | 31.1 us                                                | 30.6 us: 1.02x faster                                  |
| xml_etree_generate   | 76.2 ms                                                | 75.4 ms: 1.01x faster                                  |
| pickle               | 10.1 us                                                | 10.3 us: 1.02x slower                                  |
| Geometric mean       | (ref)                                                  | 1.02x faster                                           |

Benchmark hidden because not significant (5): unpickle_list, pickle_list, xml_etree_iterparse, xml_etree_parse, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220611-linux-x86_64-python-main-3.12.0a1+-733e15f |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.26 ms: 1.03x faster                                  |
| python_startup_no_site | 6.01 ms                                                | 6.11 ms: 1.02x slower                                  |
| Geometric mean         | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220611-linux-x86_64-python-main-3.12.0a1+-733e15f |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| django_template | 32.6 ms                                                | 31.2 ms: 1.04x faster                                  |
| mako            | 10.1 ms                                                | 9.74 ms: 1.04x faster                                  |
| Geometric mean  | (ref)                                                  | 1.04x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220611-linux-x86_64-python-main-3.12.0a1+-733e15f |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot            | 3.99 ms                                                | 3.01 ms: 1.33x faster                                  |
| pycparser               | 1.18 sec                                               | 1.07 sec: 1.11x faster                                 |
| float                   | 77.2 ms                                                | 71.0 ms: 1.09x faster                                  |
| scimark_lu              | 110 ms                                                 | 102 ms: 1.08x faster                                   |
| unpickle_pure_python    | 228 us                                                 | 212 us: 1.07x faster                                   |
| scimark_sor             | 118 ms                                                 | 110 ms: 1.07x faster                                   |
| go                      | 140 ms                                                 | 131 ms: 1.06x faster                                   |
| json_loads              | 26.5 us                                                | 25.1 us: 1.06x faster                                  |
| raytrace                | 297 ms                                                 | 281 ms: 1.06x faster                                   |
| tornado_http            | 96.3 ms                                                | 91.3 ms: 1.06x faster                                  |
| logging_format          | 6.68 us                                                | 6.36 us: 1.05x faster                                  |
| spectral_norm           | 100 ms                                                 | 95.3 ms: 1.05x faster                                  |
| richards                | 45.7 ms                                                | 43.6 ms: 1.05x faster                                  |
| meteor_contest          | 107 ms                                                 | 102 ms: 1.05x faster                                   |
| json_dumps              | 12.6 ms                                                | 12.0 ms: 1.05x faster                                  |
| deltablue               | 3.67 ms                                                | 3.51 ms: 1.05x faster                                  |
| pyflate                 | 418 ms                                                 | 400 ms: 1.05x faster                                   |
| sympy_sum               | 167 ms                                                 | 159 ms: 1.05x faster                                   |
| django_template         | 32.6 ms                                                | 31.2 ms: 1.04x faster                                  |
| pickle_pure_python      | 306 us                                                 | 293 us: 1.04x faster                                   |
| scimark_fft             | 328 ms                                                 | 315 ms: 1.04x faster                                   |
| regex_compile           | 138 ms                                                 | 132 ms: 1.04x faster                                   |
| sympy_expand            | 475 ms                                                 | 457 ms: 1.04x faster                                   |
| sympy_integrate         | 21.0 ms                                                | 20.2 ms: 1.04x faster                                  |
| regex_v8                | 22.0 ms                                                | 21.3 ms: 1.04x faster                                  |
| mako                    | 10.1 ms                                                | 9.74 ms: 1.04x faster                                  |
| json                    | 4.94 ms                                                | 4.78 ms: 1.03x faster                                  |
| xml_etree_process       | 53.9 ms                                                | 52.1 ms: 1.03x faster                                  |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                   |
| logging_simple          | 6.03 us                                                | 5.84 us: 1.03x faster                                  |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.36 ms: 1.03x faster                                  |
| hexiom                  | 6.37 ms                                                | 6.17 ms: 1.03x faster                                  |
| python_startup          | 8.52 ms                                                | 8.26 ms: 1.03x faster                                  |
| regex_dna               | 204 ms                                                 | 198 ms: 1.03x faster                                   |
| dulwich_log             | 63.7 ms                                                | 61.9 ms: 1.03x faster                                  |
| sympy_str               | 290 ms                                                 | 283 ms: 1.03x faster                                   |
| pathlib                 | 18.2 ms                                                | 17.8 ms: 1.02x faster                                  |
| nbody                   | 93.1 ms                                                | 91.3 ms: 1.02x faster                                  |
| thrift                  | 756 us                                                 | 741 us: 1.02x faster                                   |
| scimark_monte_carlo     | 68.1 ms                                                | 66.7 ms: 1.02x faster                                  |
| logging_silent          | 101 ns                                                 | 99.2 ns: 1.02x faster                                  |
| telco                   | 6.58 ms                                                | 6.46 ms: 1.02x faster                                  |
| pickle_dict             | 31.1 us                                                | 30.6 us: 1.02x faster                                  |
| html5lib                | 64.5 ms                                                | 63.4 ms: 1.02x faster                                  |
| chaos                   | 69.2 ms                                                | 68.0 ms: 1.02x faster                                  |
| fannkuch                | 388 ms                                                 | 382 ms: 1.02x faster                                   |
| chameleon               | 6.47 ms                                                | 6.40 ms: 1.01x faster                                  |
| xml_etree_generate      | 76.2 ms                                                | 75.4 ms: 1.01x faster                                  |
| crypto_pyaes            | 74.7 ms                                                | 74.0 ms: 1.01x faster                                  |
| pidigits                | 198 ms                                                 | 197 ms: 1.01x faster                                   |
| sqlite_synth            | 2.52 us                                                | 2.50 us: 1.01x faster                                  |
| unpack_sequence         | 43.1 ns                                                | 43.6 ns: 1.01x slower                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.11 ms: 1.02x slower                                  |
| pickle                  | 10.1 us                                                | 10.3 us: 1.02x slower                                  |
| Geometric mean          | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (6): unpickle_list, pickle_list, nqueens, xml_etree_iterparse, xml_etree_parse, unpickle
Ignored benchmarks (40) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
