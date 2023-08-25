
# Results vs. 3.11.0

- fork: faster-cpython
- ref: allow_non_python_fra
- machine: linux-x86_64
- commit hash: 3e2c3ab
- commit date: 2023-03-15
- overall geometric mean: 1.03x faster \*
- HPT reliability: 100.00%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230315-linux-x86_64-faster%2dcpython-allow_non_python_fra-3.12.0a6+-3e2c3ab |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 252 ms: 1.03x faster                                                             |
| chameleon      | 6.47 ms                                                | 6.42 ms: 1.01x faster                                                            |
| docutils       | 2.63 sec                                               | 2.55 sec: 1.03x faster                                                           |
| html5lib       | 64.5 ms                                                | 62.1 ms: 1.04x faster                                                            |
| tornado_http   | 96.3 ms                                                | 95.2 ms: 1.01x faster                                                            |
| Geometric mean | (ref)                                                  | 1.02x faster                                                                     |

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230315-linux-x86_64-faster%2dcpython-allow_non_python_fra-3.12.0a6+-3e2c3ab |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| pidigits       | 198 ms                                                 | 190 ms: 1.04x faster                                                             |
| float          | 77.2 ms                                                | 75.2 ms: 1.03x faster                                                            |
| nbody          | 93.1 ms                                                | 95.6 ms: 1.03x slower                                                            |
| Geometric mean | (ref)                                                  | 1.01x faster                                                                     |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230315-linux-x86_64-faster%2dcpython-allow_non_python_fra-3.12.0a6+-3e2c3ab |
|----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.36 ms: 1.19x faster                                                            |
| regex_compile  | 138 ms                                                 | 134 ms: 1.03x faster                                                             |
| regex_v8       | 22.0 ms                                                | 21.8 ms: 1.01x faster                                                            |
| regex_dna      | 204 ms                                                 | 203 ms: 1.00x faster                                                             |
| Geometric mean | (ref)                                                  | 1.06x faster                                                                     |

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230315-linux-x86_64-faster%2dcpython-allow_non_python_fra-3.12.0a6+-3e2c3ab |
|----------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.55 ms: 1.32x faster                                                            |
| unpickle_pure_python | 228 us                                                 | 201 us: 1.13x faster                                                             |
| json_loads           | 26.5 us                                                | 24.4 us: 1.08x faster                                                            |
| xml_etree_parse      | 158 ms                                                 | 148 ms: 1.07x faster                                                             |
| pickle_pure_python   | 306 us                                                 | 286 us: 1.07x faster                                                             |
| xml_etree_iterparse  | 104 ms                                                 | 99.4 ms: 1.04x faster                                                            |
| pickle               | 10.1 us                                                | 10.2 us: 1.01x slower                                                            |
| xml_etree_process    | 53.9 ms                                                | 55.2 ms: 1.03x slower                                                            |
| unpickle_list        | 4.91 us                                                | 5.05 us: 1.03x slower                                                            |
| xml_etree_generate   | 76.2 ms                                                | 81.0 ms: 1.06x slower                                                            |
| Geometric mean       | (ref)                                                  | 1.04x faster                                                                     |

Benchmark hidden because not significant (3): pickle_dict, pickle_list, unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230315-linux-x86_64-faster%2dcpython-allow_non_python_fra-3.12.0a6+-3e2c3ab |
|------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 9.02 ms: 1.06x slower                                                            |
| python_startup_no_site | 6.01 ms                                                | 6.54 ms: 1.09x slower                                                            |
| Geometric mean         | (ref)                                                  | 1.07x slower                                                                     |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230315-linux-x86_64-faster%2dcpython-allow_non_python_fra-3.12.0a6+-3e2c3ab |
|-----------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 47.7 ms: 1.09x faster                                                            |
| mako            | 10.1 ms                                                | 10.0 ms: 1.01x faster                                                            |
| django_template | 32.6 ms                                                | 33.5 ms: 1.03x slower                                                            |
| Geometric mean  | (ref)                                                  | 1.02x faster                                                                     |

Benchmark hidden because not significant (1): genshi_text

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230315-linux-x86_64-faster%2dcpython-allow_non_python_fra-3.12.0a6+-3e2c3ab |
|-------------------------|:------------------------------------------------------:|:--------------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.3 ms: 2.51x faster                                                            |
| asyncio_tcp             | 922 ms                                                 | 515 ms: 1.79x faster                                                             |
| json_dumps              | 12.6 ms                                                | 9.55 ms: 1.32x faster                                                            |
| mypy2                   | 420 ms                                                 | 335 ms: 1.25x faster                                                             |
| regex_effbot            | 3.99 ms                                                | 3.36 ms: 1.19x faster                                                            |
| deltablue               | 3.67 ms                                                | 3.21 ms: 1.14x faster                                                            |
| unpickle_pure_python    | 228 us                                                 | 201 us: 1.13x faster                                                             |
| coroutines              | 25.5 ms                                                | 22.9 ms: 1.12x faster                                                            |
| scimark_sor             | 118 ms                                                 | 107 ms: 1.11x faster                                                             |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                                            |
| genshi_xml              | 51.8 ms                                                | 47.7 ms: 1.09x faster                                                            |
| json_loads              | 26.5 us                                                | 24.4 us: 1.08x faster                                                            |
| deepcopy_memo           | 37.0 us                                                | 34.4 us: 1.08x faster                                                            |
| xml_etree_parse         | 158 ms                                                 | 148 ms: 1.07x faster                                                             |
| gunicorn                | 1.18 ms                                                | 1.10 ms: 1.07x faster                                                            |
| pickle_pure_python      | 306 us                                                 | 286 us: 1.07x faster                                                             |
| coverage                | 100 ms                                                 | 93.6 ms: 1.07x faster                                                            |
| json                    | 4.94 ms                                                | 4.64 ms: 1.07x faster                                                            |
| logging_silent          | 101 ns                                                 | 96.1 ns: 1.05x faster                                                            |
| fannkuch                | 388 ms                                                 | 371 ms: 1.05x faster                                                             |
| sqlglot_optimize        | 53.1 ms                                                | 50.8 ms: 1.05x faster                                                            |
| xml_etree_iterparse     | 104 ms                                                 | 99.4 ms: 1.04x faster                                                            |
| pprint_pformat          | 1.46 sec                                               | 1.39 sec: 1.04x faster                                                           |
| pidigits                | 198 ms                                                 | 190 ms: 1.04x faster                                                             |
| pycparser               | 1.18 sec                                               | 1.13 sec: 1.04x faster                                                           |
| logging_format          | 6.68 us                                                | 6.41 us: 1.04x faster                                                            |
| richards                | 45.7 ms                                                | 44.0 ms: 1.04x faster                                                            |
| html5lib                | 64.5 ms                                                | 62.1 ms: 1.04x faster                                                            |
| sqlglot_normalize       | 108 ms                                                 | 104 ms: 1.04x faster                                                             |
| raytrace                | 297 ms                                                 | 287 ms: 1.03x faster                                                             |
| bench_thread_pool       | 819 us                                                 | 793 us: 1.03x faster                                                             |
| docutils                | 2.63 sec                                               | 2.55 sec: 1.03x faster                                                           |
| regex_compile           | 138 ms                                                 | 134 ms: 1.03x faster                                                             |
| logging_simple          | 6.03 us                                                | 5.86 us: 1.03x faster                                                            |
| 2to3                    | 259 ms                                                 | 252 ms: 1.03x faster                                                             |
| scimark_fft             | 328 ms                                                 | 319 ms: 1.03x faster                                                             |
| nqueens                 | 83.4 ms                                                | 81.1 ms: 1.03x faster                                                            |
| float                   | 77.2 ms                                                | 75.2 ms: 1.03x faster                                                            |
| sympy_expand            | 475 ms                                                 | 462 ms: 1.03x faster                                                             |
| meteor_contest          | 107 ms                                                 | 104 ms: 1.03x faster                                                             |
| pprint_safe_repr        | 701 ms                                                 | 683 ms: 1.03x faster                                                             |
| go                      | 140 ms                                                 | 137 ms: 1.02x faster                                                             |
| pathlib                 | 18.2 ms                                                | 17.8 ms: 1.02x faster                                                            |
| gc_traversal            | 4.02 ms                                                | 3.93 ms: 1.02x faster                                                            |
| spectral_norm           | 100 ms                                                 | 97.8 ms: 1.02x faster                                                            |
| pyflate                 | 418 ms                                                 | 409 ms: 1.02x faster                                                             |
| deepcopy                | 342 us                                                 | 335 us: 1.02x faster                                                             |
| sympy_integrate         | 21.0 ms                                                | 20.5 ms: 1.02x faster                                                            |
| chaos                   | 69.2 ms                                                | 67.9 ms: 1.02x faster                                                            |
| sympy_str               | 290 ms                                                 | 285 ms: 1.02x faster                                                             |
| hexiom                  | 6.37 ms                                                | 6.27 ms: 1.02x faster                                                            |
| tornado_http            | 96.3 ms                                                | 95.2 ms: 1.01x faster                                                            |
| regex_v8                | 22.0 ms                                                | 21.8 ms: 1.01x faster                                                            |
| telco                   | 6.58 ms                                                | 6.52 ms: 1.01x faster                                                            |
| mako                    | 10.1 ms                                                | 10.0 ms: 1.01x faster                                                            |
| chameleon               | 6.47 ms                                                | 6.42 ms: 1.01x faster                                                            |
| crypto_pyaes            | 74.7 ms                                                | 74.2 ms: 1.01x faster                                                            |
| regex_dna               | 204 ms                                                 | 203 ms: 1.00x faster                                                             |
| deepcopy_reduce         | 2.94 us                                                | 2.96 us: 1.01x slower                                                            |
| mdp                     | 2.62 sec                                               | 2.63 sec: 1.01x slower                                                           |
| create_gc_cycles        | 1.49 ms                                                | 1.50 ms: 1.01x slower                                                            |
| sympy_sum               | 167 ms                                                 | 168 ms: 1.01x slower                                                             |
| sqlglot_transpile       | 1.70 ms                                                | 1.72 ms: 1.01x slower                                                            |
| pickle                  | 10.1 us                                                | 10.2 us: 1.01x slower                                                            |
| unpack_sequence         | 43.1 ns                                                | 43.8 ns: 1.02x slower                                                            |
| scimark_lu              | 110 ms                                                 | 112 ms: 1.02x slower                                                             |
| sqlglot_parse           | 1.40 ms                                                | 1.44 ms: 1.03x slower                                                            |
| xml_etree_process       | 53.9 ms                                                | 55.2 ms: 1.03x slower                                                            |
| nbody                   | 93.1 ms                                                | 95.6 ms: 1.03x slower                                                            |
| django_template         | 32.6 ms                                                | 33.5 ms: 1.03x slower                                                            |
| unpickle_list           | 4.91 us                                                | 5.05 us: 1.03x slower                                                            |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.68 ms: 1.04x slower                                                            |
| sqlite_synth            | 2.52 us                                                | 2.65 us: 1.05x slower                                                            |
| async_tree_memoization  | 627 ms                                                 | 660 ms: 1.05x slower                                                             |
| thrift                  | 756 us                                                 | 796 us: 1.05x slower                                                             |
| python_startup          | 8.52 ms                                                | 9.02 ms: 1.06x slower                                                            |
| comprehensions          | 22.4 us                                                | 23.8 us: 1.06x slower                                                            |
| xml_etree_generate      | 76.2 ms                                                | 81.0 ms: 1.06x slower                                                            |
| python_startup_no_site  | 6.01 ms                                                | 6.54 ms: 1.09x slower                                                            |
| async_generators        | 368 ms                                                 | 413 ms: 1.12x slower                                                             |
| dask                    | 360 ms                                                 | 509 ms: 1.41x slower                                                             |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                                     |

Benchmark hidden because not significant (13): genshi_text, scimark_monte_carlo, sqlalchemy_declarative, pickle_dict, bench_mp_pool, async_tree_none, pickle_list, dulwich_log, sqlalchemy_imperative, async_tree_io, async_tree_cpu_io_mixed, unpickle, djangocms
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 100.00% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.01x
- 99% likely to have a speedup of 1.00x
