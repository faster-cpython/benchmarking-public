
# Results vs. 3.11.0

- fork: iritkatriel
- ref: stdlib_single_arg_ex
- machine: linux-x86_64
- commit hash: 23ae36b
- commit date: 2023-01-29
- overall geometric mean: 1.05x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 251 ms: 1.03x faster                                                        |
| chameleon      | 6.47 ms                                                | 6.36 ms: 1.02x faster                                                       |
| docutils       | 2.63 sec                                               | 2.48 sec: 1.06x faster                                                      |
| html5lib       | 64.5 ms                                                | 59.6 ms: 1.08x faster                                                       |
| tornado_http   | 96.3 ms                                                | 93.8 ms: 1.03x faster                                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 73.8 ms: 1.05x faster                                                       |
| pidigits       | 198 ms                                                 | 193 ms: 1.03x faster                                                        |
| nbody          | 93.1 ms                                                | 95.6 ms: 1.03x slower                                                       |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.38 ms: 1.18x faster                                                       |
| regex_compile  | 138 ms                                                 | 128 ms: 1.08x faster                                                        |
| regex_v8       | 22.0 ms                                                | 21.0 ms: 1.05x faster                                                       |
| regex_dna      | 204 ms                                                 | 202 ms: 1.01x faster                                                        |
| Geometric mean | (ref)                                                  | 1.08x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.36 ms: 1.34x faster                                                       |
| unpickle_pure_python | 228 us                                                 | 199 us: 1.15x faster                                                        |
| json_loads           | 26.5 us                                                | 24.0 us: 1.10x faster                                                       |
| pickle_pure_python   | 306 us                                                 | 283 us: 1.08x faster                                                        |
| xml_etree_parse      | 158 ms                                                 | 147 ms: 1.08x faster                                                        |
| unpickle             | 13.7 us                                                | 13.0 us: 1.05x faster                                                       |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.02x faster                                                        |
| xml_etree_process    | 53.9 ms                                                | 53.2 ms: 1.01x faster                                                       |
| pickle_dict          | 31.1 us                                                | 31.0 us: 1.01x faster                                                       |
| unpickle_list        | 4.91 us                                                | 4.94 us: 1.01x slower                                                       |
| xml_etree_generate   | 76.2 ms                                                | 77.1 ms: 1.01x slower                                                       |
| pickle               | 10.1 us                                                | 10.2 us: 1.01x slower                                                       |
| pickle_list          | 4.11 us                                                | 4.22 us: 1.03x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.06x faster                                                                |

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.93 ms: 1.05x slower                                                       |
| python_startup_no_site | 6.01 ms                                                | 6.46 ms: 1.08x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 47.5 ms: 1.09x faster                                                       |
| genshi_text     | 21.6 ms                                                | 20.3 ms: 1.06x faster                                                       |
| mako            | 10.1 ms                                                | 9.85 ms: 1.02x faster                                                       |
| django_template | 32.6 ms                                                | 32.3 ms: 1.01x faster                                                       |
| Geometric mean  | (ref)                                                  | 1.05x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| asyncio_tcp             | 922 ms                                                 | 495 ms: 1.86x faster                                                        |
| json_dumps              | 12.6 ms                                                | 9.36 ms: 1.34x faster                                                       |
| regex_effbot            | 3.99 ms                                                | 3.38 ms: 1.18x faster                                                       |
| deltablue               | 3.67 ms                                                | 3.20 ms: 1.15x faster                                                       |
| unpickle_pure_python    | 228 us                                                 | 199 us: 1.15x faster                                                        |
| logging_silent          | 101 ns                                                 | 90.0 ns: 1.12x faster                                                       |
| scimark_sor             | 118 ms                                                 | 106 ms: 1.11x faster                                                        |
| aiohttp                 | 1.10 ms                                                | 992 us: 1.11x faster                                                        |
| gunicorn                | 1.18 ms                                                | 1.06 ms: 1.11x faster                                                       |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.06 ms: 1.11x faster                                                       |
| json_loads              | 26.5 us                                                | 24.0 us: 1.10x faster                                                       |
| richards                | 45.7 ms                                                | 41.9 ms: 1.09x faster                                                       |
| genshi_xml              | 51.8 ms                                                | 47.5 ms: 1.09x faster                                                       |
| pycparser               | 1.18 sec                                               | 1.08 sec: 1.09x faster                                                      |
| hexiom                  | 6.37 ms                                                | 5.86 ms: 1.09x faster                                                       |
| deepcopy_memo           | 37.0 us                                                | 34.1 us: 1.09x faster                                                       |
| fannkuch                | 388 ms                                                 | 358 ms: 1.08x faster                                                        |
| html5lib                | 64.5 ms                                                | 59.6 ms: 1.08x faster                                                       |
| regex_compile           | 138 ms                                                 | 128 ms: 1.08x faster                                                        |
| pickle_pure_python      | 306 us                                                 | 283 us: 1.08x faster                                                        |
| xml_etree_parse         | 158 ms                                                 | 147 ms: 1.08x faster                                                        |
| json                    | 4.94 ms                                                | 4.58 ms: 1.08x faster                                                       |
| sympy_str               | 290 ms                                                 | 269 ms: 1.08x faster                                                        |
| scimark_fft             | 328 ms                                                 | 305 ms: 1.08x faster                                                        |
| bench_thread_pool       | 819 us                                                 | 761 us: 1.08x faster                                                        |
| chaos                   | 69.2 ms                                                | 64.5 ms: 1.07x faster                                                       |
| sympy_sum               | 167 ms                                                 | 156 ms: 1.07x faster                                                        |
| pprint_pformat          | 1.46 sec                                               | 1.36 sec: 1.07x faster                                                      |
| genshi_text             | 21.6 ms                                                | 20.3 ms: 1.06x faster                                                       |
| sympy_integrate         | 21.0 ms                                                | 19.7 ms: 1.06x faster                                                       |
| raytrace                | 297 ms                                                 | 280 ms: 1.06x faster                                                        |
| spectral_norm           | 100 ms                                                 | 94.4 ms: 1.06x faster                                                       |
| logging_format          | 6.68 us                                                | 6.31 us: 1.06x faster                                                       |
| docutils                | 2.63 sec                                               | 2.48 sec: 1.06x faster                                                      |
| logging_simple          | 6.03 us                                                | 5.72 us: 1.05x faster                                                       |
| nqueens                 | 83.4 ms                                                | 79.1 ms: 1.05x faster                                                       |
| sympy_expand            | 475 ms                                                 | 451 ms: 1.05x faster                                                        |
| async_generators        | 368 ms                                                 | 350 ms: 1.05x faster                                                        |
| unpickle                | 13.7 us                                                | 13.0 us: 1.05x faster                                                       |
| regex_v8                | 22.0 ms                                                | 21.0 ms: 1.05x faster                                                       |
| go                      | 140 ms                                                 | 133 ms: 1.05x faster                                                        |
| pprint_safe_repr        | 701 ms                                                 | 670 ms: 1.05x faster                                                        |
| sqlglot_optimize        | 53.1 ms                                                | 50.7 ms: 1.05x faster                                                       |
| float                   | 77.2 ms                                                | 73.8 ms: 1.05x faster                                                       |
| deepcopy                | 342 us                                                 | 327 us: 1.04x faster                                                        |
| telco                   | 6.58 ms                                                | 6.38 ms: 1.03x faster                                                       |
| pyflate                 | 418 ms                                                 | 406 ms: 1.03x faster                                                        |
| scimark_lu              | 110 ms                                                 | 107 ms: 1.03x faster                                                        |
| 2to3                    | 259 ms                                                 | 251 ms: 1.03x faster                                                        |
| scimark_monte_carlo     | 68.1 ms                                                | 66.1 ms: 1.03x faster                                                       |
| pidigits                | 198 ms                                                 | 193 ms: 1.03x faster                                                        |
| tornado_http            | 96.3 ms                                                | 93.8 ms: 1.03x faster                                                       |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                        |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.03x faster                                                        |
| dulwich_log             | 63.7 ms                                                | 62.1 ms: 1.02x faster                                                       |
| coroutines              | 25.5 ms                                                | 24.9 ms: 1.02x faster                                                       |
| mako                    | 10.1 ms                                                | 9.85 ms: 1.02x faster                                                       |
| chameleon               | 6.47 ms                                                | 6.36 ms: 1.02x faster                                                       |
| mdp                     | 2.62 sec                                               | 2.57 sec: 1.02x faster                                                      |
| coverage                | 100 ms                                                 | 98.3 ms: 1.02x faster                                                       |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.02x faster                                                        |
| thrift                  | 756 us                                                 | 745 us: 1.01x faster                                                        |
| unpack_sequence         | 43.1 ns                                                | 42.5 ns: 1.01x faster                                                       |
| pathlib                 | 18.2 ms                                                | 18.0 ms: 1.01x faster                                                       |
| xml_etree_process       | 53.9 ms                                                | 53.2 ms: 1.01x faster                                                       |
| regex_dna               | 204 ms                                                 | 202 ms: 1.01x faster                                                        |
| create_gc_cycles        | 1.49 ms                                                | 1.47 ms: 1.01x faster                                                       |
| sqlglot_transpile       | 1.70 ms                                                | 1.69 ms: 1.01x faster                                                       |
| crypto_pyaes            | 74.7 ms                                                | 74.0 ms: 1.01x faster                                                       |
| django_template         | 32.6 ms                                                | 32.3 ms: 1.01x faster                                                       |
| pickle_dict             | 31.1 us                                                | 31.0 us: 1.01x faster                                                       |
| async_tree_io           | 1.30 sec                                               | 1.31 sec: 1.01x slower                                                      |
| unpickle_list           | 4.91 us                                                | 4.94 us: 1.01x slower                                                       |
| xml_etree_generate      | 76.2 ms                                                | 77.1 ms: 1.01x slower                                                       |
| pickle                  | 10.1 us                                                | 10.2 us: 1.01x slower                                                       |
| async_tree_cpu_io_mixed | 739 ms                                                 | 755 ms: 1.02x slower                                                        |
| pickle_list             | 4.11 us                                                | 4.22 us: 1.03x slower                                                       |
| nbody                   | 93.1 ms                                                | 95.6 ms: 1.03x slower                                                       |
| sqlite_synth            | 2.52 us                                                | 2.62 us: 1.04x slower                                                       |
| generators              | 73.5 ms                                                | 76.9 ms: 1.05x slower                                                       |
| python_startup          | 8.52 ms                                                | 8.93 ms: 1.05x slower                                                       |
| gc_traversal            | 4.02 ms                                                | 4.29 ms: 1.07x slower                                                       |
| python_startup_no_site  | 6.01 ms                                                | 6.46 ms: 1.08x slower                                                       |
| dask                    | 360 ms                                                 | 492 ms: 1.37x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.05x faster                                                                |

Benchmark hidden because not significant (6): djangocms, async_tree_none, bench_mp_pool, sqlglot_parse, deepcopy_reduce, async_tree_memoization
Ignored benchmarks (10) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, comprehensions, flaskblogging, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20230129-3.12.0a4+-23ae36b/bm-20230129-linux-x86_64-iritkatriel-stdlib_single_arg_ex-3.12.0a4+-23ae36b.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
