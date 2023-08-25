
# Results vs. 3.11.0

- fork: python
- ref: main
- machine: linux-x86_64
- commit hash: 5055300
- commit date: 2022-10-19
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221019-linux-x86_64-python-main-3.12.0a1+-5055300 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 249 ms: 1.04x faster                                   |
| html5lib       | 64.5 ms                                                | 60.2 ms: 1.07x faster                                  |
| tornado_http   | 96.3 ms                                                | 93.0 ms: 1.04x faster                                  |
| Geometric mean | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221019-linux-x86_64-python-main-3.12.0a1+-5055300 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| float          | 77.2 ms                                                | 71.1 ms: 1.09x faster                                  |
| pidigits       | 198 ms                                                 | 193 ms: 1.03x faster                                   |
| nbody          | 93.1 ms                                                | 94.8 ms: 1.02x slower                                  |
| Geometric mean | (ref)                                                  | 1.03x faster                                           |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221019-linux-x86_64-python-main-3.12.0a1+-5055300 |
|----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.40 ms: 1.17x faster                                  |
| regex_compile  | 138 ms                                                 | 128 ms: 1.08x faster                                   |
| regex_v8       | 22.0 ms                                                | 21.4 ms: 1.03x faster                                  |
| regex_dna      | 204 ms                                                 | 205 ms: 1.01x slower                                   |
| Geometric mean | (ref)                                                  | 1.07x faster                                           |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221019-linux-x86_64-python-main-3.12.0a1+-5055300 |
|----------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.42 ms: 1.34x faster                                  |
| unpickle_pure_python | 228 us                                                 | 202 us: 1.13x faster                                   |
| json_loads           | 26.5 us                                                | 24.0 us: 1.10x faster                                  |
| xml_etree_parse      | 158 ms                                                 | 144 ms: 1.10x faster                                   |
| pickle_pure_python   | 306 us                                                 | 285 us: 1.07x faster                                   |
| pickle_list          | 4.11 us                                                | 3.99 us: 1.03x faster                                  |
| xml_etree_process    | 53.9 ms                                                | 53.3 ms: 1.01x faster                                  |
| xml_etree_generate   | 76.2 ms                                                | 76.9 ms: 1.01x slower                                  |
| xml_etree_iterparse  | 104 ms                                                 | 106 ms: 1.02x slower                                   |
| pickle               | 10.1 us                                                | 10.3 us: 1.02x slower                                  |
| unpickle_list        | 4.91 us                                                | 5.02 us: 1.02x slower                                  |
| Geometric mean       | (ref)                                                  | 1.05x faster                                           |

Benchmark hidden because not significant (2): unpickle, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221019-linux-x86_64-python-main-3.12.0a1+-5055300 |
|------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.32 ms: 1.02x faster                                  |
| python_startup_no_site | 6.01 ms                                                | 6.03 ms: 1.00x slower                                  |
| Geometric mean         | (ref)                                                  | 1.01x faster                                           |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221019-linux-x86_64-python-main-3.12.0a1+-5055300 |
|-----------------|:------------------------------------------------------:|:------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 49.3 ms: 1.05x faster                                  |
| mako            | 10.1 ms                                                | 9.79 ms: 1.03x faster                                  |
| genshi_text     | 21.6 ms                                                | 20.9 ms: 1.03x faster                                  |
| django_template | 32.6 ms                                                | 32.7 ms: 1.00x slower                                  |
| Geometric mean  | (ref)                                                  | 1.03x faster                                           |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221019-linux-x86_64-python-main-3.12.0a1+-5055300 |
|-------------------------|:------------------------------------------------------:|:------------------------------------------------------:|
| json_dumps              | 12.6 ms                                                | 9.42 ms: 1.34x faster                                  |
| regex_effbot            | 3.99 ms                                                | 3.40 ms: 1.17x faster                                  |
| scimark_sor             | 118 ms                                                 | 104 ms: 1.14x faster                                   |
| unpickle_pure_python    | 228 us                                                 | 202 us: 1.13x faster                                   |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.04 ms: 1.11x faster                                  |
| json_loads              | 26.5 us                                                | 24.0 us: 1.10x faster                                  |
| aiohttp                 | 1.10 ms                                                | 1.00 ms: 1.10x faster                                  |
| xml_etree_parse         | 158 ms                                                 | 144 ms: 1.10x faster                                   |
| gunicorn                | 1.18 ms                                                | 1.08 ms: 1.09x faster                                  |
| deltablue               | 3.67 ms                                                | 3.36 ms: 1.09x faster                                  |
| pycparser               | 1.18 sec                                               | 1.08 sec: 1.09x faster                                 |
| float                   | 77.2 ms                                                | 71.1 ms: 1.09x faster                                  |
| logging_silent          | 101 ns                                                 | 93.3 ns: 1.08x faster                                  |
| regex_compile           | 138 ms                                                 | 128 ms: 1.08x faster                                   |
| pickle_pure_python      | 306 us                                                 | 285 us: 1.07x faster                                   |
| deepcopy_memo           | 37.0 us                                                | 34.5 us: 1.07x faster                                  |
| html5lib                | 64.5 ms                                                | 60.2 ms: 1.07x faster                                  |
| fannkuch                | 388 ms                                                 | 363 ms: 1.07x faster                                   |
| pprint_pformat          | 1.46 sec                                               | 1.37 sec: 1.06x faster                                 |
| sqlglot_parse           | 1.40 ms                                                | 1.33 ms: 1.06x faster                                  |
| scimark_fft             | 328 ms                                                 | 311 ms: 1.06x faster                                   |
| genshi_xml              | 51.8 ms                                                | 49.3 ms: 1.05x faster                                  |
| meteor_contest          | 107 ms                                                 | 102 ms: 1.05x faster                                   |
| pprint_safe_repr        | 701 ms                                                 | 669 ms: 1.05x faster                                   |
| spectral_norm           | 100 ms                                                 | 95.4 ms: 1.05x faster                                  |
| sqlglot_transpile       | 1.70 ms                                                | 1.63 ms: 1.05x faster                                  |
| hexiom                  | 6.37 ms                                                | 6.11 ms: 1.04x faster                                  |
| sympy_expand            | 475 ms                                                 | 456 ms: 1.04x faster                                   |
| sqlglot_optimize        | 53.1 ms                                                | 51.0 ms: 1.04x faster                                  |
| 2to3                    | 259 ms                                                 | 249 ms: 1.04x faster                                   |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                   |
| dulwich_log             | 63.7 ms                                                | 61.2 ms: 1.04x faster                                  |
| coroutines              | 25.5 ms                                                | 24.5 ms: 1.04x faster                                  |
| pathlib                 | 18.2 ms                                                | 17.6 ms: 1.04x faster                                  |
| json                    | 4.94 ms                                                | 4.77 ms: 1.04x faster                                  |
| sympy_str               | 290 ms                                                 | 280 ms: 1.04x faster                                   |
| logging_simple          | 6.03 us                                                | 5.83 us: 1.04x faster                                  |
| tornado_http            | 96.3 ms                                                | 93.0 ms: 1.04x faster                                  |
| sympy_integrate         | 21.0 ms                                                | 20.3 ms: 1.03x faster                                  |
| nqueens                 | 83.4 ms                                                | 80.9 ms: 1.03x faster                                  |
| logging_format          | 6.68 us                                                | 6.49 us: 1.03x faster                                  |
| pickle_list             | 4.11 us                                                | 3.99 us: 1.03x faster                                  |
| regex_v8                | 22.0 ms                                                | 21.4 ms: 1.03x faster                                  |
| mako                    | 10.1 ms                                                | 9.79 ms: 1.03x faster                                  |
| genshi_text             | 21.6 ms                                                | 20.9 ms: 1.03x faster                                  |
| generators              | 73.5 ms                                                | 71.4 ms: 1.03x faster                                  |
| go                      | 140 ms                                                 | 136 ms: 1.03x faster                                   |
| deepcopy                | 342 us                                                 | 333 us: 1.03x faster                                   |
| pidigits                | 198 ms                                                 | 193 ms: 1.03x faster                                   |
| raytrace                | 297 ms                                                 | 289 ms: 1.03x faster                                   |
| pylint                  | 465 ms                                                 | 454 ms: 1.03x faster                                   |
| python_startup          | 8.52 ms                                                | 8.32 ms: 1.02x faster                                  |
| coverage                | 100 ms                                                 | 97.7 ms: 1.02x faster                                  |
| telco                   | 6.58 ms                                                | 6.43 ms: 1.02x faster                                  |
| sympy_sum               | 167 ms                                                 | 163 ms: 1.02x faster                                   |
| pyflate                 | 418 ms                                                 | 409 ms: 1.02x faster                                   |
| scimark_lu              | 110 ms                                                 | 108 ms: 1.02x faster                                   |
| chaos                   | 69.2 ms                                                | 67.8 ms: 1.02x faster                                  |
| thrift                  | 756 us                                                 | 742 us: 1.02x faster                                   |
| deepcopy_reduce         | 2.94 us                                                | 2.89 us: 1.02x faster                                  |
| scimark_monte_carlo     | 68.1 ms                                                | 67.0 ms: 1.02x faster                                  |
| richards                | 45.7 ms                                                | 45.2 ms: 1.01x faster                                  |
| xml_etree_process       | 53.9 ms                                                | 53.3 ms: 1.01x faster                                  |
| async_tree_cpu_io_mixed | 739 ms                                                 | 732 ms: 1.01x faster                                   |
| python_startup_no_site  | 6.01 ms                                                | 6.03 ms: 1.00x slower                                  |
| django_template         | 32.6 ms                                                | 32.7 ms: 1.00x slower                                  |
| regex_dna               | 204 ms                                                 | 205 ms: 1.01x slower                                   |
| xml_etree_generate      | 76.2 ms                                                | 76.9 ms: 1.01x slower                                  |
| crypto_pyaes            | 74.7 ms                                                | 75.4 ms: 1.01x slower                                  |
| async_tree_io           | 1.30 sec                                               | 1.31 sec: 1.01x slower                                 |
| nbody                   | 93.1 ms                                                | 94.8 ms: 1.02x slower                                  |
| xml_etree_iterparse     | 104 ms                                                 | 106 ms: 1.02x slower                                   |
| pickle                  | 10.1 us                                                | 10.3 us: 1.02x slower                                  |
| unpickle_list           | 4.91 us                                                | 5.02 us: 1.02x slower                                  |
| mdp                     | 2.62 sec                                               | 2.69 sec: 1.03x slower                                 |
| sqlite_synth            | 2.52 us                                                | 2.60 us: 1.03x slower                                  |
| async_tree_memoization  | 627 ms                                                 | 657 ms: 1.05x slower                                   |
| unpack_sequence         | 43.1 ns                                                | 45.7 ns: 1.06x slower                                  |
| Geometric mean          | (ref)                                                  | 1.04x faster                                           |

Benchmark hidden because not significant (4): unpickle, chameleon, async_tree_none, pickle_dict
Ignored benchmarks (18) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: async_generators, asyncio_tcp, asyncio_tcp_ssl, bench_mp_pool, bench_thread_pool, comprehensions, create_gc_cycles, dask, djangocms, docutils, flaskblogging, gc_traversal, mypy2, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221019-3.12.0a1+-5055300/bm-20221019-linux-x86_64-python-main-3.12.0a1+-5055300.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
