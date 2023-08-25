
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 57be545
- commit date: 2022-11-12
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221112-linux-x86_64-python-main-3.12.0a2+-57be545 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 246 ms: 1.05x faster                                   |
| html5lib       | 64.5 ms                                                | 58.9 ms: 1.10x faster                                  |
| tornado_http   | 96.3 ms                                                | 92.5 ms: 1.04x faster                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221112-linux-x86_64-python-main-3.12.0a2+-57be545 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 77.2 ms                                                | 73.3 ms: 1.05x faster                                  |
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221112-linux-x86_64-python-main-3.12.0a2+-57be545 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.64 ms: 1.10x faster                                  |
| regex_compile  | 138 ms                                                 | 128 ms: 1.08x faster                                   |
| regex_dna      | 204 ms                                                 | 205 ms: 1.01x slower                                   |
| regex_v8       | 22.0 ms                                                | 22.2 ms: 1.01x slower                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221112-linux-x86_64-python-main-3.12.0a2+-57be545 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.44 ms: 1.33x faster                                  |
| unpickle_pure_python | 228 us                                                 | 200 us: 1.14x faster                                   |
| json_loads           | 26.5 us                                                | 24.2 us: 1.09x faster                                  |
| pickle_pure_python   | 306 us                                                 | 281 us: 1.09x faster                                   |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.06x faster                                   |
| xml_etree_process    | 53.9 ms                                                | 53.0 ms: 1.02x faster                                  |
| pickle_list          | 4.11 us                                                | 4.14 us: 1.01x slower                                  |
| xml_etree_generate   | 76.2 ms                                                | 76.8 ms: 1.01x slower                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (5): unpickle, xml_etree_iterparse, pickle, pickle_dict, unpickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221112-linux-x86_64-python-main-3.12.0a2+-57be545 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.52 ms: 1.00x faster                                  |
| python_startup_no_site | 6.01 ms                                                | 6.24 ms: 1.04x slower                                  |
| Geometric mean         | (ref)                                                  | 1.02x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221112-linux-x86_64-python-main-3.12.0a2+-57be545 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                | 46.8 ms: 1.10x faster                                  |
| mako           | 10.1 ms                                                | 9.70 ms: 1.04x faster                                  |
| genshi_text    | 21.6 ms                                                | 21.3 ms: 1.01x faster                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221112-linux-x86_64-python-main-3.12.0a2+-57be545 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps              | 12.6 ms                                                | 9.44 ms: 1.33x faster                                  |
| unpickle_pure_python    | 228 us                                                 | 200 us: 1.14x faster                                   |
| scimark_sor             | 118 ms                                                 | 104 ms: 1.14x faster                                   |
| deltablue               | 3.67 ms                                                | 3.22 ms: 1.14x faster                                  |
| genshi_xml              | 51.8 ms                                                | 46.8 ms: 1.10x faster                                  |
| gunicorn                | 1.18 ms                                                | 1.07 ms: 1.10x faster                                  |
| aiohttp                 | 1.10 ms                                                | 998 us: 1.10x faster                                   |
| logging_silent          | 101 ns                                                 | 91.8 ns: 1.10x faster                                  |
| regex_effbot            | 3.99 ms                                                | 3.64 ms: 1.10x faster                                  |
| richards                | 45.7 ms                                                | 41.7 ms: 1.10x faster                                  |
| html5lib                | 64.5 ms                                                | 58.9 ms: 1.10x faster                                  |
| json_loads              | 26.5 us                                                | 24.2 us: 1.09x faster                                  |
| deepcopy_memo           | 37.0 us                                                | 34.0 us: 1.09x faster                                  |
| pickle_pure_python      | 306 us                                                 | 281 us: 1.09x faster                                   |
| regex_compile           | 138 ms                                                 | 128 ms: 1.08x faster                                   |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.16 ms: 1.08x faster                                  |
| scimark_fft             | 328 ms                                                 | 309 ms: 1.06x faster                                   |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.06x faster                                   |
| mdp                     | 2.62 sec                                               | 2.47 sec: 1.06x faster                                 |
| pycparser               | 1.18 sec                                               | 1.11 sec: 1.06x faster                                 |
| raytrace                | 297 ms                                                 | 281 ms: 1.06x faster                                   |
| coroutines              | 25.5 ms                                                | 24.1 ms: 1.06x faster                                  |
| 2to3                    | 259 ms                                                 | 246 ms: 1.05x faster                                   |
| float                   | 77.2 ms                                                | 73.3 ms: 1.05x faster                                  |
| logging_format          | 6.68 us                                                | 6.34 us: 1.05x faster                                  |
| sqlglot_optimize        | 53.1 ms                                                | 50.5 ms: 1.05x faster                                  |
| spectral_norm           | 100 ms                                                 | 95.2 ms: 1.05x faster                                  |
| json                    | 4.94 ms                                                | 4.71 ms: 1.05x faster                                  |
| logging_simple          | 6.03 us                                                | 5.77 us: 1.05x faster                                  |
| dulwich_log             | 63.7 ms                                                | 61.1 ms: 1.04x faster                                  |
| telco                   | 6.58 ms                                                | 6.32 ms: 1.04x faster                                  |
| sqlglot_transpile       | 1.70 ms                                                | 1.64 ms: 1.04x faster                                  |
| pyflate                 | 418 ms                                                 | 402 ms: 1.04x faster                                   |
| pathlib                 | 18.2 ms                                                | 17.5 ms: 1.04x faster                                  |
| sqlglot_parse           | 1.40 ms                                                | 1.35 ms: 1.04x faster                                  |
| tornado_http            | 96.3 ms                                                | 92.5 ms: 1.04x faster                                  |
| mako                    | 10.1 ms                                                | 9.70 ms: 1.04x faster                                  |
| scimark_monte_carlo     | 68.1 ms                                                | 65.5 ms: 1.04x faster                                  |
| hexiom                  | 6.37 ms                                                | 6.13 ms: 1.04x faster                                  |
| fannkuch                | 388 ms                                                 | 374 ms: 1.04x faster                                   |
| sympy_expand            | 475 ms                                                 | 458 ms: 1.04x faster                                   |
| go                      | 140 ms                                                 | 135 ms: 1.04x faster                                   |
| chaos                   | 69.2 ms                                                | 67.0 ms: 1.03x faster                                  |
| sympy_integrate         | 21.0 ms                                                | 20.3 ms: 1.03x faster                                  |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                   |
| deepcopy                | 342 us                                                 | 332 us: 1.03x faster                                   |
| pprint_pformat          | 1.46 sec                                               | 1.41 sec: 1.03x faster                                 |
| nqueens                 | 83.4 ms                                                | 81.1 ms: 1.03x faster                                  |
| sympy_str               | 290 ms                                                 | 283 ms: 1.03x faster                                   |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.02x faster                                   |
| pprint_safe_repr        | 701 ms                                                 | 688 ms: 1.02x faster                                   |
| scimark_lu              | 110 ms                                                 | 108 ms: 1.02x faster                                   |
| sympy_sum               | 167 ms                                                 | 164 ms: 1.02x faster                                   |
| xml_etree_process       | 53.9 ms                                                | 53.0 ms: 1.02x faster                                  |
| thrift                  | 756 us                                                 | 745 us: 1.02x faster                                   |
| deepcopy_reduce         | 2.94 us                                                | 2.90 us: 1.01x faster                                  |
| async_tree_cpu_io_mixed | 739 ms                                                 | 731 ms: 1.01x faster                                   |
| genshi_text             | 21.6 ms                                                | 21.3 ms: 1.01x faster                                  |
| pidigits                | 198 ms                                                 | 197 ms: 1.00x faster                                   |
| python_startup          | 8.52 ms                                                | 8.52 ms: 1.00x faster                                  |
| regex_dna               | 204 ms                                                 | 205 ms: 1.01x slower                                   |
| crypto_pyaes            | 74.7 ms                                                | 75.1 ms: 1.01x slower                                  |
| pickle_list             | 4.11 us                                                | 4.14 us: 1.01x slower                                  |
| regex_v8                | 22.0 ms                                                | 22.2 ms: 1.01x slower                                  |
| xml_etree_generate      | 76.2 ms                                                | 76.8 ms: 1.01x slower                                  |
| async_tree_io           | 1.30 sec                                               | 1.31 sec: 1.01x slower                                 |
| unpack_sequence         | 43.1 ns                                                | 44.2 ns: 1.03x slower                                  |
| async_tree_memoization  | 627 ms                                                 | 646 ms: 1.03x slower                                   |
| python_startup_no_site  | 6.01 ms                                                | 6.24 ms: 1.04x slower                                  |
| sqlite_synth            | 2.52 us                                                | 2.65 us: 1.05x slower                                  |
| generators              | 73.5 ms                                                | 79.6 ms: 1.08x slower                                  |
| Geometric mean          | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (10): unpickle, xml_etree_iterparse, django_template, pickle, coverage, pickle_dict, unpickle_list, nbody, async_tree_none, chameleon
Ignored benchmarks (19) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: async_generators, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, create_gc_cycles, dask, djangocms, docutils, flaskblogging, gc_traversal, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221112-3.12.0a2+-57be545/bm-20221112-linux-x86_64-python-main-3.12.0a2+-57be545.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
