
# Results vs. 3.11.0

- fork: iritkatriel
- ref: remove_JUMP_IF_FALSE
- machine: linux-x86_64
- commit hash: b2bf829
- commit date: 2023-03-22
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230322-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-b2bf829 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 248 ms: 1.04x faster                                                        |
| chameleon      | 6.47 ms                                                | 6.39 ms: 1.01x faster                                                       |
| docutils       | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                      |
| html5lib       | 64.5 ms                                                | 60.8 ms: 1.06x faster                                                       |
| tornado_http   | 96.3 ms                                                | 91.3 ms: 1.05x faster                                                       |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230322-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-b2bf829 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 87.1 ms: 1.07x faster                                                       |
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                        |
| float          | 77.2 ms                                                | 74.1 ms: 1.04x faster                                                       |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230322-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-b2bf829 |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.43 ms: 1.16x faster                                                       |
| regex_compile  | 138 ms                                                 | 133 ms: 1.04x faster                                                        |
| regex_v8       | 22.0 ms                                                | 21.8 ms: 1.01x faster                                                       |
| regex_dna      | 204 ms                                                 | 203 ms: 1.00x faster                                                        |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230322-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-b2bf829 |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.46 ms: 1.33x faster                                                       |
| unpickle_pure_python | 228 us                                                 | 198 us: 1.15x faster                                                        |
| json_loads           | 26.5 us                                                | 23.9 us: 1.11x faster                                                       |
| pickle_pure_python   | 306 us                                                 | 285 us: 1.07x faster                                                        |
| xml_etree_parse      | 158 ms                                                 | 153 ms: 1.04x faster                                                        |
| pickle               | 10.1 us                                                | 10.2 us: 1.01x slower                                                       |
| unpickle_list        | 4.91 us                                                | 4.99 us: 1.02x slower                                                       |
| pickle_dict          | 31.1 us                                                | 31.9 us: 1.03x slower                                                       |
| xml_etree_process    | 53.9 ms                                                | 56.1 ms: 1.04x slower                                                       |
| xml_etree_generate   | 76.2 ms                                                | 80.7 ms: 1.06x slower                                                       |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                |

Benchmark hidden because not significant (3): xml_etree_iterparse, pickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230322-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-b2bf829 |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.81 ms: 1.03x slower                                                       |
| python_startup_no_site | 6.01 ms                                                | 6.51 ms: 1.08x slower                                                       |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230322-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-b2bf829 |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 47.4 ms: 1.09x faster                                                       |
| mako            | 10.1 ms                                                | 9.94 ms: 1.02x faster                                                       |
| genshi_text     | 21.6 ms                                                | 21.7 ms: 1.01x slower                                                       |
| django_template | 32.6 ms                                                | 33.4 ms: 1.02x slower                                                       |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                                |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230322-linux-x86_64-iritkatriel-remove_JUMP_IF_FALSE-3.12.0a6+-b2bf829 |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.0 ms: 2.53x faster                                                       |
| asyncio_tcp             | 922 ms                                                 | 506 ms: 1.82x faster                                                        |
| json_dumps              | 12.6 ms                                                | 9.46 ms: 1.33x faster                                                       |
| mypy2                   | 420 ms                                                 | 333 ms: 1.26x faster                                                        |
| regex_effbot            | 3.99 ms                                                | 3.43 ms: 1.16x faster                                                       |
| unpickle_pure_python    | 228 us                                                 | 198 us: 1.15x faster                                                        |
| coroutines              | 25.5 ms                                                | 22.3 ms: 1.14x faster                                                       |
| deltablue               | 3.67 ms                                                | 3.21 ms: 1.14x faster                                                       |
| scimark_sor             | 118 ms                                                 | 106 ms: 1.12x faster                                                        |
| spectral_norm           | 100 ms                                                 | 89.6 ms: 1.12x faster                                                       |
| scimark_fft             | 328 ms                                                 | 296 ms: 1.11x faster                                                        |
| json_loads              | 26.5 us                                                | 23.9 us: 1.11x faster                                                       |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.08 ms: 1.10x faster                                                       |
| deepcopy_memo           | 37.0 us                                                | 33.7 us: 1.10x faster                                                       |
| genshi_xml              | 51.8 ms                                                | 47.4 ms: 1.09x faster                                                       |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                                       |
| json                    | 4.94 ms                                                | 4.54 ms: 1.09x faster                                                       |
| gunicorn                | 1.18 ms                                                | 1.09 ms: 1.08x faster                                                       |
| pickle_pure_python      | 306 us                                                 | 285 us: 1.07x faster                                                        |
| nbody                   | 93.1 ms                                                | 87.1 ms: 1.07x faster                                                       |
| html5lib                | 64.5 ms                                                | 60.8 ms: 1.06x faster                                                       |
| chaos                   | 69.2 ms                                                | 65.4 ms: 1.06x faster                                                       |
| tornado_http            | 96.3 ms                                                | 91.3 ms: 1.05x faster                                                       |
| pycparser               | 1.18 sec                                               | 1.12 sec: 1.05x faster                                                      |
| scimark_monte_carlo     | 68.1 ms                                                | 64.7 ms: 1.05x faster                                                       |
| deepcopy                | 342 us                                                 | 326 us: 1.05x faster                                                        |
| logging_silent          | 101 ns                                                 | 96.6 ns: 1.05x faster                                                       |
| pidigits                | 198 ms                                                 | 189 ms: 1.05x faster                                                        |
| raytrace                | 297 ms                                                 | 284 ms: 1.04x faster                                                        |
| coverage                | 100 ms                                                 | 95.9 ms: 1.04x faster                                                       |
| 2to3                    | 259 ms                                                 | 248 ms: 1.04x faster                                                        |
| logging_format          | 6.68 us                                                | 6.41 us: 1.04x faster                                                       |
| float                   | 77.2 ms                                                | 74.1 ms: 1.04x faster                                                       |
| hexiom                  | 6.37 ms                                                | 6.11 ms: 1.04x faster                                                       |
| fannkuch                | 388 ms                                                 | 372 ms: 1.04x faster                                                        |
| richards                | 45.7 ms                                                | 43.9 ms: 1.04x faster                                                       |
| go                      | 140 ms                                                 | 134 ms: 1.04x faster                                                        |
| docutils                | 2.63 sec                                               | 2.53 sec: 1.04x faster                                                      |
| regex_compile           | 138 ms                                                 | 133 ms: 1.04x faster                                                        |
| bench_thread_pool       | 819 us                                                 | 790 us: 1.04x faster                                                        |
| xml_etree_parse         | 158 ms                                                 | 153 ms: 1.04x faster                                                        |
| sympy_expand            | 475 ms                                                 | 459 ms: 1.03x faster                                                        |
| sqlglot_optimize        | 53.1 ms                                                | 51.4 ms: 1.03x faster                                                       |
| nqueens                 | 83.4 ms                                                | 80.9 ms: 1.03x faster                                                       |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.03x faster                                                        |
| logging_simple          | 6.03 us                                                | 5.87 us: 1.03x faster                                                       |
| unpack_sequence         | 43.1 ns                                                | 42.0 ns: 1.03x faster                                                       |
| sympy_integrate         | 21.0 ms                                                | 20.4 ms: 1.03x faster                                                       |
| pyflate                 | 418 ms                                                 | 407 ms: 1.03x faster                                                        |
| mdp                     | 2.62 sec                                               | 2.55 sec: 1.03x faster                                                      |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.03x faster                                                        |
| sympy_str               | 290 ms                                                 | 283 ms: 1.03x faster                                                        |
| pathlib                 | 18.2 ms                                                | 17.8 ms: 1.02x faster                                                       |
| pprint_pformat          | 1.46 sec                                               | 1.43 sec: 1.02x faster                                                      |
| sqlalchemy_imperative   | 17.9 ms                                                | 17.6 ms: 1.02x faster                                                       |
| mako                    | 10.1 ms                                                | 9.94 ms: 1.02x faster                                                       |
| scimark_lu              | 110 ms                                                 | 108 ms: 1.01x faster                                                        |
| chameleon               | 6.47 ms                                                | 6.39 ms: 1.01x faster                                                       |
| gc_traversal            | 4.02 ms                                                | 3.98 ms: 1.01x faster                                                       |
| regex_v8                | 22.0 ms                                                | 21.8 ms: 1.01x faster                                                       |
| pprint_safe_repr        | 701 ms                                                 | 695 ms: 1.01x faster                                                        |
| deepcopy_reduce         | 2.94 us                                                | 2.92 us: 1.01x faster                                                       |
| crypto_pyaes            | 74.7 ms                                                | 74.1 ms: 1.01x faster                                                       |
| sympy_sum               | 167 ms                                                 | 165 ms: 1.01x faster                                                        |
| dulwich_log             | 63.7 ms                                                | 63.3 ms: 1.01x faster                                                       |
| regex_dna               | 204 ms                                                 | 203 ms: 1.00x faster                                                        |
| genshi_text             | 21.6 ms                                                | 21.7 ms: 1.01x slower                                                       |
| pickle                  | 10.1 us                                                | 10.2 us: 1.01x slower                                                       |
| unpickle_list           | 4.91 us                                                | 4.99 us: 1.02x slower                                                       |
| django_template         | 32.6 ms                                                | 33.4 ms: 1.02x slower                                                       |
| sqlglot_transpile       | 1.70 ms                                                | 1.75 ms: 1.03x slower                                                       |
| pickle_dict             | 31.1 us                                                | 31.9 us: 1.03x slower                                                       |
| sqlite_synth            | 2.52 us                                                | 2.59 us: 1.03x slower                                                       |
| thrift                  | 756 us                                                 | 780 us: 1.03x slower                                                        |
| python_startup          | 8.52 ms                                                | 8.81 ms: 1.03x slower                                                       |
| sqlglot_parse           | 1.40 ms                                                | 1.45 ms: 1.04x slower                                                       |
| async_tree_memoization  | 627 ms                                                 | 653 ms: 1.04x slower                                                        |
| xml_etree_process       | 53.9 ms                                                | 56.1 ms: 1.04x slower                                                       |
| comprehensions          | 22.4 us                                                | 23.7 us: 1.06x slower                                                       |
| xml_etree_generate      | 76.2 ms                                                | 80.7 ms: 1.06x slower                                                       |
| python_startup_no_site  | 6.01 ms                                                | 6.51 ms: 1.08x slower                                                       |
| async_generators        | 368 ms                                                 | 413 ms: 1.12x slower                                                        |
| dask                    | 360 ms                                                 | 503 ms: 1.40x slower                                                        |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                                |

Benchmark hidden because not significant (11): async_tree_none, djangocms, xml_etree_iterparse, bench_mp_pool, pickle_list, async_tree_io, create_gc_cycles, telco, async_tree_cpu_io_mixed, sqlalchemy_declarative, unpickle
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.02x
- 99% likely to have a speedup of 1.01x
