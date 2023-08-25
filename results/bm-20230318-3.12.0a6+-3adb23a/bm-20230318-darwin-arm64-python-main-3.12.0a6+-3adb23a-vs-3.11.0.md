
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: darwin-arm64
- commit hash: 3adb23a
- commit date: 2023-03-18
- overall geometric mean: 1.00x slower \*
- HPT reliability: 94.24%
- HPT 99th percentile: 1.00x slower

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230318-darwin-arm64-python-main-3.12.0a6+-3adb23a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 161 ms                                                 | 165 ms: 1.02x slower                                   |
| chameleon      | 4.60 ms                                                | 4.48 ms: 1.03x faster                                  |
| docutils       | 1.47 sec                                               | 1.51 sec: 1.02x slower                                 |
| html5lib       | 34.7 ms                                                | 35.7 ms: 1.03x slower                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                           |

Benchmark hidden because not significant (1): tornado_http

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230318-darwin-arm64-python-main-3.12.0a6+-3adb23a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| nbody          | 65.6 ms                                                | 60.7 ms: 1.08x faster                                  |
| float          | 53.0 ms                                                | 52.7 ms: 1.01x faster                                  |
| pidigits       | 281 ms                                                 | 282 ms: 1.00x slower                                   |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230318-darwin-arm64-python-main-3.12.0a6+-3adb23a |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 76.7 ms                                                | 75.9 ms: 1.01x faster                                  |
| regex_dna      | 152 ms                                                 | 152 ms: 1.00x faster                                   |
| regex_v8       | 16.1 ms                                                | 16.1 ms: 1.00x faster                                  |
| regex_effbot   | 2.63 ms                                                | 2.68 ms: 1.02x slower                                  |
| Geometric mean | (ref)                                                  | 1.00x slower                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230318-darwin-arm64-python-main-3.12.0a6+-3adb23a |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 7.63 ms                                                | 6.28 ms: 1.22x faster                                  |
| xml_etree_parse      | 108 ms                                                 | 97.4 ms: 1.11x faster                                  |
| unpickle_pure_python | 159 us                                                 | 145 us: 1.10x faster                                   |
| pickle_pure_python   | 201 us                                                 | 192 us: 1.05x faster                                   |
| unpickle_list        | 2.65 us                                                | 2.64 us: 1.00x faster                                  |
| pickle_list          | 2.81 us                                                | 2.83 us: 1.01x slower                                  |
| unpickle             | 9.67 us                                                | 9.77 us: 1.01x slower                                  |
| json_loads           | 16.1 us                                                | 16.3 us: 1.02x slower                                  |
| pickle               | 7.15 us                                                | 7.41 us: 1.04x slower                                  |
| xml_etree_process    | 35.1 ms                                                | 36.7 ms: 1.05x slower                                  |
| xml_etree_generate   | 48.3 ms                                                | 51.8 ms: 1.07x slower                                  |
| Geometric mean       | (ref)                                                  | 1.02x faster                                           |

Benchmark hidden because not significant (2): pickle_dict, xml_etree_iterparse

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230318-darwin-arm64-python-main-3.12.0a6+-3adb23a |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 12.4 ms                                                | 11.0 ms: 1.13x faster                                  |
| python_startup_no_site | 10.2 ms                                                | 8.99 ms: 1.13x faster                                  |
| Geometric mean         | (ref)                                                  | 1.13x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230318-darwin-arm64-python-main-3.12.0a6+-3adb23a |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| mako            | 8.53 ms                                                | 7.44 ms: 1.15x faster                                  |
| genshi_text     | 15.3 ms                                                | 14.8 ms: 1.03x faster                                  |
| genshi_xml      | 29.8 ms                                                | 29.3 ms: 1.02x faster                                  |
| django_template | 21.0 ms                                                | 21.9 ms: 1.04x slower                                  |
| Geometric mean  | (ref)                                                  | 1.04x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509 | bm-20230318-darwin-arm64-python-main-3.12.0a6+-3adb23a |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| asyncio_tcp             | 651 ms                                                 | 449 ms: 1.45x faster                                   |
| json_dumps              | 7.63 ms                                                | 6.28 ms: 1.22x faster                                  |
| mako                    | 8.53 ms                                                | 7.44 ms: 1.15x faster                                  |
| python_startup          | 12.4 ms                                                | 11.0 ms: 1.13x faster                                  |
| python_startup_no_site  | 10.2 ms                                                | 8.99 ms: 1.13x faster                                  |
| scimark_sparse_mat_mult | 3.19 ms                                                | 2.86 ms: 1.11x faster                                  |
| xml_etree_parse         | 108 ms                                                 | 97.4 ms: 1.11x faster                                  |
| deltablue               | 2.81 ms                                                | 2.56 ms: 1.10x faster                                  |
| unpickle_pure_python    | 159 us                                                 | 145 us: 1.10x faster                                   |
| nbody                   | 65.6 ms                                                | 60.7 ms: 1.08x faster                                  |
| hexiom                  | 4.72 ms                                                | 4.40 ms: 1.07x faster                                  |
| scimark_fft             | 200 ms                                                 | 187 ms: 1.07x faster                                   |
| richards                | 32.2 ms                                                | 30.7 ms: 1.05x faster                                  |
| pickle_pure_python      | 201 us                                                 | 192 us: 1.05x faster                                   |
| coverage                | 58.4 ms                                                | 56.0 ms: 1.04x faster                                  |
| chaos                   | 49.4 ms                                                | 47.4 ms: 1.04x faster                                  |
| mdp                     | 1.55 sec                                               | 1.49 sec: 1.04x faster                                 |
| generators              | 28.8 ms                                                | 27.8 ms: 1.04x faster                                  |
| pycparser               | 698 ms                                                 | 676 ms: 1.03x faster                                   |
| genshi_text             | 15.3 ms                                                | 14.8 ms: 1.03x faster                                  |
| scimark_lu              | 73.3 ms                                                | 71.2 ms: 1.03x faster                                  |
| chameleon               | 4.60 ms                                                | 4.48 ms: 1.03x faster                                  |
| unpack_sequence         | 34.1 ns                                                | 33.3 ns: 1.02x faster                                  |
| dulwich_log             | 30.3 ms                                                | 29.6 ms: 1.02x faster                                  |
| deepcopy_memo           | 26.3 us                                                | 25.8 us: 1.02x faster                                  |
| logging_silent          | 68.1 ns                                                | 66.9 ns: 1.02x faster                                  |
| genshi_xml              | 29.8 ms                                                | 29.3 ms: 1.02x faster                                  |
| create_gc_cycles        | 716 us                                                 | 705 us: 1.02x faster                                   |
| regex_compile           | 76.7 ms                                                | 75.9 ms: 1.01x faster                                  |
| spectral_norm           | 72.6 ms                                                | 72.1 ms: 1.01x faster                                  |
| bench_thread_pool       | 474 us                                                 | 472 us: 1.01x faster                                   |
| float                   | 53.0 ms                                                | 52.7 ms: 1.01x faster                                  |
| regex_dna               | 152 ms                                                 | 152 ms: 1.00x faster                                   |
| regex_v8                | 16.1 ms                                                | 16.1 ms: 1.00x faster                                  |
| unpickle_list           | 2.65 us                                                | 2.64 us: 1.00x faster                                  |
| pidigits                | 281 ms                                                 | 282 ms: 1.00x slower                                   |
| fannkuch                | 261 ms                                                 | 262 ms: 1.00x slower                                   |
| meteor_contest          | 73.5 ms                                                | 73.8 ms: 1.00x slower                                  |
| gc_traversal            | 2.42 ms                                                | 2.43 ms: 1.01x slower                                  |
| pickle_list             | 2.81 us                                                | 2.83 us: 1.01x slower                                  |
| json                    | 2.78 ms                                                | 2.80 ms: 1.01x slower                                  |
| async_tree_none         | 286 ms                                                 | 288 ms: 1.01x slower                                   |
| unpickle                | 9.67 us                                                | 9.77 us: 1.01x slower                                  |
| pprint_pformat          | 954 ms                                                 | 967 ms: 1.01x slower                                   |
| json_loads              | 16.1 us                                                | 16.3 us: 1.02x slower                                  |
| sympy_integrate         | 11.5 ms                                                | 11.7 ms: 1.02x slower                                  |
| sqlglot_normalize       | 171 ms                                                 | 174 ms: 1.02x slower                                   |
| regex_effbot            | 2.63 ms                                                | 2.68 ms: 1.02x slower                                  |
| pprint_safe_repr        | 466 ms                                                 | 475 ms: 1.02x slower                                   |
| coroutines              | 17.8 ms                                                | 18.1 ms: 1.02x slower                                  |
| bench_mp_pool           | 43.9 ms                                                | 44.8 ms: 1.02x slower                                  |
| sympy_str               | 151 ms                                                 | 154 ms: 1.02x slower                                   |
| 2to3                    | 161 ms                                                 | 165 ms: 1.02x slower                                   |
| pathlib                 | 27.2 ms                                                | 27.9 ms: 1.02x slower                                  |
| docutils                | 1.47 sec                                               | 1.51 sec: 1.02x slower                                 |
| telco                   | 3.41 ms                                                | 3.49 ms: 1.03x slower                                  |
| deepcopy_reduce         | 1.91 us                                                | 1.96 us: 1.03x slower                                  |
| go                      | 109 ms                                                 | 111 ms: 1.03x slower                                   |
| sympy_expand            | 242 ms                                                 | 248 ms: 1.03x slower                                   |
| async_tree_cpu_io_mixed | 533 ms                                                 | 548 ms: 1.03x slower                                   |
| sqlglot_optimize        | 31.1 ms                                                | 32.0 ms: 1.03x slower                                  |
| html5lib                | 34.7 ms                                                | 35.7 ms: 1.03x slower                                  |
| sqlalchemy_declarative  | 62.6 ms                                                | 64.5 ms: 1.03x slower                                  |
| scimark_sor             | 82.6 ms                                                | 85.2 ms: 1.03x slower                                  |
| sympy_sum               | 85.5 ms                                                | 88.3 ms: 1.03x slower                                  |
| thrift                  | 442 us                                                 | 456 us: 1.03x slower                                   |
| logging_simple          | 3.55 us                                                | 3.66 us: 1.03x slower                                  |
| pickle                  | 7.15 us                                                | 7.41 us: 1.04x slower                                  |
| nqueens                 | 59.8 ms                                                | 62.1 ms: 1.04x slower                                  |
| django_template         | 21.0 ms                                                | 21.9 ms: 1.04x slower                                  |
| logging_format          | 3.78 us                                                | 3.95 us: 1.04x slower                                  |
| xml_etree_process       | 35.1 ms                                                | 36.7 ms: 1.05x slower                                  |
| crypto_pyaes            | 51.7 ms                                                | 54.6 ms: 1.05x slower                                  |
| async_tree_io           | 704 ms                                                 | 743 ms: 1.06x slower                                   |
| sqlite_synth            | 1.27 us                                                | 1.35 us: 1.06x slower                                  |
| pyflate                 | 310 ms                                                 | 332 ms: 1.07x slower                                   |
| raytrace                | 207 ms                                                 | 222 ms: 1.07x slower                                   |
| xml_etree_generate      | 48.3 ms                                                | 51.8 ms: 1.07x slower                                  |
| scimark_monte_carlo     | 46.5 ms                                                | 50.7 ms: 1.09x slower                                  |
| sqlglot_transpile       | 1.12 ms                                                | 1.23 ms: 1.10x slower                                  |
| sqlglot_parse           | 959 us                                                 | 1.06 ms: 1.10x slower                                  |
| comprehensions          | 16.1 us                                                | 17.9 us: 1.11x slower                                  |
| mypy2                   | 195 ms                                                 | 264 ms: 1.35x slower                                   |
| async_generators        | 196 ms                                                 | 266 ms: 1.35x slower                                   |
| Geometric mean          | (ref)                                                  | 1.00x slower                                           |

Benchmark hidden because not significant (6): tornado_http, async_tree_memoization, sqlalchemy_imperative, deepcopy, pickle_dict, xml_etree_iterparse
Ignored benchmarks (8) of results/bm-20221024-3.11.0-deaf509/bm-20221024-darwin-arm64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp_ssl, flaskblogging, gunicorn, pylint, richards_super, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230318-3.12.0a6+-3adb23a/bm-20230318-darwin-arm64-python-main-3.12.0a6+-3adb23a.json: dask


# HPT report

- Reliability score: 94.24% likely to be slow
- 90% likely to have a slowdown of 1.00x
- 95% likely to have a slowdown of 1.00x
- 99% likely to have a slowdown of 1.00x
