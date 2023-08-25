
# Results vs. 3.11.0

- fork: ericsnowcurrently
- ref: per_interpreter_allo
- machine: linux-x86_64
- commit hash: 299527e
- commit date: 2023-04-04
- overall geometric mean: 1.03x faster \*
- HPT reliability: 99.99%
- HPT 99th percentile: 1.00x faster

Benchmarks with tag 'apps':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-linux-x86_64-ericsnowcurrently-per_interpreter_allo-3.12.0a7+-299527e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| 2to3           | 259 ms                                                 | 253 ms: 1.02x faster                                                              |
| docutils       | 2.63 sec                                               | 2.56 sec: 1.03x faster                                                            |
| html5lib       | 64.5 ms                                                | 62.4 ms: 1.03x faster                                                             |
| tornado_http   | 96.3 ms                                                | 91.6 ms: 1.05x faster                                                             |
| Geometric mean | (ref)                                                  | 1.03x faster                                                                      |

Benchmark hidden because not significant (1): chameleon

Benchmarks with tag 'math':
===========================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-linux-x86_64-ericsnowcurrently-per_interpreter_allo-3.12.0a7+-299527e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| nbody          | 93.1 ms                                                | 87.9 ms: 1.06x faster                                                             |
| pidigits       | 198 ms                                                 | 188 ms: 1.05x faster                                                              |
| float          | 77.2 ms                                                | 74.6 ms: 1.03x faster                                                             |
| Geometric mean | (ref)                                                  | 1.05x faster                                                                      |

Benchmarks with tag 'regex':
============================

| Benchmark      | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-linux-x86_64-ericsnowcurrently-per_interpreter_allo-3.12.0a7+-299527e |
|----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| regex_effbot   | 3.99 ms                                                | 3.42 ms: 1.17x faster                                                             |
| regex_compile  | 138 ms                                                 | 135 ms: 1.02x faster                                                              |
| regex_v8       | 22.0 ms                                                | 22.7 ms: 1.03x slower                                                             |
| Geometric mean | (ref)                                                  | 1.04x faster                                                                      |

Benchmark hidden because not significant (1): regex_dna

Benchmarks with tag 'serialize':
================================

| Benchmark            | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-linux-x86_64-ericsnowcurrently-per_interpreter_allo-3.12.0a7+-299527e |
|----------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| json_dumps           | 12.6 ms                                                | 9.75 ms: 1.29x faster                                                             |
| unpickle_pure_python | 228 us                                                 | 205 us: 1.11x faster                                                              |
| json_loads           | 26.5 us                                                | 24.4 us: 1.08x faster                                                             |
| xml_etree_parse      | 158 ms                                                 | 150 ms: 1.06x faster                                                              |
| pickle_pure_python   | 306 us                                                 | 293 us: 1.05x faster                                                              |
| xml_etree_iterparse  | 104 ms                                                 | 100 ms: 1.04x faster                                                              |
| unpickle_list        | 4.91 us                                                | 5.06 us: 1.03x slower                                                             |
| xml_etree_process    | 53.9 ms                                                | 56.6 ms: 1.05x slower                                                             |
| pickle_list          | 4.11 us                                                | 4.36 us: 1.06x slower                                                             |
| pickle_dict          | 31.1 us                                                | 33.3 us: 1.07x slower                                                             |
| pickle               | 10.1 us                                                | 10.8 us: 1.07x slower                                                             |
| xml_etree_generate   | 76.2 ms                                                | 81.7 ms: 1.07x slower                                                             |
| Geometric mean       | (ref)                                                  | 1.02x faster                                                                      |

Benchmark hidden because not significant (1): unpickle

Benchmarks with tag 'startup':
==============================

| Benchmark              | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-linux-x86_64-ericsnowcurrently-per_interpreter_allo-3.12.0a7+-299527e |
|------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| python_startup         | 8.52 ms                                                | 8.85 ms: 1.04x slower                                                             |
| python_startup_no_site | 6.01 ms                                                | 6.53 ms: 1.09x slower                                                             |
| Geometric mean         | (ref)                                                  | 1.06x slower                                                                      |

Benchmarks with tag 'template':
===============================

| Benchmark       | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-linux-x86_64-ericsnowcurrently-per_interpreter_allo-3.12.0a7+-299527e |
|-----------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| genshi_xml      | 51.8 ms                                                | 48.9 ms: 1.06x faster                                                             |
| genshi_text     | 21.6 ms                                                | 21.9 ms: 1.01x slower                                                             |
| mako            | 10.1 ms                                                | 10.3 ms: 1.02x slower                                                             |
| django_template | 32.6 ms                                                | 33.3 ms: 1.02x slower                                                             |
| Geometric mean  | (ref)                                                  | 1.00x faster                                                                      |

All benchmarks:
===============

| Benchmark               | bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509 | bm-20230404-linux-x86_64-ericsnowcurrently-per_interpreter_allo-3.12.0a7+-299527e |
|-------------------------|:------------------------------------------------------:|:---------------------------------------------------------------------------------:|
| generators              | 73.5 ms                                                | 29.2 ms: 2.51x faster                                                             |
| asyncio_tcp             | 922 ms                                                 | 501 ms: 1.84x faster                                                              |
| json_dumps              | 12.6 ms                                                | 9.75 ms: 1.29x faster                                                             |
| mypy2                   | 420 ms                                                 | 336 ms: 1.25x faster                                                              |
| regex_effbot            | 3.99 ms                                                | 3.42 ms: 1.17x faster                                                             |
| deltablue               | 3.67 ms                                                | 3.22 ms: 1.14x faster                                                             |
| unpickle_pure_python    | 228 us                                                 | 205 us: 1.11x faster                                                              |
| coroutines              | 25.5 ms                                                | 23.3 ms: 1.09x faster                                                             |
| aiohttp                 | 1.10 ms                                                | 1.01 ms: 1.09x faster                                                             |
| json_loads              | 26.5 us                                                | 24.4 us: 1.08x faster                                                             |
| gunicorn                | 1.18 ms                                                | 1.09 ms: 1.08x faster                                                             |
| scimark_sparse_mat_mult | 4.50 ms                                                | 4.19 ms: 1.07x faster                                                             |
| pycparser               | 1.18 sec                                               | 1.11 sec: 1.06x faster                                                            |
| nbody                   | 93.1 ms                                                | 87.9 ms: 1.06x faster                                                             |
| genshi_xml              | 51.8 ms                                                | 48.9 ms: 1.06x faster                                                             |
| json                    | 4.94 ms                                                | 4.68 ms: 1.06x faster                                                             |
| xml_etree_parse         | 158 ms                                                 | 150 ms: 1.06x faster                                                              |
| raytrace                | 297 ms                                                 | 281 ms: 1.06x faster                                                              |
| pidigits                | 198 ms                                                 | 188 ms: 1.05x faster                                                              |
| tornado_http            | 96.3 ms                                                | 91.6 ms: 1.05x faster                                                             |
| logging_silent          | 101 ns                                                 | 96.3 ns: 1.05x faster                                                             |
| logging_format          | 6.68 us                                                | 6.37 us: 1.05x faster                                                             |
| logging_simple          | 6.03 us                                                | 5.75 us: 1.05x faster                                                             |
| richards                | 45.7 ms                                                | 43.6 ms: 1.05x faster                                                             |
| deepcopy_memo           | 37.0 us                                                | 35.3 us: 1.05x faster                                                             |
| pickle_pure_python      | 306 us                                                 | 293 us: 1.05x faster                                                              |
| scimark_sor             | 118 ms                                                 | 113 ms: 1.04x faster                                                              |
| xml_etree_iterparse     | 104 ms                                                 | 100 ms: 1.04x faster                                                              |
| hexiom                  | 6.37 ms                                                | 6.16 ms: 1.04x faster                                                             |
| float                   | 77.2 ms                                                | 74.6 ms: 1.03x faster                                                             |
| html5lib                | 64.5 ms                                                | 62.4 ms: 1.03x faster                                                             |
| meteor_contest          | 107 ms                                                 | 103 ms: 1.03x faster                                                              |
| pprint_pformat          | 1.46 sec                                               | 1.41 sec: 1.03x faster                                                            |
| bench_thread_pool       | 819 us                                                 | 797 us: 1.03x faster                                                              |
| scimark_fft             | 328 ms                                                 | 319 ms: 1.03x faster                                                              |
| sqlglot_optimize        | 53.1 ms                                                | 51.7 ms: 1.03x faster                                                             |
| deepcopy                | 342 us                                                 | 333 us: 1.03x faster                                                              |
| docutils                | 2.63 sec                                               | 2.56 sec: 1.03x faster                                                            |
| 2to3                    | 259 ms                                                 | 253 ms: 1.02x faster                                                              |
| mdp                     | 2.62 sec                                               | 2.56 sec: 1.02x faster                                                            |
| scimark_lu              | 110 ms                                                 | 107 ms: 1.02x faster                                                              |
| regex_compile           | 138 ms                                                 | 135 ms: 1.02x faster                                                              |
| nqueens                 | 83.4 ms                                                | 81.7 ms: 1.02x faster                                                             |
| sympy_expand            | 475 ms                                                 | 466 ms: 1.02x faster                                                              |
| coverage                | 100 ms                                                 | 98.3 ms: 1.02x faster                                                             |
| sympy_str               | 290 ms                                                 | 286 ms: 1.01x faster                                                              |
| sqlglot_normalize       | 108 ms                                                 | 106 ms: 1.01x faster                                                              |
| pprint_safe_repr        | 701 ms                                                 | 692 ms: 1.01x faster                                                              |
| sympy_integrate         | 21.0 ms                                                | 20.7 ms: 1.01x faster                                                             |
| spectral_norm           | 100 ms                                                 | 99.0 ms: 1.01x faster                                                             |
| chaos                   | 69.2 ms                                                | 68.6 ms: 1.01x faster                                                             |
| go                      | 140 ms                                                 | 139 ms: 1.01x faster                                                              |
| create_gc_cycles        | 1.49 ms                                                | 1.48 ms: 1.00x faster                                                             |
| fannkuch                | 388 ms                                                 | 389 ms: 1.00x slower                                                              |
| sympy_sum               | 167 ms                                                 | 167 ms: 1.00x slower                                                              |
| crypto_pyaes            | 74.7 ms                                                | 75.2 ms: 1.01x slower                                                             |
| async_tree_cpu_io_mixed | 739 ms                                                 | 747 ms: 1.01x slower                                                              |
| genshi_text             | 21.6 ms                                                | 21.9 ms: 1.01x slower                                                             |
| pathlib                 | 18.2 ms                                                | 18.5 ms: 1.01x slower                                                             |
| scimark_monte_carlo     | 68.1 ms                                                | 69.0 ms: 1.01x slower                                                             |
| pyflate                 | 418 ms                                                 | 426 ms: 1.02x slower                                                              |
| mako                    | 10.1 ms                                                | 10.3 ms: 1.02x slower                                                             |
| deepcopy_reduce         | 2.94 us                                                | 3.00 us: 1.02x slower                                                             |
| django_template         | 32.6 ms                                                | 33.3 ms: 1.02x slower                                                             |
| async_tree_memoization  | 627 ms                                                 | 646 ms: 1.03x slower                                                              |
| unpickle_list           | 4.91 us                                                | 5.06 us: 1.03x slower                                                             |
| thrift                  | 756 us                                                 | 780 us: 1.03x slower                                                              |
| regex_v8                | 22.0 ms                                                | 22.7 ms: 1.03x slower                                                             |
| sqlglot_transpile       | 1.70 ms                                                | 1.76 ms: 1.03x slower                                                             |
| python_startup          | 8.52 ms                                                | 8.85 ms: 1.04x slower                                                             |
| sqlglot_parse           | 1.40 ms                                                | 1.46 ms: 1.04x slower                                                             |
| sqlite_synth            | 2.52 us                                                | 2.64 us: 1.05x slower                                                             |
| unpack_sequence         | 43.1 ns                                                | 45.1 ns: 1.05x slower                                                             |
| xml_etree_process       | 53.9 ms                                                | 56.6 ms: 1.05x slower                                                             |
| pickle_list             | 4.11 us                                                | 4.36 us: 1.06x slower                                                             |
| pickle_dict             | 31.1 us                                                | 33.3 us: 1.07x slower                                                             |
| gc_traversal            | 4.02 ms                                                | 4.31 ms: 1.07x slower                                                             |
| pickle                  | 10.1 us                                                | 10.8 us: 1.07x slower                                                             |
| xml_etree_generate      | 76.2 ms                                                | 81.7 ms: 1.07x slower                                                             |
| comprehensions          | 22.4 us                                                | 24.1 us: 1.08x slower                                                             |
| python_startup_no_site  | 6.01 ms                                                | 6.53 ms: 1.09x slower                                                             |
| async_generators        | 368 ms                                                 | 425 ms: 1.15x slower                                                              |
| dask                    | 360 ms                                                 | 515 ms: 1.43x slower                                                              |
| Geometric mean          | (ref)                                                  | 1.03x faster                                                                      |

Benchmark hidden because not significant (11): sqlalchemy_declarative, djangocms, chameleon, async_tree_none, regex_dna, bench_mp_pool, sqlalchemy_imperative, telco, async_tree_io, dulwich_log, unpickle
Ignored benchmarks (6) of results/bm-20221024-3.11.0-deaf509/bm-20221024-linux-x86_64-python-v3.11.0-3.11.0-deaf509.json: asyncio_tcp_ssl, flaskblogging, pylint, richards_super, tomli_loads, typing_runtime_protocols


# HPT report

- Reliability score: 99.99% likely to be faster
- 90% likely to have a speedup of 1.01x
- 95% likely to have a speedup of 1.00x
- 99% likely to have a speedup of 1.00x
