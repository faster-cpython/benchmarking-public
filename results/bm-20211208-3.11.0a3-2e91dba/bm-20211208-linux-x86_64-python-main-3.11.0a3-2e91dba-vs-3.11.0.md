
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 2e91dba
- commit date: 2021-12-08
- overall geometric mean: 1.05x slower \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| 2to3           | 259 ms                                                 | 264 ms: 1.02x slower                                  |
| chameleon      | 6.47 ms                                                | 7.44 ms: 1.15x slower                                 |
| html5lib       | 64.5 ms                                                | 68.5 ms: 1.06x slower                                 |
| tornado_http   | 96.3 ms                                                | 108 ms: 1.12x slower                                  |
| Geometric mean | (ref)                                                  | 1.09x slower                                          |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pidigits       | 198 ms                                                 | 198 ms: 1.00x slower                                  |
| float          | 77.2 ms                                                | 79.2 ms: 1.02x slower                                 |
| nbody          | 93.1 ms                                                | 96.1 ms: 1.03x slower                                 |
| Geometric mean | (ref)                                                  | 1.02x slower                                          |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba |
|----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.21 ms: 1.24x faster                                 |
| regex_compile  | 138 ms                                                 | 139 ms: 1.00x slower                                  |
| regex_dna      | 204 ms                                                 | 212 ms: 1.04x slower                                  |
| regex_v8       | 22.0 ms                                                | 24.5 ms: 1.11x slower                                 |
| Geometric mean | (ref)                                                  | 1.02x faster                                          |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba |
|----------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| pickle_dict          | 31.1 us                                                | 27.7 us: 1.12x faster                                 |
| json_loads           | 26.5 us                                                | 25.6 us: 1.03x faster                                 |
| xml_etree_parse      | 158 ms                                                 | 156 ms: 1.02x faster                                  |
| pickle               | 10.1 us                                                | 9.95 us: 1.01x faster                                 |
| xml_etree_iterparse  | 104 ms                                                 | 105 ms: 1.01x slower                                  |
| xml_etree_generate   | 76.2 ms                                                | 80.8 ms: 1.06x slower                                 |
| unpickle_list        | 4.91 us                                                | 5.21 us: 1.06x slower                                 |
| unpickle             | 13.7 us                                                | 14.6 us: 1.07x slower                                 |
| xml_etree_process    | 53.9 ms                                                | 57.8 ms: 1.07x slower                                 |
| unpickle_pure_python | 228 us                                                 | 251 us: 1.10x slower                                  |
| pickle_pure_python   | 306 us                                                 | 347 us: 1.14x slower                                  |
| pickle_list          | 4.11 us                                                | 4.68 us: 1.14x slower                                 |
| Geometric mean       | (ref)                                                  | 1.03x slower                                          |

Benchmark hidden because not significant (1): json_dumps

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba |
|------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.00 ms: 1.07x faster                                 |
| python_startup_no_site | 6.01 ms                                                | 5.78 ms: 1.04x faster                                 |
| Geometric mean         | (ref)                                                  | 1.05x faster                                          |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba |
|-----------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| django_template | 32.6 ms                                                | 36.5 ms: 1.12x slower                                 |
| mako            | 10.1 ms                                                | 11.9 ms: 1.18x slower                                 |
| Geometric mean  | (ref)                                                  | 1.15x slower                                          |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20211208-linux-x86_64-python-main-3.11.0a3-2e91dba |
|-------------------------|:------------------------------------------------------:|:-----------------------------------------------------:|
| regex_effbot            | 3.99 ms                                                | 3.21 ms: 1.24x faster                                 |
| pickle_dict             | 31.1 us                                                | 27.7 us: 1.12x faster                                 |
| python_startup          | 8.52 ms                                                | 8.00 ms: 1.07x faster                                 |
| python_startup_no_site  | 6.01 ms                                                | 5.78 ms: 1.04x faster                                 |
| json_loads              | 26.5 us                                                | 25.6 us: 1.03x faster                                 |
| logging_format          | 6.68 us                                                | 6.49 us: 1.03x faster                                 |
| json                    | 4.94 ms                                                | 4.83 ms: 1.02x faster                                 |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.02x faster                                  |
| xml_etree_parse         | 158 ms                                                 | 156 ms: 1.02x faster                                  |
| pickle                  | 10.1 us                                                | 9.95 us: 1.01x faster                                 |
| logging_simple          | 6.03 us                                                | 5.97 us: 1.01x faster                                 |
| fannkuch                | 388 ms                                                 | 386 ms: 1.00x faster                                  |
| pidigits                | 198 ms                                                 | 198 ms: 1.00x slower                                  |
| regex_compile           | 138 ms                                                 | 139 ms: 1.00x slower                                  |
| scimark_fft             | 328 ms                                                 | 332 ms: 1.01x slower                                  |
| xml_etree_iterparse     | 104 ms                                                 | 105 ms: 1.01x slower                                  |
| nqueens                 | 83.4 ms                                                | 84.6 ms: 1.01x slower                                 |
| 2to3                    | 259 ms                                                 | 264 ms: 1.02x slower                                  |
| scimark_lu              | 110 ms                                                 | 112 ms: 1.02x slower                                  |
| float                   | 77.2 ms                                                | 79.2 ms: 1.02x slower                                 |
| sympy_sum               | 167 ms                                                 | 172 ms: 1.03x slower                                  |
| nbody                   | 93.1 ms                                                | 96.1 ms: 1.03x slower                                 |
| spectral_norm           | 100 ms                                                 | 104 ms: 1.03x slower                                  |
| sympy_integrate         | 21.0 ms                                                | 21.7 ms: 1.04x slower                                 |
| regex_dna               | 204 ms                                                 | 212 ms: 1.04x slower                                  |
| pycparser               | 1.18 sec                                               | 1.24 sec: 1.05x slower                                |
| dulwich_log             | 63.7 ms                                                | 67.2 ms: 1.06x slower                                 |
| xml_etree_generate      | 76.2 ms                                                | 80.8 ms: 1.06x slower                                 |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.77 ms: 1.06x slower                                 |
| unpickle_list           | 4.91 us                                                | 5.21 us: 1.06x slower                                 |
| html5lib                | 64.5 ms                                                | 68.5 ms: 1.06x slower                                 |
| sympy_str               | 290 ms                                                 | 308 ms: 1.06x slower                                  |
| hexiom                  | 6.37 ms                                                | 6.77 ms: 1.06x slower                                 |
| pathlib                 | 18.2 ms                                                | 19.4 ms: 1.07x slower                                 |
| unpickle                | 13.7 us                                                | 14.6 us: 1.07x slower                                 |
| chaos                   | 69.2 ms                                                | 73.9 ms: 1.07x slower                                 |
| sympy_expand            | 475 ms                                                 | 509 ms: 1.07x slower                                  |
| xml_etree_process       | 53.9 ms                                                | 57.8 ms: 1.07x slower                                 |
| thrift                  | 756 us                                                 | 814 us: 1.08x slower                                  |
| sqlite_synth            | 2.52 us                                                | 2.74 us: 1.09x slower                                 |
| scimark_monte_carlo     | 68.1 ms                                                | 74.0 ms: 1.09x slower                                 |
| logging_silent          | 101 ns                                                 | 110 ns: 1.09x slower                                  |
| unpickle_pure_python    | 228 us                                                 | 251 us: 1.10x slower                                  |
| scimark_sor             | 118 ms                                                 | 130 ms: 1.10x slower                                  |
| regex_v8                | 22.0 ms                                                | 24.5 ms: 1.11x slower                                 |
| tornado_http            | 96.3 ms                                                | 108 ms: 1.12x slower                                  |
| django_template         | 32.6 ms                                                | 36.5 ms: 1.12x slower                                 |
| raytrace                | 297 ms                                                 | 333 ms: 1.12x slower                                  |
| go                      | 140 ms                                                 | 158 ms: 1.13x slower                                  |
| pickle_pure_python      | 306 us                                                 | 347 us: 1.14x slower                                  |
| pickle_list             | 4.11 us                                                | 4.68 us: 1.14x slower                                 |
| pyflate                 | 418 ms                                                 | 477 ms: 1.14x slower                                  |
| unpack_sequence         | 43.1 ns                                                | 49.2 ns: 1.14x slower                                 |
| chameleon               | 6.47 ms                                                | 7.44 ms: 1.15x slower                                 |
| crypto_pyaes            | 74.7 ms                                                | 88.1 ms: 1.18x slower                                 |
| mako                    | 10.1 ms                                                | 11.9 ms: 1.18x slower                                 |
| richards                | 45.7 ms                                                | 54.5 ms: 1.19x slower                                 |
| deltablue               | 3.67 ms                                                | 4.54 ms: 1.24x slower                                 |
| Geometric mean          | (ref)                                                  | 1.05x slower                                          |

Benchmark hidden because not significant (2): telco, json_dumps
Ignored benchmarks (40) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be slow
- 90% likely to have a slowdown of 1.03x
- 95% likely to have a slowdown of 1.03x
- 99% likely to have a slowdown of 1.02x
