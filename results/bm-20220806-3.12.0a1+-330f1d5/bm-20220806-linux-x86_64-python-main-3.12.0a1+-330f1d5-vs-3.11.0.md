
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 330f1d5
- commit date: 2022-08-06
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220806-linux-x86_64-python-main-3.12.0a1+-330f1d5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 248 ms: 1.04x faster                                   |
| chameleon      | 6.47 ms                                                | 6.50 ms: 1.00x slower                                  |
| html5lib       | 64.5 ms                                                | 62.6 ms: 1.03x faster                                  |
| tornado_http   | 96.3 ms                                                | 91.7 ms: 1.05x faster                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220806-linux-x86_64-python-main-3.12.0a1+-330f1d5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 77.2 ms                                                | 74.1 ms: 1.04x faster                                  |
| pidigits       | 198 ms                                                 | 194 ms: 1.02x faster                                   |
| nbody          | 93.1 ms                                                | 91.3 ms: 1.02x faster                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220806-linux-x86_64-python-main-3.12.0a1+-330f1d5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.50 ms: 1.14x faster                                  |
| regex_compile  | 138 ms                                                 | 127 ms: 1.09x faster                                   |
| regex_v8       | 22.0 ms                                                | 20.8 ms: 1.06x faster                                  |
| regex_dna      | 204 ms                                                 | 203 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220806-linux-x86_64-python-main-3.12.0a1+-330f1d5 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.51 ms: 1.32x faster                                  |
| unpickle_pure_python | 228 us                                                 | 199 us: 1.14x faster                                   |
| json_loads           | 26.5 us                                                | 24.6 us: 1.08x faster                                  |
| pickle_pure_python   | 306 us                                                 | 288 us: 1.06x faster                                   |
| xml_etree_process    | 53.9 ms                                                | 52.2 ms: 1.03x faster                                  |
| unpickle             | 13.7 us                                                | 13.3 us: 1.03x faster                                  |
| xml_etree_generate   | 76.2 ms                                                | 75.0 ms: 1.02x faster                                  |
| xml_etree_parse      | 158 ms                                                 | 156 ms: 1.01x faster                                   |
| xml_etree_iterparse  | 104 ms                                                 | 105 ms: 1.01x slower                                   |
| pickle_dict          | 31.1 us                                                | 31.9 us: 1.03x slower                                  |
| pickle               | 10.1 us                                                | 10.4 us: 1.03x slower                                  |
| unpickle_list        | 4.91 us                                                | 5.06 us: 1.03x slower                                  |
| pickle_list          | 4.11 us                                                | 4.26 us: 1.04x slower                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220806-linux-x86_64-python-main-3.12.0a1+-330f1d5 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.15 ms: 1.05x faster                                  |
| python_startup_no_site | 6.01 ms                                                | 6.01 ms: 1.00x slower                                  |
| Geometric mean         | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220806-linux-x86_64-python-main-3.12.0a1+-330f1d5 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako           | 10.1 ms                                                | 9.50 ms: 1.06x faster                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220806-linux-x86_64-python-main-3.12.0a1+-330f1d5 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps              | 12.6 ms                                                | 9.51 ms: 1.32x faster                                  |
| scimark_sparse_mat_mult | 4.50 ms                                                | 3.91 ms: 1.15x faster                                  |
| unpickle_pure_python    | 228 us                                                 | 199 us: 1.14x faster                                   |
| deltablue               | 3.67 ms                                                | 3.21 ms: 1.14x faster                                  |
| regex_effbot            | 3.99 ms                                                | 3.50 ms: 1.14x faster                                  |
| pycparser               | 1.18 sec                                               | 1.04 sec: 1.13x faster                                 |
| logging_silent          | 101 ns                                                 | 89.9 ns: 1.12x faster                                  |
| regex_compile           | 138 ms                                                 | 127 ms: 1.09x faster                                   |
| json_loads              | 26.5 us                                                | 24.6 us: 1.08x faster                                  |
| scimark_sor             | 118 ms                                                 | 110 ms: 1.07x faster                                   |
| go                      | 140 ms                                                 | 131 ms: 1.07x faster                                   |
| raytrace                | 297 ms                                                 | 278 ms: 1.07x faster                                   |
| spectral_norm           | 100 ms                                                 | 93.8 ms: 1.07x faster                                  |
| hexiom                  | 6.37 ms                                                | 5.98 ms: 1.07x faster                                  |
| pyflate                 | 418 ms                                                 | 393 ms: 1.06x faster                                   |
| mako                    | 10.1 ms                                                | 9.50 ms: 1.06x faster                                  |
| regex_v8                | 22.0 ms                                                | 20.8 ms: 1.06x faster                                  |
| pickle_pure_python      | 306 us                                                 | 288 us: 1.06x faster                                   |
| scimark_monte_carlo     | 68.1 ms                                                | 64.2 ms: 1.06x faster                                  |
| scimark_fft             | 328 ms                                                 | 311 ms: 1.06x faster                                   |
| logging_simple          | 6.03 us                                                | 5.72 us: 1.06x faster                                  |
| logging_format          | 6.68 us                                                | 6.34 us: 1.05x faster                                  |
| nqueens                 | 83.4 ms                                                | 79.2 ms: 1.05x faster                                  |
| meteor_contest          | 107 ms                                                 | 101 ms: 1.05x faster                                   |
| json                    | 4.94 ms                                                | 4.70 ms: 1.05x faster                                  |
| tornado_http            | 96.3 ms                                                | 91.7 ms: 1.05x faster                                  |
| python_startup          | 8.52 ms                                                | 8.15 ms: 1.05x faster                                  |
| float                   | 77.2 ms                                                | 74.1 ms: 1.04x faster                                  |
| 2to3                    | 259 ms                                                 | 248 ms: 1.04x faster                                   |
| dulwich_log             | 63.7 ms                                                | 61.2 ms: 1.04x faster                                  |
| pathlib                 | 18.2 ms                                                | 17.6 ms: 1.04x faster                                  |
| sympy_sum               | 167 ms                                                 | 160 ms: 1.04x faster                                   |
| fannkuch                | 388 ms                                                 | 374 ms: 1.04x faster                                   |
| scimark_lu              | 110 ms                                                 | 106 ms: 1.04x faster                                   |
| chaos                   | 69.2 ms                                                | 66.8 ms: 1.04x faster                                  |
| sympy_integrate         | 21.0 ms                                                | 20.3 ms: 1.03x faster                                  |
| xml_etree_process       | 53.9 ms                                                | 52.2 ms: 1.03x faster                                  |
| html5lib                | 64.5 ms                                                | 62.6 ms: 1.03x faster                                  |
| unpickle                | 13.7 us                                                | 13.3 us: 1.03x faster                                  |
| sympy_expand            | 475 ms                                                 | 461 ms: 1.03x faster                                   |
| sympy_str               | 290 ms                                                 | 282 ms: 1.03x faster                                   |
| crypto_pyaes            | 74.7 ms                                                | 72.6 ms: 1.03x faster                                  |
| telco                   | 6.58 ms                                                | 6.41 ms: 1.03x faster                                  |
| richards                | 45.7 ms                                                | 44.5 ms: 1.03x faster                                  |
| pidigits                | 198 ms                                                 | 194 ms: 1.02x faster                                   |
| nbody                   | 93.1 ms                                                | 91.3 ms: 1.02x faster                                  |
| xml_etree_generate      | 76.2 ms                                                | 75.0 ms: 1.02x faster                                  |
| xml_etree_parse         | 158 ms                                                 | 156 ms: 1.01x faster                                   |
| thrift                  | 756 us                                                 | 748 us: 1.01x faster                                   |
| regex_dna               | 204 ms                                                 | 203 ms: 1.00x faster                                   |
| python_startup_no_site  | 6.01 ms                                                | 6.01 ms: 1.00x slower                                  |
| chameleon               | 6.47 ms                                                | 6.50 ms: 1.00x slower                                  |
| xml_etree_iterparse     | 104 ms                                                 | 105 ms: 1.01x slower                                   |
| pickle_dict             | 31.1 us                                                | 31.9 us: 1.03x slower                                  |
| sqlite_synth            | 2.52 us                                                | 2.59 us: 1.03x slower                                  |
| pickle                  | 10.1 us                                                | 10.4 us: 1.03x slower                                  |
| unpickle_list           | 4.91 us                                                | 5.06 us: 1.03x slower                                  |
| pickle_list             | 4.11 us                                                | 4.26 us: 1.04x slower                                  |
| unpack_sequence         | 43.1 ns                                                | 45.9 ns: 1.07x slower                                  |
| Geometric mean          | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (1): django_template
Ignored benchmarks (40) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x
