
# Results vs. 3.11.0

- fork: iritkatriel
- ref: remove_JUMP_IF_FALSE
- machine: linux-x86_64
- commit hash: 12595f6
- commit date: 2023-03-21
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230321-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-12595f6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 249 ms: 1.04x faster                                                        |
| chameleon      | 6.47 ms                                                | 6.56 ms: 1.01x slower                                                       |
| docutils       | 2.63 sec                                               | 2.54 sec: 1.03x faster                                                      |
| html5lib       | 64.5 ms                                                | 60.8 ms: 1.06x faster                                                       |
| tornado_http   | 96.3 ms                                                | 91.5 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230321-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-12595f6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 87.2 ms: 1.07x faster                                                       |
| float          | 77.2 ms                                                | 73.2 ms: 1.05x faster                                                       |
| pidigits       | 198 ms                                                 | 189 ms: 1.04x faster                                                        |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230321-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-12595f6 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.59 ms: 1.11x faster                                                       |
| regex_compile  | 138 ms                                                 | 134 ms: 1.03x faster                                                        |
| regex_dna      | 204 ms                                                 | 201 ms: 1.01x faster                                                        |
| regex_v8       | 22.0 ms                                                | 22.0 ms: 1.00x faster                                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230321-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-12595f6 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.51 ms: 1.32x faster                                                       |
| unpickle_pure_python | 228 us                                                 | 198 us: 1.15x faster                                                        |
| json_loads           | 26.5 us                                                | 24.0 us: 1.10x faster                                                       |
| pickle_pure_python   | 306 us                                                 | 287 us: 1.07x faster                                                        |
| xml_etree_parse      | 158 ms                                                 | 150 ms: 1.06x faster                                                        |
| pickle_dict          | 31.1 us                                                | 30.8 us: 1.01x faster                                                       |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                                        |
| pickle_list          | 4.11 us                                                | 4.08 us: 1.01x faster                                                       |
| pickle               | 10.1 us                                                | 10.2 us: 1.01x slower                                                       |
| unpickle_list        | 4.91 us                                                | 5.01 us: 1.02x slower                                                       |
| xml_etree_process    | 53.9 ms                                                | 56.8 ms: 1.05x slower                                                       |
| xml_etree_generate   | 76.2 ms                                                | 81.6 ms: 1.07x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230321-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-12595f6 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.87 ms: 1.04x slower                                                       |
| python_startup_no_site | 6.01 ms                                                | 6.50 ms: 1.08x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230321-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-12595f6 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 46.8 ms: 1.11x faster                                                       |
| mako            | 10.1 ms                                                | 10.0 ms: 1.00x faster                                                       |
| genshi_text     | 21.6 ms                                                | 21.8 ms: 1.01x slower                                                       |
| django_template | 32.6 ms                                                | 33.2 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230321-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-12595f6 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.2 ms: 2.52x faster                                                       |
| asyncio_tcp             | 922 ms                                                 | 512 ms: 1.80x faster                                                        |
| json_dumps              | 12.6 ms                                                | 9.51 ms: 1.32x faster                                                       |
| mypy2                   | 420 ms                                                 | 333 ms: 1.26x faster                                                        |
| coroutines              | 25.5 ms                                                | 22.0 ms: 1.16x faster                                                       |
| deltablue               | 3.67 ms                                                | 3.18 ms: 1.15x faster                                                       |
| unpickle_pure_python    | 228 us                                                 | 198 us: 1.15x faster                                                        |
| scimark_sor             | 118 ms                                                 | 104 ms: 1.13x faster                                                        |
| spectral_norm           | 100 ms                                                 | 88.6 ms: 1.13x faster                                                       |
| regex_effbot            | 3.99 ms                                                | 3.59 ms: 1.11x faster                                                       |
| genshi_xml              | 51.8 ms                                                | 46.8 ms: 1.11x faster                                                       |
| json_loads              | 26.5 us                                                | 24.0 us: 1.10x faster                                                       |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                                       |
| gunicorn                | 1.18 ms                                                | 1.09 ms: 1.08x faster                                                       |
| mdp                     | 2.62 sec                                               | 2.43 sec: 1.08x faster                                                      |
| json                    | 4.94 ms                                                | 4.61 ms: 1.07x faster                                                       |
| deepcopy_memo           | 37.0 us                                                | 34.6 us: 1.07x faster                                                       |
| nbody                   | 93.1 ms                                                | 87.2 ms: 1.07x faster                                                       |
| pickle_pure_python      | 306 us                                                 | 287 us: 1.07x faster                                                        |
| scimark_fft             | 328 ms                                                 | 309 ms: 1.06x faster                                                        |
| html5lib                | 64.5 ms                                                | 60.8 ms: 1.06x faster                                                       |
| logging_format          | 6.68 us                                                | 6.32 us: 1.06x faster                                                       |
| xml_etree_parse         | 158 ms                                                 | 150 ms: 1.06x faster                                                        |
| float                   | 77.2 ms                                                | 73.2 ms: 1.05x faster                                                       |
| coverage                | 100 ms                                                 | 94.9 ms: 1.05x faster                                                       |
| tornado_http            | 96.3 ms                                                | 91.5 ms: 1.05x faster                                                       |
| richards                | 45.7 ms                                                | 43.5 ms: 1.05x faster                                                       |
| gc_traversal            | 4.02 ms                                                | 3.83 ms: 1.05x faster                                                       |
| pycparser               | 1.18 sec                                               | 1.13 sec: 1.05x faster                                                      |
| raytrace                | 297 ms                                                 | 283 ms: 1.05x faster                                                        |
| fannkuch                | 388 ms                                                 | 371 ms: 1.05x faster                                                        |
| go                      | 140 ms                                                 | 134 ms: 1.05x faster                                                        |
| pidigits                | 198 ms                                                 | 189 ms: 1.04x faster                                                        |
| logging_simple          | 6.03 us                                                | 5.78 us: 1.04x faster                                                       |
| hexiom                  | 6.37 ms                                                | 6.11 ms: 1.04x faster                                                       |
| 2to3                    | 259 ms                                                 | 249 ms: 1.04x faster                                                        |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.32 ms: 1.04x faster                                                       |
| chaos                   | 69.2 ms                                                | 66.6 ms: 1.04x faster                                                       |
| bench_thread_pool       | 819 us                                                 | 788 us: 1.04x faster                                                        |
| deepcopy                | 342 us                                                 | 330 us: 1.04x faster                                                        |
| docutils                | 2.63 sec                                               | 2.54 sec: 1.03x faster                                                      |
| sympy_expand            | 475 ms                                                 | 459 ms: 1.03x faster                                                        |
| regex_compile           | 138 ms                                                 | 134 ms: 1.03x faster                                                        |
| meteor_contest          | 107 ms                                                 | 103 ms: 1.03x faster                                                        |
| nqueens                 | 83.4 ms                                                | 80.8 ms: 1.03x faster                                                       |
| sqlglot_optimize        | 53.1 ms                                                | 51.5 ms: 1.03x faster                                                       |
| scimark_monte_carlo     | 68.1 ms                                                | 66.2 ms: 1.03x faster                                                       |
| logging_silent          | 101 ns                                                 | 98.4 ns: 1.03x faster                                                       |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                                       |
| pyflate                 | 418 ms                                                 | 407 ms: 1.03x faster                                                        |
| sympy_str               | 290 ms                                                 | 283 ms: 1.03x faster                                                        |
| pathlib                 | 18.2 ms                                                | 17.8 ms: 1.02x faster                                                       |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.02x faster                                                        |
| crypto_pyaes            | 74.7 ms                                                | 73.4 ms: 1.02x faster                                                       |
| sqlalchemy_declarative  | 138 ms                                                 | 136 ms: 1.01x faster                                                        |
| regex_dna               | 204 ms                                                 | 201 ms: 1.01x faster                                                        |
| scimark_lu              | 110 ms                                                 | 109 ms: 1.01x faster                                                        |
| pickle_dict             | 31.1 us                                                | 30.8 us: 1.01x faster                                                       |
| telco                   | 6.58 ms                                                | 6.51 ms: 1.01x faster                                                       |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                                        |
| pickle_list             | 4.11 us                                                | 4.08 us: 1.01x faster                                                       |
| pprint_pformat          | 1.46 sec                                               | 1.45 sec: 1.01x faster                                                      |
| dulwich_log             | 63.7 ms                                                | 63.3 ms: 1.01x faster                                                       |
| mako                    | 10.1 ms                                                | 10.0 ms: 1.00x faster                                                       |
| regex_v8                | 22.0 ms                                                | 22.0 ms: 1.00x faster                                                       |
| create_gc_cycles        | 1.49 ms                                                | 1.50 ms: 1.01x slower                                                       |
| genshi_text             | 21.6 ms                                                | 21.8 ms: 1.01x slower                                                       |
| pprint_safe_repr        | 701 ms                                                 | 711 ms: 1.01x slower                                                        |
| chameleon               | 6.47 ms                                                | 6.56 ms: 1.01x slower                                                       |
| pickle                  | 10.1 us                                                | 10.2 us: 1.01x slower                                                       |
| deepcopy_reduce         | 2.94 us                                                | 2.98 us: 1.02x slower                                                       |
| django_template         | 32.6 ms                                                | 33.2 ms: 1.02x slower                                                       |
| unpickle_list           | 4.91 us                                                | 5.01 us: 1.02x slower                                                       |
| thrift                  | 756 us                                                 | 773 us: 1.02x slower                                                        |
| sqlglot_transpile       | 1.70 ms                                                | 1.74 ms: 1.02x slower                                                       |
| unpack_sequence         | 43.1 ns                                                | 44.2 ns: 1.02x slower                                                       |
| sqlglot_parse           | 1.40 ms                                                | 1.45 ms: 1.04x slower                                                       |
| sqlite_synth            | 2.52 us                                                | 2.61 us: 1.04x slower                                                       |
| python_startup          | 8.52 ms                                                | 8.87 ms: 1.04x slower                                                       |
| xml_etree_process       | 53.9 ms                                                | 56.8 ms: 1.05x slower                                                       |
| async_tree_memoization  | 627 ms                                                 | 666 ms: 1.06x slower                                                        |
| comprehensions          | 22.4 us                                                | 23.9 us: 1.06x slower                                                       |
| xml_etree_generate      | 76.2 ms                                                | 81.6 ms: 1.07x slower                                                       |
| python_startup_no_site  | 6.01 ms                                                | 6.50 ms: 1.08x slower                                                       |
| async_generators        | 368 ms                                                 | 411 ms: 1.12x slower                                                        |
| dask                    | 360 ms                                                 | 508 ms: 1.41x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                                |

Benchmark hidden because not significant (8): sympy_sum, djangocms, bench_mp_pool, sqlalchemy_imperative, async_tree_none, async_tree_io, async_tree_cpu_io_mixed, unpickle
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x
