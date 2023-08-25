
# Results vs. 3.11.0

- fork: penguin-wwy
- ref: add_return_none
- machine: linux-x86_64
- commit hash: f1deb5c
- commit date: 2023-02-07
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                                     |
| chameleon      | 6.47 ms                                                | 6.36 ms: 1.02x faster                                                    |
| docutils       | 2.63 sec                                               | 2.49 sec: 1.06x faster                                                   |
| html5lib       | 64.5 ms                                                | 59.6 ms: 1.08x faster                                                    |
| tornado_http   | 96.3 ms                                                | 93.8 ms: 1.03x faster                                                    |
| Geometric mean | (ref)                                                  | 1.04x faster                                                             |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.1 ms: 1.07x faster                                                    |
| pidigits       | 198 ms                                                 | 197 ms: 1.00x faster                                                     |
| nbody          | 93.1 ms                                                | 95.5 ms: 1.02x slower                                                    |
| Geometric mean | (ref)                                                  | 1.02x faster                                                             |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.50 ms: 1.14x faster                                                    |
| regex_compile  | 138 ms                                                 | 127 ms: 1.09x faster                                                     |
| regex_v8       | 22.0 ms                                                | 21.2 ms: 1.04x faster                                                    |
| regex_dna      | 204 ms                                                 | 200 ms: 1.02x faster                                                     |
| Geometric mean | (ref)                                                  | 1.07x faster                                                             |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.37 ms: 1.34x faster                                                    |
| unpickle_pure_python | 228 us                                                 | 198 us: 1.15x faster                                                     |
| json_loads           | 26.5 us                                                | 24.2 us: 1.09x faster                                                    |
| pickle_pure_python   | 306 us                                                 | 284 us: 1.08x faster                                                     |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.07x faster                                                     |
| unpickle             | 13.7 us                                                | 13.1 us: 1.04x faster                                                    |
| pickle_dict          | 31.1 us                                                | 30.6 us: 1.02x faster                                                    |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                     |
| pickle_list          | 4.11 us                                                | 4.07 us: 1.01x faster                                                    |
| xml_etree_process    | 53.9 ms                                                | 53.5 ms: 1.01x faster                                                    |
| xml_etree_generate   | 76.2 ms                                                | 77.1 ms: 1.01x slower                                                    |
| unpickle_list        | 4.91 us                                                | 5.07 us: 1.03x slower                                                    |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                             |

Benchmark hidden because not significant (1): pickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.90 ms: 1.04x slower                                                    |
| python_startup_no_site | 6.01 ms                                                | 6.46 ms: 1.07x slower                                                    |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                             |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 46.6 ms: 1.11x faster                                                    |
| genshi_text     | 21.6 ms                                                | 20.5 ms: 1.05x faster                                                    |
| mako            | 10.1 ms                                                | 9.63 ms: 1.05x faster                                                    |
| django_template | 32.6 ms                                                | 33.2 ms: 1.02x slower                                                    |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                             |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 491 ms: 1.88x faster                                                     |
| json_dumps              | 12.6 ms                                                | 9.37 ms: 1.34x faster                                                    |
| deltablue               | 3.67 ms                                                | 3.16 ms: 1.16x faster                                                    |
| unpickle_pure_python    | 228 us                                                 | 198 us: 1.15x faster                                                     |
| gc_traversal            | 4.02 ms                                                | 3.52 ms: 1.14x faster                                                    |
| regex_effbot            | 3.99 ms                                                | 3.50 ms: 1.14x faster                                                    |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.01 ms: 1.12x faster                                                    |
| logging_silent          | 101 ns                                                 | 90.7 ns: 1.12x faster                                                    |
| genshi_xml              | 51.8 ms                                                | 46.6 ms: 1.11x faster                                                    |
| scimark_sor             | 118 ms                                                 | 106 ms: 1.11x faster                                                     |
| aiohttp                 | 1.10 ms                                                | 995 us: 1.11x faster                                                     |
| gunicorn                | 1.18 ms                                                | 1.07 ms: 1.10x faster                                                    |
| json_loads              | 26.5 us                                                | 24.2 us: 1.09x faster                                                    |
| richards                | 45.7 ms                                                | 41.9 ms: 1.09x faster                                                    |
| regex_compile           | 138 ms                                                 | 127 ms: 1.09x faster                                                     |
| scimark_fft             | 328 ms                                                 | 303 ms: 1.08x faster                                                     |
| html5lib                | 64.5 ms                                                | 59.6 ms: 1.08x faster                                                    |
| sympy_str               | 290 ms                                                 | 269 ms: 1.08x faster                                                     |
| pickle_pure_python      | 306 us                                                 | 284 us: 1.08x faster                                                     |
| deepcopy_memo           | 37.0 us                                                | 34.5 us: 1.07x faster                                                    |
| nqueens                 | 83.4 ms                                                | 77.8 ms: 1.07x faster                                                    |
| chaos                   | 69.2 ms                                                | 64.6 ms: 1.07x faster                                                    |
| float                   | 77.2 ms                                                | 72.1 ms: 1.07x faster                                                    |
| sympy_sum               | 167 ms                                                 | 156 ms: 1.07x faster                                                     |
| hexiom                  | 6.37 ms                                                | 5.96 ms: 1.07x faster                                                    |
| pycparser               | 1.18 sec                                               | 1.11 sec: 1.07x faster                                                   |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.07x faster                                                     |
| sympy_integrate         | 21.0 ms                                                | 19.7 ms: 1.06x faster                                                    |
| logging_format          | 6.68 us                                                | 6.29 us: 1.06x faster                                                    |
| pprint_pformat          | 1.46 sec                                               | 1.37 sec: 1.06x faster                                                   |
| json                    | 4.94 ms                                                | 4.66 ms: 1.06x faster                                                    |
| logging_simple          | 6.03 us                                                | 5.69 us: 1.06x faster                                                    |
| docutils                | 2.63 sec                                               | 2.49 sec: 1.06x faster                                                   |
| async_generators        | 368 ms                                                 | 349 ms: 1.06x faster                                                     |
| spectral_norm           | 100 ms                                                 | 94.9 ms: 1.05x faster                                                    |
| genshi_text             | 21.6 ms                                                | 20.5 ms: 1.05x faster                                                    |
| bench_thread_pool       | 819 us                                                 | 780 us: 1.05x faster                                                     |
| pprint_safe_repr        | 701 ms                                                 | 668 ms: 1.05x faster                                                     |
| fannkuch                | 388 ms                                                 | 370 ms: 1.05x faster                                                     |
| mako                    | 10.1 ms                                                | 9.63 ms: 1.05x faster                                                    |
| sympy_expand            | 475 ms                                                 | 454 ms: 1.05x faster                                                     |
| unpickle                | 13.7 us                                                | 13.1 us: 1.04x faster                                                    |
| scimark_monte_carlo     | 68.1 ms                                                | 65.3 ms: 1.04x faster                                                    |
| raytrace                | 297 ms                                                 | 285 ms: 1.04x faster                                                     |
| sqlglot_optimize        | 53.1 ms                                                | 51.0 ms: 1.04x faster                                                    |
| telco                   | 6.58 ms                                                | 6.33 ms: 1.04x faster                                                    |
| regex_v8                | 22.0 ms                                                | 21.2 ms: 1.04x faster                                                    |
| scimark_lu              | 110 ms                                                 | 106 ms: 1.04x faster                                                     |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                                     |
| pathlib                 | 18.2 ms                                                | 17.7 ms: 1.03x faster                                                    |
| deepcopy                | 342 us                                                 | 332 us: 1.03x faster                                                     |
| pyflate                 | 418 ms                                                 | 406 ms: 1.03x faster                                                     |
| go                      | 140 ms                                                 | 136 ms: 1.03x faster                                                     |
| tornado_http            | 96.3 ms                                                | 93.8 ms: 1.03x faster                                                    |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                     |
| dulwich_log             | 63.7 ms                                                | 62.2 ms: 1.02x faster                                                    |
| thrift                  | 756 us                                                 | 739 us: 1.02x faster                                                     |
| regex_dna               | 204 ms                                                 | 200 ms: 1.02x faster                                                     |
| sqlalchemy_imperative   | 17.9 ms                                                | 17.5 ms: 1.02x faster                                                    |
| crypto_pyaes            | 74.7 ms                                                | 73.2 ms: 1.02x faster                                                    |
| create_gc_cycles        | 1.49 ms                                                | 1.46 ms: 1.02x faster                                                    |
| pickle_dict             | 31.1 us                                                | 30.6 us: 1.02x faster                                                    |
| chameleon               | 6.47 ms                                                | 6.36 ms: 1.02x faster                                                    |
| coverage                | 100 ms                                                 | 98.4 ms: 1.02x faster                                                    |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                                     |
| sqlalchemy_declarative  | 138 ms                                                 | 136 ms: 1.01x faster                                                     |
| pickle_list             | 4.11 us                                                | 4.07 us: 1.01x faster                                                    |
| coroutines              | 25.5 ms                                                | 25.3 ms: 1.01x faster                                                    |
| sqlglot_transpile       | 1.70 ms                                                | 1.69 ms: 1.01x faster                                                    |
| xml_etree_process       | 53.9 ms                                                | 53.5 ms: 1.01x faster                                                    |
| mdp                     | 2.62 sec                                               | 2.60 sec: 1.00x faster                                                   |
| pidigits                | 198 ms                                                 | 197 ms: 1.00x faster                                                     |
| xml_etree_generate      | 76.2 ms                                                | 77.1 ms: 1.01x slower                                                    |
| django_template         | 32.6 ms                                                | 33.2 ms: 1.02x slower                                                    |
| async_tree_cpu_io_mixed | 739 ms                                                 | 754 ms: 1.02x slower                                                     |
| sqlite_synth            | 2.52 us                                                | 2.58 us: 1.02x slower                                                    |
| async_tree_io           | 1.30 sec                                               | 1.33 sec: 1.02x slower                                                   |
| nbody                   | 93.1 ms                                                | 95.5 ms: 1.02x slower                                                    |
| generators              | 73.5 ms                                                | 75.6 ms: 1.03x slower                                                    |
| unpickle_list           | 4.91 us                                                | 5.07 us: 1.03x slower                                                    |
| python_startup          | 8.52 ms                                                | 8.90 ms: 1.04x slower                                                    |
| async_tree_memoization  | 627 ms                                                 | 667 ms: 1.06x slower                                                     |
| python_startup_no_site  | 6.01 ms                                                | 6.46 ms: 1.07x slower                                                    |
| Geometric mean          | (ref)                                                  | 1.05x faster                                                             |

Benchmark hidden because not significant (8): pickle, meteor_contest, async_tree_none, unpack_sequence, bench_mp_pool, djangocms, sqlglot_parse, deepcopy_reduce
Ignored benchmarks (9) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, dask, flaskblogging, mypy2, pylint, richards_super, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230207-3.12.0a4+-f1deb5c/bm-20230207-linux-x86_64-penguin%2dwwy-add_return_none-3.12.0a4+-f1deb5c.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x
