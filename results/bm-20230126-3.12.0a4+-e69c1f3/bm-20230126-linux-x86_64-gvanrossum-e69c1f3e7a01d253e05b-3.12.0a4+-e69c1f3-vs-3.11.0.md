
# Results vs. 3.11.0

- fork: gvanrossum
- ref: e69c1f3e7a01d253e05b
- machine: linux-x86_64
- commit hash: e69c1f3
- commit date: 2023-01-26
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 250 ms: 1.04x faster                                                       |
| chameleon      | 6.47 ms                                                | 6.38 ms: 1.01x faster                                                      |
| docutils       | 2.63 sec                                               | 2.50 sec: 1.05x faster                                                     |
| html5lib       | 64.5 ms                                                | 59.7 ms: 1.08x faster                                                      |
| tornado_http   | 96.3 ms                                                | 94.1 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.04x faster                                                               |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 71.8 ms: 1.08x faster                                                      |
| pidigits       | 198 ms                                                 | 193 ms: 1.03x faster                                                       |
| nbody          | 93.1 ms                                                | 95.4 ms: 1.02x slower                                                      |
| Geometric mean | (ref)                                                  | 1.03x faster                                                               |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.54 ms: 1.13x faster                                                      |
| regex_compile  | 138 ms                                                 | 127 ms: 1.09x faster                                                       |
| regex_v8       | 22.0 ms                                                | 21.2 ms: 1.04x faster                                                      |
| regex_dna      | 204 ms                                                 | 208 ms: 1.02x slower                                                       |
| Geometric mean | (ref)                                                  | 1.06x faster                                                               |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.40 ms: 1.34x faster                                                      |
| unpickle_pure_python | 228 us                                                 | 196 us: 1.17x faster                                                       |
| json_loads           | 26.5 us                                                | 24.0 us: 1.11x faster                                                      |
| xml_etree_parse      | 158 ms                                                 | 147 ms: 1.08x faster                                                       |
| pickle_pure_python   | 306 us                                                 | 286 us: 1.07x faster                                                       |
| unpickle             | 13.7 us                                                | 13.0 us: 1.05x faster                                                      |
| pickle_list          | 4.11 us                                                | 3.96 us: 1.04x faster                                                      |
| pickle_dict          | 31.1 us                                                | 30.4 us: 1.02x faster                                                      |
| unpickle_list        | 4.91 us                                                | 5.01 us: 1.02x slower                                                      |
| xml_etree_generate   | 76.2 ms                                                | 78.3 ms: 1.03x slower                                                      |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                               |

Benchmark hidden because not significant (3): xml_etree_iterparse, pickle, xml_etree_process

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.90 ms: 1.04x slower                                                      |
| python_startup_no_site | 6.01 ms                                                | 6.44 ms: 1.07x slower                                                      |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                               |

Benchmarks with tag 'template':
===============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| genshi_xml     | 51.8 ms                                                | 47.3 ms: 1.09x faster                                                      |
| mako           | 10.1 ms                                                | 9.70 ms: 1.04x faster                                                      |
| genshi_text    | 21.6 ms                                                | 21.2 ms: 1.02x faster                                                      |
| Geometric mean | (ref)                                                  | 1.04x faster                                                               |

Benchmark hidden because not significant (1): django_template

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 501 ms: 1.84x faster                                                       |
| json_dumps              | 12.6 ms                                                | 9.40 ms: 1.34x faster                                                      |
| unpickle_pure_python    | 228 us                                                 | 196 us: 1.17x faster                                                       |
| deltablue               | 3.67 ms                                                | 3.22 ms: 1.14x faster                                                      |
| scimark_sparse_mat_mult | 4.50 ms                                                | 3.95 ms: 1.14x faster                                                      |
| regex_effbot            | 3.99 ms                                                | 3.54 ms: 1.13x faster                                                      |
| scimark_sor             | 118 ms                                                 | 106 ms: 1.11x faster                                                       |
| aiohttp                 | 1.10 ms                                                | 993 us: 1.11x faster                                                       |
| gc_traversal            | 4.02 ms                                                | 3.63 ms: 1.11x faster                                                      |
| gunicorn                | 1.18 ms                                                | 1.06 ms: 1.11x faster                                                      |
| json_loads              | 26.5 us                                                | 24.0 us: 1.11x faster                                                      |
| richards                | 45.7 ms                                                | 41.7 ms: 1.10x faster                                                      |
| genshi_xml              | 51.8 ms                                                | 47.3 ms: 1.09x faster                                                      |
| logging_silent          | 101 ns                                                 | 92.5 ns: 1.09x faster                                                      |
| regex_compile           | 138 ms                                                 | 127 ms: 1.09x faster                                                       |
| html5lib                | 64.5 ms                                                | 59.7 ms: 1.08x faster                                                      |
| chaos                   | 69.2 ms                                                | 64.0 ms: 1.08x faster                                                      |
| deepcopy_memo           | 37.0 us                                                | 34.3 us: 1.08x faster                                                      |
| sympy_str               | 290 ms                                                 | 269 ms: 1.08x faster                                                       |
| xml_etree_parse         | 158 ms                                                 | 147 ms: 1.08x faster                                                       |
| sympy_sum               | 167 ms                                                 | 155 ms: 1.08x faster                                                       |
| float                   | 77.2 ms                                                | 71.8 ms: 1.08x faster                                                      |
| pycparser               | 1.18 sec                                               | 1.10 sec: 1.07x faster                                                     |
| pickle_pure_python      | 306 us                                                 | 286 us: 1.07x faster                                                       |
| json                    | 4.94 ms                                                | 4.63 ms: 1.07x faster                                                      |
| pprint_pformat          | 1.46 sec                                               | 1.37 sec: 1.07x faster                                                     |
| scimark_fft             | 328 ms                                                 | 308 ms: 1.07x faster                                                       |
| hexiom                  | 6.37 ms                                                | 5.99 ms: 1.06x faster                                                      |
| sympy_integrate         | 21.0 ms                                                | 19.7 ms: 1.06x faster                                                      |
| nqueens                 | 83.4 ms                                                | 78.5 ms: 1.06x faster                                                      |
| logging_format          | 6.68 us                                                | 6.31 us: 1.06x faster                                                      |
| fannkuch                | 388 ms                                                 | 367 ms: 1.06x faster                                                       |
| logging_simple          | 6.03 us                                                | 5.71 us: 1.06x faster                                                      |
| unpickle                | 13.7 us                                                | 13.0 us: 1.05x faster                                                      |
| sympy_expand            | 475 ms                                                 | 451 ms: 1.05x faster                                                       |
| pprint_safe_repr        | 701 ms                                                 | 667 ms: 1.05x faster                                                       |
| docutils                | 2.63 sec                                               | 2.50 sec: 1.05x faster                                                     |
| bench_thread_pool       | 819 us                                                 | 779 us: 1.05x faster                                                       |
| async_generators        | 368 ms                                                 | 351 ms: 1.05x faster                                                       |
| pyflate                 | 418 ms                                                 | 399 ms: 1.05x faster                                                       |
| sqlglot_optimize        | 53.1 ms                                                | 50.7 ms: 1.05x faster                                                      |
| telco                   | 6.58 ms                                                | 6.30 ms: 1.05x faster                                                      |
| deepcopy                | 342 us                                                 | 327 us: 1.04x faster                                                       |
| scimark_monte_carlo     | 68.1 ms                                                | 65.2 ms: 1.04x faster                                                      |
| raytrace                | 297 ms                                                 | 284 ms: 1.04x faster                                                       |
| coverage                | 100 ms                                                 | 96.1 ms: 1.04x faster                                                      |
| mako                    | 10.1 ms                                                | 9.70 ms: 1.04x faster                                                      |
| pickle_list             | 4.11 us                                                | 3.96 us: 1.04x faster                                                      |
| regex_v8                | 22.0 ms                                                | 21.2 ms: 1.04x faster                                                      |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                                       |
| crypto_pyaes            | 74.7 ms                                                | 72.1 ms: 1.04x faster                                                      |
| 2to3                    | 259 ms                                                 | 250 ms: 1.04x faster                                                       |
| create_gc_cycles        | 1.49 ms                                                | 1.44 ms: 1.03x faster                                                      |
| pidigits                | 198 ms                                                 | 193 ms: 1.03x faster                                                       |
| unpack_sequence         | 43.1 ns                                                | 41.9 ns: 1.03x faster                                                      |
| go                      | 140 ms                                                 | 136 ms: 1.03x faster                                                       |
| mdp                     | 2.62 sec                                               | 2.55 sec: 1.03x faster                                                     |
| dulwich_log             | 63.7 ms                                                | 62.1 ms: 1.03x faster                                                      |
| pathlib                 | 18.2 ms                                                | 17.8 ms: 1.02x faster                                                      |
| pickle_dict             | 31.1 us                                                | 30.4 us: 1.02x faster                                                      |
| tornado_http            | 96.3 ms                                                | 94.1 ms: 1.02x faster                                                      |
| genshi_text             | 21.6 ms                                                | 21.2 ms: 1.02x faster                                                      |
| meteor_contest          | 107 ms                                                 | 105 ms: 1.02x faster                                                       |
| scimark_lu              | 110 ms                                                 | 108 ms: 1.02x faster                                                       |
| chameleon               | 6.47 ms                                                | 6.38 ms: 1.01x faster                                                      |
| thrift                  | 756 us                                                 | 746 us: 1.01x faster                                                       |
| coroutines              | 25.5 ms                                                | 25.2 ms: 1.01x faster                                                      |
| sqlglot_parse           | 1.40 ms                                                | 1.42 ms: 1.01x slower                                                      |
| regex_dna               | 204 ms                                                 | 208 ms: 1.02x slower                                                       |
| unpickle_list           | 4.91 us                                                | 5.01 us: 1.02x slower                                                      |
| deepcopy_reduce         | 2.94 us                                                | 3.00 us: 1.02x slower                                                      |
| generators              | 73.5 ms                                                | 75.1 ms: 1.02x slower                                                      |
| async_tree_cpu_io_mixed | 739 ms                                                 | 756 ms: 1.02x slower                                                       |
| nbody                   | 93.1 ms                                                | 95.4 ms: 1.02x slower                                                      |
| xml_etree_generate      | 76.2 ms                                                | 78.3 ms: 1.03x slower                                                      |
| sqlite_synth            | 2.52 us                                                | 2.61 us: 1.03x slower                                                      |
| python_startup          | 8.52 ms                                                | 8.90 ms: 1.04x slower                                                      |
| python_startup_no_site  | 6.01 ms                                                | 6.44 ms: 1.07x slower                                                      |
| dask                    | 360 ms                                                 | 496 ms: 1.38x slower                                                       |
| Geometric mean          | (ref)                                                  | 1.05x faster                                                               |

Benchmark hidden because not significant (11): spectral_norm, async_tree_none, xml_etree_iterparse, pickle, async_tree_memoization, django_template, bench_mp_pool, sqlglot_transpile, xml_etree_process, async_tree_io, djangocms
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230126-3.12.0a4+-e69c1f3/bm-20230126-linux-x86_64-gvanrossum-e69c1f3e7a01d253e05b-3.12.0a4+-e69c1f3.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.03x
- 99% likely to have a speedup of 1.02x
