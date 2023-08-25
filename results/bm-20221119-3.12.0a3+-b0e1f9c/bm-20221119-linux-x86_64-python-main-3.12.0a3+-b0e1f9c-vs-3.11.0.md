
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: b0e1f9c
- commit date: 2022-11-19
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221119-linux-x86_64-python-main-3.12.0a3+-b0e1f9c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 245 ms: 1.06x faster                                   |
| html5lib       | 64.5 ms                                                | 59.1 ms: 1.09x faster                                  |
| tornado_http   | 96.3 ms                                                | 92.7 ms: 1.04x faster                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221119-linux-x86_64-python-main-3.12.0a3+-b0e1f9c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 77.2 ms                                                | 71.6 ms: 1.08x faster                                  |
| pidigits       | 198 ms                                                 | 192 ms: 1.03x faster                                   |
| nbody          | 93.1 ms                                                | 94.1 ms: 1.01x slower                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221119-linux-x86_64-python-main-3.12.0a3+-b0e1f9c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_compile  | 138 ms                                                 | 127 ms: 1.09x faster                                   |
| regex_effbot   | 3.99 ms                                                | 3.77 ms: 1.06x faster                                  |
| regex_v8       | 22.0 ms                                                | 22.2 ms: 1.00x slower                                  |
| regex_dna      | 204 ms                                                 | 213 ms: 1.04x slower                                   |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221119-linux-x86_64-python-main-3.12.0a3+-b0e1f9c |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.42 ms: 1.34x faster                                  |
| unpickle_pure_python | 228 us                                                 | 201 us: 1.13x faster                                   |
| json_loads           | 26.5 us                                                | 24.2 us: 1.10x faster                                  |
| pickle_pure_python   | 306 us                                                 | 283 us: 1.08x faster                                   |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                   |
| xml_etree_process    | 53.9 ms                                                | 52.9 ms: 1.02x faster                                  |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| pickle_dict          | 31.1 us                                                | 31.0 us: 1.01x faster                                  |
| pickle               | 10.1 us                                                | 10.2 us: 1.01x slower                                  |
| unpickle_list        | 4.91 us                                                | 5.10 us: 1.04x slower                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (3): unpickle, pickle_list, xml_etree_generate

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221119-linux-x86_64-python-main-3.12.0a3+-b0e1f9c |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.51 ms: 1.00x faster                                  |
| python_startup_no_site | 6.01 ms                                                | 6.25 ms: 1.04x slower                                  |
| Geometric mean         | (ref)                                                  | 1.02x slower                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221119-linux-x86_64-python-main-3.12.0a3+-b0e1f9c |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                | 46.2 ms: 1.12x faster                                  |
| genshi_text    | 21.6 ms                                                | 20.4 ms: 1.05x faster                                  |
| mako           | 10.1 ms                                                | 9.94 ms: 1.01x faster                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221119-linux-x86_64-python-main-3.12.0a3+-b0e1f9c |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps              | 12.6 ms                                                | 9.42 ms: 1.34x faster                                  |
| deltablue               | 3.67 ms                                                | 3.23 ms: 1.14x faster                                  |
| scimark_sparse_mat_mult | 4.50 ms                                                | 3.96 ms: 1.14x faster                                  |
| unpickle_pure_python    | 228 us                                                 | 201 us: 1.13x faster                                   |
| scimark_sor             | 118 ms                                                 | 104 ms: 1.13x faster                                   |
| genshi_xml              | 51.8 ms                                                | 46.2 ms: 1.12x faster                                  |
| logging_silent          | 101 ns                                                 | 91.1 ns: 1.11x faster                                  |
| aiohttp                 | 1.10 ms                                                | 999 us: 1.10x faster                                   |
| richards                | 45.7 ms                                                | 41.6 ms: 1.10x faster                                  |
| json_loads              | 26.5 us                                                | 24.2 us: 1.10x faster                                  |
| gunicorn                | 1.18 ms                                                | 1.08 ms: 1.10x faster                                  |
| html5lib                | 64.5 ms                                                | 59.1 ms: 1.09x faster                                  |
| regex_compile           | 138 ms                                                 | 127 ms: 1.09x faster                                   |
| scimark_fft             | 328 ms                                                 | 303 ms: 1.08x faster                                   |
| deepcopy_memo           | 37.0 us                                                | 34.2 us: 1.08x faster                                  |
| pickle_pure_python      | 306 us                                                 | 283 us: 1.08x faster                                   |
| float                   | 77.2 ms                                                | 71.6 ms: 1.08x faster                                  |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                   |
| raytrace                | 297 ms                                                 | 278 ms: 1.07x faster                                   |
| scimark_monte_carlo     | 68.1 ms                                                | 64.0 ms: 1.06x faster                                  |
| json                    | 4.94 ms                                                | 4.67 ms: 1.06x faster                                  |
| regex_effbot            | 3.99 ms                                                | 3.77 ms: 1.06x faster                                  |
| pprint_pformat          | 1.46 sec                                               | 1.38 sec: 1.06x faster                                 |
| 2to3                    | 259 ms                                                 | 245 ms: 1.06x faster                                   |
| sqlglot_parse           | 1.40 ms                                                | 1.33 ms: 1.06x faster                                  |
| pycparser               | 1.18 sec                                               | 1.12 sec: 1.06x faster                                 |
| sqlglot_transpile       | 1.70 ms                                                | 1.61 ms: 1.06x faster                                  |
| scimark_lu              | 110 ms                                                 | 104 ms: 1.05x faster                                   |
| genshi_text             | 21.6 ms                                                | 20.4 ms: 1.05x faster                                  |
| logging_format          | 6.68 us                                                | 6.35 us: 1.05x faster                                  |
| dulwich_log             | 63.7 ms                                                | 60.6 ms: 1.05x faster                                  |
| telco                   | 6.58 ms                                                | 6.27 ms: 1.05x faster                                  |
| fannkuch                | 388 ms                                                 | 369 ms: 1.05x faster                                   |
| chaos                   | 69.2 ms                                                | 66.0 ms: 1.05x faster                                  |
| sqlglot_optimize        | 53.1 ms                                                | 50.7 ms: 1.05x faster                                  |
| logging_simple          | 6.03 us                                                | 5.77 us: 1.05x faster                                  |
| pprint_safe_repr        | 701 ms                                                 | 673 ms: 1.04x faster                                   |
| pathlib                 | 18.2 ms                                                | 17.5 ms: 1.04x faster                                  |
| sympy_expand            | 475 ms                                                 | 457 ms: 1.04x faster                                   |
| pyflate                 | 418 ms                                                 | 403 ms: 1.04x faster                                   |
| tornado_http            | 96.3 ms                                                | 92.7 ms: 1.04x faster                                  |
| deepcopy                | 342 us                                                 | 330 us: 1.04x faster                                   |
| go                      | 140 ms                                                 | 135 ms: 1.03x faster                                   |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.03x faster                                   |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                  |
| pidigits                | 198 ms                                                 | 192 ms: 1.03x faster                                   |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                   |
| coroutines              | 25.5 ms                                                | 24.8 ms: 1.03x faster                                  |
| hexiom                  | 6.37 ms                                                | 6.21 ms: 1.03x faster                                  |
| spectral_norm           | 100 ms                                                 | 97.6 ms: 1.02x faster                                  |
| sympy_str               | 290 ms                                                 | 283 ms: 1.02x faster                                   |
| nqueens                 | 83.4 ms                                                | 81.5 ms: 1.02x faster                                  |
| coverage                | 100 ms                                                 | 98.2 ms: 1.02x faster                                  |
| xml_etree_process       | 53.9 ms                                                | 52.9 ms: 1.02x faster                                  |
| mako                    | 10.1 ms                                                | 9.94 ms: 1.01x faster                                  |
| async_tree_cpu_io_mixed | 739 ms                                                 | 729 ms: 1.01x faster                                   |
| thrift                  | 756 us                                                 | 746 us: 1.01x faster                                   |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| sympy_sum               | 167 ms                                                 | 165 ms: 1.01x faster                                   |
| pickle_dict             | 31.1 us                                                | 31.0 us: 1.01x faster                                  |
| crypto_pyaes            | 74.7 ms                                                | 74.3 ms: 1.00x faster                                  |
| python_startup          | 8.52 ms                                                | 8.51 ms: 1.00x faster                                  |
| regex_v8                | 22.0 ms                                                | 22.2 ms: 1.00x slower                                  |
| nbody                   | 93.1 ms                                                | 94.1 ms: 1.01x slower                                  |
| mdp                     | 2.62 sec                                               | 2.65 sec: 1.01x slower                                 |
| pickle                  | 10.1 us                                                | 10.2 us: 1.01x slower                                  |
| deepcopy_reduce         | 2.94 us                                                | 2.98 us: 1.01x slower                                  |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                 |
| unpickle_list           | 4.91 us                                                | 5.10 us: 1.04x slower                                  |
| python_startup_no_site  | 6.01 ms                                                | 6.25 ms: 1.04x slower                                  |
| regex_dna               | 204 ms                                                 | 213 ms: 1.04x slower                                   |
| sqlite_synth            | 2.52 us                                                | 2.64 us: 1.05x slower                                  |
| async_tree_memoization  | 627 ms                                                 | 665 ms: 1.06x slower                                   |
| generators              | 73.5 ms                                                | 78.0 ms: 1.06x slower                                  |
| Geometric mean          | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (7): unpickle, unpack_sequence, pickle_list, django_template, async_tree_none, xml_etree_generate, chameleon
Ignored benchmarks (19) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: async_generators, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, create_gc_cycles, dask, djangocms, docutils, flaskblogging, gc_traversal, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221119-3.12.0a3+-b0e1f9c/bm-20221119-linux-x86_64-python-main-3.12.0a3+-b0e1f9c.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
