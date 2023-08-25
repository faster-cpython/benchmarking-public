
# Results vs. 3.11.0

- fork: faster-cpython
- ref: no_local_eval_breake
- machine: linux-x86_64
- commit hash: f8eb171
- commit date: 2023-03-23
- overall geometric mean: 1.04x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.01x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 254 ms: 1.02x faster                                                             |
| chameleon      | 6.47 ms                                                | 6.44 ms: 1.01x faster                                                            |
| docutils       | 2.63 sec                                               | 2.54 sec: 1.03x faster                                                           |
| html5lib       | 64.5 ms                                                | 62.5 ms: 1.03x faster                                                            |
| tornado_http   | 96.3 ms                                                | 91.1 ms: 1.06x faster                                                            |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 87.6 ms: 1.06x faster                                                            |
| pidigits       | 198 ms                                                 | 188 ms: 1.05x faster                                                             |
| float          | 77.2 ms                                                | 75.2 ms: 1.03x faster                                                            |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.50 ms: 1.14x faster                                                            |
| regex_compile  | 138 ms                                                 | 135 ms: 1.02x faster                                                             |
| regex_v8       | 22.0 ms                                                | 21.9 ms: 1.01x faster                                                            |
| regex_dna      | 204 ms                                                 | 207 ms: 1.02x slower                                                             |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.61 ms: 1.31x faster                                                            |
| unpickle_pure_python | 228 us                                                 | 203 us: 1.12x faster                                                             |
| json_loads           | 26.5 us                                                | 24.1 us: 1.10x faster                                                            |
| xml_etree_parse      | 158 ms                                                 | 149 ms: 1.06x faster                                                             |
| pickle_pure_python   | 306 us                                                 | 288 us: 1.06x faster                                                             |
| xml_etree_iterparse  | 104 ms                                                 | 100 ms: 1.04x faster                                                             |
| unpickle_list        | 4.91 us                                                | 5.00 us: 1.02x slower                                                            |
| pickle_list          | 4.11 us                                                | 4.21 us: 1.02x slower                                                            |
| pickle               | 10.1 us                                                | 10.3 us: 1.02x slower                                                            |
| xml_etree_process    | 53.9 ms                                                | 56.5 ms: 1.05x slower                                                            |
| xml_etree_generate   | 76.2 ms                                                | 81.8 ms: 1.07x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                     |

Benchmark hidden because not significant (2): unpickle, pickle_dict

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.84 ms: 1.04x slower                                                            |
| python_startup_no_site | 6.01 ms                                                | 6.53 ms: 1.09x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 48.2 ms: 1.07x faster                                                            |
| mako            | 10.1 ms                                                | 9.95 ms: 1.01x faster                                                            |
| django_template | 32.6 ms                                                | 33.6 ms: 1.03x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.01x faster                                                                     |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230323-linux-x86_64-faster%2dcpython-no_local_eval_breake-3.12.0a6+-f8eb171 |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.3 ms: 2.51x faster                                                            |
| asyncio_tcp             | 922 ms                                                 | 506 ms: 1.82x faster                                                             |
| json_dumps              | 12.6 ms                                                | 9.61 ms: 1.31x faster                                                            |
| mypy2                   | 420 ms                                                 | 334 ms: 1.26x faster                                                             |
| regex_effbot            | 3.99 ms                                                | 3.50 ms: 1.14x faster                                                            |
| deltablue               | 3.67 ms                                                | 3.26 ms: 1.13x faster                                                            |
| unpickle_pure_python    | 228 us                                                 | 203 us: 1.12x faster                                                             |
| coroutines              | 25.5 ms                                                | 23.1 ms: 1.11x faster                                                            |
| json_loads              | 26.5 us                                                | 24.1 us: 1.10x faster                                                            |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                                            |
| spectral_norm           | 100 ms                                                 | 92.1 ms: 1.09x faster                                                            |
| gunicorn                | 1.18 ms                                                | 1.09 ms: 1.08x faster                                                            |
| genshi_xml              | 51.8 ms                                                | 48.2 ms: 1.07x faster                                                            |
| scimark_fft             | 328 ms                                                 | 307 ms: 1.07x faster                                                             |
| json                    | 4.94 ms                                                | 4.63 ms: 1.07x faster                                                            |
| xml_etree_parse         | 158 ms                                                 | 149 ms: 1.06x faster                                                             |
| deepcopy_memo           | 37.0 us                                                | 34.8 us: 1.06x faster                                                            |
| nbody                   | 93.1 ms                                                | 87.6 ms: 1.06x faster                                                            |
| pickle_pure_python      | 306 us                                                 | 288 us: 1.06x faster                                                             |
| logging_format          | 6.68 us                                                | 6.30 us: 1.06x faster                                                            |
| logging_simple          | 6.03 us                                                | 5.71 us: 1.06x faster                                                            |
| tornado_http            | 96.3 ms                                                | 91.1 ms: 1.06x faster                                                            |
| scimark_sor             | 118 ms                                                 | 112 ms: 1.05x faster                                                             |
| pycparser               | 1.18 sec                                               | 1.12 sec: 1.05x faster                                                           |
| gc_traversal            | 4.02 ms                                                | 3.82 ms: 1.05x faster                                                            |
| pidigits                | 198 ms                                                 | 188 ms: 1.05x faster                                                             |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.28 ms: 1.05x faster                                                            |
| chaos                   | 69.2 ms                                                | 66.1 ms: 1.05x faster                                                            |
| fannkuch                | 388 ms                                                 | 370 ms: 1.05x faster                                                             |
| raytrace                | 297 ms                                                 | 285 ms: 1.04x faster                                                             |
| hexiom                  | 6.37 ms                                                | 6.14 ms: 1.04x faster                                                            |
| mdp                     | 2.62 sec                                               | 2.52 sec: 1.04x faster                                                           |
| pprint_pformat          | 1.46 sec                                               | 1.40 sec: 1.04x faster                                                           |
| xml_etree_iterparse     | 104 ms                                                 | 100 ms: 1.04x faster                                                             |
| bench_thread_pool       | 819 us                                                 | 791 us: 1.04x faster                                                             |
| nqueens                 | 83.4 ms                                                | 80.6 ms: 1.03x faster                                                            |
| docutils                | 2.63 sec                                               | 2.54 sec: 1.03x faster                                                           |
| html5lib                | 64.5 ms                                                | 62.5 ms: 1.03x faster                                                            |
| sympy_expand            | 475 ms                                                 | 460 ms: 1.03x faster                                                             |
| sqlglot_optimize        | 53.1 ms                                                | 51.5 ms: 1.03x faster                                                            |
| telco                   | 6.58 ms                                                | 6.39 ms: 1.03x faster                                                            |
| logging_silent          | 101 ns                                                 | 98.2 ns: 1.03x faster                                                            |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.03x faster                                                             |
| deepcopy                | 342 us                                                 | 333 us: 1.03x faster                                                             |
| pprint_safe_repr        | 701 ms                                                 | 683 ms: 1.03x faster                                                             |
| float                   | 77.2 ms                                                | 75.2 ms: 1.03x faster                                                            |
| coverage                | 100 ms                                                 | 97.5 ms: 1.03x faster                                                            |
| go                      | 140 ms                                                 | 137 ms: 1.02x faster                                                             |
| richards                | 45.7 ms                                                | 44.7 ms: 1.02x faster                                                            |
| regex_compile           | 138 ms                                                 | 135 ms: 1.02x faster                                                             |
| sympy_integrate         | 21.0 ms                                                | 20.5 ms: 1.02x faster                                                            |
| 2to3                    | 259 ms                                                 | 254 ms: 1.02x faster                                                             |
| sympy_str               | 290 ms                                                 | 285 ms: 1.02x faster                                                             |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.01x faster                                                             |
| scimark_monte_carlo     | 68.1 ms                                                | 67.1 ms: 1.01x faster                                                            |
| mako                    | 10.1 ms                                                | 9.95 ms: 1.01x faster                                                            |
| regex_v8                | 22.0 ms                                                | 21.9 ms: 1.01x faster                                                            |
| pathlib                 | 18.2 ms                                                | 18.1 ms: 1.01x faster                                                            |
| dulwich_log             | 63.7 ms                                                | 63.3 ms: 1.01x faster                                                            |
| chameleon               | 6.47 ms                                                | 6.44 ms: 1.01x faster                                                            |
| sympy_sum               | 167 ms                                                 | 166 ms: 1.01x faster                                                             |
| pyflate                 | 418 ms                                                 | 423 ms: 1.01x slower                                                             |
| sqlglot_transpile       | 1.70 ms                                                | 1.72 ms: 1.01x slower                                                            |
| regex_dna               | 204 ms                                                 | 207 ms: 1.02x slower                                                             |
| unpickle_list           | 4.91 us                                                | 5.00 us: 1.02x slower                                                            |
| sqlglot_parse           | 1.40 ms                                                | 1.43 ms: 1.02x slower                                                            |
| pickle_list             | 4.11 us                                                | 4.21 us: 1.02x slower                                                            |
| pickle                  | 10.1 us                                                | 10.3 us: 1.02x slower                                                            |
| deepcopy_reduce         | 2.94 us                                                | 3.02 us: 1.03x slower                                                            |
| django_template         | 32.6 ms                                                | 33.6 ms: 1.03x slower                                                            |
| sqlite_synth            | 2.52 us                                                | 2.61 us: 1.04x slower                                                            |
| python_startup          | 8.52 ms                                                | 8.84 ms: 1.04x slower                                                            |
| thrift                  | 756 us                                                 | 786 us: 1.04x slower                                                             |
| async_tree_memoization  | 627 ms                                                 | 656 ms: 1.05x slower                                                             |
| comprehensions          | 22.4 us                                                | 23.5 us: 1.05x slower                                                            |
| xml_etree_process       | 53.9 ms                                                | 56.5 ms: 1.05x slower                                                            |
| xml_etree_generate      | 76.2 ms                                                | 81.8 ms: 1.07x slower                                                            |
| unpack_sequence         | 43.1 ns                                                | 46.5 ns: 1.08x slower                                                            |
| python_startup_no_site  | 6.01 ms                                                | 6.53 ms: 1.09x slower                                                            |
| async_generators        | 368 ms                                                 | 407 ms: 1.10x slower                                                             |
| dask                    | 360 ms                                                 | 512 ms: 1.42x slower                                                             |
| Geometric mean          | (ref)                                                  | 1.04x faster                                                                     |

Benchmark hidden because not significant (13): djangocms, sqlalchemy_imperative, sqlalchemy_declarative, async_tree_none, unpickle, pickle_dict, create_gc_cycles, bench_mp_pool, crypto_pyaes, async_tree_io, genshi_text, async_tree_cpu_io_mixed, scimark_lu
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.01x
