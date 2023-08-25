
# Results vs. 3.11.0

- fork: brandtbucher
- ref: compressed_bytecode
- machine: linux-x86_64
- commit hash: bcd7980
- commit date: 2022-12-17
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.02x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 253 ms: 1.02x faster                                                        |
| chameleon      | 6.47 ms                                                | 6.43 ms: 1.01x faster                                                       |
| docutils       | 2.63 sec                                               | 2.49 sec: 1.05x faster                                                      |
| html5lib       | 64.5 ms                                                | 59.7 ms: 1.08x faster                                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 72.3 ms: 1.07x faster                                                       |
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                        |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                |

Benchmark hidden because not significant (1): nbody

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.58 ms: 1.12x faster                                                       |
| regex_compile  | 138 ms                                                 | 130 ms: 1.06x faster                                                        |
| regex_v8       | 22.0 ms                                                | 22.2 ms: 1.01x slower                                                       |
| regex_dna      | 204 ms                                                 | 219 ms: 1.07x slower                                                        |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.49 ms: 1.33x faster                                                       |
| unpickle_pure_python | 228 us                                                 | 199 us: 1.15x faster                                                        |
| json_loads           | 26.5 us                                                | 24.0 us: 1.10x faster                                                       |
| pickle_pure_python   | 306 us                                                 | 282 us: 1.08x faster                                                        |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.07x faster                                                        |
| unpickle             | 13.7 us                                                | 13.3 us: 1.03x faster                                                       |
| pickle_dict          | 31.1 us                                                | 30.6 us: 1.02x faster                                                       |
| xml_etree_iterparse  | 104 ms                                                 | 102 ms: 1.01x faster                                                        |
| xml_etree_process    | 53.9 ms                                                | 53.6 ms: 1.00x faster                                                       |
| xml_etree_generate   | 76.2 ms                                                | 77.2 ms: 1.01x slower                                                       |
| pickle               | 10.1 us                                                | 10.2 us: 1.02x slower                                                       |
| unpickle_list        | 4.91 us                                                | 5.12 us: 1.04x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.05x faster                                                                |

Benchmark hidden because not significant (1): pickle_list

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.50 ms: 1.00x faster                                                       |
| python_startup_no_site | 6.01 ms                                                | 6.08 ms: 1.01x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.00x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 47.0 ms: 1.10x faster                                                       |
| mako            | 10.1 ms                                                | 9.72 ms: 1.04x faster                                                       |
| genshi_text     | 21.6 ms                                                | 21.3 ms: 1.01x faster                                                       |
| django_template | 32.6 ms                                                | 32.9 ms: 1.01x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.03x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps              | 12.6 ms                                                | 9.49 ms: 1.33x faster                                                       |
| unpickle_pure_python    | 228 us                                                 | 199 us: 1.15x faster                                                        |
| deltablue               | 3.67 ms                                                | 3.22 ms: 1.14x faster                                                       |
| scimark_sor             | 118 ms                                                 | 105 ms: 1.12x faster                                                        |
| regex_effbot            | 3.99 ms                                                | 3.58 ms: 1.12x faster                                                       |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.03 ms: 1.11x faster                                                       |
| deepcopy_memo           | 37.0 us                                                | 33.5 us: 1.11x faster                                                       |
| json_loads              | 26.5 us                                                | 24.0 us: 1.10x faster                                                       |
| genshi_xml              | 51.8 ms                                                | 47.0 ms: 1.10x faster                                                       |
| richards                | 45.7 ms                                                | 41.6 ms: 1.10x faster                                                       |
| logging_silent          | 101 ns                                                 | 92.1 ns: 1.10x faster                                                       |
| pickle_pure_python      | 306 us                                                 | 282 us: 1.08x faster                                                        |
| html5lib                | 64.5 ms                                                | 59.7 ms: 1.08x faster                                                       |
| float                   | 77.2 ms                                                | 72.3 ms: 1.07x faster                                                       |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.07x faster                                                        |
| telco                   | 6.58 ms                                                | 6.17 ms: 1.07x faster                                                       |
| logging_format          | 6.68 us                                                | 6.28 us: 1.06x faster                                                       |
| nqueens                 | 83.4 ms                                                | 78.5 ms: 1.06x faster                                                       |
| regex_compile           | 138 ms                                                 | 130 ms: 1.06x faster                                                        |
| logging_simple          | 6.03 us                                                | 5.69 us: 1.06x faster                                                       |
| raytrace                | 297 ms                                                 | 280 ms: 1.06x faster                                                        |
| bench_thread_pool       | 819 us                                                 | 774 us: 1.06x faster                                                        |
| sympy_expand            | 475 ms                                                 | 449 ms: 1.06x faster                                                        |
| docutils                | 2.63 sec                                               | 2.49 sec: 1.05x faster                                                      |
| sqlglot_optimize        | 53.1 ms                                                | 50.5 ms: 1.05x faster                                                       |
| hexiom                  | 6.37 ms                                                | 6.08 ms: 1.05x faster                                                       |
| deepcopy                | 342 us                                                 | 326 us: 1.05x faster                                                        |
| pycparser               | 1.18 sec                                               | 1.13 sec: 1.05x faster                                                      |
| chaos                   | 69.2 ms                                                | 66.1 ms: 1.05x faster                                                       |
| pidigits                | 198 ms                                                 | 189 ms: 1.05x faster                                                        |
| pprint_pformat          | 1.46 sec                                               | 1.39 sec: 1.05x faster                                                      |
| fannkuch                | 388 ms                                                 | 372 ms: 1.04x faster                                                        |
| scimark_fft             | 328 ms                                                 | 315 ms: 1.04x faster                                                        |
| spectral_norm           | 100 ms                                                 | 96.1 ms: 1.04x faster                                                       |
| sympy_integrate         | 21.0 ms                                                | 20.2 ms: 1.04x faster                                                       |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                                        |
| go                      | 140 ms                                                 | 135 ms: 1.04x faster                                                        |
| async_generators        | 368 ms                                                 | 355 ms: 1.04x faster                                                        |
| mako                    | 10.1 ms                                                | 9.72 ms: 1.04x faster                                                       |
| unpack_sequence         | 43.1 ns                                                | 41.6 ns: 1.04x faster                                                       |
| pprint_safe_repr        | 701 ms                                                 | 677 ms: 1.04x faster                                                        |
| pathlib                 | 18.2 ms                                                | 17.6 ms: 1.04x faster                                                       |
| sympy_sum               | 167 ms                                                 | 161 ms: 1.03x faster                                                        |
| mdp                     | 2.62 sec                                               | 2.54 sec: 1.03x faster                                                      |
| scimark_lu              | 110 ms                                                 | 106 ms: 1.03x faster                                                        |
| json                    | 4.94 ms                                                | 4.80 ms: 1.03x faster                                                       |
| sympy_str               | 290 ms                                                 | 282 ms: 1.03x faster                                                        |
| scimark_monte_carlo     | 68.1 ms                                                | 66.1 ms: 1.03x faster                                                       |
| unpickle                | 13.7 us                                                | 13.3 us: 1.03x faster                                                       |
| pyflate                 | 418 ms                                                 | 407 ms: 1.03x faster                                                        |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.03x faster                                                        |
| dulwich_log             | 63.7 ms                                                | 62.0 ms: 1.03x faster                                                       |
| 2to3                    | 259 ms                                                 | 253 ms: 1.02x faster                                                        |
| coroutines              | 25.5 ms                                                | 25.0 ms: 1.02x faster                                                       |
| deepcopy_reduce         | 2.94 us                                                | 2.88 us: 1.02x faster                                                       |
| pickle_dict             | 31.1 us                                                | 30.6 us: 1.02x faster                                                       |
| thrift                  | 756 us                                                 | 745 us: 1.02x faster                                                        |
| xml_etree_iterparse     | 104 ms                                                 | 102 ms: 1.01x faster                                                        |
| genshi_text             | 21.6 ms                                                | 21.3 ms: 1.01x faster                                                       |
| sqlglot_transpile       | 1.70 ms                                                | 1.69 ms: 1.01x faster                                                       |
| crypto_pyaes            | 74.7 ms                                                | 74.1 ms: 1.01x faster                                                       |
| chameleon               | 6.47 ms                                                | 6.43 ms: 1.01x faster                                                       |
| xml_etree_process       | 53.9 ms                                                | 53.6 ms: 1.00x faster                                                       |
| sqlglot_parse           | 1.40 ms                                                | 1.39 ms: 1.00x faster                                                       |
| python_startup          | 8.52 ms                                                | 8.50 ms: 1.00x faster                                                       |
| regex_v8                | 22.0 ms                                                | 22.2 ms: 1.01x slower                                                       |
| django_template         | 32.6 ms                                                | 32.9 ms: 1.01x slower                                                       |
| async_tree_none         | 526 ms                                                 | 533 ms: 1.01x slower                                                        |
| xml_etree_generate      | 76.2 ms                                                | 77.2 ms: 1.01x slower                                                       |
| python_startup_no_site  | 6.01 ms                                                | 6.08 ms: 1.01x slower                                                       |
| sqlite_synth            | 2.52 us                                                | 2.56 us: 1.02x slower                                                       |
| pickle                  | 10.1 us                                                | 10.2 us: 1.02x slower                                                       |
| async_tree_io           | 1.30 sec                                               | 1.32 sec: 1.02x slower                                                      |
| async_tree_cpu_io_mixed | 739 ms                                                 | 765 ms: 1.03x slower                                                        |
| unpickle_list           | 4.91 us                                                | 5.12 us: 1.04x slower                                                       |
| generators              | 73.5 ms                                                | 77.6 ms: 1.06x slower                                                       |
| regex_dna               | 204 ms                                                 | 219 ms: 1.07x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                                |

Benchmark hidden because not significant (6): coverage, bench_mp_pool, pickle_list, nbody, djangocms, async_tree_memoization
Ignored benchmarks (17) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: aiohttp, asyncio_tcp, asyncio_tcp_ssl, comprehensions, create_gc_cycles, dask, flaskblogging, gc_traversal, gunicorn, mypy2, pylint, richards_super, sqlalchemy_declarative, sqlalchemy_imperative, tomli_loads, tornado_http, typing_runtime_protocols
Ignored benchmarks (1) of results/bm-20221217-3.12.0a3+-bcd7980/bm-20221217-linux-x86_64-brandtbucher-compressed_bytecode-3.12.0a3+-bcd7980.json: mypy


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.03x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.02x
