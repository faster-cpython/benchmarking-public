
# Results vs. 3.11.0

- fork: python
- ref: 848bdbe166b71ab2ac2c
- machine: linux-x86_64
- commit hash: 848bdbe
- commit date: 2023-04-01
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230401-linux-x86_64-python-848bdbe166b71ab2ac2c-3.12.0a6+-848bdbe |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 253 ms: 1.03x faster                                                   |
| chameleon      | 6.47 ms                                                | 6.55 ms: 1.01x slower                                                  |
| docutils       | 2.63 sec                                               | 2.54 sec: 1.04x faster                                                 |
| html5lib       | 64.5 ms                                                | 61.5 ms: 1.05x faster                                                  |
| tornado_http   | 96.3 ms                                                | 91.8 ms: 1.05x faster                                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230401-linux-x86_64-python-848bdbe166b71ab2ac2c-3.12.0a6+-848bdbe |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 86.7 ms: 1.07x faster                                                  |
| pidigits       | 198 ms                                                 | 188 ms: 1.05x faster                                                   |
| float          | 77.2 ms                                                | 74.7 ms: 1.03x faster                                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230401-linux-x86_64-python-848bdbe166b71ab2ac2c-3.12.0a6+-848bdbe |
|----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.64 ms: 1.10x faster                                                  |
| regex_compile  | 138 ms                                                 | 135 ms: 1.02x faster                                                   |
| regex_v8       | 22.0 ms                                                | 21.8 ms: 1.01x faster                                                  |
| regex_dna      | 204 ms                                                 | 202 ms: 1.01x faster                                                   |
| Geometric mean | (ref)                                                  | 1.04x faster                                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230401-linux-x86_64-python-848bdbe166b71ab2ac2c-3.12.0a6+-848bdbe |
|----------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.62 ms: 1.31x faster                                                  |
| unpickle_pure_python | 228 us                                                 | 201 us: 1.14x faster                                                   |
| json_loads           | 26.5 us                                                | 24.4 us: 1.09x faster                                                  |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.06x faster                                                   |
| pickle_pure_python   | 306 us                                                 | 289 us: 1.06x faster                                                   |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                   |
| pickle_dict          | 31.1 us                                                | 31.6 us: 1.01x slower                                                  |
| unpickle_list        | 4.91 us                                                | 4.99 us: 1.02x slower                                                  |
| pickle               | 10.1 us                                                | 10.3 us: 1.02x slower                                                  |
| pickle_list          | 4.11 us                                                | 4.24 us: 1.03x slower                                                  |
| xml_etree_process    | 53.9 ms                                                | 56.1 ms: 1.04x slower                                                  |
| xml_etree_generate   | 76.2 ms                                                | 81.3 ms: 1.07x slower                                                  |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230401-linux-x86_64-python-848bdbe166b71ab2ac2c-3.12.0a6+-848bdbe |
|------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.83 ms: 1.04x slower                                                  |
| python_startup_no_site | 6.01 ms                                                | 6.52 ms: 1.09x slower                                                  |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230401-linux-x86_64-python-848bdbe166b71ab2ac2c-3.12.0a6+-848bdbe |
|-----------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 47.0 ms: 1.10x faster                                                  |
| mako            | 10.1 ms                                                | 10.0 ms: 1.01x faster                                                  |
| django_template | 32.6 ms                                                | 34.0 ms: 1.04x slower                                                  |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                           |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230401-linux-x86_64-python-848bdbe166b71ab2ac2c-3.12.0a6+-848bdbe |
|-------------------------|:------------------------------------------------------:|:----------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.5 ms: 2.49x faster                                                  |
| asyncio_tcp             | 922 ms                                                 | 506 ms: 1.82x faster                                                   |
| json_dumps              | 12.6 ms                                                | 9.62 ms: 1.31x faster                                                  |
| mypy2                   | 420 ms                                                 | 332 ms: 1.26x faster                                                   |
| unpickle_pure_python    | 228 us                                                 | 201 us: 1.14x faster                                                   |
| deltablue               | 3.67 ms                                                | 3.24 ms: 1.13x faster                                                  |
| genshi_xml              | 51.8 ms                                                | 47.0 ms: 1.10x faster                                                  |
| regex_effbot            | 3.99 ms                                                | 3.64 ms: 1.10x faster                                                  |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                                  |
| json_loads              | 26.5 us                                                | 24.4 us: 1.09x faster                                                  |
| gunicorn                | 1.18 ms                                                | 1.09 ms: 1.08x faster                                                  |
| nbody                   | 93.1 ms                                                | 86.7 ms: 1.07x faster                                                  |
| scimark_fft             | 328 ms                                                 | 306 ms: 1.07x faster                                                   |
| coroutines              | 25.5 ms                                                | 23.9 ms: 1.07x faster                                                  |
| pycparser               | 1.18 sec                                               | 1.11 sec: 1.07x faster                                                 |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.06x faster                                                   |
| logging_format          | 6.68 us                                                | 6.31 us: 1.06x faster                                                  |
| pickle_pure_python      | 306 us                                                 | 289 us: 1.06x faster                                                   |
| hexiom                  | 6.37 ms                                                | 6.03 ms: 1.06x faster                                                  |
| json                    | 4.94 ms                                                | 4.68 ms: 1.06x faster                                                  |
| deepcopy_memo           | 37.0 us                                                | 35.0 us: 1.06x faster                                                  |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.27 ms: 1.05x faster                                                  |
| logging_silent          | 101 ns                                                 | 96.1 ns: 1.05x faster                                                  |
| pidigits                | 198 ms                                                 | 188 ms: 1.05x faster                                                   |
| spectral_norm           | 100 ms                                                 | 95.2 ms: 1.05x faster                                                  |
| html5lib                | 64.5 ms                                                | 61.5 ms: 1.05x faster                                                  |
| tornado_http            | 96.3 ms                                                | 91.8 ms: 1.05x faster                                                  |
| richards                | 45.7 ms                                                | 43.6 ms: 1.05x faster                                                  |
| logging_simple          | 6.03 us                                                | 5.76 us: 1.05x faster                                                  |
| scimark_sor             | 118 ms                                                 | 113 ms: 1.05x faster                                                   |
| mdp                     | 2.62 sec                                               | 2.50 sec: 1.05x faster                                                 |
| raytrace                | 297 ms                                                 | 284 ms: 1.05x faster                                                   |
| nqueens                 | 83.4 ms                                                | 79.8 ms: 1.04x faster                                                  |
| bench_thread_pool       | 819 us                                                 | 790 us: 1.04x faster                                                   |
| docutils                | 2.63 sec                                               | 2.54 sec: 1.04x faster                                                 |
| deepcopy                | 342 us                                                 | 331 us: 1.03x faster                                                   |
| float                   | 77.2 ms                                                | 74.7 ms: 1.03x faster                                                  |
| meteor_contest          | 107 ms                                                 | 103 ms: 1.03x faster                                                   |
| fannkuch                | 388 ms                                                 | 376 ms: 1.03x faster                                                   |
| sympy_expand            | 475 ms                                                 | 461 ms: 1.03x faster                                                   |
| sqlglot_optimize        | 53.1 ms                                                | 51.6 ms: 1.03x faster                                                  |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                                  |
| 2to3                    | 259 ms                                                 | 253 ms: 1.03x faster                                                   |
| pathlib                 | 18.2 ms                                                | 17.8 ms: 1.02x faster                                                  |
| regex_compile           | 138 ms                                                 | 135 ms: 1.02x faster                                                   |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                   |
| chaos                   | 69.2 ms                                                | 67.7 ms: 1.02x faster                                                  |
| coverage                | 100 ms                                                 | 98.0 ms: 1.02x faster                                                  |
| pprint_pformat          | 1.46 sec                                               | 1.43 sec: 1.02x faster                                                 |
| sqlalchemy_declarative  | 138 ms                                                 | 136 ms: 1.02x faster                                                   |
| sympy_str               | 290 ms                                                 | 285 ms: 1.02x faster                                                   |
| create_gc_cycles        | 1.49 ms                                                | 1.46 ms: 1.02x faster                                                  |
| scimark_monte_carlo     | 68.1 ms                                                | 67.1 ms: 1.01x faster                                                  |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.01x faster                                                   |
| regex_v8                | 22.0 ms                                                | 21.8 ms: 1.01x faster                                                  |
| crypto_pyaes            | 74.7 ms                                                | 73.8 ms: 1.01x faster                                                  |
| telco                   | 6.58 ms                                                | 6.51 ms: 1.01x faster                                                  |
| regex_dna               | 204 ms                                                 | 202 ms: 1.01x faster                                                   |
| pprint_safe_repr        | 701 ms                                                 | 695 ms: 1.01x faster                                                   |
| mako                    | 10.1 ms                                                | 10.0 ms: 1.01x faster                                                  |
| chameleon               | 6.47 ms                                                | 6.55 ms: 1.01x slower                                                  |
| gc_traversal            | 4.02 ms                                                | 4.07 ms: 1.01x slower                                                  |
| pickle_dict             | 31.1 us                                                | 31.6 us: 1.01x slower                                                  |
| deepcopy_reduce         | 2.94 us                                                | 2.98 us: 1.02x slower                                                  |
| sqlglot_transpile       | 1.70 ms                                                | 1.73 ms: 1.02x slower                                                  |
| unpickle_list           | 4.91 us                                                | 4.99 us: 1.02x slower                                                  |
| pickle                  | 10.1 us                                                | 10.3 us: 1.02x slower                                                  |
| sqlglot_parse           | 1.40 ms                                                | 1.44 ms: 1.03x slower                                                  |
| pickle_list             | 4.11 us                                                | 4.24 us: 1.03x slower                                                  |
| thrift                  | 756 us                                                 | 782 us: 1.03x slower                                                   |
| python_startup          | 8.52 ms                                                | 8.83 ms: 1.04x slower                                                  |
| sqlite_synth            | 2.52 us                                                | 2.63 us: 1.04x slower                                                  |
| xml_etree_process       | 53.9 ms                                                | 56.1 ms: 1.04x slower                                                  |
| django_template         | 32.6 ms                                                | 34.0 ms: 1.04x slower                                                  |
| async_tree_memoization  | 627 ms                                                 | 658 ms: 1.05x slower                                                   |
| comprehensions          | 22.4 us                                                | 23.8 us: 1.06x slower                                                  |
| xml_etree_generate      | 76.2 ms                                                | 81.3 ms: 1.07x slower                                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.52 ms: 1.09x slower                                                  |
| async_generators        | 368 ms                                                 | 416 ms: 1.13x slower                                                   |
| dask                    | 360 ms                                                 | 514 ms: 1.43x slower                                                   |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                           |

Benchmark hidden because not significant (14): unpickle, genshi_text, pyflate, async_tree_none, bench_mp_pool, scimark_lu, sympy_sum, sqlalchemy_imperative, dulwich_log, unpack_sequence, go, async_tree_io, djangocms, async_tree_cpu_io_mixed
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x
