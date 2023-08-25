
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 206f05a
- commit date: 2023-01-14
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230114-linux-x86_64-python-main-3.12.0a4+-206f05a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 252 ms: 1.03x faster                                   |
| chameleon      | 6.47 ms                                                | 6.35 ms: 1.02x faster                                  |
| docutils       | 2.63 sec                                               | 2.48 sec: 1.06x faster                                 |
| html5lib       | 64.5 ms                                                | 59.2 ms: 1.09x faster                                  |
| tornado_http   | 96.3 ms                                                | 93.4 ms: 1.03x faster                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230114-linux-x86_64-python-main-3.12.0a4+-206f05a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.2 ms: 1.07x faster                                  |
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                   |
| nbody          | 93.1 ms                                                | 95.1 ms: 1.02x slower                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230114-linux-x86_64-python-main-3.12.0a4+-206f05a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.39 ms: 1.18x faster                                  |
| regex_compile  | 138 ms                                                 | 130 ms: 1.06x faster                                   |
| regex_v8       | 22.0 ms                                                | 21.2 ms: 1.04x faster                                  |
| regex_dna      | 204 ms                                                 | 201 ms: 1.02x faster                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230114-linux-x86_64-python-main-3.12.0a4+-206f05a |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.40 ms: 1.34x faster                                  |
| unpickle_pure_python | 228 us                                                 | 198 us: 1.15x faster                                   |
| json_loads           | 26.5 us                                                | 24.2 us: 1.09x faster                                  |
| pickle_pure_python   | 306 us                                                 | 281 us: 1.09x faster                                   |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.07x faster                                   |
| unpickle             | 13.7 us                                                | 13.1 us: 1.04x faster                                  |
| pickle_dict          | 31.1 us                                                | 30.5 us: 1.02x faster                                  |
| pickle_list          | 4.11 us                                                | 4.08 us: 1.01x faster                                  |
| xml_etree_process    | 53.9 ms                                                | 53.5 ms: 1.01x faster                                  |
| xml_etree_generate   | 76.2 ms                                                | 76.6 ms: 1.00x slower                                  |
| unpickle_list        | 4.91 us                                                | 4.97 us: 1.01x slower                                  |
| pickle               | 10.1 us                                                | 10.2 us: 1.01x slower                                  |
| xml_etree_iterparse  | 104 ms                                                 | 107 ms: 1.03x slower                                   |
| Geometric mean       | (ref)                                                  | 1.05x faster                                           |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230114-linux-x86_64-python-main-3.12.0a4+-206f05a |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.95 ms: 1.05x slower                                  |
| python_startup_no_site | 6.01 ms                                                | 6.49 ms: 1.08x slower                                  |
| Geometric mean         | (ref)                                                  | 1.07x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230114-linux-x86_64-python-main-3.12.0a4+-206f05a |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 47.1 ms: 1.10x faster                                  |
| genshi_text     | 21.6 ms                                                | 20.2 ms: 1.06x faster                                  |
| mako            | 10.1 ms                                                | 9.90 ms: 1.02x faster                                  |
| django_template | 32.6 ms                                                | 32.0 ms: 1.02x faster                                  |
| Geometric mean  | (ref)                                                  | 1.05x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230114-linux-x86_64-python-main-3.12.0a4+-206f05a |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 505 ms: 1.83x faster                                   |
| json_dumps              | 12.6 ms                                                | 9.40 ms: 1.34x faster                                  |
| regex_effbot            | 3.99 ms                                                | 3.39 ms: 1.18x faster                                  |
| unpickle_pure_python    | 228 us                                                 | 198 us: 1.15x faster                                   |
| deltablue               | 3.67 ms                                                | 3.23 ms: 1.14x faster                                  |
| logging_silent          | 101 ns                                                 | 90.6 ns: 1.12x faster                                  |
| richards                | 45.7 ms                                                | 41.1 ms: 1.11x faster                                  |
| scimark_sor             | 118 ms                                                 | 106 ms: 1.11x faster                                   |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.05 ms: 1.11x faster                                  |
| gunicorn                | 1.18 ms                                                | 1.07 ms: 1.10x faster                                  |
| aiohttp                 | 1.10 ms                                                | 998 us: 1.10x faster                                   |
| genshi_xml              | 51.8 ms                                                | 47.1 ms: 1.10x faster                                  |
| deepcopy_memo           | 37.0 us                                                | 33.7 us: 1.10x faster                                  |
| json_loads              | 26.5 us                                                | 24.2 us: 1.09x faster                                  |
| pycparser               | 1.18 sec                                               | 1.08 sec: 1.09x faster                                 |
| html5lib                | 64.5 ms                                                | 59.2 ms: 1.09x faster                                  |
| pickle_pure_python      | 306 us                                                 | 281 us: 1.09x faster                                   |
| logging_format          | 6.68 us                                                | 6.20 us: 1.08x faster                                  |
| logging_simple          | 6.03 us                                                | 5.61 us: 1.07x faster                                  |
| scimark_fft             | 328 ms                                                 | 306 ms: 1.07x faster                                   |
| float                   | 77.2 ms                                                | 72.2 ms: 1.07x faster                                  |
| scimark_monte_carlo     | 68.1 ms                                                | 63.8 ms: 1.07x faster                                  |
| spectral_norm           | 100 ms                                                 | 93.9 ms: 1.07x faster                                  |
| raytrace                | 297 ms                                                 | 278 ms: 1.07x faster                                   |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.07x faster                                   |
| genshi_text             | 21.6 ms                                                | 20.2 ms: 1.06x faster                                  |
| regex_compile           | 138 ms                                                 | 130 ms: 1.06x faster                                   |
| go                      | 140 ms                                                 | 132 ms: 1.06x faster                                   |
| docutils                | 2.63 sec                                               | 2.48 sec: 1.06x faster                                 |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.06x faster                                 |
| gc_traversal            | 4.02 ms                                                | 3.81 ms: 1.06x faster                                  |
| json                    | 4.94 ms                                                | 4.68 ms: 1.06x faster                                  |
| telco                   | 6.58 ms                                                | 6.24 ms: 1.05x faster                                  |
| sqlglot_optimize        | 53.1 ms                                                | 50.5 ms: 1.05x faster                                  |
| bench_thread_pool       | 819 us                                                 | 779 us: 1.05x faster                                   |
| pyflate                 | 418 ms                                                 | 398 ms: 1.05x faster                                   |
| hexiom                  | 6.37 ms                                                | 6.07 ms: 1.05x faster                                  |
| pprint_safe_repr        | 701 ms                                                 | 670 ms: 1.05x faster                                   |
| pidigits                | 198 ms                                                 | 189 ms: 1.05x faster                                   |
| fannkuch                | 388 ms                                                 | 371 ms: 1.04x faster                                   |
| unpack_sequence         | 43.1 ns                                                | 41.3 ns: 1.04x faster                                  |
| regex_v8                | 22.0 ms                                                | 21.2 ms: 1.04x faster                                  |
| unpickle                | 13.7 us                                                | 13.1 us: 1.04x faster                                  |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                   |
| sympy_expand            | 475 ms                                                 | 459 ms: 1.04x faster                                   |
| deepcopy                | 342 us                                                 | 331 us: 1.03x faster                                   |
| nqueens                 | 83.4 ms                                                | 80.8 ms: 1.03x faster                                  |
| scimark_lu              | 110 ms                                                 | 106 ms: 1.03x faster                                   |
| tornado_http            | 96.3 ms                                                | 93.4 ms: 1.03x faster                                  |
| dulwich_log             | 63.7 ms                                                | 61.9 ms: 1.03x faster                                  |
| async_generators        | 368 ms                                                 | 358 ms: 1.03x faster                                   |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                  |
| 2to3                    | 259 ms                                                 | 252 ms: 1.03x faster                                   |
| sympy_str               | 290 ms                                                 | 283 ms: 1.02x faster                                   |
| pathlib                 | 18.2 ms                                                | 17.9 ms: 1.02x faster                                  |
| meteor_contest          | 107 ms                                                 | 105 ms: 1.02x faster                                   |
| chameleon               | 6.47 ms                                                | 6.35 ms: 1.02x faster                                  |
| pickle_dict             | 31.1 us                                                | 30.5 us: 1.02x faster                                  |
| mako                    | 10.1 ms                                                | 9.90 ms: 1.02x faster                                  |
| chaos                   | 69.2 ms                                                | 67.9 ms: 1.02x faster                                  |
| django_template         | 32.6 ms                                                | 32.0 ms: 1.02x faster                                  |
| sqlglot_transpile       | 1.70 ms                                                | 1.67 ms: 1.02x faster                                  |
| regex_dna               | 204 ms                                                 | 201 ms: 1.02x faster                                   |
| sympy_sum               | 167 ms                                                 | 164 ms: 1.02x faster                                   |
| coverage                | 100 ms                                                 | 98.6 ms: 1.02x faster                                  |
| create_gc_cycles        | 1.49 ms                                                | 1.47 ms: 1.01x faster                                  |
| coroutines              | 25.5 ms                                                | 25.2 ms: 1.01x faster                                  |
| thrift                  | 756 us                                                 | 749 us: 1.01x faster                                   |
| async_tree_cpu_io_mixed | 739 ms                                                 | 732 ms: 1.01x faster                                   |
| sqlglot_parse           | 1.40 ms                                                | 1.39 ms: 1.01x faster                                  |
| pickle_list             | 4.11 us                                                | 4.08 us: 1.01x faster                                  |
| xml_etree_process       | 53.9 ms                                                | 53.5 ms: 1.01x faster                                  |
| crypto_pyaes            | 74.7 ms                                                | 74.3 ms: 1.01x faster                                  |
| xml_etree_generate      | 76.2 ms                                                | 76.6 ms: 1.00x slower                                  |
| unpickle_list           | 4.91 us                                                | 4.97 us: 1.01x slower                                  |
| pickle                  | 10.1 us                                                | 10.2 us: 1.01x slower                                  |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                 |
| nbody                   | 93.1 ms                                                | 95.1 ms: 1.02x slower                                  |
| mdp                     | 2.62 sec                                               | 2.69 sec: 1.03x slower                                 |
| sqlite_synth            | 2.52 us                                                | 2.59 us: 1.03x slower                                  |
| xml_etree_iterparse     | 104 ms                                                 | 107 ms: 1.03x slower                                   |
| python_startup          | 8.52 ms                                                | 8.95 ms: 1.05x slower                                  |
| generators              | 73.5 ms                                                | 78.8 ms: 1.07x slower                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.49 ms: 1.08x slower                                  |
| dask                    | 360 ms                                                 | 494 ms: 1.37x slower                                   |
| Geometric mean          | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (5): djangocms, async_tree_none, bench_mp_pool, deepcopy_reduce, async_tree_memoization
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230114-3.12.0a4+-206f05a/bm-20230114-linux-x86_64-python-main-3.12.0a4+-206f05a.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
