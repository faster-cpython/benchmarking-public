
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 660f102
- commit date: 2022-10-15
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221015-linux-x86_64-python-main-3.12.0a1+-660f102 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 249 ms: 1.04x faster                                   |
| chameleon      | 6.47 ms                                                | 6.71 ms: 1.04x slower                                  |
| html5lib       | 64.5 ms                                                | 59.2 ms: 1.09x faster                                  |
| tornado_http   | 96.3 ms                                                | 92.6 ms: 1.04x faster                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221015-linux-x86_64-python-main-3.12.0a1+-660f102 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.2 ms: 1.07x faster                                  |
| pidigits       | 198 ms                                                 | 199 ms: 1.01x slower                                   |
| nbody          | 93.1 ms                                                | 94.2 ms: 1.01x slower                                  |
| Geometric mean | (ref)                                                  | 1.02x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221015-linux-x86_64-python-main-3.12.0a1+-660f102 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.60 ms: 1.11x faster                                  |
| regex_compile  | 138 ms                                                 | 129 ms: 1.07x faster                                   |
| regex_dna      | 204 ms                                                 | 200 ms: 1.02x faster                                   |
| regex_v8       | 22.0 ms                                                | 22.2 ms: 1.01x slower                                  |
| Geometric mean | (ref)                                                  | 1.05x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221015-linux-x86_64-python-main-3.12.0a1+-660f102 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.60 ms: 1.31x faster                                  |
| unpickle_pure_python | 228 us                                                 | 202 us: 1.13x faster                                   |
| json_loads           | 26.5 us                                                | 23.9 us: 1.11x faster                                  |
| xml_etree_parse      | 158 ms                                                 | 145 ms: 1.09x faster                                   |
| unpickle             | 13.7 us                                                | 12.9 us: 1.06x faster                                  |
| pickle_pure_python   | 306 us                                                 | 293 us: 1.04x faster                                   |
| xml_etree_iterparse  | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| pickle_list          | 4.11 us                                                | 4.14 us: 1.01x slower                                  |
| xml_etree_generate   | 76.2 ms                                                | 76.9 ms: 1.01x slower                                  |
| unpickle_list        | 4.91 us                                                | 4.96 us: 1.01x slower                                  |
| pickle               | 10.1 us                                                | 10.3 us: 1.02x slower                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (2): xml_etree_process, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221015-linux-x86_64-python-main-3.12.0a1+-660f102 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.41 ms: 1.01x faster                                  |
| python_startup_no_site | 6.01 ms                                                | 6.09 ms: 1.01x slower                                  |
| Geometric mean         | (ref)                                                  | 1.00x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221015-linux-x86_64-python-main-3.12.0a1+-660f102 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                | 49.2 ms: 1.05x faster                                  |
| mako           | 10.1 ms                                                | 9.82 ms: 1.03x faster                                  |
| genshi_text    | 21.6 ms                                                | 21.0 ms: 1.03x faster                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221015-linux-x86_64-python-main-3.12.0a1+-660f102 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps              | 12.6 ms                                                | 9.60 ms: 1.31x faster                                  |
| scimark_sor             | 118 ms                                                 | 104 ms: 1.14x faster                                   |
| unpickle_pure_python    | 228 us                                                 | 202 us: 1.13x faster                                   |
| regex_effbot            | 3.99 ms                                                | 3.60 ms: 1.11x faster                                  |
| json_loads              | 26.5 us                                                | 23.9 us: 1.11x faster                                  |
| deltablue               | 3.67 ms                                                | 3.31 ms: 1.11x faster                                  |
| aiohttp                 | 1.10 ms                                                | 997 us: 1.10x faster                                   |
| gunicorn                | 1.18 ms                                                | 1.08 ms: 1.09x faster                                  |
| xml_etree_parse         | 158 ms                                                 | 145 ms: 1.09x faster                                   |
| html5lib                | 64.5 ms                                                | 59.2 ms: 1.09x faster                                  |
| logging_silent          | 101 ns                                                 | 92.9 ns: 1.09x faster                                  |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.16 ms: 1.08x faster                                  |
| pycparser               | 1.18 sec                                               | 1.10 sec: 1.08x faster                                 |
| float                   | 77.2 ms                                                | 72.2 ms: 1.07x faster                                  |
| regex_compile           | 138 ms                                                 | 129 ms: 1.07x faster                                   |
| deepcopy_memo           | 37.0 us                                                | 34.6 us: 1.07x faster                                  |
| richards                | 45.7 ms                                                | 43.0 ms: 1.06x faster                                  |
| pprint_pformat          | 1.46 sec                                               | 1.37 sec: 1.06x faster                                 |
| unpickle                | 13.7 us                                                | 12.9 us: 1.06x faster                                  |
| hexiom                  | 6.37 ms                                                | 6.05 ms: 1.05x faster                                  |
| fannkuch                | 388 ms                                                 | 368 ms: 1.05x faster                                   |
| logging_simple          | 6.03 us                                                | 5.73 us: 1.05x faster                                  |
| genshi_xml              | 51.8 ms                                                | 49.2 ms: 1.05x faster                                  |
| pprint_safe_repr        | 701 ms                                                 | 669 ms: 1.05x faster                                   |
| nqueens                 | 83.4 ms                                                | 79.5 ms: 1.05x faster                                  |
| logging_format          | 6.68 us                                                | 6.38 us: 1.05x faster                                  |
| chaos                   | 69.2 ms                                                | 66.1 ms: 1.05x faster                                  |
| sqlglot_transpile       | 1.70 ms                                                | 1.63 ms: 1.05x faster                                  |
| dulwich_log             | 63.7 ms                                                | 60.9 ms: 1.05x faster                                  |
| go                      | 140 ms                                                 | 134 ms: 1.05x faster                                   |
| sqlglot_parse           | 1.40 ms                                                | 1.34 ms: 1.04x faster                                  |
| pickle_pure_python      | 306 us                                                 | 293 us: 1.04x faster                                   |
| 2to3                    | 259 ms                                                 | 249 ms: 1.04x faster                                   |
| scimark_fft             | 328 ms                                                 | 315 ms: 1.04x faster                                   |
| pyflate                 | 418 ms                                                 | 402 ms: 1.04x faster                                   |
| raytrace                | 297 ms                                                 | 285 ms: 1.04x faster                                   |
| tornado_http            | 96.3 ms                                                | 92.6 ms: 1.04x faster                                  |
| coroutines              | 25.5 ms                                                | 24.6 ms: 1.04x faster                                  |
| sympy_expand            | 475 ms                                                 | 458 ms: 1.04x faster                                   |
| scimark_monte_carlo     | 68.1 ms                                                | 65.6 ms: 1.04x faster                                  |
| json                    | 4.94 ms                                                | 4.78 ms: 1.03x faster                                  |
| spectral_norm           | 100 ms                                                 | 96.7 ms: 1.03x faster                                  |
| sympy_str               | 290 ms                                                 | 281 ms: 1.03x faster                                   |
| sqlglot_optimize        | 53.1 ms                                                | 51.5 ms: 1.03x faster                                  |
| meteor_contest          | 107 ms                                                 | 103 ms: 1.03x faster                                   |
| deepcopy                | 342 us                                                 | 332 us: 1.03x faster                                   |
| mdp                     | 2.62 sec                                               | 2.54 sec: 1.03x faster                                 |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                  |
| pathlib                 | 18.2 ms                                                | 17.7 ms: 1.03x faster                                  |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                   |
| mako                    | 10.1 ms                                                | 9.82 ms: 1.03x faster                                  |
| genshi_text             | 21.6 ms                                                | 21.0 ms: 1.03x faster                                  |
| generators              | 73.5 ms                                                | 71.8 ms: 1.02x faster                                  |
| sympy_sum               | 167 ms                                                 | 163 ms: 1.02x faster                                   |
| thrift                  | 756 us                                                 | 742 us: 1.02x faster                                   |
| telco                   | 6.58 ms                                                | 6.46 ms: 1.02x faster                                  |
| regex_dna               | 204 ms                                                 | 200 ms: 1.02x faster                                   |
| coverage                | 100 ms                                                 | 98.4 ms: 1.02x faster                                  |
| scimark_lu              | 110 ms                                                 | 108 ms: 1.02x faster                                   |
| python_startup          | 8.52 ms                                                | 8.41 ms: 1.01x faster                                  |
| async_tree_cpu_io_mixed | 739 ms                                                 | 730 ms: 1.01x faster                                   |
| deepcopy_reduce         | 2.94 us                                                | 2.91 us: 1.01x faster                                  |
| xml_etree_iterparse     | 104 ms                                                 | 103 ms: 1.01x faster                                   |
| pidigits                | 198 ms                                                 | 199 ms: 1.01x slower                                   |
| pickle_list             | 4.11 us                                                | 4.14 us: 1.01x slower                                  |
| crypto_pyaes            | 74.7 ms                                                | 75.2 ms: 1.01x slower                                  |
| regex_v8                | 22.0 ms                                                | 22.2 ms: 1.01x slower                                  |
| xml_etree_generate      | 76.2 ms                                                | 76.9 ms: 1.01x slower                                  |
| unpickle_list           | 4.91 us                                                | 4.96 us: 1.01x slower                                  |
| nbody                   | 93.1 ms                                                | 94.2 ms: 1.01x slower                                  |
| async_tree_none         | 526 ms                                                 | 533 ms: 1.01x slower                                   |
| python_startup_no_site  | 6.01 ms                                                | 6.09 ms: 1.01x slower                                  |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                 |
| pickle                  | 10.1 us                                                | 10.3 us: 1.02x slower                                  |
| unpack_sequence         | 43.1 ns                                                | 44.1 ns: 1.02x slower                                  |
| async_tree_memoization  | 627 ms                                                 | 647 ms: 1.03x slower                                   |
| chameleon               | 6.47 ms                                                | 6.71 ms: 1.04x slower                                  |
| sqlite_synth            | 2.52 us                                                | 2.62 us: 1.04x slower                                  |
| Geometric mean          | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (4): pylint, xml_etree_process, pickle_dict, django_template
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: async_generators, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, create_gc_cycles, dask, djangocms, docutils, flaskblogging, gc_traversal, mypy2, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221015-3.12.0a1+-660f102/bm-20221015-linux-x86_64-python-main-3.12.0a1+-660f102.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
