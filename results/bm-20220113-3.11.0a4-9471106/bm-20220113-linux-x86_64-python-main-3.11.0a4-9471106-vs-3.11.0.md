
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 9471106
- commit date: 2022-01-13
- overall geometric mean: 1.03x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 259 ms                                                 | 264 ms: 1.02x slower                                  |
| chameleon      | 6.47 ms                                                | 7.55 ms: 1.17x slower                                 |
| html5lib       | 64.5 ms                                                | 68.1 ms: 1.06x slower                                 |
| tornado_http   | 96.3 ms                                                | 107 ms: 1.11x slower                                  |
| Geometric mean | (ref)                                                  | 1.09x slower                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pidigits       | 198 ms                                                 | 194 ms: 1.02x faster                                  |
| float          | 77.2 ms                                                | 78.0 ms: 1.01x slower                                 |
| nbody          | 93.1 ms                                                | 95.1 ms: 1.02x slower                                 |
| Geometric mean | (ref)                                                  | 1.00x slower                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106 |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.25 ms: 1.23x faster                                 |
| regex_dna      | 204 ms                                                 | 212 ms: 1.04x slower                                  |
| regex_v8       | 22.0 ms                                                | 24.8 ms: 1.13x slower                                 |
| Geometric mean | (ref)                                                  | 1.01x faster                                          |

Benchmark hidden because not significant (1): regex_compile

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106 |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_dict          | 31.1 us                                                | 26.8 us: 1.16x faster                                 |
| json_loads           | 26.5 us                                                | 25.1 us: 1.06x faster                                 |
| xml_etree_parse      | 158 ms                                                 | 155 ms: 1.03x faster                                  |
| json_dumps           | 12.6 ms                                                | 12.4 ms: 1.02x faster                                 |
| pickle               | 10.1 us                                                | 9.95 us: 1.01x faster                                 |
| xml_etree_iterparse  | 104 ms                                                 | 107 ms: 1.03x slower                                  |
| unpickle             | 13.7 us                                                | 14.3 us: 1.04x slower                                 |
| xml_etree_generate   | 76.2 ms                                                | 80.2 ms: 1.05x slower                                 |
| xml_etree_process    | 53.9 ms                                                | 56.9 ms: 1.06x slower                                 |
| unpickle_list        | 4.91 us                                                | 5.20 us: 1.06x slower                                 |
| pickle_list          | 4.11 us                                                | 4.37 us: 1.06x slower                                 |
| pickle_pure_python   | 306 us                                                 | 329 us: 1.08x slower                                  |
| unpickle_pure_python | 228 us                                                 | 254 us: 1.11x slower                                  |
| Geometric mean       | (ref)                                                  | 1.02x slower                                          |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106 |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.07 ms: 1.06x faster                                 |
| python_startup_no_site | 6.01 ms                                                | 5.85 ms: 1.03x faster                                 |
| Geometric mean         | (ref)                                                  | 1.04x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106 |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| django_template | 32.6 ms                                                | 35.2 ms: 1.08x slower                                 |
| mako            | 10.1 ms                                                | 11.5 ms: 1.14x slower                                 |
| Geometric mean  | (ref)                                                  | 1.11x slower                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220113-linux-x86_64-python-main-3.11.0a4-9471106 |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot            | 3.99 ms                                                | 3.25 ms: 1.23x faster                                 |
| pickle_dict             | 31.1 us                                                | 26.8 us: 1.16x faster                                 |
| json_loads              | 26.5 us                                                | 25.1 us: 1.06x faster                                 |
| python_startup          | 8.52 ms                                                | 8.07 ms: 1.06x faster                                 |
| json                    | 4.94 ms                                                | 4.74 ms: 1.04x faster                                 |
| meteor_contest          | 107 ms                                                 | 103 ms: 1.04x faster                                  |
| logging_format          | 6.68 us                                                | 6.51 us: 1.03x faster                                 |
| python_startup_no_site  | 6.01 ms                                                | 5.85 ms: 1.03x faster                                 |
| xml_etree_parse         | 158 ms                                                 | 155 ms: 1.03x faster                                  |
| pidigits                | 198 ms                                                 | 194 ms: 1.02x faster                                  |
| json_dumps              | 12.6 ms                                                | 12.4 ms: 1.02x faster                                 |
| logging_simple          | 6.03 us                                                | 5.95 us: 1.01x faster                                 |
| pycparser               | 1.18 sec                                               | 1.17 sec: 1.01x faster                                |
| pickle                  | 10.1 us                                                | 9.95 us: 1.01x faster                                 |
| spectral_norm           | 100 ms                                                 | 99.0 ms: 1.01x faster                                 |
| scimark_fft             | 328 ms                                                 | 330 ms: 1.00x slower                                  |
| nqueens                 | 83.4 ms                                                | 84.0 ms: 1.01x slower                                 |
| fannkuch                | 388 ms                                                 | 392 ms: 1.01x slower                                  |
| float                   | 77.2 ms                                                | 78.0 ms: 1.01x slower                                 |
| telco                   | 6.58 ms                                                | 6.69 ms: 1.02x slower                                 |
| sympy_sum               | 167 ms                                                 | 170 ms: 1.02x slower                                  |
| 2to3                    | 259 ms                                                 | 264 ms: 1.02x slower                                  |
| sympy_integrate         | 21.0 ms                                                | 21.4 ms: 1.02x slower                                 |
| nbody                   | 93.1 ms                                                | 95.1 ms: 1.02x slower                                 |
| xml_etree_iterparse     | 104 ms                                                 | 107 ms: 1.03x slower                                  |
| dulwich_log             | 63.7 ms                                                | 65.8 ms: 1.03x slower                                 |
| scimark_lu              | 110 ms                                                 | 114 ms: 1.04x slower                                  |
| unpack_sequence         | 43.1 ns                                                | 44.8 ns: 1.04x slower                                 |
| regex_dna               | 204 ms                                                 | 212 ms: 1.04x slower                                  |
| sympy_str               | 290 ms                                                 | 302 ms: 1.04x slower                                  |
| hexiom                  | 6.37 ms                                                | 6.63 ms: 1.04x slower                                 |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.69 ms: 1.04x slower                                 |
| unpickle                | 13.7 us                                                | 14.3 us: 1.04x slower                                 |
| pathlib                 | 18.2 ms                                                | 19.1 ms: 1.05x slower                                 |
| chaos                   | 69.2 ms                                                | 72.7 ms: 1.05x slower                                 |
| xml_etree_generate      | 76.2 ms                                                | 80.2 ms: 1.05x slower                                 |
| scimark_sor             | 118 ms                                                 | 124 ms: 1.05x slower                                  |
| html5lib                | 64.5 ms                                                | 68.1 ms: 1.06x slower                                 |
| xml_etree_process       | 53.9 ms                                                | 56.9 ms: 1.06x slower                                 |
| go                      | 140 ms                                                 | 148 ms: 1.06x slower                                  |
| unpickle_list           | 4.91 us                                                | 5.20 us: 1.06x slower                                 |
| pyflate                 | 418 ms                                                 | 444 ms: 1.06x slower                                  |
| pickle_list             | 4.11 us                                                | 4.37 us: 1.06x slower                                 |
| sympy_expand            | 475 ms                                                 | 506 ms: 1.07x slower                                  |
| scimark_monte_carlo     | 68.1 ms                                                | 72.7 ms: 1.07x slower                                 |
| thrift                  | 756 us                                                 | 812 us: 1.07x slower                                  |
| pickle_pure_python      | 306 us                                                 | 329 us: 1.08x slower                                  |
| raytrace                | 297 ms                                                 | 320 ms: 1.08x slower                                  |
| django_template         | 32.6 ms                                                | 35.2 ms: 1.08x slower                                 |
| sqlite_synth            | 2.52 us                                                | 2.73 us: 1.08x slower                                 |
| tornado_http            | 96.3 ms                                                | 107 ms: 1.11x slower                                  |
| unpickle_pure_python    | 228 us                                                 | 254 us: 1.11x slower                                  |
| crypto_pyaes            | 74.7 ms                                                | 83.8 ms: 1.12x slower                                 |
| logging_silent          | 101 ns                                                 | 113 ns: 1.12x slower                                  |
| regex_v8                | 22.0 ms                                                | 24.8 ms: 1.13x slower                                 |
| richards                | 45.7 ms                                                | 51.5 ms: 1.13x slower                                 |
| deltablue               | 3.67 ms                                                | 4.16 ms: 1.13x slower                                 |
| mako                    | 10.1 ms                                                | 11.5 ms: 1.14x slower                                 |
| chameleon               | 6.47 ms                                                | 7.55 ms: 1.17x slower                                 |
| Geometric mean          | (ref)                                                  | 1.03x slower                                          |

Benchmark hidden because not significant (1): regex_compile
Ignored benchmarks (40) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.02x
- 95% likely to have a slowdown of 1.01x
- 99% likely to have a slowdown of 1.01x
