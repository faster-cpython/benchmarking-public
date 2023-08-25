
# Results vs. 3.11.0

- fork: thatbirdguythatuknownot
- ref: patch_30
- machine: linux-x86_64
- commit hash: 148c833
- commit date: 2023-04-15
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230415-linux-x86_64-thatbirdguythatuknownot-patch_30-3.12.0a7+-148c833 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 249 ms: 1.04x faster                                                        |
| docutils       | 2.63 sec                                               | 2.52 sec: 1.04x faster                                                      |
| html5lib       | 64.5 ms                                                | 60.3 ms: 1.07x faster                                                       |
| tornado_http   | 96.3 ms                                                | 93.0 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230415-linux-x86_64-thatbirdguythatuknownot-patch_30-3.12.0a7+-148c833 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 83.5 ms: 1.12x faster                                                       |
| pidigits       | 198 ms                                                 | 188 ms: 1.05x faster                                                        |
| float          | 77.2 ms                                                | 73.7 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                  | 1.07x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230415-linux-x86_64-thatbirdguythatuknownot-patch_30-3.12.0a7+-148c833 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.52 ms: 1.14x faster                                                       |
| regex_compile  | 138 ms                                                 | 129 ms: 1.07x faster                                                        |
| regex_v8       | 22.0 ms                                                | 21.8 ms: 1.01x faster                                                       |
| regex_dna      | 204 ms                                                 | 207 ms: 1.02x slower                                                        |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230415-linux-x86_64-thatbirdguythatuknownot-patch_30-3.12.0a7+-148c833 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.32 ms: 1.35x faster                                                       |
| unpickle_pure_python | 228 us                                                 | 202 us: 1.13x faster                                                        |
| json_loads           | 26.5 us                                                | 24.4 us: 1.09x faster                                                       |
| pickle_pure_python   | 306 us                                                 | 286 us: 1.07x faster                                                        |
| xml_etree_parse      | 158 ms                                                 | 150 ms: 1.06x faster                                                        |
| xml_etree_iterparse  | 104 ms                                                 | 99.8 ms: 1.04x faster                                                       |
| pickle_dict          | 31.1 us                                                | 31.7 us: 1.02x slower                                                       |
| xml_etree_process    | 53.9 ms                                                | 55.0 ms: 1.02x slower                                                       |
| pickle_list          | 4.11 us                                                | 4.24 us: 1.03x slower                                                       |
| unpickle             | 13.7 us                                                | 14.3 us: 1.04x slower                                                       |
| xml_etree_generate   | 76.2 ms                                                | 79.8 ms: 1.05x slower                                                       |
| unpickle_list        | 4.91 us                                                | 5.15 us: 1.05x slower                                                       |
| pickle               | 10.1 us                                                | 10.7 us: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.03x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230415-linux-x86_64-thatbirdguythatuknownot-patch_30-3.12.0a7+-148c833 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.90 ms: 1.04x slower                                                       |
| python_startup_no_site | 6.01 ms                                                | 6.60 ms: 1.10x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230415-linux-x86_64-thatbirdguythatuknownot-patch_30-3.12.0a7+-148c833 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                | 47.1 ms: 1.10x faster                                                       |
| mako           | 10.1 ms                                                | 9.96 ms: 1.01x faster                                                       |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                |

Benchmark hidden because not significant (2): genshi_text, django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230415-linux-x86_64-thatbirdguythatuknownot-patch_30-3.12.0a7+-148c833 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 28.9 ms: 2.54x faster                                                       |
| asyncio_tcp             | 922 ms                                                 | 500 ms: 1.84x faster                                                        |
| json_dumps              | 12.6 ms                                                | 9.32 ms: 1.35x faster                                                       |
| mypy2                   | 420 ms                                                 | 330 ms: 1.27x faster                                                        |
| coroutines              | 25.5 ms                                                | 21.7 ms: 1.17x faster                                                       |
| sqlglot_parse           | 1.40 ms                                                | 1.22 ms: 1.15x faster                                                       |
| deltablue               | 3.67 ms                                                | 3.23 ms: 1.14x faster                                                       |
| regex_effbot            | 3.99 ms                                                | 3.52 ms: 1.14x faster                                                       |
| sqlglot_transpile       | 1.70 ms                                                | 1.50 ms: 1.13x faster                                                       |
| unpickle_pure_python    | 228 us                                                 | 202 us: 1.13x faster                                                        |
| nbody                   | 93.1 ms                                                | 83.5 ms: 1.12x faster                                                       |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.03 ms: 1.11x faster                                                       |
| genshi_xml              | 51.8 ms                                                | 47.1 ms: 1.10x faster                                                       |
| spectral_norm           | 100 ms                                                 | 91.4 ms: 1.09x faster                                                       |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                                       |
| gunicorn                | 1.18 ms                                                | 1.08 ms: 1.09x faster                                                       |
| json_loads              | 26.5 us                                                | 24.4 us: 1.09x faster                                                       |
| richards                | 45.7 ms                                                | 42.3 ms: 1.08x faster                                                       |
| pycparser               | 1.18 sec                                               | 1.10 sec: 1.08x faster                                                      |
| scimark_sor             | 118 ms                                                 | 110 ms: 1.08x faster                                                        |
| html5lib                | 64.5 ms                                                | 60.3 ms: 1.07x faster                                                       |
| pickle_pure_python      | 306 us                                                 | 286 us: 1.07x faster                                                        |
| hexiom                  | 6.37 ms                                                | 5.96 ms: 1.07x faster                                                       |
| chaos                   | 69.2 ms                                                | 64.8 ms: 1.07x faster                                                       |
| regex_compile           | 138 ms                                                 | 129 ms: 1.07x faster                                                        |
| pathlib                 | 18.2 ms                                                | 17.2 ms: 1.06x faster                                                       |
| deepcopy_memo           | 37.0 us                                                | 34.9 us: 1.06x faster                                                       |
| xml_etree_parse         | 158 ms                                                 | 150 ms: 1.06x faster                                                        |
| pylint                  | 465 ms                                                 | 439 ms: 1.06x faster                                                        |
| scimark_fft             | 328 ms                                                 | 310 ms: 1.06x faster                                                        |
| json                    | 4.94 ms                                                | 4.67 ms: 1.06x faster                                                       |
| logging_silent          | 101 ns                                                 | 95.8 ns: 1.06x faster                                                       |
| raytrace                | 297 ms                                                 | 282 ms: 1.05x faster                                                        |
| pidigits                | 198 ms                                                 | 188 ms: 1.05x faster                                                        |
| logging_format          | 6.68 us                                                | 6.36 us: 1.05x faster                                                       |
| comprehensions          | 22.4 us                                                | 21.4 us: 1.05x faster                                                       |
| logging_simple          | 6.03 us                                                | 5.76 us: 1.05x faster                                                       |
| float                   | 77.2 ms                                                | 73.7 ms: 1.05x faster                                                       |
| docutils                | 2.63 sec                                               | 2.52 sec: 1.04x faster                                                      |
| bench_thread_pool       | 819 us                                                 | 786 us: 1.04x faster                                                        |
| scimark_lu              | 110 ms                                                 | 105 ms: 1.04x faster                                                        |
| xml_etree_iterparse     | 104 ms                                                 | 99.8 ms: 1.04x faster                                                       |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                                        |
| 2to3                    | 259 ms                                                 | 249 ms: 1.04x faster                                                        |
| sqlglot_optimize        | 53.1 ms                                                | 51.2 ms: 1.04x faster                                                       |
| sympy_expand            | 475 ms                                                 | 459 ms: 1.04x faster                                                        |
| tornado_http            | 96.3 ms                                                | 93.0 ms: 1.04x faster                                                       |
| coverage                | 100 ms                                                 | 96.8 ms: 1.03x faster                                                       |
| sympy_str               | 290 ms                                                 | 281 ms: 1.03x faster                                                        |
| sqlalchemy_imperative   | 17.9 ms                                                | 17.3 ms: 1.03x faster                                                       |
| go                      | 140 ms                                                 | 136 ms: 1.03x faster                                                        |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                                       |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.03x faster                                                        |
| scimark_monte_carlo     | 68.1 ms                                                | 66.2 ms: 1.03x faster                                                       |
| mdp                     | 2.62 sec                                               | 2.55 sec: 1.03x faster                                                      |
| nqueens                 | 83.4 ms                                                | 81.1 ms: 1.03x faster                                                       |
| deepcopy                | 342 us                                                 | 334 us: 1.02x faster                                                        |
| dulwich_log             | 63.7 ms                                                | 62.3 ms: 1.02x faster                                                       |
| sqlalchemy_declarative  | 138 ms                                                 | 135 ms: 1.02x faster                                                        |
| sympy_sum               | 167 ms                                                 | 163 ms: 1.02x faster                                                        |
| async_tree_cpu_io_mixed | 739 ms                                                 | 724 ms: 1.02x faster                                                        |
| async_tree_none         | 526 ms                                                 | 517 ms: 1.02x faster                                                        |
| async_tree_memoization  | 627 ms                                                 | 616 ms: 1.02x faster                                                        |
| telco                   | 6.58 ms                                                | 6.48 ms: 1.02x faster                                                       |
| create_gc_cycles        | 1.49 ms                                                | 1.47 ms: 1.01x faster                                                       |
| mako                    | 10.1 ms                                                | 9.96 ms: 1.01x faster                                                       |
| async_tree_io           | 1.30 sec                                               | 1.28 sec: 1.01x faster                                                      |
| pprint_pformat          | 1.46 sec                                               | 1.44 sec: 1.01x faster                                                      |
| pyflate                 | 418 ms                                                 | 414 ms: 1.01x faster                                                        |
| regex_v8                | 22.0 ms                                                | 21.8 ms: 1.01x faster                                                       |
| pprint_safe_repr        | 701 ms                                                 | 704 ms: 1.00x slower                                                        |
| gc_traversal            | 4.02 ms                                                | 4.06 ms: 1.01x slower                                                       |
| regex_dna               | 204 ms                                                 | 207 ms: 1.02x slower                                                        |
| pickle_dict             | 31.1 us                                                | 31.7 us: 1.02x slower                                                       |
| xml_etree_process       | 53.9 ms                                                | 55.0 ms: 1.02x slower                                                       |
| deepcopy_reduce         | 2.94 us                                                | 3.02 us: 1.03x slower                                                       |
| pickle_list             | 4.11 us                                                | 4.24 us: 1.03x slower                                                       |
| python_startup          | 8.52 ms                                                | 8.90 ms: 1.04x slower                                                       |
| unpickle                | 13.7 us                                                | 14.3 us: 1.04x slower                                                       |
| sqlite_synth            | 2.52 us                                                | 2.64 us: 1.05x slower                                                       |
| thrift                  | 756 us                                                 | 792 us: 1.05x slower                                                        |
| xml_etree_generate      | 76.2 ms                                                | 79.8 ms: 1.05x slower                                                       |
| unpickle_list           | 4.91 us                                                | 5.15 us: 1.05x slower                                                       |
| pickle                  | 10.1 us                                                | 10.7 us: 1.06x slower                                                       |
| python_startup_no_site  | 6.01 ms                                                | 6.60 ms: 1.10x slower                                                       |
| async_generators        | 368 ms                                                 | 427 ms: 1.16x slower                                                        |
| dask                    | 360 ms                                                 | 491 ms: 1.37x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.05x faster                                                                |

Benchmark hidden because not significant (8): djangocms, unpack_sequence, crypto_pyaes, fannkuch, genshi_text, bench_mp_pool, chameleon, django_template
Ignored benchmarks (5) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
