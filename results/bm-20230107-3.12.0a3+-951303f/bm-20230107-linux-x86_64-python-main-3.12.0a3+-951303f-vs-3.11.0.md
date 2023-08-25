
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 951303f
- commit date: 2023-01-07
- overall geometric mean: 1.03x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230107-linux-x86_64-python-main-3.12.0a3+-951303f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 255 ms: 1.02x faster                                   |
| chameleon      | 6.47 ms                                                | 6.41 ms: 1.01x faster                                  |
| docutils       | 2.63 sec                                               | 2.50 sec: 1.05x faster                                 |
| html5lib       | 64.5 ms                                                | 59.7 ms: 1.08x faster                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230107-linux-x86_64-python-main-3.12.0a3+-951303f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.8 ms: 1.06x faster                                  |
| pidigits       | 198 ms                                                 | 190 ms: 1.04x faster                                   |
| nbody          | 93.1 ms                                                | 96.7 ms: 1.04x slower                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230107-linux-x86_64-python-main-3.12.0a3+-951303f |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.17 ms: 1.26x faster                                  |
| regex_dna      | 204 ms                                                 | 189 ms: 1.08x faster                                   |
| regex_compile  | 138 ms                                                 | 128 ms: 1.08x faster                                   |
| regex_v8       | 22.0 ms                                                | 20.8 ms: 1.06x faster                                  |
| Geometric mean | (ref)                                                  | 1.12x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230107-linux-x86_64-python-main-3.12.0a3+-951303f |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.51 ms: 1.32x faster                                  |
| unpickle_pure_python | 228 us                                                 | 210 us: 1.09x faster                                   |
| pickle_pure_python   | 306 us                                                 | 284 us: 1.08x faster                                   |
| xml_etree_parse      | 158 ms                                                 | 150 ms: 1.06x faster                                   |
| unpickle             | 13.7 us                                                | 13.1 us: 1.04x faster                                  |
| json_loads           | 26.5 us                                                | 26.1 us: 1.02x faster                                  |
| xml_etree_process    | 53.9 ms                                                | 53.4 ms: 1.01x faster                                  |
| pickle_list          | 4.11 us                                                | 4.14 us: 1.01x slower                                  |
| pickle               | 10.1 us                                                | 10.2 us: 1.01x slower                                  |
| unpickle_list        | 4.91 us                                                | 5.01 us: 1.02x slower                                  |
| xml_etree_generate   | 76.2 ms                                                | 78.2 ms: 1.03x slower                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (2): xml_etree_iterparse, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230107-linux-x86_64-python-main-3.12.0a3+-951303f |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.51 ms: 1.00x faster                                  |
| python_startup_no_site | 6.01 ms                                                | 6.09 ms: 1.01x slower                                  |
| Geometric mean         | (ref)                                                  | 1.01x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230107-linux-x86_64-python-main-3.12.0a3+-951303f |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 47.4 ms: 1.09x faster                                  |
| mako            | 10.1 ms                                                | 9.54 ms: 1.06x faster                                  |
| genshi_text     | 21.6 ms                                                | 20.7 ms: 1.04x faster                                  |
| django_template | 32.6 ms                                                | 32.9 ms: 1.01x slower                                  |
| Geometric mean  | (ref)                                                  | 1.04x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230107-linux-x86_64-python-main-3.12.0a3+-951303f |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps              | 12.6 ms                                                | 9.51 ms: 1.32x faster                                  |
| regex_effbot            | 3.99 ms                                                | 3.17 ms: 1.26x faster                                  |
| deltablue               | 3.67 ms                                                | 3.25 ms: 1.13x faster                                  |
| deepcopy_memo           | 37.0 us                                                | 33.6 us: 1.10x faster                                  |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.11 ms: 1.10x faster                                  |
| scimark_sor             | 118 ms                                                 | 108 ms: 1.09x faster                                   |
| genshi_xml              | 51.8 ms                                                | 47.4 ms: 1.09x faster                                  |
| unpickle_pure_python    | 228 us                                                 | 210 us: 1.09x faster                                   |
| richards                | 45.7 ms                                                | 42.3 ms: 1.08x faster                                  |
| html5lib                | 64.5 ms                                                | 59.7 ms: 1.08x faster                                  |
| regex_dna               | 204 ms                                                 | 189 ms: 1.08x faster                                   |
| regex_compile           | 138 ms                                                 | 128 ms: 1.08x faster                                   |
| pickle_pure_python      | 306 us                                                 | 284 us: 1.08x faster                                   |
| logging_silent          | 101 ns                                                 | 94.1 ns: 1.07x faster                                  |
| float                   | 77.2 ms                                                | 72.8 ms: 1.06x faster                                  |
| logging_format          | 6.68 us                                                | 6.31 us: 1.06x faster                                  |
| xml_etree_parse         | 158 ms                                                 | 150 ms: 1.06x faster                                   |
| regex_v8                | 22.0 ms                                                | 20.8 ms: 1.06x faster                                  |
| mako                    | 10.1 ms                                                | 9.54 ms: 1.06x faster                                  |
| scimark_monte_carlo     | 68.1 ms                                                | 64.6 ms: 1.05x faster                                  |
| raytrace                | 297 ms                                                 | 282 ms: 1.05x faster                                   |
| hexiom                  | 6.37 ms                                                | 6.06 ms: 1.05x faster                                  |
| docutils                | 2.63 sec                                               | 2.50 sec: 1.05x faster                                 |
| bench_thread_pool       | 819 us                                                 | 781 us: 1.05x faster                                   |
| logging_simple          | 6.03 us                                                | 5.77 us: 1.05x faster                                  |
| pidigits                | 198 ms                                                 | 190 ms: 1.04x faster                                   |
| pycparser               | 1.18 sec                                               | 1.13 sec: 1.04x faster                                 |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                 |
| pyflate                 | 418 ms                                                 | 402 ms: 1.04x faster                                   |
| unpickle                | 13.7 us                                                | 13.1 us: 1.04x faster                                  |
| genshi_text             | 21.6 ms                                                | 20.7 ms: 1.04x faster                                  |
| deepcopy                | 342 us                                                 | 330 us: 1.04x faster                                   |
| telco                   | 6.58 ms                                                | 6.36 ms: 1.03x faster                                  |
| async_generators        | 368 ms                                                 | 356 ms: 1.03x faster                                   |
| fannkuch                | 388 ms                                                 | 376 ms: 1.03x faster                                   |
| pprint_safe_repr        | 701 ms                                                 | 681 ms: 1.03x faster                                   |
| nqueens                 | 83.4 ms                                                | 81.0 ms: 1.03x faster                                  |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                  |
| sympy_expand            | 475 ms                                                 | 462 ms: 1.03x faster                                   |
| sqlglot_optimize        | 53.1 ms                                                | 51.7 ms: 1.03x faster                                  |
| go                      | 140 ms                                                 | 136 ms: 1.03x faster                                   |
| pathlib                 | 18.2 ms                                                | 17.9 ms: 1.02x faster                                  |
| 2to3                    | 259 ms                                                 | 255 ms: 1.02x faster                                   |
| unpack_sequence         | 43.1 ns                                                | 42.4 ns: 1.02x faster                                  |
| sympy_str               | 290 ms                                                 | 285 ms: 1.02x faster                                   |
| json_loads              | 26.5 us                                                | 26.1 us: 1.02x faster                                  |
| spectral_norm           | 100 ms                                                 | 98.6 ms: 1.01x faster                                  |
| meteor_contest          | 107 ms                                                 | 105 ms: 1.01x faster                                   |
| dulwich_log             | 63.7 ms                                                | 62.9 ms: 1.01x faster                                  |
| deepcopy_reduce         | 2.94 us                                                | 2.90 us: 1.01x faster                                  |
| coroutines              | 25.5 ms                                                | 25.2 ms: 1.01x faster                                  |
| scimark_fft             | 328 ms                                                 | 325 ms: 1.01x faster                                   |
| chameleon               | 6.47 ms                                                | 6.41 ms: 1.01x faster                                  |
| xml_etree_process       | 53.9 ms                                                | 53.4 ms: 1.01x faster                                  |
| scimark_lu              | 110 ms                                                 | 109 ms: 1.01x faster                                   |
| coverage                | 100 ms                                                 | 99.3 ms: 1.01x faster                                  |
| sqlglot_transpile       | 1.70 ms                                                | 1.69 ms: 1.01x faster                                  |
| sympy_sum               | 167 ms                                                 | 165 ms: 1.01x faster                                   |
| sqlglot_normalize       | 108 ms                                                 | 107 ms: 1.01x faster                                   |
| python_startup          | 8.52 ms                                                | 8.51 ms: 1.00x faster                                  |
| mdp                     | 2.62 sec                                               | 2.63 sec: 1.00x slower                                 |
| pickle_list             | 4.11 us                                                | 4.14 us: 1.01x slower                                  |
| pickle                  | 10.1 us                                                | 10.2 us: 1.01x slower                                  |
| django_template         | 32.6 ms                                                | 32.9 ms: 1.01x slower                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.09 ms: 1.01x slower                                  |
| chaos                   | 69.2 ms                                                | 70.2 ms: 1.02x slower                                  |
| async_tree_none         | 526 ms                                                 | 536 ms: 1.02x slower                                   |
| unpickle_list           | 4.91 us                                                | 5.01 us: 1.02x slower                                  |
| async_tree_cpu_io_mixed | 739 ms                                                 | 757 ms: 1.02x slower                                   |
| xml_etree_generate      | 76.2 ms                                                | 78.2 ms: 1.03x slower                                  |
| async_tree_io           | 1.30 sec                                               | 1.33 sec: 1.03x slower                                 |
| sqlite_synth            | 2.52 us                                                | 2.60 us: 1.03x slower                                  |
| crypto_pyaes            | 74.7 ms                                                | 77.2 ms: 1.03x slower                                  |
| generators              | 73.5 ms                                                | 76.2 ms: 1.04x slower                                  |
| nbody                   | 93.1 ms                                                | 96.7 ms: 1.04x slower                                  |
| async_tree_memoization  | 627 ms                                                 | 672 ms: 1.07x slower                                   |
| Geometric mean          | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (7): djangocms, json, sqlglot_parse, bench_mp_pool, thrift, xml_etree_iterparse, pickle_dict
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230107-3.12.0a3+-951303f/bm-20230107-linux-x86_64-python-main-3.12.0a3+-951303f.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x
