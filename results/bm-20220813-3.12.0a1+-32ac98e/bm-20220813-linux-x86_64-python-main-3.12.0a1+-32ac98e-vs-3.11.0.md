
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 32ac98e
- commit date: 2022-08-13
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.03x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220813-linux-x86_64-python-main-3.12.0a1+-32ac98e |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 250 ms: 1.04x faster                                   |
| chameleon      | 6.47 ms                                                | 6.30 ms: 1.03x faster                                  |
| html5lib       | 64.5 ms                                                | 62.9 ms: 1.03x faster                                  |
| tornado_http   | 96.3 ms                                                | 91.6 ms: 1.05x faster                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220813-linux-x86_64-python-main-3.12.0a1+-32ac98e |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.6 ms: 1.06x faster                                  |
| nbody          | 93.1 ms                                                | 91.3 ms: 1.02x faster                                  |
| pidigits       | 198 ms                                                 | 201 ms: 1.02x slower                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220813-linux-x86_64-python-main-3.12.0a1+-32ac98e |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.42 ms: 1.17x faster                                  |
| regex_compile  | 138 ms                                                 | 127 ms: 1.09x faster                                   |
| regex_v8       | 22.0 ms                                                | 20.9 ms: 1.05x faster                                  |
| regex_dna      | 204 ms                                                 | 205 ms: 1.01x slower                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220813-linux-x86_64-python-main-3.12.0a1+-32ac98e |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.67 ms: 1.30x faster                                  |
| unpickle_pure_python | 228 us                                                 | 201 us: 1.14x faster                                   |
| json_loads           | 26.5 us                                                | 24.2 us: 1.10x faster                                  |
| pickle_pure_python   | 306 us                                                 | 287 us: 1.07x faster                                   |
| xml_etree_process    | 53.9 ms                                                | 51.3 ms: 1.05x faster                                  |
| unpickle             | 13.7 us                                                | 13.2 us: 1.03x faster                                  |
| xml_etree_generate   | 76.2 ms                                                | 74.3 ms: 1.03x faster                                  |
| xml_etree_parse      | 158 ms                                                 | 155 ms: 1.02x faster                                   |
| unpickle_list        | 4.91 us                                                | 4.94 us: 1.01x slower                                  |
| xml_etree_iterparse  | 104 ms                                                 | 105 ms: 1.01x slower                                   |
| pickle_dict          | 31.1 us                                                | 31.4 us: 1.01x slower                                  |
| pickle_list          | 4.11 us                                                | 4.25 us: 1.03x slower                                  |
| pickle               | 10.1 us                                                | 10.5 us: 1.04x slower                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220813-linux-x86_64-python-main-3.12.0a1+-32ac98e |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.17 ms: 1.04x faster                                  |
| python_startup_no_site | 6.01 ms                                                | 6.04 ms: 1.01x slower                                  |
| Geometric mean         | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220813-linux-x86_64-python-main-3.12.0a1+-32ac98e |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako           | 10.1 ms                                                | 9.21 ms: 1.10x faster                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20220813-linux-x86_64-python-main-3.12.0a1+-32ac98e |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps              | 12.6 ms                                                | 9.67 ms: 1.30x faster                                  |
| regex_effbot            | 3.99 ms                                                | 3.42 ms: 1.17x faster                                  |
| deltablue               | 3.67 ms                                                | 3.20 ms: 1.15x faster                                  |
| unpickle_pure_python    | 228 us                                                 | 201 us: 1.14x faster                                   |
| logging_silent          | 101 ns                                                 | 89.6 ns: 1.13x faster                                  |
| pycparser               | 1.18 sec                                               | 1.05 sec: 1.13x faster                                 |
| json_loads              | 26.5 us                                                | 24.2 us: 1.10x faster                                  |
| mako                    | 10.1 ms                                                | 9.21 ms: 1.10x faster                                  |
| regex_compile           | 138 ms                                                 | 127 ms: 1.09x faster                                   |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.15 ms: 1.08x faster                                  |
| hexiom                  | 6.37 ms                                                | 5.97 ms: 1.07x faster                                  |
| pickle_pure_python      | 306 us                                                 | 287 us: 1.07x faster                                   |
| scimark_fft             | 328 ms                                                 | 308 ms: 1.06x faster                                   |
| float                   | 77.2 ms                                                | 72.6 ms: 1.06x faster                                  |
| scimark_sor             | 118 ms                                                 | 111 ms: 1.06x faster                                   |
| json                    | 4.94 ms                                                | 4.68 ms: 1.06x faster                                  |
| meteor_contest          | 107 ms                                                 | 101 ms: 1.06x faster                                   |
| regex_v8                | 22.0 ms                                                | 20.9 ms: 1.05x faster                                  |
| pyflate                 | 418 ms                                                 | 397 ms: 1.05x faster                                   |
| scimark_monte_carlo     | 68.1 ms                                                | 64.7 ms: 1.05x faster                                  |
| spectral_norm           | 100 ms                                                 | 95.1 ms: 1.05x faster                                  |
| tornado_http            | 96.3 ms                                                | 91.6 ms: 1.05x faster                                  |
| xml_etree_process       | 53.9 ms                                                | 51.3 ms: 1.05x faster                                  |
| go                      | 140 ms                                                 | 134 ms: 1.05x faster                                   |
| logging_format          | 6.68 us                                                | 6.39 us: 1.05x faster                                  |
| sympy_sum               | 167 ms                                                 | 159 ms: 1.05x faster                                   |
| sympy_str               | 290 ms                                                 | 278 ms: 1.04x faster                                   |
| python_startup          | 8.52 ms                                                | 8.17 ms: 1.04x faster                                  |
| sympy_integrate         | 21.0 ms                                                | 20.1 ms: 1.04x faster                                  |
| sympy_expand            | 475 ms                                                 | 457 ms: 1.04x faster                                   |
| logging_simple          | 6.03 us                                                | 5.81 us: 1.04x faster                                  |
| thrift                  | 756 us                                                 | 728 us: 1.04x faster                                   |
| 2to3                    | 259 ms                                                 | 250 ms: 1.04x faster                                   |
| chaos                   | 69.2 ms                                                | 66.8 ms: 1.04x faster                                  |
| unpickle                | 13.7 us                                                | 13.2 us: 1.03x faster                                  |
| dulwich_log             | 63.7 ms                                                | 61.6 ms: 1.03x faster                                  |
| fannkuch                | 388 ms                                                 | 375 ms: 1.03x faster                                   |
| nqueens                 | 83.4 ms                                                | 80.9 ms: 1.03x faster                                  |
| chameleon               | 6.47 ms                                                | 6.30 ms: 1.03x faster                                  |
| html5lib                | 64.5 ms                                                | 62.9 ms: 1.03x faster                                  |
| xml_etree_generate      | 76.2 ms                                                | 74.3 ms: 1.03x faster                                  |
| xml_etree_parse         | 158 ms                                                 | 155 ms: 1.02x faster                                   |
| scimark_lu              | 110 ms                                                 | 107 ms: 1.02x faster                                   |
| nbody                   | 93.1 ms                                                | 91.3 ms: 1.02x faster                                  |
| telco                   | 6.58 ms                                                | 6.47 ms: 1.02x faster                                  |
| pathlib                 | 18.2 ms                                                | 17.9 ms: 1.02x faster                                  |
| richards                | 45.7 ms                                                | 45.1 ms: 1.01x faster                                  |
| raytrace                | 297 ms                                                 | 293 ms: 1.01x faster                                   |
| crypto_pyaes            | 74.7 ms                                                | 74.2 ms: 1.01x faster                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.04 ms: 1.01x slower                                  |
| unpickle_list           | 4.91 us                                                | 4.94 us: 1.01x slower                                  |
| xml_etree_iterparse     | 104 ms                                                 | 105 ms: 1.01x slower                                   |
| regex_dna               | 204 ms                                                 | 205 ms: 1.01x slower                                   |
| pickle_dict             | 31.1 us                                                | 31.4 us: 1.01x slower                                  |
| pidigits                | 198 ms                                                 | 201 ms: 1.02x slower                                   |
| sqlite_synth            | 2.52 us                                                | 2.58 us: 1.03x slower                                  |
| pickle_list             | 4.11 us                                                | 4.25 us: 1.03x slower                                  |
| pickle                  | 10.1 us                                                | 10.5 us: 1.04x slower                                  |
| Geometric mean          | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (2): django_template, unpack_sequence
Ignored benchmarks (40) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, async_generators, async_tree_cpu_io_mixed, async_tree_io, async_tree_memoization, async_tree_none, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, coroutines, coverage, create_gc_cycles, dask, deepcopy, deepcopy_memo, deepcopy_reduce, djangocms, docutils, flaskblogging, gc_traversal, generators, genshi_text, genshi_xml, gunicorn, mdp, mypy2, pprint_pformat, pprint_safe_repr, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, sqlglot_normalize, sqlglot_optimize, sqlglot_parse, sqlglot_transpile, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.03x
