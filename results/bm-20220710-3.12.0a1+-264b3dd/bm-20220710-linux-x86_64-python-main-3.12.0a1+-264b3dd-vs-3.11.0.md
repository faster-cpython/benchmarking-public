
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 264b3dd
- commit date: 2022-07-10
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220710-linux-x86_64-python-main-3.12.0a1+-264b3dd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 249 ms: 1.04x faster                                   |
| chameleon      | 6.47 ms                                                | 6.30 ms: 1.03x faster                                  |
| html5lib       | 64.5 ms                                                | 62.6 ms: 1.03x faster                                  |
| tornado_http   | 96.3 ms                                                | 91.3 ms: 1.05x faster                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220710-linux-x86_64-python-main-3.12.0a1+-264b3dd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.4 ms: 1.07x faster                                  |
| nbody          | 93.1 ms                                                | 90.5 ms: 1.03x faster                                  |
| pidigits       | 198 ms                                                 | 193 ms: 1.03x faster                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220710-linux-x86_64-python-main-3.12.0a1+-264b3dd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.54 ms: 1.13x faster                                  |
| regex_compile  | 138 ms                                                 | 126 ms: 1.10x faster                                   |
| regex_dna      | 204 ms                                                 | 207 ms: 1.01x slower                                   |
| Geometric mean | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (1): regex_v8

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220710-linux-x86_64-python-main-3.12.0a1+-264b3dd |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| unpickle_pure_python | 228 us                                                 | 201 us: 1.13x faster                                   |
| json_loads           | 26.5 us                                                | 24.2 us: 1.09x faster                                  |
| pickle_pure_python   | 306 us                                                 | 286 us: 1.07x faster                                   |
| json_dumps           | 12.6 ms                                                | 11.8 ms: 1.06x faster                                  |
| unpickle             | 13.7 us                                                | 13.1 us: 1.04x faster                                  |
| xml_etree_parse      | 158 ms                                                 | 156 ms: 1.01x faster                                   |
| xml_etree_process    | 53.9 ms                                                | 53.3 ms: 1.01x faster                                  |
| xml_etree_generate   | 76.2 ms                                                | 75.9 ms: 1.00x faster                                  |
| pickle_dict          | 31.1 us                                                | 31.6 us: 1.02x slower                                  |
| unpickle_list        | 4.91 us                                                | 5.04 us: 1.03x slower                                  |
| pickle               | 10.1 us                                                | 10.5 us: 1.04x slower                                  |
| Geometric mean       | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (2): xml_etree_iterparse, pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220710-linux-x86_64-python-main-3.12.0a1+-264b3dd |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup | 8.52 ms                                                | 8.16 ms: 1.05x faster                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmark hidden because not significant (1): python_startup_no_site

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220710-linux-x86_64-python-main-3.12.0a1+-264b3dd |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 10.1 ms                                                | 9.45 ms: 1.07x faster                                  |
| django_template | 32.6 ms                                                | 31.5 ms: 1.03x faster                                  |
| Geometric mean  | (ref)                                                  | 1.05x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220710-linux-x86_64-python-main-3.12.0a1+-264b3dd |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| unpickle_pure_python    | 228 us                                                 | 201 us: 1.13x faster                                   |
| deltablue               | 3.67 ms                                                | 3.24 ms: 1.13x faster                                  |
| regex_effbot            | 3.99 ms                                                | 3.54 ms: 1.13x faster                                  |
| pycparser               | 1.18 sec                                               | 1.06 sec: 1.11x faster                                 |
| regex_compile           | 138 ms                                                 | 126 ms: 1.10x faster                                   |
| json_loads              | 26.5 us                                                | 24.2 us: 1.09x faster                                  |
| logging_silent          | 101 ns                                                 | 92.5 ns: 1.09x faster                                  |
| go                      | 140 ms                                                 | 130 ms: 1.08x faster                                   |
| hexiom                  | 6.37 ms                                                | 5.92 ms: 1.08x faster                                  |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.18 ms: 1.08x faster                                  |
| pickle_pure_python      | 306 us                                                 | 286 us: 1.07x faster                                   |
| scimark_sor             | 118 ms                                                 | 111 ms: 1.07x faster                                   |
| float                   | 77.2 ms                                                | 72.4 ms: 1.07x faster                                  |
| mako                    | 10.1 ms                                                | 9.45 ms: 1.07x faster                                  |
| json_dumps              | 12.6 ms                                                | 11.8 ms: 1.06x faster                                  |
| logging_simple          | 6.03 us                                                | 5.67 us: 1.06x faster                                  |
| chaos                   | 69.2 ms                                                | 65.0 ms: 1.06x faster                                  |
| meteor_contest          | 107 ms                                                 | 101 ms: 1.06x faster                                   |
| json                    | 4.94 ms                                                | 4.69 ms: 1.05x faster                                  |
| sympy_expand            | 475 ms                                                 | 450 ms: 1.05x faster                                   |
| scimark_lu              | 110 ms                                                 | 104 ms: 1.05x faster                                   |
| tornado_http            | 96.3 ms                                                | 91.3 ms: 1.05x faster                                  |
| logging_format          | 6.68 us                                                | 6.35 us: 1.05x faster                                  |
| scimark_monte_carlo     | 68.1 ms                                                | 64.6 ms: 1.05x faster                                  |
| pyflate                 | 418 ms                                                 | 398 ms: 1.05x faster                                   |
| thrift                  | 756 us                                                 | 720 us: 1.05x faster                                   |
| sympy_sum               | 167 ms                                                 | 158 ms: 1.05x faster                                   |
| scimark_fft             | 328 ms                                                 | 313 ms: 1.05x faster                                   |
| python_startup          | 8.52 ms                                                | 8.16 ms: 1.05x faster                                  |
| sympy_integrate         | 21.0 ms                                                | 20.1 ms: 1.04x faster                                  |
| unpickle                | 13.7 us                                                | 13.1 us: 1.04x faster                                  |
| sympy_str               | 290 ms                                                 | 279 ms: 1.04x faster                                   |
| dulwich_log             | 63.7 ms                                                | 61.2 ms: 1.04x faster                                  |
| 2to3                    | 259 ms                                                 | 249 ms: 1.04x faster                                   |
| raytrace                | 297 ms                                                 | 286 ms: 1.04x faster                                   |
| django_template         | 32.6 ms                                                | 31.5 ms: 1.03x faster                                  |
| nqueens                 | 83.4 ms                                                | 80.8 ms: 1.03x faster                                  |
| html5lib                | 64.5 ms                                                | 62.6 ms: 1.03x faster                                  |
| nbody                   | 93.1 ms                                                | 90.5 ms: 1.03x faster                                  |
| chameleon               | 6.47 ms                                                | 6.30 ms: 1.03x faster                                  |
| pidigits                | 198 ms                                                 | 193 ms: 1.03x faster                                   |
| fannkuch                | 388 ms                                                 | 378 ms: 1.02x faster                                   |
| spectral_norm           | 100 ms                                                 | 97.7 ms: 1.02x faster                                  |
| richards                | 45.7 ms                                                | 45.0 ms: 1.02x faster                                  |
| pathlib                 | 18.2 ms                                                | 18.0 ms: 1.02x faster                                  |
| xml_etree_parse         | 158 ms                                                 | 156 ms: 1.01x faster                                   |
| telco                   | 6.58 ms                                                | 6.51 ms: 1.01x faster                                  |
| xml_etree_process       | 53.9 ms                                                | 53.3 ms: 1.01x faster                                  |
| crypto_pyaes            | 74.7 ms                                                | 74.3 ms: 1.01x faster                                  |
| xml_etree_generate      | 76.2 ms                                                | 75.9 ms: 1.00x faster                                  |
| regex_dna               | 204 ms                                                 | 207 ms: 1.01x slower                                   |
| pickle_dict             | 31.1 us                                                | 31.6 us: 1.02x slower                                  |
| unpickle_list           | 4.91 us                                                | 5.04 us: 1.03x slower                                  |
| pickle                  | 10.1 us                                                | 10.5 us: 1.04x slower                                  |
| sqlite_synth            | 2.52 us                                                | 2.62 us: 1.04x slower                                  |
| unpack_sequence         | 43.1 ns                                                | 46.4 ns: 1.08x slower                                  |
| Geometric mean          | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (4): xml_etree_iterparse, python_startup_no_site, pickle_list, regex_v8
Ignored benchmarks (40) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x
