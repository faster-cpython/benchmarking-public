
# Results vs. 3.11.0

- fork: brandtbucher
- ref: de_epfreeze
- machine: linux-x86_64
- commit hash: 034e2bf
- commit date: 2023-03-16
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230316-linux-x86_64-brandtbucher-de_epfreeze-3.12.0a6+-034e2bf |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 253 ms: 1.02x faster                                                |
| chameleon      | 6.47 ms                                                | 6.43 ms: 1.01x faster                                               |
| docutils       | 2.63 sec                                               | 2.53 sec: 1.04x faster                                              |
| html5lib       | 64.5 ms                                                | 59.6 ms: 1.08x faster                                               |
| tornado_http   | 96.3 ms                                                | 91.7 ms: 1.05x faster                                               |
| Geometric mean | (ref)                                                  | 1.04x faster                                                        |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230316-linux-x86_64-brandtbucher-de_epfreeze-3.12.0a6+-034e2bf |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| float          | 77.2 ms                                                | 73.6 ms: 1.05x faster                                               |
| pidigits       | 198 ms                                                 | 189 ms: 1.05x faster                                                |
| nbody          | 93.1 ms                                                | 89.3 ms: 1.04x faster                                               |
| Geometric mean | (ref)                                                  | 1.05x faster                                                        |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230316-linux-x86_64-brandtbucher-de_epfreeze-3.12.0a6+-034e2bf |
|----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.42 ms: 1.17x faster                                               |
| regex_compile  | 138 ms                                                 | 135 ms: 1.02x faster                                                |
| regex_dna      | 204 ms                                                 | 203 ms: 1.00x faster                                                |
| regex_v8       | 22.0 ms                                                | 25.6 ms: 1.16x slower                                               |
| Geometric mean | (ref)                                                  | 1.01x faster                                                        |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230316-linux-x86_64-brandtbucher-de_epfreeze-3.12.0a6+-034e2bf |
|----------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.41 ms: 1.34x faster                                               |
| unpickle_pure_python | 228 us                                                 | 199 us: 1.14x faster                                                |
| json_loads           | 26.5 us                                                | 24.4 us: 1.09x faster                                               |
| pickle_pure_python   | 306 us                                                 | 282 us: 1.08x faster                                                |
| xml_etree_parse      | 158 ms                                                 | 147 ms: 1.08x faster                                                |
| xml_etree_iterparse  | 104 ms                                                 | 100 ms: 1.04x faster                                                |
| pickle_dict          | 31.1 us                                                | 30.8 us: 1.01x faster                                               |
| pickle_list          | 4.11 us                                                | 4.16 us: 1.01x slower                                               |
| pickle               | 10.1 us                                                | 10.2 us: 1.01x slower                                               |
| xml_etree_process    | 53.9 ms                                                | 56.3 ms: 1.05x slower                                               |
| unpickle_list        | 4.91 us                                                | 5.19 us: 1.06x slower                                               |
| xml_etree_generate   | 76.2 ms                                                | 81.7 ms: 1.07x slower                                               |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230316-linux-x86_64-brandtbucher-de_epfreeze-3.12.0a6+-034e2bf |
|------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| python_startup_no_site | 6.01 ms                                                | 6.47 ms: 1.08x slower                                               |
| python_startup         | 8.52 ms                                                | 9.50 ms: 1.11x slower                                               |
| Geometric mean         | (ref)                                                  | 1.10x slower                                                        |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230316-linux-x86_64-brandtbucher-de_epfreeze-3.12.0a6+-034e2bf |
|-----------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 48.4 ms: 1.07x faster                                               |
| genshi_text     | 21.6 ms                                                | 21.7 ms: 1.01x slower                                               |
| mako            | 10.1 ms                                                | 10.2 ms: 1.01x slower                                               |
| django_template | 32.6 ms                                                | 33.2 ms: 1.02x slower                                               |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                        |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230316-linux-x86_64-brandtbucher-de_epfreeze-3.12.0a6+-034e2bf |
|-------------------------|:------------------------------------------------------:|:-------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 30.1 ms: 2.44x faster                                               |
| asyncio_tcp             | 922 ms                                                 | 508 ms: 1.81x faster                                                |
| json_dumps              | 12.6 ms                                                | 9.41 ms: 1.34x faster                                               |
| regex_effbot            | 3.99 ms                                                | 3.42 ms: 1.17x faster                                               |
| deltablue               | 3.67 ms                                                | 3.16 ms: 1.16x faster                                               |
| coroutines              | 25.5 ms                                                | 22.0 ms: 1.16x faster                                               |
| unpickle_pure_python    | 228 us                                                 | 199 us: 1.14x faster                                                |
| gc_traversal            | 4.02 ms                                                | 3.55 ms: 1.13x faster                                               |
| scimark_sor             | 118 ms                                                 | 106 ms: 1.11x faster                                                |
| spectral_norm           | 100 ms                                                 | 90.3 ms: 1.11x faster                                               |
| coverage                | 100 ms                                                 | 90.3 ms: 1.11x faster                                               |
| aiohttp                 | 1.10 ms                                                | 1.00 ms: 1.10x faster                                               |
| mdp                     | 2.62 sec                                               | 2.39 sec: 1.09x faster                                              |
| json_loads              | 26.5 us                                                | 24.4 us: 1.09x faster                                               |
| pickle_pure_python      | 306 us                                                 | 282 us: 1.08x faster                                                |
| gunicorn                | 1.18 ms                                                | 1.09 ms: 1.08x faster                                               |
| html5lib                | 64.5 ms                                                | 59.6 ms: 1.08x faster                                               |
| deepcopy_memo           | 37.0 us                                                | 34.2 us: 1.08x faster                                               |
| xml_etree_parse         | 158 ms                                                 | 147 ms: 1.08x faster                                                |
| scimark_fft             | 328 ms                                                 | 306 ms: 1.07x faster                                                |
| genshi_xml              | 51.8 ms                                                | 48.4 ms: 1.07x faster                                               |
| json                    | 4.94 ms                                                | 4.69 ms: 1.05x faster                                               |
| logging_silent          | 101 ns                                                 | 96.1 ns: 1.05x faster                                               |
| float                   | 77.2 ms                                                | 73.6 ms: 1.05x faster                                               |
| tornado_http            | 96.3 ms                                                | 91.7 ms: 1.05x faster                                               |
| raytrace                | 297 ms                                                 | 284 ms: 1.05x faster                                                |
| pidigits                | 198 ms                                                 | 189 ms: 1.05x faster                                                |
| hexiom                  | 6.37 ms                                                | 6.10 ms: 1.05x faster                                               |
| nbody                   | 93.1 ms                                                | 89.3 ms: 1.04x faster                                               |
| richards                | 45.7 ms                                                | 43.9 ms: 1.04x faster                                               |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                              |
| xml_etree_iterparse     | 104 ms                                                 | 100 ms: 1.04x faster                                                |
| docutils                | 2.63 sec                                               | 2.53 sec: 1.04x faster                                              |
| deepcopy                | 342 us                                                 | 332 us: 1.03x faster                                                |
| async_tree_memoization  | 627 ms                                                 | 609 ms: 1.03x faster                                                |
| chaos                   | 69.2 ms                                                | 67.2 ms: 1.03x faster                                               |
| fannkuch                | 388 ms                                                 | 377 ms: 1.03x faster                                                |
| bench_thread_pool       | 819 us                                                 | 796 us: 1.03x faster                                                |
| pathlib                 | 18.2 ms                                                | 17.7 ms: 1.03x faster                                               |
| sqlglot_optimize        | 53.1 ms                                                | 51.7 ms: 1.03x faster                                               |
| logging_simple          | 6.03 us                                                | 5.88 us: 1.03x faster                                               |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.39 ms: 1.03x faster                                               |
| scimark_lu              | 110 ms                                                 | 107 ms: 1.03x faster                                                |
| regex_compile           | 138 ms                                                 | 135 ms: 1.02x faster                                                |
| pprint_safe_repr        | 701 ms                                                 | 685 ms: 1.02x faster                                                |
| go                      | 140 ms                                                 | 137 ms: 1.02x faster                                                |
| sympy_integrate         | 21.0 ms                                                | 20.5 ms: 1.02x faster                                               |
| sqlglot_normalize       | 108 ms                                                 | 105 ms: 1.02x faster                                                |
| 2to3                    | 259 ms                                                 | 253 ms: 1.02x faster                                                |
| logging_format          | 6.68 us                                                | 6.54 us: 1.02x faster                                               |
| sqlalchemy_declarative  | 138 ms                                                 | 135 ms: 1.02x faster                                                |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.02x faster                                                |
| sqlalchemy_imperative   | 17.9 ms                                                | 17.6 ms: 1.02x faster                                               |
| scimark_monte_carlo     | 68.1 ms                                                | 66.8 ms: 1.02x faster                                               |
| sympy_expand            | 475 ms                                                 | 467 ms: 1.02x faster                                                |
| dulwich_log             | 63.7 ms                                                | 62.6 ms: 1.02x faster                                               |
| sympy_str               | 290 ms                                                 | 285 ms: 1.02x faster                                                |
| unpack_sequence         | 43.1 ns                                                | 42.4 ns: 1.02x faster                                               |
| nqueens                 | 83.4 ms                                                | 82.3 ms: 1.01x faster                                               |
| pickle_dict             | 31.1 us                                                | 30.8 us: 1.01x faster                                               |
| crypto_pyaes            | 74.7 ms                                                | 74.2 ms: 1.01x faster                                               |
| chameleon               | 6.47 ms                                                | 6.43 ms: 1.01x faster                                               |
| regex_dna               | 204 ms                                                 | 203 ms: 1.00x faster                                                |
| genshi_text             | 21.6 ms                                                | 21.7 ms: 1.01x slower                                               |
| pickle_list             | 4.11 us                                                | 4.16 us: 1.01x slower                                               |
| deepcopy_reduce         | 2.94 us                                                | 2.97 us: 1.01x slower                                               |
| pyflate                 | 418 ms                                                 | 423 ms: 1.01x slower                                                |
| mako                    | 10.1 ms                                                | 10.2 ms: 1.01x slower                                               |
| pickle                  | 10.1 us                                                | 10.2 us: 1.01x slower                                               |
| django_template         | 32.6 ms                                                | 33.2 ms: 1.02x slower                                               |
| sqlglot_transpile       | 1.70 ms                                                | 1.73 ms: 1.02x slower                                               |
| thrift                  | 756 us                                                 | 774 us: 1.02x slower                                                |
| async_tree_none         | 526 ms                                                 | 539 ms: 1.02x slower                                                |
| sqlglot_parse           | 1.40 ms                                                | 1.44 ms: 1.03x slower                                               |
| xml_etree_process       | 53.9 ms                                                | 56.3 ms: 1.05x slower                                               |
| sqlite_synth            | 2.52 us                                                | 2.64 us: 1.05x slower                                               |
| unpickle_list           | 4.91 us                                                | 5.19 us: 1.06x slower                                               |
| async_tree_cpu_io_mixed | 739 ms                                                 | 782 ms: 1.06x slower                                                |
| comprehensions          | 22.4 us                                                | 23.9 us: 1.07x slower                                               |
| xml_etree_generate      | 76.2 ms                                                | 81.7 ms: 1.07x slower                                               |
| python_startup_no_site  | 6.01 ms                                                | 6.47 ms: 1.08x slower                                               |
| python_startup          | 8.52 ms                                                | 9.50 ms: 1.11x slower                                               |
| async_generators        | 368 ms                                                 | 416 ms: 1.13x slower                                                |
| regex_v8                | 22.0 ms                                                | 25.6 ms: 1.16x slower                                               |
| dask                    | 360 ms                                                 | 511 ms: 1.42x slower                                                |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                        |

Benchmark hidden because not significant (9): pycparser, djangocms, sympy_sum, telco, bench_mp_pool, unpickle, create_gc_cycles, async_tree_io, mypy2
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.02x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x
